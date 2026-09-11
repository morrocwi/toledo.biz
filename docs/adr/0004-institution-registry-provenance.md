# ADR-0004 — Institution Registry Requires Provenance and Freshness

- Status: Accepted
- Date: 2026-09-11

## Context

Public programs, application windows, service availability, eligibility, accreditation, entry channels, and turnaround times change frequently. A static list of institution names is not enough for safe routing.

## Decision

Institution routing data is treated as a versioned, evidence-backed dataset.

Every live record must have at least:

```text
specific mechanism identity
capability
phase fit
accessibility
eligibility information
public entry channel
public source
last-verified date
```

Mature records should add claim-level provenance, verification level, operational status, availability state, and fallback routes.

## Consequences

Positive:

- routing can distinguish known, stale, and unknown facts;
- public-service data can be audited;
- historical programs remain preserved without being mistaken for live routes;
- adapter contributors have a clear evidence standard.

Cost:

- records require recurring maintenance;
- some fields will remain `unknown` instead of being filled optimistically;
- live routing may need last-mile verification before consequential action.

## Rule

```text
Website exists != Service currently available
Historical funding != Current call
Institution mandate != Local operational capacity
Official source != Every claim on the record is current
```

When current availability cannot be confirmed, preserve `unknown` and use a verified fallback rather than inventing certainty.
