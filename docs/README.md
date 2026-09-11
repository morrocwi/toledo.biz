# Toledo Citizen Platform — Documentation

This directory is the documentation entry point for `morrocwi/toledo.biz`.

The repository follows a **specification-first, evidence-aware, executable-protocol, global-core/local-adapter** structure. Citizen-facing behavior should stay simple; governance, data, equation provenance and routing contracts behind it should stay explicit and auditable.

## Runtime and machine access

| Document / artifact | Purpose | Status |
|---|---|---|
| [`PROTOCOL_COMPILER.md`](PROTOCOL_COMPILER.md) | Deterministic minimal-subgraph compiler | Reference runtime contract |
| [`API.md`](API.md) | HTTP API usage and endpoint map | Reference implementation |
| [`MCP.md`](MCP.md) | MCP tools/resources for AI agents | Reference implementation |
| [`../openapi/toledo.protocol.v1.yaml`](../openapi/toledo.protocol.v1.yaml) | Versioned API contract | Machine contract |
| [`../llms.txt`](../llms.txt) | AI-readable repository index | Discovery |
| [`../.well-known/toledo.json`](../.well-known/toledo.json) | Service/repository discovery manifest | Discovery |
| [`../registry/equation-index.json`](../registry/equation-index.json) | Pinned equation read mirror | Mirror only; upstream governs |

## Start here

| Document | Purpose | Status |
|---|---|---|
| [`../README.md`](../README.md) | Project overview, boundaries, current maturity | Informative |
| [`CITIZEN_PROTOCOL.md`](CITIZEN_PROTOCOL.md) | Plain-language citizen workflow | Normative for product behavior |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Reference system architecture | Normative architecture baseline |
| [`GLOSSARY.md`](GLOSSARY.md) | Controlled vocabulary | Normative terminology |
| [`SPECIFICATION_STATUS.md`](SPECIFICATION_STATUS.md) | Stable/draft/upstream-controlled status map | Normative status map |

## Trust, governance, and safety

| Document | Purpose | Status |
|---|---|---|
| [`GOVERNANCE.md`](GOVERNANCE.md) | Rights, meaning preservation, case stewardship, actor boundaries | Normative |
| [`TRUST_AND_SAFETY.md`](TRUST_AND_SAFETY.md) | Hard gates, high-stakes boundaries, human/institutional escalation | Normative |
| [`DATA_GOVERNANCE.md`](DATA_GOVERNANCE.md) | Provenance, freshness, evidence classes, privacy, record lifecycle | Normative |
| [`../SECURITY.md`](../SECURITY.md) | Public-repository and sensitive-case security boundary | Normative |

## Routing, adapters, and data

| Document | Purpose | Status |
|---|---|---|
| [`INSTITUTION_ROUTING.md`](INSTITUTION_ROUTING.md) | Capability-first routing model | Normative |
| [`INSTITUTION_REGISTRY_STANDARD.md`](INSTITUTION_REGISTRY_STANDARD.md) | Institution-record data standard and verification rules | Normative |
| [`COUNTRY_ADAPTER_STANDARD.md`](COUNTRY_ADAPTER_STANDARD.md) | Requirements for jurisdiction/country adapters | Normative |
| [`DATA_CATALOG.md`](DATA_CATALOG.md) | Human-readable dataset catalog | Reference |
| [`../registry/DATA_CATALOG.json`](../registry/DATA_CATALOG.json) | Machine-readable dataset catalog | Machine reference |
| [`../adapters/thailand/README.md`](../adapters/thailand/README.md) | Thailand reference adapter | Reference implementation |

## Mathematical authority and bindings

| Document | Purpose | Status |
|---|---|---|
| [`EQUATION_BINDINGS.md`](EQUATION_BINDINGS.md) | Product-to-upstream equation binding | Normative binding contract |
| [`../registry/README.md`](../registry/README.md) | Local registry authority boundary | Normative |

## Project operations

| Document | Purpose | Status |
|---|---|---|
| [`RELEASE_AND_VERSIONING.md`](RELEASE_AND_VERSIONING.md) | Platform, schema, adapter and equation-baseline versioning | Normative |
| [`../ROADMAP.md`](../ROADMAP.md) | Delivery sequence and exit criteria | Planning |
| [`../CONTRIBUTING.md`](../CONTRIBUTING.md) | Contribution rules | Normative contributor policy |
| [`../CHANGELOG.md`](../CHANGELOG.md) | Notable repository changes | Release record |

## Source-of-truth hierarchy

When artifacts disagree, use this precedence:

1. **Upstream Toledo mathematics** in `morrocwi/toledo` for equation statement, lineage and status.
2. **JSON Schemas / OpenAPI** for machine-readable data and API contracts.
3. **Normative documentation** for behavior and governance.
4. **Country adapters / evidence-backed snapshots** for jurisdiction-specific routing facts.
5. **Equation mirror** only as a pinned convenience readout; never higher than upstream.
6. **Examples, README prose, issues and roadmap** as informative material.

A downstream artifact MUST NOT silently redefine a higher-authority object.

## Documentation quality rule

Every material concept should have one primary definition. Other documents should link to that definition rather than create competing versions. Every time-sensitive institutional fact should carry provenance and a verification date.
