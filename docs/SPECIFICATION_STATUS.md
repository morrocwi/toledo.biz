# Specification Status Map

This document prevents draft ideas, implementation contracts, public data, and upstream mathematics from being mistaken for one another.

## Current repository maturity

```text
Project maturity: specification-first / pre-alpha
Current public citation version: 0.1.0
Current architecture family: Toledo Citizen Platform aligned to Toledo v0.17
```

The repository already contains a coherent specification baseline, schemas, country-adapter seed data, and governance contracts. The deterministic reference engine is not yet complete.

## Authority classes

### A. Upstream mathematical authority

Source:

```text
https://github.com/morrocwi/toledo
```

Controls:

- canonical Toledo equations;
- equation provenance;
- equation status;
- mathematical lineage;
- equation source policy.

`toledo.biz` MUST consume those bindings; it MUST NOT silently fork them.

### B. Machine-readable contract authority

Source:

```text
packages/schemas/
```

Controls:

- Case Passport structure;
- Return Object structure;
- Institution Capability Record structure;
- future adapter/registry schemas.

Where prose and schema conflict on field shape, schema is the machine-readable contract and the conflict should be fixed.

### C. Normative platform specification

Current normative documents:

```text
docs/CITIZEN_PROTOCOL.md
docs/ARCHITECTURE.md
docs/GOVERNANCE.md
docs/TRUST_AND_SAFETY.md
docs/DATA_GOVERNANCE.md
docs/INSTITUTION_ROUTING.md
docs/INSTITUTION_REGISTRY_STANDARD.md
docs/COUNTRY_ADAPTER_STANDARD.md
docs/EQUATION_BINDINGS.md
docs/RELEASE_AND_VERSIONING.md
docs/GLOSSARY.md
```

These define intended behavior, boundaries, and terminology.

### D. Country/jurisdiction reference data

Source:

```text
adapters/<country>/
```

Status:

- time-sensitive;
- evidence/provenance dependent;
- not universal;
- not mathematical authority.

Thailand is currently the reference adapter.

### E. Informative material

Includes:

```text
README.md
ROADMAP.md
examples
issues
planning notes
```

Useful for orientation and planning, but lower authority than schemas and normative documents.

## Stable concepts

The following concepts are architecture anchors and should not be changed casually:

```text
Citizen owns the original life problem
AI-first != AI-only
P_C / P_S / P_D remain separate
Case Passport preserves continuity
Hard gates precede soft optimization
Referral != Handoff != Collaboration
Return-to-citizen is mandatory
Academic capability != University executability
Government functions remain typed
Problem resolution does not require innovation
Innovation does not require founder entrepreneurship
Global core / local adapter separation
```

Changes to these require an ADR and explicit migration review.

## Draft / evolving areas

The following remain expected to evolve:

- exact routing/scoring implementation;
- controlled capability vocabulary;
- country adapter manifest schema;
- institution data freshness automation;
- deterministic phase classifier;
- UI language and interaction patterns;
- production privacy architecture;
- steward operating workflow;
- cross-country compatibility rules;
- canonical promotion of citizen-bridge equation proposals upstream.

## Equation binding status

The citizen/institution/cross-actor equation family is currently registered upstream as a governed proposal set until canonical promotion is completed.

Implementation code MUST preserve that status rather than labeling proposals as canonical.

See:

```text
docs/EQUATION_BINDINGS.md
morrocwi/toledo/registry/proposals/TOLEDO_CITIZEN_BRIDGE_v0.17.json
```

## Change-control rule

A change requires an ADR when it materially alters any of:

```text
repository authority boundary
Case Passport concept
Return Gate semantics
hard-gate semantics
global-core/local-adapter boundary
citizen meaning-preservation rule
rights decomposition
phase semantics
```

A data refresh or non-semantic wording fix normally does not require an ADR.

## Conformance

A downstream implementation may call itself Toledo Citizen Platform-compatible only if it preserves, at minimum:

- original citizen problem representation;
- typed hard gates;
- explicit consent/data scope;
- valid handoff requirements;
- return-to-citizen requirement;
- non-collapse of academic fit and institutional executability;
- jurisdiction-specific authority handling;
- upstream equation provenance boundary.
