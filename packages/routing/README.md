# `packages/routing`

Capability-first routing engine.

Planned responsibilities:

- minimum-sufficient route selection;
- institutional escalation decision;
- institution capability matching;
- eligibility and accessibility checks;
- response-time fit;
- fallback route selection;
- cross-actor utility evaluation;
- explanation trace: why this route, why not another route.

Routing order:

```text
hard safety / authority gates
    ↓
required capability
    ↓
eligibility / accessibility
    ↓
time fit
    ↓
decision gain vs total burden
    ↓
route
```

Never route by institution prestige alone.

Country-specific institution registries live under `adapters/<country>/`.
