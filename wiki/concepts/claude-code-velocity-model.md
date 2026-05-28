---
schema_version: 1
type: concept
slug: claude-code-velocity-model
canonical_name: Claude Code Velocity Model
domains:
- orita-cmo
created_at: '2026-05-28T01:52:47Z'
last_updated: '2026-05-28T01:52:47Z'
---

# Claude Code Velocity Model

## Summary

The Claude Code Velocity Model is Orita's internal calibration of build effort under Claude Code with Opus-class agents: the dominant cost is spec writing and CMO knowledge extraction, not implementation labor, and traditional engineering timelines collapse by roughly 10x [[sources/docx-92ec692fb0f8]].

## Key claims

- MCP connectors (HubSpot, Google Workspace, Slack, Notion) are configuration, not engineering, with minutes-per-connector setup [[sources/docx-92ec692fb0f8]].
- REST API integrations against documented endpoints (Apollo, ZeroBounce, StoreLeads via Sheets API) are implemented by Claude Code in a single session, exemplified by the etail-contact-enrichment pipeline [[sources/docx-92ec692fb0f8]].
- Level 0 skills are structured prompts plus a cron trigger plus one or two API calls, scaffolded directly; the variable cost is prompt-tuning iterations, not architecture [[sources/docx-92ec692fb0f8]].
- Prompt-iteration cadence is 1–2 rounds for simple skills (pipeline reports, CRM hygiene) and more for judgment-heavy skills (competitive monitoring, enrichment-on-create, content generation); each round is minutes, not hours [[sources/docx-92ec692fb0f8]].
- Calibration: a focused technical operator can wire four core integrations in an afternoon and scaffold eight Level 0 skills in 1–2 additional days, putting a full Phase 1 equivalent at 2–3 focused days [[sources/docx-92ec692fb0f8]].
- Multiple Opus 4.6 agents working independent workflow clusters in parallel compress calendar time further; the binding constraints become human inputs — CMO interviews (4–6 hours), brand-voice formalization, and quality review cycles [[sources/docx-92ec692fb0f8]].
- The estimation contract for Orita is to measure spec hours plus stakeholder hours and present cost as a one-time build sprint plus monthly operating, never as weekly engineering hours over months [[sources/docx-92ec692fb0f8]].

## Sources

- [[sources/docx-92ec692fb0f8]]

## Related

- [[concepts/agent-escalation-levels]]
- [[concepts/workflow-resource-agent-architecture]]
- [[entities/claude-code]]
- [[entities/orita]]
