---
schema_version: 1
type: entity
slug: claude-code
canonical_name: Claude Code
entity_kind: product
domains:
- orita-cmo
created_at: '2026-05-28T01:45:51Z'
last_updated: '2026-05-28T14:46:49Z'
---

# Claude Code

## Summary

Claude Code is Anthropic's agentic coding harness, used by Orita's CMO as the runtime for building company-wide skills and agents [[sources/pdf-4931157e130a]]. Orita's internal practice treats Claude Code as the primary build surface where spec writing dominates over coding effort [[sources/docx-92ec692fb0f8]]. Outside Orita, Claude Code is also the runtime of choice for SaaS-admin automation patterns that bypass thin or read-only first-party MCP servers by driving REST APIs directly from generated scripts [[sources/yt-ZUIprPSbYO4]].

## Key facts

- Used by Orita's CMO as the runtime for building company-wide skills and agents [[sources/pdf-4931157e130a]].
- The dominant build cost under Claude Code is spec writing, not coding [[sources/docx-92ec692fb0f8]].
- Supports an **ask-user / interview feature** that lets a skill proactively interview the operator for requirements at plan time (used by Tom Granot's ICP-tier skill to elicit fit and engagement definitions) [[sources/yt-ZUIprPSbYO4]].
- Supports **Chrome / browser-use inside Claude Code**, which Tom Granot uses to drive HubSpot's UI when the Workflows API is too unstable to script reliably [[sources/yt-ZUIprPSbYO4]].
- Claude Code skills can be packaged as installable extensions that ship with structured plan/before/execute/after stages and explicit checklists per skill [[sources/yt-ZUIprPSbYO4]].
- For SaaS-admin work, practitioners prefer generating their own REST scripts inside Claude Code over relying on first-party MCP servers, because the MCP often lacks write tools or cross-system reach (e.g. HubSpot MCP is read-only and cannot fetch from external resources mid-flow) [[sources/yt-ZUIprPSbYO4]].

## Sources

- [[sources/pdf-4931157e130a]]
- [[sources/docx-92ec692fb0f8]]
- [[sources/yt-ZUIprPSbYO4]]

## Related

- [[entities/orita]]
- [[entities/hubspot]]
- [[entities/hubspot-admin-skills]]
- [[entities/tom-granot]]
- [[concepts/plan-before-execute-after]]
- [[concepts/claude-code-velocity-model]]
