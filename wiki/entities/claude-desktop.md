---
schema_version: 1
type: entity
slug: claude-desktop
canonical_name: Claude Desktop
entity_kind: product
domains:
- orita-cmo
created_at: '2026-05-28T04:05:18Z'
last_updated: '2026-05-28T04:05:18Z'
---

# Claude Desktop

## Summary

Claude Desktop is Anthropic's desktop chat client for Claude, distinct from the Claude Code agentic-coding harness; it is the runtime in which end users wire up MCP servers — including HubSpot's official MCP — to give the model tool access to external systems [[sources/yt-bZo4jVdZfaI]].

## Key facts

- MCP configuration UX: Settings → Developer → "Edit config" opens `claude_desktop_config.json` for direct edit; users paste an MCP server entry there [[sources/yt-bZo4jVdZfaI]].
- A full app restart ("quit it and reopen it") is required after editing the config for the new MCP server to register [[sources/yt-bZo4jVdZfaI]].
- Operator-facing surface for MCP demos: the same chat thread issues natural-language commands and renders intermediate tool calls (query planning, deal-stage resolution, contact lookup, record creation) inline as they execute [[sources/yt-bZo4jVdZfaI]].
- Distinct from Claude Code: Claude Desktop is the consumer chat app and is the runtime in the source's demo; Claude Code is the agentic coding harness referenced elsewhere in Orita's stack [[sources/yt-bZo4jVdZfaI]].

## Sources

- [[sources/yt-bZo4jVdZfaI]] — Greg Karelitz demo, configuration walkthrough segment

## Related

- [[entities/hubspot-mcp]]
- [[entities/claude-code]]
- [[entities/hubspot]]
- [[concepts/external-ai-crm-surface]]
