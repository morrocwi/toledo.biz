import unittest

from toledo_runtime import EquationStore, InstitutionStore, compile_protocol


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


if __name__ == "__main__":
    unittest.main()
