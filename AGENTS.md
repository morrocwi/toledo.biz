# AGENTS.md

Rules for AI/code agents working in this repository.

## Required read order

Before a material change, read:

1. `docs/README.md`
2. `docs/SPECIFICATION_STATUS.md`
3. `docs/GLOSSARY.md`
4. the normative document for the layer being changed
5. `docs/EQUATION_BINDINGS.md` when behavior depends on Toledo mathematics
6. `docs/PROTOCOL_COMPILER.md` for runtime/routing/compiler changes
7. `docs/CASE_LIFECYCLE.md` for Case Passport/event/closure changes
8. `docs/API.md` or `docs/MCP.md` when changing machine interfaces

For institution/country data, also read `docs/DATA_GOVERNANCE.md`, `docs/INSTITUTION_REGISTRY_STANDARD.md`, and `docs/COUNTRY_ADAPTER_STANDARD.md`.

## Authority boundaries

- `morrocwi/toledo` is authoritative for Toledo equations and provenance.
- `registry/equation-index.json` is a pinned read mirror only.
- Do not invent, silently modify, or promote equations in `toledo.biz`.
- JSON Schemas and OpenAPI are machine contracts for this repository.
- Country adapters govern only their jurisdictional routing data, subject to freshness/provenance.

## Citizen-first invariant

Every feature must preserve a path back to the citizen's original problem and goal. Do not optimize for institutional completion while losing citizen outcome.

## AI role

AI is mediator/translator/router, not universal expert or truth authority. AI may structure, retrieve, compare, question, hypothesize and route; it may not silently satisfy professional, laboratory, regulatory, legal or independent-validation requirements.

## Protocol-engine rule

```text
AI interprets
Protocol engine controls typed gates
```

Hard `FAIL` or `HOLD_UNKNOWN` states must never be averaged into a soft score.

## Meaning preservation

Keep separate:

```text
P_C = citizen problem verbatim
P_S = AI-structured problem
P_D = disciplinary/institutional problem
```

Never overwrite `P_C` through an ordinary Case Event. If a citizen genuinely corrects the original problem statement, preserve the prior representation and use an explicit migration/correction mechanism rather than silent replacement.

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

External institutional work is incomplete until a Return Object reaches the citizen/decision owner in usable form.

Do not mark a case `CLOSED` merely because a project, report, consultation or institutional task is complete. The reference runtime requires a passing Return Gate plus an explicit citizen outcome state before emitting `STOP`.

## Privacy

Never place real sensitive case data in this public repository. Use synthetic fixtures only.

## Institution freshness

Never assert current program availability without evidence appropriate to that claim. Preserve `unknown` when availability, timing, price, eligibility or accreditation cannot be confirmed.

## Global core / local adapters

Keep jurisdiction-neutral logic out of country-specific adapter code. Country adapters may specialize institutions, laws, regulators, standards, language and access constraints.

## No forced innovation or entrepreneurship

A correct local fix is a valid terminal state. A useful innovation need not become a founder-operated startup.

## Runtime changes

Any compiler/routing/case-lifecycle change should test at least:

- low-risk citizen+AI path;
- hard escalation path;
- Case Passport schema validity;
- monotonic version update;
- `P_C` preservation;
- inaccessible/ineligible institution fallback;
- no-restart rerouting;
- Return Gate behavior;
- citizen closure / `STOP` behavior;
- equation provenance/status disclosure.

Machine interfaces MUST expose equation references rather than copy equations as local authority.

## Change hygiene

For material changes update `CHANGELOG.md`, validate schemas/data, preserve backward compatibility or document migration, and never fabricate a release or canonical equation status.
