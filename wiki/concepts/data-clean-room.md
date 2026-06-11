---
schema_version: 1
type: concept
slug: data-clean-room
canonical_name: Data Clean Room
domains:
- data-collectives
created_at: '2026-06-10T22:30:00Z'
last_updated: '2026-06-10T22:30:00Z'
draft: true
draft_started_at: '2026-06-10T22:30:00Z'
draft_unresolved_claims: 0
---

# Data Clean Room

## Summary

A data clean room is a protected shared execution environment in which multiple organizations pool sensitive data and run joint computations without exposing raw records to one another or to the environment's operator [[sources/web-2026-06-03-4ff]]. Clean rooms combine confidential computing, cryptographic remote attestation, schema-level access controls, and output-suppression rules to make competitor or cross-institution data collaboration feasible where privacy, regulation, or commercial sensitivity would otherwise block it [[sources/web-2026-06-03-4ff]].

## Key claims

- A clean room provides a single shared compute boundary in which combined datasets from multiple parties are queried, while the operator (in Azure's case, Microsoft) is excluded from access to raw data during query execution [[sources/web-2026-06-03-4ff]].
- Clean rooms typically enforce a schema-level access control: each contributed dataset declares an `allowedFields` list, which limits queries to a whitelisted column projection and excludes every other source column from access [[sources/web-2026-06-03-4ff]].
- Clean rooms enforce per-query pre-conditions (minimum input row counts under which the query is rejected) and post-filters (minimum group counts below which aggregated output groups are suppressed) to prevent individual-level re-identification from query outputs [[sources/web-2026-06-03-4ff]].
- Approval workflows require every collaborator whose data is referenced by a query to consent to that query before execution [[sources/web-2026-06-03-4ff]].
- Microsoft documents target deployments across media/advertising audience activation, bank–insurer and bank–retailer joint offers, intra-government collaboration, multi-hospital disease-pattern studies and clinical-trial recruitment, and cross-retailer customer-behavior analysis [[sources/web-2026-06-03-4ff]].

## Sources

- [[sources/web-2026-06-03-4ff]] — Microsoft Learn: Perform Protected Multiparty Data Collaboration on Azure (2026-06-03)

## Related

- [[concepts/trusted-execution-environment]]
- [[concepts/confidential-computing]]
- [[concepts/remote-attestation]]
- [[concepts/query-output-controls]]
- [[concepts/data-intermediary]]
- [[entities/azure-confidential-clean-rooms]]
- [[entities/confidential-consortium-framework]]
