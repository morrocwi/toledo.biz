from __future__ import annotations

from typing import Any


EXPERT_CLASSES = ("INTERACTION_EXPERT", "FIELD_EXPERT")
AUTHORITY_OVERLAYS = (
    "LICENSED_PROFESSIONAL",
    "LAB_INFRASTRUCTURE",
    "REGULATORY_AUTHORITY",
)


def _text(value: Any) -> str:
    return str(value or "").strip()


def _add_requirement(
    items: list[dict[str, Any]],
    cls: str,
    *,
    requiredness: str,
    reason: str,
    basis: str,
) -> None:
    for item in items:
        if item["class"] == cls:
            if requiredness == "REQUIRED":
                item["requiredness"] = "REQUIRED"
            if reason not in item["reasons"]:
                item["reasons"].append(reason)
            if basis not in item["basis"]:
                item["basis"].append(basis)
            return
    items.append(
        {
            "class": cls,
            "requiredness": requiredness,
            "reasons": [reason],
            "basis": [basis],
        }
    )


def _working_signature(problem_signature: dict[str, Any]) -> tuple[dict[str, Any], str]:
    candidates = problem_signature.get("candidate_signatures") or []
    endorsed_id = _text(problem_signature.get("endorsed_signature_id"))
    if endorsed_id:
        match = next((x for x in candidates if _text(x.get("signature_id")) == endorsed_id), None)
        if isinstance(match, dict):
            return match, "ENDORSED"
    if len(candidates) == 1 and isinstance(candidates[0], dict):
        return candidates[0], "CANDIDATE"
    return {}, _text(problem_signature.get("status")).upper() or "NOT_PROVIDED"


def _contains_any(text: str, words: tuple[str, ...]) -> bool:
    return any(word in text for word in words)


def resolve_execution_route(
    case: dict[str, Any],
    *,
    hard_escalation: bool = False,
    hard_reasons: list[str] | None = None,
) -> dict[str, Any]:
    """Translate case state into flexible execution requirements.

    This is an implementation routing aid, not a new Toledo equation and not a
    mandatory P0->P11 sequence. Phase is context. Hard safety/authority gates
    remain authoritative. AI is represented as mediator/translator, not as an
    expert class or independent validator.
    """

    phase = _text(case.get("phase") or "P0").upper()
    case_status = _text(case.get("case_status") or "OPEN").upper()
    problem_signature = case.get("problem_signature") or {}
    signature, signature_basis = _working_signature(problem_signature)
    signature_endorsed = signature_basis == "ENDORSED"
    signature_candidate = signature_basis == "CANDIDATE"
    barrier_state = problem_signature.get("barrier_state") or {}
    evidence_need = [str(x) for x in signature.get("evidence_need", [])]
    unknowns = [str(x) for x in (case.get("evidence") or {}).get("unknowns", [])]
    observations = [str(x) for x in (case.get("evidence") or {}).get("observations", [])]
    authority_need = _text(signature.get("authority_need")).upper() or "UNKNOWN"
    requested_capability = _text(case.get("requested_capability"))
    goal = _text(case.get("goal"))
    problem = _text(case.get("problem"))

    corpus = " ".join(
        [problem, goal, requested_capability, *evidence_need, *unknowns]
    ).lower()

    requirements: list[dict[str, Any]] = []

    # Knowledge-like material is an input/readout class, not a human expert and
    # not truth merely because AI organized it.
    if phase in {"P0", "P1", "P4", "P6", "P7", "P11"} or _contains_any(
        corpus,
        ("document", "record", "literature", "prior art", "evidence", "standard", "rule", "compare"),
    ):
        _add_requirement(
            requirements,
            "KNOWLEDGE_LIKE_SOURCE",
            requiredness="CANDIDATE",
            reason="decision may benefit from records, prior knowledge, or a structured provisional readout",
            basis="problem/evidence/phase context",
        )

    if _contains_any(
        corpus,
        ("measure", "measurement", "sensor", "test", "sample", "assay", "calibrate", "instrument"),
    ) or barrier_state.get("tool") == "PRESENT":
        _add_requirement(
            requirements,
            "MEASUREMENT_TOOL",
            requiredness="CANDIDATE",
            reason="a world-side measurement can reduce uncertainty that explanation alone cannot",
            basis="evidence need or tool barrier",
        )

    field_signal = _contains_any(
        corpus,
        (
            "inspect",
            "field",
            "site",
            "machine",
            "process",
            "operator",
            "farm",
            "production",
            "physical",
            "installation",
            "worksite",
            "batch",
        ),
    )
    interaction_signal = _contains_any(
        corpus,
        (
            "interpret",
            "explain",
            "compare",
            "decision",
            "stakeholder",
            "customer",
            "negotiate",
            "requirements",
            "strategy",
            "claim",
            "meaning",
            "coordination",
        ),
    )

    if field_signal:
        _add_requirement(
            requirements,
            "FIELD_EXPERT",
            requiredness="CANDIDATE",
            reason="situated/tacit judgment or direct contact with the real operating context may matter",
            basis="field/context signal",
        )
    if interaction_signal:
        _add_requirement(
            requirements,
            "INTERACTION_EXPERT",
            requiredness="CANDIDATE",
            reason="the decision may benefit from expert elicitation, interpretation, dialogue, or stakeholder alignment",
            basis="interaction/interpretation signal",
        )

    # A candidate signature may suggest an expert route, but it does not promote
    # that route to a required fact until endorsement/evidence or a hard gate does.
    if authority_need == "EXPERT":
        expert_requiredness = "REQUIRED" if signature_endorsed else "CANDIDATE"
        if field_signal and not interaction_signal:
            _add_requirement(
                requirements,
                "FIELD_EXPERT",
                requiredness=expert_requiredness,
                reason="working signature points to expert input and the unresolved context is primarily situated/field-side",
                basis=f"authority_need=EXPERT ({signature_basis})",
            )
        elif interaction_signal and not field_signal:
            _add_requirement(
                requirements,
                "INTERACTION_EXPERT",
                requiredness=expert_requiredness,
                reason="working signature points to expert input and the unresolved context is primarily interpretive/interactive",
                basis=f"authority_need=EXPERT ({signature_basis})",
            )
        else:
            _add_requirement(
                requirements,
                "INTERACTION_EXPERT",
                requiredness="CANDIDATE",
                reason="expert input is indicated but the expert mode is not yet resolved",
                basis=f"authority_need=EXPERT ({signature_basis})",
            )
            _add_requirement(
                requirements,
                "FIELD_EXPERT",
                requiredness="CANDIDATE",
                reason="expert input is indicated but the expert mode is not yet resolved",
                basis=f"authority_need=EXPERT ({signature_basis})",
            )

    authority_map = {
        "LICENSED_PROFESSIONAL": (
            "LICENSED_PROFESSIONAL",
            "licensed professional authority may be material",
        ),
        "LAB": (
            "LAB_INFRASTRUCTURE",
            "laboratory evidence may be material",
        ),
        "REGULATOR": (
            "REGULATORY_AUTHORITY",
            "formal regulatory authority may be material",
        ),
    }
    if authority_need in authority_map:
        cls, reason = authority_map[authority_need]
        requiredness = "REQUIRED" if signature_endorsed else "CANDIDATE"
        _add_requirement(
            requirements,
            cls,
            requiredness=requiredness,
            reason=(
                reason.replace("may be", "is")
                if signature_endorsed
                else f"candidate signature indicates {reason}; confirmation is still required"
            ),
            basis=f"authority_need ({signature_basis})",
        )

    if _contains_any(corpus, ("lab", "laboratory", "assay", "sample analysis")):
        _add_requirement(
            requirements,
            "LAB_INFRASTRUCTURE",
            requiredness="CANDIDATE",
            reason="laboratory infrastructure may be the minimum useful world-side evidence source",
            basis="evidence need",
        )

    if _contains_any(corpus, ("document", "certificate", "contract", "record", "license", "standard")):
        _add_requirement(
            requirements,
            "ORIGINAL_DOCUMENT",
            requiredness="CANDIDATE",
            reason="an original or authoritative record may be more probative than another interpretation",
            basis="evidence need",
        )

    if barrier_state.get("credential") == "PRESENT" or barrier_state.get("permission") == "PRESENT":
        _add_requirement(
            requirements,
            "AUTHORITY_OR_PERMISSION_PATH",
            requiredness="REQUIRED",
            reason="credential/permission barrier cannot be solved by explanation alone",
            basis="barrier state",
        )

    market_signal = phase in {"P7", "P8", "P9", "P10", "P11"} or _contains_any(
        corpus,
        ("market", "customer", "sell", "sale", "launch", "pilot", "order", "transaction", "buyer"),
    )

    irreversibility = _text(signature.get("irreversibility")).upper()
    third_party = _text(signature.get("third_party_exposure")).upper()
    explicit_permission_block = barrier_state.get("permission") == "PRESENT"
    explicit_credential_block = barrier_state.get("credential") == "PRESENT"
    dependency_blocked = bool(case.get("dependency_blocked"))
    return_gate = _text(case.get("latest_return_gate")).upper()
    unresolved_authority_candidate = (
        signature_candidate
        and authority_need in {"LICENSED_PROFESSIONAL", "LAB", "REGULATOR"}
    )
    endorsed_authority_block = (
        signature_endorsed
        and authority_need in {"LICENSED_PROFESSIONAL", "LAB", "REGULATOR"}
    )

    forward_allowed = (
        case_status != "CLOSED"
        and not hard_escalation
        and not endorsed_authority_block
        and not unresolved_authority_candidate
        and not explicit_permission_block
        and not explicit_credential_block
        and not dependency_blocked
        and return_gate not in {"FAIL", "HOLD_UNKNOWN"}
        and irreversibility not in {"HIGH"}
        and third_party not in {"HIGH"}
    )

    # Market-facing action has stronger requirements than a generic world test.
    # It must be positively grounded as bounded/reversible rather than inferred
    # safe merely because risk/authority fields are missing.
    market_forward_allowed = (
        forward_allowed
        and market_signal
        and signature_endorsed
        and authority_need == "NONE"
        and irreversibility == "LOW"
        and third_party == "LOW"
    )

    if forward_allowed:
        _add_requirement(
            requirements,
            "WORLD_TEST",
            requiredness="CANDIDATE",
            reason="a bounded reversible action can generate real-world information without waiting for unnecessary escalation",
            basis="no blocking hard gate",
        )
        if market_forward_allowed:
            _add_requirement(
                requirements,
                "BOUNDED_MARKET_TEST",
                requiredness="CANDIDATE",
                reason="market/world contact can be used as evidence because boundedness, reversibility, low third-party exposure, and absence of authority need are positively established",
                basis="endorsed low-risk market state",
            )

    if hard_escalation:
        # Preserve the upstream hard-gate decision without inventing a new
        # expert category. The precise actor remains a routing decision.
        _add_requirement(
            requirements,
            "HARD_GATE_EXTERNAL_ROUTE",
            requiredness="REQUIRED",
            reason="hard safety/authority gate requires an external/world-side route before unrestricted action",
            basis="hard gate",
        )

    if case_status == "CLOSED":
        route_mode = "CLOSED"
    elif dependency_blocked:
        route_mode = "DEPENDENCY_HOLD"
    elif hard_escalation or endorsed_authority_block:
        route_mode = "EXTERNAL_REQUIRED"
    elif unresolved_authority_candidate:
        route_mode = "AUTHORITY_UNRESOLVED"
    elif market_forward_allowed:
        route_mode = "PARALLEL_OR_FORWARD_EXPERIMENT"
    else:
        route_mode = "MINIMUM_SUFFICIENT_FLEXIBLE"

    external_used = bool(case.get("external_actor_used", False))
    knowledge_class = "K*_I" if external_used and return_gate == "PASS" else "K*_0"

    return {
        "matrix_version": "0.1.2",
        "phase": phase,
        "phase_semantics": "ROUTING_CONTEXT_NOT_MANDATORY_SEQUENCE",
        "route_mode": route_mode,
        "ai_role": {
            "class": "MEDIATOR_TRANSLATOR",
            "connects": [
                "citizen language",
                "knowledge-like sources/readouts",
                "interaction experts",
                "field experts",
                "tools/infrastructure",
                "institutions/authorities",
                "world return",
            ],
            "is_expert_class": False,
            "confers_professional_authority": False,
            "counts_as_independent_validation": False,
        },
        "expert_model": {
            "expert_classes": list(EXPERT_CLASSES),
            "interaction_expert": "expertise expressed through elicitation, interpretation, dialogue, teaching, negotiation, or stakeholder interaction",
            "field_expert": "situated/front-line expertise grounded in direct practice, tacit distinctions, physical context, or repeated world contact",
            "authority_overlays": list(AUTHORITY_OVERLAYS),
            "note": "licensed authority, laboratory infrastructure, and regulation are overlays/constraints; they do not erase the interaction-vs-field expert distinction",
        },
        "knowledge_like": {
            "class": knowledge_class,
            "status": "PROVISIONAL",
            "is_human_expert": False,
            "is_truth_certificate": False,
            "note": "K*_I is emitted only after a usable external return passes the Return Gate; otherwise the readout remains K*_0",
        },
        "signature_basis": signature_basis,
        "authority_need": authority_need,
        "requirements": requirements,
        "forward_experiment": {
            "allowed": forward_allowed,
            "market_test_candidate": market_forward_allowed,
            "rule": "bounded/reversible world action may run when no blocking gate exists; market-facing tests additionally require an endorsed LOW-irreversibility, LOW-third-party, authority_need=NONE state",
            "not_a_phase_skip_claim": True,
        },
        "hard_gate_reasons": list(hard_reasons or []),
        "observed_context_count": len(observations),
        "unknown_context_count": len(unknowns),
    }
