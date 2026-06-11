---
schema_version: 1
type: entity
slug: azure-confidential-clean-rooms
canonical_name: Azure Confidential Clean Rooms
entity_kind: product
domains:
- data-collectives
created_at: '2026-06-10T22:30:00Z'
last_updated: '2026-06-10T22:30:00Z'
draft: true
draft_started_at: '2026-06-10T22:30:00Z'
draft_unresolved_claims: 0
---

# Azure Confidential Clean Rooms

## Summary

Azure Confidential Clean Rooms is Microsoft's commercial clean-room substrate for multiparty data collaboration, providing a protected environment in which organizations can pool sensitive data and run joint analytics without exposing raw records to one another or to the Azure operator [[sources/web-2026-06-03-4ff]]. The "Analytics" variant of the service is in limited preview as of June 2026 and uses confidential-compute-enabled Apache Spark SQL for big-data analytics over combined datasets [[sources/web-2026-06-03-4ff]].

## Key facts

- Azure Confidential Clean Rooms is a fully managed Azure service whose Analytics variant exposes Spark SQL over confidential computing infrastructure, freeing customers from provisioning or scaling the underlying compute [[sources/web-2026-06-03-4ff]].
- The Spark driver and executors run as fully-attested policy-governed enclaves on virtual nodes deployed on Confidential Azure Container Instances (C-ACI) inside an Azure Kubernetes Service (AKS) cluster [[sources/web-2026-06-03-4ff]].
- The service supports CSV, Parquet, and JSON as input and output formats [[sources/web-2026-06-03-4ff]].
- More than two organizations may participate in a single clean-room collaboration [[sources/web-2026-06-03-4ff]].
- Every collaborator whose dataset is referenced by a query must approve that query before it executes [[sources/web-2026-06-03-4ff]].
- Each contributed dataset declares an `allowedFields` list so that only whitelisted columns are exposed to clean-room queries; every other column in the source storage is excluded from access [[sources/web-2026-06-03-4ff]].
- Published queries can declare a minimum row count per input view (a pre-condition that rejects the query if unmet) and a minimum group count under which aggregated output groups are suppressed (a post-filter), to prevent individual-level re-identification from query outputs [[sources/web-2026-06-03-4ff]].
- Microsoft publishes the clean-room container images and sidecars at `mcr.microsoft.com/cleanroom`, with source code in the Azure/azure-cleanroom GitHub repository and provenance verifiable via GitHub artifact attestation [[sources/web-2026-06-03-4ff]].
- The service's governance (membership management, query approval, consent verification, tamper-resistant audit trails) is built on an implementation of the Confidential Consortium Framework (CCF) [[sources/web-2026-06-03-4ff]].
- Microsoft documents target use cases across media/advertising (CRM × publisher audience activation, measurement and attribution), banking and finance (bank–insurer upsell, bank–retailer joint offers), government and public sector (cross-department collaboration, traffic and weather workloads), healthcare (multi-hospital disease-pattern studies, clinical trial recruitment), and retail (cross-retailer customer-behavior analysis) [[sources/web-2026-06-03-4ff]].
- Microsoft explicitly forbids using the preview to process personal data or data subject to legal or regulatory compliance requirements [[sources/web-2026-06-03-4ff]].

## Sources

- [[sources/web-2026-06-03-4ff]] — Microsoft Learn: Perform Protected Multiparty Data Collaboration on Azure (2026-06-03)

## Related

- [[concepts/data-clean-room]]
- [[concepts/trusted-execution-environment]]
- [[concepts/confidential-computing]]
- [[concepts/remote-attestation]]
- [[concepts/query-output-controls]]
- [[entities/confidential-consortium-framework]]
