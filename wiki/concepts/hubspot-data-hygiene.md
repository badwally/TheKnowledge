---
schema_version: 1
type: concept
slug: hubspot-data-hygiene
canonical_name: HubSpot Data Hygiene
domains:
- orita-cmo
created_at: '2026-05-28T01:45:53Z'
last_updated: '2026-05-28T14:46:49Z'
---

# HubSpot Data Hygiene

## Summary

HubSpot data hygiene at Orita is the maintenance problem of keeping CRM records — especially agency-of-record fields and audience-list-pull logic — accurate enough to drive downstream automation reliably [[sources/docx-92ec692fb0f8]]. A complementary external view treats data hygiene as a recurring, taxonomized set of cleanup routines that should run on different cadences (weekly manual cleanup, quarterly deep cleanup) and that benefit from being encoded as Claude Code skills rather than ad-hoc scripts [[sources/yt-ZUIprPSbYO4]].

## Key claims

- Maintaining agency-of-record fields is necessary for Orita's audience-list-pull logic to work correctly [[sources/docx-92ec692fb0f8]].
- Hygiene work decomposes into easy categorical rules (suppress contacts whose email has hard-bounced, suppress contacts with unsubscribe state) and harder rules (ghost contacts, stale owners) [[sources/yt-ZUIprPSbYO4]].
- **Ghost contacts** — contacts with no activity since their addition to the CRM, often years prior — should be suppressed from marketing-contact status even when their flag from creation time persists; otherwise they continue to consume paid contact quota [[sources/yt-ZUIprPSbYO4]].
- **Data enrichment** in hygiene practice is cross-referential — company-level data is used to fill contact-level gaps and vice versa [[sources/yt-ZUIprPSbYO4]].
- Hygiene should run on two cadences: a lightweight **weekly cleanup routine** (manually triggered) and a deeper **quarterly database cleanup** that may take an hour or two to complete [[sources/yt-ZUIprPSbYO4]].
- A **HubSpot audit skill** that walks the portal and makes recommendations is treated as the entry point — its output feeds an implementation plan that drives the downstream hygiene work [[sources/yt-ZUIprPSbYO4]].

## Sources

- [[sources/docx-92ec692fb0f8]]
- [[sources/yt-ZUIprPSbYO4]]

## Related

- [[entities/hubspot]]
- [[entities/orita]]
- [[entities/hubspot-admin-skills]]
- [[concepts/icp-tiering]]
- [[concepts/plan-before-execute-after]]
