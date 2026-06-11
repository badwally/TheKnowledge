---
schema_version: 1
type: concept
slug: network-of-networks
canonical_name: Network-of-Networks Health Information Exchange
domains:
- data-collectives
created_at: '2026-06-11T03:30:34Z'
last_updated: '2026-06-11T03:30:34Z'
draft: true
draft_started_at: '2026-06-11T03:30:34Z'
draft_unresolved_claims: 0
---

# Network-of-Networks Health Information Exchange

## Summary

The "network-of-networks" pattern is the architectural model TEFCA implements: rather than centralizing data, a small number of designated backbone networks (QHINs) interconnect under a shared legal contract and shared technical specification, with end organizations (Participants and Subparticipants) connecting upward to a QHIN to reach all the others. [[sources/web-2026-06-09-e4c]]

## Key claims

- TEFCA's nationwide exchange architecture is a "network-of-networks" in which Qualified Health Information Networks (QHINs) form the backbone and act as the central connection points. [[sources/web-2026-06-09-e4c]]
- The pattern is designed to establish a "universal floor for interoperability," enabling data to be shared beyond proprietary boundaries regardless of where the information is stored. [[sources/web-2026-06-09-e4c]]
- Participants — including hospitals, health systems, public health agencies, and regional health information exchanges (HIEs) — connect to QHINs to reach other Participants under other QHINs; some Participants have their own Subparticipants. [[sources/web-2026-06-09-e4c]]
- A stated economic rationale for the network-of-networks pattern is that providers no longer need to join multiple networks or build one-off, point-to-point connections to reach every counterparty, lowering integration cost per relationship. [[sources/web-2026-06-09-e4c]]
- The pattern relies on a shared legal contract (the Common Agreement) and a shared technical specification (the QHIN Technical Framework) to enforce uniform privacy, security, and interoperability requirements across heterogeneous participating networks. [[sources/web-2026-06-09-e4c]]

## Sources

- [[sources/web-2026-06-09-e4c]]

## Related

- [[entities/tefca]]
- [[concepts/qhin]]
- [[concepts/common-agreement]]
- [[concepts/data-intermediary]]
- [[concepts/biomedical-data-commons]]
- [[concepts/consumer-driven-banking]]
