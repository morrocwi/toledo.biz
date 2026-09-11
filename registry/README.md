# Implementation Registry Contract

This directory contains implementation-side registries and read mirrors for Toledo Citizen Platform. It does **not** own Toledo mathematics.

Canonical/proposal equation authority belongs to `https://github.com/morrocwi/toledo`.

## Authority boundary

```text
morrocwi/toledo
    equation statement / lineage / canonical status

morrocwi/toledo.biz/registry
    implementation binding / compatibility / read mirror / data catalog
```

A copied equation string is never more authoritative than the upstream registry entry it came from.

## Equation read mirror

`equation-index.json` exists so APIs, MCP clients and other AI systems can read the bound citizen-bridge family immediately without scraping prose.

It MUST carry:

```text
source repo
source path
pinned source commit
upstream status
authority = mirror_only
```

The runtime may optionally fetch the pinned upstream file live. If live retrieval fails, it may fall back to the local mirror only if the fallback is disclosed.

## Machine data catalog

`DATA_CATALOG.json` inventories schemas, adapter datasets, equation bindings and machine-readable mirrors.

## Required equation binding fields

Implementation behavior that materially depends on Toledo mathematics should expose:

```text
equation_ref
source_repo
source_commit_or_release
upstream_status
implementation_version
implementation_note
```

`proposal` must remain visibly a proposal until upstream promotion.

## Short rule

```text
Equation meaning comes from morrocwi/toledo.
Implementation behavior comes from bound code/spec here.
Country/service facts come from evidence-backed adapters.
Citizen case data does not belong in this public registry.
```
