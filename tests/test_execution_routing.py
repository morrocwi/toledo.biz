import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from toledo_runtime import compile_protocol, resolve_execution_route


ROOT = Path(__file__).resolve().parents[1]


def _signature(**overrides):
    candidate = {
        "signature_id": "sig-1",
        "intent": {
            "value": "IDENTIFY_CAUSE",
            "provenance": ["AI_INFERENCE"],
            "confidence": "MEDIUM",
            "citizen_confirmed": None,
        },
        "object_readout": {
            "value": "PHYSICAL_SYSTEM",
            "provenance": ["CITIZEN_VERBATIM"],
            "confidence": "MEDIUM",
            "citizen_confirmed": None,
        },
        "observed_difference": [],
        "evidence_need": [],
        "stakes": "LOW",
        "irreversibility": "LOW",
        "third_party_exposure": "LOW",
        "authority_need": "NONE",
        "jurisdiction": "TH",
        "candidate_alternatives": [],
        "next_discriminating_action": None,
        "citizen_endorsement": "PASS",
    }
    candidate.update(overrides)
    return {
        "status": "ENDORSED",
        "candidate_signatures": [candidate],
        "endorsed_signature_id": "sig-1",
        "context_known": [],
        "context_unknown": [],
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
        "domain_adapter_required": "NO",
    }


def _candidate_signature(**overrides):
    signature = _signature(**overrides)
    signature["status"] = "CANDIDATE"
    signature["endorsed_signature_id"] = None
    signature["candidate_signatures"][0]["citizen_endorsement"] = "NOT_CHECKED"
    return signature


def _classes(result):
    return {x["class"]: x for x in result["execution_requirements"]}


class ExecutionRoutingTests(unittest.TestCase):
    def test_ai_is_translator_not_expert_or_authority(self):
        result = compile_protocol({"problem": "Customers describe two different failure patterns", "phase": "P0"})
        role = result["execution_routing"]["ai_role"]
        self.assertEqual(role["class"], "MEDIATOR_TRANSLATOR")
        self.assertFalse(role["is_expert_class"])
        self.assertFalse(role["confers_professional_authority"])
        self.assertFalse(role["counts_as_independent_validation"])

    def test_field_and_interaction_experts_are_distinct_classes(self):
        field = compile_protocol({
            "problem": "Inspect the machine on site because the production operator sees an intermittent failure",
            "phase": "P1",
            "problem_signature": _signature(evidence_need=["field inspection", "machine measurement"]),
            "evidence": {"unknowns": ["physical failure cause"]},
        })
        self.assertIn("FIELD_EXPERT", _classes(field))
        self.assertIn("MEASUREMENT_TOOL", _classes(field))

        interaction = compile_protocol({
            "problem": "Interpret conflicting customer requirements and negotiate the decision",
            "phase": "P1",
            "problem_signature": _signature(evidence_need=["stakeholder interpretation"]),
        })
        self.assertIn("INTERACTION_EXPERT", _classes(interaction))

    def test_knowledge_like_material_is_not_human_expertise(self):
        result = compile_protocol({
            "problem": "Compare prior records and standards before deciding",
            "phase": "P4",
            "problem_signature": _signature(evidence_need=["prior record", "standard comparison"]),
        })
        self.assertIn("KNOWLEDGE_LIKE_SOURCE", _classes(result))
        k = result["execution_routing"]["knowledge_like"]
        self.assertEqual(k["class"], "K*_0")
        self.assertFalse(k["is_human_expert"])
        self.assertFalse(k["is_truth_certificate"])

    def test_external_selection_alone_does_not_promote_kstar_i(self):
        plan = resolve_execution_route({
            "problem": "An external expert was selected but has not returned a usable result",
            "phase": "P3",
            "external_actor_used": True,
            "latest_return_gate": "NOT_APPLICABLE",
        })
        self.assertEqual(plan["knowledge_like"]["class"], "K*_0")

    def test_passing_external_return_marks_escalated_knowledge_like_without_truth_claim(self):
        plan = resolve_execution_route({
            "problem": "An external expert has returned a usable provisional interpretation",
            "phase": "P3",
            "external_actor_used": True,
            "latest_return_gate": "PASS",
        })
        self.assertEqual(plan["knowledge_like"]["class"], "K*_I")
        self.assertEqual(plan["knowledge_like"]["status"], "PROVISIONAL")

    def test_safe_market_first_route_can_be_candidate_before_later_phases(self):
        result = compile_protocol({
            "problem": "I have a reversible sample offer and want to learn whether customers will pay",
            "goal": "run a small customer market pilot",
            "phase": "P1",
            "problem_signature": _signature(
                intent={
                    "value": "TEST_DEMAND",
                    "provenance": ["CITIZEN_VERBATIM"],
                    "confidence": "HIGH",
                    "citizen_confirmed": True,
                },
                evidence_need=["customer transaction"],
                irreversibility="LOW",
                third_party_exposure="LOW",
                authority_need="NONE",
            ),
        })
        routing = result["execution_routing"]
        self.assertEqual(routing["phase_semantics"], "ROUTING_CONTEXT_NOT_MANDATORY_SEQUENCE")
        self.assertEqual(routing["route_mode"], "PARALLEL_OR_FORWARD_EXPERIMENT")
        self.assertTrue(routing["forward_experiment"]["allowed"])
        self.assertTrue(routing["forward_experiment"]["market_test_candidate"])
        self.assertIn("BOUNDED_MARKET_TEST", _classes(result))

    def test_market_language_alone_does_not_authorize_market_first(self):
        result = compile_protocol({
            "problem": "I want to launch this product to customers",
            "goal": "enter the market",
            "phase": "P1",
        })
        routing = result["execution_routing"]
        self.assertFalse(routing["forward_experiment"]["market_test_candidate"])
        self.assertNotIn("BOUNDED_MARKET_TEST", _classes(result))
        self.assertNotEqual(routing["route_mode"], "PARALLEL_OR_FORWARD_EXPERIMENT")

    def test_candidate_authority_need_is_not_promoted_to_required_fact(self):
        result = compile_protocol({
            "problem": "A candidate interpretation says a market claim may require regulator review",
            "goal": "run a customer market pilot",
            "phase": "P1",
            "problem_signature": _candidate_signature(
                evidence_need=["regulatory claim review"],
                authority_need="REGULATOR",
            ),
        })
        routing = result["execution_routing"]
        self.assertEqual(routing["signature_basis"], "CANDIDATE")
        self.assertEqual(routing["route_mode"], "AUTHORITY_UNRESOLVED")
        self.assertFalse(routing["forward_experiment"]["allowed"])
        self.assertEqual(_classes(result)["REGULATORY_AUTHORITY"]["requiredness"], "CANDIDATE")

    def test_hard_authority_gate_blocks_forward_market_experiment(self):
        result = compile_protocol({
            "problem": "Launch a regulated public claim to customers",
            "goal": "enter the market",
            "phase": "P1",
            "risk": {"regulatory_required": True},
            "problem_signature": _signature(
                evidence_need=["regulatory claim review"],
                authority_need="REGULATOR",
            ),
        })
        routing = result["execution_routing"]
        self.assertEqual(routing["route_mode"], "EXTERNAL_REQUIRED")
        self.assertFalse(routing["forward_experiment"]["allowed"])
        classes = _classes(result)
        self.assertEqual(classes["REGULATORY_AUTHORITY"]["requiredness"], "REQUIRED")
        self.assertEqual(classes["HARD_GATE_EXTERNAL_ROUTE"]["requiredness"], "REQUIRED")

    def test_closed_case_does_not_emit_forward_experiment(self):
        result = compile_protocol({
            "problem": "A resolved reversible market question",
            "goal": "customer pilot",
            "phase": "P1",
            "case_status": "CLOSED",
            "problem_signature": _signature(),
        })
        self.assertEqual(result["next_action"], "STOP")
        self.assertEqual(result["execution_routing"]["route_mode"], "CLOSED")
        self.assertFalse(result["execution_routing"]["forward_experiment"]["allowed"])

    def test_occupation_does_not_change_execution_matrix_for_same_case_state(self):
        base = {
            "problem": "The physical process fails intermittently and needs a field inspection",
            "phase": "P1",
            "problem_signature": _signature(evidence_need=["field inspection"]),
            "evidence": {"unknowns": ["cause"]},
        }
        mushroom = compile_protocol({**base, "practice_context": {"occupation": "mushroom grower"}})
        mechanic = compile_protocol({**base, "practice_context": {"occupation": "mechanic"}})
        self.assertEqual(
            [x["class"] for x in mushroom["execution_requirements"]],
            [x["class"] for x in mechanic["execution_requirements"]],
        )

    def test_execution_routing_schema_accepts_runtime_output(self):
        schema = json.loads((ROOT / "packages/schemas/execution-routing.schema.json").read_text())
        result = compile_protocol({
            "problem": "Measure a machine and inspect it on site",
            "phase": "P1",
            "problem_signature": _signature(evidence_need=["machine measurement", "field inspection"]),
            "evidence": {"unknowns": ["cause"]},
        })
        validator = Draft202012Validator(schema)
        self.assertEqual(list(validator.iter_errors(result["execution_routing"])), [])


if __name__ == "__main__":
    unittest.main()
