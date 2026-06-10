---
schema_version: 1
type: concept
slug: data-access-committee
canonical_name: Data Access Committee (DAC)
domains:
- data-collectives
created_at: '2026-06-10T21:14:43Z'
last_updated: '2026-06-10T21:14:43Z'
draft: true
draft_started_at: '2026-06-10T21:14:43Z'
draft_unresolved_claims: 0
---

# Data Access Committee (DAC)

## Summary

A Data Access Committee (DAC) is a project-level review body within a biomedical data commons that decides whether a specific researcher's Data Access Request (DAR) is consistent with the consent codes and Data Use Limitations (DULs) attached to a dataset [[sources/web-2023-04-12-931]]. The DAC is the predominant authorization mechanism across the NIH cloud commons surveyed by Dahlquist, Nelson, and Fullerton (2023), with the explicit exception of the All of Us Research Hub, which uses a user-level 'data passport' model instead [[sources/web-2023-04-12-931]].

## Key claims

- A DAC determines access via Data Access Requests (DARs), dbGaP consent codes, and Data Use Limitations (DULs) [[sources/web-2023-04-12-931]].
- AnVIL's DAC determines access using DARs, dbGaP consent codes, and DULs, and places consent groups into different workspaces [[sources/web-2023-04-12-931]].
- BDC's DAC determines access using DARs, dbGaP consent codes, and DULs, and may require a Cloud Use Statement [[sources/web-2023-04-12-931]].
- GDC applies via dbGaP and the DAC approves or denies access [[sources/web-2023-04-12-931]].
- AoURH explicitly does not use project-based DACs; access authorization is instead determined via a user-based 'data passport' model [[sources/web-2023-04-12-931]].
- AnVIL is piloting the Data Use Oversight System (DUOS) to streamline DAR approval — a partial automation of the DAC workflow [[sources/web-2023-04-12-931]].
- Data Management Incidents (DMIs) at AnVIL must be reported to the DAC within 24 hours [[sources/web-2023-04-12-931]].
- GDC removes data access if data are discovered to contain PHI or PII, or if data are shared out of compliance with sharing conditions set by the DAC [[sources/web-2023-04-12-931]].

## Sources

- [[sources/web-2023-04-12-931]] — Dahlquist, Nelson, Fullerton (2023), 'Cloud-based biomedical data storage and analysis for genomic research'.

## Related

- [[concepts/biomedical-data-commons]]
- [[concepts/tiered-data-access]]
- [[entities/anvil-platform]]
- [[entities/biodata-catalyst]]
- [[entities/genomic-data-commons]]
- [[entities/all-of-us-research-hub]]
- [[entities/dbgap]]
