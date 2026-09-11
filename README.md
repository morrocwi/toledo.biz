# Toledo Citizen Platform

**Turn lived experience into usable knowledge — AI first, institutions only when necessary.**

Toledo Citizen Platform is the citizen-facing implementation layer of the Toledo framework. It helps ordinary people structure real-life problems, obtain the **minimum sufficient** expert or institutional support needed for a safe next action, preserve the same case across actors, and return useful knowledge to everyday life.

> **North Star:** How can citizens translate experiential capital, with AI, into usable knowledge and innovation capital at the lowest total cost that remains safe, while calling on existing knowledge institutions only as much as necessary?

## Project status

| Item | Status |
|---|---|
| Product maturity | **Specification-first / pre-alpha** |
| Public citation version | `0.1.0` |
| Architecture baseline | aligned to Toledo citizen/cross-actor framework v0.17 |
| Deterministic routing engine | planned / not yet complete |
| Reference country adapter | Thailand |
| Production citizen-case storage | **not provided by this public repository** |
| Mathematical authority | [`morrocwi/toledo`](https://github.com/morrocwi/toledo) |

This repository is not yet a production public service. It is a structured specification, schema, routing, governance, and adapter foundation.

## The citizen flow

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
Citizen+AI / Expert / Lab / University / Public Service / Regulator
      ↓
CASE PASSPORT + VALID HANDOFF
      ↓
RETURN OBJECT
      ↓
SAFE / JUSTIFIED ACTION
      ↓
WORLD RESULT
      ↓
Better life / Local fix / Repeatable knowledge / Research / Innovation
```

A good local solution is a complete success. A citizen does **not** have to become a researcher, inventor, or entrepreneur.

## Core invariants

```text
AI-first != AI-only
Observation != Interpretation != Diagnosis
Academic capability != University executability
Referral != Handoff != Collaboration
Institutional output != Citizen outcome
Grant approval != Regulatory approval
Experience provenance != IP ownership
Company registration != Business-0
Innovation success != Creator becomes entrepreneur
Vehicle != Matching channel
```

The citizen's original problem remains visible throughout the case.

## Repository boundaries

| Repository | Authority |
|---|---|
| [`morrocwi/toledo`](https://github.com/morrocwi/toledo) | canonical Toledo mathematics, equation provenance, governance primitives |
| **`morrocwi/toledo.biz`** | citizen-facing product specification, schemas, routing, country adapters, orchestration |
| `morrocwi/readout_genesis` | ontology lens |
| `morrocwi/readout_universe` | epistemology lens |
| `morrocwi/glosa` | human–AI / collaboration lens |

**Equation rule:** if a behavior depends on Toledo mathematics, bind to the upstream Toledo registry. Do not silently fork an equation in product code or documentation.

## Documentation

Start with [`docs/README.md`](docs/README.md), which defines the documentation hierarchy and authority order.

Key documents:

- [`docs/CITIZEN_PROTOCOL.md`](docs/CITIZEN_PROTOCOL.md) — citizen-facing protocol
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — reference architecture
- [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md) — rights, stewardship, meaning preservation
- [`docs/TRUST_AND_SAFETY.md`](docs/TRUST_AND_SAFETY.md) — hard gates and escalation boundaries
- [`docs/DATA_GOVERNANCE.md`](docs/DATA_GOVERNANCE.md) — provenance, freshness, evidence and data lifecycle
- [`docs/INSTITUTION_ROUTING.md`](docs/INSTITUTION_ROUTING.md) — capability-first institutional routing
- [`docs/INSTITUTION_REGISTRY_STANDARD.md`](docs/INSTITUTION_REGISTRY_STANDARD.md) — public-service data standard
- [`docs/COUNTRY_ADAPTER_STANDARD.md`](docs/COUNTRY_ADAPTER_STANDARD.md) — global adapter contract
- [`docs/GLOSSARY.md`](docs/GLOSSARY.md) — controlled vocabulary
- [`docs/SPECIFICATION_STATUS.md`](docs/SPECIFICATION_STATUS.md) — normative/draft/upstream status map
- [`docs/RELEASE_AND_VERSIONING.md`](docs/RELEASE_AND_VERSIONING.md) — versioning policy
- [`docs/EQUATION_BINDINGS.md`](docs/EQUATION_BINDINGS.md) — upstream equation bindings

## Routing phases

`P0`–`P11` are routing coordinates, not a maturity ranking or mandatory funnel.

| Phase | State |
|---|---|
| P0 | citizen problem + AI entry |
| P1 | diagnosis / minimum-sufficient check |
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

A case may terminate successfully at any appropriate phase.

## Cross-actor architecture

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

The platform routes by **capability, eligibility, access, evidence need, time fit, rights, and burden** — not prestige.

## Global core, local adapters

The global core is jurisdiction-neutral. Country adapters contain institutions, regulators, standards, public programs, language, and local access constraints.

Current adapter:

- [`adapters/thailand/`](adapters/thailand/) — reference adapter with evidence-backed institution seed data and explicit known gaps.

See [`adapters/README.md`](adapters/README.md) and [`docs/COUNTRY_ADAPTER_STANDARD.md`](docs/COUNTRY_ADAPTER_STANDARD.md).

## Data discipline

Institutional routing data is treated as a versioned evidence-backed dataset.

Every live record should make clear:

```text
what mechanism it describes
what capability it offers
who it targets
how it can be accessed
what evidence supports the record
when it was verified
what remains unknown
what fallback exists
```

`Website exists != Service currently available`.

See [`docs/DATA_GOVERNANCE.md`](docs/DATA_GOVERNANCE.md).

## Schemas

Machine-readable contracts live in [`packages/schemas/`](packages/schemas/):

- Case Passport
- Return Object
- Institution Capability Record
- Country Adapter Manifest

CI validates the reference datasets against these schemas.

## Repository layout

```text
apps/                    future citizen/steward applications
packages/
  core/                  state-machine and core implementation contracts
  routing/               capability/institution routing implementation
  schemas/               machine-readable contracts
adapters/                 country/jurisdiction adapters
docs/                     normative specification + architecture decisions
registry/                 implementation bindings; never equation authority
.github/                  validation and contribution automation
```

## Safety and privacy boundary

This public repository is **not** an approved location for real sensitive citizen case data.

Do not submit medical records, identity documents, private addresses, passwords/tokens, confidential contracts, patent-sensitive material, or restricted community knowledge through public issues, examples, logs, or fixtures.

Production deployments need private case storage, access control, encryption, retention/deletion rules, consent enforcement, and audit logs. See [`SECURITY.md`](SECURITY.md).

## Development priorities

See [`ROADMAP.md`](ROADMAP.md). The current active engineering objective is a small deterministic, auditable routing engine before a polished citizen UI.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`AGENTS.md`](AGENTS.md).

Country-adapter and institution-data contributions must include provenance and freshness metadata. Routing changes must preserve hard gates, meaning, consent, rights, decision ownership, and return-to-citizen.

## Citation

Citation metadata is in [`CITATION.cff`](CITATION.cff).

## License

Documentation and registries: CC BY 4.0. Software/code: MIT. See [`LICENSE`](LICENSE).
