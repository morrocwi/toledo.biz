# Toledo Citizen Platform

**Turn lived experience into usable knowledge — AI first, institutions only when necessary.**

Toledo Citizen Platform is the citizen-facing implementation layer of the Toledo framework. It helps ordinary people structure real-life problems, obtain the **minimum sufficient** expert or institutional support needed for a safe next action, preserve the same case across actors, and return useful knowledge to everyday life.

> **North Star:** How can citizens translate experiential capital, with AI, into usable knowledge and innovation capital at the lowest total cost that remains safe, while calling on existing knowledge institutions only as much as necessary?

## Project status

| Item | Status |
|---|---|
| Product maturity | **Pre-alpha reference runtime** |
| Public citation version | `0.1.0` |
| Runtime package | `0.3.0` |
| Architecture baseline | aligned to Toledo citizen/cross-actor framework v0.17 |
| Protocol Compiler | **reference v0.2 implemented** |
| Closed-loop Case Passport | **implemented; stateless reference lifecycle** |
| Protocol API | **reference implementation available** |
| MCP server | **reference stdio server available** |
| Equation machine readout | **36-entry pinned mirror + optional live upstream read** |
| Reference country adapter | Thailand |
| Production citizen-case storage | **not provided by this public repository** |
| Mathematical authority | [`morrocwi/toledo`](https://github.com/morrocwi/toledo) |

This repository is not yet a production public service. The runtime is intentionally small, deterministic, auditable and designed to make the protocol executable before a polished UI is built.

## Closed-loop citizen flow

```text
REAL-LIFE PROBLEM
      ↓
CASE PASSPORT v1
      ↓
AI-MEDIATED STRUCTURE
      ↓
PROTOCOL COMPILER
      ↓
MINIMUM RELEVANT SUBGRAPH / NEXT ACTION
      ↓
Citizen+AI / World / Expert / Lab / University / Public Service / Regulator
      ↓
CASE EVENT or RETURN OBJECT
      ↓
CASE PASSPORT v2...vN
      ↓
RECOMPILE
      ↓
RETURN GATE + CITIZEN OUTCOME
      ↓
STOP / or continue from the same case
```

A good local solution is a complete success. A citizen does **not** have to become a researcher, inventor, or entrepreneur.

## Machine access for AI systems

Toledo exposes three machine-first surfaces:

1. **Protocol API** — HTTP/FastAPI reference service.
2. **MCP server** — stdio MCP tools/resources for AI agents.
3. **Equation readout index** — pinned machine-readable mirror of the upstream Toledo citizen-bridge proposal family.

Start here:

```text
llms.txt
docs/PROTOCOL_COMPILER.md
docs/CASE_LIFECYCLE.md
docs/API.md
docs/MCP.md
openapi/toledo.protocol.v1.yaml
registry/equation-index.json
.well-known/toledo.json
```

Run locally:

```bash
python -m pip install -e .
toledo-api   # HTTP API on 127.0.0.1:8787
toledo-mcp   # MCP stdio server
```

The preferred machine loop is:

```text
initialize_case
→ advance_case
→ world/institution action
→ update_case or advance_case(event)
→ Return Object
→ OUTCOME_UPDATED
→ STOP when citizen closure is satisfied
```

## Equation authority

`toledo.biz` consumes Toledo mathematics; it does not own it.

```text
morrocwi/toledo
    = equation statement / lineage / status authority

morrocwi/toledo.biz
    = implementation / protocol / API / MCP / adapters
```

The current citizen-bridge family is pinned to upstream proposal commit:

```text
361546c934829de56f3dcff2032c740209de847a
```

`registry/equation-index.json` is a **read mirror**, not canonical authority. Responses preserve proposal status and upstream provenance.

## Core invariants

```text
AI-first != AI-only
Observation != Interpretation != Diagnosis
P_C != P_S != P_D
Academic capability != University executability
Referral != Handoff != Collaboration
Institutional output != Citizen outcome
Route failure != Case restart
Grant approval != Regulatory approval
Experience provenance != IP ownership
Company registration != Business-0
Innovation success != Creator becomes entrepreneur
Vehicle != Matching channel
```

The citizen's original problem `P_C = citizen_problem_verbatim` is preserved and cannot be silently overwritten by ordinary Case Events.

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
                                  ↓
                          CASE EVENT / RECOMPILE
```

The platform routes by **capability, eligibility, access, evidence need, time fit, rights, and burden** — not prestige.

## Global core, local adapters

The global core is jurisdiction-neutral. Country adapters contain institutions, regulators, standards, public programs, language, and local access constraints.

Current adapter:

- [`adapters/thailand/`](adapters/thailand/) — reference adapter with evidence-backed institution seed data and explicit known gaps.

## Documentation

Start with [`docs/README.md`](docs/README.md).

Key runtime documents:

- [`docs/PROTOCOL_COMPILER.md`](docs/PROTOCOL_COMPILER.md)
- [`docs/CASE_LIFECYCLE.md`](docs/CASE_LIFECYCLE.md)
- [`docs/API.md`](docs/API.md)
- [`docs/MCP.md`](docs/MCP.md)
- [`docs/EQUATION_BINDINGS.md`](docs/EQUATION_BINDINGS.md)

Key governance documents:

- [`docs/CITIZEN_PROTOCOL.md`](docs/CITIZEN_PROTOCOL.md)
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md)
- [`docs/TRUST_AND_SAFETY.md`](docs/TRUST_AND_SAFETY.md)
- [`docs/DATA_GOVERNANCE.md`](docs/DATA_GOVERNANCE.md)
- [`docs/INSTITUTION_ROUTING.md`](docs/INSTITUTION_ROUTING.md)
- [`docs/GLOSSARY.md`](docs/GLOSSARY.md)

## Schemas

Machine-readable contracts live in [`packages/schemas/`](packages/schemas/), including Case Passport, Case Event, Case Step request/response, Return Object, institution records, country adapters, protocol compile requests and protocol instances.

## Repository layout

```text
apps/
  protocol_api/            HTTP Protocol API
  mcp_server/              MCP server for AI agents
  citizen-web/             future citizen UI
  steward-console/         future steward UI
src/toledo_runtime/        deterministic runtime + closed-loop case engine
packages/schemas/          machine-readable contracts
openapi/                   API contract
adapters/                  country/jurisdiction adapters
docs/                      normative specification + runtime docs
registry/                  implementation data + equation read mirror
llms.txt                   AI-readable repository index
.well-known/               service discovery metadata
.github/                   validation and contribution automation
```

## Safety and privacy boundary

This public repository is **not** an approved location for real sensitive citizen case data.

Do not submit medical records, identity documents, private addresses, passwords/tokens, confidential contracts, patent-sensitive material, or restricted community knowledge through public issues, examples, logs, or fixtures.

The reference lifecycle is deliberately stateless: the caller holds the Case Passport. Production deployments need private case storage, access control, encryption, retention/deletion rules, consent enforcement, audit logs and domain-specific safety review. See [`SECURITY.md`](SECURITY.md).

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`AGENTS.md`](AGENTS.md). Equation changes belong upstream in `morrocwi/toledo`; product code must bind to and disclose upstream status rather than silently forking mathematical meaning.

## Citation

Citation metadata is in [`CITATION.cff`](CITATION.cff).

## License

Documentation and registries: CC BY 4.0. Software/code: MIT. See [`LICENSE`](LICENSE).
