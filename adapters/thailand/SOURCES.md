# Thailand Adapter — Evidence and Source Index

**Snapshot reviewed:** 2026-09-11

This file indexes evidence used to build and interpret the Thailand adapter. It is not itself proof that every program is currently open. Operational routing must still verify volatile fields at the time of use.

Source classes follow [`../../docs/DATA_GOVERNANCE.md`](../../docs/DATA_GOVERNANCE.md):

```text
S0 law / regulator / standards authority
S1 official institution / program / service source
S2 official government report / open data / press release
S3 peer-reviewed academic research
S4 reputable independent secondary source
S5 community / anecdotal discovery signal
```

## Official service and institutional sources

| Mechanism / topic | Class | Source |
|---|---:|---|
| MHESI Technology Clinic / ClinicTech | S1 | https://clinictech.ops.go.th/online/cmo/site.asp |
| Regional Science Parks | S1 | https://rsp.mhesi.go.th/about/ |
| NSTDA / ITAP | S1 | https://itap.nstda.or.th/ |
| NSTDA services | S1 | https://www.nstda.or.th/home/service/overview-service/ |
| Thailand Science Park / TED route | S1 | https://www.sciencepark.or.th/th/ted-fund/service |
| TISTR services | S1 | https://www.tistr.or.th/page_services.php |
| TISTR service portal | S1 | https://tistrservices.tistr.or.th/ |
| NIA 4G | S1 | https://www.nia.or.th/4G-for-business-innovation |
| NIA 4G strategy | S1 | https://www.nia.or.th/index.php/4GStrategyInnovationNation |
| NIA trends / program context | S1 | https://www.nia.or.th/NIA-Trend-2026 |
| DIP / patent information | S1/S0 depending claim | https://www.ipthailand.go.th/th/patent.html |
| DIP IP Mart | S1 | https://ipmart.ipthailand.go.th/web-content/about-us |
| TED Fund youth/startup program | S1 | https://www.tedfund.mhesi.go.th/index.php/join-proj/ted-fund-youth-startup |
| depa funds | S1 | https://depa.or.th/th/funds |
| depa startup | S1 | https://www.depa.or.th/th/startup |
| PMUC proposal guide | S1 | https://pmuc.or.th/proposal-guide-book/ |
| PMUC Connect | S1 | https://pmuc.or.th/pmuc-connect/ |
| DIPROM | S1 | https://diprom.go.th/ |
| OSMEP SME One ID | S1 | https://oneid.sme.go.th/ |
| OSMEP SME Navi | S1 | https://smenavi.sme.go.th/home/ |
| DBD business registration | S1/S0 depending claim | https://edbruat.dbd.go.th/loginjuristicpage |
| TISI services | S1/S0 depending claim | https://www2.tisi.go.th/website/service |
| Mobile Agricultural Clinic | S1 | https://clinickaset.doae.go.th/site/about |
| EXIM Thailand policy/target programs | S1 | https://www.exim.go.th/TH/policyTarget.aspx |
| NXPO Reverse Innovation Journey | S2/S1 | https://www.nxpo.or.th/th/en/48855/ |
| NXPO UHC / ecosystem reporting | S2/S1 | https://www.nxpo.or.th/th/report/44835/ |

### Source-use caution

A single official webpage may support only some fields. For example:

```text
program existence
    does not automatically support
current application window

institution mandate
    does not automatically support
local operational capacity

service page
    does not automatically prove
legal authority or accreditation
```

Use the strongest source for each consequential claim.

## Academic/system evidence

These sources help interpret Thailand's innovation/intermediary system. They do not replace current official service eligibility or legal sources.

| Topic | Class | Source |
|---|---:|---|
| Regional factors and science park performance in Thailand | S3 | https://doi.org/10.1080/19761597.2020.1858718 |
| Thailand innovation-driven enterprise ecosystem | S3 | https://link.springer.com/article/10.1186/s13731-024-00371-x |
| Firm engagement with universities in Thailand | S3 | https://www.sciencedirect.com/science/article/pii/S2199853124000428 |
| Innovation intermediaries in Thai science parks | S3 | https://research.manchester.ac.uk/en/publications/innovation-intermediaries-for-universityindustry-rampd-collaborat/ |
| Intermediary role portfolios in science parks | S3 | https://www.tandfonline.com/doi/abs/10.1080/19761597.2026.2618708 |
| Regional innovation systems / university responses in Thailand | S3 | https://www.tandfonline.com/doi/abs/10.1080/13662710601032903 |

## Claims requiring live verification

The following should not be treated as durable facts from this source index alone:

```text
program open/closed status
current grant amount
current co-funding ratio
current eligibility rules
current queue/turnaround
specific local expert availability
lab sample acceptance
current accreditation scope
current regulator forms/fees
application deadline
current phone/email contact
```

Verify these at routing time or mark them unknown.

## Future evidence structure

A production adapter should move toward claim-level records such as:

```json
{
  "claim_id": "TH-NIA-4G:application-window",
  "record_id": "TH-NIA-4G",
  "field": "application_window_if_any",
  "value": "...",
  "source_class": "S1",
  "source_url": "...",
  "verified_at": "...",
  "valid_from": "...",
  "valid_until": null,
  "notes": "..."
}
```

This separates evidence for volatile fields from stable institution identity.
