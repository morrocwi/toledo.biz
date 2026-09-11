# Toledo Citizen Platform Schemas

Machine-readable contracts live here.

## Current schemas

| Schema | Purpose |
|---|---|
| `case-passport.schema.json` | Persistent cross-actor case state |
| `return-object.schema.json` | Structured return from expert/institution to citizen/decision owner |
| `institution-record.schema.json` | Capability-bearing public/university/institution mechanism |
| `country-adapter-manifest.schema.json` | Country adapter identity, compatibility and dataset manifest |
| `protocol-compile-request.schema.json` | Input contract for deterministic protocol compilation |
| `protocol-instance.schema.json` | Output contract for compiled protocol instances |

## Authority

For object shape, these schemas are machine-readable contracts. Normative behavior is in `docs/`. Mathematical equations are authoritative only in `morrocwi/toledo` and are referenced through `docs/EQUATION_BINDINGS.md`.

## Validation

CI validates all Draft 2020-12 schemas, reference adapter data, equation mirror integrity, runtime unit tests and service imports.

## Privacy

Schemas define structure, not permission to store data publicly. Real Case Passports and Return Objects may contain sensitive data and must live only in appropriately private deployments.
