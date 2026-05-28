---
schema_version: 1
type: concept
slug: hubspot-segments
canonical_name: HubSpot Segments
domains:
- orita-cmo
created_at: '2026-05-28T14:04:49Z'
last_updated: '2026-05-28T14:04:49Z'
---

# HubSpot Segments

## Summary

HubSpot Segments are object-scoped dynamic lists defined by record criteria, and serve as the bridge between low-level data (e.g. association labels) and surface features such as deal tags and workflow triggers [[sources/yt-PmViuQw2fNs]]. Saved as active lists, they stay continuously up to date as underlying records change [[sources/yt-PmViuQw2fNs]].

## Key claims

- Segments are accessed under CRM → Segments and can be scoped to any object (deals, contacts, etc.) [[sources/yt-PmViuQw2fNs]].
- Segment criteria can reference associations and association labels — e.g. "associated contacts with label = Economic Buyer, where record ID is known" — which yields all deals with at least one labeled contact of that role [[sources/yt-PmViuQw2fNs]].
- Saving a segment as an "active list" makes it continuously re-evaluated so its membership reflects the current data state [[sources/yt-PmViuQw2fNs]].
- Segments are the filter input to downstream visual features — most notably deal tags, whose filter clause is segment membership or non-membership [[sources/yt-PmViuQw2fNs]].

## Sources

- [[sources/yt-PmViuQw2fNs]]

## Related

- [[concepts/hubspot-association-labels]]
- [[concepts/hubspot-deal-tags]]
- [[entities/hubspot]]
