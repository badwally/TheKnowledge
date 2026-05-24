---
type: entity
slug: bc-assessment
canonical_name: BC Assessment
entity_kind: organization
domains:
- condo-capital-infra
draft: true
draft_started_at: '2026-05-19T14:49:03Z'
draft_unresolved_claims: 0
---
# BC Assessment

## Summary

BC Assessment is the British Columbia provincial assessment authority that provides local governments and other taxing authorities with accurate and independent property assessment information used to determine how property taxes are distributed across taxing authorities and funding for community services [[sources/web-2026-01-02-6fe]]. BC Assessment announces property assessment information on an annual basis, with the 2026 roll released January 2, 2026 reflecting market values as of July 1, 2025 [[sources/web-2026-01-02-6fe]]. The organization operates both the BC Assessment Search Service (the per-property online lookup tool governed by a private-personal-non-commercial-use Terms of Use; see `[[entities/bc-assessment-search-service]]`) and a broader data-product portfolio that includes the 2026 BC Assessment News Releases, regional highlight breakdowns (Lower Mainland, Vancouver Island, Southern Interior, North Central), and a province-wide property statistics page that exposes the data-product inventory (Top 500 Highest Residential Properties, Assessment Roll Total Value, Assessment Roll Total Value by Property Class, Assessment Roll Total Value by Area and Property Class, BC Property Count, Property Count by Subclass, New Construction) [[sources/web-2026-01-02-6fe]]. The data-product inventory page carries a distinct commercial-use prohibition notice — separate from the parallel prohibition in the Search Service Terms of Use — that confirms bulk Data Advice commercial licensing as the only defensible route to province-wide BC strata covariates for the condo-capital-infra engine's BC wave under ADR-0004 [[sources/web-2026-01-02-6fe]].

## Key facts

### Organizational role

- BC Assessment provides local governments and other taxing authorities with accurate and independent assessment information [[sources/web-2026-01-02-6fe]].
- Local governments and other taxing authorities use that information to determine funding for important services used every day in communities across British Columbia [[sources/web-2026-01-02-6fe]].
- Property assessments are about determining how property taxes are distributed, not the absolute level of taxes collected [[sources/web-2026-01-02-6fe]].

### Annual roll publication cadence

- Property assessment information is announced on an annual basis [[sources/web-2026-01-02-6fe]].
- The 2026 roll was released on January 2, 2026 and is based on market values as of July 1, 2025 — establishing the ~6-month lag between the valuation date and the release date as the operative cadence [[sources/web-2026-01-02-6fe]].
- BC Assessment publishes annual News Releases announcing the roll, accompanied by regional breakdowns of highlights for Lower Mainland, Vancouver Island, Southern Interior, and North Central [[sources/web-2026-01-02-6fe]].
- The annual roll release is supported by a Media Backgrounder published for the relevant year (e.g., 2026 Assessment Roll Media Backgrounder) [[sources/web-2026-01-02-6fe]].

### 2026 BC Assessment Roll — province-wide highlights

- Number of properties assessed: 2,233,648 [[sources/web-2026-01-02-6fe]].
- Total value of real estate assessed: $2.75 trillion [[sources/web-2026-01-02-6fe]].
- Total value of new construction, subdivisions and rezoning: $34.7 billion [[sources/web-2026-01-02-6fe]].
- Percentage of accepted assessments (appeals not filed): 99% — establishing that fewer than 1% of BC assessments are challenged through the appeals process in any given roll year [[sources/web-2026-01-02-6fe]].

### Data-product inventory (per the property-information-trends page)

- The province-wide property-information-trends page exposes a data-product inventory with the following named data products: British Columbia's Top 500 Highest Residential Properties; Assessment Roll Total Value; Assessment Roll Total Value by Property Class; Assessment Roll Total Value by Area and Property Class; BC Property Count; Property Count by Subclass; New Construction [[sources/web-2026-01-02-6fe]].
- The page also publishes regional highlight breakdowns for Lower Mainland, Vancouver Island, Southern Interior, and North Central [[sources/web-2026-01-02-6fe]].
- The data-product inventory page is distinct from the BC Assessment Search Service's per-property online lookup tool (see `[[entities/bc-assessment-search-service]]`) — it surfaces aggregate, province-scoped statistics rather than per-property records [[sources/web-2026-01-02-6fe]].

### Commercial-use prohibition notice (data-product inventory page)

- The property-information-trends page carries an explicit Privacy Notification: "Any commercial use of this data in whole or in part, directly or indirectly, including the use of such data for business, residential address or telephone directory services or any solicitation service is specifically prohibited" [[sources/web-2026-01-02-6fe]].
- This commercial-use prohibition is distinct from the Terms of Use that governs the BC Assessment Search Service (the per-property online lookup tool) — making the data-product inventory page a second BC Assessment surface that codifies the commercial-use prohibition at the aggregate-statistics level, reinforcing that BC Assessment operates a multi-surface ToS posture across both per-property and province-aggregate data products [[sources/web-2026-01-02-6fe]].
- The two-surface commercial-use prohibition confirms that bulk Data Advice commercial licensing — negotiated directly with BC Assessment — is the only defensible route to province-wide BC strata covariates for any automated covariate-acquisition pipeline operating across the BC wave under ADR-0004's Canada-first sequence [[sources/web-2026-01-02-6fe]].

### Implication for condo-capital-infra GTM

- The 99% appeals-acceptance rate on the 2026 roll surfaces a structurally low-noise jurisdictional baseline for BC assessment-roll data — useful context for sizing the data-quality assumptions in any BC adapter that ingests assessed values or building-attribute fields downstream of the assessment roll [[sources/web-2026-01-02-6fe]].
- The $34.7B 2026 new construction / subdivisions / rezoning total establishes a province-wide construction-pipeline scale anchor for any BC-wave building-stock-growth model, with the released roll capturing valuation as of July 1 of the prior year [[sources/web-2026-01-02-6fe]].
- The data-product-inventory-page commercial-use prohibition codifies — at a second BC Assessment surface — the same legal constraint flagged by Finding-0017 §7B as load-bearing for the can-pilot Vancouver wave tos.py adapter: the adapter must encode both prohibition notices (Search Service ToS and data-product-inventory page Privacy Notification) and route any commercial covariate-acquisition pipeline through bulk Data Advice licensing rather than uncontracted scraping of either surface [[sources/web-2026-01-02-6fe]].

## Sources

- [[sources/web-2026-01-02-6fe]]

## Related

- [[entities/bc-assessment-search-service]]
- [[entities/bc-strata-property-act]]
- [[entities/bc-housing]]
- [[entities/bc-housing-maintenance-matters-series]]
