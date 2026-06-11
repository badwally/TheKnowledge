---
schema_version: 1
type: concept
slug: confidential-computing
canonical_name: Confidential Computing
domains:
- data-collectives
created_at: '2026-06-10T22:30:00Z'
last_updated: '2026-06-10T22:30:00Z'
draft: true
draft_started_at: '2026-06-10T22:30:00Z'
draft_unresolved_claims: 0
---

# Confidential Computing

## Summary

Confidential computing is the practice of protecting data in use — during computation — by running workloads inside hardware-isolated trusted execution environments combined with cryptographic remote attestation, so that the cloud operator and other tenants cannot inspect or tamper with the data or code [[sources/web-2026-06-03-4ff]]. Azure Confidential Clean Rooms is Microsoft's implementation of confidential computing applied specifically to multiparty data collaboration use cases [[sources/web-2026-06-03-4ff]].

## Key claims

- Confidential computing as deployed in Azure Confidential Clean Rooms combines TEE-isolated execution with cryptographic remote attestation at each step, so every participant can independently verify that the clean room is running known and attested code on genuine confidential hardware [[sources/web-2026-06-03-4ff]].
- Microsoft's confidential-computing-enabled Spark SQL runs the Spark driver and executors as fully-attested policy-governed enclaves on Confidential Azure Container Instances backed by an AKS cluster [[sources/web-2026-06-03-4ff]].
- Confidential computing in this deployment is paired with open-source publication of clean-room container images and sidecars, so attested code identities can be traced back to verifiable source artifacts via GitHub artifact attestation [[sources/web-2026-06-03-4ff]].

## Sources

- [[sources/web-2026-06-03-4ff]] — Microsoft Learn: Perform Protected Multiparty Data Collaboration on Azure (2026-06-03)

## Related

- [[concepts/trusted-execution-environment]]
- [[concepts/remote-attestation]]
- [[concepts/data-clean-room]]
- [[entities/azure-confidential-clean-rooms]]
