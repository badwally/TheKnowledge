---
schema_version: 1
type: concept
slug: economic-buyer
canonical_name: Economic Buyer
domains:
- orita-cmo
created_at: '2026-05-28T14:04:49Z'
last_updated: '2026-05-28T14:04:49Z'
---

# Economic Buyer

## Summary

The economic buyer is the person on the buyer side of a deal who actually signs the check — the role MEDDIC specifically requires sales reps to identify before treating a deal as close-ready [[sources/yt-PmViuQw2fNs]]. In a HubSpot implementation of MEDDIC, the economic buyer is represented as an association label on the deal↔contact relationship [[sources/yt-PmViuQw2fNs]].

## Key claims

- The canonical MEDDIC failure mode is a rep saying a deal is about to close without having spoken to the economic buyer [[sources/yt-PmViuQw2fNs]].
- In HubSpot, the economic buyer can be modeled as an association label between a deal and a contact, with the cardinality optionally constrained to one economic buyer per deal [[sources/yt-PmViuQw2fNs]].
- The "deal is missing an economic buyer" condition is detected by building an active segment of deals whose associated contacts carry the economic-buyer label, and treating non-membership in that segment as the alert criterion [[sources/yt-PmViuQw2fNs]].
- A natural extension is to make the check stage-gated — e.g. fire an alert (to rep and manager) if a deal reaches "presentation scheduled" without an identified economic buyer [[sources/yt-PmViuQw2fNs]].

## Sources

- [[sources/yt-PmViuQw2fNs]]

## Related

- [[concepts/meddic]]
- [[concepts/hubspot-association-labels]]
- [[concepts/hubspot-deal-tags]]
- [[concepts/hubspot-segments]]
