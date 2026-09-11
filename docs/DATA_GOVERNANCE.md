# Data Governance and Provenance Standard

This document defines how Toledo Citizen Platform handles public institutional data, implementation registries, synthetic examples, and metadata. It does **not** authorize storing real sensitive citizen cases in this public repository.

## 1. Scope

This standard applies to:

- institution capability records;
- country-adapter data;
- public-service routing metadata;
- equation-to-implementation bindings;
- synthetic fixtures and examples;
- documentation claims that may change over time.

Real citizen case data belongs in a private deployment governed by separate privacy, retention, access, and legal controls.

## 2. Data principles

1. **Provenance before convenience.** Every material external fact should be traceable to a source.
2. **Currentness is typed.** Historical evidence cannot be silently presented as current availability.
3. **Identity is not capability.** Record specific programs/services, not only institution names.
4. **Unknown is a valid state.** Missing cost, timing, eligibility, or availability should remain unknown rather than guessed.
5. **Claims are separable.** One source may support identity but not current availability, price, accreditation, or eligibility.
6. **Jurisdiction is explicit.** Country-specific facts stay in adapters.
7. **Hard authority is explicit.** Regulatory or legal authority must not be inferred from branding or public-sector ownership.
8. **No sensitive case data in public Git.** Public registries contain service metadata, not citizen dossiers.

## 3. Source hierarchy

Use the strongest available source for the claim being made.

| Source class | Description | Typical use |
|---|---|---|
| `S0` | Law, regulation, official regulator/standards source | legal authority, mandatory requirements, regulated scope |
| `S1` | Official institution/program/service source | current service identity, eligibility, entry channel, program description |
| `S2` | Official government report/open data/press release | activity, public performance, program outcomes |
| `S3` | Peer-reviewed academic research | system behavior, institutional effectiveness, structural interpretation |
| `S4` | Reputable independent secondary source | corroboration/context when primary source is unavailable |
| `S5` | Community report, forum, anecdotal evidence | discovery signal only; not sufficient for current official availability |

A lower source class MAY be useful for discovery, but MUST NOT silently override a stronger authoritative source.

## 4. Verification levels

Institution records should use one of the following verification levels:

```text
V0 = unverified / imported
V1 = one current official source checked
V2 = multiple compatible official/public sources checked
V3 = direct service/contact confirmation or equivalent operational evidence
```

`V3` is not required for every record. The level tells the router how much confidence to place in operational availability.

## 5. Freshness and volatility

Every time-sensitive record MUST have a verification date.

Recommended volatility classes:

```text
stable_identity       institution identity / mandate
service_catalog       ongoing service or facility
program_rules         eligibility / co-funding / program conditions
call_window           open/close application windows
operational_capacity  current availability / turnaround / queue
regulatory_rule       law / regulation / mandatory standard
```

Recommended review behavior:

- `stable_identity`: periodic review;
- `service_catalog`: review before production routing when stale;
- `program_rules`: verify before application;
- `call_window`: verify at routing time;
- `operational_capacity`: treat as unknown unless recently confirmed;
- `regulatory_rule`: verify effective/current version before consequential use.

The repository SHOULD avoid a false universal freshness interval because volatility differs by field.

## 6. Claim-level provenance

A mature record may contain several sources because different claims require different evidence.

Example:

```json
{
  "claim": "application window",
  "value": "2026-10-01/2026-10-31",
  "source_class": "S1",
  "source_url": "https://example.go.th/current-call",
  "verified_at": "2026-09-11T07:00:00Z"
}
```

Until claim-level provenance is fully implemented, `source_url`, optional `source_urls`, `last_verified`, and verification metadata act as the minimum contract.

## 7. Record lifecycle

Institution/service records SHOULD support:

```text
active
unknown
inactive
superseded
archived
historical
```

Rules:

- Do not delete a historically important record merely because a program closes.
- Mark it inactive/archived and link to a successor when known.
- Do not route a live case to `historical`, `archived`, or `inactive` records.
- `unknown` means current status could not be confirmed.

## 8. Conflict handling

When sources conflict:

1. preserve both claims;
2. prefer the more authoritative and more current source for operational routing;
3. record the conflict in notes or claim metadata;
4. downgrade availability to `unknown` when the conflict affects routing safety;
5. re-verify before consequential use.

Do not silently reconcile conflicting eligibility or legal requirements.

## 9. Stable identifiers

`institution_id` identifies a specific institution/mechanism record and SHOULD remain stable across wording changes.

Recommended form:

```text
<COUNTRY>-<INSTITUTION>-<MECHANISM>
```

Examples:

```text
TH-NSTDA-ITAP
TH-DIP-IPMART
```

Do not reuse an identifier for a materially different program.

## 10. Language and localization

Source language and display language are distinct.

A country adapter SHOULD record:

- source-language material where practical;
- localized display names;
- language availability of the service;
- translated summaries as non-authoritative renderings.

Translations MUST NOT silently expand legal, technical, or eligibility claims.

## 11. Personal and sensitive data

Public repository data MUST be non-case-specific.

Never commit:

- names or identifiers of real citizens from cases;
- medical/financial/legal records;
- exact private addresses;
- private credentials or contact details not already intended for publication;
- confidential research or patent-sensitive case material;
- restricted community knowledge.

Synthetic fixtures SHOULD be obviously synthetic and MUST NOT be reversible transformations of real sensitive cases.

## 12. Dataset licensing

Before importing an external dataset, verify its license and redistribution terms.

A public URL does not automatically imply redistribution permission.

Where redistribution is uncertain, store metadata and the source link rather than copying the entire external dataset.

## 13. Audit fields

A production-grade record SHOULD be able to answer:

```text
Who created this record?
Which source supports it?
When was it verified?
What changed?
Why did it change?
What prior state existed?
Which router decisions depended on it?
```

Git history provides repository-level change provenance; production systems should add record-level audit events.

## 14. Data quality dimensions

Do not reduce data quality to one number. Track separately:

```text
provenance_quality
freshness
completeness
operational_confirmability
jurisdiction_fit
capability_specificity
rights_to_redistribute
```

A record may be excellent on one dimension and weak on another.

## 15. Routing rule

Before a record is used for a consequential live route:

```text
identity is known
AND relevant capability is evidenced
AND eligibility is not known to fail
AND current availability is not falsely asserted
AND legal/authority status is verified where material
AND source freshness is appropriate to the claim
```

If any mandatory field is unresolved, route state should remain `HOLD_UNKNOWN` or use a verified fallback.
