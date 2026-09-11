from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from mcp.server import MCPServer

from toledo_runtime import (
    EquationStore,
    InstitutionStore,
    apply_case_event,
    compile_protocol,
    create_case_passport,
    step_case,
    validate_handoff,
    validate_return_gate,
)

mcp = MCPServer(
    "toledo-citizen",
    instructions=(
        "Use Toledo as a citizen-centered protocol and equation readout layer. "
        "Preserve equation provenance and proposal/canonical status. "
        "Preserve P_C, Case Passport continuity, typed gates, and Return-to-Citizen. "
        "Do not treat AI as professional, regulatory, laboratory, or truth authority."
    ),
)
_eq = EquationStore()
_inst = InstitutionStore()
_ROOT = Path(__file__).resolve().parents[2]


@mcp.tool()
def get_equation(equation_id: str, live: bool = False) -> dict[str, Any]:
    """Return one Toledo equation/definition with upstream provenance."""
    item = _eq.get(equation_id, live=live)
    if item is None:
        return {"found": False, "equation_id": equation_id}
    return {"found": True, "equation": item}


@mcp.tool()
def search_equations(query: str = "", domain: str = "", live: bool = False) -> dict[str, Any]:
    """Search Toledo equation IDs, names, domains, kinds, and statements."""
    rows = _eq.search(query, domain=domain or None, live=live)
    return {"count": len(rows), "entries": rows}


@mcp.tool()
def compile_citizen_protocol(case: dict[str, Any]) -> dict[str, Any]:
    """Compile a minimal deterministic Toledo protocol instance from a compact case state."""
    return compile_protocol(case)


@mcp.tool()
def initialize_case(case: dict[str, Any]) -> dict[str, Any]:
    """Create a versioned Case Passport from a citizen problem without public persistence."""
    passport = create_case_passport(case)
    return {"passport": passport, "protocol": step_case({"passport": passport})["protocol"]}


@mcp.tool()
def update_case(passport: dict[str, Any], event: dict[str, Any]) -> dict[str, Any]:
    """Apply one auditable event to a Case Passport and return the next version."""
    return {"passport": apply_case_event(passport, event)}


@mcp.tool()
def advance_case(payload: dict[str, Any]) -> dict[str, Any]:
    """Initialize or update a Case Passport, then compile the next protocol step."""
    return step_case(payload)


@mcp.tool()
def route_institutions(
    phase: str,
    capability: str = "",
    jurisdiction: str = "TH",
    target_user: str = "",
    limit: int = 5,
) -> dict[str, Any]:
    """Find phase-fit institutional routes from an installed country adapter."""
    rows = _inst.route(
        jurisdiction=jurisdiction,
        phase=phase,
        capability=capability or None,
        target_user=target_user or None,
        limit=limit,
    )
    return {"count": len(rows), "entries": rows}


@mcp.tool()
def check_handoff(payload: dict[str, Any]) -> dict[str, Any]:
    """Evaluate the TCB-X003 valid-handoff predicate."""
    return validate_handoff(payload)


@mcp.tool()
def check_return_gate(payload: dict[str, Any]) -> dict[str, Any]:
    """Evaluate the TCB-X005 Return-to-Citizen Gate."""
    return validate_return_gate(payload)


@mcp.resource("toledo://equations/index")
def equation_index() -> str:
    """Machine-readable pinned mirror of the upstream Toledo citizen equation family."""
    return json.dumps(_eq.data(), ensure_ascii=False, indent=2)


@mcp.resource("toledo://equations/{equation_id}")
def equation_resource(equation_id: str) -> str:
    item = _eq.get(equation_id)
    return json.dumps(item or {"found": False, "equation_id": equation_id}, ensure_ascii=False, indent=2)


@mcp.resource("toledo://protocol/compiler")
def protocol_spec() -> str:
    return (_ROOT / "docs" / "PROTOCOL_COMPILER.md").read_text(encoding="utf-8")


@mcp.resource("toledo://protocol/case-lifecycle")
def case_lifecycle_spec() -> str:
    return (_ROOT / "docs" / "CASE_LIFECYCLE.md").read_text(encoding="utf-8")


@mcp.resource("toledo://schema/case-passport")
def case_passport_schema() -> str:
    return (_ROOT / "packages" / "schemas" / "case-passport.schema.json").read_text(encoding="utf-8")


@mcp.resource("toledo://schema/case-event")
def case_event_schema() -> str:
    return (_ROOT / "packages" / "schemas" / "case-event.schema.json").read_text(encoding="utf-8")


@mcp.resource("toledo://schema/case-step-request")
def case_step_request_schema() -> str:
    return (_ROOT / "packages" / "schemas" / "case-step-request.schema.json").read_text(encoding="utf-8")


@mcp.resource("toledo://schema/protocol-instance")
def protocol_instance_schema() -> str:
    return (_ROOT / "packages" / "schemas" / "protocol-instance.schema.json").read_text(encoding="utf-8")


def run() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    run()
