---
schema_version: 1
type: entity
slug: breeze
canonical_name: Breeze
entity_kind: product
domains:
- orita-cmo
created_at: '2026-05-28T04:05:19Z'
last_updated: '2026-05-28T04:05:19Z'
---

# Breeze

## Summary

Breeze is HubSpot's AI product family — the current incarnation of in-platform AI in HubSpot, comprising an in-app assistant for portal queries, "agents" that run as ongoing automations, and a metered credits system [[sources/yt-ZUIprPSbYO4]].

## Key facts

- Branded as the new HubSpot AI incarnation, replacing earlier AI surface areas inside the platform [[sources/yt-ZUIprPSbYO4]].
- Includes an **AI assistant** rendered as a side panel in the HubSpot UI, used primarily for asking specific questions and getting specific answers grounded in the portal's data [[sources/yt-ZUIprPSbYO4]].
- Includes **agents** — ongoing workflow-style automations, positioned as the always-on counterpart to Operations Hub's manually-triggered automations [[sources/yt-ZUIprPSbYO4]].
- Breeze agents are characterized by Tom Granot as "priced to the teeth," appropriate only when continuous execution is required rather than periodic runs [[sources/yt-ZUIprPSbYO4]].
- Backed by a **HubSpot credits system** that meters AI usage across the platform [[sources/yt-ZUIprPSbYO4]].
- Breeze is strong at **read/query operations** but weak at write operations — Tom Granot reports that any action requiring writes was hard to plan and audit through Breeze, pushing him to external Claude Code + REST API tooling [[sources/yt-ZUIprPSbYO4]].
- Breeze cannot create complex workflows or edit existing workflows from natural-language prompts; it refuses certain workflow shapes (e.g. those that could cause infinite loops) [[sources/yt-ZUIprPSbYO4]].

## Sources

- [[sources/yt-ZUIprPSbYO4]]

## Related

- [[entities/hubspot]]
- [[entities/claude-code]]
- [[concepts/hubspot-data-hygiene]]
