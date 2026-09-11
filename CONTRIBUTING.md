# Contributing to Toledo Citizen Platform

Thank you for contributing.

This project combines citizen-facing product behavior, governance, routing, schemas, country data, and upstream mathematical bindings. Contributions are welcome, but each layer has a different authority and evidence burden.

## 1. Read first

Start with:

1. [`docs/README.md`](docs/README.md)
2. [`docs/SPECIFICATION_STATUS.md`](docs/SPECIFICATION_STATUS.md)
3. [`AGENTS.md`](AGENTS.md) if using AI/code agents
4. the normative document for the layer you plan to change.

If your change depends on a Toledo equation, inspect:

`https://github.com/morrocwi/toledo`

Do not introduce a new equation here as though it were canonical.

## 2. Identify the change class

Every PR should primarily identify as one or more of:

```text
citizen UX / language
architecture
case schema
governance / rights
safety / escalation
institution routing
institution data
country adapter
localization
equation binding
implementation code
documentation
security
```

## 3. Authority rules

Before changing a concept, check its source of truth:

- equations → `morrocwi/toledo`;
- object shape → `packages/schemas/`;
- terminology → `docs/GLOSSARY.md`;
- routing/governance semantics → normative `docs/`;
- country facts → `adapters/<country>/` with public provenance.

Do not fix a higher-authority conflict by quietly changing a lower-authority file.

## 4. Pull-request expectations

A change affecting routing, governance, schemas, or safety should state:

- problem being solved;
- current case state/phase affected;
- hard gates affected;
- expected citizen benefit;
- failure mode reduced or introduced;
- privacy/rights implications;
- compatibility/migration impact;
- equation references when applicable;
- tests/evidence added.

Architecture-anchor changes require an ADR.

## 5. Safety-sensitive changes

Changes affecting health, legal, regulatory, financial, physical-safety, or irreversible-action routing require tests for at least:

```text
hard escalation
HOLD_UNKNOWN
fallback route
response-time fit
meaning preservation
return-to-citizen
```

Never replace a hard gate with a soft score.

## 6. Institution-data contributions

Institution records must follow:

- [`docs/INSTITUTION_REGISTRY_STANDARD.md`](docs/INSTITUTION_REGISTRY_STANDARD.md)
- [`docs/DATA_GOVERNANCE.md`](docs/DATA_GOVERNANCE.md)
- `packages/schemas/institution-record.schema.json`

Minimum requirements:

```text
specific mechanism
public source
last_verified date
capability
phase fit
accessibility
entry channel
```

Do not mark a program as currently available from historical evidence alone.

When a field cannot be verified, use an explicit unknown/null state rather than guessing.

## 7. Country adapters

New adapters must follow [`docs/COUNTRY_ADAPTER_STANDARD.md`](docs/COUNTRY_ADAPTER_STANDARD.md).

At minimum include:

- adapter manifest;
- country README;
- institution seed data;
- public sources and verification dates;
- known gaps;
- no sensitive citizen data.

## 8. Schema changes

Schema changes should document:

- backward compatibility;
- migration impact;
- whether required fields change;
- effect on existing adapters/fixtures;
- validation updates.

Breaking schema changes require explicit version/migration handling under [`docs/RELEASE_AND_VERSIONING.md`](docs/RELEASE_AND_VERSIONING.md).

## 9. Documentation changes

Prefer:

- one primary definition per concept;
- explicit definitions;
- typed states;
- non-collapse statements where they prevent category errors;
- links to the authoritative definition rather than repeated divergent prose;
- source boundaries and verification dates for changing external facts.

Avoid language that turns AI into a truth authority or institutions into a mandatory hierarchy.

## 10. Architecture Decision Records

Add an ADR under `docs/adr/` when a change materially alters:

```text
repository authority boundary
Case Passport concept
hard-gate semantics
Return Gate semantics
global-core/local-adapter boundary
citizen meaning-preservation
rights decomposition
P0-P11 semantics
```

ADR format:

```text
Status
Date
Context
Decision
Consequences
Rejected alternatives / trade-offs
```

## 11. Privacy and synthetic data

Do not include real citizen case data in fixtures unless deliberately synthetic and non-reversible.

Never commit:

- identity documents;
- medical records;
- private addresses;
- credentials/secrets;
- confidential contracts;
- unpublished patent-sensitive material;
- restricted community knowledge.

Public issues are not a case-management channel.

## 12. Quality checks

Before submitting:

- run/confirm JSON syntax validity;
- ensure schema-constrained data validates;
- ensure IDs are unique;
- check internal documentation links you changed;
- update changelog for material repository behavior/data-contract changes;
- update ADR/status docs if architecture changed;
- verify no secret/sensitive files were added.

GitHub Actions runs baseline repository validation.

## 13. Equation changes

If a new mathematical expression is needed:

1. inspect `morrocwi/toledo` first;
2. check relevant ontology/epistemology/human–AI lenses when required by upstream policy;
3. propose/register the equation upstream;
4. label it as proposal until canonical promotion;
5. bind to its stable upstream identity here.

Do not retrospectively call a product heuristic a canonical Toledo theorem.

## 14. License

By contributing, you agree that software contributions are MIT-licensed and documentation/specification/registry contributions are CC BY 4.0 unless a file states otherwise.
