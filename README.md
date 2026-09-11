# Toledo Citizen Platform

**Turn lived experience into usable knowledge — with AI first, institutions only when necessary.**

Toledo Citizen Platform is the citizen-facing implementation layer of the Toledo framework. It is designed for ordinary people who encounter real problems in daily life and need a safer, better-justified next action without first becoming researchers, founders, or experts.

## North Star

> How can citizens translate experiential capital, with AI, into usable knowledge and innovation capital at the lowest total cost that remains safe, while calling on existing knowledge institutions only as much as necessary, so the resulting knowledge returns to improve everyday life?

The default success condition is **not** a paper, patent, grant, or startup. The default success condition is a better, safer, usable decision in the citizen's real situation.

```text
REAL-LIFE PROBLEM
      ↓
CITIZEN EXPERIENCE
      ↕
AI-MEDIATED EXCHANGE
      ↓
PROVISIONAL KNOWLEDGE-LIKE CAPITAL (K*_0)
      ↓
MINIMUM-SUFFICIENT CHECK
      ↓
Citizen+AI  /  Expert  /  Lab  /  University  /  Public Service  /  Regulator
      ↓
SAFE / JUSTIFIED ACTION
      ↓
WORLD RESULT
      ↓
Better life / Local fix / Repeatable knowledge / Research / Innovation
```

## What this repository is

`morrocwi/toledo.biz` is the **citizen product and orchestration repository**.

It should contain:

- citizen-facing workflows and interfaces;
- case continuity and Case Passport schemas;
- institutional capability/routing adapters;
- safety and escalation logic;
- steward tooling;
- localization and accessibility layers;
- reference applications and APIs.

It does **not** become the authoritative mathematical source for Toledo equations.

### Repository boundaries

| Repository | Authority |
|---|---|
| [`morrocwi/toledo`](https://github.com/morrocwi/toledo) | canonical Toledo mathematics, equation provenance, governance primitives |
| `morrocwi/toledo.biz` | citizen-facing implementation, routing, schemas, product architecture |
| `morrocwi/readout_genesis` | ontology lens |
| `morrocwi/readout_universe` | epistemology lens |
| `morrocwi/glosa` | human–AI / collaboration lens |

**Rule:** if an equation is needed here, reference its Toledo registry ID. Do not silently fork the mathematics.

## Design principles

1. **Citizen first.** The citizen remains the owner of the original life problem.
2. **AI first, not AI only.** AI lowers the cost of articulation, structuring, retrieval, comparison, questioning, and routing; it does not become the final authority.
3. **Minimum-sufficient escalation.** Call experts and institutions only when they materially reduce risk/uncertainty or satisfy a hard authority requirement.
4. **Problem resolution before innovation.** A local fix or correct adoption of existing practice is a valid success.
5. **No forced entrepreneurship.** Knowledge may become a startup, license, transfer, cooperative, public protocol, or simply remain a useful local solution.
6. **Meaning preservation.** Citizen language, AI-structured language, and disciplinary language are stored separately.
7. **No restart between institutions.** A versioned Case Passport carries context, rights, consent, evidence, timing, and return obligations.
8. **Return to citizen is mandatory.** Institutional output is not citizen outcome.
9. **Rights remain explicit.** Experience provenance, data rights, authorship, inventorship, IP ownership, publication rights, commercial rights, and benefit sharing are distinct.
10. **Global core, local adapters.** The core is jurisdiction-neutral; institutional registries and legal/regulatory routes are country adapters.

## Toledo phases

These are routing coordinates, not a maturity ranking.

| Phase | State |
|---|---|
| P0 | citizen problem + AI entry |
| P1 | field diagnosis / minimum-sufficient check |
| P2 | local resolution / standard practice |
| P3 | expert / lab / university escalation |
| P4 | pre-innovation / research candidate |
| P5 | prototype / proof-of-concept / validation |
| P6 | knowledge asset / IP / rights |
| P7 | knowledge-utilization route |
| P8 | Business-0 formed (`B0_F`) |
| P9 | first economic cycle closed (`B0_C`) |
| P10 | business dynamics / growth |
| P11 | global / cross-border |

A case may stop successfully at any phase.

## Core cross-actor architecture

```text
                           ACADEMIC / EXPERT
                                  ↕
                                  │
CITIZEN ↔ AI ↔ CASE STEWARD ↔ CASE PASSPORT
                                  │
                 ┌────────────────┼────────────────┐
                 ↕                ↕                ↕
             UNIVERSITY       PUBLIC SERVICE     REGULATOR
             / LAB / TTO       / FUNDER          / STANDARD
                 ↕                ↕                ↕
                 └──────── RETURN OBJECT ──────────┘
                                  ↓
                               CITIZEN
                                  ↓
                            WORLD-SIDE ACTION
```

## Monorepo target layout

```text
apps/
  citizen-web/          citizen interface
  steward-console/      case-steward workspace
packages/
  core/                 state machine / routing contracts
  schemas/              Case Passport, Return Object, institution records
  safety/               hard gates and escalation policy
  routing/              capability and institution matching
  localization/         language / jurisdiction adapters
docs/
  ARCHITECTURE.md
  CITIZEN_PROTOCOL.md
  GOVERNANCE.md
  INSTITUTION_ROUTING.md
registry/
  README.md              implementation-side registry contract
```

The initial repository is specification-first. Implementation should follow the schemas and governance contracts rather than burying policy in UI code.

## Safety boundary

Do **not** submit personal medical records, passwords, identity documents, private addresses, confidential commercial information, or other sensitive case data into public GitHub issues.

This repository is infrastructure. Real citizen cases require an appropriately private execution environment.

## Current status

**Architecture baseline: Toledo Citizen Platform v0.1**, aligned to Toledo cross-actor framework v0.17.

Next implementation priorities:

1. validate Case Passport and Return Object schemas;
2. build a deterministic phase/risk router;
3. implement an institution capability registry interface;
4. implement citizen confirmation / meaning-preservation gates;
5. implement steward handoff + return loop;
6. add country adapters, beginning with Thailand;
7. add a multilingual citizen web interface.

## License

Documentation and registries: CC BY 4.0. Software/code: MIT. See `LICENSE`.
