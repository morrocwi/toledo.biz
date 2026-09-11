import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from toledo_runtime import (
    EquationStore,
    InstitutionStore,
    apply_case_event,
    compile_protocol,
    create_case_passport,
    step_case,
)


ROOT = Path(__file__).resolve().parents[1]


def candidate_signature():
    return {
        "status": "CANDIDATE",
        "candidate_signatures": [
            {
                "signature_id": "sig-1",
                "intent": {
                    "value": "IDENTIFY_CAUSE",
                    "provenance": ["AI_INFERENCE", "CITIZEN_VERBATIM"],
                    "confidence": "MEDIUM",
                    "citizen_confirmed": None,
                },
                "object_readout": {
                    "value": "PRODUCTION_SYSTEM",
                    "provenance": ["CITIZEN_VERBATIM"],
                    "confidence": "MEDIUM",
                    "citizen_confirmed": None,
                },
                "observed_difference": ["failure rate increased compared with prior batch"],
                "evidence_need": ["batch comparison", "process trace"],
                "stakes": "MODERATE",
                "irreversibility": "LOW",
                "third_party_exposure": "LOW",
                "authority_need": "UNKNOWN",
                "jurisdiction": "TH",
                "candidate_alternatives": ["input", "process", "environment", "operator"],
                "next_discriminating_action": "compare failure pattern by batch",
                "citizen_endorsement": "NOT_CHECKED",
            }
        ],
        "endorsed_signature_id": None,
        "context_known": ["failure increased in current batch"],
        "context_unknown": ["which process step differs"],
        "barrier_state": {
            "knowledge": "UNKNOWN",
            "skill": "UNKNOWN",
            "language": "ABSENT",
            "tool": "UNKNOWN",
            "resource_time": "UNKNOWN",
            "network": "UNKNOWN",
            "credential": "UNKNOWN",
            "permission": "UNKNOWN",
            "opportunity": "UNKNOWN",
            "unknown": "PRESENT",
        },
        "domain_adapter_required": "HOLD_UNKNOWN",
    }


class RuntimeTests(unittest.TestCase):
    def test_equation_mirror_contains_expected_family(self):
        store = EquationStore()
        entries = store.list()
        self.assertEqual(len(entries), 36)
        handoff = store.get("TCB-X003")
        self.assertIsNotNone(handoff)
        self.assertIn("HANDOFF_VALID", handoff["statement"])

    def test_low_risk_p0_starts_with_observation(self):
        result = compile_protocol({"problem": "Trees decline after heavy rain", "phase": "P0"})
        self.assertEqual(result["next_action"], "OBSERVE")
        self.assertFalse(result["hard_gates"]["escalation_required"])

    def test_hard_risk_escalates(self):
        result = compile_protocol({
            "problem": "A decision with licensed authority requirement",
            "phase": "P0",
            "risk": {"professional_authority_required": True},
        })
        self.assertEqual(result["next_action"], "ESCALATE")
        self.assertTrue(result["hard_gates"]["escalation_required"])

    def test_dependency_hold_does_not_override_hard_escalation(self):
        held = compile_protocol({
            "problem": "Scale decision waits for quality evidence",
            "phase": "P10",
            "dependency_blocked": True,
            "dependency_reasons": ["waiting_for:td-1111111111111111"],
        })
        self.assertEqual(held["next_action"], "HOLD")
        self.assertEqual(held["status"], "HOLD_FOR_DEPENDENCY")

        hard = compile_protocol({
            "problem": "Regulated scale decision with unresolved dependency",
            "phase": "P10",
            "dependency_blocked": True,
            "risk": {"regulatory_required": True},
        })
        self.assertEqual(hard["next_action"], "ESCALATE")
        self.assertEqual(hard["status"], "HOLD_FOR_ESCALATION")

    def test_thailand_phase_routing(self):
        rows = InstitutionStore().route(jurisdiction="TH", phase="P1", limit=10)
        self.assertTrue(rows)
        ids = {r["institution_id"] for r in rows}
        self.assertIn("TH-MHESI-CLINICTECH", ids)

    def test_case_passport_is_created_and_schema_valid(self):
        passport = create_case_passport({"problem": "Trees decline after heavy rain"})
        self.assertEqual(passport["version"], 1)
        self.assertEqual(passport["case_status"], "OPEN")
        self.assertEqual(passport["citizen_problem_verbatim"], "Trees decline after heavy rain")
        self.assertEqual(passport["goal_state"], "PROVISIONAL")
        self.assertEqual(passport["problem_signature"]["status"], "NOT_PROVIDED")
        self.assertFalse(passport["external_actor_used"])
        self.assertEqual(len(passport["events"]), 1)
        self.assertEqual(len(passport["decision_threads"]), 1)
        self.assertEqual(passport["decision_threads"][0]["thread_id"], passport["primary_thread_id"])
        self.assertEqual(passport["current_phase"], passport["decision_threads"][0]["phase"])

        schema = json.loads((ROOT / "packages/schemas/case-passport.schema.json").read_text())
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        self.assertEqual(list(validator.iter_errors(passport)), [])

        thread_schema = json.loads((ROOT / "packages/schemas/decision-thread.schema.json").read_text())
        thread_validator = Draft202012Validator(thread_schema, format_checker=FormatChecker())
        self.assertEqual(list(thread_validator.iter_errors(passport["decision_threads"][0])), [])

    def test_problem_signature_schema_accepts_candidate_with_provenance(self):
        schema = json.loads((ROOT / "packages/schemas/problem-signature.schema.json").read_text())
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        self.assertEqual(list(validator.iter_errors(candidate_signature())), [])

    def test_event_updates_version_without_overwriting_pc(self):
        passport = create_case_passport({"problem": "Water pools in one corner"})
        updated = apply_case_event(passport, {
            "event_type": "OBSERVATION_ADDED",
            "actor": "citizen",
            "payload": {"value": "Pooling appears after heavy rain"},
        })
        self.assertEqual(updated["version"], 2)
        self.assertIn("Pooling appears after heavy rain", updated["observations"])
        self.assertIn("Pooling appears after heavy rain", updated["decision_threads"][0]["observations"])
        self.assertEqual(updated["citizen_problem_verbatim"], passport["citizen_problem_verbatim"])
        self.assertEqual(passport["version"], 1)

    def test_candidate_signature_can_be_endorsed_without_overwriting_pc(self):
        passport = create_case_passport({"problem": "Something changed after the last production batch"})
        updated = apply_case_event(passport, {
            "event_type": "SIGNATURE_CANDIDATES_UPDATED",
            "actor": "ai",
            "payload": {"problem_signature": candidate_signature()},
        })
        self.assertEqual(updated["problem_signature"]["status"], "CANDIDATE")
        self.assertEqual(updated["citizen_problem_verbatim"], passport["citizen_problem_verbatim"])

        endorsed = apply_case_event(updated, {
            "event_type": "SIGNATURE_ENDORSED",
            "actor": "citizen",
            "payload": {"signature_id": "sig-1"},
        })
        self.assertEqual(endorsed["problem_signature"]["status"], "ENDORSED")
        self.assertEqual(endorsed["problem_signature"]["endorsed_signature_id"], "sig-1")
        self.assertEqual(endorsed["citizen_problem_verbatim"], passport["citizen_problem_verbatim"])

    def test_practice_context_does_not_select_a_bespoke_core_protocol(self):
        mushroom = compile_protocol({
            "problem": "Output fails intermittently",
            "phase": "P0",
            "practice_context": {"occupation": "mushroom grower"},
        })
        mechanic = compile_protocol({
            "problem": "Output fails intermittently",
            "phase": "P0",
            "practice_context": {"occupation": "mechanic"},
        })
        self.assertEqual(mushroom["next_action"], mechanic["next_action"])
        self.assertEqual(mushroom["hard_gates"], mechanic["hard_gates"])

    def test_local_citizen_outcome_can_close_without_fake_external_return(self):
        passport = create_case_passport({
            "problem": "A reversible local process gives inconsistent results",
            "goal": "Stabilize the process",
        })
        closed = apply_case_event(passport, {
            "event_type": "OUTCOME_UPDATED",
            "actor": "citizen",
            "payload": {"outcome_state": "improved", "result": "The local change stabilized the next run"},
        })
        self.assertFalse(closed["external_actor_used"])
        self.assertEqual(closed["latest_return_gate"], "NOT_APPLICABLE")
        self.assertEqual(closed["decision_threads"][0]["status"], "CLOSED")
        self.assertEqual(closed["case_status"], "CLOSED")
        result = step_case({"passport": closed})
        self.assertEqual(result["protocol"]["next_action"], "STOP")

    def test_hard_risk_local_outcome_does_not_close_without_escalation(self):
        passport = create_case_passport({
            "problem": "A high-risk decision seems improved after a local attempt",
            "risk": {"professional_authority_required": True},
        })
        updated = apply_case_event(passport, {
            "event_type": "OUTCOME_UPDATED",
            "actor": "citizen",
            "payload": {"outcome_state": "improved", "result": "The immediate symptom appears better"},
        })
        self.assertFalse(updated["external_actor_used"])
        self.assertEqual(updated["risk_state"], "HARD_ESCALATION")
        self.assertEqual(updated["case_status"], "HOLD")
        result = step_case({"passport": updated})
        self.assertEqual(result["protocol"]["next_action"], "ESCALATE")
        self.assertEqual(result["protocol"]["status"], "HOLD_FOR_ESCALATION")

    def test_external_contribution_still_requires_return_gate(self):
        passport = create_case_passport({"problem": "Need an external specialist check"})
        routed = apply_case_event(passport, {
            "event_type": "INSTITUTION_SELECTED",
            "actor": "steward",
            "payload": {"institution_id": "example-lab"},
        })
        self.assertTrue(routed["external_actor_used"])
        outcome = apply_case_event(routed, {
            "event_type": "OUTCOME_UPDATED",
            "actor": "citizen",
            "payload": {"outcome_state": "improved"},
        })
        self.assertEqual(outcome["case_status"], "HOLD")
        self.assertEqual(outcome["latest_return_gate"], "NOT_APPLICABLE")

    def test_closed_loop_return_then_outcome_closes_case(self):
        passport = create_case_passport({"problem": "Water pools in one corner", "goal": "Keep trees healthy"})
        returned = apply_case_event(passport, {
            "event_type": "RETURN_RECEIVED",
            "actor": "expert",
            "payload": {
                "return_object": {
                    "case_id": passport["case_id"],
                    "source_actor": "expert",
                    "source_institution": "example-lab",
                    "plain_language_result": "The low area remains waterlogged longer than the comparison area.",
                    "what_is_known": ["water persists longer in the low area"],
                    "what_is_unknown": ["root pathogen status"],
                    "limits": ["single-site observation"],
                    "recommended_next_action": "Improve drainage cautiously and continue observation.",
                    "unsafe_actions_to_avoid": [],
                    "data_returned_refs": [],
                    "rights_state": "no new rights claim",
                    "followup_trigger": "symptoms worsen",
                    "citizen_correction_possible": True,
                    "return_gate_state": "PASS"
                }
            },
        })
        self.assertTrue(returned["external_actor_used"])
        self.assertEqual(returned["latest_return_gate"], "PASS")
        closed = apply_case_event(returned, {
            "event_type": "OUTCOME_UPDATED",
            "actor": "citizen",
            "payload": {"outcome_state": "improved", "result": "Pooling reduced and trees stabilized"},
        })
        self.assertEqual(closed["case_status"], "CLOSED")
        result = step_case({"passport": closed})
        self.assertTrue(result["closed"])
        self.assertEqual(result["protocol"]["next_action"], "STOP")
        self.assertEqual(result["protocol"]["status"], "CLOSED")

    def test_route_failure_preserves_case_and_recompiles(self):
        passport = create_case_passport({
            "problem": "Need licensed review",
            "risk": {"professional_authority_required": True},
        })
        failed = apply_case_event(passport, {
            "event_type": "ROUTE_FAILED",
            "actor": "steward",
            "payload": {"institution_id": "X", "reason": "unavailable", "fallback_route": "alternate provider"},
        })
        result = step_case({"passport": failed})
        self.assertEqual(result["case_id"], passport["case_id"])
        self.assertIn("X: unavailable", result["passport"]["failed_routes"])
        self.assertEqual(result["protocol"]["next_action"], "ESCALATE")

    def test_cosmetics_case_uses_concurrent_decision_threads_without_new_domain_protocol(self):
        quality = "td-1111111111111111"
        regulatory = "td-2222222222222222"
        scale = "td-3333333333333333"
        case = create_case_passport({
            "problem": (
                "Our OEM serum has irritation complaints and some bottles darken after opening; "
                "we are deciding whether to order a much larger second lot and run marketing claims."
            ),
            "goal": "Protect customers and make a justified next production decision",
            "practice_context": {"industry": "cosmetics", "product": "topical serum", "manufacturing": "OEM"},
            "primary_thread_id": quality,
            "decision_threads": [
                {
                    "thread_id": quality,
                    "decision": "identify the cause and significance of the batch quality signals",
                    "phase": "P1",
                    "unknowns": ["cause of irritation reports", "cause of post-opening color change"],
                    "risk_profile": {"third_party_exposure": 0.4}
                },
                {
                    "thread_id": regulatory,
                    "decision": "determine whether the intended market claim is regulatorily usable",
                    "phase": "P3",
                    "risk_profile": {"regulatory_required": True}
                },
                {
                    "thread_id": scale,
                    "decision": "decide whether to commit to the larger second production lot",
                    "phase": "P10",
                    "depends_on": [quality, regulatory]
                }
            ]
        })

        result = step_case({"passport": case})
        by_id = {x["thread_id"]: x for x in result["thread_protocols"]}
        self.assertEqual(len(by_id), 3)
        self.assertEqual(result["primary_thread_id"], quality)
        self.assertEqual(by_id[quality]["next_action"], "MEASURE")
        self.assertEqual(by_id[regulatory]["next_action"], "ESCALATE")
        self.assertEqual(by_id[scale]["next_action"], "HOLD")
        self.assertEqual(by_id[scale]["status"], "HOLD_FOR_DEPENDENCY")
        self.assertCountEqual(by_id[scale]["blocking_threads"], [quality, regulatory])
        self.assertEqual(case["citizen_problem_verbatim"], result["passport"]["citizen_problem_verbatim"])

        quality_done = apply_case_event(case, {
            "event_type": "OUTCOME_UPDATED",
            "actor": "citizen",
            "payload": {
                "thread_id": quality,
                "outcome_state": "improved",
                "result": "A reversible batch-control change reduced the quality signal in the next comparison run"
            }
        })
        self.assertEqual(
            next(x for x in quality_done["decision_threads"] if x["thread_id"] == quality)["status"],
            "CLOSED",
        )

        routed = apply_case_event(quality_done, {
            "event_type": "INSTITUTION_SELECTED",
            "actor": "steward",
            "payload": {"thread_id": regulatory, "institution_id": "example-regulatory-review"}
        })
        returned = apply_case_event(routed, {
            "event_type": "RETURN_RECEIVED",
            "actor": "external-reviewer",
            "payload": {
                "thread_id": regulatory,
                "return_object": {
                    "case_id": case["case_id"],
                    "source_actor": "external-reviewer",
                    "source_institution": "example-regulatory-review",
                    "plain_language_result": "The proposed claim needs revision before use.",
                    "what_is_known": ["the proposed wording is not ready for use"],
                    "what_is_unknown": [],
                    "limits": ["review limited to the submitted wording"],
                    "recommended_next_action": "Revise the wording and retain the review record.",
                    "unsafe_actions_to_avoid": ["publish the unreviewed wording"],
                    "data_returned_refs": ["review-record"],
                    "rights_state": "no new rights claim",
                    "followup_trigger": "claim wording changes",
                    "citizen_correction_possible": True,
                    "return_gate_state": "PASS"
                }
            }
        })
        regulatory_done = apply_case_event(returned, {
            "event_type": "OUTCOME_UPDATED",
            "actor": "citizen",
            "payload": {"thread_id": regulatory, "outcome_state": "safely_held"}
        })

        after_dependencies = step_case({"passport": regulatory_done})
        by_id = {x["thread_id"]: x for x in after_dependencies["thread_protocols"]}
        self.assertEqual(by_id[scale]["blocking_threads"], [])
        self.assertEqual(by_id[scale]["next_action"], "SCALE_CHECK")

        scale_done = apply_case_event(regulatory_done, {
            "event_type": "OUTCOME_UPDATED",
            "actor": "citizen",
            "payload": {
                "thread_id": scale,
                "outcome_state": "safely_held",
                "result": "Large lot commitment paused pending the next evidence cycle"
            }
        })
        closed = apply_case_event(scale_done, {
            "event_type": "OUTCOME_UPDATED",
            "actor": "citizen",
            "payload": {"outcome_state": "safely_held", "result": "All required decisions are in a safe state"}
        })
        self.assertEqual(closed["case_status"], "CLOSED")
        final = step_case({"passport": closed})
        self.assertTrue(final["closed"])
        self.assertTrue(all(x["next_action"] == "STOP" for x in final["thread_protocols"]))


if __name__ == "__main__":
    unittest.main()
