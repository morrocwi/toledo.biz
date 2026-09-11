from __future__ import annotations

import copy
import hashlib
from datetime import datetime, timezone
from typing import Any

PHASES = {f"P{i}" for i in range(12)}
THREAD_STATUSES = {"OPEN", "HOLD", "BLOCKED", "CLOSED", "CANCELLED"}
CLOSURE_OUTCOMES = {
    "resolved",
    "improved",
    "safely_held",
    "explicitly_rescoped_with_consent",
}
THREAD_SCOPABLE_EVENTS = {
    "OBSERVATION_ADDED",
    "UNKNOWN_ADDED",
    "UNKNOWN_RESOLVED",
    "HYPOTHESIS_ADDED",
    "ACTION_RECORDED",
    "RESULT_RECORDED",
    "RISK_UPDATED",
    "PHASE_CHANGED",
    "SIGNATURE_CANDIDATES_UPDATED",
    "SIGNATURE_ENDORSED",
    "BARRIER_UPDATED",
    "CAPABILITY_REQUESTED",
    "INSTITUTION_SELECTED",
    "ROUTE_FAILED",
    "HANDOFF_CHECKED",
    "RETURN_RECEIVED",
    "OUTCOME_UPDATED",
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _text(value: Any) -> str:
    return str(value or "").strip()


def _append_unique(values: list[str], value: Any) -> None:
    item = _text(value)
    if item and item not in values:
        values.append(item)


def _risk_state(risk: dict[str, Any] | None) -> str:
    # Lazy import avoids a module-import cycle while preserving the one risk rule.
    from .cases import risk_state

    return risk_state(risk)


def _make_thread_id(case_id: str, decision: str, ordinal: int) -> str:
    seed = f"{case_id}|{ordinal}|{decision}".encode("utf-8")
    return "td-" + hashlib.sha256(seed).hexdigest()[:16]


def _valid_thread_id(value: Any) -> bool:
    text = _text(value)
    if not text.startswith("td-") or len(text) != 19:
        return False
    try:
        int(text[3:], 16)
        return True
    except ValueError:
        return False


def normalize_thread(
    raw: dict[str, Any],
    *,
    case_id: str,
    ordinal: int,
    default_decision_owner: str | None = "citizen",
) -> dict[str, Any]:
    decision = _text(raw.get("decision")) or "identify the minimum sufficient next action"
    phase = _text(raw.get("phase") or "P0").upper()
    if phase not in PHASES:
        raise ValueError("decision thread phase must be P0..P11")

    thread_id = _text(raw.get("thread_id"))
    if not _valid_thread_id(thread_id):
        thread_id = _make_thread_id(case_id, decision, ordinal)

    status = _text(raw.get("status") or "OPEN").upper()
    if status not in THREAD_STATUSES:
        raise ValueError(f"decision thread status must be one of {sorted(THREAD_STATUSES)}")

    created_at = _text(raw.get("created_at")) or _now()
    updated_at = _text(raw.get("updated_at")) or created_at
    risk = copy.deepcopy(raw.get("risk_profile") or {})

    return {
        "thread_id": thread_id,
        "decision": decision,
        "phase": phase,
        "status": status,
        "required_for_case_closure": bool(raw.get("required_for_case_closure", True)),
        "depends_on": list(dict.fromkeys(_text(x) for x in raw.get("depends_on", []) if _text(x))),
        "blocking_threads": list(dict.fromkeys(_text(x) for x in raw.get("blocking_threads", []) if _text(x))),
        "problem_signature": copy.deepcopy(raw.get("problem_signature")),
        "observations": [_text(x) for x in raw.get("observations", []) if _text(x)],
        "unknowns": [_text(x) for x in raw.get("unknowns", []) if _text(x)],
        "hypotheses": [_text(x) for x in raw.get("hypotheses", []) if _text(x)],
        "evidence_refs": [_text(x) for x in raw.get("evidence_refs", []) if _text(x)],
        "risk_profile": risk,
        "risk_state": _risk_state(risk),
        "requested_capability": raw.get("requested_capability"),
        "why_capability_is_needed": raw.get("why_capability_is_needed"),
        "decision_owner": raw.get("decision_owner") or default_decision_owner,
        "current_institution": raw.get("current_institution"),
        "external_actor_used": bool(raw.get("external_actor_used", False)),
        "latest_return_gate": _text(raw.get("latest_return_gate") or "NOT_APPLICABLE").upper(),
        "outcome_state": _text(raw.get("outcome_state") or "ongoing").lower(),
        "previous_actions": [_text(x) for x in raw.get("previous_actions", []) if _text(x)],
        "previous_results": [_text(x) for x in raw.get("previous_results", []) if _text(x)],
        "failed_routes": [_text(x) for x in raw.get("failed_routes", []) if _text(x)],
        "domain_overlay_refs": [_text(x) for x in raw.get("domain_overlay_refs", []) if _text(x)],
        "created_at": created_at,
        "updated_at": updated_at,
    }


def initialize_decision_threads(
    passport: dict[str, Any],
    supplied: list[dict[str, Any]] | None = None,
    primary_thread_id: str | None = None,
) -> None:
    existing = passport.get("decision_threads")
    source = existing if isinstance(existing, list) and existing else supplied

    if isinstance(source, list) and source:
        threads = [
            normalize_thread(
                item if isinstance(item, dict) else {},
                case_id=_text(passport.get("case_id")),
                ordinal=index,
                default_decision_owner=passport.get("decision_owner") or "citizen",
            )
            for index, item in enumerate(source)
        ]
    else:
        threads = [normalize_thread({
            "decision": passport.get("current_decision") or "identify the minimum sufficient next action",
            "phase": passport.get("current_phase") or "P0",
            "problem_signature": passport.get("problem_signature"),
            "observations": passport.get("observations") or [],
            "unknowns": passport.get("unknowns") or [],
            "hypotheses": passport.get("hypotheses") or [],
            "evidence_refs": passport.get("evidence_refs") or [],
            "risk_profile": passport.get("risk_profile") or {},
            "requested_capability": passport.get("requested_capability"),
            "why_capability_is_needed": passport.get("why_capability_is_needed"),
            "decision_owner": passport.get("decision_owner") or "citizen",
            "current_institution": passport.get("current_institution"),
            "external_actor_used": bool(passport.get("external_actor_used", False)),
            "latest_return_gate": passport.get("latest_return_gate") or "NOT_APPLICABLE",
            "outcome_state": passport.get("outcome_state") or "ongoing",
        }, case_id=_text(passport.get("case_id")), ordinal=0)]

    ids = [x["thread_id"] for x in threads]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate decision thread IDs")

    passport["decision_threads"] = threads
    requested_primary = _text(primary_thread_id or passport.get("primary_thread_id"))
    passport["primary_thread_id"] = requested_primary if requested_primary in ids else ids[0]
    refresh_thread_dependencies(passport)
    sync_primary_projection(passport)


def ensure_decision_threads(passport: dict[str, Any]) -> None:
    if not isinstance(passport.get("decision_threads"), list) or not passport.get("decision_threads"):
        initialize_decision_threads(passport)
        return

    # Normalize legacy or partially populated thread objects without changing identity.
    normalized = []
    for index, raw in enumerate(passport["decision_threads"]):
        normalized.append(normalize_thread(
            raw if isinstance(raw, dict) else {},
            case_id=_text(passport.get("case_id")),
            ordinal=index,
            default_decision_owner=passport.get("decision_owner") or "citizen",
        ))
    passport["decision_threads"] = normalized
    ids = [x["thread_id"] for x in normalized]
    primary = _text(passport.get("primary_thread_id"))
    if primary not in ids:
        passport["primary_thread_id"] = ids[0]
    refresh_thread_dependencies(passport)
    sync_primary_projection(passport)


def get_thread(passport: dict[str, Any], thread_id: str) -> dict[str, Any]:
    ensure_decision_threads(passport)
    target = _text(thread_id)
    for thread in passport["decision_threads"]:
        if thread["thread_id"] == target:
            return thread
    raise ValueError(f"decision thread not found: {target or '<empty>'}")


def create_thread(passport: dict[str, Any], payload: dict[str, Any]) -> dict[str, Any]:
    ensure_decision_threads(passport)
    raw = payload.get("thread") if isinstance(payload.get("thread"), dict) else payload
    thread = normalize_thread(
        raw,
        case_id=_text(passport.get("case_id")),
        ordinal=len(passport["decision_threads"]),
        default_decision_owner=passport.get("decision_owner") or "citizen",
    )
    if any(x["thread_id"] == thread["thread_id"] for x in passport["decision_threads"]):
        raise ValueError("decision thread ID already exists")
    passport["decision_threads"].append(thread)
    if payload.get("make_primary") is True:
        passport["primary_thread_id"] = thread["thread_id"]
    refresh_thread_dependencies(passport)
    sync_primary_projection(passport)
    return thread


def set_primary_thread(passport: dict[str, Any], thread_id: str) -> None:
    thread = get_thread(passport, thread_id)
    if thread["status"] == "CANCELLED":
        raise ValueError("cancelled decision thread cannot be primary")
    passport["primary_thread_id"] = thread["thread_id"]
    sync_primary_projection(passport)


def update_dependencies(passport: dict[str, Any], thread_id: str, depends_on: list[Any]) -> None:
    thread = get_thread(passport, thread_id)
    dependencies = list(dict.fromkeys(_text(x) for x in depends_on if _text(x)))
    if thread_id in dependencies:
        raise ValueError("decision thread cannot depend on itself")
    thread["depends_on"] = dependencies
    thread["updated_at"] = _now()
    refresh_thread_dependencies(passport)


def cancel_thread(passport: dict[str, Any], thread_id: str) -> None:
    thread = get_thread(passport, thread_id)
    thread["status"] = "CANCELLED"
    thread["updated_at"] = _now()
    refresh_thread_dependencies(passport)
    if passport.get("primary_thread_id") == thread_id:
        active = [x for x in passport["decision_threads"] if x["status"] != "CANCELLED"]
        if active:
            passport["primary_thread_id"] = active[0]["thread_id"]
    sync_primary_projection(passport)


def refresh_thread_dependencies(passport: dict[str, Any]) -> None:
    threads = passport.get("decision_threads") or []
    by_id = {x.get("thread_id"): x for x in threads if isinstance(x, dict)}
    for thread in threads:
        blockers = []
        for dependency in thread.get("depends_on", []) or []:
            target = by_id.get(dependency)
            if target is None or target.get("status") not in {"CLOSED", "CANCELLED"}:
                blockers.append(dependency)
        thread["blocking_threads"] = list(dict.fromkeys(blockers))
        if thread.get("status") not in {"CLOSED", "CANCELLED"}:
            if blockers:
                thread["status"] = "BLOCKED"
            elif thread.get("status") == "BLOCKED":
                if thread.get("latest_return_gate") in {"FAIL", "HOLD_UNKNOWN"}:
                    thread["status"] = "HOLD"
                else:
                    thread["status"] = "OPEN"


def sync_primary_projection(passport: dict[str, Any]) -> None:
    threads = passport.get("decision_threads") or []
    if not threads:
        return
    primary_id = _text(passport.get("primary_thread_id"))
    primary = next((x for x in threads if x.get("thread_id") == primary_id), threads[0])
    passport["primary_thread_id"] = primary["thread_id"]
    passport["current_phase"] = primary["phase"]
    passport["current_decision"] = primary["decision"]


def required_threads_closed(passport: dict[str, Any]) -> bool:
    ensure_decision_threads(passport)
    required = [
        x for x in passport["decision_threads"]
        if x.get("required_for_case_closure", True) and x.get("status") != "CANCELLED"
    ]
    return bool(required) and all(x.get("status") == "CLOSED" for x in required)


def apply_thread_scoped_event(
    passport: dict[str, Any],
    event_type: str,
    payload: dict[str, Any],
    *,
    return_gate_state: str | None = None,
) -> bool:
    thread_id = _text(payload.get("thread_id"))
    if not thread_id or event_type not in THREAD_SCOPABLE_EVENTS:
        return False

    thread = get_thread(passport, thread_id)

    if event_type == "OBSERVATION_ADDED":
        _append_unique(thread["observations"], payload.get("value") or payload.get("observation"))
    elif event_type == "UNKNOWN_ADDED":
        _append_unique(thread["unknowns"], payload.get("value") or payload.get("unknown"))
    elif event_type == "UNKNOWN_RESOLVED":
        target = _text(payload.get("value") or payload.get("unknown"))
        if target:
            thread["unknowns"] = [x for x in thread["unknowns"] if _text(x) != target]
        _append_unique(thread["previous_results"], payload.get("resolution"))
    elif event_type == "HYPOTHESIS_ADDED":
        _append_unique(thread["hypotheses"], payload.get("value") or payload.get("hypothesis"))
    elif event_type == "ACTION_RECORDED":
        _append_unique(thread["previous_actions"], payload.get("action") or payload.get("value"))
    elif event_type == "RESULT_RECORDED":
        _append_unique(thread["previous_results"], payload.get("result") or payload.get("value"))
    elif event_type == "RISK_UPDATED":
        patch = payload.get("risk") if isinstance(payload.get("risk"), dict) else {
            key: value for key, value in payload.items() if key != "thread_id"
        }
        thread["risk_profile"].update(copy.deepcopy(patch))
        thread["risk_state"] = _risk_state(thread["risk_profile"])
    elif event_type == "PHASE_CHANGED":
        phase = _text(payload.get("phase")).upper()
        if phase not in PHASES:
            raise ValueError("phase must be P0..P11")
        thread["phase"] = phase
    elif event_type == "SIGNATURE_CANDIDATES_UPDATED":
        incoming = payload.get("problem_signature") if isinstance(payload.get("problem_signature"), dict) else None
        if incoming is None:
            raise ValueError("thread-scoped SIGNATURE_CANDIDATES_UPDATED requires problem_signature")
        thread["problem_signature"] = copy.deepcopy(incoming)
    elif event_type == "SIGNATURE_ENDORSED":
        signature_id = _text(payload.get("signature_id"))
        signature = thread.get("problem_signature")
        if not signature_id or not isinstance(signature, dict):
            raise ValueError("thread-scoped SIGNATURE_ENDORSED requires an existing problem signature")
        candidates = signature.get("candidate_signatures") or []
        match = next((x for x in candidates if _text(x.get("signature_id")) == signature_id), None)
        if match is None:
            raise ValueError("signature_id is not present in the thread candidate signatures")
        match["citizen_endorsement"] = "PASS"
        signature["endorsed_signature_id"] = signature_id
        signature["status"] = "ENDORSED"
    elif event_type == "BARRIER_UPDATED":
        signature = thread.get("problem_signature")
        if not isinstance(signature, dict):
            raise ValueError("thread-scoped BARRIER_UPDATED requires a problem signature")
        barriers = signature.setdefault("barrier_state", {})
        barrier = _text(payload.get("barrier")).lower()
        state = _text(payload.get("state")).upper()
        if state not in {"PRESENT", "ABSENT", "UNKNOWN"}:
            raise ValueError("barrier state must be PRESENT, ABSENT, or UNKNOWN")
        barriers[barrier] = state
    elif event_type == "CAPABILITY_REQUESTED":
        capability = _text(payload.get("requested_capability"))
        if not capability:
            raise ValueError("CAPABILITY_REQUESTED requires requested_capability")
        thread["requested_capability"] = capability
        thread["why_capability_is_needed"] = payload.get("why_capability_is_needed")
    elif event_type == "INSTITUTION_SELECTED":
        institution = _text(payload.get("institution_id") or payload.get("institution"))
        if not institution:
            raise ValueError("INSTITUTION_SELECTED requires institution_id")
        thread["current_institution"] = institution
        thread["external_actor_used"] = True
    elif event_type == "ROUTE_FAILED":
        reason = _text(payload.get("reason")) or "route failed"
        institution = _text(payload.get("institution_id") or thread.get("current_institution"))
        _append_unique(thread["failed_routes"], f"{institution}: {reason}" if institution else reason)
        thread["current_institution"] = None
        if thread.get("status") not in {"CLOSED", "CANCELLED"}:
            thread["status"] = "OPEN"
    elif event_type == "HANDOFF_CHECKED":
        result = payload.get("result") or {}
        if payload.get("external_actor_used") is True:
            thread["external_actor_used"] = True
        if result.get("valid") is False:
            thread["status"] = "HOLD"
        elif result.get("valid") is True and thread["status"] not in {"CLOSED", "CANCELLED"}:
            thread["status"] = "OPEN"
    elif event_type == "RETURN_RECEIVED":
        if return_gate_state is None:
            raise ValueError("thread-scoped RETURN_RECEIVED requires computed return gate state")
        return_object = payload.get("return_object") if isinstance(payload.get("return_object"), dict) else payload
        thread["external_actor_used"] = True
        thread["latest_return_gate"] = return_gate_state
        if return_object.get("source_institution"):
            thread["current_institution"] = return_object.get("source_institution")
        _append_unique(thread["previous_results"], return_object.get("plain_language_result"))
        for item in return_object.get("what_is_unknown", []) or []:
            _append_unique(thread["unknowns"], item)
        thread["status"] = "OPEN" if return_gate_state == "PASS" else "HOLD"
    elif event_type == "OUTCOME_UPDATED":
        outcome = _text(payload.get("outcome_state")).lower()
        allowed = CLOSURE_OUTCOMES | {"ongoing", "worsened", "unknown"}
        if outcome not in allowed:
            raise ValueError(f"outcome_state must be one of {sorted(allowed)}")
        thread["outcome_state"] = outcome
        _append_unique(thread["previous_results"], payload.get("result"))
        local_closure = (
            not thread["external_actor_used"]
            and thread["latest_return_gate"] == "NOT_APPLICABLE"
            and thread["risk_state"] != "HARD_ESCALATION"
        )
        external_closure = thread["external_actor_used"] and thread["latest_return_gate"] == "PASS"
        if outcome in CLOSURE_OUTCOMES and (local_closure or external_closure):
            thread["status"] = "CLOSED"
        elif outcome in CLOSURE_OUTCOMES:
            thread["status"] = "HOLD"
        elif outcome == "worsened":
            thread["status"] = "OPEN"

    thread["updated_at"] = _now()
    refresh_thread_dependencies(passport)
    sync_primary_projection(passport)
    return True


def thread_compile_input(passport: dict[str, Any], thread: dict[str, Any]) -> dict[str, Any]:
    return {
        "problem": passport.get("citizen_problem_verbatim"),
        "goal": passport.get("citizen_goal"),
        "phase": thread.get("phase") or "P0",
        "jurisdiction": passport.get("jurisdiction") or "TH",
        "target_user": passport.get("target_user") or "citizen",
        "practice_context": passport.get("practice_context") or {},
        "problem_signature": thread.get("problem_signature") or passport.get("problem_signature") or {},
        "requested_capability": thread.get("requested_capability"),
        "evidence": {
            "observations": thread.get("observations") or [],
            "unknowns": thread.get("unknowns") or [],
        },
        "risk": thread.get("risk_profile") or {},
        "case_id": passport.get("case_id"),
        "case_passport_version": passport.get("version"),
        "case_status": "CLOSED" if thread.get("status") in {"CLOSED", "CANCELLED"} else "OPEN",
        "latest_return_gate": thread.get("latest_return_gate") or "NOT_APPLICABLE",
        "external_actor_used": bool(thread.get("external_actor_used", False)),
        "outcome_state": thread.get("outcome_state") or "ongoing",
        "failed_routes": thread.get("failed_routes") or [],
        "dependency_blocked": bool(thread.get("blocking_threads")),
        "dependency_reasons": [f"waiting_for:{x}" for x in thread.get("blocking_threads", [])],
    }


def compile_decision_threads(passport: dict[str, Any]) -> list[dict[str, Any]]:
    from .protocol import compile_protocol

    ensure_decision_threads(passport)
    refresh_thread_dependencies(passport)
    results = []
    for thread in passport["decision_threads"]:
        protocol = compile_protocol(thread_compile_input(passport, thread))
        protocol.update({
            "thread_id": thread["thread_id"],
            "decision": thread["decision"],
            "thread_status": thread["status"],
            "depends_on": copy.deepcopy(thread["depends_on"]),
            "blocking_threads": copy.deepcopy(thread["blocking_threads"]),
            "required_for_case_closure": thread["required_for_case_closure"],
        })
        results.append(protocol)
    return results
