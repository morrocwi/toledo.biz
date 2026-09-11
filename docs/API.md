# Toledo Protocol API

The reference API exposes the Protocol Compiler, domain-neutral Problem & Capability Grammar contracts, anchor-preserved Decision Threads, stateless closed-loop Case Passport lifecycle, equation readouts, institution routing, handoff validation and Return Gate validation.

## Run

```bash
python -m pip install -e .
toledo-api
```

Default development address: `http://127.0.0.1:8787`.

FastAPI also exposes generated OpenAPI at `/openapi.json` and interactive docs at `/docs`.

A repository-controlled contract is stored at `openapi/toledo.protocol.v1.yaml`.

Current reference API metadata version: `0.4.0`.

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
POST /v1/cases/threads/compile
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

### Decision Thread machine contract

Retrieve:

```text
GET /v1/schemas/decision-thread
```

A Decision Thread is a decision-specific subgraph inside one persistent Case Passport.

```text
Case != SingleDecision
DecisionThread != NewCase
ThreadPhase != CaseMaturity
```

Existing `current_phase` and `current_decision` fields remain as the primary-thread projection for backward compatibility.

### Direct compile

```bash
curl -X POST http://127.0.0.1:8787/v1/protocols/compile \
  -H 'content-type: application/json' \
  -d '{"problem":"Water pools in one part of my orchard","phase":"P0","jurisdiction":"TH"}'
```

`practice_context` may be supplied, but core behavior does not use an occupation or industry label as a bespoke protocol selector.

### Initialize a Case Passport

```bash
curl -X POST http://127.0.0.1:8787/v1/cases/init \
  -H 'content-type: application/json' \
  -d '{"problem":"Water pools in one part of my orchard","goal":"Protect the trees","jurisdiction":"TH"}'
```

The response contains:

```text
passport
protocol              # primary-thread compatibility surface
thread_protocols[]    # all Decision Threads
primary_thread_id
```

A Case Passport can carry:

```text
practice_context
problem_signature
decision_threads[]
primary_thread_id
external_actor_used
```

without replacing `citizen_problem_verbatim`.

### Initialize a multi-decision case

A caller may supply Decision Threads from the start:

```json
{
  "problem": "Product quality signals appeared while a larger production commitment and a regulated marketing claim are being considered.",
  "primary_thread_id": "td-1111111111111111",
  "decision_threads": [
    {
      "thread_id": "td-1111111111111111",
      "decision": "identify the quality cause",
      "phase": "P1",
      "unknowns": ["cause of observed quality change"]
    },
    {
      "thread_id": "td-2222222222222222",
      "decision": "check the regulated claim",
      "phase": "P3",
      "risk_profile": {"regulatory_required": true}
    },
    {
      "thread_id": "td-3333333333333333",
      "decision": "decide whether to scale production",
      "phase": "P10",
      "depends_on": ["td-1111111111111111", "td-2222222222222222"]
    }
  ]
}
```

The P10 thread is not reclassified into another phase. It is held by an explicit dependency gate until required upstream decisions close.

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

The API applies the event, increments the passport version and recompiles all Decision Threads.

### Thread-scoped events

Existing events become decision-specific when `payload.thread_id` is supplied:

```json
{
  "event_type": "RISK_UPDATED",
  "actor": "steward",
  "payload": {
    "thread_id": "td-2222222222222222",
    "risk": {"regulatory_required": true}
  }
}
```

Supported thread-scoped semantics include observations, unknowns, hypotheses, phase, risk, signatures/barriers, capability requests, institution selection, route failure, handoff, return and outcome.

Structural Decision Thread events are:

```text
DECISION_THREAD_CREATED
DECISION_THREAD_DEPENDENCIES_UPDATED
DECISION_THREAD_CANCELLED
PRIMARY_THREAD_SET
```

### Compile all threads without mutation

```text
POST /v1/cases/threads/compile
```

Request body: one caller-held Case Passport.

Response:

```text
case_id
primary_thread_id
count
thread_protocols[]
```

This is useful for AI hosts that want the full decision surface without applying a new event.

### Problem-grammar events

```text
SIGNATURE_CANDIDATES_UPDATED
SIGNATURE_ENDORSED
BARRIER_UPDATED
```

`SIGNATURE_CANDIDATES_UPDATED` must not be interpreted as a diagnosis merely because the actor is AI.

### Dependency hold

A blocked thread compiles as:

```text
next_action = HOLD
status = HOLD_FOR_DEPENDENCY
```

Hard safety/authority escalation has higher priority than an ordinary dependency hold.

### Return and closure

External institutional/expert results should arrive as `RETURN_RECEIVED` with a structured Return Object. For a Decision Thread, include `thread_id` in the event payload so the Return Gate attaches to the correct decision.

A local thread that never used an external actor may close without a fake institutional Return Object when a closure outcome is recorded and no hard safety/authority trigger remains.

A multi-decision case closes only when all required non-cancelled threads are closed and the citizen-level outcome condition is satisfied.

## Storage boundary

The API is stateless in this reference implementation. It does not retain the Case Passport between requests.

Production deployments need authenticated private case storage, access control, encryption, consent enforcement, retention/deletion policy and audit logging.
