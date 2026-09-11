# AGENTS.md

Rules for AI/code agents working in this repository.

## 1. Authority boundaries

- `morrocwi/toledo` is the authoritative source for Toledo mathematics and equation provenance.
- Do not invent or silently modify Toledo equations in this repository.
- If an equation is missing, mark the need and propose it upstream in `morrocwi/toledo` before treating it as canonical here.

## 2. Citizen-first invariant

Every feature must preserve a path from implementation behavior back to the citizen's original problem and goal.

Do not optimize for institutional completion while losing citizen outcome.

## 3. AI role

AI is a mediator/translator/router, not a universal expert or truth authority.

AI may structure, retrieve, compare, question, and route.

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

A valid handoff requires meaning preservation, capability request, decision owner, consent/data scope, return obligation, response-time fit, and fallback.

## 7. Return gate

External institutional work is incomplete until a Return Object reaches the citizen/decision owner in usable form.

## 8. Privacy

Never place real sensitive case data in this public repository.

Use synthetic fixtures.

## 9. Institution freshness

Never assert current program availability without a current public source and `last_verified` date.

## 10. Global core / local adapters

Keep jurisdiction-neutral logic out of country-specific adapter code where possible.

Country adapters may specialize institutions, laws, regulators, language, and access constraints.

## 11. No forced innovation or entrepreneurship

A correct local fix is a valid terminal state.

A useful innovation need not become a founder-operated startup.

## 12. Tests for routing changes

Any routing change should test at least:

- low-risk citizen+AI-only path;
- hard escalation path;
- inaccessible institution fallback;
- response-time failure;
- meaning-preservation failure;
- return-gate failure;
- non-founder utilization route where relevant.
