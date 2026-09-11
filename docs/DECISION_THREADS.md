# Toledo Decision Threads v0.1

Status: **normative additive runtime contract / pre-alpha**.

Decision Threads extend the existing Case Passport without replacing any Toledo anchors.

## 1. Why threads exist

A real citizen or business case can contain several simultaneous decisions that belong to different Toledo routing phases.

```text
Case != SingleDecision
```

Example:

```text
quality cause          -> P1
specialist testing     -> P3
regulatory claim       -> regulatory overlay / P3-P5
scale commitment       -> P10
```

Collapsing these into one `current_phase` destroys information. Creating a bespoke industry protocol causes domain explosion. Decision Threads preserve both the global core and the original phase system.

## 2. Anchor-preserving model

The Case Passport remains the stable case identity and still owns:

```text
P_C
citizen goal
shared context
consent / rights
case steward
case history
```

It now may contain:

```text
decision_threads[]
primary_thread_id
```

Each thread carries one decision-specific subgraph:

```text
DECISION_THREAD = {
  thread_id,
  decision,
  phase,
  status,
  problem_signature,
  observations,
  unknowns,
  hypotheses,
  risk_profile,
  requested_capability,
  depends_on,
  blocking_threads,
  external_actor_used,
  latest_return_gate,
  outcome_state
}
```

The machine contract is `packages/schemas/decision-thread.schema.json`.

## 3. Backward compatibility

Existing fields are preserved as a projection of the primary thread:

```text
current_phase    := primary_thread.phase
current_decision := primary_thread.decision
```

A legacy case that provides no `decision_threads` receives one automatically created primary thread. Existing single-decision callers therefore keep the old behavior.

## 4. Dependency semantics

A thread can depend on other threads:

```text
T_scale.depends_on = [T_quality, T_regulatory]
```

The runtime calculates:

```text
blocking_threads = {
  dependency | dependency.status not in {CLOSED, CANCELLED}
}
```

If blockers exist, the dependent thread is `BLOCKED` and its compiled action is `HOLD` unless its own hard safety/authority gate requires escalation first.

```text
DependencyHold < HardSafetyEscalation
```

A blocked thread is not a failed case.

## 5. Thread-local events

Existing Case Events can be scoped to a thread by putting `thread_id` in the event payload. The semantic meaning of the event does not change.

Examples:

```text
PHASE_CHANGED + thread_id
RISK_UPDATED + thread_id
OBSERVATION_ADDED + thread_id
UNKNOWN_ADDED + thread_id
CAPABILITY_REQUESTED + thread_id
INSTITUTION_SELECTED + thread_id
ROUTE_FAILED + thread_id
RETURN_RECEIVED + thread_id
OUTCOME_UPDATED + thread_id
```

Additional structural events are:

```text
DECISION_THREAD_CREATED
DECISION_THREAD_DEPENDENCIES_UPDATED
DECISION_THREAD_CANCELLED
PRIMARY_THREAD_SET
```

A thread-scoped event MUST NOT silently overwrite `P_C` or create a new case.

## 6. Thread closure

A decision thread closes under the same core distinction already used by Toledo:

```text
local route:
  external_actor_used = false
  hard risk cleared
  outcome in closure outcomes
  -> thread CLOSED

external route:
  external_actor_used = true
  latest_return_gate = PASS
  outcome in closure outcomes
  -> thread CLOSED
```

No fake Return Object is created for a local-only thread.

## 7. Case closure

Thread closure and case closure are separate.

For multi-decision cases:

```text
RequiredThreadsClosed = TRUE
iff every required non-cancelled thread is CLOSED
```

Citizen-level closure then requires both:

```text
RequiredThreadsClosed = TRUE
AND
citizen outcome satisfies the existing closure condition
```

This prevents a scale decision from closing a case while a required safety or regulatory decision is unresolved.

## 8. Compiler output

`step_case()` returns:

```text
passport
protocol            # primary-thread protocol, backward-compatible
thread_protocols[]  # protocol for every Decision Thread
```

The primary protocol remains the compatibility surface. New agents SHOULD inspect all `thread_protocols` before recommending a material decision.

## 9. Domain-neutrality

Decision Threads do not encode occupations or industries.

A cosmetics business, mushroom farm, school, software team or machine shop can all use the same model:

```text
Problem
-> several decisions
-> several phase-specific subgraphs
-> dependencies
-> capabilities
-> providers / world checks only when required
```

Domain adapters may add legal, safety, measurement or provider constraints. They MUST NOT redefine Decision Thread semantics.

## 10. Non-collapse rules

```text
Case != SingleDecision
DecisionThread != NewCase
ThreadPhase != CaseMaturity
BlockedThread != FailedCase
ThreadClosure != CaseClosure
PrimaryThread != MostImportantTruth
Occupation != ThreadSelector
```

## 11. Current limits

The reference implementation is intentionally conservative. It does not yet infer threads from natural language automatically. AI may propose candidate threads, but the runtime governs thread identity, dependency state, hard gates, Return Gate behavior and closure.
