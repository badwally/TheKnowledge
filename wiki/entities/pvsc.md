---
schema_version: 1
type: entity
slug: pvsc
canonical_name: Property Valuation Services Corporation
entity_kind: organization
domains:
- condo-capital-infra
draft: true
draft_started_at: '2026-05-19T14:50:00Z'
draft_unresolved_claims: 0
created_at: '2026-05-19T15:13:35Z'
last_updated: '2026-05-19T15:13:35Z'
---
# Property Valuation Services Corporation

## Summary

Property Valuation Services Corporation (PVSC) is Nova Scotia's property-assessment agency, operating www.pvsc.ca and the datazONE open-data portal to provide public access to select property-related assessment information under the goals of increasing transparency and accountability, improving data quality, improving service to the public, and empowering citizens and supporting greater public engagement [[sources/web-2022-03-01-ef4]]. PVSC was incorporated in 2008, and its data-disclosure policy operates under the Nova Scotia Freedom of Information and Protection of Privacy Act (FOIPOP Act) as the governing legal framework [[sources/web-2022-03-01-ef4]]. Critically for any NS property-assessment-data covariate ingest, the PVSC Data Disclosure policy explicitly routes bulk sales data and historical assessment values requests to the Geographic Information Services (GIS) Division of the Office of Service Nova Scotia — NOT to PVSC directly — making the GIS Division the correct procurement contact for any bulk-data seed file rather than PVSC itself [[sources/web-2022-03-01-ef4]]. PVSC is the Nova Scotia provincial analog to British Columbia's BC Assessment in the Canadian provincial property-assessment-agency comparator set, with the parallel role of publishing per-property assessment information and operating a provincial open-data release channel (datazONE for NS, the BC Assessment Search Service for BC) [[sources/web-2022-03-01-ef4]].

## Key facts

### Corporate identity

- Nova Scotia property-assessment agency operating www.pvsc.ca; public inquiry line 1-800-380-7775; inquiry email inquiry@pvsc.ca [[sources/web-2022-03-01-ef4]].
- Incorporated in 2008 — PVSC's data record for property owners runs from the 2008 assessment year (the date of PVSC's incorporation) onwards [[sources/web-2022-03-01-ef4]].
- Operates under the Nova Scotia Freedom of Information and Protection of Privacy Act (FOIPOP Act) as the governing legal framework for data disclosure [[sources/web-2022-03-01-ef4]].

### Public data-release surfaces

- PVSC makes data available to the public on the PVSC website (www.pvsc.ca) and on the datazONE open-data portal [[sources/web-2022-03-01-ef4]].
- Data is released to the public surfaces only where PVSC determines that the data: (i) is of interest or useful to the public; (ii) is reviewed for privacy, security, copyright or other risks; (iii) meets the criteria and can be released under the FOIPOP Act; and (iv) is prepared and made available in accordance with PVSC procedures [[sources/web-2022-03-01-ef4]].

### Bulk-data access pathway (GIS Division of Service Nova Scotia)

- Requests for all other data, including bulk sales data and historical assessment values, must be directed to the Geographic Information Services (GIS) Division of the Office of Service Nova Scotia — explicitly NOT to PVSC directly [[sources/web-2022-03-01-ef4]].
- The GIS Division of Service Nova Scotia is therefore the correct procurement contact for any bulk NS property-assessment data seed file, including the bulk-data requirements of any NS covariate adapter built against the condo-capital-infra engine [[sources/web-2022-03-01-ef4]].
- This bulk-data routing surfaces a two-agency structure for NS property-assessment data: PVSC produces and curates the underlying assessment records and operates the public per-property and datazONE channels; the GIS Division of Service Nova Scotia controls bulk-data release [[sources/web-2022-03-01-ef4]].

### Property-owner direct-access channel

- PVSC makes data available to property owners for the purpose of helping them better understand their property assessment [[sources/web-2022-03-01-ef4]].
- Property-owner direct access is keyed to two identifiers printed on the current Property Assessment Notice: the unique Assessment Account Number (AAN) and the Personal Identification Number (PIN) [[sources/web-2022-03-01-ef4]].
- Upon request, PVSC may also provide owners with data related to their property from the 2008 assessment year (the date of PVSC's incorporation) onwards [[sources/web-2022-03-01-ef4]].

### FOIPOP Act exclusion categories

- The policy explicitly does not apply to data that is exempt under the FOIPOP Act, including but not limited to three named exclusion categories: (i) personal information or information that could lead to the identification of an individual; (ii) confidential information or information that may harm a third party's business interests; (iii) information that if disclosed to the public may threaten the safety or mental or physical health of a person or the safety of the public [[sources/web-2022-03-01-ef4]].
- The PVSC policy does not replace or limit an individual's right of access to information or PVSC's obligations under the FOIPOP Act [[sources/web-2022-03-01-ef4]].
- These three exclusion categories define the legal-defensibility perimeter any NS property-assessment-data ingest pipeline must operate within: personal-identification risk, third-party business-harm risk, and personal-or-public-safety risk [[sources/web-2022-03-01-ef4]].

### Cross-jurisdictional comparator framing

- PVSC is Nova Scotia's provincial property-assessment agency analog to British Columbia's BC Assessment (which operates the BC Assessment Search Service) — both are provincial-tier agencies producing per-property assessment records and operating public-facing data-access surfaces [[sources/web-2022-03-01-ef4]].
- Unlike BC Assessment's Search Service Terms of Use, which imposes a commercial-use prohibition restricting the service to private, personal, non-commercial use with commercial access requiring direct contact with BC Assessment, PVSC's policy frames its public data-release model around FOIPOP Act risk-categories rather than a commercial-use prohibition — making the operative legal-pathway question for an NS commercial-use adapter "does the requested record satisfy FOIPOP Act criteria?" rather than "does the use fall within a private-personal-non-commercial license?" [[sources/web-2022-03-01-ef4]].
- The two-agency NS structure (PVSC for curation + per-property/datazONE release; GIS Division of Service Nova Scotia for bulk release) is structurally distinct from BC's single-agency BC Assessment model, where both per-property and bulk commercial access flow through BC Assessment directly [[sources/web-2022-03-01-ef4]].

### Implication for condo-capital-infra GTM

- For any can-pilot NS covariate adapter built against the condo-capital-infra engine's Halifax wave under ADR-0004, the bulk-data procurement workflow must route through the GIS Division of the Office of Service Nova Scotia — not through PVSC directly, despite PVSC being the underlying data producer [[sources/web-2022-03-01-ef4]].
- The FOIPOP Act exclusion categories (personal-identification, third-party business-harm, safety) define the legal-defensibility framework any structured-data extraction or downstream analytics product built on NS property-assessment data must respect — particularly relevant for any owner-level disclosure layer or third-party valuation comparative product [[sources/web-2022-03-01-ef4]].
- The datazONE open-data portal is the public-facing release channel for PVSC-curated assessment data deemed of public interest and FOIPOP-compliant — establishing the open-data surface separate from the bulk-data GIS Division pathway for non-public records [[sources/web-2022-03-01-ef4]].
- The 2008 incorporation date is the data-history floor — owner-level retrospective data is available from 2008 forward, defining the minimum-feasible-history boundary for any longitudinal NS property-assessment analysis [[sources/web-2022-03-01-ef4]].

## Sources

- [[sources/web-2022-03-01-ef4]]

## Related

- [[entities/bc-assessment-search-service]]
- [[entities/ns-registrar-condominiums]]
- [[entities/ns-active-condo-corporations-dataset]]
- [[entities/halifax-regional-municipality]]
- [[entities/hrm-pplc-building-permits-dataset]]
