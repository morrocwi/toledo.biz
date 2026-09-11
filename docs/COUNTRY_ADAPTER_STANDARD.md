# Country Adapter Standard

Country adapters specialize the jurisdiction-neutral Toledo core without contaminating it with one country's institutions, language, laws, or administrative assumptions.

## 1. Principle

```text
Global Core
    +
Country Adapter
    =
Jurisdiction-Executable Toledo Route
```

A country adapter MAY specialize local institutions, regulation, language, geography, access, standards, and public programs. It MUST NOT silently redefine upstream Toledo mathematics or universal platform invariants.

## 2. Required directory shape

Each adapter SHOULD follow:

```text
adapters/<country-code>/
  README.md
  adapter.manifest.json
  institutions.seed.json
  regulators.seed.json          # optional until needed
  standards.seed.json           # optional until needed
  localization/                 # optional
  examples/                     # synthetic only
```

Use lowercase ISO-style country codes for directories where practical, e.g. `thailand` for the human-readable reference implementation. Machine-readable manifest fields should use ISO 3166-1 alpha-2 codes such as `TH`.

## 3. Adapter manifest

Every production-grade adapter SHOULD declare:

```json
{
  "adapter_id": "TH",
  "name": "Thailand",
  "adapter_version": "0.1.0",
  "status": "reference",
  "languages": ["th", "en"],
  "jurisdictions": ["Thailand"],
  "institution_dataset": "institutions.seed.json",
  "last_reviewed": "2026-09-11",
  "maintainers": [],
  "upstream_platform_compatibility": ">=0.1.0"
}
```

## 4. Adapter status

Use:

```text
experimental
reference
supported
maintenance
archived
```

`reference` means useful as a design/example adapter; it does not imply guaranteed production service availability.

## 5. Required content

A country adapter should explain:

- citizen-facing public entry points;
- expert/university/laboratory routes;
- innovation and prototype support;
- IP and knowledge-utilization mechanisms;
- business/SME support;
- regulators and standards bodies;
- growth/export infrastructure;
- system/policy bodies;
- major language and geographic constraints;
- how live data is verified.

## 6. Global/core separation

Country adapters MUST NOT hard-code local assumptions into global definitions of:

```text
Case Passport
Return Object
Handoff
Citizen rights
Meaning preservation
Hard gate semantics
P0-P11 phase meanings
AI role boundary
```

If a country reveals a genuinely missing universal concept, propose that concept in the global core rather than smuggling it into a local adapter.

## 7. Legal and regulatory content

Legal/regulatory entries MUST identify the jurisdiction and source authority.

Adapters SHOULD distinguish:

```text
law / regulation
regulator guidance
program policy
institutional practice
informal advice
```

A government program page MUST NOT be treated as equivalent to law.

## 8. Public institution data

Institution records must conform to `packages/schemas/institution-record.schema.json` and [`INSTITUTION_REGISTRY_STANDARD.md`](INSTITUTION_REGISTRY_STANDARD.md).

Every time-sensitive routing record MUST include at least a public source and verification date.

## 9. Localization

Localization is more than translation.

Adapters SHOULD account for:

- language and script;
- public-service terminology;
- common citizen vocabulary;
- regional differences;
- local document conventions;
- access channels used in practice;
- culturally relevant ways to preserve citizen meaning.

Translated legal/technical summaries are informative renderings, not new authorities.

## 10. Geography and access

Country-wide programs may have uneven regional capacity.

Adapters SHOULD represent specific local nodes when:

```text
facility availability
expertise
language
queue time
travel burden
sample acceptance
local eligibility
```

materially affect routing.

## 11. Country-specific hard gates

Adapters MAY add jurisdiction-specific hard gates, such as:

```text
licensed professional requirement
regulatory authorization
mandatory conformity assessment
age/eligibility rule
restricted service category
```

Each such gate MUST cite its authority and MUST NOT be promoted into a global invariant unless universally justified.

## 12. Fallback design

Country adapters SHOULD avoid single-institution dependence.

For critical capabilities, record alternatives such as:

```text
local public service
university service
national laboratory
private accredited service
remote expert
standard practice / interim safe action
```

where applicable.

## 13. Evidence bundle

A mature adapter SHOULD maintain an evidence bundle or index showing:

```text
claim
source
source class
last verified
scope
notes
```

This can live in adapter-local metadata or a shared registry service.

## 14. Contribution checklist

A new country adapter PR should include:

- [ ] manifest;
- [ ] country README;
- [ ] at least one verified citizen-facing entry route;
- [ ] institution dataset conforming to schema;
- [ ] source URLs and dates;
- [ ] explicit unknowns and gaps;
- [ ] no copied restricted data;
- [ ] no sensitive citizen case data;
- [ ] examples are synthetic;
- [ ] regulator/standard claims distinguish legal authority from support services;
- [ ] compatibility with current global core documented.

## 15. Adapter quality

Do not score an adapter with one number. Review separately:

```text
coverage
freshness
source quality
regional granularity
language coverage
regulatory completeness
fallback diversity
citizen accessibility
```

A thin but honest adapter is preferable to a broad adapter that invents current availability.
