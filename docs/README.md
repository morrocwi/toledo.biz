# Toledo Citizen Platform — Documentation

This directory is the documentation entry point for `morrocwi/toledo.biz`.

The repository follows a **specification-first, evidence-aware, executable-protocol, domain-neutral-core, anchor-preserved multi-decision, global-core/local-adapter** structure. Citizen-facing behavior should stay simple; governance, data, equation provenance and routing contracts behind it should stay explicit and auditable.

## Runtime and machine access

| Document / artifact | Purpose | Status |
|---|---|---|
| [`PROTOCOL_COMPILER.md`](PROTOCOL_COMPILER.md) | Deterministic minimal-subgraph compiler, dependency holds and recompile semantics | Reference runtime contract |
| [`CASE_LIFECYCLE.md`](CASE_LIFECYCLE.md) | Versioned Case Passport, event loop, Decision Threads, return and closure semantics | Normative runtime contract |
| [`PROBLEM_CAPABILITY_GRAMMAR.md`](PROBLEM_CAPABILITY_GRAMMAR.md) | Domain-neutral problem signatures, barriers, optional domain adapters, cross-domain scaling rules | Normative architecture extension |
| [`DECISION_THREADS.md`](DECISION_THREADS.md) | Concurrent decision subgraphs that preserve P0-P11 and Case Passport anchors | Normative additive runtime contract |
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
| [`PROBLEM_CAPABILITY_GRAMMAR.md`](PROBLEM_CAPABILITY_GRAMMAR.md) | Scaling layer that prevents occupation/domain-specific core explosion | Normative |
| [`DECISION_THREADS.md`](DECISION_THREADS.md) | Multi-decision layer that prevents one scalar phase from erasing concurrent decisions | Normative |
| [`GLOSSARY.md`](GLOSSARY.md) | Controlled vocabulary | Normative terminology |
| [`SPECIFICATION_STATUS.md`](SPECIFICATION_STATUS.md) | Stable/draft/upstream-controlled status map | Normative status map |

## Architecture decisions

Important ADRs include:

```text
0001 repository authority boundary
0002 Case Passport continuity
0003 global core / local adapters
0004 institution registry provenance
0005 anchor-preserved Decision Threads
```

ADR 0005 explicitly preserves the existing Case Passport and P0-P11 semantics while permitting several decision subgraphs in one real-life case.

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
| [`PROBLEM_CAPABILITY_GRAMMAR.md`](PROBLEM_CAPABILITY_GRAMMAR.md) | Problem/Barrier Signature to required capability; optional domain adapter boundary | Normative |
| [`DECISION_THREADS.md`](DECISION_THREADS.md) | Decision dependencies, blocking, thread-local gates and closure | Normative |
| [`INSTITUTION_ROUTING.md`](INSTITUTION_ROUTING.md) | Capability-first routing model | Normative |
| [`INSTITUTION_REGISTRY_STANDARD.md`](INSTITUTION_REGISTRY_STANDARD.md) | Institution-record data standard and verification rules | Normative |
| [`COUNTRY_ADAPTER_STANDARD.md`](COUNTRY_ADAPTER_STANDARD.md) | Requirements for jurisdiction/country adapters | Normative |
| [`DATA_CATALOG.md`](DATA_CATALOG.md) | Human-readable dataset catalog | Reference |
| [`../registry/DATA_CATALOG.json`](../registry/DATA_CATALOG.json) | Machine-readable dataset catalog | Machine reference |
| [`../adapters/thailand/README.md`](../adapters/thailand/README.md) | Thailand reference country adapter | Reference implementation |

## Machine schemas

Important contracts include:

```text
case-passport.schema.json
decision-thread.schema.json
case-event.schema.json
case-step-request.schema.json
case-step-response.schema.json
problem-signature.schema.json
return-object.schema.json
institution-record.schema.json
country-adapter-manifest.schema.json
protocol-compile-request.schema.json
protocol-instance.schema.json
```

`problem-signature.schema.json` is deliberately domain-neutral. It carries candidate signatures, facet provenance, context gaps, barrier state and whether an optional domain adapter may be needed. It is not an ontology of truth.

`decision-thread.schema.json` is deliberately phase-preserving. A thread uses the existing P0-P11 coordinates; it does not create a new maturity system.

## Mathematical authority and bindings

| Document | Purpose | Status |
|---|---|---|
| [`EQUATION_BINDINGS.md`](EQUATION_BINDINGS.md) | Product-to-upstream equation binding | Normative binding contract |
| [`../registry/README.md`](../registry/README.md) | Local registry authority boundary | Normative |

Decision Threads and the Problem & Capability Grammar are runtime/product architecture. They do not silently create new mathematical authority.

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
3. **Normative documentation / accepted ADRs** for behavior and governance.
4. **Country/domain adapters / evidence-backed snapshots** for jurisdiction- or domain-specific routing constraints.
5. **Equation mirror** only as a pinned convenience readout; never higher than upstream.
6. **Examples, README prose, issues and roadmap** as informative material.

A downstream artifact MUST NOT silently redefine a higher-authority object.

## Documentation quality rule

Every material concept should have one primary definition. Other documents should link to that definition rather than create competing versions. Every time-sensitive institutional fact should carry provenance and a verification date.
