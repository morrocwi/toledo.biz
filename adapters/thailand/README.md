# Thailand Reference Adapter

Thailand is the first jurisdictional reference adapter for Toledo Citizen Platform.

It translates the global citizen/problem/routing model into Thai institutions, public services, innovation infrastructure, business support, IP mechanisms, regulators, language, and access constraints.

**Status:** `reference` — useful for design, testing, and evidence-backed routing research; not yet a guarantee of production availability for every listed service.

## Adapter files

| File | Purpose |
|---|---|
| `adapter.manifest.json` | Adapter identity, version, compatibility, snapshot date, known gaps |
| `institutions.seed.json` | Initial institution/mechanism capability registry |
| `README.md` | Human-readable adapter guide |

Future production-grade expansion should separate regulator, standards, localization, and local-node datasets.

## Routing principle

For an ordinary citizen, the default order is usually:

```text
1. Citizen + AI
2. Low-friction local intermediary
3. Specialist expert / lab / science park
4. Innovation / IP / venture mechanism
5. Growth / regulatory / global mechanism
```

A hard safety, professional-authority, or legal gate may skip directly to the appropriate professional, laboratory, or regulator.

## Institutional topology

The seed dataset currently spans mechanisms such as:

```text
Technology Clinic Network / MHESI
Regional Science Parks
universities / academic services
NSTDA / ITAP / Thailand Science Park
TISTR
NIA
DIP / IP Mart
TED Fund
depa
PMUC
DIPROM
OSMEP
DBD
sector regulators / standards bodies
DITP
EXIM Thailand
NXPO / policy architecture
```

Institution name alone is not a route. Toledo routes to a **specific mechanism/capability**.

## Important distinctions

```text
DIP != DIPROM
DIP = Department of Intellectual Property
DIPROM = Department of Industrial Promotion

NIA support != regulatory authorization
IP Mart = matching channel, not commercialization vehicle
NXPO = system/policy architect, not normal citizen service counter
AcademicFit != UniversityExecutability
Government service != Government funding != Regulation
```

## Phase use

The adapter follows the global `P0`–`P11` routing coordinates.

Typical pattern:

| Phase range | Typical Thai capability |
|---|---|
| P0–P2 | Citizen+AI, ClinicTech, extension, nearby university/public service |
| P3 | expert, university lab, science park, NSTDA/ITAP, TISTR |
| P4–P5 | research, prototype, POC, NIA/TED/depa/PMUC where eligible |
| P6–P7 | DIP, TTO, IP Mart, science park, industry matching |
| P8–P9 | DBD, OSMEP, DIPROM, incubators, NIA/TED/depa where eligible |
| P10 | growth, quality, capacity, finance, standards/regulation |
| P11 | DITP, EXIM, NIA Global, international IP/regulatory routes |

This is a routing map, not a mandatory funnel.

## Data quality and freshness

`institutions.seed.json` is a starting registry, not a claim that every service is open now.

Every record currently carries at least:

```text
specific mechanism
phase fit
accessibility class
capability
entry channel
public source
last_verified
fallback route
```

Before production routing, re-verify volatile fields such as:

```text
eligibility
application window
contact/entry channel
cost/co-funding
turnaround
geographic/local capacity
accreditation where relevant
current availability
```

See:

- [`../../docs/DATA_GOVERNANCE.md`](../../docs/DATA_GOVERNANCE.md)
- [`../../docs/INSTITUTION_REGISTRY_STANDARD.md`](../../docs/INSTITUTION_REGISTRY_STANDARD.md)
- [`../../docs/COUNTRY_ADAPTER_STANDARD.md`](../../docs/COUNTRY_ADAPTER_STANDARD.md)

## Source policy

Prefer official Thai sources for current service and regulatory facts. Peer-reviewed research is valuable for system behavior and institutional interpretation but does not replace current official eligibility/availability sources.

Historical program evidence must not be presented as current availability.

## Language

A production Thailand adapter should support Thai as a first-class citizen language and preserve the citizen's original Thai wording before generating English or disciplinary translations.

Technical or legal translation must not silently expand claims or authority.

## Geographic granularity

National programs can have uneven local capacity. Future adapter versions should add specific regional/local nodes when routing depends on:

```text
facility
expertise
language
travel burden
sample acceptance
queue time
local eligibility
```

## Known gaps

The current reference adapter does not yet provide:

- exhaustive local university/lab nodes;
- real-time queue/turnaround data;
- complete regulator and standards datasets;
- machine-readable Thai localization bundle;
- live application-window monitoring.

These are recorded in `adapter.manifest.json` rather than hidden.

## Privacy boundary

Do not store citizen Case Passports or sensitive case data inside this adapter. This directory contains public routing metadata only.
