# Implementation Registry Contract

This repository does **not** own Toledo mathematics.

Canonical equation provenance belongs to:

`https://github.com/morrocwi/toledo`

## Rule

Every implementation rule that depends on Toledo mathematics should carry:

```text
equation_ref
source_repo
source_version_or_commit
implementation_note
```

Do not copy an equation into application code and later treat the copy as authoritative.

## Registry roles

This repository may maintain implementation registries for:

- institution capabilities;
- country/jurisdiction adapters;
- UI state labels;
- route adapters;
- safety-policy mappings;
- localization strings;
- equation-to-code bindings.

It must not silently redefine the canonical statement of an equation.

## Versioning

When a canonical Toledo equation changes:

1. update the binding;
2. preserve the old implementation version where needed for audit;
3. record migration impact;
4. re-run affected route/safety tests.

## Initial equation family

The first implementation family is the citizen / institutional / cross-actor layer developed through Toledo v0.17:

```text
experiential capital
provisional K*_0
minimum-sufficient routing
institution utility
field information action
risk exposure
innovation promotion
knowledge utilization
Business-0 formation / closure
cross-actor handoff
return-to-citizen
bridge integrity
```

The corresponding equation registration belongs in `morrocwi/toledo`.
