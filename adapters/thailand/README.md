# Thailand Adapter

Thailand is the first country adapter for Toledo Citizen Platform.

The adapter supplies local institutions, access channels, regulators, language, and phase-specific routing while keeping the core citizen protocol jurisdiction-neutral.

## Routing priorities

For an ordinary citizen, the default order is usually:

```text
1. Citizen + AI
2. Low-friction local intermediary
3. Specialist expert / lab / science park
4. Innovation / IP / venture mechanism
5. Growth / regulatory / global mechanism
```

A hard safety/legal gate may skip directly to the appropriate professional or regulator.

## Important distinctions

```text
DIP != DIPROM
DIP = Department of Intellectual Property
DIPROM = Department of Industrial Promotion

NIA support != regulatory authorization
IP Mart = matching channel, not commercialization vehicle
NXPO = system/policy architect, not normal citizen service counter
AcademicFit != UniversityExecutability
```

## Seed registry

`institutions.seed.json` is a starting registry, not a guarantee of current availability.

Before production routing, every record must be re-verified for:

- eligibility;
- current application window;
- current contact/entry channel;
- cost/co-funding;
- response time;
- geographic coverage;
- service availability.

## Phase map

The adapter follows the global P0–P11 phase model described in the root README and `docs/INSTITUTION_ROUTING.md`.

## Language

The production adapter should support Thai first and retain the citizen's original wording before generating an English or disciplinary translation.
