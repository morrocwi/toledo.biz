# Changelog

All notable repository-level changes are recorded here.

The project follows the spirit of Keep a Changelog while remaining pre-1.0.

## Unreleased

No unreleased repository-level changes are recorded after the v0.2.0 release cut.

## 0.2.0 — 2026-09-11

### Added

- deterministic Toledo Protocol Compiler reference runtime;
- closed-loop Case Passport lifecycle with versioned, auditable Case Events;
- stateless `initialize -> event -> recompile -> return -> outcome -> stop` reference loop;
- Domain-Neutral Problem & Capability Grammar grounded in existing Toledo/Readout commitments without replacing prior layers;
- machine-readable Problem Signature schema with multiple candidate signatures, facet provenance, context gaps, Barrier Signature state and optional domain-adapter need;
- Practice Context preservation without occupation- or industry-specific core branching;
- anchor-preserved Decision Threads allowing one Case Passport to carry multiple concurrent decisions at different P0–P11 routing coordinates;
- explicit Decision Thread dependencies, `HOLD_FOR_DEPENDENCY`, thread-level hard-gate precedence, thread closure and case-closure aggregation;
- backward-compatible primary-thread projection through legacy `current_phase` and `current_decision` fields;
- Decision Thread JSON Schema, runtime engine, API endpoint, MCP tool/resource and normative ADR/documentation;
- cosmetics multi-decision regression case proving concurrent quality, regulatory and scale threads without adding a cosmetics-specific core protocol;
- HTTP Protocol API with equation, protocol, case lifecycle, Decision Thread, institution, handoff and Return Gate endpoints;
- MCP stdio server exposing equation, protocol, Case Passport, Decision Thread, routing and gate tools/resources for AI agents;
- pinned 36-entry machine-readable equation mirror with upstream Toledo provenance;
- `llms.txt` AI discovery index and `.well-known/toledo.json` service manifest;
- versioned OpenAPI contract;
- Case Event and Case Step request/response JSON Schemas;
- local citizen+AI/world closure path separated from externally routed Return-Gate closure;
- synthetic runtime test suite covering P_C preservation, signature endorsement, cross-domain invariance, no-restart rerouting, local closure, external Return-Gate closure and multi-decision dependencies;
- structured documentation, controlled glossary, data governance, institution registry, country-adapter standard and trust/safety contracts.

### Changed

- runtime package advanced to `0.5.0`;
- Protocol Compiler advanced to `v0.4`;
- API metadata advanced to `0.4.0`;
- public platform/citation version advanced to `0.2.0`;
- P0–P11 remain routing coordinates but may now apply independently to each Decision Thread rather than forcing one scalar phase onto a complex case;
- Case Passport remains the stable case anchor while multi-decision state is carried in `decision_threads[]`;
- hard safety/authority escalation outranks ordinary dependency holds;
- external closure requires a passing Return Gate plus citizen outcome;
- local citizen+AI/world closure does not require a fake institutional Return Object when no external actor was used and safety/authority conditions are satisfied;
- machine interfaces expose Decision Thread compilation while preserving the single-primary-protocol compatibility surface;
- equation mirror remains explicitly lower authority than `morrocwi/toledo`.

### Governance

- equation statements/status remain upstream-controlled by `morrocwi/toledo`;
- Decision Threads and the Domain-Neutral Problem & Capability Grammar are runtime/specification architecture, not new canonical equation families;
- occupation/practice context is preserved as situated context but MUST NOT silently select a bespoke core protocol;
- AI-generated candidate Problem Signatures MUST NOT be treated as diagnosis or truth merely because AI generated them;
- unknown/context-gap states remain legitimate outputs;
- optional domain adapters may specialize safety, professional, measurement, regulatory and provider constraints but MUST NOT redefine global Case Passport, provenance, hard-gate, Return Gate or equation semantics;
- public reference runtime remains stateless and is not an approved sensitive citizen-case store.

### Validation

Release-cut CI passed:

- JSON and Draft 2020-12 schema validation;
- deterministic runtime tests;
- Decision Thread and cosmetics multi-decision regression tests;
- API/MCP smoke imports;
- policy guards;
- repository hygiene.

## 0.1.0 — 2026-09-11

### Added

- citizen-first project mission and North Star;
- reference architecture and Citizen Protocol;
- Case Passport, Return Object and Institution Capability schemas;
- Thailand institution seed registry;
- equation binding boundary to `morrocwi/toledo`;
- security/contribution policies and baseline validation workflow.

### Notes

`0.1.0` was the specification baseline preceding the executable v0.2.0 platform release.
