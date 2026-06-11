# Stream 3 — Legal (analytical working note)

> Working note, not canonical wiki. Date: 2026-06-10. Deep-research verified
> (107 agents; primary legal sources — DOJ, Competition Bureau, law reviews,
> Ada Lovelace). Grounded via filter-correct + re-ingest. US + Canada primary.

## Antitrust / competition law (the load-bearing constraint)

**US — the 2023 regime change.** On **Feb 3 2023 the DOJ withdrew** the
1993/1996/2011 healthcare policy statements that had supplied the
**information-exchange "safety zones"** competitor data pools relied on
(independent third-party administration, 3+ month-old data, sufficient
aggregation). FTC followed **Jul 14 2023**. DOJ now does **case-by-case**
review and explicitly warns that **AI/algorithms can re-disaggregate
"aggregated" data** and that third-party intermediaries can be
circumvention / hub-and-spoke vehicles (PDAAG Mekki). →
`[[sources/web-2023-02-14-d0c]]` (Arnold & Porter). *DOJ primary release
JS-gated; cite by reference: justice.gov 2023-02-03.*

**Implication:** there is **no US bright-line safe design left** — only
rule-of-reason litigation-risk management. This is a material legal risk for
any US-side pool and a reason the **Canada-first** sequencing has a genuine
legal-certainty advantage, not just a market one.

**Canada — clearer, two-track, but mid-transition.** Criminal **s.45** (per se
for naked restraints) vs civil **s.90.1** (only on substantial-lessening-of-
competition effects test, with published market-share safe harbours). The
Competition Bureau still endorses **aggregation, independent third-party
administration, historical-only data** as concern-reducing. BUT: Dec 2024
amendments expanded s.90.1; an **Oct 31 2025 draft** would replace the
safe-harbour approach with a principles-based one (consultation to Jan 29 2026).
→ `[[sources/web-2024-06-27-57a]]` (Competitor Collaboration Guidelines),
`[[sources/web-2022-01-19-c5a]]` (draft). Antitrust-safe design mechanics also
in `[[sources/web-2021-03-07-5c3]]` (blockchain/permissioned access).

## Data ownership & trade secret

- **No general property right in data** (US/EU deliberately). Trade secrecy +
  contract are the principal IP-like protections — **fragile**: lost on
  disclosure, no remedy against reverse engineering / independent invention. →
  `[[sources/web-2019-01-23-bbd]]` (Hastings LJ). Implication: a pool's value
  rights must be **contractually constructed**, not assumed from ownership.

## Privacy law (constrains, does not enable)

- Canada **PIPEDA** (in force); **Bill C-27/CPPA is dead** (did not pass) — so
  current de-identification/sharing rules are PIPEDA-as-enacted, not the
  proposed CPPA standard. **Québec Law 25** + US **CCPA/CPRA** add
  consent/de-identification constraints; cross-border pools face the strictest
  applicable standard. → `[[sources/web-2023-09-25-318]]` (Aird Berlis,
  PIPEDA vs C-27 de-identification). Privacy law gates pooling of *personal*
  data via consent/de-id; it is a constraint, not an enabler.

## Legal entity options

- Realistic forms: **contractual data-sharing agreement**, **corporate / JV
  entity**, or **fiduciary data trust**. The data trust is increasingly
  theorized (Ada Lovelace 2021; Houser & Bagby 2023) as a **"bundle of
  contracts" pooling statutory data rights**, NOT a classical common-law trust
  over data-as-property (since there's no property in data). →
  `[[sources/web-2021-03-04-e0f]]` (Ada Lovelace, legal mechanisms for data
  stewardship) → `[[entities/data-trusts-initiative]]`, enriched
  `[[concepts/data-trust]]`. *Vanderbilt JETLaw (Houser & Bagby) 403; cite by
  reference.*

## Adversarial caveats / open questions

1. Post-2023 US: is there ANY defensible safe design under case-by-case
   rule-of-reason, given the explicit AI-disaggregation + hub-and-spoke
   warnings — or only risk management? (load-bearing for US entry)
2. Final form of Canada's ACCA guidelines after the Jan 29 2026 consultation —
   do the 35%/65%/10% s.90.1 safe-harbour thresholds survive the principles-based shift? (→ Stream 4 regulatory)
3. Liability allocation for **downstream model harms** from pooled data +
   standard indemnification structures — entity findings cover structural
   liability only. (→ Stage 2 design)
4. Cross-border (US+Canada) de-identification standard for a single pool — which
   regime binds. (→ Stage 2)

## Source → status

| Topic | Source ID | Status |
|---|---|---|
| US DOJ safety-zone withdrawal | web-2023-02-14-d0c | grounded (Arnold&Porter; DOJ primary by ref) |
| Canada Competitor Collaboration Guidelines | web-2024-06-27-57a | grounded |
| Canada draft ACCA guidelines | web-2022-01-19-c5a | grounded |
| Privacy de-id PIPEDA vs C-27 | web-2023-09-25-318 | grounded |
| Property in data | web-2019-01-23-bbd | grounded |
| Entity forms / data trusts | web-2021-03-04-e0f | grounded |
| Antitrust via blockchain/permissioned | web-2021-03-07-5c3 | grounded (Stream 0) |
| DOJ primary release | — | JS-gated; by reference |
| Houser & Bagby data-trust (Vanderbilt) | — | 403; by reference |
