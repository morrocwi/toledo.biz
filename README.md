# Toledo Citizen Platform

**Turn lived experience into usable knowledge — AI first, institutions only when necessary.**

Toledo Citizen Platform is the citizen-facing implementation layer of the Toledo framework. It helps ordinary people structure real-life problems, obtain the **minimum sufficient** expert or institutional support needed for a safe next action, preserve the same case across actors, and return useful knowledge to everyday life.

> **North Star:** How can citizens translate experiential capital, with AI, into usable knowledge and innovation capital at the lowest total cost that remains safe, while calling on existing knowledge institutions only as much as necessary?

## Project status

| Item | Status |
|---|---|
| Product maturity | **Pre-alpha executable reference release** |
| Public citation version | `0.2.0` |
| Runtime package | `0.5.0` |
| Architecture baseline | aligned to Toledo citizen/cross-actor framework v0.17 |
| Protocol Compiler | **reference v0.4 implemented** |
| Domain-neutral Problem & Capability Grammar | **normative architecture + machine schema implemented** |
| Decision Threads | **anchor-preserved multi-decision runtime implemented** |
| Closed-loop Case Passport | **implemented; stateless reference lifecycle** |
| Protocol API | **reference implementation available** |
| MCP server | **reference stdio server available** |
| Equation machine readout | **36-entry pinned mirror + optional live upstream read** |
| Reference country adapter | Thailand |
| Production citizen-case storage | **not provided by this public repository** |
| Mathematical authority | [`morrocwi/toledo`](https://github.com/morrocwi/toledo) |

Release notes: [`docs/releases/v0.2.0.md`](docs/releases/v0.2.0.md).

This repository is not yet a production public service. The runtime is intentionally small, deterministic, auditable and designed to make the protocol executable before a polished UI is built.

## Closed-loop citizen flow

```text
REAL-LIFE PROBLEM (P_C preserved)
      ↓
CASE PASSPORT v1
      ↓
AI-MEDIATED CANDIDATE SIGNATURE(S)
      ↓
CITIZEN / EVIDENCE ENDORSEMENT or HOLD_UNKNOWN
      ↓
PROBLEM + BARRIER STATE
      ↓
DECISION THREAD(S)
      ↓
PROTOCOL COMPILER
      ↓
MINIMUM RELEVANT SUBGRAPH / NEXT ACTION PER DECISION
      ↓
Citizen+AI / World / Expert / Lab / University / Public Service / Regulator
      ↓
CASE EVENT or RETURN OBJECT when external work is used
      ↓
CASE PASSPORT v2...vN
      ↓
RECOMPILE THREADS
      ↓
CITIZEN OUTCOME
      ↓
STOP / or continue from the same case
```

A good local solution is a complete success. A citizen does **not** have to become a researcher, inventor, or entrepreneur.

## Scale without one protocol per occupation

Toledo does not attempt to maintain a mushroom-farmer protocol, mechanic protocol, teacher protocol, shop-owner protocol, cosmetics protocol, and thousands of other bespoke cores.

```text
Occupation != ProtocolSelector
Industry != ProtocolSelector
```

Occupation and practice history are preserved as context because they may contain experiential expertise. The core instead represents the problem through candidate signatures, context gaps, barriers, risk/authority needs and required capabilities.

```text
P_C
→ Candidate Signature(s)
→ Endorsed / unresolved working signature
→ Barrier State
→ Minimal Protocol
→ Capability Need
→ Optional Domain Adapter
→ Provider / World Action
```

The Problem Signature is a routing readout, not a diagnosis and not a universal ontology of reality.

See [`docs/PROBLEM_CAPABILITY_GRAMMAR.md`](docs/PROBLEM_CAPABILITY_GRAMMAR.md) and [`packages/schemas/problem-signature.schema.json`](packages/schemas/problem-signature.schema.json).

## One case can contain several decisions

A real case does not always have one meaningful phase. A business can simultaneously have a quality decision at P1, an external test/regulatory decision at P3, and a scale decision at P10.

Toledo therefore preserves the original Case Passport and P0-P11 anchors but adds decision-specific subgraphs:

```text
Case Passport
  ├── shared P_C / goal / rights / context
  ├── Decision Thread T1 -> phase / evidence / gates / capability
  ├── Decision Thread T2 -> phase / evidence / gates / capability
  └── Decision Thread T3 -> phase / dependencies / next action
```

```text
Case != SingleDecision
DecisionThread != NewCase
ThreadPhase != CaseMaturity
BlockedThread != FailedCase
```

The old `current_phase` and `current_decision` fields remain as a **primary-thread projection**, preserving compatibility with the prior single-decision runtime.

Thread dependencies are explicit. If a scale decision depends on unresolved quality and regulatory decisions, the scale thread emits `HOLD` rather than pretending P10 is ready. Hard safety/authority escalation still outranks an ordinary dependency hold.

See [`docs/DECISION_THREADS.md`](docs/DECISION_THREADS.md), [`docs/adr/0005-anchor-preserved-decision-threads.md`](docs/adr/0005-anchor-preserved-decision-threads.md), and [`packages/schemas/decision-thread.schema.json`](packages/schemas/decision-thread.schema.json).

## Machine access for AI systems

Toledo exposes three machine-first surfaces:

1. **Protocol API** — HTTP/FastAPI reference service.
2. **MCP server** — stdio MCP tools/resources for AI agents.
3. **Equation readout index** — pinned machine-readable mirror of the upstream Toledo citizen-bridge proposal family.

Start here:

```text
llms.txt
docs/PROBLEM_CAPABILITY_GRAMMAR.md
docs/DECISION_THREADS.md
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
→ optional SIGNATURE_CANDIDATES_UPDATED / SIGNATURE_ENDORSED / BARRIER_UPDATED
→ create or inspect Decision Threads
→ advance_case
→ world/institution action
→ update_case or advance_case(event, optionally scoped by thread_id)
→ Return Object when an external actor was used
→ thread outcome(s)
→ citizen-level OUTCOME_UPDATED
→ STOP when closure is satisfied
```

`step_case()` returns both:

```text
protocol            # primary-thread compatibility surface
thread_protocols[]  # all concurrent decision subgraphs
```

New AI agents SHOULD inspect all thread protocols before recommending a material downstream decision.

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

The Problem & Capability Grammar and Decision Thread layer do not create new Toledo equations. Any future equation change belongs upstream.

## Core invariants

```text
AI-first != AI-only
Observation != Interpretation != Diagnosis
P_C != P_S != P_D != ProblemSignature
Occupation != ProtocolSelector
PracticeContext != IrrelevantContext
ProblemSignature != Diagnosis
CandidateSignature != EndorsedSignature
Unknown != Failure
MissingEvidence != NegativeEvidence
DomainAdapter != NewCore
ProviderName != Capability
Case != SingleDecision
DecisionThread != NewCase
ThreadPhase != CaseMaturity
BlockedThread != FailedCase
ThreadClosure != CaseClosure
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

## Closure semantics

External work must return to the citizen through the Return Gate.

A local citizen+AI/world thread that never used an external actor does not need a fake institutional Return Object. It may close only when the thread outcome reaches a closure state and no unresolved hard safety/authority trigger remains.

```text
local thread:
external_actor_used = false
+ Return Gate = NOT_APPLICABLE
+ thread outcome
+ safety/authority satisfied
→ thread CLOSED

external thread:
external_actor_used = true
+ Return Gate = PASS
+ thread outcome
→ thread CLOSED
```

For a multi-decision case, case closure is stronger:

```text
all required non-cancelled threads CLOSED
+ citizen-level outcome satisfied
+ shared hard safety/authority state cleared
→ case CLOSED
```

## Routing phases

`P0`–`P11` are routing coordinates, not a maturity ranking or mandatory funnel. They now apply to each active Decision Thread rather than forcing one scalar phase onto an entire complex case.

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

A thread may terminate successfully at any appropriate phase. The case may contain other active threads at other phases.

## Cross-actor architecture

```text
                           ACADEMIC / EXPERT
                                  ↕
                                  │
CITIZEN ↔ AI ↔ CASE STEWARD ↔ CASE PASSPORT
                                  │
                         DECISION THREADS
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

The platform routes by **capability, eligibility, access, evidence need, time fit, rights, dependencies, and burden** — not prestige, occupation, or industry label.

## Global core, local adapters

The global core is jurisdiction-neutral and domain-neutral at the protocol level.

Country adapters contain institutions, regulators, standards, public programs, language, and local access constraints.

Optional domain adapters add specialized vocabulary, hazards, measurement/sample rules, professional boundaries, regulation or provider mappings only when materially required.

Current country adapter:

- [`adapters/thailand/`](adapters/thailand/) — reference adapter with evidence-backed institution seed data and explicit known gaps.

## Documentation

Start with [`docs/README.md`](docs/README.md).

Key runtime documents:

- [`docs/PROBLEM_CAPABILITY_GRAMMAR.md`](docs/PROBLEM_CAPABILITY_GRAMMAR.md)
- [`docs/DECISION_THREADS.md`](docs/DECISION_THREADS.md)
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

Machine-readable contracts live in [`packages/schemas/`](packages/schemas/), including Case Passport, Decision Thread, Case Event, Case Step request/response, Problem Signature, Return Object, institution records, country adapters, protocol compile requests and protocol instances.

## Repository layout

```text
apps/
  protocol_api/            HTTP Protocol API
  mcp_server/              MCP server for AI agents
  citizen-web/             future citizen UI
  steward-console/         future steward UI
src/toledo_runtime/        deterministic runtime + closed-loop case/thread engine
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
