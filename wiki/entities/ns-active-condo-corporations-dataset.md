---
schema_version: 1
type: entity
slug: ns-active-condo-corporations-dataset
canonical_name: Nova Scotia Active Condominium Corporations Dataset
entity_kind: dataset
domains:
- condo-capital-infra
created_at: '2026-05-12T02:46:22Z'
last_updated: '2026-05-27T19:12:45Z'
finalized_at: '2026-05-27T19:12:45Z'
---
# Nova Scotia Active Condominium Corporations Dataset

## Summary

The Nova Scotia Active Condominium Corporations Dataset is the provincial open-data registry of every active condominium corporation phase in Nova Scotia, published by Service Nova Scotia (Registrar of Condominiums) on the `data.novascotia.ca` Socrata portal under the Open Government Licence - Nova Scotia [[sources/web-2026-05-10-nsa]]. It is the open-data surface of the Condominium Corporations Register maintained by the Registrar under Part II §9 of the Nova Scotia Condominium Act (R.S.N.S. 1989, c.85), with the Registrar's recordkeeping duties anchored at §10 [[sources/pdf-e3717ebcf2bc]]. It is the authoritative primary-source market-frame dataset bounding the Year-1 NS acquisition universe for the Canada-first GTM in the condo-capital-infra engagement, providing per-phase corporation number, declarant, unit-mix decomposition, and geospatial polygon for the registered footprint [[sources/web-2026-05-10-nsa]].

## Key facts

### Publication and provenance

- Publisher: Service Nova Scotia, Registrar of Condominiums [[sources/web-2026-05-10-nsa]].
- Statutory authority for the underlying register: Nova Scotia Condominium Act Part II §9 (Condominium Corporations Register) and §10 (Registrar to maintain records), with the office of "Registrar" defined at §3(1)(v) [[sources/pdf-e3717ebcf2bc]].
- Host portal: `data.novascotia.ca` (Socrata) [[sources/web-2026-05-10-nsa]].
- License: Open Government Licence - Nova Scotia (`OGL_NOVA_SCOTIA`) — freely usable, modifiable, and redistributable under attribution to the Province of Nova Scotia / Service Nova Scotia [[sources/web-2026-05-10-nsa]].
- Created 2015-12-11; published 2023-07-26; rows last updated 2026-05-05 [[sources/web-2026-05-10-nsa]].
- Two related assets: the underlying tabular poly layer (asset id `eq9a-ayyh`) and a derived visualization chart "Active Condominium Corporations - Total Number of Units by County" (asset id `9w9g-2c83`) built as a `modifyingViewUid` view on the poly layer [[sources/web-2026-05-10-nsa]].
- The poly layer is the only `data.novascotia.ca` resource that exposes the underlying tabular data; the visualization-chart asset returns navigation chrome only when fetched directly because rendering is JS-mediated [[sources/web-2026-05-10-nsa]].
- Programmatic access via Socrata REST API: metadata at `GET /api/views/eq9a-ayyh.json`, data at `GET /resource/eq9a-ayyh.csv` [[sources/web-2026-05-10-nsa]].

### Schema (19 columns)

- `county` — Nova Scotia county of registration [[sources/web-2026-05-10-nsa]].
- `number` — Condominium Corporation registration number assigned by the Registrar of Condominiums [[sources/web-2026-05-10-nsa]].
- `phase_if_applicable` — Phase number for phased developments, reflecting the Act's Part II §8 phased-development condominium framework [[sources/web-2026-05-10-nsa]] [[sources/pdf-e3717ebcf2bc]].
- `community` — Municipal community (sub-municipal locality) [[sources/web-2026-05-10-nsa]].
- `declarant` — Legal name of the corporation's declarant of record, mapping to the statutory definition of "declarant" at Condominium Act §3(1)(l) [[sources/web-2026-05-10-nsa]] [[sources/pdf-e3717ebcf2bc]].
- `residential_units`, `commercial_units`, `recreational_units`, `parking_units`, `storage` — Unit-count breakdown by unit type [[sources/web-2026-05-10-nsa]].
- `bare_land_residential`, `bare_land_commercial` — Bare-land condominium unit counts [[sources/web-2026-05-10-nsa]].
- `total_units` — Sum of unit counts for the phase [[sources/web-2026-05-10-nsa]].
- `pid`, `pid_corp`, `nsprd_s_id`, `nsprd_mu`, `nsprd_date` — NS Property Identifier and Property Records Database identifiers and polygon refresh date [[sources/web-2026-05-10-nsa]].
- `the_geom` — MultiPolygon WKT geometry in WGS84 of the registered footprint [[sources/web-2026-05-10-nsa]].

### Provincial totals (snapshot fetched 2026-05-10)

- 526 active corporation phases across 13 NS counties, accounting for 16,949 residential units and 20,572 total units across all unit types [[sources/web-2026-05-10-nsa]].
- Halifax County: 425 phases, 15,881 residential units, 18,263 total units — 80.8% of phases and 88.8% of total units in the province [[sources/web-2026-05-10-nsa]].
- Lunenburg County: 38 phases, 358 residential units, 637 total units [[sources/web-2026-05-10-nsa]].
- Halifax + Lunenburg combined account for 88.0% of phases and 91.9% of total units [[sources/web-2026-05-10-nsa]].
- Outside the HRM + South Shore corridor, no NS county exceeds 11 active corporation phases [[sources/web-2026-05-10-nsa]].
- Full county-level summary (phases / residential units / total units): Halifax 425 / 15,881 / 18,263; Lunenburg 38 / 358 / 637; Hants 11 / 13 / 717; Colchester 11 / 135 / 182; Kings 9 / 121 / 178; Pictou 9 / 167 / 204; Annapolis 5 / 111 / 121; Inverness 5 / 27 / 67; Cumberland 4 / 10 / 71; Antigonish 3 / 26 / 26; Victoria 2 / 37 / 37; Queens 2 / 16 / 16; Cape Breton 2 / 47 / 53 [[sources/web-2026-05-10-nsa]].
- 82.4% of all registered units are residential [[sources/web-2026-05-10-nsa]].

### Counting semantics

- One row equals one Condominium Corporation phase, not one unique corporation; phased developments register each phase separately under one Corporation number, consistent with Part II §8 of the Act [[sources/web-2026-05-10-nsa]] [[sources/pdf-e3717ebcf2bc]].
- The `(number, phase_if_applicable)` composite key uniquely identifies a registered phase; deduplicating to `number` gives the corporation count [[sources/web-2026-05-10-nsa]].
- The 526-phase total is consistent with a Cox & Palmer figure of "400+ NS corporations represented" assuming a phase-to-corporation ratio of roughly 1.1-1.3 [[sources/web-2026-05-10-nsa]].

### Documented Halifax County example: Halifax Condominium Corporation No. 130 (Summer Gardens)

- Halifax Condominium Corporation No. 130 — 1470 Summer Street, Halifax — is a documented primary-source example of a Halifax-County row in the Registrar dataset, with property attributes confirmed by the June 11, 2025 Sense Engineering Reserve Fund Study [[sources/pdf-3c6b4345c8c4]].
- Building attributes: 21 storeys, 118 residential suites, single-level underground parking garage, constructed 1987; common amenities include indoor pool and hot tub, fitness room, men's and women's saunas, men's and women's changerooms/washrooms, lobby lounge, and party room [[sources/pdf-3c6b4345c8c4]].
- Fiscal year end: June 30; for reserve-fund-contribution purposes the corporation calculates 123 equivalent suites (five suites with larger footprints contribute proportionally more than the base 118) [[sources/pdf-3c6b4345c8c4]].
- Property manager: Real Estate 360 (650-33 Alderney Drive, Dartmouth, NS B2Y 2N4), with Andrew Buchanan as the named board contact [[sources/pdf-3c6b4345c8c4]].
- The corporation has retained two distinct NS-area engineering firms for capital-renewal work: BRK Engineering Inc. (2021 Reserve Fund Study; 2024 annual roof anchor inspection) and Sense Engineering (Atlantic) Ltd. (2025 Reserve Fund Study) [[sources/pdf-3c6b4345c8c4]].
- The corporation's 2025 Reserve Fund Study documents elected funding plan: Immediately Adequately Funded, with first-year contribution rising from $320,000 (2025) to $578,619 (2026) — an 80.8% one-time increase — followed by 2.5% annual increases over 2027-2030 [[sources/pdf-3c6b4345c8c4]].

### Coverage and gaps

- The dataset contains no contingency-fund or reserve-fund-study data — completed corporation contingency-fund studies are corporation records anchored to the Condominium Act's contingency-fund definition at §3(1)(i) and financial provisions at §31, not Registrar filings; the Registrar's public dataset surfaces register metadata only [[sources/web-2026-05-10-nsa]] [[sources/pdf-e3717ebcf2bc]].
- No funding-adequacy fields: contingency-fund balance, contribution rate, and study cadence are not present in the dataset [[sources/web-2026-05-10-nsa]].
- The Halifax Condominium Corporation No. 130 example illustrates the funding-adequacy data gap concretely: the corporation's 2025 RFS-driven 80.8% contribution increase, 2024 site visit findings, and 2021 predecessor study are corporation-held records not visible through the Registrar's open-data surface [[sources/pdf-3c6b4345c8c4]] [[sources/web-2026-05-10-nsa]].
- The `declarant` column is the primary lever for understanding developer concentration — a small number of declarants repeat across many corporations, providing the structural basis for management-firm channel referral strategies [[sources/web-2026-05-10-nsa]].
- The `the_geom` MultiPolygon geometry enables direct cross-validation against HRM open-data building permits and Statistics Canada census condo-dwelling tables [[sources/web-2026-05-10-nsa]].

### Cross-reference to HRM permits

- The HRM PPLC Building Permits Dataset (csv-7e5affc7bb1b, 17,803 records spanning 2021-2026) is the now-ingested municipal-tier complement to this Registrar dataset, joinable on the `pid` / `pid_corp` columns to surface new-construction and renovation activity on registered corporation footprints — operationalizing the cross-validation loop the dataset's `the_geom` field anticipates [[sources/csv-7e5affc7bb1b]].
- The HRM permits dataset's `Type_of_Structure` = "Dwelling - Multiple Units" filter, combined with `Work_Type` = "New Building", surfaces the new-condominium-eligible construction pipeline that will become future entries in this Registrar dataset as those corporations register [[sources/csv-7e5affc7bb1b]].

## Sources

- [[sources/web-2026-05-10-nsa]]
- [[sources/pdf-e3717ebcf2bc]]
- [[sources/csv-7e5affc7bb1b]]
- [[sources/pdf-3c6b4345c8c4]]

## Related

- [[entities/ns-condominium-act]]
- [[entities/ns-registrar-condominiums]]
- [[entities/summer-gardens-condo]]
- [[entities/real-estate-360]]
- [[entities/sense-engineering-atlantic]]
- [[entities/brk-engineering]]
- [[entities/hrm-pplc-building-permits-dataset]]
- [[entities/halifax-regional-municipality]]
- [[entities/bc-strata-property-act]]
- [[entities/california-davis-stirling-5550]]
- [[entities/florida-sirs]]
