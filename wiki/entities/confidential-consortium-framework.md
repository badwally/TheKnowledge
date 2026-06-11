---
schema_version: 1
type: entity
slug: confidential-consortium-framework
canonical_name: Confidential Consortium Framework (CCF)
entity_kind: product
domains:
- data-collectives
created_at: '2026-06-10T22:30:00Z'
last_updated: '2026-06-10T22:30:00Z'
draft: true
draft_started_at: '2026-06-10T22:30:00Z'
draft_unresolved_claims: 0
---

# Confidential Consortium Framework (CCF)

## Summary

The Confidential Consortium Framework (CCF) is a framework for building governance, consent, and audit primitives on top of confidential computing; Azure Confidential Clean Rooms incorporates an implementation of CCF to manage clean-room membership, query approval, consent verification, and tamper-resistant audit trails for multiparty data collaboration [[sources/web-2026-06-03-4ff]].

## Key facts

- Azure Confidential Clean Rooms ships with an implementation of CCF that enforces clean-room governance, including approval workflows for queries and verification of collaborator consent to access sensitive data [[sources/web-2026-06-03-4ff]].
- The CCF-based governance layer is the mechanism by which Azure Confidential Clean Rooms produces tamper-resistant audit trails of salient clean-room events [[sources/web-2026-06-03-4ff]].

## Sources

- [[sources/web-2026-06-03-4ff]] — Microsoft Learn: Perform Protected Multiparty Data Collaboration on Azure (2026-06-03)

## Related

- [[entities/azure-confidential-clean-rooms]]
- [[concepts/data-clean-room]]
- [[concepts/confidential-computing]]
