---
schema_version: 1
type: entity
slug: ns-registrar-condominiums
canonical_name: Service Nova Scotia Registrar of Condominiums
entity_kind: organization
domains:
- condo-capital-infra
created_at: '2026-05-11T21:23:42Z'
last_updated: '2026-05-27T19:12:45Z'
finalized_at: '2026-05-27T19:12:45Z'
---
# Service Nova Scotia Registrar of Condominiums

## Summary

The Registrar of Condominiums is the Service Nova Scotia office that maintains the provincial register of active condominium corporations under Nova Scotia's condominium statutory regime, and publishes the Active Condominium Corporations open dataset to `data.novascotia.ca` under the Open Government Licence - Nova Scotia [[sources/web-2026-05-10-nsa]]. The office sits within Service Nova Scotia, the provincial department whose minister at the May 23, 2023 proclamation of the Nova Scotia Condominium Act amendments was Colton LeBlanc, Minister of Service Nova Scotia and Internal Services [[sources/web-2026-01-01-577]]. It is the authoritative provincial source for the NS market-frame data bounding the Year-1 acquisition universe in the condo-capital-infra Canada-first GTM [[sources/web-2026-05-10-nsa]].

## Key facts

- Office within Service Nova Scotia (the provincial service-delivery department of the Government of Nova Scotia) responsible for the register of condominium corporations [[sources/web-2026-05-10-nsa]].
- At the May 23, 2023 proclamation of Nova Scotia Condominium Act amendments — which introduced more frequent reserve-fund studies, governance changes around developer-to-elected-board transition, modernized voting methods (including email balloting), and consumer-protection enhancements (rental-agreement disclosure to the board and clear bare-land-condominium advertising) — the responsible minister was Colton LeBlanc, Minister of Service Nova Scotia and Internal Services [[sources/web-2026-01-01-577]].
- Assigns each Condominium Corporation a registration number on first registration; phased developments register each phase separately under one corporation number [[sources/web-2026-05-10-nsa]].
- Maintains per-corporation records of declarant, phase, community, unit-mix decomposition (residential, commercial, recreational, parking, storage, bare-land residential, bare-land commercial), NS Property Identifier (PID) and NS Property Records Database identifiers, and the registered MultiPolygon footprint of the corporation [[sources/web-2026-05-10-nsa]].
- Publishes the Active Condominium Corporations dataset on `data.novascotia.ca` under the Open Government Licence - Nova Scotia (`OGL_NOVA_SCOTIA`), making the register freely usable, modifiable, and redistributable under attribution to the Province of Nova Scotia / Service Nova Scotia [[sources/web-2026-05-10-nsa]].
- The Registrar publishes the dataset under two related assets: an underlying tabular poly layer (`eq9a-ayyh`, created 2015-12-11) and a derived visualization chart "Active Condominium Corporations - Total Number of Units by County" (`9w9g-2c83`, published 2023-07-26); the poly layer is the source of truth for the tabular data, with `9w9g-2c83` declared as its `modifyingViewUid` [[sources/web-2026-05-10-nsa]].
- Dataset rows were last refreshed 2026-05-05; access is via the Socrata REST API at `GET https://data.novascotia.ca/resource/eq9a-ayyh.csv` (data) and `GET https://data.novascotia.ca/api/views/eq9a-ayyh.json` (metadata) [[sources/web-2026-05-10-nsa]].
- The Registrar's public dataset surfaces register metadata only — completed 5-year reserve-fund studies are corporation records, not Registrar filings, and are therefore not visible through the open-data portal [[sources/web-2026-05-10-nsa]].
- The cadence of reserve-fund studies under the Nova Scotia Condominium Act was tightened by the May 23, 2023 proclamation of Act amendments, which require condominium corporations to undertake more frequent reserve-fund studies to help them plan for future capital repairs; the revised cadence is set in the subordinate Regulations (https://novascotia.ca/just/regulations/regs/conregs.htm) rather than in the proclamation announcement [[sources/web-2026-01-01-577]].
- As of the 2026-05-10 snapshot, the Registrar's active register contains 526 corporation phases across 13 NS counties, with 16,949 residential units and 20,572 total units; Halifax County alone accounts for 425 phases (80.8%) and 18,263 total units (88.8%) of the registered footprint [[sources/web-2026-05-10-nsa]].

## Sources

- [[sources/web-2026-05-10-nsa]]
- [[sources/web-2026-01-01-577]]

## Related

- [[entities/ns-active-condo-corporations-dataset]]
- [[entities/ns-condominium-act]]
- [[entities/cci-nova-scotia]]
- [[entities/bc-strata-property-act]]
- [[entities/dbpr-condominiums-division]]
