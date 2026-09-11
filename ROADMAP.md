# Roadmap

Toledo Citizen Platform is specification-first but now includes an executable pre-alpha reference runtime. The roadmap prioritizes a small auditable routing core, data integrity, and governed cross-actor continuity before a polished interface.

## Milestone status

| Milestone | Status |
|---|---|
| M0 — Specification and governance baseline | **complete** |
| M1 — Deterministic reference engine | **active / core loop implemented** |
| M2 — Thailand adapter hardening | next |
| M3 — Citizen web application | planned |
| M4 — Steward console | planned |
| M5 — Institution adapters / live registry | planned |
| M6 — Global country-adapter expansion | planned |
| M7 — Evidence and impact evaluation | planned |

## M0 — Specification and governance baseline

Status: **complete**

Delivered:

- [x] citizen-first mission and repository boundary
- [x] citizen protocol
- [x] reference architecture
- [x] cross-actor governance model
- [x] trust and safety model
- [x] Case Passport schema
- [x] Return Object schema
- [x] Institution Capability schema
- [x] Country Adapter Manifest schema
- [x] Thailand reference routing model
- [x] documentation hierarchy and glossary
- [x] data-governance/provenance standard
- [x] institution registry standard
- [x] global country-adapter standard
- [x] architecture decision records
- [x] equation proposal/binding lane to `morrocwi/toledo`
- [x] schema/data validation CI

Exit criterion: a contributor can identify the source of truth for concepts, schemas, equations, country data, and routing behavior without relying on conversation history.

## M1 — Deterministic reference engine

Status: **active / core closed loop implemented**

Goal: implement a small auditable core before building a polished UI.

Delivered:

- [x] versioned Case Passport state machine
- [x] Case Event contract and monotonic passport versioning
- [x] hard escalation gate evaluator
- [x] institution registry query interface
- [x] handoff validator
- [x] Return Gate validator
- [x] no-restart rerouting state
- [x] equation binding/readout loader
- [x] stateless initialize → event → recompile loop
- [x] citizen closure → `STOP` behavior
- [x] HTTP API and MCP access
- [x] synthetic runtime test suite

Still active:

- [ ] richer P0–P11 phase classifier
- [ ] minimum-sufficient route scorer using full cost/fit state
- [ ] explicit `AcademicFit != UniversityExecutability` executable check
- [ ] meaning-preservation checkpoint beyond stored state
- [ ] response-time/fallback evaluator using actual decision windows
- [ ] typed `HOLD_UNKNOWN` propagation across all gate families
- [ ] controlled reopening semantics for closed cases
- [ ] domain/jurisdiction policy plug-ins for hard thresholds

Minimum test cases still to add or deepen:

```text
unknown hard-gate state
ineligible institution
institution too slow for decision window
meaning drift
consent/data-scope failure
handoff failure
return-gate failure
non-founder knowledge-utilization route
multi-country adapter behavior
```

Current reference loop already covers:

```text
low-risk citizen+AI path
hard professional escalation
Case Passport schema validity
versioned observation event
successful no-restart reroute
Return Gate PASS
citizen outcome closure
STOP
```

M1 exit criterion: a deterministic library/API/MCP runtime consumes a synthetic Case Passport, applies typed events, returns the next routing state with traceable equation/gate references, and passes the remaining hard-gate/time-fit/meaning-preservation test matrix.

## M2 — Thailand adapter hardening

Goal: turn the current reference seed into a more operational, evidence-maintained adapter.

- [ ] assign verification metadata (`V0`–`V3`) to seed records
- [ ] normalize capability codes
- [ ] separate regulator and standards datasets
- [ ] add local/regional nodes where access materially differs
- [ ] add availability lifecycle fields
- [ ] add source/evidence bundles for high-volatility claims
- [ ] freshness monitoring for calls/application windows
- [ ] Thai-language citizen intake vocabulary
- [ ] Thai public-service routing examples
- [ ] synthetic Thai cases across P0–P11
- [ ] local fallback route coverage

Exit criterion: a live-routing prototype can explain both **why** a Thai mechanism is a fit and **how current** the supporting routing data is.

## M3 — Citizen web application

- [ ] plain-language intake
- [ ] observation vs interpretation UI
- [ ] citizen confirmation of AI reframe
- [ ] risk/escalation explanation
- [ ] "why this route?" view
- [ ] Case Passport timeline
- [ ] Return Object view
- [ ] private case-store interface
- [ ] multilingual UI
- [ ] accessibility audit
- [ ] low-bandwidth/mobile-first review

Exit criterion: a user can complete a synthetic end-to-end case without seeing institutional complexity unless escalation is needed.

## M4 — Steward console

- [ ] pending handoffs
- [ ] decision deadlines
- [ ] consent/data-use scopes
- [ ] response-time alerts
- [ ] fallback activation
- [ ] failed-route logging
- [ ] Return Gate enforcement
- [ ] rights/provenance checklist
- [ ] institution capacity/status notes

Exit criterion: a steward can move a case across institutions without asking the citizen to restart or losing rights/return obligations.

## M5 — Institution adapters / live registry

- [ ] capability-provider API contract
- [ ] verified public-service directory ingestion
- [ ] lab/service availability adapters
- [ ] application-window adapters
- [ ] regulator adapters
- [ ] TTO/IP-market adapters
- [ ] source conflict handling
- [ ] historical/superseded record lifecycle
- [ ] operational verification audit trail

Exit criterion: country adapter data can refresh independently from platform releases while preserving source and change provenance.

## M6 — Globalization

- [ ] country adapter onboarding workflow
- [ ] adapter conformance tests
- [ ] jurisdiction-specific hard-gate policy interface
- [ ] localization contribution workflow
- [ ] cross-border institution discovery
- [ ] multi-country regulator/standard representation
- [ ] adapter comparison without collapsing local context

Exit criterion: a second country adapter can be added without changing global citizen/core semantics.

## M7 — Evidence and impact

Measure separately:

```text
routing accuracy
hard-gate correctness
handoff completion
return-to-citizen rate
citizen problem resolution
time saved
money saved
retelling burden
institutional burden
meaning-drift incidents
rights/consent failures
fallback success
repeat institutional use
innovation / transfer / venture outcomes when relevant
```

Avoid a single vanity metric.

Research questions should include whether minimum-sufficient routing actually reduces citizen cost without increasing safety failures.

## Upstream dependency

The citizen/cross-actor equation family is registered in `morrocwi/toledo` as governed proposals pending canonical promotion. `toledo.biz` must preserve proposal/canonical status in bindings and implementations.

## Non-goals

The platform is not intended to become:

- a replacement for professional or regulatory authority;
- a universal truth engine;
- a mandatory innovation funnel;
- a startup factory;
- a centralized owner of citizen knowledge;
- a public repository for sensitive case data;
- a global database that erases local legal/cultural context.
