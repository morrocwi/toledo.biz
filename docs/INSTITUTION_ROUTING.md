# Institutional Routing

## Goal

A citizen should not need to understand the institutional ecosystem before receiving help.

Toledo should translate:

```text
current case state
→ required capability
→ best currently executable route
```

The system routes by capability, eligibility, accessibility, decision gain, timing, and burden.

## Capability classes

```text
I0 citizen-facing / community service
I1 expert / university intermediary
I2 technical / laboratory / prototype infrastructure
I3 innovation / venture development
I4 IP / knowledge-utilization infrastructure
I5 business / SME support
I6 regulator / standards authority
I7 growth / finance / market infrastructure
I8 global / export infrastructure
I9 policy / ecosystem orchestration
```

## Accessibility classes

```text
A0 system/policy body; not a normal citizen front door
A1 selective, call-based, eligibility-heavy
A2 defined target group / registered organization
A3 clear public service channel
A4 low-entry local / community / online front door
```

Accessibility is not quality.

## Routing rule

A route is evaluated on:

```text
capability fit
eligibility
accessibility
expected decision gain
response-time fit
money cost
time cost
coordination burden
rights risk
```

Hard safety, legal, or authority requirements override soft optimization.

## Institution record contract

See `packages/schemas/institution-record.schema.json`.

Every live record should include:

- mechanism/service name;
- institution class;
- phase fit;
- target user;
- accessibility;
- eligibility;
- entry channel;
- capability;
- geography/coverage;
- cost/co-funding when known;
- turnaround when known;
- legal authority/accreditation when relevant;
- public source;
- last-verified timestamp;
- fallback routes.

## Thailand reference adapter

Thailand is the first reference ecosystem because it contains several usable public and university mechanisms spanning the full Toledo path.

### P0–P2: low-friction front doors

Typical routes:

```text
Citizen + AI
Technology Clinic Network (ClinicTech)
nearby university academic service
agricultural extension / mobile agricultural clinic where relevant
DIPROM or depa for defined enterprise/digital cases
```

Do not send an unresolved everyday problem directly into startup funding simply because an innovation agency exists.

### P3: expert / lab / technical escalation

Typical routes:

```text
regional science parks
universities
NSTDA / ITAP
TISTR
specialized public laboratories
```

### P4–P5: research / innovation / prototype / POC

Typical routes:

```text
university research groups
regional science parks
NSTDA / Thailand Science Park
NIA Groom / Grant where eligible
TED Fund / TED Fellows
depa for digital innovation
PMUC for deep-tech / research commercialization
TISTR
```

### P6–P7: knowledge asset / IP / utilization

Typical routes:

```text
DIP
university TTO
IP specialists
DIP IP Mart
science parks
industry matching
```

Important distinction:

```text
License != IP Market
```

A license is a utilization/transaction form. IP Mart is matching infrastructure.

### P8–P9: Business-0 / first cycle

Typical routes:

```text
DBD Biz Regist
OSMEP / SME One ID
DIPROM
university incubators / science parks
NIA Groom / Grant / Growth where eligible
TED Fund
depa
corporate matching
```

Company registration is only one legal operation. It is not Business-0 by itself.

### P10: growth

Typical routes:

```text
NIA Growth
OSMEP
DIPROM
NSTDA / TSP
PMUC accelerator / IDE mechanisms
depa
TISTR
sector standards / regulators
finance institutions
```

### P11: global / cross-border

Typical routes:

```text
NIA Global
DITP
EXIM Thailand
Thailand Science Park global mechanisms
DIP for international IP strategy
sector regulators
```

Destination-specific regulation and economics must be recomputed before international entry.

## System-level bodies

Some institutions are best modeled as system architects rather than citizen counters.

### NXPO / สอวช.

Useful as a policy/orchestration source for:

- University Holding Company architecture;
- innovation-driven-enterprise policy;
- commercialization mechanisms;
- reverse-innovation / demand-driven matching;
- ecosystem bottleneck analysis.

### MHESI / อว.

Useful as an umbrella/orchestrator whose citizen-facing capabilities are delivered through:

- Technology Clinics;
- regional science parks;
- universities;
- TED Fund;
- NSTDA;
- TISTR;
- other ministry mechanisms.

## Cross-actor rule

Routing is not complete until the case has a valid handoff.

The platform must distinguish:

```text
AcademicFit
from
UniversityExecutability
```

and must carry a Case Passport across the handoff.

## Registry freshness

Institutional programs change frequently.

Every country adapter must treat:

```text
eligibility
budget
application window
service availability
contact route
price/co-funding
turnaround
```

as time-sensitive fields.

A stale record must not be silently treated as currently available.
