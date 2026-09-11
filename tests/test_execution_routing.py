import json
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


def _classes(result):
    return {x["class"]: x for x in result["execution_requirements"]}


def test_ai_is_translator_not_expert_or_authority():
    result = compile_protocol({"problem": "Customers describe two different failure patterns", "phase": "P0"})
    role = result["execution_routing"]["ai_role"]
    assert role["class"] == "MEDIATOR_TRANSLATOR"
    assert role["is_expert_class"] is False
    assert role["confers_professional_authority"] is False
    assert role["counts_as_independent_validation"] is False


def test_field_and_interaction_experts_are_distinct_classes():
    field = compile_protocol({
        "problem": "Inspect the machine on site because the production operator sees an intermittent failure",
        "phase": "P1",
        "problem_signature": _signature(evidence_need=["field inspection", "machine measurement"]),
        "evidence": {"unknowns": ["physical failure cause"]},
    })
    assert "FIELD_EXPERT" in _classes(field)
    assert "MEASUREMENT_TOOL" in _classes(field)

    interaction = compile_protocol({
        "problem": "Interpret conflicting customer requirements and negotiate the decision",
        "phase": "P1",
        "problem_signature": _signature(evidence_need=["stakeholder interpretation"]),
    })
    assert "INTERACTION_EXPERT" in _classes(interaction)


def test_knowledge_like_material_is_not_human_expertise():
    result = compile_protocol({
        "problem": "Compare prior records and standards before deciding",
        "phase": "P4",
        "problem_signature": _signature(evidence_need=["prior record", "standard comparison"]),
    })
    assert "KNOWLEDGE_LIKE_SOURCE" in _classes(result)
    k = result["execution_routing"]["knowledge_like"]
    assert k["class"] == "K*_0"
    assert k["is_human_expert"] is False
    assert k["is_truth_certificate"] is False


def test_external_contribution_marks_escalated_knowledge_like_without_truth_claim():
    plan = resolve_execution_route({
        "problem": "An external expert has returned a provisional interpretation",
        "phase": "P3",
        "external_actor_used": True,
    })
    assert plan["knowledge_like"]["class"] == "K*_I"
    assert plan["knowledge_like"]["status"] == "PROVISIONAL"


def test_safe_market_first_route_can_be_candidate_before_later_phases():
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
    assert routing["phase_semantics"] == "ROUTING_CONTEXT_NOT_MANDATORY_SEQUENCE"
    assert routing["route_mode"] == "PARALLEL_OR_FORWARD_EXPERIMENT"
    assert routing["forward_experiment"]["allowed"] is True
    assert routing["forward_experiment"]["market_test_candidate"] is True
    assert "BOUNDED_MARKET_TEST" in _classes(result)


def test_hard_authority_gate_blocks_forward_market_experiment():
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
    assert routing["route_mode"] == "EXTERNAL_REQUIRED"
    assert routing["forward_experiment"]["allowed"] is False
    classes = _classes(result)
    assert classes["REGULATORY_AUTHORITY"]["requiredness"] == "REQUIRED"
    assert classes["HARD_GATE_EXTERNAL_ROUTE"]["requiredness"] == "REQUIRED"


def test_occupation_does_not_change_execution_matrix_for_same_case_state():
    base = {
        "problem": "The physical process fails intermittently and needs a field inspection",
        "phase": "P1",
        "problem_signature": _signature(evidence_need=["field inspection"]),
        "evidence": {"unknowns": ["cause"]},
    }
    mushroom = compile_protocol({**base, "practice_context": {"occupation": "mushroom grower"}})
    mechanic = compile_protocol({**base, "practice_context": {"occupation": "mechanic"}})
    assert [x["class"] for x in mushroom["execution_requirements"]] == [
        x["class"] for x in mechanic["execution_requirements"]
    ]


def test_execution_routing_schema_accepts_runtime_output():
    schema = json.loads((ROOT / "packages/schemas/execution-routing.schema.json").read_text())
    result = compile_protocol({
        "problem": "Measure a machine and inspect it on site",
        "phase": "P1",
        "problem_signature": _signature(evidence_need=["machine measurement", "field inspection"]),
        "evidence": {"unknowns": ["cause"]},
    })
    validator = Draft202012Validator(schema)
    assert list(validator.iter_errors(result["execution_routing"])) == []
