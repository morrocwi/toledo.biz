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
        self.assertEqual(len(passport["events"]), 1)

        schema = json.loads((ROOT / "packages/schemas/case-passport.schema.json").read_text())
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(validator.iter_errors(passport))
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
