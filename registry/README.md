# Implementation Registry Contract

This directory contains **implementation-side registries and bindings** for Toledo Citizen Platform.

It does **not** own Toledo mathematics.

Canonical equation provenance belongs to:

`https://github.com/morrocwi/toledo`

## Authority boundary

```text
morrocwi/toledo
    equation statement / lineage / canonical status

morrocwi/toledo.biz/registry
    implementation binding / compatibility / local registry metadata
```

A copied equation string is never more authoritative than the upstream registry entry it came from.

## What may live here

This repository may maintain implementation registries for:

- institution capabilities;
- country/jurisdiction adapters;
- UI/state labels;
- route adapters;
- safety-policy mappings;
- localization strings;
- equation-to-code bindings;
- compatibility and migration metadata.

It must not silently redefine the canonical statement of an upstream Toledo equation.

## Required equation binding fields

Every implementation rule that materially depends on Toledo mathematics should be able to identify:

```text
equation_ref
source_repo
source_commit_or_release
upstream_status
implementation_version
implementation_note
```

Recommended upstream status values:

```text
canonical
proposal
superseded
unbound
```

`proposal` must remain visibly a proposal until upstream canonical promotion.

## Citizen bridge equation family

The citizen / institutional / cross-actor equation family developed through Toledo v0.17 is currently registered upstream through:

```text
morrocwi/toledo/docs/TOLEDO_CITIZEN_BRIDGE_EQUATIONS_v0.17.md
morrocwi/toledo/registry/proposals/TOLEDO_CITIZEN_BRIDGE_v0.17.json
```

These are repository-grounded proposals pending canonical registry promotion. `toledo.biz` should bind to proposal IDs/status honestly rather than invent canonical codes.

## Versioning

When an upstream equation changes:

1. update the binding;
2. preserve old implementation behavior where audit/migration requires it;
3. record migration impact;
4. re-run affected routing/safety tests;
5. update changelog/status documentation when behavior changes materially.

See [`../docs/RELEASE_AND_VERSIONING.md`](../docs/RELEASE_AND_VERSIONING.md).

## Data registries are different

Institution/country data follows a different governance path from equations.

Institution data is:

```text
time-sensitive
jurisdiction-specific
provenance-dependent
operationally re-verifiable
```

See:

- [`../docs/DATA_GOVERNANCE.md`](../docs/DATA_GOVERNANCE.md)
- [`../docs/INSTITUTION_REGISTRY_STANDARD.md`](../docs/INSTITUTION_REGISTRY_STANDARD.md)
- [`../docs/COUNTRY_ADAPTER_STANDARD.md`](../docs/COUNTRY_ADAPTER_STANDARD.md)

Do not confuse equation authority with public-service data freshness.

## Short rule

```text
Equation meaning comes from morrocwi/toledo.
Implementation meaning comes from bound code/spec here.
Country/service facts come from evidence-backed adapters.
Citizen case data does not belong in this public registry.
```
