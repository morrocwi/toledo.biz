# AGENTS.md

Rules for AI/code agents working in this repository.

## Required read order

Before making a material change, read:

1. `docs/README.md`
2. `docs/SPECIFICATION_STATUS.md`
3. `docs/GLOSSARY.md`
4. the normative document for the layer being changed
5. `docs/EQUATION_BINDINGS.md` when behavior depends on Toledo mathematics

For institution/country data, also read:

- `docs/DATA_GOVERNANCE.md`
- `docs/INSTITUTION_REGISTRY_STANDARD.md`
- `docs/COUNTRY_ADAPTER_STANDARD.md`

## 1. Authority boundaries

- `morrocwi/toledo` is the authoritative source for Toledo mathematics and equation provenance.
- Do not invent or silently modify Toledo equations in this repository.
- If an equation is missing, propose/register it upstream before treating it as canonical here.
- JSON Schemas are authoritative for machine-readable object shape.
- Country adapters are authoritative only for their own jurisdictional data, subject to provenance/freshness.

## 2. Citizen-first invariant

Every feature must preserve a path from implementation behavior back to the citizen's original problem and goal.

Do not optimize for institutional completion while losing citizen outcome.

## 3. AI role

AI is a mediator/translator/router, not a universal expert or truth authority.

AI may structure, retrieve, compare, question, hypothesize, and route.

AI may not silently satisfy professional, laboratory, regulatory, legal, or independent-validation requirements.

## 4. Hard gates

Never average a hard `FAIL` or `HOLD_UNKNOWN` into a soft readiness score.

Safety, authority, rights, consent, and required regulatory gates remain typed.

## 5. Meaning preservation

Keep separate:

```text
P_C = citizen problem verbatim
P_S = AI-structured problem
P_D = disciplinary / institutional problem
```

Never overwrite `P_C`.

## 6. Case continuity

Institution routing must carry a Case Passport.

A valid handoff requires meaning preservation, requested capability, decision owner, consent/data scope, return obligation, response-time fit, and fallback.

Do not treat a generic referral as successful handoff.

## 7. Return gate

External institutional work is incomplete until a Return Object reaches the citizen/decision owner in usable form.

## 8. Privacy

Never place real sensitive case data in this public repository.

Use synthetic fixtures. Public issues are not a citizen case store.

## 9. Institution freshness

Never assert current program availability without evidence appropriate to that claim.

Preserve `unknown` when availability, timing, price, eligibility, or accreditation cannot be confirmed.

Every institution record needs a public source and `last_verified` date; mature records should use verification metadata.

## 10. Data provenance

Do not collapse:

```text
institution identity
service availability
legal authority
accreditation
eligibility
operational capacity
```

They may require different sources and different verification dates.

## 11. Global core / local adapters

Keep jurisdiction-neutral logic out of country-specific adapter code where possible.

Country adapters may specialize institutions, laws, regulators, standards, language, and access constraints.

If a local case reveals a missing universal concept, propose a global-core change rather than hard-coding a country workaround into core semantics.

## 12. No forced innovation or entrepreneurship

A correct local fix is a valid terminal state.

A useful innovation need not become a founder-operated startup.

## 13. Architecture decisions

Changes to architecture anchors require an ADR under `docs/adr/`.

Do not silently change:

```text
repository authority
Case Passport semantics
Return Gate semantics
hard-gate semantics
P0-P11 meaning
global/local boundary
rights decomposition
meaning-preservation rule
```

## 14. Tests for routing changes

Any routing change should test at least:

- low-risk citizen+AI-only path;
- hard escalation path;
- `HOLD_UNKNOWN` path;
- inaccessible/ineligible institution fallback;
- response-time failure;
- meaning-preservation failure;
- consent/data-scope failure;
- return-gate failure;
- no-restart rerouting;
- non-founder utilization route where relevant.

## 15. Documentation discipline

Prefer one primary definition per concept. Link to the authoritative definition instead of creating competing versions.

When adding time-sensitive facts, include source and verification metadata.

## 16. Change hygiene

For material changes:

- update `CHANGELOG.md`;
- update status/version docs if contract maturity changes;
- validate schemas/datasets;
- preserve backward compatibility or document migration;
- never fabricate a release/version or canonical equation status.
