---
schema_version: 1
type: concept
slug: trusted-execution-environment
canonical_name: Trusted Execution Environment (TEE)
domains:
- data-collectives
created_at: '2026-06-10T22:30:00Z'
last_updated: '2026-06-10T22:30:00Z'
draft: true
draft_started_at: '2026-06-10T22:30:00Z'
draft_unresolved_claims: 0
---

# Trusted Execution Environment (TEE)

## Summary

A Trusted Execution Environment (TEE) is a hardware-isolated compute boundary in which code and data are protected from inspection or modification by the host operating system, hypervisor, or cloud operator [[sources/web-2026-06-03-4ff]]. TEEs are the primitive Azure Confidential Clean Rooms uses to run multiparty analytics over combined sensitive data without exposing raw records to the Azure operator [[sources/web-2026-06-03-4ff]].

## Key claims

- Azure Confidential Clean Rooms performs the Spark SQL computation inside a TEE specifically so that raw collaborator data is protected from other collaborators and from the Azure operator during query execution [[sources/web-2026-06-03-4ff]].
- In Azure's clean-room deployment, the TEE instantiation is Confidential Azure Container Instances (C-ACI) running as virtual nodes inside an Azure Kubernetes Service (AKS) cluster [[sources/web-2026-06-03-4ff]].

## Sources

- [[sources/web-2026-06-03-4ff]] — Microsoft Learn: Perform Protected Multiparty Data Collaboration on Azure (2026-06-03)

## Related

- [[concepts/confidential-computing]]
- [[concepts/remote-attestation]]
- [[concepts/data-clean-room]]
- [[entities/azure-confidential-clean-rooms]]
