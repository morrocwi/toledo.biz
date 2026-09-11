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
toledo://schema/case-passport
toledo://schema/case-event
toledo://schema/case-step-request
toledo://schema/protocol-instance
```

## Authority rule

MCP responses MUST preserve upstream equation provenance. The equation mirror in `toledo.biz` is a read mirror; mathematical authority remains `morrocwi/toledo`.

## Suggested AI workflow

1. read `toledo://protocol/compiler` and `toledo://protocol/case-lifecycle`;
2. call `initialize_case` for a new citizen problem;
3. use `advance_case` after each observation, action, route result or institutional return;
4. search/get only equations needed for the current Protocol Instance;
5. route institutions only when the protocol requires external capability;
6. validate handoff before treating referral as collaboration;
7. preserve the same Case Passport when a route fails;
8. require Return Gate plus citizen outcome before closure;
9. stop when the compiler emits `STOP`.

## P_C rule

`citizen_problem_verbatim` is the machine representation of `P_C` and ordinary Case Events cannot overwrite it. AI restructuring and disciplinary reframing must use separate fields.

## Storage boundary

The reference MCP server does not persist citizen passports. The host application is responsible for secure storage if persistence is needed.

## Safety

The MCP server is an orchestration/readout layer. A host or agent MUST NOT treat an MCP tool response as licensed professional judgment, laboratory evidence, regulatory approval, or independent external validation unless the returned case state explicitly contains that external authority/evidence.
