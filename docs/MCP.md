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

### Protocol, Decision Threads, and Case Passport lifecycle

```text
compile_citizen_protocol(case)
compile_case_threads(passport)
initialize_case(case)
update_case(passport, event)
advance_case(payload)
```

`advance_case` is the preferred closed-loop tool. It accepts a new case or an existing caller-held Case Passport plus optional event(s), then returns:

```text
passport
protocol              # primary-thread compatibility surface
thread_protocols[]    # all Decision Threads
primary_thread_id
```

`compile_case_threads` compiles every Decision Thread without applying a new event.

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
toledo://protocol/decision-threads
toledo://schema/case-passport
toledo://schema/case-event
toledo://schema/case-step-request
toledo://schema/problem-signature
toledo://schema/decision-thread
toledo://schema/protocol-instance
```

## Problem & Capability Grammar rule

An AI agent MUST NOT create one core protocol per occupation or industry merely because the citizen names a profession or domain.

```text
Occupation != ProtocolSelector
Industry != ProtocolSelector
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

## Decision Thread rule

One citizen case may contain several simultaneous decisions.

```text
Case != SingleDecision
DecisionThread != NewCase
ThreadPhase != CaseMaturity
BlockedThread != FailedCase
```

An agent MUST NOT collapse all active decisions into one scalar phase when the case contains materially different decision subgraphs.

Example:

```text
quality diagnosis -> P1
regulatory review -> P3
scale decision     -> P10 depends_on quality + regulatory
```

The P10 thread remains P10. While its dependencies are unresolved, its protocol returns:

```text
next_action = HOLD
status = HOLD_FOR_DEPENDENCY
```

Hard safety/authority escalation remains higher priority than an ordinary dependency hold.

Agents should read:

```text
toledo://protocol/decision-threads
toledo://schema/decision-thread
```

before implementing their own multi-decision orchestration.

## Thread-scoped events

Existing Case Events can target one Decision Thread by adding `thread_id` to the payload.

Examples:

```text
OBSERVATION_ADDED
UNKNOWN_ADDED
RISK_UPDATED
PHASE_CHANGED
SIGNATURE_CANDIDATES_UPDATED
BARRIER_UPDATED
CAPABILITY_REQUESTED
INSTITUTION_SELECTED
ROUTE_FAILED
HANDOFF_CHECKED
RETURN_RECEIVED
OUTCOME_UPDATED
```

Structural events are:

```text
DECISION_THREAD_CREATED
DECISION_THREAD_DEPENDENCIES_UPDATED
DECISION_THREAD_CANCELLED
PRIMARY_THREAD_SET
```

A thread-scoped event changes the decision subgraph, not `P_C` and not the Case ID.

## Authority rule

MCP responses MUST preserve upstream equation provenance. The equation mirror in `toledo.biz` is a read mirror; mathematical authority remains `morrocwi/toledo`.

The Problem & Capability Grammar and Decision Thread layer are product/runtime architecture, not a new canonical equation family or validated universal ontology.

## Suggested AI workflow

1. read `toledo://protocol/problem-capability-grammar`, `toledo://protocol/decision-threads`, `toledo://protocol/compiler` and `toledo://protocol/case-lifecycle`;
2. call `initialize_case` for a new citizen problem;
3. preserve `P_C` and, when useful, record multiple candidate Problem Signatures rather than forcing one diagnosis;
4. if the real case contains several material decisions, propose/record separate Decision Threads rather than collapsing them into one phase;
5. use `SIGNATURE_ENDORSED` only when endorsement is actually obtained;
6. keep unobserved context as unknown rather than inventing event-specific facts;
7. inspect **all** `thread_protocols` before recommending a downstream commitment such as scale, commercialization, public release, or irreversible action;
8. use `advance_case` after each observation, action, route result or institutional return;
9. search/get only equations needed for the current Protocol Instance;
10. route institutions only when the relevant thread requires external capability;
11. validate handoff before treating referral as collaboration;
12. preserve the same Case Passport and thread when a route fails;
13. require the thread Return Gate when an external actor was used;
14. allow a low-risk citizen+AI/world-only local thread to close without fabricating an institutional Return Object;
15. close a multi-decision case only after all required non-cancelled threads close and the citizen-level outcome condition is satisfied;
16. stop when the compiler emits `STOP`.

## P_C rule

`citizen_problem_verbatim` is the machine representation of `P_C` and ordinary Case Events cannot overwrite it. AI restructuring, candidate Problem Signatures, Decision Threads and disciplinary reframing must use separate fields.

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

The MCP server is an orchestration/readout layer. A host or agent MUST NOT treat an MCP tool response as licensed professional judgment, laboratory evidence, regulatory approval, or independent external validation unless the returned case/thread state explicitly contains that external authority/evidence.
