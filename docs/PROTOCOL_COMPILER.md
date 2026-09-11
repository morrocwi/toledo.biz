# Toledo Protocol Compiler v0.4

Status: **reference implementation / pre-alpha**.

The compiler turns a decision state into the smallest relevant executable subgraph of Toledo, while the Case Passport preserves one citizen case across several concurrent decisions.

```text
Citizen Input
    → Case Passport
    → Candidate Problem Signature(s)
    → Problem / Barrier State
    → Decision Thread(s)
    → Protocol Compiler
    → Minimal Relevant Subgraph per active decision
    → Next Action
    → World / Institution
    → Case Event / Return Object
    → Updated Case Passport
    → Recompile all threads
```

It is deliberately not a P0→P11 conveyor belt. A Decision Thread may stop successfully at any appropriate phase, and one case may contain threads at different phases simultaneously.

## Design rule

```text
AI interprets
Protocol engine controls typed gates
Case Passport preserves continuity
Decision Threads preserve concurrent decisions
Problem Signature remains a readout, not a diagnosis
```

The reference compiler is deterministic. It does not permit an LLM to silently override hard safety, authority, consent, rights, dependency, or Return Gate semantics.

## Domain-neutral problem grammar

The compiler does not branch by occupation or industry.

```text
Occupation != ProtocolSelector
Industry != ProtocolSelector
```

Occupation, practice history and situated expertise remain available as `practice_context`, but core routing is driven by the current problem state, evidence need, barriers, risk, authority need, capability need, dependencies and jurisdiction.

AI may provide several candidate problem signatures. Candidates retain provenance and may remain `HOLD_UNKNOWN`. A candidate signature is not automatically a diagnosis or an endorsed fact.

See [`PROBLEM_CAPABILITY_GRAMMAR.md`](PROBLEM_CAPABILITY_GRAMMAR.md).

## Decision Thread compilation

A Case Passport may contain:

```text
decision_threads[]
primary_thread_id
```

Each thread is compiled separately through the same P0-P11 action logic.

```text
Case
  ├── T1 -> compile_protocol(T1)
  ├── T2 -> compile_protocol(T2)
  └── T3 -> compile_protocol(T3)
```

`step_case()` returns:

```text
protocol            # primary-thread compatibility surface
thread_protocols[]  # protocol instance for every Decision Thread
```

The original fields remain compatible:

```text
current_phase    = primary_thread.phase
current_decision = primary_thread.decision
```

See [`DECISION_THREADS.md`](DECISION_THREADS.md).

## Dependency gate

A Decision Thread may depend on other threads.

If any declared dependency is unresolved:

```text
thread.status = BLOCKED
next_action = HOLD
status = HOLD_FOR_DEPENDENCY
```

`HOLD` is an implementation action, not a newly claimed Toledo equation.

Hard safety/authority escalation remains higher priority:

```text
HardSafetyEscalation > DependencyHold
```

This allows, for example, a P10 scale decision to wait for P1 quality evidence and P3 regulatory review without rewriting phase semantics.

## Stateless reference architecture

The public reference runtime does not persist real citizen cases. The caller stores the Case Passport and sends it back on the next step.

```text
POST /v1/cases/step
    input: case OR passport + optional event(s)
    output: updated passport + primary protocol + thread_protocols[]
```

This makes the lifecycle executable without turning the public repository into a sensitive citizen-data store.

Production deployments need private persistence, access control, encryption, retention/deletion controls, consent enforcement, and audit policy.

## Core actions

```text
OBSERVE
STRUCTURE
MEASURE
ESCALATE
HOLD
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

`HOLD` means the current decision is not yet executable because a declared dependency remains unresolved.

`STOP` is emitted only after the relevant thread/case closure state is recorded. Closure is not inferred from institutional completion alone.

## Case lifecycle functions

The reference runtime exposes:

```text
create_case_passport(case)
apply_case_event(passport, event)
compile_decision_threads(passport)
step_case(payload)
```

`step_case` is the closed-loop entry point.

See `docs/CASE_LIFECYCLE.md`.

## P_C immutability

The original citizen problem is stored as:

```text
P_C = citizen_problem_verbatim
```

A normal Case Event cannot overwrite it. Clarifications, candidate signatures, Decision Threads and disciplinary reframings are stored separately.

```text
P_C != P_S != P_D != ProblemSignature
DecisionThread != P_C
```

This prevents later AI or institutional language from silently replacing the citizen's original problem.

## Candidate signatures and barriers

The Case Passport or a Decision Thread may carry:

```text
problem_signature.status
problem_signature.candidate_signatures[]
problem_signature.endorsed_signature_id
problem_signature.context_known[]
problem_signature.context_unknown[]
problem_signature.barrier_state
problem_signature.domain_adapter_required
```

Reference events include:

```text
SIGNATURE_CANDIDATES_UPDATED
SIGNATURE_ENDORSED
BARRIER_UPDATED
```

These events can be scoped to a Decision Thread with `payload.thread_id` when different decisions need different working signatures.

The runtime does not infer that AI-generated candidate signatures are true. It stores and transports them with provenance for later endorsement or correction.

## Return and closure

A Return Object is evaluated against the implementation of `TCB-X005` when external contribution is used.

### Local thread closure

A thread may close without manufacturing a fake institutional Return Object when:

```text
thread.external_actor_used = false
AND thread.latest_return_gate = NOT_APPLICABLE
AND thread.outcome_state ∈ {
  resolved,
  improved,
  safely_held,
  explicitly_rescoped_with_consent
}
AND no unresolved hard safety / authority trigger remains
```

### External thread closure

When an external route was actually used:

```text
thread.external_actor_used = true
AND thread.latest_return_gate = PASS
AND thread.outcome_state ∈ {
  resolved,
  improved,
  safely_held,
  explicitly_rescoped_with_consent
}
```

### Multi-decision case closure

A multi-decision case additionally requires:

```text
all required non-cancelled Decision Threads = CLOSED
AND citizen-level closure outcome satisfied
```

before the case becomes `CLOSED`.

This operationalizes the current Toledo Citizen Closure proposal with an additive orchestration rule. It does not claim that Decision Threads are a new scientific law.

## No-restart rerouting

A failed route is recorded as a Case Event. The same Case Passport and Decision Thread are recompiled with prior problem, evidence, rights state, failed route and history intact.

```text
ROUTE_FAILED != RESTART_CASE
BlockedThread != FailedCase
```

## Hard escalation reference rule

The reference implementation escalates when any configured hard trigger is present, including professional/regulatory authority requirements or high severity/irreversibility/third-party exposure. These thresholds are implementation defaults, not universal scientific laws. Deployments must review them by domain and jurisdiction.

A domain adapter may specialize safety, authority, measurement or regulatory constraints. It must not redefine the global Case Passport, Decision Thread semantics, provenance or hard-gate semantics.

## Equation status

Citizen-bridge equations are currently bound to the upstream v0.17 proposal family unless individually promoted in `morrocwi/toledo`.

The compiler MUST disclose that status. It MUST NOT present planning heuristics, the problem grammar, Decision Threads or domain mappings as validated physical or social laws.

## Safety boundary

This implementation is a routing/protocol reference. It is not itself a medical, legal, engineering, regulatory, laboratory or other licensed professional authority.
