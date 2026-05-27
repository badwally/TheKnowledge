---
schema_version: 1
type: entity
slug: toronto-apartment-building-registration
canonical_name: City of Toronto Apartment Building Registration Dataset
entity_kind: dataset
domains:
- condo-capital-infra
draft: true
draft_started_at: '2026-05-19T14:56:53Z'
draft_unresolved_claims: 0
created_at: '2026-05-19T14:58:08Z'
last_updated: '2026-05-19T14:58:08Z'
---
# City of Toronto Apartment Building Registration Dataset

## Summary

The City of Toronto Apartment Building Registration Dataset is an Ontario municipal open-data dataset published on the City of Toronto Open Data Portal (`open.toronto.ca`) by the City's Municipal Licensing & Standards division under the RentSafeTO apartment-building-standards program, and made available for download as a 1.6 MB CSV under the Open Government Licence — Toronto [[sources/web-2025-10-21-a7b]]. The dataset is the canonical free covariate anchor for the can-pilot Ontario wave (Brief-0011 Wave C1/C2): its per-building fields — including `year_built`, `no_of_storeys`, `no_of_units`, `site_address`, and `property_type` — feed the Ontario covariate schema directly and define the building-stock characterization layer available without commercial-license negotiation for the Year-2 ON expansion arm of the condo-capital-infra Canada-first GTM under ADR-0004 [[sources/web-2025-10-21-a7b]]. Coverage scope is bounded by RentSafeTO's statutory perimeter: all rental apartment buildings in the City of Toronto with three or more storeys and ten or more units [[sources/web-2025-10-21-a7b]]. As of the May 19, 2026 scrape, the dataset is marked **Retired** on the portal landing page (rows last refreshed 2026-05-05; refreshed monthly) — a material finding that affects can-pilot Wave C reliability and requires a successor-dataset search before the ON adapter builds against these fields [[sources/web-2025-10-21-a7b]].

## Key facts

### Publication and provenance

- Hosted on the City of Toronto Open Data Portal at `open.toronto.ca/dataset/apartment-building-registration/` [[sources/web-2025-10-21-a7b]].
- Published by the City of Toronto's Municipal Licensing & Standards division through the RentSafeTO apartment-building-standards program [[sources/web-2025-10-21-a7b]].
- License: Open Government Licence — Toronto, permitting use, modification, and redistribution under attribution to the City of Toronto [[sources/web-2025-10-21-a7b]].
- Download format: CSV, ~1.6 MB file size [[sources/web-2025-10-21-a7b]].
- Refresh cadence: monthly; rows last refreshed 2026-05-05 as of the May 19, 2026 scrape [[sources/web-2025-10-21-a7b]].

### Retirement status (load-bearing finding)

- As of the May 19, 2026 scrape, the dataset is marked **Retired** on the portal landing page — the operative status flag that downstream consumers of the dataset must encode in any can-pilot adapter built against these fields [[sources/web-2025-10-21-a7b]].
- The retirement status is material to the can-pilot Ontario Wave C1/C2 reliability framing: a successor dataset (or alternative covariate source) must be identified before the ON adapter is operationalized against these fields, since the monthly-refresh data feed will not continue indefinitely under the Retired status [[sources/web-2025-10-21-a7b]].
- The retirement status is the structural reason the source's filter score moved from 0.5 (review) to 1.0 (include) at the curation step — the retired-status finding is load-bearing for the can-pilot pipeline and warrants recording in the wiki source even though the substantive dataset contents are not directly visible in the trafilatura-extracted page body [[sources/web-2025-10-21-a7b]].

### Coverage scope (RentSafeTO statutory perimeter)

- Covers all rental apartment buildings in the City of Toronto with three or more storeys and ten or more units, consistent with the RentSafeTO program's statutory perimeter for apartment-building-standards enforcement [[sources/web-2025-10-21-a7b]].
- The 3-storey-plus / 10-unit-plus threshold excludes small rental properties (duplexes, triplexes, walk-up four-plexes below the threshold) and owner-occupied condominium and freehold stock — limiting the dataset's coverage to the rental-apartment-tower segment of Toronto's residential building stock [[sources/web-2025-10-21-a7b]].
- The dataset's rental-apartment scope is structurally distinct from the Ontario condominium-corporation universe surveyed by the Condominium Authority of Ontario; rental-apartment registrations do not directly populate the ON condo-corporation register and serve as a building-stock-characterization covariate source rather than as a condominium-corporation-identification source for the can-pilot pipeline [[sources/web-2025-10-21-a7b]].

### Per-building covariate schema

- Building-stock characterization fields named in the curatorial scrape annotation: `year_built` (year of construction); `no_of_storeys` (count of storeys); `no_of_units` (total rental units in the building); `site_address` (civic address); `property_type` (rental-apartment classification) [[sources/web-2025-10-21-a7b]].
- The five fields together define the load-bearing covariate set the dataset contributes to the Ontario covariate schema: building age (via `year_built`), building height (via `no_of_storeys`), building size (via `no_of_units`), spatial location (via `site_address`), and property classification (via `property_type`) [[sources/web-2025-10-21-a7b]].
- The page body fetched by trafilatura contains only the metadata field labels (`First published`, `Data last refreshed`, `Refreshed`, `Data type`, `Civic issues`, `Topics`, `More information`, `Licence`, `Published by`, `Contact`) with empty values, reflecting JavaScript-rendered population of the actual values on the live portal page — the curatorial scrape annotation supplies the substantive metadata that the trafilatura extraction could not retrieve from the JS-rendered landing surface [[sources/web-2025-10-21-a7b]].

### Implication for can-pilot Ontario wave (Brief-0011 Wave C1/C2)

- The dataset is the canonical free covariate anchor for the can-pilot Ontario wave under Brief-0011 Wave C1/C2: it provides `year_built`, `no_of_storeys`, `no_of_units`, `site_address`, and `property_type` directly without commercial-license negotiation, populating the ON covariate schema's building-stock-characterization layer at zero data-acquisition cost under the Open Government Licence — Toronto [[sources/web-2025-10-21-a7b]].
- The dataset's `site_address` field provides the spatial join key into the City of Toronto's other open datasets and into Statistics Canada census geographies, making it the entry point for cross-validating Toronto rental-apartment building-stock against other municipal-tier and federal-tier covariate sources for the Year-2 ON expansion arm [[sources/web-2025-10-21-a7b]].
- The Retired status is the operative constraint on can-pilot Wave C reliability: any adapter that builds against the dataset's monthly-refresh feed must encode the retirement state and trigger a successor-dataset search, since the data feed's continuation cannot be assumed under the Retired flag [[sources/web-2025-10-21-a7b]].
- The rental-apartment scope of the dataset (3+ storeys, 10+ units, rental tenure) is structurally narrower than the condo-corporation scope of the Ontario Condominium Act 1998 regulatory perimeter — the dataset complements rather than substitutes for any ON condo-corporation register that the can-pilot Ontario wave will ultimately need for the condominium-corporation-identification layer [[sources/web-2025-10-21-a7b]].

## Sources

- [[sources/web-2025-10-21-a7b]]

## Related

- [[entities/ontario-condominium-act-1998]]
- [[entities/condominium-authority-ontario]]
- [[entities/cao-2024-reserve-fund-survey]]
- [[entities/bc-assessment-search-service]]
- [[entities/ns-active-condo-corporations-dataset]]
- [[entities/hrm-pplc-building-permits-dataset]]
