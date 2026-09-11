from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any

from .cases import evaluate_hard_risk
from .institutions import InstitutionStore

PHASES = {f"P{i}" for i in range(12)}

_ACTION_EQUATIONS = {
    "OBSERVE": ["TCB-E001", "TCB-F001"],
    "STRUCTURE": ["TCB-E001", "TCB-E002", "TCB-X001"],
    "MEASURE": ["TCB-F001", "TCB-F002"],
    "ESCALATE": ["TCB-R001", "TCB-R002", "TCB-I001", "TCB-X003"],
    "ACT": ["TCB-A001"],
    "TEST": ["TCB-F001", "TCB-F002", "TCB-F003"],
    "CHECK_PRIOR_ART": ["TCB-F004", "TCB-F005"],
    "MAP_RIGHTS": ["TCB-K001", "TCB-K002", "TCB-K003"],
    "SELECT_ROUTE": ["TCB-U001", "TCB-U002", "TCB-U003"],
    "FORM_BUSINESS_0": ["TCB-B001", "TCB-B004"],
    "CLOSE_FIRST_CYCLE": ["TCB-B002", "TCB-B003"],
    "SCALE_CHECK": ["TCB-G001", "TCB-G002", "TCB-G003", "TCB-G004"],
    "GLOBAL_CHECK": ["TCB-U001", "TCB-X004"],
    "RETURN": ["TCB-X005", "TCB-X008", "TCB-X009"],
    "STOP": ["TCB-X008", "TCB-X009"],
}


def _hard_escalation(risk: dict[str, Any]) -> tuple[bool, list[str]]:
    return evaluate_hard_risk(risk)


def _next_action(
    phase: str,
    observations: list[str],
    unknowns: list[str],
    hard: bool,
    *,
    case_status: str = "OPEN",
    latest_return_gate: str = "NOT_APPLICABLE",
) -> str:
    if case_status == "CLOSED":
        return "STOP"
    if latest_return_gate in {"FAIL", "HOLD_UNKNOWN"}:
        return "RETURN"
    if hard:
        return "ESCALATE"
    if phase == "P0":
        return "OBSERVE" if not observations else "STRUCTURE"
    if phase == "P1":
        return "MEASURE" if unknowns else "TEST"
    if phase == "P2":
        return "ACT"
    if phase == "P3":
        return "ESCALATE"
    if phase == "P4":
        return "CHECK_PRIOR_ART"
    if phase == "P5":
        return "TEST"
    if phase == "P6":
        return "MAP_RIGHTS"
    if phase == "P7":
        return "SELECT_ROUTE"
    if phase == "P8":
        return "FORM_BUSINESS_0"
    if phase == "P9":
        return "CLOSE_FIRST_CYCLE"
    if phase == "P10":
        return "SCALE_CHECK"
    if phase == "P11":
        return "GLOBAL_CHECK"
    return "STRUCTURE"


def compile_protocol(case: dict[str, Any]) -> dict[str, Any]:
    problem = str(case.get("problem", "")).strip()
    if not problem:
        raise ValueError("problem is required")
    phase = str(case.get("phase") or "P0").upper()
    if phase not in PHASES:
        raise ValueError("phase must be P0..P11")

    evidence = case.get("evidence") or {}
    observations = [str(x) for x in evidence.get("observations", [])]
    unknowns = [str(x) for x in evidence.get("unknowns", [])]
    risk = case.get("risk") or {}
    hard, hard_reasons = _hard_escalation(risk)

    case_status = str(case.get("case_status") or "OPEN").upper()
    latest_return_gate = str(case.get("latest_return_gate") or "NOT_APPLICABLE").upper()
    action = _next_action(
        phase,
        observations,
        unknowns,
        hard,
        case_status=case_status,
        latest_return_gate=latest_return_gate,
    )

    requested_capability = case.get("requested_capability")
    if action == "ESCALATE" and not requested_capability:
        requested_capability = "professional or specialist review"
    if action == "MEASURE" and not requested_capability:
        requested_capability = "measurement or testing"

    jurisdiction = str(case.get("jurisdiction") or "TH")
    institutions: list[dict[str, Any]] = []
    if action in {"ESCALATE", "MEASURE"}:
        institutions = InstitutionStore().route(
            jurisdiction=jurisdiction,
            phase=phase,
            capability=str(requested_capability or ""),
            target_user=case.get("target_user"),
            limit=int(case.get("institution_limit", 5)),
        )
        if not institutions and requested_capability:
            institutions = InstitutionStore().route(
                jurisdiction=jurisdiction,
                phase=phase,
                limit=int(case.get("institution_limit", 5)),
            )

    canonical_input = json.dumps(case, ensure_ascii=False, sort_keys=True)
    protocol_id = "tp-" + hashlib.sha256(canonical_input.encode("utf-8")).hexdigest()[:16]

    if case_status == "CLOSED":
        status = "CLOSED"
        why = ["citizen_closure_condition_recorded"]
    elif action == "RETURN":
        status = "HOLD_FOR_RETURN"
        why = ["return_gate_not_yet_passed"]
    elif hard:
        status = "HOLD_FOR_ESCALATION"
        why = hard_reasons
    else:
        status = "ACTIONABLE"
        why = [
            "minimal_relevant_subgraph_selected",
            "action_is_phase_and_evidence_sensitive",
        ]

    return {
        "protocol_id": protocol_id,
        "protocol_version": "0.2.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase": phase,
        "citizen_problem": problem,
        "goal": case.get("goal"),
        "status": status,
        "next_action": action,
        "why_this_action": why,
        "hard_gates": {
            "escalation_required": hard,
            "reasons": hard_reasons,
        },
        "known": observations,
        "unknown": unknowns,
        "requested_capability": requested_capability,
        "institution_candidates": institutions,
        "equation_refs": _ACTION_EQUATIONS.get(action, []),
        "equation_status": "proposal unless upstream registry says otherwise",
        "stop_condition": (
            "case is closed; reopen only on a new material trigger"
            if action == "STOP"
            else "return a usable result to the citizen/decision owner"
        ),
        "escalation_trigger": "hard safety/authority gate or evidence need exceeds citizen+AI route",
        "fallback": "preserve Case Passport and reroute without restarting the case",
        "return_requirement": "RETURN_GATE must pass before institutional work closes the case",
        "case_id": case.get("case_id"),
        "case_passport_version": case.get("case_passport_version"),
        "outcome_state": case.get("outcome_state"),
        "failed_routes": case.get("failed_routes") or [],
    }


def validate_handoff(payload: dict[str, Any]) -> dict[str, Any]:
    required = {
        "meaning_preserved": payload.get("meaning_preserved") == "PASS",
        "requested_capability_named": bool(payload.get("requested_capability")),
        "decision_owner_named": bool(payload.get("decision_owner")),
        "consent_pass": payload.get("consent") == "PASS",
        "data_use_scope_known": bool(payload.get("data_use_scope")),
        "return_required": payload.get("return_required") is True,
        "response_time_fit": payload.get("response_time_fit") is True,
        "fallback_route_known": bool(payload.get("fallback_route")),
    }
    return {
        "valid": all(required.values()),
        "checks": required,
        "equation_ref": "TCB-X003",
    }


def validate_return_gate(payload: dict[str, Any]) -> dict[str, Any]:
    required = {
        "usable_result_returned": payload.get("usable_result_returned") is True,
        "known_unknowns_stated": payload.get("known_unknowns_stated") is True,
        "next_action_stated": payload.get("next_action_stated") is True,
        "relevant_data_returned": payload.get("relevant_data_returned") is True,
        "citizen_correction_possible": payload.get("citizen_correction_possible") is True,
        "unresolved_risk_and_rights_disclosed": payload.get("unresolved_risk_and_rights_disclosed") is True,
    }
    return {
        "pass": all(required.values()),
        "checks": required,
        "equation_ref": "TCB-X005",
    }
