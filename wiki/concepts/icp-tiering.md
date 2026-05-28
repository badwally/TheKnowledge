---
schema_version: 1
type: concept
slug: icp-tiering
canonical_name: ICP Tiering (Fit + Engagement Scoring)
domains:
- orita-cmo
created_at: '2026-05-28T04:05:19Z'
last_updated: '2026-05-28T04:05:19Z'
---

# ICP Tiering (Fit + Engagement Scoring)

## Summary

ICP Tiering, as implemented in Tom Granot's HubSpot admin skills, is an end-to-end pipeline that elicits ICP criteria from the operator via Claude Code's ask-user interview, audits the current HubSpot property landscape, then builds an ICP-tier property, fit + engagement scoring, classification workflows, and smart lists keyed to the resulting tiers [[sources/yt-ZUIprPSbYO4]].

## Key claims

- The skill is interactive: it uses Claude Code's **ask-user interview** capability to elicit ICP definitions from the operator — e.g. what employee count ranges define each tier, what fit and disqualification criteria apply [[sources/yt-ZUIprPSbYO4]].
- Before building anything, the skill **audits the current state** of properties in the HubSpot portal so its tier construction fits the existing schema [[sources/yt-ZUIprPSbYO4]].
- A new **ICP tier property** is created in HubSpot to carry the classification output [[sources/yt-ZUIprPSbYO4]].
- Scoring is built on HubSpot's **new score feature** combining **fit** and **engagement** components into a composite [[sources/yt-ZUIprPSbYO4]].
- The skill emits **classification workflows** that assign contacts to tiers, and the operator can review them via **smart lists** scoped to each ICP tier [[sources/yt-ZUIprPSbYO4]].
- Because the HubSpot Workflows API is unreliable, the classification-workflow portion is delivered as **manual UI build instructions** that Claude Code (optionally via its Chrome browser-use feature) walks through, rather than as fully-programmatic workflow creation [[sources/yt-ZUIprPSbYO4]].
- Tom Granot describes this skill as his "proud and joy" within the repo, signaling its perceived value relative to the other admin skills [[sources/yt-ZUIprPSbYO4]].

## Sources

- [[sources/yt-ZUIprPSbYO4]]

## Related

- [[entities/hubspot]]
- [[entities/hubspot-admin-skills]]
- [[entities/claude-code]]
- [[entities/tom-granot]]
- [[concepts/hubspot-data-hygiene]]
- [[concepts/plan-before-execute-after]]
