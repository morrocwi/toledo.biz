# Toledo Protocol API

The reference API exposes the Protocol Compiler, stateless closed-loop Case Passport lifecycle, equation readouts, institution routing, handoff validation and Return Gate validation.

## Run

```bash
python -m pip install -e .
toledo-api
```

Default development address: `http://127.0.0.1:8787`.

FastAPI also exposes generated OpenAPI at `/openapi.json` and interactive docs at `/docs`.

A repository-controlled contract is stored at `openapi/toledo.protocol.v1.yaml`.

## Endpoints

```text
GET  /health
GET  /.well-known/toledo
GET  /v1/equations
GET  /v1/equations/{equation_id}
POST /v1/protocols/compile
POST /v1/cases/init
POST /v1/cases/update
POST /v1/cases/step
GET  /v1/institutions
POST /v1/handoffs/validate
POST /v1/returns/validate
GET  /v1/schemas/{schema_name}
```

### Equations

`GET /v1/equations?domain=cross_actor&q=handoff`

Use `live=true` to attempt a read from the pinned upstream Toledo commit. Failure falls back to the local auditable mirror and is disclosed in the response.

### Direct compile

```bash
curl -X POST http://127.0.0.1:8787/v1/protocols/compile \
  -H 'content-type: application/json' \
  -d '{"problem":"Water pools in one part of my orchard","phase":"P0","jurisdiction":"TH"}'
```

### Initialize a Case Passport

```bash
curl -X POST http://127.0.0.1:8787/v1/cases/init \
  -H 'content-type: application/json' \
  -d '{"problem":"Water pools in one part of my orchard","goal":"Protect the trees","jurisdiction":"TH"}'
```

The response contains a caller-held `passport` plus the initial `protocol`.

### Advance a case

Send the passport back with one event:

```json
{
  "passport": {"...": "caller-held Case Passport"},
  "event": {
    "event_type": "OBSERVATION_ADDED",
    "actor": "citizen",
    "payload": {"value": "Pooling appears after heavy rain"}
  }
}
```

POST it to:

```text
/v1/cases/step
```

The API applies the event, increments the passport version and recompiles the next action.

### Return and closure

Institutional/expert results should arrive as `RETURN_RECEIVED` with a structured Return Object. The case closes only after a passing Return Gate and a citizen outcome event satisfying the current closure predicate.

## Storage boundary

The API is stateless in this reference implementation. It does not retain the Case Passport between requests.

Production deployments need authenticated private case storage, access control, encryption, consent enforcement, retention/deletion policy and audit logging.
