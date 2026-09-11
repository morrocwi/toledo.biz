# Release and Versioning Policy

Toledo Citizen Platform has several independently changing artifacts. A single version number is not enough to describe all of them.

## 1. Version families

The project tracks at least four version families:

```text
Platform version
Schema version
Country-adapter version / data snapshot
Upstream Toledo equation baseline
```

These MUST remain distinguishable.

## 2. Platform version

Use Semantic Versioning for the citizen platform implementation/specification:

```text
MAJOR.MINOR.PATCH
```

Guidance:

- `MAJOR`: incompatible change to public platform contracts or core semantics;
- `MINOR`: backward-compatible feature/specification expansion;
- `PATCH`: backward-compatible correction, clarification, or data/doc fix.

Pre-1.0 versions indicate that contracts may still evolve substantially.

## 3. Schema version

Machine-readable schemas SHOULD carry an explicit version in their `$id`, metadata, or documented release mapping.

A schema breaking change requires either:

- a new schema major version; or
- a documented migration path with compatibility handling.

Do not change required semantics silently while leaving consumers unable to identify the schema generation.

## 4. Country-adapter version

Country adapters version separately from the platform because public programs, regulations, institutions, and entry channels change independently.

Recommended fields:

```text
adapter_version
last_reviewed
data_snapshot_date
upstream_platform_compatibility
```

A data refresh does not necessarily require a platform release.

## 5. Data snapshot date

Time-sensitive registry datasets SHOULD expose a snapshot date such as:

```text
2026-09-11
```

Individual records still keep their own `last_verified` metadata.

## 6. Equation baseline

`morrocwi/toledo` is the mathematical source of truth.

This repository SHOULD record:

```text
source repository
commit or release/tag when available
canonical equation IDs or proposal IDs
binding status
```

Implementation behavior tied to an upstream equation should be reproducible against that exact baseline.

## 7. Binding status

Recommended equation-binding states:

```text
canonical
proposal
superseded
unbound
```

`proposal` MUST NOT be presented as a canonical Toledo equation.

## 8. Release maturity

Use these project maturity labels independently from SemVer:

```text
specification
prototype
alpha
beta
production-candidate
stable
```

The current repository remains specification-first until the deterministic routing engine and schema-validation tests exist.

## 9. Document status

Normative documents SHOULD identify whether they are:

```text
Draft
Current
Deprecated
Superseded
```

See [`SPECIFICATION_STATUS.md`](SPECIFICATION_STATUS.md).

## 10. Change categories

Changelog entries should use:

```text
Added
Changed
Deprecated
Removed
Fixed
Security
Data
Governance
```

## 11. Breaking changes

Examples of breaking changes:

- removing a required Case Passport field;
- changing hard-gate semantics;
- changing `P0`–`P11` meanings incompatibly;
- changing `PASS/HOLD_UNKNOWN/FAIL/N/A` interpretation;
- collapsing separate rights fields into one;
- changing an institution identifier to refer to a different mechanism;
- changing equation meaning locally without upstream Toledo update.

## 12. Non-breaking changes

Examples:

- adding optional institution metadata;
- adding a new country adapter;
- adding new capability codes while preserving existing mapping;
- improving documentation;
- adding a new fallback route;
- refreshing `last_verified` data.

## 13. Release checklist

Before a tagged release:

- [ ] schemas parse and validation tests pass;
- [ ] normative docs agree with schemas;
- [ ] equation bindings identify upstream status;
- [ ] adapter data has provenance and snapshot date;
- [ ] changelog is updated;
- [ ] security/privacy boundary is unchanged or explicitly reviewed;
- [ ] migration notes exist for breaking changes;
- [ ] synthetic examples contain no sensitive real case data;
- [ ] repository status document is updated;
- [ ] citation metadata version is updated when a release is actually cut.

## 14. No fake releases

Do not update citation/release metadata to a version that has not actually been released/tagged under the project's chosen release process.

Documentation may describe a `draft` specification version without pretending that a release exists.
