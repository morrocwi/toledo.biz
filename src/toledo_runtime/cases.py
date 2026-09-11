from __future__ import annotations

import copy
import hashlib
import json
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

PHASES = {f"P{i}" for i in range(12)}

EVENT_TYPES = {
    "OBSERVATION_ADDED",
    "UNKNOWN_ADDED",
    "UNKNOWN_RESOLVED",
    "HYPOTHESIS_ADDED",
    "ACTION_RECORDED",
    "RESULT_RECORDED",
    "RISK_UPDATED",
    "PHASE_CHANGED",
    "GOAL_CONFIRMED",
    "STRUCTURED_PROBLEM_UPDATED",
    "DISCIPLINARY_PROBLEM_UPDATED",
    "SIGNATURE_CANDIDATES_UPDATED",
    "SIGNATURE_ENDORSED",
    "BARRIER_UPDATED",
    "CAPABILITY_REQUESTED",
    "INSTITUTION_SELECTED",
    "ROUTE_FAILED",
    "HANDOFF_CHECKED",
    "RETURN_RECEIVED",
    "OUTCOME_UPDATED",
    "NOTE",
}

CLOSURE_OUTCOMES = {
    "resolved",
    "improved",
    "safely_held",
    "explicitly_rescoped_with_consent",
}

BARRIER_KEYS = {
    "knowledge",
    "skill",
    "language",
    "tool",
    "resource_time",
    "network",
    "credential",
    "permission",
    "opportunity",
    "unknown",
}

BARRIER_STATES = {"PRESENT", "ABSENT", "UNKNOWN"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _text(value: Any) -> str:
    return str(value or "").strip()


def _append_unique(values: list[str], value: Any) -> None:
    item = _text(value)
    if item and item not in values:
        values.append(item)


def _empty_problem_signature() -> dict[str, Any]:
    return {
        "status": "NOT_PROVIDED",
        "candidate_signatures": [],
        "endorsed_signature_id": None,
        "context_known": [],
        "context_unknown": [],
        "barrier_state": {key: "UNKNOWN" for key in sorted(BARRIER_KEYS)},
        "domain_adapter_required": "HOLD_UNKNOWN",
    }


def _normalize_problem_signature(value: Any) -> dict[str, Any]:
    signature = _empty_problem_signature()
    if not isinstance(value, dict):
        return signature

    if value.get("status") in {"NOT_PROVIDED", "CANDIDATE", "ENDORSED", "HOLD_UNKNOWN"}:
        signature["status"] = value["status"]

    if isinstance(value.get("candidate_signatures"), list):
        signature["candidate_signatures"] = copy.deepcopy(value["candidate_signatures"])

    endorsed = value.get("endorsed_signature_id")
    signature["endorsed_signature_id"] = _text(endorsed) or None

    for key in ("context_known", "context_unknown"):
        if isinstance(value.get(key), list):
            signature[key] = [_text(x) for x in value[key] if _text(x)]

    barriers = value.get("barrier_state")
    if isinstance(barriers, dict):
        for key, state in barriers.items():
            state_text = _text(state).upper()
            if key in BARRIER_KEYS and state_text in BARRIER_STATES:
                signature["barrier_state"][key] = state_text

    domain_state = _text(value.get("domain_adapter_required")).upper()
    if domain_state in {"YES", "NO", "HOLD_UNKNOWN"}:
        signature["domain_adapter_required"] = domain_state

    return signature


def evaluate_hard_risk(risk: dict[str, Any] | None) -> tuple[bool, list[str]]:
    risk = risk or {}
    reasons: list[str] = []
    if risk.get("professional_authority_required"):
        reasons.append("professional_authority_required")
    if risk.get("regulatory_required"):
        reasons.append("regulatory_required")
    if float(risk.get("severity", 0) or 0) >= 0.7:
        reasons.append("high_severity")
    if float(risk.get("irreversibility", 0) or 0) >= 0.8:
        reasons.append("high_irreversibility")
    if float(risk.get("third_party_exposure", 0) or 0) >= 0.7:
        reasons.append("high_third_party_exposure")
    return bool(reasons), reasons


def risk_state(risk: dict[str, Any] | None) -> str:
    hard, _ = evaluate_hard_risk(risk)
    return "HARD_ESCALATION" if hard else "NO_HARD_TRIGGER"


def create_case_passport(case: dict[str, Any]) -> dict[str, Any]:
    """Create a versioned Case Passport from a citizen-facing case input.

    This is a pure in-memory constructor. The public repository does not persist
    sensitive citizen cases. Deployments are responsible for private storage.
    """
    problem = _text(case.get("problem") or case.get("citizen_problem_verbatim"))
    if not problem:
        raise ValueError("problem is required")

    phase = _text(case.get("phase") or case.get("current_phase") or "P0").upper()
    if phase not in PHASES:
        raise ValueError("phase must be P0..P11")

    supplied_goal = _text(case.get("goal") or case.get("citizen_goal"))
    goal = supplied_goal or "Address the stated problem safely with minimum sufficient support."
    goal_state = "USER_SUPPLIED" if supplied_goal else "PROVISIONAL"

    evidence = case.get("evidence") or {}
    observations = [_text(x) for x in evidence.get("observations", []) if _text(x)]
    unknowns = [_text(x) for x in evidence.get("unknowns", []) if _text(x)]
    hypotheses = [_text(x) for x in evidence.get("hypotheses", []) if _text(x)]
    risk = copy.deepcopy(case.get("risk") or case.get("risk_profile") or {})

    now = _now()
    case_id = _text(case.get("case_id")) or f"tc-{uuid4().hex}"
    steward = copy.deepcopy(case.get("case_steward") or {
        "steward_id": "citizen-self",
        "host_institution": None,
        "authority_scope": [
            "preserve_context",
            "request_routing",
            "receive_return",
        ],
    })
    consent = copy.deepcopy(case.get("consent") or {
        "status": "HOLD_UNKNOWN",
        "scope": ["local_protocol_compilation"],
        "expires_at": None,
    })
    problem_signature = _normalize_problem_signature(case.get("problem_signature"))

    passport: dict[str, Any] = {
        "case_id": case_id,
        "version": 1,
        "created_at": now,
        "updated_at": now,
        "case_status": "OPEN",
        "jurisdiction": _text(case.get("jurisdiction")) or "TH",
        "target_user": _text(case.get("target_user")) or "citizen",
        "practice_context": copy.deepcopy(case.get("practice_context") or {}),
        "citizen_problem_verbatim": problem,
        "citizen_goal": goal,
        "goal_state": goal_state,
        "citizen_constraints": [_text(x) for x in case.get("citizen_constraints", []) if _text(x)],
        "ai_structured_problem": case.get("ai_structured_problem"),
        "disciplinary_problem": case.get("disciplinary_problem"),
        "meaning_preservation_state": _text(case.get("meaning_preservation_state")) or "NOT_CHECKED",
        "problem_signature": problem_signature,
        "observations": observations,
        "evidence_refs": [_text(x) for x in case.get("evidence_refs", []) if _text(x)],
        "unknowns": unknowns,
        "hypotheses": hypotheses,
        "risk_state": risk_state(risk),
        "risk_profile": risk,
        "current_phase": phase,
        "current_decision": _text(case.get("current_decision")) or "identify the minimum sufficient next action",
        "next_decision": case.get("next_decision"),
        "requested_capability": case.get("requested_capability"),
        "why_capability_is_needed": case.get("why_capability_is_needed"),
        "current_actor": case.get("current_actor") or "citizen+ai",
        "current_institution": case.get("current_institution"),
        "external_actor_used": bool(case.get("external_actor_used", False)),
        "decision_owner": case.get("decision_owner") or "citizen",
        "consent": consent,
        "allowed_data_use": [_text(x) for x in case.get("allowed_data_use", []) if _text(x)],
        "publication_permission": _text(case.get("publication_permission")) or "UNKNOWN",
        "commercial_use_permission": _text(case.get("commercial_use_permission")) or "UNKNOWN",
        "experience_provenance": [_text(x) for x in case.get("experience_provenance", []) if _text(x)],
        "inventorship_state": case.get("inventorship_state"),
        "authorship_state": case.get("authorship_state"),
        "ip_state": case.get("ip_state"),
        "benefit_sharing_state": case.get("benefit_sharing_state"),
        "previous_actions": [],
        "previous_results": [],
        "failed_routes": [],
        "case_steward": steward,
        "expected_return": case.get("expected_return"),
        "response_deadline": case.get("response_deadline"),
        "decision_window": case.get("decision_window"),
        "known_cost": case.get("known_cost"),
        "currency": case.get("currency"),
        "fallback_route": case.get("fallback_route") or "reroute without restarting the case",
        "latest_return_gate": "NOT_APPLICABLE",
        "outcome_state": "ongoing",
        "return_obligation": copy.deepcopy(case.get("return_obligation") or {
            "required": True,
            "return_format": "plain-language result + knowns + unknowns + next action",
            "return_to": "citizen/decision owner",
        }),
        "events": [],
    }

    creation_event = {
        "event_id": _event_id(case_id, 1, "CASE_CREATED", {"phase": phase}),
        "event_type": "CASE_CREATED",
        "occurred_at": now,
        "actor": "system",
        "payload": {
            "phase": phase,
            "goal_state": goal_state,
            "risk_state": passport["risk_state"],
            "problem_signature_state": problem_signature["status"],
        },
    }
    passport["events"].append(creation_event)
    return passport


def _event_id(case_id: str, version: int, event_type: str, payload: dict[str, Any]) -> str:
    canonical = json.dumps(
        {"case_id": case_id, "version": version, "event_type": event_type, "payload": payload},
        ensure_ascii=False,
        sort_keys=True,
        default=str,
    )
    return "ev-" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]


def evaluate_return_object(return_object: dict[str, Any]) -> dict[str, Any]:
    """Evaluate a structured Return Object against the TCB-X005 implementation gate."""
    from .protocol import validate_return_gate

    gate_input = {
        "usable_result_returned": bool(_text(return_object.get("plain_language_result"))),
        "known_unknowns_stated": (
            "what_is_known" in return_object and "what_is_unknown" in return_object
        ),
        "next_action_stated": bool(_text(return_object.get("recommended_next_action"))),
        "relevant_data_returned": "data_returned_refs" in return_object,
        "citizen_correction_possible": return_object.get("citizen_correction_possible") is True,
        "unresolved_risk_and_rights_disclosed": (
            "limits" in return_object
            and "rights_state" in return_object
            and return_object.get("rights_state") is not None
        ),
    }
    computed = validate_return_gate(gate_input)
    declared = _text(return_object.get("return_gate_state")) or "HOLD_UNKNOWN"

    # Conservative rule: PASS requires both the declared state and computed gate.
    final_state = "PASS" if declared == "PASS" and computed["pass"] else (
        "FAIL" if declared == "FAIL" else "HOLD_UNKNOWN"
    )
    if declared == "PASS" and not computed["pass"]:
        final_state = "FAIL"

    return {
        "state": final_state,
        "declared_state": declared,
        "computed": computed,
        "equation_ref": "TCB-X005",
    }


def apply_case_event(passport: dict[str, Any], event: dict[str, Any]) -> dict[str, Any]:
    """Apply one auditable event and return a new Case Passport version."""
    if not isinstance(passport, dict) or not _text(passport.get("case_id")):
        raise ValueError("valid passport with case_id is required")

    event_type = _text(event.get("event_type")).upper()
    if event_type not in EVENT_TYPES:
        raise ValueError(f"unsupported event_type: {event_type or '<empty>'}")

    payload = copy.deepcopy(event.get("payload") or {})
    if "citizen_problem_verbatim" in payload:
        candidate = _text(payload.get("citizen_problem_verbatim"))
        if candidate and candidate != _text(passport.get("citizen_problem_verbatim")):
            raise ValueError("citizen_problem_verbatim is immutable; preserve P_C and add clarification instead")

    updated = copy.deepcopy(passport)
    updated.setdefault("events", [])
    updated.setdefault("observations", [])
    updated.setdefault("unknowns", [])
    updated.setdefault("hypotheses", [])
    updated.setdefault("previous_actions", [])
    updated.setdefault("previous_results", [])
    updated.setdefault("failed_routes", [])
    updated.setdefault("risk_profile", {})
    updated.setdefault("practice_context", {})
    updated["problem_signature"] = _normalize_problem_signature(updated.get("problem_signature"))
    updated.setdefault("external_actor_used", False)

    new_version = int(updated.get("version", 0)) + 1
    occurred_at = _text(event.get("occurred_at")) or _now()
    record = {
        "event_id": _event_id(updated["case_id"], new_version, event_type, payload),
        "event_type": event_type,
        "occurred_at": occurred_at,
        "actor": _text(event.get("actor")) or "unknown",
        "payload": payload,
    }

    if event_type == "OBSERVATION_ADDED":
        _append_unique(updated["observations"], payload.get("value") or payload.get("observation"))

    elif event_type == "UNKNOWN_ADDED":
        _append_unique(updated["unknowns"], payload.get("value") or payload.get("unknown"))

    elif event_type == "UNKNOWN_RESOLVED":
        target = _text(payload.get("value") or payload.get("unknown"))
        if target:
            updated["unknowns"] = [x for x in updated["unknowns"] if _text(x) != target]
        resolution = _text(payload.get("resolution"))
        if resolution:
            _append_unique(updated["previous_results"], resolution)

    elif event_type == "HYPOTHESIS_ADDED":
        _append_unique(updated["hypotheses"], payload.get("value") or payload.get("hypothesis"))

    elif event_type == "ACTION_RECORDED":
        _append_unique(updated["previous_actions"], payload.get("action") or payload.get("value"))

    elif event_type == "RESULT_RECORDED":
        _append_unique(updated["previous_results"], payload.get("result") or payload.get("value"))

    elif event_type == "RISK_UPDATED":
        patch = payload.get("risk") if isinstance(payload.get("risk"), dict) else payload
        updated["risk_profile"].update(copy.deepcopy(patch))
        updated["risk_state"] = risk_state(updated["risk_profile"])

    elif event_type == "PHASE_CHANGED":
        phase = _text(payload.get("phase")).upper()
        if phase not in PHASES:
            raise ValueError("phase must be P0..P11")
        updated["current_phase"] = phase

    elif event_type == "GOAL_CONFIRMED":
        goal = _text(payload.get("goal"))
        if not goal:
            raise ValueError("GOAL_CONFIRMED requires payload.goal")
        updated["citizen_goal"] = goal
        updated["goal_state"] = "CONFIRMED"

    elif event_type == "STRUCTURED_PROBLEM_UPDATED":
        structured = _text(payload.get("structured_problem"))
        if not structured:
            raise ValueError("STRUCTURED_PROBLEM_UPDATED requires payload.structured_problem")
        updated["ai_structured_problem"] = structured
        updated["meaning_preservation_state"] = _text(payload.get("meaning_preservation_state")) or "HOLD_UNKNOWN"

    elif event_type == "DISCIPLINARY_PROBLEM_UPDATED":
        disciplinary = _text(payload.get("disciplinary_problem"))
        if not disciplinary:
            raise ValueError("DISCIPLINARY_PROBLEM_UPDATED requires payload.disciplinary_problem")
        updated["disciplinary_problem"] = disciplinary
        updated["meaning_preservation_state"] = _text(payload.get("meaning_preservation_state")) or "HOLD_UNKNOWN"

    elif event_type == "SIGNATURE_CANDIDATES_UPDATED":
        incoming = payload.get("problem_signature") if isinstance(payload.get("problem_signature"), dict) else payload
        updated["problem_signature"] = _normalize_problem_signature(incoming)
        if updated["problem_signature"]["candidate_signatures"] and updated["problem_signature"]["status"] == "NOT_PROVIDED":
            updated["problem_signature"]["status"] = "CANDIDATE"

    elif event_type == "SIGNATURE_ENDORSED":
        signature_id = _text(payload.get("signature_id"))
        if not signature_id:
            raise ValueError("SIGNATURE_ENDORSED requires payload.signature_id")
        candidates = updated["problem_signature"].get("candidate_signatures", [])
        match = None
        for candidate in candidates:
            if _text(candidate.get("signature_id")) == signature_id:
                match = candidate
                break
        if match is None:
            raise ValueError("SIGNATURE_ENDORSED signature_id is not present in candidate_signatures")
        match["citizen_endorsement"] = "PASS"
        updated["problem_signature"]["endorsed_signature_id"] = signature_id
        updated["problem_signature"]["status"] = "ENDORSED"

    elif event_type == "BARRIER_UPDATED":
        barrier = _text(payload.get("barrier")).lower()
        state = _text(payload.get("state")).upper()
        if barrier not in BARRIER_KEYS:
            raise ValueError(f"BARRIER_UPDATED barrier must be one of {sorted(BARRIER_KEYS)}")
        if state not in BARRIER_STATES:
            raise ValueError(f"BARRIER_UPDATED state must be one of {sorted(BARRIER_STATES)}")
        updated["problem_signature"]["barrier_state"][barrier] = state

    elif event_type == "CAPABILITY_REQUESTED":
        capability = _text(payload.get("requested_capability"))
        if not capability:
            raise ValueError("CAPABILITY_REQUESTED requires payload.requested_capability")
        updated["requested_capability"] = capability
        updated["why_capability_is_needed"] = payload.get("why_capability_is_needed")

    elif event_type == "INSTITUTION_SELECTED":
        institution = _text(payload.get("institution_id") or payload.get("institution"))
        if not institution:
            raise ValueError("INSTITUTION_SELECTED requires institution_id")
        updated["current_institution"] = institution
        updated["current_actor"] = payload.get("actor") or "institution"
        updated["external_actor_used"] = True

    elif event_type == "ROUTE_FAILED":
        reason = _text(payload.get("reason")) or "route failed"
        institution = _text(payload.get("institution_id") or updated.get("current_institution"))
        _append_unique(updated["failed_routes"], f"{institution}: {reason}" if institution else reason)
        updated["current_institution"] = None
        if payload.get("fallback_route"):
            updated["fallback_route"] = payload.get("fallback_route")
        updated["case_status"] = "OPEN"

    elif event_type == "HANDOFF_CHECKED":
        result = payload.get("result") or {}
        if payload.get("external_actor_used") is True:
            updated["external_actor_used"] = True
        if result and result.get("valid") is False:
            updated["case_status"] = "HOLD"
        elif result and result.get("valid") is True and updated.get("case_status") != "CLOSED":
            updated["case_status"] = "OPEN"

    elif event_type == "RETURN_RECEIVED":
        return_object = payload.get("return_object") if isinstance(payload.get("return_object"), dict) else payload
        if _text(return_object.get("case_id")) not in {"", _text(updated.get("case_id"))}:
            raise ValueError("Return Object case_id does not match Case Passport")
        updated["external_actor_used"] = True
        gate = evaluate_return_object(return_object)
        updated["latest_return_gate"] = gate["state"]
        updated["current_actor"] = return_object.get("source_actor") or updated.get("current_actor")
        if return_object.get("source_institution"):
            updated["current_institution"] = return_object.get("source_institution")
        _append_unique(updated["previous_results"], return_object.get("plain_language_result"))
        for item in return_object.get("what_is_unknown", []) or []:
            _append_unique(updated["unknowns"], item)
        if gate["state"] == "PASS":
            updated["case_status"] = "OPEN"
        else:
            updated["case_status"] = "HOLD"
        record["gate_result"] = gate

    elif event_type == "OUTCOME_UPDATED":
        outcome = _text(payload.get("outcome_state")).lower()
        allowed = CLOSURE_OUTCOMES | {"ongoing", "worsened", "unknown"}
        if outcome not in allowed:
            raise ValueError(f"outcome_state must be one of {sorted(allowed)}")
        updated["outcome_state"] = outcome
        if payload.get("result"):
            _append_unique(updated["previous_results"], payload.get("result"))

        external = bool(updated.get("external_actor_used"))
        return_gate = updated.get("latest_return_gate")
        local_closure = (not external and return_gate == "NOT_APPLICABLE")
        external_closure = (external and return_gate == "PASS")

        if outcome in CLOSURE_OUTCOMES and (local_closure or external_closure):
            updated["case_status"] = "CLOSED"
        elif outcome in CLOSURE_OUTCOMES:
            updated["case_status"] = "HOLD"
        elif outcome == "worsened":
            updated["case_status"] = "OPEN"

    updated["version"] = new_version
    updated["updated_at"] = _now()
    updated["events"].append(record)
    return updated


def case_to_compile_input(passport: dict[str, Any]) -> dict[str, Any]:
    """Project a Case Passport into the protocol compiler's compact input shape."""
    return {
        "problem": passport.get("citizen_problem_verbatim"),
        "goal": passport.get("citizen_goal"),
        "phase": passport.get("current_phase") or "P0",
        "jurisdiction": passport.get("jurisdiction") or "TH",
        "target_user": passport.get("target_user") or "citizen",
        "practice_context": passport.get("practice_context") or {},
        "problem_signature": passport.get("problem_signature") or _empty_problem_signature(),
        "requested_capability": passport.get("requested_capability"),
        "evidence": {
            "observations": passport.get("observations") or [],
            "unknowns": passport.get("unknowns") or [],
        },
        "risk": passport.get("risk_profile") or {},
        "case_id": passport.get("case_id"),
        "case_passport_version": passport.get("version"),
        "case_status": passport.get("case_status") or "OPEN",
        "latest_return_gate": passport.get("latest_return_gate") or "NOT_APPLICABLE",
        "external_actor_used": bool(passport.get("external_actor_used", False)),
        "outcome_state": passport.get("outcome_state") or "ongoing",
        "failed_routes": passport.get("failed_routes") or [],
    }


def step_case(payload: dict[str, Any]) -> dict[str, Any]:
    """Initialize/update a Case Passport and compile the next deterministic protocol step.

    The function is stateless: callers hold the Case Passport and send it back on
    each step. This keeps the public reference runtime from becoming a citizen-data
    store while still providing a complete closed-loop state transition contract.
    """
    passport = payload.get("passport")
    raw_case = payload.get("case")

    if passport is None:
        if not isinstance(raw_case, dict):
            raise ValueError("either passport or case is required")
        passport = create_case_passport(raw_case)
    elif not isinstance(passport, dict):
        raise ValueError("passport must be an object")
    else:
        passport = copy.deepcopy(passport)

    events: list[dict[str, Any]] = []
    if isinstance(payload.get("event"), dict):
        events.append(payload["event"])
    if payload.get("events") is not None:
        if not isinstance(payload.get("events"), list):
            raise ValueError("events must be an array")
        events.extend(x for x in payload["events"] if isinstance(x, dict))

    for event in events:
        passport = apply_case_event(passport, event)

    from .protocol import compile_protocol

    protocol = compile_protocol(case_to_compile_input(passport))
    protocol["case_id"] = passport["case_id"]
    protocol["case_passport_version"] = passport["version"]
    protocol["case_status"] = passport.get("case_status")

    return {
        "case_id": passport["case_id"],
        "passport_version": passport["version"],
        "case_status": passport.get("case_status"),
        "closed": passport.get("case_status") == "CLOSED",
        "passport": passport,
        "protocol": protocol,
    }
