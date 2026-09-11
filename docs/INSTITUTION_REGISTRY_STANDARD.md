# Institution Capability Registry Standard

This standard defines how Toledo describes institutions and public-service mechanisms for routing. The unit of routing is a **capability-bearing mechanism**, not institutional prestige or brand.

## 1. Design objective

Translate:

```text
case state
→ required capability
→ currently executable mechanism
```

The registry must help answer:

- Can this mechanism provide the needed capability?
- Is the citizen/case eligible?
- Can the service be accessed now and in time?
- Is there a cost, co-funding, location, or documentation barrier?
- Does it have legal or accredited authority when that matters?
- What source supports these claims?
- What is the fallback if the mechanism is unavailable?

## 2. Record granularity

Prefer:

```text
NSTDA + ITAP
DIP + IP Mart
NIA + 4G mechanism
University X + specific laboratory/service
```

over:

```text
NSTDA
DIP
NIA
University X
```

One institution may therefore have many records.

## 3. Core identifiers

Required stable fields:

```text
institution_id
institution_name
mechanism_name
country
jurisdiction
```

`institution_id` SHOULD identify the mechanism record, not merely the parent organization.

## 4. Capability classes

Use these high-level institution classes:

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

Class is a routing aid, not a legal characterization.

## 5. Accessibility classes

```text
A0 system/policy body; not a normal citizen front door
A1 selective / call-based / high eligibility burden
A2 defined target group / organizational eligibility
A3 clear public service channel
A4 low-entry local / community / online front door
```

Accessibility is not quality, authority, or prestige.

## 6. Phase fit

`phase_fit` uses Toledo routing coordinates `P0`–`P11`.

A mechanism MAY fit several phases. Phase fit means the capability is plausibly useful there; it does not guarantee eligibility or current availability.

## 7. Capability vocabulary

Free-text capability labels are allowed during the specification phase, but country adapters SHOULD converge on a controlled capability vocabulary.

Recommended top-level capability codes:

```text
CONSULT_EXPERT
DIAGNOSE_FIELD
MEASURE_LAB
TEST_STANDARD
PROTOTYPE
PILOT_PLANT
RND_COLLAB
TECH_TRANSFER
IP_PROTECT
IP_MATCH
INCUBATE
FUND_GRANT
FUND_COFINANCE
ACCELERATE
MARKET_MATCH
REGISTER_BUSINESS
REGULATE_AUTHORIZE
STANDARD_CONFORMITY
PROCURE_BUY
EXPORT_SUPPORT
FINANCE_EXPORT
POLICY_ORCHESTRATE
TRAIN_CAPABILITY
COMMUNITY_VALIDATE
```

Adapters MAY add local subcodes, but SHOULD map them to a global top-level code.

## 8. Operational status

Recommended `record_status` values:

```text
active
unknown
inactive
superseded
archived
historical
```

Recommended availability states:

```text
open
closed
call-dependent
capacity-dependent
unknown
```

Never infer `open` from the existence of a website or old program page.

## 9. Provenance

At minimum every record MUST have:

```text
source_url
last_verified
```

Mature records SHOULD also include:

```text
source_urls[]
verification.level
verification.verified_at
verification.evidence_urls[]
verification.notes
```

See [`DATA_GOVERNANCE.md`](DATA_GOVERNANCE.md).

## 10. Freshness by claim

The following fields are time-sensitive and SHOULD be re-verified before live consequential routing when stale:

```text
eligibility
application window
price / co-funding
turnaround
availability
contact route
accreditation
legal authority
```

Stable identity fields generally change more slowly.

## 11. Authority and accreditation

Separate:

```text
provides technical advice
from
has accredited test capability
from
has legal authority
```

A public institution may provide useful technical services without being the regulator. A regulator may authorize without providing technical development support.

## 12. Geographic coverage

Record both declared coverage and practical access when possible.

Country-wide mandate does not imply equally accessible local capacity.

For distributed networks, the global record SHOULD be supplemented by specific node records when routing quality depends on local facilities, staff, language, or queues.

## 13. Entry channels

`entry_channel` should point to a real public entry path when possible:

```text
service page
application portal
contact form
phone/public office
local node directory
```

Generic homepages are acceptable only when no more specific route is available.

## 14. Target users and eligibility

Distinguish:

```text
target_user
eligibility
```

A mechanism may target SMEs but require additional criteria. Do not infer eligibility solely from target audience.

## 15. Fallback routes

Every important live mechanism SHOULD identify fallback route types or alternative mechanisms where practical.

Fallback is particularly important for:

- deadline-sensitive cases;
- regional capacity differences;
- call-based funding;
- accreditation-dependent testing;
- high-volatility public programs.

## 16. Institution utility

Routing implementations may consume upstream Toledo equations/heuristics for institution utility. This repository MUST bind to the upstream registry rather than silently redefining those equations.

Implementation comparison SHOULD treat separately:

```text
CapabilityFit
Accessibility
Eligibility
ExpectedDecisionGain
ResponseTimeFit
MoneyCost
AccessBurden
CoordinationCost
RightsRisk
```

A hard eligibility, legal, or safety failure cannot be averaged away by a high soft score.

## 17. Minimum record example

```json
{
  "institution_id": "TH-NSTDA-ITAP",
  "institution_name": "NSTDA",
  "mechanism_name": "Industrial Technology Assistance Program (ITAP)",
  "country": "TH",
  "jurisdiction": "Thailand",
  "institution_class": "I2",
  "phase_fit": ["P1", "P2", "P3", "P4", "P5"],
  "target_user": ["SME", "private enterprise"],
  "citizen_accessibility": "A2",
  "eligibility": ["program criteria apply"],
  "entry_channel": ["https://itap.nstda.or.th/"],
  "capability": ["technical diagnosis", "expert matching"],
  "source_url": "https://itap.nstda.or.th/",
  "last_verified": "2026-09-11"
}
```

## 18. Record acceptance checklist

Before merging a new or changed institution record:

- [ ] mechanism is specific enough to route;
- [ ] identifier is stable and unique;
- [ ] institution class is plausible;
- [ ] phase fit is justified;
- [ ] eligibility is not guessed;
- [ ] entry channel is public and usable;
- [ ] capability wording is evidence-backed;
- [ ] authority/accreditation is not overstated;
- [ ] source is public and appropriate;
- [ ] verification date is present;
- [ ] volatile fields are marked unknown when not confirmed;
- [ ] fallback exists where routing failure would matter;
- [ ] no citizen-sensitive data is included.

## 19. Production rule

A registry record is discovery/routing evidence, not a guarantee that a service will accept a case. Production systems SHOULD verify high-volatility fields at routing time and preserve the returned operational result in the case audit trail.
