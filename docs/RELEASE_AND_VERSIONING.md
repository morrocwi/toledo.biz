# Release and Versioning Policy

Toledo Citizen Platform has several independently changing artifacts. A single version number is not enough to describe all of them.

## 1. Version families

The project tracks at least six version families:

```text
Public citation / platform version
Runtime package version
Protocol Compiler version
Schema generation
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

The public citation version does not have to change for every pre-alpha runtime commit.

## 3. Runtime package version

The executable Python package has its own SemVer declared in `pyproject.toml` and `toledo_runtime.__version__`.

The current pre-alpha runtime line is `0.3.x`.

## 4. Protocol Compiler version

Compiler semantics are versioned separately because a runtime release may contain implementation fixes without changing the protocol contract.

Current reference line:

```text
Protocol Compiler v0.2
```

A material change to case-state transition, typed-gate behavior, closure semantics or next-action selection requires a compiler version review.

## 5. Schema version

Machine-readable schemas SHOULD carry an explicit version in their `$id`, metadata, or documented release mapping.

A schema breaking change requires either:

- a new schema major version; or
- a documented migration path with compatibility handling.

Do not change required semantics silently while leaving consumers unable to identify the schema generation.

## 6. Country-adapter version

Country adapters version separately from the platform because public programs, regulations, institutions, and entry channels change independently.

Recommended fields:

```text
adapter_version
last_reviewed
data_snapshot_date
upstream_platform_compatibility
```

A data refresh does not necessarily require a platform release.

## 7. Data snapshot date

Time-sensitive registry datasets SHOULD expose a snapshot date such as:

```text
2026-09-11
```

Individual records still keep their own `last_verified` metadata.

## 8. Equation baseline

`morrocwi/toledo` is the mathematical source of truth.

This repository SHOULD record:

```text
source repository
commit or release/tag when available
canonical equation IDs or proposal IDs
binding status
```

Implementation behavior tied to an upstream equation should be reproducible against that exact baseline.

## 9. Binding status

Recommended equation-binding states:

```text
canonical
proposal
superseded
unbound
```

`proposal` MUST NOT be presented as a canonical Toledo equation.

## 10. Release maturity

Use these project maturity labels independently from SemVer:

```text
specification
prototype
alpha
beta
production-candidate
stable
```

The current repository is a **pre-alpha executable reference runtime**: deterministic compiler, closed-loop Case Passport engine, schemas, API and MCP exist, but production persistence, domain validation, security deployment and broad interoperability testing are not complete.

## 11. Document status

Normative documents SHOULD identify whether they are:

```text
Draft
Current
Deprecated
Superseded
```

See [`SPECIFICATION_STATUS.md`](SPECIFICATION_STATUS.md).

## 12. Change categories

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

## 13. Breaking changes

Examples of breaking changes:

- removing a required Case Passport field;
- changing Case Event meaning incompatibly;
- changing case identity/version semantics;
- changing hard-gate semantics;
- changing citizen closure semantics;
- changing `P0`–`P11` meanings incompatibly;
- changing `PASS/HOLD_UNKNOWN/FAIL/N/A` interpretation;
- collapsing separate rights fields into one;
- changing an institution identifier to refer to a different mechanism;
- changing equation meaning locally without upstream Toledo update.

## 14. Non-breaking changes

Examples:

- adding optional institution metadata;
- adding a new country adapter;
- adding new capability codes while preserving existing mapping;
- improving documentation;
- adding a new fallback route;
- refreshing `last_verified` data.

## 15. Release checklist

Before a tagged release:

- [ ] schemas parse and validation tests pass;
- [ ] runtime tests pass;
- [ ] API and MCP smoke imports pass;
- [ ] normative docs agree with schemas;
- [ ] equation bindings identify upstream status;
- [ ] adapter data has provenance and snapshot date;
- [ ] changelog is updated;
- [ ] security/privacy boundary is unchanged or explicitly reviewed;
- [ ] migration notes exist for breaking changes;
- [ ] synthetic examples contain no sensitive real case data;
- [ ] repository status document is updated;
- [ ] citation metadata version is updated when a release is actually cut.

## 16. No fake releases

Do not update citation/release metadata to a version that has not actually been released/tagged under the project's chosen release process.

Documentation may describe a `draft` or reference protocol/runtime version without pretending that a public release exists.
