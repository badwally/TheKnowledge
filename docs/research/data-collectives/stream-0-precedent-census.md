# Stream 0 — Precedent census (analytical working note)

> Working note, not canonical wiki. The canonical grounded layer is the
> `data-collectives` concept/entity/source pages. This note preserves the
> adversarially-verified deep-research findings (3-vote verification, 24/25
> claims confirmed) that feed the Task-10 synthesis and the condo Stage-2 leg.
> Date: 2026-06-10.

## Taxonomy (four governance models)

| Model | Defining trait | Canonical precedent | Wiki concept |
|---|---|---|---|
| Data cooperative | Member-owned, democratic collective control | MIDATA (CH, 2015) | `[[concepts/data-cooperative]]` |
| Data commons | Governed shared resource, tiered access | NIH biomedical commons (GDC, All of Us, AnVIL…) | `[[concepts/biomedical-data-commons]]` |
| Data trust | Independent/fiduciary legal stewardship | ODI 2018 pilots | `[[concepts/data-trust]]` |
| Federated-learning consortium | Shared model, raw data stays in custody | MELLODDY (10 pharma) | `[[concepts/federated-data-cooperative]]` |

Source: Mendonca et al. four-model taxonomy (arXiv 2504.10058, 2025-04-14);
ODI; Internet Policy Review glossary `[[sources/web-2024-04-04-ad6]]`.

## The core finding — four incentive families solve "why give up my edge"

1. **Policy mandate** — the dilemma is removed, not solved. NIH has *required*
   submission of high-throughput genomic data to dbGaP-class repositories since
   2008. `[[sources/web-2023-04-12-931]]` (verified 2-1; primary/government).
2. **Civic / intrinsic non-financial** — MIDATA, explicitly modeled on blood
   donation; members receive no dividends, profits reinvested.
   `[[sources/web-2021-05-05-125]]` (3-0).
3. **Anti-lock-in bargaining power** — JoinData (NL ag): farmers pool to escape
   tech-vendor lock-in and negotiate terms. (arXiv 2504.10058; 3-0.)
4. **Asymmetric private value capture** — MELLODDY: ten competing pharma firms
   trained shared QSAR models over 2.6B+ confidential activity points / 21M+
   molecules. Two stacked design features: (a) federated — raw data and private
   model heads never leave owner custody; (b) the contributor of a task's data
   becomes *exclusive* owner of that task's model components, so contributing
   improves **your own** model more than rivals'. Outcome: typically ~4%
   classification gain, ~10% applicability-domain increase; all 10 benefited on
   classification. `[[sources/web-2025-08-18-fa4]]` (3-0).

**Why this matters for the condo leg (Stage 2):** mechanism 4 is the only one
that fits *competing* commercial firms without a mandate or pure altruism. It is
the load-bearing precedent for a reserve-study collective among engineering
firms. Stream 1 (economics) must pressure-test whether asymmetric value capture
survives when contributors are direct substitutes (pharma assays are largely
complementary; competing engineering firms in one metro may be substitutes).

## The failure case

**Sidewalk Labs Urban Data Trust (Toronto).** Structured as a non-profit with a
5-member board hiring a CDO to write a charter + Responsible Data Use guidelines;
any party using "urban data" needed Trust permission. Waterfront Toronto
questioned legality (Jun 2019); dropped Nov 2019 after Ontario IPC criticism;
whole project cancelled May 2020. **Cause (Austin & Lie):** incoherent fusion of
an *open-data* model (public-by-default) with a *stewardship* model — conflicting
accountability assumptions. `[[sources/web-2021-06-25-2aa]]` (3-0). This is the
strongest *North American* case and it is a failure — a sobering datapoint for
the "why Canada" spine.

## Antitrust mechanics (feeds Stream 3)

Harvard JOLT: competitor data-sharing via permissioned blockchain + smart
contracts can mitigate antitrust risk through controlled access and regulator
transparency; names MOBI, Toyota/MIT. US-law-only.
`[[sources/web-2021-03-07-5c3]]` → `[[concepts/antitrust-risks-data-sharing]]`.

## Contrast tier (NOT genuine pooling)

Data brokers exhibit "co-opetition" (FTC 2014: 7/9 brokers shared data) but this
is pure resale, the domain's explicit exclusion — kept only as contrast.

## Adversarial caveats (carry forward — do not let synthesis paper over)

- **Scope mismatch:** the two best *voluntary* coopetition cases (MELLODDY,
  MIDATA) are EU/Swiss reference-tier, not US/Canada-primary. The strongest NA
  case (Sidewalk) is a failure. The biggest US construct (NIH) works only by
  mandate. **There is no clean US/Canada voluntary-coopetition success on record.**
- **Recency gap (direct hit on the research question):** the requested
  2023–2026 *agentic / vertical-AI on pooled proprietary data* category produced
  **zero** surviving verified claims. Absence of evidence vs evidence of absence
  is itself the open question — the commercial pattern may not have materialized
  yet. This is the single most important thing for Stream 7 (industrial) and the
  Task-10 "why now" argument to resolve.
- **Terminology:** "pooled" is wrong for federated cases — raw data is never
  centralized; read "federated."

## Open questions (seed later streams)

1. Any verified 2023–2026 agentic/vertical-AI venture on pooled competitor data? (→ Stream 7)
2. Strongest *genuinely US/Canada-primary* voluntary-coopetition success? (→ Streams 5, 7)
3. Did MELLODDY produce a durable commercial successor post-funding (May 2022), or did the incentive collapse once subsidy ended? (→ Stream 1)
4. Uncovered named candidates that didn't survive verification: Driver's Seat, Salus Coop, Swash, Owkin standalone, NVIDIA FLARE deployments, MobilityData/GBFS, clean rooms. (→ revisit in relevant streams)

## Source → wiki mapping

| Case | Source ID | URL |
|---|---|---|
| Taxonomy paper | (arxiv-2504.10058, review-band) | arxiv.org/abs/2504.10058 |
| MIDATA | web-2021-05-05-125 | midata.coop |
| Data-coop glossary / OPAL | web-2024-04-04-ad6 | policyreview.info |
| ODI data trusts | web-2019-04-13-653 | theodi.org |
| NIH commons | web-2023-04-12-931 | ncbi PMC10173774 |
| MELLODDY | web-2025-08-18-fa4 | melloddy.eu |
| Sidewalk failure | web-2021-06-25-2aa | queensu ojs 14409 |
| Antitrust/blockchain | web-2021-03-07-5c3 | jolt.law.harvard.edu |
