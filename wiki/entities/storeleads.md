---
schema_version: 1
type: entity
slug: storeleads
canonical_name: StoreLeads
entity_kind: product
domains:
- orita-cmo
created_at: '2026-05-28T01:52:47Z'
last_updated: '2026-05-28T02:08:37Z'
---

# StoreLeads

## Summary

StoreLeads is a third-party ecommerce data source in Orita's internal stack, identified specifically as the supplier of a 418K Klaviyo customer domain list maintained in a Google Sheet [[sources/docx-92ec692fb0f8]]. In Orita's planned always-on prospecting motion, StoreLeads also serves as the monitor for new Klaviyo adopters, generating real-time signals into the Pipeline Agent's input queue [[sources/docx-25c1bcf28fb8]].

## Key facts

- Source of Orita's 418K Klaviyo domain list [[sources/docx-92ec692fb0f8]].
- New-Klaviyo-adopter alerts are a named always-on prospecting input alongside Apollo pulls and G2 intent data [[sources/docx-25c1bcf28fb8]].

## Sources

- [[sources/docx-92ec692fb0f8]]
- [[sources/docx-25c1bcf28fb8]]

## Related

- [[entities/orita]]
- [[entities/apollo]]
- [[concepts/workflow-resource-agent-architecture]]
