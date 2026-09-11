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

        schema = json.loads((ROOT / "packages/schemas/case-passport.schema.json").read_text())
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(validator.iter_errors(passport))
        self.assertEqual(errors, [])

    def test_problem_signature_schema_accepts_candidate_with_provenance(self):
        schema = json.loads((ROOT / "packages/schemas/problem-signature.schema.json").read_text())
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(validator.iter_errors(candidate_signature()))
        self.assertEqual(errors, [])

    def test_event_updates_version_without_overwriting_pc(self):
        passport = create_case_passport({"problem": "Water pools in one corner"})
        updated = apply_case_event(passport, {
            "event_type": "OBSERVATION_ADDED",
            "actor": "citizen",
            "payload": {"value": "Pooling appears after heavy rain"},
        })
        self.assertEqual(updated["version"], 2)
        self.assertIn("Pooling appears after heavy rain", updated["observations"])
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
        self.assertEqual(closed["case_status"], "CLOSED")
        result = step_case({"passport": closed})
        self.assertEqual(result["protocol"]["next_action"], "STOP")

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


if __name__ == "__main__":
    unittest.main()
