# Toledo Protocol Compiler v0.2

Status: **reference implementation / pre-alpha**.

The compiler turns a Case State into the smallest relevant executable subgraph of Toledo, then supports an auditable loop back into the same Case Passport.

```text
Citizen Input
    → Case Passport
    → Protocol Compiler
    → Minimal Relevant Subgraph
    → Next Action
    → World / Institution
    → Case Event / Return Object
    → Updated Case Passport
    → Recompile
```

It is deliberately not a P0→P11 conveyor belt. A case may stop successfully at any appropriate phase.

## Design rule

```text
AI interprets
Protocol engine controls typed gates
Case Passport preserves continuity
```

The reference compiler is deterministic. It does not permit an LLM to silently override hard safety, authority, consent, rights or Return Gate semantics.

## Stateless reference architecture

The public reference runtime does not persist real citizen cases. The caller stores the Case Passport and sends it back on the next step.

```text
POST /v1/cases/step
    input: case OR passport + optional event(s)
    output: updated passport + next protocol instance
```

This makes the lifecycle executable without turning the public repository into a sensitive citizen-data store.

Production deployments need private persistence, access control, encryption, retention/deletion controls, consent enforcement, and audit policy.

## Core actions

```text
OBSERVE
STRUCTURE
MEASURE
ESCALATE
ACT
TEST
CHECK_PRIOR_ART
MAP_RIGHTS
SELECT_ROUTE
FORM_BUSINESS_0
CLOSE_FIRST_CYCLE
SCALE_CHECK
GLOBAL_CHECK
RETURN
STOP
```

`STOP` is emitted only after the Case Passport records citizen closure. Closure is not inferred from institutional completion alone.

## Case lifecycle functions

The reference runtime exposes:

```text
create_case_passport(case)
apply_case_event(passport, event)
step_case(payload)
```

`step_case` is the closed-loop entry point.

See `docs/CASE_LIFECYCLE.md`.

## P_C immutability

The original citizen problem is stored as:

```text
P_C = citizen_problem_verbatim
```

A normal Case Event cannot overwrite it. Clarifications or disciplinary reframings are stored separately.

```text
P_C != P_S != P_D
```

This prevents later institutional language from silently replacing the citizen's original problem.

## Return and closure

A Return Object is evaluated against the implementation of `TCB-X005`.

A case is marked `CLOSED` only when:

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

The compiler then emits:

```text
status = CLOSED
next_action = STOP
```

This operationalizes the current `TCB-X008` Citizen Closure proposal without treating it as a validated universal law.

## No-restart rerouting

A failed route is recorded as a Case Event. The same Case Passport is recompiled with its prior problem, evidence, rights state, failed route and history intact.

```text
ROUTE_FAILED
    !=
RESTART_CASE
```

## Hard escalation reference rule

The reference implementation escalates when any configured hard trigger is present, including professional/regulatory authority requirements or high severity/irreversibility/third-party exposure. These thresholds are implementation defaults, not universal scientific laws. Deployments must review them by domain and jurisdiction.

## Equation status

Citizen-bridge equations are currently bound to the upstream v0.17 proposal family unless individually promoted in `morrocwi/toledo`.

The compiler MUST disclose that status. It MUST NOT present planning heuristics as validated physical or social laws.

## Safety boundary

This implementation is a routing/protocol reference. It is not itself a medical, legal, engineering, regulatory, laboratory or other licensed professional authority.
