# Changelog

All notable repository-level changes are recorded here.

The project follows the spirit of Keep a Changelog while remaining pre-1.0 and specification-first.

## Unreleased

### Added

- structured documentation index under `docs/README.md`;
- controlled glossary and source-of-truth hierarchy;
- data-governance and provenance standard;
- institution capability registry standard;
- global country-adapter standard;
- trust and safety model;
- release/versioning policy;
- specification status map;
- architecture decision records for repository authority, Case Passport continuity, country adapters, and institution provenance;
- country adapter manifest schema;
- Thailand adapter manifest with known gaps and compatibility metadata;
- schema package documentation;
- adapters index.

### Changed

- institution-record schema expanded with optional provenance, verification, availability, delivery-mode, localization, lifecycle, and maintenance metadata;
- Thailand adapter documentation reorganized around routing, data quality, evidence, gaps, and privacy;
- CI upgraded from JSON syntax checks to JSON Schema validation, unique institution-ID checks, adapter-manifest validation, documentation policy guards, and repository hygiene checks.

### Governance

- clarified that institution identity, service availability, accreditation, legal authority, and eligibility are distinct claims;
- formalized source classes `S0`–`S5` and verification levels `V0`–`V3`;
- formalized global-core/local-adapter boundary and documentation authority precedence.

## 0.1.0 — 2026-09-11

### Added

- citizen-first project mission and North Star;
- reference architecture;
- Citizen Protocol;
- governance/rights model;
- institutional routing model;
- Case Passport, Return Object, and Institution Capability JSON Schemas;
- Thailand institution seed registry;
- equation binding boundary to `morrocwi/toledo`;
- security and contribution policies;
- baseline validation workflow;
- project roadmap and citation metadata.

### Notes

`0.1.0` is a specification baseline, not a production-ready citizen service.
