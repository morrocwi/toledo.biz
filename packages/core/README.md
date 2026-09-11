# `packages/core`

Jurisdiction-neutral case engine.

Planned responsibilities:

- case state types;
- P0–P11 phase coordinates;
- typed hard-gate states (`PASS`, `HOLD_UNKNOWN`, `FAIL`, `N/A` where applicable);
- Case Passport version transitions;
- problem representation separation (`P_C`, `P_S`, `P_D`);
- pre-innovation disposition;
- utilization-route state;
- Business-0 (`B0_F`, `B0_C`) state;
- deterministic audit events.

This package must not contain country-specific institution names or silently redefine upstream Toledo equations.

All equation-dependent logic should reference `docs/EQUATION_BINDINGS.md`.
