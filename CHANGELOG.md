# Changelog

All notable repository-level changes are recorded here.

The project follows the spirit of Keep a Changelog while remaining pre-1.0.

## Unreleased

### Added

- deterministic Toledo Protocol Compiler reference runtime;
- HTTP Protocol API (`apps/protocol_api`) with equation, protocol, institution, handoff and Return Gate endpoints;
- MCP stdio server (`apps/mcp_server`) exposing tools and resources for AI agents;
- pinned 36-entry machine-readable equation mirror with upstream Toledo provenance;
- `llms.txt` AI discovery index and `.well-known/toledo.json` service manifest;
- versioned OpenAPI contract;
- protocol compile request / protocol instance JSON Schemas;
- runtime unit tests and service import validation;
- structured documentation, controlled glossary, data governance, institution registry, country-adapter standard and trust/safety contracts.

### Changed

- project status advanced from specification-only to pre-alpha reference runtime;
- MCP runtime targets stable SDK v2 (`MCPServer`) with `mcp>=2.2,<3`;
- CI validates runtime contracts in addition to schemas, adapters, policy guards and repository hygiene;
- equation mirror remains explicitly lower authority than `morrocwi/toledo`.

### Governance

- equation statements/status remain upstream-controlled;
- machine interfaces must disclose equation provenance and proposal/canonical status;
- Protocol Compiler uses deterministic typed-gate behavior rather than allowing an AI model to silently override hard gates.

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
