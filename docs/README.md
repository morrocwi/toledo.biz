# Toledo Citizen Platform — Documentation

This directory is the documentation entry point for `morrocwi/toledo.biz`.

The repository follows a **specification-first, evidence-aware, global-core/local-adapter** structure. The citizen-facing product should stay simple; the governance, data, and routing contracts behind it should stay explicit and auditable.

## Documentation map

### Start here

| Document | Purpose | Status |
|---|---|---|
| [`../README.md`](../README.md) | Project overview, boundaries, current maturity | Informative |
| [`CITIZEN_PROTOCOL.md`](CITIZEN_PROTOCOL.md) | Plain-language citizen workflow | Normative for product behavior |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Reference system architecture | Normative architecture baseline |
| [`GLOSSARY.md`](GLOSSARY.md) | Controlled vocabulary | Normative terminology |

### Trust, governance, and safety

| Document | Purpose | Status |
|---|---|---|
| [`GOVERNANCE.md`](GOVERNANCE.md) | Rights, meaning preservation, case stewardship, actor boundaries | Normative |
| [`TRUST_AND_SAFETY.md`](TRUST_AND_SAFETY.md) | Hard gates, high-stakes boundaries, human/institutional escalation | Normative |
| [`DATA_GOVERNANCE.md`](DATA_GOVERNANCE.md) | Provenance, freshness, evidence classes, privacy, record lifecycle | Normative |
| [`../SECURITY.md`](../SECURITY.md) | Public-repository and sensitive-case security boundary | Normative |

### Routing and institutional data

| Document | Purpose | Status |
|---|---|---|
| [`INSTITUTION_ROUTING.md`](INSTITUTION_ROUTING.md) | Capability-first routing model | Normative |
| [`INSTITUTION_REGISTRY_STANDARD.md`](INSTITUTION_REGISTRY_STANDARD.md) | Institution-record data standard and verification rules | Normative |
| [`COUNTRY_ADAPTER_STANDARD.md`](COUNTRY_ADAPTER_STANDARD.md) | Requirements for jurisdiction/country adapters | Normative |
| [`../adapters/thailand/README.md`](../adapters/thailand/README.md) | Thailand reference adapter | Reference implementation |

### Mathematical authority and implementation bindings

| Document | Purpose | Status |
|---|---|---|
| [`EQUATION_BINDINGS.md`](EQUATION_BINDINGS.md) | Binding between implementation rules and upstream Toledo mathematics | Normative binding contract |
| [`../registry/README.md`](../registry/README.md) | Local implementation-registry boundary | Normative |
| [`SPECIFICATION_STATUS.md`](SPECIFICATION_STATUS.md) | What is stable, draft, proposed, or upstream-controlled | Normative status map |

### Project operations

| Document | Purpose | Status |
|---|---|---|
| [`RELEASE_AND_VERSIONING.md`](RELEASE_AND_VERSIONING.md) | Platform, schema, adapter, and equation-baseline versioning | Normative |
| [`../ROADMAP.md`](../ROADMAP.md) | Delivery sequence and exit criteria | Planning |
| [`../CONTRIBUTING.md`](../CONTRIBUTING.md) | Contribution rules | Normative contributor policy |
| [`../CHANGELOG.md`](../CHANGELOG.md) | Notable repository changes | Release record |

### Architecture decisions

Architecture Decision Records (ADRs) preserve decisions that should not be rediscovered repeatedly:

- [`adr/0001-repository-authority-boundary.md`](adr/0001-repository-authority-boundary.md)
- [`adr/0002-case-passport-continuity.md`](adr/0002-case-passport-continuity.md)
- [`adr/0003-global-core-local-adapters.md`](adr/0003-global-core-local-adapters.md)
- [`adr/0004-institution-registry-provenance.md`](adr/0004-institution-registry-provenance.md)

## Normative language

In normative documents:

- **MUST / MUST NOT** = required for conformance;
- **SHOULD / SHOULD NOT** = strong default; deviations require a recorded reason;
- **MAY** = optional.

## Source-of-truth hierarchy

When two repository artifacts disagree, use this precedence:

1. **Upstream Toledo mathematics** in `morrocwi/toledo` for equations and equation provenance.
2. **JSON Schemas** in `packages/schemas/` for machine-readable data contracts.
3. **Normative documentation** listed above for behavior and governance.
4. **Country adapters / data snapshots** for jurisdiction-specific routing facts.
5. **Examples, README prose, issues, and roadmap text** as informative material.

A downstream file MUST NOT silently redefine a higher-authority object.

## Documentation quality rule

Every material concept should have exactly one primary definition. Other documents should link to that definition rather than create competing versions.

Every time-sensitive institutional fact should carry provenance and a verification date. Every country-specific rule should remain outside the jurisdiction-neutral core unless the core contract explicitly requires it.
