---
schema_version: 1
type: concept
slug: hubspot-deal-tags
canonical_name: HubSpot Deal Tags
domains:
- orita-cmo
created_at: '2026-05-28T14:04:49Z'
last_updated: '2026-05-28T14:04:49Z'
---

# HubSpot Deal Tags

## Summary

Deal tags are colored visual labels that appear on deal cards in the HubSpot pipeline view, driven by membership (or non-membership) in a HubSpot segment, and provide the at-a-glance surface for process-compliance alerts such as "economic buyer missing" [[sources/yt-PmViuQw2fNs]]. They are the rendering layer that turns a segment definition into something a sales manager actually sees during a pipeline review [[sources/yt-PmViuQw2fNs]].

## Key claims

- Deal tags are configured at Settings → Data Management → Objects → Deals → Pipelines → Deal Tags ("Manage deal tags") [[sources/yt-PmViuQw2fNs]].
- A tag has a name, color, pipeline scope (specific pipeline or all pipelines), description, and a filter clause [[sources/yt-PmViuQw2fNs]].
- The description is shown on hover — the recommended pattern is to put the corrective instruction there (e.g. "Economic buyer is missing. Make sure to add one.") so the surface is self-explanatory [[sources/yt-PmViuQw2fNs]].
- The filter clause uses HubSpot segment membership — e.g. "is not a member of: Admin Deals With an Economic Buyer" — so the tag appears on every deal failing the segment criterion [[sources/yt-PmViuQw2fNs]].
- Design principle: encode the *negative* state (missing) as red so that in steady-state most deals are clean and the few non-conforming deals stand out [[sources/yt-PmViuQw2fNs]].
- Behavioral effect on pipeline reviews: managers stop asking the rep about every deal one by one and instead point to the red tags, shifting the conversation toward exception management [[sources/yt-PmViuQw2fNs]].

## Sources

- [[sources/yt-PmViuQw2fNs]]

## Related

- [[concepts/hubspot-segments]]
- [[concepts/hubspot-association-labels]]
- [[concepts/meddic]]
- [[entities/hubspot]]
