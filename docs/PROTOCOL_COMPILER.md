# Toledo Protocol Compiler v0.3

Status: **reference implementation / pre-alpha**.

The compiler turns a Case State into the smallest relevant executable subgraph of Toledo, then supports an auditable loop back into the same Case Passport.

```text
Citizen Input
    → Case Passport
    → Candidate Problem Signature(s)
    → Problem / Barrier State
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
Problem Signature remains a readout, not a diagnosis
```

The reference compiler is deterministic. It does not permit an LLM to silently override hard safety, authority, consent, rights or Return Gate semantics.

## Domain-neutral problem grammar

The compiler does not branch by occupation.

```text
Occupation != ProtocolSelector
```

Occupation, practice history and situated expertise remain available as `practice_context`, but core routing is driven by the current problem state, evidence need, barriers, risk, authority need, capability need and jurisdiction.

AI may provide several candidate problem signatures. Candidates retain provenance and may remain `HOLD_UNKNOWN`. A candidate signature is not automatically a diagnosis or an endorsed fact.

See [`PROBLEM_CAPABILITY_GRAMMAR.md`](PROBLEM_CAPABILITY_GRAMMAR.md).

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

These runtime action labels are operational primitives. They are not claims that every real-world problem belongs to one metaphysical category.

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

A normal Case Event cannot overwrite it. Clarifications, candidate signatures and disciplinary reframings are stored separately.

```text
P_C != P_S != P_D != ProblemSignature
```

This prevents later AI or institutional language from silently replacing the citizen's original problem.

## Candidate signatures and barriers

The Case Passport may carry:

```text
problem_signature.status
problem_signature.candidate_signatures[]
problem_signature.endorsed_signature_id
problem_signature.context_known[]
problem_signature.context_unknown[]
problem_signature.barrier_state
problem_signature.domain_adapter_required
```

New reference events include:

```text
SIGNATURE_CANDIDATES_UPDATED
SIGNATURE_ENDORSED
BARRIER_UPDATED
```

The runtime does not infer that AI-generated candidate signatures are true. It stores and transports them with provenance for later endorsement or correction.

## Return and closure

A Return Object is evaluated against the implementation of `TCB-X005` when external contribution is used.

The lifecycle distinguishes two closure paths.

### Local citizen+AI/world closure

A case may close without manufacturing a fake institutional Return Object when:

```text
external_actor_used = false
AND latest_return_gate = NOT_APPLICABLE
AND outcome_state ∈ {
  resolved,
  improved,
  safely_held,
  explicitly_rescoped_with_consent
}
AND no unresolved hard safety / authority trigger remains
```

### External-route closure

When an external institution/expert route was actually used:

```text
external_actor_used = true
AND latest_return_gate = PASS
AND outcome_state ∈ {
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

A domain adapter may specialize safety, authority, measurement or regulatory constraints. It must not redefine the global Case Passport, provenance or hard-gate semantics.

## Equation status

Citizen-bridge equations are currently bound to the upstream v0.17 proposal family unless individually promoted in `morrocwi/toledo`.

The compiler MUST disclose that status. It MUST NOT present planning heuristics, the problem grammar, or domain mappings as validated physical or social laws.

## Safety boundary

This implementation is a routing/protocol reference. It is not itself a medical, legal, engineering, regulatory, laboratory or other licensed professional authority.
