from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from mcp.server import MCPServer

from toledo_runtime import (
    EquationStore,
    InstitutionStore,
    compile_protocol,
    validate_handoff,
    validate_return_gate,
)

mcp = MCPServer(
    "toledo-citizen",
    instructions=(
        "Use Toledo as a citizen-centered protocol and equation readout layer. "
        "Preserve equation provenance and proposal/canonical status. "
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
    """Compile a minimal deterministic Toledo protocol instance from a case state."""
    return compile_protocol(case)


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


@mcp.resource("toledo://schema/case-passport")
def case_passport_schema() -> str:
    return (_ROOT / "packages" / "schemas" / "case-passport.schema.json").read_text(encoding="utf-8")


@mcp.resource("toledo://schema/protocol-instance")
def protocol_instance_schema() -> str:
    return (_ROOT / "packages" / "schemas" / "protocol-instance.schema.json").read_text(encoding="utf-8")


def run() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    run()
