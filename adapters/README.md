# Country Adapters

Country adapters contain jurisdiction-specific routing data and localization for Toledo Citizen Platform.

The global product core remains jurisdiction-neutral. Each adapter answers:

```text
Which real institutions, regulators, standards, public programs,
languages, and access constraints apply in this jurisdiction?
```

## Directory contract

Recommended adapter layout:

```text
adapters/<country>/
  README.md
  adapter.manifest.json
  institutions.seed.json
  regulators.seed.json        # optional
  standards.seed.json         # optional
  localization/               # optional
  examples/                   # synthetic only
```

See [`../docs/COUNTRY_ADAPTER_STANDARD.md`](../docs/COUNTRY_ADAPTER_STANDARD.md).

## Current adapters

| Adapter | Status | Languages | Notes |
|---|---|---|---|
| [`thailand/`](thailand/) | reference | Thai, English | First reference adapter; public/university/innovation ecosystem seed |

## Rules

- Country adapters MUST NOT redefine global hard-gate semantics.
- Institution records MUST conform to the institution schema.
- Legal/regulatory claims MUST be jurisdiction-scoped and source-backed.
- Time-sensitive public-program claims MUST carry verification dates.
- Real citizen cases MUST NOT be stored here.
- External datasets MUST NOT be copied unless redistribution rights are clear.

## Adding an adapter

Before adding a country, provide:

1. adapter manifest;
2. country README;
3. verified public entry route(s);
4. at least a minimal institution registry;
5. explicit source and freshness metadata;
6. known gaps and unknowns;
7. compatibility with the current global core.

A narrow, honest adapter is preferred over a broad adapter that guesses current availability.
