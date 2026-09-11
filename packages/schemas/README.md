# Toledo Citizen Platform Schemas

Machine-readable contracts live here.

## Current schemas

| Schema | Purpose |
|---|---|
| `case-passport.schema.json` | Persistent cross-actor case state |
| `return-object.schema.json` | Structured return from expert/institution to citizen/decision owner |
| `institution-record.schema.json` | Capability-bearing public/university/institution mechanism |
| `country-adapter-manifest.schema.json` | Country adapter identity, compatibility, and dataset manifest |

## Authority

For object shape, these schemas are the machine-readable contract.

Normative behavior and semantics are described in `docs/`.

Mathematical equations are authoritative only in `morrocwi/toledo` and are referenced through `docs/EQUATION_BINDINGS.md`.

## Compatibility

Schema evolution must follow `docs/RELEASE_AND_VERSIONING.md`.

Breaking field changes require a documented migration path or a new incompatible schema version.

## Validation

CI should validate:

- every schema is valid JSON Schema Draft 2020-12;
- Thailand institution seed records against `institution-record.schema.json`;
- adapter manifests against `country-adapter-manifest.schema.json`;
- internal data identifiers are unique where required.

## Privacy

Schemas define structure, not permission to store data publicly.

Real citizen Case Passports and Return Objects may contain sensitive data and must live only in appropriately private deployments.
