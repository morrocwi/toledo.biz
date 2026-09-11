# Equation Bindings

`toledo.biz` consumes Toledo mathematics; it does not own it.

## Source authority

Canonical/proposed source repository:

`https://github.com/morrocwi/toledo`

Current citizen-bridge proposal registry:

```text
path: registry/proposals/TOLEDO_CITIZEN_BRIDGE_v0.17.json
proposal registration commit: 361546c934829de56f3dcff2032c740209de847a
status: new derivation/proposal
```

Human-readable equation register:

```text
path: docs/TOLEDO_CITIZEN_BRIDGE_EQUATIONS_v0.17.md
document commit: ef20d326e766a1579f2800f79eb58fe0b5d7a708
```

Upstream promotion tracking:

```text
morrocwi/toledo issue #20
Promote Toledo Citizen Bridge v0.17 proposals into canonical registry
```

## Binding status vocabulary

```text
canonical   = promoted into upstream canonical registry
proposal    = repository-grounded proposal, not yet canonical
superseded  = no longer current for new implementation
unbound     = implementation behavior has no upstream equation binding yet
```

The current citizen-bridge family is `proposal` unless an individual binding is later promoted upstream.

## Initial bindings

| Implementation concern | Toledo proposal ID | Status |
|---|---|---|
| experiential capital | `TCB-E001` | proposal |
| provisional `K*_0` | `TCB-E002` | proposal |
| institutionally escalated `K*_I` | `TCB-E003` | proposal |
| institutional escalation need | `TCB-R001` | proposal |
| total route cost | `TCB-C001` | proposal |
| minimum-cost sufficient route | `TCB-R002` | proposal |
| citizen action readiness | `TCB-A001` | proposal |
| next-best information action | `TCB-F001` | proposal |
| field risk exposure | `TCB-F002` | proposal |
| innovation promotion gate | `TCB-F005` | proposal |
| knowledge-like asset map | `TCB-K001` | proposal |
| utilization route value / selection | `TCB-U001`, `TCB-U002` | proposal |
| Business-0 formation / first cycle | `TCB-B001`, `TCB-B002` | proposal |
| true resource cost / milestone runway | `TCB-B003`, `TCB-B004` | proposal |
| sustainable capacity / execution debt | `TCB-G002`, `TCB-G003` | proposal |
| institution utility | `TCB-I001` | proposal |
| problem representation triplet | `TCB-X001` | proposal |
| meaning preservation | `TCB-X002` | proposal |
| valid handoff | `TCB-X003` | proposal |
| response-time fit | `TCB-X004` | proposal |
| return gate | `TCB-X005` | proposal |
| bridge integrity | `TCB-X006` | proposal |
| cross-actor utility | `TCB-X007` | proposal |
| citizen closure | `TCB-X008` | proposal |

## Implementation binding contract

A code path that implements a mathematical/proposal rule SHOULD be able to expose:

```text
equation_ref
source_repo
source_commit
upstream_status
implementation_version
implementation_note
```

Example:

```json
{
  "equation_ref": "TCB-X003",
  "source_repo": "morrocwi/toledo",
  "source_commit": "361546c934829de56f3dcff2032c740209de847a",
  "upstream_status": "proposal",
  "implementation_version": "0.1.0",
  "implementation_note": "Typed handoff validation predicate."
}
```

## Binding rule

Until an entry is promoted to Toledo `registry/CANONICAL.json`, application code and documentation must preserve the status:

```text
new derivation/proposal
```

Do not present proposal equations to citizens or researchers as scientifically validated universal laws. Several entries are planning/governance heuristics, definitions, or typed predicates rather than empirical laws.

When upstream promotion occurs:

1. update this table to the canonical Toledo code;
2. pin the tested upstream commit;
3. preserve old proposal IDs as migration aliases where needed;
4. rerun routing/safety tests affected by the semantics;
5. record the migration in `CHANGELOG.md`.

## Boundary rule

```text
Upstream equation statement/status
    >
local copied prose or implementation comment
```

If this file disagrees with `morrocwi/toledo`, the upstream registry governs and this binding file must be repaired.
