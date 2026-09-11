# Toledo Case Lifecycle v0.3

Status: **normative reference contract for the pre-alpha runtime**.

This document defines how one citizen case remains the same case across AI, field observation, experts, universities, public services, regulators and return-to-citizen.

## 1. Core loop

```text
Citizen Problem
    ↓
Create Case Passport
    ↓
Candidate Problem Signature(s) / Barrier State
    ↓
Compile Next Action
    ↓
World / Human / Institution
    ↓
Record Case Event
    ↓
Update Case Passport Version
    ↓
Recompile
    ↓
...
    ↓
Citizen Outcome (+ Return Gate when external work was used)
    ↓
CLOSED / STOP
```

The system is event-driven rather than stage-driven.

## 2. Identity and versioning

A case has a stable:

```text
case_id
```

and a monotonically increasing:

```text
version
```

Every accepted event creates the next Case Passport version.

A reroute MUST NOT create a new case solely because one institution is unavailable.

## 3. Original problem preservation

The citizen's original wording is:

```text
P_C = citizen_problem_verbatim
```

Normal events MUST NOT overwrite `P_C`.

AI and institutions may add:

```text
P_S = ai_structured_problem
P_D = disciplinary_problem
ProblemSignature = candidate/endorsed routing readout
```

but:

```text
P_C != P_S != P_D != ProblemSignature
```

and the representations remain traceable.

## 4. Problem Signature and practice context

The Case Passport may carry a domain-neutral Problem Signature with multiple candidates, facet-level provenance, known/unknown context, barrier state, optional domain-adapter need, and an endorsed signature only when endorsement is actually recorded.

Occupation or practice history may be stored in:

```text
practice_context
```

but it MUST NOT silently select a bespoke core protocol.

```text
Occupation != ProtocolSelector
```

See [`PROBLEM_CAPABILITY_GRAMMAR.md`](PROBLEM_CAPABILITY_GRAMMAR.md).

## 5. Event vocabulary

Reference event types:

```text
OBSERVATION_ADDED
UNKNOWN_ADDED
UNKNOWN_RESOLVED
HYPOTHESIS_ADDED
ACTION_RECORDED
RESULT_RECORDED
RISK_UPDATED
PHASE_CHANGED
GOAL_CONFIRMED
STRUCTURED_PROBLEM_UPDATED
DISCIPLINARY_PROBLEM_UPDATED
SIGNATURE_CANDIDATES_UPDATED
SIGNATURE_ENDORSED
BARRIER_UPDATED
CAPABILITY_REQUESTED
INSTITUTION_SELECTED
ROUTE_FAILED
HANDOFF_CHECKED
RETURN_RECEIVED
OUTCOME_UPDATED
NOTE
```

Country/domain adapters MAY extend local event semantics, but MUST NOT silently change the meaning of these global event names.

## 6. Candidate signature state

`SIGNATURE_CANDIDATES_UPDATED` records candidate translations without promoting them to diagnosis or fact.

`SIGNATURE_ENDORSED` records the selected working signature and citizen endorsement.

`BARRIER_UPDATED` updates one of the reference barrier dimensions:

```text
knowledge
skill
language
tool
resource_time
network
credential
permission
opportunity
unknown
```

with states:

```text
PRESENT
ABSENT
UNKNOWN
```

Unknown is a legitimate state.

## 7. Risk updates

`RISK_UPDATED` changes the current risk profile and forces the next compile to reconsider hard escalation.

The reference thresholds are implementation defaults only.

Hard gate state is never averaged into a soft route score.

## 8. Route failure

`ROUTE_FAILED` records:

```text
institution / route
reason
fallback if known
```

while preserving:

```text
case_id
P_C
Problem Signature
observations
unknowns
rights state
history
```

The next compile reroutes from the same Case Passport.

## 9. External-actor state

The lifecycle records:

```text
external_actor_used
```

This becomes `true` when an external institution/provider is selected or an external Return Object is received.

This state prevents two opposite errors:

```text
forcing a fake external return onto a local citizen+AI case
```

and:

```text
allowing an externally routed case to close without returning usable results
```

## 10. Return Object

External work returns through a structured Return Object containing at minimum:

```text
plain-language result
what is known
what is unknown
recommended next action
return gate state
```

The reference runtime independently computes the implementation checks for `TCB-X005`.

A declared `PASS` does not override failed machine checks.

## 11. Closure

Institutional completion alone cannot close a case.

### Local closure

When no external actor was used, the case may close without an artificial institutional Return Object when:

```text
external_actor_used = false
latest_return_gate = NOT_APPLICABLE
outcome_state ∈ {
    resolved,
    improved,
    safely_held,
    explicitly_rescoped_with_consent
}
no unresolved hard safety/authority trigger remains
```

### External-route closure

When an external actor was used:

```text
external_actor_used = true
latest_return_gate = PASS
outcome_state ∈ {
    resolved,
    improved,
    safely_held,
    explicitly_rescoped_with_consent
}
```

before setting:

```text
case_status = CLOSED
```

The Protocol Compiler then emits `STOP`.

This is an implementation of the current Toledo Citizen Closure proposal, not a claim that one scalar rule captures every real-world definition of success.

## 12. Reopening

A production implementation SHOULD reopen a closed case only when a material new trigger appears, for example:

```text
problem recurrence
new harm signal
new evidence
regulatory change
citizen requests a new decision
```

The reference runtime currently leaves reopening to the caller rather than silently reopening a closed case.

## 13. Stateless public runtime

The public reference API/MCP server is stateless by design.

```text
caller stores passport
caller sends passport back
runtime returns next version
```

This is not a claim that production systems should lack persistence. It prevents the public reference repository from becoming an accidental sensitive-data service.

## 14. Audit invariant

For any material case transition, an auditor should be able to answer:

```text
What changed?
Who supplied the change?
Which distinction came from citizen, AI, world evidence, or external return?
Which Case Passport version resulted?
Which Toledo equations/predicates informed the next action?
Why was the next route selected?
What must return to the citizen?
```

## 15. Non-collapse rules

```text
Case Event != Truth
Problem Signature != Diagnosis
Candidate Signature != Endorsed Signature
Occupation != Protocol Selector
Return Object != Independent Validation
Institutional Output != Citizen Outcome
Route Failure != Case Failure
Case Closure != Innovation Success
Citizen Success != Entrepreneurship
```
