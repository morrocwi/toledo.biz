# AGENTS.md

Rules for AI/code agents working in this repository.

## Required read order

Before a material change, read:

1. `docs/README.md`
2. `docs/SPECIFICATION_STATUS.md`
3. `docs/GLOSSARY.md`
4. the normative document for the layer being changed
5. `docs/EQUATION_BINDINGS.md` when behavior depends on Toledo mathematics
6. `docs/PROBLEM_CAPABILITY_GRAMMAR.md` for problem abstraction, candidate signatures, barriers, capability mapping, or domain adapters
7. `docs/EXECUTION_ROUTING.md` for AI mediation, interaction-vs-field expert roles, knowledge-like/tool/authority routing, or bounded forward/world/market testing
8. `docs/DECISION_THREADS.md` for multi-decision cases, dependencies, blocking, thread-local events, or closure
9. `docs/PROTOCOL_COMPILER.md` for runtime/routing/compiler changes
10. `docs/CASE_LIFECYCLE.md` for Case Passport/event/closure changes
11. `docs/API.md` or `docs/MCP.md` when changing machine interfaces

For institution/country data, also read `docs/DATA_GOVERNANCE.md`, `docs/INSTITUTION_REGISTRY_STANDARD.md`, and `docs/COUNTRY_ADAPTER_STANDARD.md`.

## Authority boundaries

- `morrocwi/toledo` is authoritative for Toledo equations and provenance.
- `registry/equation-index.json` is a pinned read mirror only.
- Do not invent, silently modify, or promote equations in `toledo.biz`.
- JSON Schemas and OpenAPI are machine contracts for this repository.
- Accepted ADRs govern product/runtime architecture unless a later ADR explicitly supersedes them.
- Country adapters govern only their jurisdictional routing data, subject to freshness/provenance.
- Domain adapters may specialize vocabulary, hazards, measurements, professional boundaries, regulation or provider mappings; they may not redefine the global core.
- Decision Threads and Flexible Execution Routing are runtime/product architecture. Do not present them as new canonical Toledo equations or scientific laws.

## Mandatory Toledo-Genesis reuse-first gate

When work depends on mathematics, every agent MUST obey the canonical `TG-RFG-01` rule from `morrocwi/toledo/EQUATION_SOURCE_POLICY.md`:

```text
Toledo lookup
    -> Genesis compatibility
    -> reuse existing object
    -> derive only the missing piece
    -> mark PROPOSAL
```

In this repository:

- lookup and status resolution happen upstream in Toledo before a new equation binding is introduced;
- ontology/translation compatibility is checked against `morrocwi/readout_genesis` when relevant;
- existing upstream objects are reused rather than duplicated locally;
- genuinely missing mathematics stays `unbound` or `proposal` until an upstream Toledo proposal exists;
- ambiguous/superseded/conflicting lookup states are `HOLD`, never permission to invent a replacement;
- bypassing this order is `DRIFT` and must not be used to justify implementation or claim promotion.

This gate controls provenance only. It does not promote a proposal, validate a scientific law, or strengthen a claim tier.

## Citizen-first invariant

Every feature must preserve a path back to the citizen's original problem and goal. Do not optimize for institutional completion while losing citizen outcome.

## AI role

AI is mediator/translator/router, not universal expert or truth authority. AI may structure, retrieve, compare, question, hypothesize, translate and route; it may not silently satisfy professional, laboratory, regulatory, legal or independent-validation requirements.

AI-generated Problem Signatures and proposed Decision Threads are candidate translations/orchestration objects. They are not diagnoses, observations, truths, or authority merely because an AI produced them.

Execution routing MUST preserve:

```text
AI != ExpertClass
AITranslation != IndependentValidation
KnowledgeLike != HumanExpert
InteractionExpert != FieldExpert
Expertise != Authority
```

## Protocol-engine rule

```text
AI interprets and translates
Protocol engine controls typed gates
```

Hard `FAIL` or `HOLD_UNKNOWN` states must never be averaged into a soft score.

Hard safety/authority escalation must outrank an ordinary Decision Thread dependency hold.

## Domain-neutral core rule

Do not add occupation- or industry-specific branching to the core merely because a new profession or domain appears.

```text
Occupation != ProtocolSelector
Industry != ProtocolSelector
PracticeContext != IrrelevantContext
ProblemSignature != Diagnosis
CandidateSignature != EndorsedSignature
```

Preserve occupation/practice history as context when it carries experiential knowledge, constraints, tools, vocabulary or repeated observations.

Use an optional domain adapter only when safety, professional authority, specialized measurement/sample handling, regulation, high-risk terminology, or provider matching materially requires it.

## Flexible execution rule

Do not convert P0-P11 into a fixed expert/tool conveyor belt.

```text
Phase != ExpertSelector
Phase != MandatorySequence
```

A bounded reversible world or market test may occur before later expert/institution phases when no hard safety, authority, permission, credential, unresolved Return Gate, or Decision Thread dependency blocks it.

```text
ForwardExperiment != PermissionToIgnoreHardGates
MarketEntry != CaseClosure
```

When expert input is material, distinguish interaction expertise from field/front-line expertise. A single person may satisfy both roles, but the routing reason must remain explicit.

Knowledge-like material such as structured readouts, documents, standards, papers, datasets, prior cases or provisional synthesis is not a human expert and not a truth certificate.

## Multi-decision rule

Do not force a real case with several material decisions into one scalar phase.

```text
Case != SingleDecision
DecisionThread != NewCase
ThreadPhase != CaseMaturity
BlockedThread != FailedCase
ThreadClosure != CaseClosure
```

Use the existing P0-P11 coordinates **inside each Decision Thread**. Do not invent a second phase system.

Preserve backward compatibility:

```text
current_phase    = primary_thread.phase
current_decision = primary_thread.decision
```

If a thread declares `depends_on`, unresolved dependencies must appear in `blocking_threads` and must prevent downstream execution through `HOLD` / `HOLD_FOR_DEPENDENCY`, unless the thread has a hard safety/authority escalation requirement.

Before an AI agent recommends a downstream commitment such as scale, commercialization, public release, or another materially irreversible action, inspect all relevant `thread_protocols`, not only the primary thread.

## Meaning preservation

Keep separate:

```text
P_C = citizen problem verbatim
P_S = AI-structured problem
P_D = disciplinary/institutional problem
Problem Signature = routing readout
Decision Thread = one decision-specific subgraph
```

Never overwrite `P_C` through an ordinary Case Event. If a citizen genuinely corrects the original problem statement, preserve the prior representation and use an explicit migration/correction mechanism rather than silent replacement.

## Provenance and unknowns

Material Problem Signature facets should preserve provenance. Do not convert AI inference into citizen observation or world fact.

Unknown and unresolved states are valid outputs:

```text
Unknown != Failure
MissingEvidence != NegativeEvidence
UnobservedContext != AIInferredFact
```

## Closed-loop Case Passport rule

A case has a stable `case_id` and monotonic `version`.

```text
Case Passport
→ Case Event
→ next Passport version
→ recompile Decision Threads
```

A route failure must remain inside the same case and, where applicable, the same Decision Thread unless the citizen is actually starting a materially different problem.

```text
ROUTE_FAILED != RESTART_CASE
```

The public reference runtime is stateless; caller-held passports are the transport contract. Do not add public persistence for sensitive citizen data without a separate security/privacy design review.

## Case continuity

Institution routing must carry a Case Passport and the relevant Decision Thread context. A valid handoff requires meaning preservation, requested capability, decision owner, consent/data scope, return obligation, response-time fit and fallback. Do not treat a generic referral as successful handoff.

## Return Gate and closure

External institutional/professional work is incomplete until a Return Object reaches the citizen/decision owner in usable form.

Do not mark a thread or case `CLOSED` merely because a project, report, consultation or institutional task is complete.

Do not manufacture a fake institutional Return Object for a citizen+AI/world-only local thread. Local thread closure is permitted only when no external actor was used, its outcome is a closure outcome, and no unresolved hard safety/authority trigger remains. External threads still require a passing Return Gate plus thread outcome.

A multi-decision case closes only when all required non-cancelled Decision Threads are closed, the citizen-level outcome condition is satisfied, and shared hard safety/authority state is clear.

## Privacy

Never place real sensitive case data in this public repository. Use synthetic fixtures only.

## Institution freshness

Never assert current program availability without evidence appropriate to that claim. Preserve `unknown` when availability, timing, price, eligibility or accreditation cannot be confirmed.

## Global core / local adapters

Keep jurisdiction-neutral logic out of country-specific adapter code. Country adapters may specialize institutions, laws, regulators, standards, language and access constraints.

Keep domain-neutral problem/routing semantics out of occupation-specific code. Domain adapters are bounded specializations, not new cores.

## No forced innovation or entrepreneurship

A correct local fix is a valid terminal state. A useful innovation need not become a founder-operated startup. A P10/P11 thread must not pull unrelated unresolved P1/P3 decisions forward merely because the business is mature elsewhere.

A bounded market test is allowed to generate world evidence when gates permit it, but a transaction does not prove that unrelated safety, rights, regulatory, quality or scale decisions are solved.

## Runtime changes

Any compiler/routing/case-lifecycle change should test at least:

- low-risk citizen+AI path;
- hard escalation path;
- hard escalation precedence over ordinary dependency hold;
- Case Passport schema validity;
- Decision Thread schema validity when relevant;
- Problem Signature schema validity when relevant;
- Execution Routing schema validity when relevant;
- AI mediator/translator role remains distinct from expert/authority when relevant;
- interaction-vs-field expert distinction when relevant;
- bounded forward/world/market route remains available in a reversible low-gate case when relevant;
- forward route is blocked by hard safety/authority gates when relevant;
- monotonic version update;
- `P_C` preservation;
- primary-thread projection compatibility;
- candidate signature provenance/endorsement behavior when relevant;
- inaccessible/ineligible institution fallback;
- no-restart rerouting;
- Return Gate behavior;
- local citizen-only/thread-only closure where relevant;
- external-route closure requiring Return Gate;
- multi-decision dependency blocking and release;
- multi-decision case closure requiring all required threads;
- at least one cross-domain invariance case where occupation/industry changes but the same structural problem does not create bespoke core branching;
- equation provenance/status disclosure.

Machine interfaces MUST expose equation references rather than copy equations as local authority.

## Change hygiene

For material changes update `CHANGELOG.md`, validate schemas/data, preserve backward compatibility or document migration, and never fabricate a release or canonical equation status.
