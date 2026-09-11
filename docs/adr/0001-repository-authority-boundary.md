# ADR-0001 — Repository Authority Boundary

- Status: Accepted
- Date: 2026-09-11

## Context

Toledo spans mathematics, epistemology, ontology, human–AI collaboration, product implementation, country routing data, and citizen-facing workflows. Without explicit authority boundaries, equations can drift across repositories and product code can accidentally become a competing source of truth.

## Decision

Use the following authority split:

```text
morrocwi/toledo
    canonical Toledo mathematics and equation provenance

morrocwi/toledo.biz
    citizen-facing implementation, schemas, orchestration,
    routing, country adapters, and product governance

morrocwi/readout_genesis
    ontology lens

morrocwi/readout_universe
    epistemology lens

morrocwi/glosa
    human–AI / collaboration lens
```

`toledo.biz` may bind to equation IDs and implement them, but MUST NOT silently redefine them.

## Consequences

Positive:

- one mathematical source of truth;
- product iteration does not fragment equation lineage;
- country adapters remain implementation/data concerns;
- cross-domain interpretation remains reviewable.

Cost:

- some changes require coordinated upstream/downstream updates;
- proposal status must be tracked until canonical promotion;
- implementers must record exact equation baselines.

## Rejected alternatives

1. **Copy equations into `toledo.biz`.** Rejected because copies would drift.
2. **Make `toledo.biz` the umbrella authority.** Rejected because product concerns would contaminate mathematical provenance.
3. **Store all knowledge in one monorepo.** Rejected because domain authority and release cadence differ materially.
