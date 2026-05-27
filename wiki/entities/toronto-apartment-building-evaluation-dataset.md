---
schema_version: 1
type: entity
slug: toronto-apartment-building-evaluation-dataset
canonical_name: City of Toronto Apartment Building Evaluation Dataset
entity_kind: dataset
domains:
- condo-capital-infra
draft: true
draft_started_at: '2026-05-19T15:51:38Z'
draft_unresolved_claims: 0
created_at: '2026-05-19T15:52:41Z'
last_updated: '2026-05-19T15:52:41Z'
---
# City of Toronto Apartment Building Evaluation Dataset

## Summary

The City of Toronto Apartment Building Evaluation Dataset is a municipal open-data product published on the City of Toronto Open Data Portal (open.toronto.ca) at the canonical landing-page URL `https://open.toronto.ca/dataset/apartment-building-evaluation/` [[sources/web-2025-10-21-9f1]]. The dataset landing page is JS-rendered: a trafilatura extraction of the page returns only the dataset-card field-label scaffolding (First published, Data last refreshed, Refreshed, Data type, Civic issues, Topics, More information, Licence, Published by, Contact) without populated values, indicating that the dataset's title, refresh cadence, license, and publisher metadata are loaded dynamically rather than rendered server-side and are not accessible without either a JS-capable fetch path or a direct CKAN / Socrata API call against the underlying resource endpoint [[sources/web-2025-10-21-9f1]]. The dataset is the Toronto municipal-tier counterpart in role to the HRM PPLC Building Permits Dataset and the Nova Scotia Active Condominium Corporations Dataset, positioned as a candidate building-stock-quality covariate anchor for any Ontario-wave reserve-study engine adapter under ADR-0004's Year-2 Ontario expansion arm.

## Key facts

### Publication and access surface

- Published on the City of Toronto Open Data Portal at the host domain `open.toronto.ca`, with canonical landing-page URL `https://open.toronto.ca/dataset/apartment-building-evaluation/` [[sources/web-2025-10-21-9f1]].
- The landing page presents a dataset-card layout enumerating the metadata field labels: First published, Data last refreshed, Refreshed, Data type, Civic issues, Topics, More information, Licence, Published by, Contact [[sources/web-2025-10-21-9f1]].
- Field values on the landing page are JS-rendered; a server-side text extraction returns only the field labels with no populated values, consistent with the Socrata / CKAN JS-rendered open-data-portal pattern previously observed on `data.novascotia.ca` for the NS Active Condominium Corporations Dataset landing page [[sources/web-2025-10-21-9f1]].
- Slug evidence: the URL path component `apartment-building-evaluation` distinguishes this dataset from the City of Toronto's separate `apartment-building-registration` dataset published on the same portal, and the two slugs should not be conflated when constructing API or download paths against the underlying CKAN / Socrata resource [[sources/web-2025-10-21-9f1]].

### Implication for condo-capital-infra GTM

- The dataset sits inside the Ontario municipal-open-data perimeter that frames the Year-2 Ontario expansion arc under ADR-0004's Canada-first GTM sequence, occupying the structural role for Toronto that the HRM PPLC Building Permits Dataset occupies for Halifax — a municipal-tier building-stock data product joinable to the provincial regulatory regime (Ontario Condominium Act 1998 + O. Reg. 48/01) by parcel / address-level identifiers exposed in the CKAN / Socrata resource layer [[sources/web-2025-10-21-9f1]].
- The JS-rendered landing-page surface means provenance-defensible ingest must bypass the human-facing landing page and target the underlying CKAN / Socrata resource API endpoint; field-level schema, refresh cadence, license terms, and publisher contact details are not present in the trafilatura extraction of the landing page and must be discovered through a separate API fetch before this dataset can be treated as a covariate-ingest target for an Ontario-wave engine adapter [[sources/web-2025-10-21-9f1]].

## Sources

- [[sources/web-2025-10-21-9f1]]

## Related

- [[entities/ns-active-condo-corporations-dataset]]
- [[entities/hrm-pplc-building-permits-dataset]]
- [[entities/bc-assessment-search-service]]
- [[entities/ontario-condominium-act-1998]]
