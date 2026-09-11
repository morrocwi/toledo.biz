# Changelog

All notable repository-level changes are recorded here.

The project follows the spirit of Keep a Changelog while remaining pre-1.0.

## Unreleased

### Added

- deterministic Toledo Protocol Compiler reference runtime;
- closed-loop Case Passport lifecycle with versioned, auditable Case Events;
- stateless `initialize -> event -> recompile -> return -> outcome -> stop` reference loop;
- Domain-Neutral Problem & Capability Grammar grounded in existing Toledo/Readout commitments without replacing prior layers;
- machine-readable `problem-signature.schema.json` with multiple candidate signatures, facet provenance, context gaps, Barrier Signature state and optional domain-adapter need;
- **anchor-preserved Decision Threads** for several concurrent decisions inside one Case Passport while retaining P0-P11 semantics;
- machine-readable `decision-thread.schema.json` with decision, phase, dependencies, blocking state, thread-local evidence/risk/capability/return/outcome state;
- `DECISION_THREADS.md` normative additive runtime contract and ADR 0005 (`anchor-preserved-decision-threads`);
- Decision Thread structural Case Events: `DECISION_THREAD_CREATED`, `DECISION_THREAD_DEPENDENCIES_UPDATED`, `DECISION_THREAD_CANCELLED`, `PRIMARY_THREAD_SET`;
- thread-scoped reuse of existing Case Events through `payload.thread_id`;
- dependency action `HOLD` / status `HOLD_FOR_DEPENDENCY`, with hard safety/authority escalation taking precedence;
- `compile_decision_threads()` runtime function and `thread_protocols[]` in Case Step responses;
- API endpoint `POST /v1/cases/threads/compile` and schema endpoint `/v1/schemas/decision-thread`;
- MCP tool `compile_case_threads` plus `toledo://protocol/decision-threads` and `toledo://schema/decision-thread` resources;
- cosmetics-business cross-domain regression case proving that quality P1, regulatory P3 and scale P10 decisions can coexist without creating a cosmetics-specific core protocol;
- cross-domain regression coverage ensuring occupation/industry changes do not create bespoke core protocol branching;
- local citizen+AI/world closure path separated from externally routed Return-Gate closure;
- pinned 36-entry machine-readable equation mirror with upstream Toledo provenance;
- `llms.txt` AI discovery index and `.well-known/toledo.json` service manifest;
- HTTP Protocol API, MCP stdio server, OpenAPI contract and schema/data/runtime CI.

### Changed

- Protocol Compiler advanced to **v0.4**, retaining the original P0-P11 action logic while adding dependency-aware `HOLD`;
- runtime package advanced to **`0.5.0`**;
- API reference metadata advanced to **`0.4.0`**;
- Case Passport now carries `decision_threads[]` and `primary_thread_id` while keeping legacy `current_phase` / `current_decision` as a primary-thread projection;
- `step_case()` now returns a backward-compatible primary `protocol` plus `thread_protocols[]` for all concurrent decisions;
- `P_C = citizen_problem_verbatim` remains protected against ordinary event overwrite while Problem Signatures and Decision Threads remain separate routing/readout objects;
- failed institutional routes remain inside the same Case Passport/thread instead of forcing case restart;
- external thread closure requires a passing Return Gate plus a recorded thread outcome;
- local citizen+AI/world thread closure does not require a fake institutional Return Object when no external actor was used and safety/authority conditions are satisfied;
- multi-decision case closure additionally requires all required non-cancelled Decision Threads to be closed plus a citizen-level closure outcome;
- CI now validates Decision Thread schema/contracts, dependency precedence, multi-decision closure and the cosmetics regression alongside prior problem-grammar, adapter, policy and repository-hygiene checks;
- equation mirror remains explicitly lower authority than `morrocwi/toledo`.

### Governance

- equation statements/status remain upstream-controlled;
- the Domain-Neutral Problem & Capability Grammar is a product/runtime architecture, not a new equation family or validated universal ontology;
- Decision Threads are an additive runtime/product orchestration layer, not a replacement phase system and not a new canonical equation;
- `Case != SingleDecision`, `DecisionThread != NewCase`, `ThreadPhase != CaseMaturity`, `BlockedThread != FailedCase`, and `ThreadClosure != CaseClosure` are implementation non-collapse rules;
- occupation/practice/industry context is preserved as situated context but MUST NOT silently select a bespoke core protocol;
- candidate Problem Signatures MUST NOT be treated as diagnosis or truth merely because AI generated them;
- unknown/context-gap states are legitimate outputs and MUST NOT be silently filled by inference;
- optional domain adapters may specialize safety, professional, measurement, regulatory and provider constraints but MUST NOT redefine global Case Passport, Decision Thread, provenance, hard-gate, Return Gate or equation semantics;
- machine interfaces must disclose equation provenance and proposal/canonical status;
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
