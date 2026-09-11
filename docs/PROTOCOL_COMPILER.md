# Toledo Protocol Compiler v0.1

Status: **reference implementation / pre-alpha**.

The compiler turns a case state into the smallest relevant executable subgraph of Toledo.

```text
CaseState
    → ProtocolCompiler
    → MinimalRelevantSubgraph
    → NextAction
    → World / Institution
    → Return
    → UpdatedCaseState
```

It is deliberately not a P0→P11 conveyor belt. A case may stop successfully at any phase.

## Design rule

```text
AI interprets
Protocol engine controls typed gates
```

The reference compiler is deterministic. It does not permit an LLM to silently override hard safety, authority, consent, rights or Return Gate semantics.

## Core actions

```text
OBSERVE
STRUCTURE
MEASURE
ESCALATE
ACT
TEST
CHECK_PRIOR_ART
MAP_RIGHTS
SELECT_ROUTE
FORM_BUSINESS_0
CLOSE_FIRST_CYCLE
SCALE_CHECK
GLOBAL_CHECK
RETURN
```

## Input

Machine contract: `packages/schemas/protocol-compile-request.schema.json`.

Minimum input:

```json
{"problem":"Trees in the lower corner of my orchard decline after heavy rain."}
```

## Output

Machine contract: `packages/schemas/protocol-instance.schema.json`.

Every instance exposes equation references rather than copying mathematical authority into product code.

## Hard escalation reference rule

The reference implementation escalates when any configured hard trigger is present, including professional/regulatory authority requirements or high severity/irreversibility/third-party exposure. These thresholds are implementation defaults, not universal scientific laws. Deployments must review them by domain and jurisdiction.

## Equation status

Citizen-bridge equations are currently bound to the upstream v0.17 proposal family unless individually promoted in `morrocwi/toledo`.

The compiler MUST disclose that status. It MUST NOT present planning heuristics as validated physical or social laws.

## Safety boundary

This implementation is a routing/protocol reference. It is not itself a medical, legal, engineering, regulatory, laboratory or other licensed professional authority.
