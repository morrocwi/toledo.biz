# Toledo Case Lifecycle v0.2

Status: **normative reference contract for the pre-alpha runtime**.

This document defines how one citizen case remains the same case across AI, field observation, experts, universities, public services, regulators and return-to-citizen.

## 1. Core loop

```text
Citizen Problem
    ↓
Create Case Passport
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
Return Gate + Citizen Outcome
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
```

but:

```text
P_C != P_S != P_D
```

and the three representations remain traceable.

## 4. Event vocabulary

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
CAPABILITY_REQUESTED
INSTITUTION_SELECTED
ROUTE_FAILED
HANDOFF_CHECKED
RETURN_RECEIVED
OUTCOME_UPDATED
NOTE
```

Country/domain adapters MAY extend local event semantics, but MUST NOT silently change the meaning of these global event names.

## 5. Risk updates

`RISK_UPDATED` changes the current risk profile and forces the next compile to reconsider hard escalation.

The reference thresholds are implementation defaults only.

Hard gate state is never averaged into a soft route score.

## 6. Route failure

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
observations
unknowns
rights state
history
```

The next compile reroutes from the same Case Passport.

## 7. Return Object

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

## 8. Closure

Institutional completion alone cannot close a case.

The reference lifecycle uses:

```text
latest_return_gate = PASS
AND
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

## 9. Reopening

A production implementation SHOULD reopen a closed case only when a material new trigger appears, for example:

```text
problem recurrence
new harm signal
new evidence
regulatory change
citizen requests a new decision
```

The reference runtime currently leaves reopening to the caller rather than silently reopening a closed case.

## 10. Stateless public runtime

The public reference API/MCP server is stateless by design.

```text
caller stores passport
caller sends passport back
runtime returns next version
```

This is not a claim that production systems should lack persistence. It prevents the public reference repository from becoming an accidental sensitive-data service.

## 11. Audit invariant

For any material case transition, an auditor should be able to answer:

```text
What changed?
Who supplied the change?
Which Case Passport version resulted?
Which Toledo equations/predicates informed the next action?
Why was the next route selected?
What must return to the citizen?
```

## 12. Non-collapse rules

```text
Case Event != Truth
Return Object != Independent Validation
Institutional Output != Citizen Outcome
Route Failure != Case Failure
Case Closure != Innovation Success
Citizen Success != Entrepreneurship
```
