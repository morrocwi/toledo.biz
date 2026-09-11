# Toledo Protocol API

The reference API exposes the Protocol Compiler, domain-neutral Problem & Capability Grammar contracts, stateless closed-loop Case Passport lifecycle, equation readouts, institution routing, handoff validation and Return Gate validation.

## Run

```bash
python -m pip install -e .
toledo-api
```

Default development address: `http://127.0.0.1:8787`.

FastAPI also exposes generated OpenAPI at `/openapi.json` and interactive docs at `/docs`.

A repository-controlled contract is stored at `openapi/toledo.protocol.v1.yaml`.

Current reference API metadata version: `0.3.0`.

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

### Problem Signature machine contract

Retrieve:

```text
GET /v1/schemas/problem-signature
```

The schema represents **candidate routing readouts**, not a diagnosis or universal ontology. Material facets can carry provenance, multiple candidates may remain live, and unresolved context is valid.

```text
P_C != ProblemSignature
CandidateSignature != EndorsedSignature
Occupation != ProtocolSelector
```

### Direct compile

```bash
curl -X POST http://127.0.0.1:8787/v1/protocols/compile \
  -H 'content-type: application/json' \
  -d '{"problem":"Water pools in one part of my orchard","phase":"P0","jurisdiction":"TH"}'
```

`practice_context` may be supplied, but core behavior does not use an occupation label as a bespoke protocol selector.

### Initialize a Case Passport

```bash
curl -X POST http://127.0.0.1:8787/v1/cases/init \
  -H 'content-type: application/json' \
  -d '{"problem":"Water pools in one part of my orchard","goal":"Protect the trees","jurisdiction":"TH"}'
```

The response contains a caller-held `passport` plus the initial `protocol`.

A Case Passport can carry:

```text
practice_context
problem_signature
external_actor_used
```

without replacing `citizen_problem_verbatim`.

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

Problem-grammar events include:

```text
SIGNATURE_CANDIDATES_UPDATED
SIGNATURE_ENDORSED
BARRIER_UPDATED
```

`SIGNATURE_CANDIDATES_UPDATED` must not be interpreted as a diagnosis merely because the actor is AI.

### Return and closure

External institutional/expert results should arrive as `RETURN_RECEIVED` with a structured Return Object. An externally routed case closes only after a passing Return Gate plus a citizen outcome satisfying the current closure predicate.

A citizen+AI/world-only case that never used an external actor may close without a fake institutional Return Object when a closure outcome is recorded and no hard safety/authority trigger remains.

```text
external_actor_used = false
+ latest_return_gate = NOT_APPLICABLE
+ closure outcome
+ no hard escalation
→ CLOSED
```

This distinction prevents both false institutional closure and needless institutionalization of a valid local solution.

## Storage boundary

The API is stateless in this reference implementation. It does not retain the Case Passport between requests.

Production deployments need authenticated private case storage, access control, encryption, consent enforcement, retention/deletion policy and audit logging.
