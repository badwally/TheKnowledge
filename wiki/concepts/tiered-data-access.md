---
schema_version: 1
type: concept
slug: tiered-data-access
canonical_name: Tiered Data Access
domains:
- data-collectives
created_at: '2026-06-10T21:14:43Z'
last_updated: '2026-06-10T21:14:43Z'
draft: true
draft_started_at: '2026-06-10T21:14:43Z'
draft_unresolved_claims: 0
---

# Tiered Data Access

## Summary

Tiered data access is a governance pattern in which a data commons exposes its holdings through multiple access levels, each with progressively stricter user authentication and authorization requirements [[sources/web-2023-04-12-931]]. Dahlquist, Nelson, and Fullerton (2023) document tiered access as a near-universal feature of the NIH biomedical data commons, but find substantial divergence in the number and labelling of tiers and in the credential and committee mechanisms that gate them [[sources/web-2023-04-12-931]].

## Key claims

- Multiple tiers of data access with varying user authentication and/or authorization requirements is a shared feature of the surveyed NIH cloud platforms [[sources/web-2023-04-12-931]].
- AoURH uses three tiers labelled 'public', 'registered', and 'controlled', with no login required for public, eRA Commons for registered, and eRA Commons plus more stringent requirements for controlled [[sources/web-2023-04-12-931]].
- AnVIL uses three tiers labelled 'open', 'controlled', and 'consortium', with a Google account for open, eRA Commons for controlled, and direct grant by a designated consortium official for consortium members [[sources/web-2023-04-12-931]].
- BDC uses two tiers labelled 'open' and 'controlled', accepting eRA Commons, Google, or ORCID for open and eRA Commons for controlled [[sources/web-2023-04-12-931]].
- GDC uses two tiers labelled 'open' (no login) and 'controlled' (eRA Commons), with controlled access granted via dbGaP application and Data Access Committee approval [[sources/web-2023-04-12-931]].
- Tier labels are not standardized across platforms — 'public' versus 'open' versus 'registered' refer to overlapping but non-identical access regimes [[sources/web-2023-04-12-931]].
- Differences in tier organization and in authentication/authorization specifics across tiers surface aspects of governance that may require harmonization to achieve interoperability [[sources/web-2023-04-12-931]].

## Sources

- [[sources/web-2023-04-12-931]] — Dahlquist, Nelson, Fullerton (2023), 'Cloud-based biomedical data storage and analysis for genomic research'.

## Related

- [[concepts/biomedical-data-commons]]
- [[concepts/data-access-committee]]
- [[entities/all-of-us-research-hub]]
- [[entities/anvil-platform]]
- [[entities/biodata-catalyst]]
- [[entities/genomic-data-commons]]
