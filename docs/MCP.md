# Toledo MCP Server

The MCP server makes Toledo directly readable and executable by other AI systems without requiring them to scrape prose documentation.

## SDK / transport

The reference server targets the stable MCP Python SDK v2 line:

```text
mcp>=2.2,<3
MCPServer
stdio transport
```

## Run

```bash
python -m pip install -e .
toledo-mcp
```

Transport: `stdio`.

## Tools

### Equation readout

```text
get_equation(equation_id, live=false)
search_equations(query="", domain="", live=false)
```

### Protocol and Case Passport lifecycle

```text
compile_citizen_protocol(case)
initialize_case(case)
update_case(passport, event)
advance_case(payload)
```

`advance_case` is the preferred closed-loop tool. It accepts a new case or an existing caller-held Case Passport plus optional event(s), then returns the next passport version and Protocol Instance.

### Routing and gates

```text
route_institutions(phase, capability="", jurisdiction="TH", target_user="", limit=5)
check_handoff(payload)
check_return_gate(payload)
```

## Resources

```text
toledo://equations/index
toledo://equations/{equation_id}
toledo://protocol/compiler
toledo://protocol/case-lifecycle
toledo://protocol/problem-capability-grammar
toledo://schema/case-passport
toledo://schema/case-event
toledo://schema/case-step-request
toledo://schema/problem-signature
toledo://schema/protocol-instance
```

## Problem & Capability Grammar rule

An AI agent MUST NOT create one core protocol per occupation merely because the citizen names a profession or domain.

```text
Occupation != ProtocolSelector
PracticeContext != IrrelevantContext
ProblemSignature != Diagnosis
CandidateSignature != EndorsedSignature
```

The citizen's occupation/practice history may carry important situated experience and should remain in `practice_context`. Candidate Problem Signatures may be proposed with provenance and may remain unresolved.

Agents should read:

```text
toledo://protocol/problem-capability-grammar
toledo://schema/problem-signature
```

before implementing their own problem abstraction layer.

## Authority rule

MCP responses MUST preserve upstream equation provenance. The equation mirror in `toledo.biz` is a read mirror; mathematical authority remains `morrocwi/toledo`.

The Problem & Capability Grammar is a product/runtime architecture, not a new canonical equation family or validated universal ontology.

## Suggested AI workflow

1. read `toledo://protocol/problem-capability-grammar`, `toledo://protocol/compiler` and `toledo://protocol/case-lifecycle`;
2. call `initialize_case` for a new citizen problem;
3. preserve `P_C` and, when useful, record multiple candidate Problem Signatures rather than forcing one diagnosis;
4. use `SIGNATURE_ENDORSED` only when endorsement is actually obtained;
5. keep unobserved context as unknown rather than inventing event-specific facts;
6. use `advance_case` after each observation, action, route result or institutional return;
7. search/get only equations needed for the current Protocol Instance;
8. route institutions only when the protocol requires external capability;
9. validate handoff before treating referral as collaboration;
10. preserve the same Case Passport when a route fails;
11. require Return Gate plus citizen outcome when an external actor was used;
12. allow a low-risk citizen+AI/world-only local case to close without fabricating an institutional Return Object;
13. stop when the compiler emits `STOP`.

## P_C rule

`citizen_problem_verbatim` is the machine representation of `P_C` and ordinary Case Events cannot overwrite it. AI restructuring, candidate Problem Signatures and disciplinary reframing must use separate fields.

## Unknown/context rule

```text
Unknown != Failure
MissingEvidence != NegativeEvidence
UnobservedContext != AIInferredFact
```

If the available record does not support a distinction, ask, observe, retrieve, measure, or preserve `HOLD_UNKNOWN` rather than silently lifting the claim.

## Storage boundary

The reference MCP server does not persist citizen passports. The host application is responsible for secure storage if persistence is needed.

## Safety

The MCP server is an orchestration/readout layer. A host or agent MUST NOT treat an MCP tool response as licensed professional judgment, laboratory evidence, regulatory approval, or independent external validation unless the returned case state explicitly contains that external authority/evidence.
