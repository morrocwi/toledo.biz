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
7. `docs/PROTOCOL_COMPILER.md` for runtime/routing/compiler changes
8. `docs/CASE_LIFECYCLE.md` for Case Passport/event/closure changes
9. `docs/API.md` or `docs/MCP.md` when changing machine interfaces

For institution/country data, also read `docs/DATA_GOVERNANCE.md`, `docs/INSTITUTION_REGISTRY_STANDARD.md`, and `docs/COUNTRY_ADAPTER_STANDARD.md`.

## Authority boundaries

- `morrocwi/toledo` is authoritative for Toledo equations and provenance.
- `registry/equation-index.json` is a pinned read mirror only.
- Do not invent, silently modify, or promote equations in `toledo.biz`.
- JSON Schemas and OpenAPI are machine contracts for this repository.
- Country adapters govern only their jurisdictional routing data, subject to freshness/provenance.
- Domain adapters may specialize vocabulary, hazards, measurements, professional boundaries, regulation or provider mappings; they may not redefine the global core.

## Citizen-first invariant

Every feature must preserve a path back to the citizen's original problem and goal. Do not optimize for institutional completion while losing citizen outcome.

## AI role

AI is mediator/translator/router, not universal expert or truth authority. AI may structure, retrieve, compare, question, hypothesize and route; it may not silently satisfy professional, laboratory, regulatory, legal or independent-validation requirements.

AI-generated Problem Signatures are candidate translations. They are not diagnoses, observations, or truth merely because an AI produced them.

## Protocol-engine rule

```text
AI interprets
Protocol engine controls typed gates
```

Hard `FAIL` or `HOLD_UNKNOWN` states must never be averaged into a soft score.

## Domain-neutral core rule

Do not add occupation-specific branching to the core merely because a new profession or domain appears.

```text
Occupation != ProtocolSelector
PracticeContext != IrrelevantContext
ProblemSignature != Diagnosis
CandidateSignature != EndorsedSignature
```

Preserve occupation/practice history as context when it carries experiential knowledge, constraints, tools, vocabulary or repeated observations.

Use an optional domain adapter only when safety, professional authority, specialized measurement/sample handling, regulation, high-risk terminology, or provider matching materially requires it.

## Meaning preservation

Keep separate:

```text
P_C = citizen problem verbatim
P_S = AI-structured problem
P_D = disciplinary/institutional problem
Problem Signature = routing readout
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
→ Protocol recompile
```

A route failure must remain inside the same case unless the citizen is actually starting a materially different problem.

```text
ROUTE_FAILED != RESTART_CASE
```

The public reference runtime is stateless; caller-held passports are the transport contract. Do not add public persistence for sensitive citizen data without a separate security/privacy design review.

## Case continuity

Institution routing must carry a Case Passport. A valid handoff requires meaning preservation, requested capability, decision owner, consent/data scope, return obligation, response-time fit and fallback. Do not treat a generic referral as successful handoff.

## Return Gate and closure

External institutional/professional work is incomplete until a Return Object reaches the citizen/decision owner in usable form.

Do not mark a case `CLOSED` merely because a project, report, consultation or institutional task is complete.

Do not manufacture a fake institutional Return Object for a citizen+AI/world-only local case. Local closure is permitted only when no external actor was used, the citizen outcome is a closure outcome, and no unresolved hard safety/authority trigger remains. External routes still require a passing Return Gate plus citizen outcome before `STOP`.

## Privacy

Never place real sensitive case data in this public repository. Use synthetic fixtures only.

## Institution freshness

Never assert current program availability without evidence appropriate to that claim. Preserve `unknown` when availability, timing, price, eligibility or accreditation cannot be confirmed.

## Global core / local adapters

Keep jurisdiction-neutral logic out of country-specific adapter code. Country adapters may specialize institutions, laws, regulators, standards, language and access constraints.

Keep domain-neutral problem/routing semantics out of occupation-specific code. Domain adapters are bounded specializations, not new cores.

## No forced innovation or entrepreneurship

A correct local fix is a valid terminal state. A useful innovation need not become a founder-operated startup.

## Runtime changes

Any compiler/routing/case-lifecycle change should test at least:

- low-risk citizen+AI path;
- hard escalation path;
- Case Passport schema validity;
- Problem Signature schema validity when relevant;
- monotonic version update;
- `P_C` preservation;
- candidate signature provenance/endorsement behavior when relevant;
- inaccessible/ineligible institution fallback;
- no-restart rerouting;
- Return Gate behavior;
- local citizen-only closure where relevant;
- external-route closure requiring Return Gate;
- at least one cross-domain invariance case where occupation changes but the same structural problem does not create bespoke core branching;
- equation provenance/status disclosure.

Machine interfaces MUST expose equation references rather than copy equations as local authority.

## Change hygiene

For material changes update `CHANGELOG.md`, validate schemas/data, preserve backward compatibility or document migration, and never fabricate a release or canonical equation status.
