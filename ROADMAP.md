# Roadmap

## Stage 0 — Specification baseline

Status: **active**

- [x] citizen-first mission and repository boundary
- [x] citizen protocol
- [x] reference architecture
- [x] cross-actor governance model
- [x] Case Passport schema
- [x] Return Object schema
- [x] Institution Capability schema
- [x] Thailand reference routing model
- [ ] equation bindings to canonical Toledo IDs

## Stage 1 — Deterministic reference engine

Goal: implement a small auditable core before building a polished UI.

- [ ] case state machine
- [ ] P0–P11 phase classifier
- [ ] hard escalation gate evaluator
- [ ] minimum-sufficient route scorer
- [ ] institution registry query interface
- [ ] handoff validator
- [ ] return-gate validator
- [ ] meaning-preservation checkpoint
- [ ] no-restart rerouting
- [ ] JSON Schema validation tests

## Stage 2 — Thailand adapter

- [ ] live institution registry seeded from public sources
- [ ] freshness / `last_verified` monitoring
- [ ] capability tags for ClinicTech, science parks, universities, NSTDA/ITAP, TISTR, NIA, DIP/IP Mart, TED Fund, depa, PMUC, DIPROM, OSMEP, DBD, regulators, DITP, EXIM
- [ ] Thai-language citizen intake
- [ ] Thai public-service routing examples
- [ ] local fallback routes

## Stage 3 — Citizen web application

- [ ] plain-language intake
- [ ] observation vs interpretation UI
- [ ] citizen confirmation of AI reframe
- [ ] risk / escalation explanation
- [ ] "why this institution?" view
- [ ] Case Passport timeline
- [ ] Return Object view
- [ ] privacy-first case storage
- [ ] multilingual UI
- [ ] accessibility audit

## Stage 4 — Steward console

- [ ] pending handoffs
- [ ] decision deadlines
- [ ] consent scope
- [ ] response-time alerts
- [ ] fallback route activation
- [ ] failed-route logging
- [ ] return-gate enforcement
- [ ] rights/provenance checklist

## Stage 5 — Institution adapters

- [ ] capability-provider API contract
- [ ] verified service-directory ingestion
- [ ] lab/service availability adapters
- [ ] application-window adapters
- [ ] regulator adapters
- [ ] TTO/IP-market adapters

## Stage 6 — Globalization

- [ ] country adapter interface
- [ ] jurisdiction-specific safety/authority policies
- [ ] localization contribution workflow
- [ ] cross-border institution registry
- [ ] global public-service discovery

## Stage 7 — Evidence and impact

Measure separately:

```text
routing accuracy
handoff completion
return-to-citizen rate
citizen problem resolution
time saved
money saved
institutional burden
meaning-drift incidents
rights disputes
repeat institutional use
innovation / transfer / venture outcomes when relevant
```

Avoid a single vanity metric.

## Non-goals

The platform is not intended to become:

- a replacement for professional or regulatory authority;
- a universal truth engine;
- a mandatory innovation funnel;
- a startup factory;
- a centralized owner of citizen knowledge;
- a public repository for sensitive case data.
