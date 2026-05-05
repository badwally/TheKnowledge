---
type: concept
slug: manifest-based-deployment
canonical_name: Manifest-Based Deployment
domains:
  - trading-and-markets
---

# Manifest-Based Deployment

## Summary

Declarative deployment model proposed by the 2018 Akash Network position paper: the user describes their desired deployment in a manifest file containing workload definitions, configuration, and connection rules; the manifest is distributed peer-to-peer between a client's providers, and a hash of the manifest — the deployment version — is anchored on the blockchain-based distributed database [[sources/pdf-c9b8f466ea39]].

## Key claims

- "A user describes their desired deployment in a manifest. The manifest is written in a declarative file format that contains workload definitions, configuration, and connection rules" [[sources/pdf-c9b8f466ea39]].
- Providers use workload definitions and configuration to execute the workloads on the resources they are providing, and use the connection rules to build an overlay network and firewall configurations [[sources/pdf-c9b8f466ea39]].
- "A hash of the manifest is known as the deployment version and is stored on the blockchain-based distributed database" [[sources/pdf-c9b8f466ea39]].
- The manifest contains sensitive information that should only be shared with participants of the deployment, posing a problem for self-managed deployments — Akash must distribute the workload definition autonomously without revealing its contents to unauthorized parties [[sources/pdf-c9b8f466ea39]].
- Akash provides a peer-to-peer protocol for distributing workloads and deployment configuration to and between a client's providers [[sources/pdf-c9b8f466ea39]].
- Workloads are defined as Docker containers, chosen because they "allow for highly-isolated and configurable execution environments, and are already part of many cloud-based deployments today" [[sources/pdf-c9b8f466ea39]].

## Sources

- [[sources/pdf-c9b8f466ea39]]

## Related

- [[entities/akash-network]]
- [[concepts/akash-deployment-fulfillment-order]]
