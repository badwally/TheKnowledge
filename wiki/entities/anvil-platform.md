---
schema_version: 1
type: entity
slug: anvil-platform
canonical_name: Analysis Visualization and Informatics Lab-space (AnVIL)
entity_kind: product
domains:
- data-collectives
created_at: '2026-06-10T21:14:43Z'
last_updated: '2026-06-10T21:14:43Z'
draft: true
draft_started_at: '2026-06-10T21:14:43Z'
draft_unresolved_claims: 0
---

# Analysis Visualization and Informatics Lab-space (AnVIL)

## Summary

AnVIL is a cloud-based biomedical data platform funded by the National Human Genome Research Institute (NHGRI) that pairs cloud storage with workspace-based analysis tools for genomic data [[sources/web-2023-04-12-931]]. Among the five NIH cloud platforms surveyed by Dahlquist et al. (2023), AnVIL is notable for an explicit 'consortium' access tier in addition to open and controlled tiers, and for piloting the Data Use Oversight System (DUOS) to streamline Data Access Request approvals [[sources/web-2023-04-12-931]].

## Key facts

- Primary funder is the National Human Genome Research Institute (NHGRI) [[sources/web-2023-04-12-931]].
- Data submission requires approval from NHGRI and the AnVIL Ingestion Committee and must conform to the NIH Genomic Data Sharing (GDS) Policy [[sources/web-2023-04-12-931]].
- Participants must be explicitly consented for data sharing, and studies must be registered in dbGaP [[sources/web-2023-04-12-931]].
- The AnVIL Ingestion Committee evaluates applications and coordinates with dataset stewards to determine retention timeframes, long-term storage, archival, and data availability [[sources/web-2023-04-12-931]].
- Uses Gen3 to ingest data [[sources/web-2023-04-12-931]].
- Three access tiers: open, controlled, and consortium [[sources/web-2023-04-12-931]].
- Three authorized user groups: developers, consortia, and external researchers [[sources/web-2023-04-12-931]].
- Authentication uses a Google account for the open tier and eRA Commons for the controlled tier; consortium members are granted access directly by a designated consortium official [[sources/web-2023-04-12-931]].
- Access for controlled tiers is granted by a Data Access Committee (DAC) using the Data Access Request (DAR), dbGaP consent codes, and Data Use Limitations (DULs); consent groups are placed into different workspaces [[sources/web-2023-04-12-931]].
- Piloting the Data Use Oversight System (DUOS) to streamline DAR approval [[sources/web-2023-04-12-931]].
- Security features include two-factor authentication, coverage of all data by a Certificate of Confidentiality, annual independent testing, continuous testing and scanning, and consistency with NIH Security Best Practices and the GDS Policy [[sources/web-2023-04-12-931]].
- Data Management Incidents (DMIs) must be reported to the DAC within 24 hours; Terra and Gen3 log access, undergo audits, and are monitored for abnormal use [[sources/web-2023-04-12-931]].
- Sanctions include access suspension or termination with notification of the user's institution [[sources/web-2023-04-12-931]].

## Sources

- [[sources/web-2023-04-12-931]] — Dahlquist, Nelson, Fullerton (2023), 'Cloud-based biomedical data storage and analysis for genomic research'.

## Related

- [[concepts/biomedical-data-commons]]
- [[concepts/tiered-data-access]]
- [[concepts/data-access-committee]]
- [[entities/dbgap]]
- [[entities/nih-gds-policy]]
