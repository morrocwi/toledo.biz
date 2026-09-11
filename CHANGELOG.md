# Changelog

All notable repository-level changes are recorded here.

The project follows the spirit of Keep a Changelog while remaining pre-1.0.

## Unreleased

### Added

- deterministic Toledo Protocol Compiler reference runtime;
- closed-loop Case Passport lifecycle with versioned, auditable Case Events;
- stateless `initialize -> event -> recompile -> return -> outcome -> stop` reference loop;
- `create_case_passport`, `apply_case_event`, `evaluate_return_object` and `step_case` runtime functions;
- HTTP Protocol API (`apps/protocol_api`) with equation, protocol, case lifecycle, institution, handoff and Return Gate endpoints;
- MCP stdio server (`apps/mcp_server`) exposing equation, protocol, Case Passport, routing and gate tools/resources for AI agents;
- `CASE_LIFECYCLE.md` normative runtime contract;
- Domain-Neutral Problem & Capability Grammar grounded in the existing Toledo/Readout architectural commitments without replacing prior layers;
- machine-readable `problem-signature.schema.json` with multiple candidate signatures, facet provenance, context gaps, Barrier Signature state and optional domain-adapter need;
- `practice_context` and `external_actor_used` Case Passport state;
- `SIGNATURE_CANDIDATES_UPDATED`, `SIGNATURE_ENDORSED` and `BARRIER_UPDATED` Case Events;
- cross-domain regression coverage ensuring occupation changes do not create bespoke core protocol branching;
- local citizen+AI/world closure path separated from externally routed Return-Gate closure;
- Case Event and Case Step request/response JSON Schemas;
- pinned 36-entry machine-readable equation mirror with upstream Toledo provenance;
- `llms.txt` AI discovery index and `.well-known/toledo.json` service manifest;
- versioned OpenAPI contract;
- runtime unit tests including Case Passport schema validation, Problem Signature validation, no-restart rerouting, candidate-signature endorsement, local closure and external Return-Gate closure;
- structured documentation, controlled glossary, data governance, institution registry, country-adapter standard and trust/safety contracts.

### Changed

- Protocol Compiler advanced from v0.2 closed-loop compilation to v0.3 with domain-neutral problem-signature readouts and explicit local/external closure semantics;
- runtime package advanced from `0.3.0` to `0.4.0`;
- API reference metadata advanced to `0.3.0`;
- project status remains pre-alpha executable reference runtime but now includes a governed scaling layer intended to avoid one protocol per occupation/domain;
- MCP exposes `toledo://protocol/problem-capability-grammar` and `toledo://schema/problem-signature`;
- Protocol API exposes `/v1/schemas/problem-signature`;
- `P_C = citizen_problem_verbatim` remains protected against ordinary event overwrite while Problem Signatures remain separate routing readouts;
- failed institutional routes remain inside the same Case Passport instead of forcing case restart;
- external closure requires a passing Return Gate plus a recorded citizen outcome before `STOP`;
- local citizen+AI/world closure no longer requires a fake institutional Return Object when no external actor was used and safety/authority conditions are satisfied;
- CI validates the Problem Signature schema and domain-neutral architecture guards in addition to runtime contracts, schemas, adapters, policy guards and repository hygiene;
- equation mirror remains explicitly lower authority than `morrocwi/toledo`.

### Governance

- equation statements/status remain upstream-controlled;
- the Domain-Neutral Problem & Capability Grammar is explicitly a product/runtime architecture, not a new equation family or validated universal ontology;
- occupation/practice context is preserved as situated context but MUST NOT silently select a bespoke core protocol;
- candidate Problem Signatures MUST NOT be treated as diagnosis or truth merely because AI generated them;
- unknown/context-gap states are legitimate outputs and MUST NOT be silently filled by inference;
- optional domain adapters may specialize safety, professional, measurement, regulatory and provider constraints but MUST NOT redefine global Case Passport, provenance, hard-gate, Return Gate or equation semantics;
- machine interfaces must disclose equation provenance and proposal/canonical status;
- Protocol Compiler uses deterministic typed-gate behavior rather than allowing an AI model to silently override hard gates;
- the public reference runtime remains stateless and is not an approved sensitive citizen-case store.

## 0.1.0 — 2026-09-11

### Added

- citizen-first project mission and North Star;
- reference architecture and Citizen Protocol;
- Case Passport, Return Object and Institution Capability schemas;
- Thailand institution seed registry;
- equation binding boundary to `morrocwi/toledo`;
- security/contribution policies and baseline validation workflow.

### Notes

`0.1.0` is a specification baseline, not a production-ready citizen service.
