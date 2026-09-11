# Specification Status Map

This document prevents draft ideas, implementation contracts, public data, and upstream mathematics from being mistaken for one another.

## Current repository maturity

```text
Project maturity: pre-alpha executable reference release
Current public citation version: 0.2.0
Current runtime package: 0.6.0
Current Protocol Compiler: v0.5
Current API metadata: 0.5.0
Current architecture family: Toledo Citizen Platform aligned to Toledo v0.17
Current release notes: docs/releases/v0.2.0.md
```

The repository contains a coherent specification baseline, schemas, country-adapter seed data, governance contracts, a deterministic Protocol Compiler, a stateless closed-loop Case Passport engine, a domain-neutral Problem & Capability Grammar, anchor-preserved Decision Threads, flexible execution routing, an HTTP API and an MCP server. It is still not a production public service.

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
openapi/
```

Controls:

- Case Passport structure;
- Decision Thread structure;
- Case Event structure;
- Case Step request/response structure;
- Problem Signature structure;
- flexible execution-routing structure;
- Return Object structure;
- Institution Capability Record structure;
- protocol instance shape;
- API transport contract.

Where prose and schema conflict on field shape, schema/OpenAPI is the machine-readable contract and the conflict should be fixed.

### C. Normative platform specification

Current normative/reference-contract documents include:

```text
docs/CITIZEN_PROTOCOL.md
docs/ARCHITECTURE.md
docs/PROBLEM_CAPABILITY_GRAMMAR.md
docs/EXECUTION_ROUTING.md
docs/DECISION_THREADS.md
docs/GOVERNANCE.md
docs/TRUST_AND_SAFETY.md
docs/DATA_GOVERNANCE.md
docs/INSTITUTION_ROUTING.md
docs/INSTITUTION_REGISTRY_STANDARD.md
docs/COUNTRY_ADAPTER_STANDARD.md
docs/EQUATION_BINDINGS.md
docs/PROTOCOL_COMPILER.md
docs/CASE_LIFECYCLE.md
docs/RELEASE_AND_VERSIONING.md
docs/GLOSSARY.md
```

These define intended behavior, boundaries, terminology and the reference case lifecycle.

The Domain-Neutral Problem & Capability Grammar, Decision Thread layer, and Flexible Execution Routing layer are product/runtime architecture. They are **not** new equation families and are **not** claimed to be validated universal ontologies or scientific laws.

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

Thailand is currently the reference country adapter.

### E. Optional domain adapters

Domain adapters may be added when safety, professional authority, specialized measurement/sample handling, regulation, high-risk terminology, or provider matching materially requires specialization.

They may add:

```text
vocabulary
hazards
professional boundaries
measurement/sample rules
sector regulation
provider mappings
```

They MUST NOT redefine:

```text
P_C preservation
Case Passport identity
Decision Thread identity/dependency semantics
provenance semantics
hard-gate semantics
Return Gate semantics
equation authority
```

A new occupation or industry by itself does not justify a new core protocol.

### F. Informative material

Includes:

```text
README.md
ROADMAP.md
docs/releases/
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
AI != ExpertClass
AI acts as mediator/translator across citizen, knowledge-like, expert, tool, institution and world-return layers
P_C / P_S / P_D remain separate
P_C is not silently overwritten
Problem Signature is a routing readout, not a diagnosis
Candidate Signature != Endorsed Signature
KnowledgeLike != HumanExpert
KnowledgeLike != TruthCertificate
InteractionExpert != FieldExpert
Expertise != Authority
Occupation != Protocol Selector
Industry != Protocol Selector
Practice Context remains available as situated context
Unknown / unresolved is a valid state
Case Passport preserves continuity
Case ID is stable across ordinary rerouting
Case version advances through auditable events
Case != SingleDecision
DecisionThread != NewCase
ThreadPhase != CaseMaturity
BlockedThread != FailedCase
ThreadClosure != CaseClosure
Legacy current_phase/current_decision remain primary-thread projections
Phase != ExpertSelector
Phase != MandatorySequence
Bounded reversible world/market testing may occur before later phases when no hard gate blocks it
ForwardExperiment != PermissionToIgnoreHardGates
Hard gates precede soft optimization and ordinary dependency holds
Referral != Handoff != Collaboration
External work requires Return-to-Citizen
Local citizen+AI/world closure must not require a fake institutional return
Institutional completion != citizen closure
Academic capability != University executability
Government functions remain typed
Problem resolution does not require innovation
Innovation does not require founder entrepreneurship
Global core / country adapter / optional domain adapter separation
```

Changes to these require an ADR and explicit migration review.

## Implemented reference runtime

Implemented but still pre-alpha:

- deterministic Protocol Compiler v0.5;
- stateless Case Passport initialization/update/recompile loop;
- domain-neutral candidate Problem Signatures with provenance/endorsement state;
- Barrier Signature state;
- Practice Context preservation without occupation-specific core branching;
- anchor-preserved Decision Threads with dependency-aware compilation;
- primary-thread backward-compatibility projection;
- flexible Execution Requirement Matrix with interaction-vs-field expert distinction, knowledge-like state, tool/authority overlays and bounded forward experiment support;
- explicit AI mediator/translator role in execution routing;
- no-restart route-failure continuity;
- local citizen-only closure separated from external Return-Gate closure;
- Return Object evaluation and citizen-closure state;
- HTTP Protocol API 0.5.0;
- MCP v2 server;
- machine-readable equation mirror with upstream provenance.

These are reference implementations, not universal scientific validation of the underlying planning heuristics, problem grammar, execution matrix or thread decomposition.

## Draft / evolving areas

The following remain expected to evolve:

- exact routing/scoring implementation;
- controlled capability vocabulary;
- provider capability signatures;
- richer expert-role selection between interaction and field expertise when both are plausible;
- domain-adapter trigger logic;
- institution data freshness automation;
- deterministic phase/thread classifier;
- richer meaning-preservation checks;
- response-time/fallback evaluation;
- richer case reopening semantics;
- production persistence/privacy architecture;
- steward operating workflow;
- UI language and interaction patterns;
- cross-country compatibility rules;
- cross-domain falsification suite for the Problem & Capability Grammar, Flexible Execution Routing and Decision Threads;
- canonical promotion of citizen-bridge equation proposals upstream.

## Equation binding status

The citizen/institution/cross-actor equation family is currently registered upstream as a governed proposal set until canonical promotion is completed.

Implementation code MUST preserve that status rather than labeling proposals as canonical.

See:

```text
docs/EQUATION_BINDINGS.md
morrocwi/toledo/registry/proposals/TOLEDO_CITIZEN_BRIDGE_v0.17.json
```

No equation-status promotion is implied by the addition of the Domain-Neutral Problem & Capability Grammar, Decision Threads or Flexible Execution Routing.

## Change-control rule

A change requires an ADR when it materially alters any of:

```text
repository authority boundary
Case Passport concept
Case identity/version semantics
Decision Thread identity/dependency semantics
primary-thread projection compatibility
Problem Signature semantics
occupation-neutral core rule
Return Gate semantics
citizen/thread closure semantics
hard-gate semantics
global-core/country-adapter/domain-adapter boundary
citizen meaning-preservation rule
rights decomposition
phase semantics
AI mediator/expert boundary
interaction-vs-field expert distinction
forward-experiment hard-gate boundary
```

A data refresh or non-semantic wording fix normally does not require an ADR.

## Conformance

A downstream implementation may call itself Toledo Citizen Platform-compatible only if it preserves, at minimum:

- original citizen problem representation;
- stable Case Passport identity and auditable version changes;
- candidate/endorsed Problem Signature distinction when signatures are used;
- provenance for material AI-added problem distinctions;
- unknown/unresolved states instead of forced classification;
- occupation/practice context without occupation-specific core lock-in;
- Decision Thread identity/dependency behavior when multi-decision cases are used;
- primary-thread compatibility if claiming compatibility with the v0.2.0 reference release;
- typed hard gates;
- AI mediation without silently treating AI as expert authority or independent validation;
- distinction between knowledge-like material and human expertise;
- distinction between interaction expertise and field/front-line expertise when expert routing is material;
- non-linear phase semantics that permit bounded reversible world/market testing when gates allow it;
- explicit consent/data scope;
- valid handoff requirements;
- return-to-citizen requirement for external work;
- valid local closure without a fake external Return Object;
- no false closure from institutional output alone;
- non-collapse of academic fit and institutional executability;
- jurisdiction-specific authority handling;
- upstream equation provenance boundary.
