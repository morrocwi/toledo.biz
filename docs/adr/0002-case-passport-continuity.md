# ADR-0002 — Case Passport as the Cross-Actor Continuity Object

- Status: Accepted
- Date: 2026-09-11

## Context

Citizen cases may move across AI systems, experts, universities, laboratories, public services, funders, regulators, and market actors. Generic referral causes repeated re-telling, meaning drift, consent ambiguity, lost evidence, unclear decision ownership, and missing return obligations.

## Decision

Use a versioned **Case Passport** as the persistent continuity object.

The passport preserves at least:

```text
P_C citizen problem
P_S structured problem
P_D disciplinary formulation when present
citizen goal and constraints
evidence / unknowns / hypotheses
risk state
current phase / current decision
requested capability
decision owner
consent and data-use scope
rights / provenance state
previous actions and results
current actor / institution
response deadline
expected return
fallback route
```

Material reframing creates a new version; prior versions remain auditable.

## Consequences

Positive:

- citizens do not restart at every institution;
- original meaning remains visible;
- handoffs can be validated;
- institutional failure can reroute without discarding the case;
- consent and rights travel with context.

Cost:

- production deployments need access control and audit design;
- schema migration becomes a governance concern;
- privacy/data-minimization requirements are stronger than a simple referral system.

## Non-goals

The Case Passport does not itself transfer:

```text
IP ownership
authorship
inventorship
data ownership
professional decision authority
regulatory authority
```

It transports case state and governance metadata.
