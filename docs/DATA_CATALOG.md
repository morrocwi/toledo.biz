# Data Catalog

This catalog identifies the machine-readable and evidence-backed datasets currently maintained in Toledo Citizen Platform.

Machine-readable catalog:

```text
registry/DATA_CATALOG.json
```

The JSON catalog is checked in CI for unique dataset IDs and valid local paths. This document explains the domains and governance expectations around those entries.

## Catalog

| Dataset / contract | Path | Scope | Authority | Volatility |
|---|---|---|---|---|
| Case Passport schema | `packages/schemas/case-passport.schema.json` | global | machine contract | schema-versioned |
| Return Object schema | `packages/schemas/return-object.schema.json` | global | machine contract | schema-versioned |
| Institution Record schema | `packages/schemas/institution-record.schema.json` | global | machine contract | schema-versioned |
| Country Adapter Manifest schema | `packages/schemas/country-adapter-manifest.schema.json` | global | machine contract | schema-versioned |
| Thailand adapter manifest | `adapters/thailand/adapter.manifest.json` | Thailand | adapter metadata | medium |
| Thailand institution seed | `adapters/thailand/institutions.seed.json` | Thailand | public routing metadata | high by field |
| Thailand source index | `adapters/thailand/SOURCES.md` | Thailand | evidence index | medium/high |
| Equation binding table | `docs/EQUATION_BINDINGS.md` | global implementation | binding metadata; upstream math governs | upstream-dependent |

## Data domains

### 1. Case data

Schemas exist here, but real case instances MUST NOT be stored in this public repository.

Production case data includes:

```text
citizen intake
Case Passport
Return Objects
consent scopes
private evidence
institution handoff events
world-result updates
```

This domain is privacy-sensitive.

### 2. Public institution data

Country adapters may store public mechanism metadata such as:

```text
capability
phase fit
eligibility
entry channel
coverage
cost/co-funding
turnaround
legal authority
accreditation
source
last_verified
fallback
```

This domain is time-sensitive.

### 3. Regulatory / standards data

Future adapter datasets should separate regulators, mandatory standards, and legal authority from general support-service records where doing so improves safety and maintainability.

This domain is jurisdiction-specific and high-consequence.

### 4. Equation bindings

This repository stores references/bindings only. Equation statements and canonical status belong to `morrocwi/toledo`.

This domain is provenance-sensitive rather than operationally volatile.

### 5. Localization data

Future machine-readable localization should distinguish:

```text
citizen UI language
institution official name
technical translation
legal/regulatory source language
```

Translations do not become new legal/technical authorities.

## Dataset metadata expectations

Every maintained dataset should eventually declare:

```text
dataset_id
schema_version
dataset_version_or_snapshot
jurisdiction
source/provenance policy
last_reviewed
maintainer
license
known_gaps
```

## Freshness principle

Freshness is field-specific.

For example:

```text
institution name          low volatility
program eligibility       medium/high volatility
application window        high volatility
current queue/capacity    very high volatility
legal authority           high consequence; effective-version check required
```

Do not assign one universal expiry period to all fields.

## Audit principle

Production systems should be able to reconstruct:

```text
which data version was used
which institution record was selected
which source supported it
which equation/rule version drove routing
which fallback existed
which result returned
```

This is necessary for trustworthy citizen/institution orchestration.

## Catalog update rule

Whenever a new maintained dataset or machine contract is added:

1. add it to `registry/DATA_CATALOG.json`;
2. document its scope and authority;
3. link its schema when applicable;
4. record source/freshness policy for external data;
5. update this human-readable catalog when the data domain is materially new.
