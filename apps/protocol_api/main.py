from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

from toledo_runtime import (
    EquationStore,
    InstitutionStore,
    apply_case_event,
    compile_decision_threads,
    compile_protocol,
    create_case_passport,
    step_case,
    validate_handoff,
    validate_return_gate,
)

app = FastAPI(
    title="Toledo Protocol API",
    version="0.5.0",
    description=(
        "Reference API for the Toledo Citizen Protocol Compiler, domain-neutral problem grammar, "
        "flexible execution routing, anchor-preserved Decision Threads, stateless Case Passport lifecycle, "
        "equation readouts, institution routing, handoff validation and Return Gate checks."
    ),
)

_eq = EquationStore()
_inst = InstitutionStore()
_ROOT = Path(__file__).resolve().parents[2]


@app.get("/health")
def health() -> dict[str, Any]:
    return {"ok": True, "service": "toledo-protocol-api", "version": "0.5.0"}


@app.get("/.well-known/toledo")
def well_known() -> dict[str, Any]:
    return json.loads((_ROOT / ".well-known" / "toledo.json").read_text(encoding="utf-8"))


@app.get("/v1/equations")
def equations(q: str = "", domain: str | None = None, live: bool = False) -> dict[str, Any]:
    entries = _eq.search(q, domain=domain, live=live)
    return {"count": len(entries), "entries": entries, "source": _eq.data(live=live).get("source")}


@app.get("/v1/equations/{equation_id}")
def equation(equation_id: str, live: bool = False) -> dict[str, Any]:
    item = _eq.get(equation_id, live=live)
    if not item:
        raise HTTPException(status_code=404, detail="equation not found")
    return item


@app.post("/v1/protocols/compile")
def protocol_compile(case: dict[str, Any]) -> dict[str, Any]:
    try:
        return compile_protocol(case)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.post("/v1/cases/init")
def case_init(case: dict[str, Any]) -> dict[str, Any]:
    try:
        passport = create_case_passport(case)
        return step_case({"passport": passport})
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.post("/v1/cases/update")
def case_update(payload: dict[str, Any]) -> dict[str, Any]:
    try:
        passport = payload.get("passport")
        event = payload.get("event")
        if not isinstance(passport, dict) or not isinstance(event, dict):
            raise ValueError("passport and event objects are required")
        updated = apply_case_event(passport, event)
        return {"passport": updated, "thread_protocols": compile_decision_threads(updated)}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.post("/v1/cases/step")
def case_step(payload: dict[str, Any]) -> dict[str, Any]:
    try:
        return step_case(payload)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.post("/v1/cases/threads/compile")
def case_threads_compile(passport: dict[str, Any]) -> dict[str, Any]:
    """Compile every Decision Thread without mutating the caller-held passport."""
    try:
        rows = compile_decision_threads(passport)
        return {
            "case_id": passport.get("case_id"),
            "primary_thread_id": passport.get("primary_thread_id"),
            "count": len(rows),
            "thread_protocols": rows,
        }
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@app.get("/v1/institutions")
def institutions(
    jurisdiction: str = "TH",
    phase: str | None = None,
    capability: str | None = None,
    target_user: str | None = None,
    limit: int = Query(default=5, ge=1, le=25),
) -> dict[str, Any]:
    rows = _inst.route(
        jurisdiction=jurisdiction,
        phase=phase,
        capability=capability,
        target_user=target_user,
        limit=limit,
    )
    return {"count": len(rows), "entries": rows}


@app.post("/v1/handoffs/validate")
def handoff_validate(payload: dict[str, Any]) -> dict[str, Any]:
    return validate_handoff(payload)


@app.post("/v1/returns/validate")
def return_validate(payload: dict[str, Any]) -> dict[str, Any]:
    return validate_return_gate(payload)


@app.get("/v1/schemas/{schema_name}")
def schema(schema_name: str) -> JSONResponse:
    allowed = {
        "case-passport": "case-passport.schema.json",
        "case-event": "case-event.schema.json",
        "case-step-request": "case-step-request.schema.json",
        "case-step-response": "case-step-response.schema.json",
        "problem-signature": "problem-signature.schema.json",
        "decision-thread": "decision-thread.schema.json",
        "execution-routing": "execution-routing.schema.json",
        "return-object": "return-object.schema.json",
        "institution-record": "institution-record.schema.json",
        "protocol-compile-request": "protocol-compile-request.schema.json",
        "protocol-instance": "protocol-instance.schema.json",
    }
    filename = allowed.get(schema_name)
    if not filename:
        raise HTTPException(status_code=404, detail="schema not found")
    path = _ROOT / "packages" / "schemas" / filename
    return JSONResponse(json.loads(path.read_text(encoding="utf-8")))


def run() -> None:
    import uvicorn
    uvicorn.run("apps.protocol_api.main:app", host="127.0.0.1", port=8787, reload=False)


if __name__ == "__main__":
    run()
