---
schema_version: 1
type: entity
slug: genomic-data-commons
canonical_name: NCI Genomic Data Commons (GDC)
entity_kind: product
domains:
- data-collectives
created_at: '2026-06-10T21:14:43Z'
last_updated: '2026-06-10T21:14:43Z'
draft: true
draft_started_at: '2026-06-10T21:14:43Z'
draft_unresolved_claims: 0
---

# NCI Genomic Data Commons (GDC)

## Summary

The Genomic Data Commons (GDC) is a cloud-based biomedical data platform funded by the National Cancer Institute (NCI) that aggregates cancer genomic data from multiple study groups for community use [[sources/web-2023-04-12-931]]. Among the five NIH cloud platforms surveyed by Dahlquist et al. (2023), GDC stands out for explicitly preserving data submitter ownership of contributed data and for not specifying sanctions for inappropriate use [[sources/web-2023-04-12-931]].

## Key facts

- Primary funder is the National Cancer Institute (NCI) [[sources/web-2023-04-12-931]].
- Accepts data from different cancer study groups; data submission adheres to NIH and NCI Genomic Data Sharing (GDS) policies [[sources/web-2023-04-12-931]].
- Aggregates data for patients aged 90+ and does not house electronic health records, and does not accept data for participants over 90 years old as individual-level records [[sources/web-2023-04-12-931]].
- Submissions are reviewed by considering a study's size, quality, compatibility with already-hosted data, and likely impact on the field [[sources/web-2023-04-12-931]].
- Any investigator or consortium with cancer genomic data can apply for data submission [[sources/web-2023-04-12-931]].
- Data submitters retain ownership of their data but understand that data will be made available to the scientific community [[sources/web-2023-04-12-931]].
- Submitted data is processed, validated, and harmonized before being hosted [[sources/web-2023-04-12-931]].
- Two access tiers: open (no login required) and controlled (eRA Commons required) [[sources/web-2023-04-12-931]].
- Controlled access is granted via dbGaP application and Data Access Committee (DAC) approval, agreement to the Data Use Agreement and NIH GDS Policy, and submission of a data sharing plan [[sources/web-2023-04-12-931]].
- Data are de-identified according to Health and Human Services Safe Harbor guidelines [[sources/web-2023-04-12-931]].
- The GDC Data Management Incident standard operating procedure is referenced but details of auditing are not specified [[sources/web-2023-04-12-931]].
- Data access is removed if data are discovered to contain Protected Health Information (PHI), Personally Identifiable Information (PII), or are shared out of compliance with sharing conditions set by the DAC; sanctions for inappropriate data use are not specified [[sources/web-2023-04-12-931]].

## Sources

- [[sources/web-2023-04-12-931]] — Dahlquist, Nelson, Fullerton (2023), 'Cloud-based biomedical data storage and analysis for genomic research'.

## Related

- [[concepts/biomedical-data-commons]]
- [[concepts/tiered-data-access]]
- [[concepts/data-access-committee]]
- [[entities/dbgap]]
- [[entities/nih-gds-policy]]
