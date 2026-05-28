---
schema_version: 1
type: entity
slug: hubspot
canonical_name: HubSpot
entity_kind: product
domains:
- orita-cmo
created_at: '2026-05-28T01:45:51Z'
last_updated: '2026-05-28T02:08:37Z'
---

# HubSpot

## Summary

HubSpot is the CRM system Orita uses as its customer source-of-truth, holding both current customer and target-list prospect records along with agency-of-record relationships [[sources/pdf-4931157e130a]]. HubSpot is the system of record for pipeline management in Orita's planned marketing automation chain, covering contact lifecycle, lead scoring, pipeline stages, deal tracking, and forecasting [[sources/docx-25c1bcf28fb8]].

## Key facts

- CRM source-of-truth for customer and prospect records and agency-of-record relationships [[sources/pdf-4931157e130a]].
- Designated system of record for Stage 5 (CRM & Pipeline Management) of Orita's end-to-end marketing automation chain [[sources/docx-25c1bcf28fb8]].
- Accessed via HubSpot MCP by the Pipeline, Engagement, Customer Success, and Analytics Agents in Orita's planned architecture [[sources/docx-25c1bcf28fb8]].
- All prospecting inputs (Apollo, StoreLeads, G2 intent, event lists) terminate in HubSpot through the same identify-filter-enrich-validate routing pattern [[sources/docx-25c1bcf28fb8]].

## Sources

- [[sources/pdf-4931157e130a]]
- [[sources/docx-92ec692fb0f8]]
- [[sources/docx-25c1bcf28fb8]]

## Related

- [[entities/orita]]
- [[entities/apollo]]
- [[entities/storeleads]]
- [[concepts/hubspot-data-hygiene]]
- [[concepts/workflow-resource-agent-architecture]]
