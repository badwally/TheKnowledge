---
schema_version: 1
type: entity
slug: hubspot
canonical_name: HubSpot
entity_kind: product
domains:
- orita-cmo
created_at: '2026-05-28T01:45:51Z'
last_updated: '2026-05-28T14:54:19Z'
---

# HubSpot

## Summary

HubSpot is the CRM system Orita uses as its customer source-of-truth, holding both current customer and target-list prospect records along with agency-of-record relationships [[sources/pdf-4931157e130a]]. HubSpot also publishes an official **HubSpot MCP** server — an npm package linked from `developers.hubspot.com/mcp` — that exposes CRM read, write, and cross-object operations to MCP-capable AI clients such as Claude Desktop [[sources/yt-bZo4jVdZfaI]].

## Key facts

- Customer source-of-truth at Orita; holds both current customers and target-list prospects, including agency-of-record fields [[sources/pdf-4931157e130a]].
- AI integration paths into HubSpot now include at least three operator-relevant options: (a) **Breeze**, HubSpot's in-platform AI product family; (b) the official **HubSpot MCP** server for external AI clients via the Model Context Protocol [[sources/yt-bZo4jVdZfaI]]; and (c) third-party Claude Code skills that hit HubSpot's REST API directly (Tom Granot's HubSpot Admin Skills) [[sources/yt-bZo4jVdZfaI]].
- MCP authentication uses HubSpot **private app** tokens, generated under Settings → Integrations → Account Management → Private Apps; the private app's scope selection bounds the MCP server's effective API surface [[sources/yt-bZo4jVdZfaI]].
- Demonstrated MCP operations from a Claude Desktop chat: deal queries by close-date window with value rollups, traversal from deal to associated contacts, contact creation with deal association, and writing web-research output back as new contact records with research notes [[sources/yt-bZo4jVdZfaI]].
- Setup posture for the MCP path is operator/developer-grade — create private app, pick scopes, copy token, edit `claude_desktop_config.json`, restart the client — not a one-click consumer install [[sources/yt-bZo4jVdZfaI]].

## Sources

- [[sources/pdf-4931157e130a]] — Orita strategic planning session, agency-of-record context
- [[sources/yt-bZo4jVdZfaI]] — Greg Karelitz demo of Claude + HubSpot MCP

## Related

- [[entities/orita]]
- [[entities/breeze]]
- [[entities/hubspot-mcp]]
- [[entities/claude-desktop]]
- [[entities/hubspot-admin-skills]]
- [[entities/tom-granot]]
- [[concepts/hubspot-data-hygiene]]
- [[concepts/external-ai-crm-surface]]
