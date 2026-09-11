# Toledo MCP Server

The MCP server makes Toledo directly readable by other AI systems without requiring them to scrape prose documentation.

## Run

```bash
python -m pip install -e .
toledo-mcp
```

Transport: `stdio`.

## Tools

```text
get_equation(equation_id, live=false)
search_equations(query="", domain="", live=false)
compile_citizen_protocol(case)
route_institutions(phase, capability="", jurisdiction="TH", target_user="", limit=5)
check_handoff(payload)
check_return_gate(payload)
```

## Resources

```text
toledo://equations/index
toledo://equations/{equation_id}
toledo://protocol/compiler
toledo://schema/case-passport
toledo://schema/protocol-instance
```

## Authority rule

MCP responses MUST preserve upstream equation provenance. The equation mirror in `toledo.biz` is a read cache; mathematical authority remains `morrocwi/toledo`.

## Suggested AI workflow

1. read `toledo://protocol/compiler`;
2. search/get only equations needed for the current case;
3. compile a protocol instance;
4. route institutions only when the protocol requires external capability;
5. validate handoff before treating referral as collaboration;
6. require Return Gate before institutional work closes the case.
