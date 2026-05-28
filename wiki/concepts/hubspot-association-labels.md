---
schema_version: 1
type: concept
slug: hubspot-association-labels
canonical_name: HubSpot Association Labels
domains:
- orita-cmo
created_at: '2026-05-28T14:04:49Z'
last_updated: '2026-05-28T14:04:49Z'
---

# HubSpot Association Labels

## Summary

Association labels in HubSpot are typed annotations on the relationship between two records — for example, marking a contact as the *economic buyer*, *champion*, or *blocker* on a specific deal [[sources/yt-PmViuQw2fNs]]. They are configured under Data Management → Data Model → Associations and are unavailable on Starter licenses; Professional or Enterprise is required [[sources/yt-PmViuQw2fNs]].

## Key claims

- Association labels are managed under Settings → Data Management → Data Model → Associations, scoped per object pair such as deals ↔ contacts [[sources/yt-PmViuQw2fNs]].
- Two configuration shapes are offered: *single labels* and *pair labels*; single labels are the simpler default for role-style annotations [[sources/yt-PmViuQw2fNs]].
- Cardinality is configurable per label — default is many-to-many, but a label can be restricted (e.g. one economic buyer per deal) [[sources/yt-PmViuQw2fNs]].
- Feature gating: association labels require a Professional or Enterprise HubSpot license; Starter licenses cannot use them [[sources/yt-PmViuQw2fNs]].
- Operational pattern: a sales rep working a deal applies the appropriate label (economic buyer / champion / blocker) to the contact on that deal, which becomes the trigger data for downstream segments and deal tags [[sources/yt-PmViuQw2fNs]].

## Sources

- [[sources/yt-PmViuQw2fNs]]

## Related

- [[entities/hubspot]]
- [[concepts/meddic]]
- [[concepts/economic-buyer]]
- [[concepts/hubspot-segments]]
- [[concepts/hubspot-deal-tags]]
