# ADR-0003 — Global Core with Local Country Adapters

- Status: Accepted
- Date: 2026-09-11

## Context

Toledo is intended for citizens across jurisdictions, but institutions, regulators, public programs, languages, service access, professional authority, and legal requirements vary by country and region.

Embedding Thailand-specific or any single-country assumptions into the global core would make the platform difficult to reuse and would silently turn local administrative facts into universal rules.

## Decision

Keep the global core jurisdiction-neutral and specialize execution through country adapters.

Global core owns concepts such as:

```text
Citizen problem
AI-mediated exchange
Case Passport
Hard Gate
Handoff
Return Object
Meaning preservation
P0-P11 routing coordinates
Knowledge utilization
```

Country adapters own:

```text
institutions
regulators
standards
laws / authority mappings
public programs
funding mechanisms
language/localization
geography/access constraints
country-specific hard gates
```

## Consequences

Positive:

- global reuse without pretending institutions are universal;
- country data can refresh independently;
- legal/regulatory claims remain jurisdiction-scoped;
- local communities can contribute adapters without forking core semantics.

Cost:

- adapter maintenance becomes an ongoing data-governance task;
- cross-country comparisons require explicit normalization;
- local execution quality depends on adapter freshness and coverage.

## Rule

If a country reveals a missing universal concept, propose it to the global core. Do not encode a local workaround as a universal rule by accident.
