# Toledo Citizen Platform Schemas

Machine-readable contracts live here.

## Current schemas

| Schema | Purpose |
|---|---|
| `case-passport.schema.json` | Persistent cross-actor case state and event history |
| `case-event.schema.json` | One auditable state transition applied to a Case Passport |
| `case-step-request.schema.json` | Stateless initialize/update/recompile request |
| `case-step-response.schema.json` | Updated Case Passport plus next Protocol Instance |
| `return-object.schema.json` | Structured return from expert/institution to citizen/decision owner |
| `institution-record.schema.json` | Capability-bearing public/university/institution mechanism |
| `country-adapter-manifest.schema.json` | Country adapter identity, compatibility and dataset manifest |
| `protocol-compile-request.schema.json` | Compact direct Protocol Compiler input |
| `protocol-instance.schema.json` | Deterministic next-action readout |

## Authority

For object shape, these schemas are machine-readable contracts. Normative behavior is in `docs/`. Mathematical equations are authoritative only in `morrocwi/toledo` and are referenced through `docs/EQUATION_BINDINGS.md`.

## Closed-loop relation

```text
Case Input
  → Case Passport
  → Case Event*
  → Case Step Request
  → Protocol Instance
  → World / Institution
  → Return Object / Case Event
  → next Case Passport version
```

The public runtime is stateless. Schemas define the transport contract; they do not authorize public storage of real citizen data.

## Validation

CI validates all Draft 2020-12 schemas, reference adapter data, equation mirror integrity, runtime-generated Case Passports, runtime unit tests and service imports.

## Privacy

Schemas define structure, not permission to store data publicly. Real Case Passports and Return Objects may contain sensitive data and must live only in appropriately private deployments.
