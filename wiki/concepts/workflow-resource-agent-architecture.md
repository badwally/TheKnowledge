---
schema_version: 1
type: concept
slug: workflow-resource-agent-architecture
canonical_name: Workflow / Resource Agent Architecture
domains:
- orita-cmo
created_at: '2026-05-28T01:52:47Z'
last_updated: '2026-05-28T02:08:38Z'
---

# Workflow / Resource Agent Architecture

## Summary

Orita's marketing-automation system is decomposed into two tiers of agents organized by shared state and decision boundary rather than by org chart [[sources/docx-92ec692fb0f8]]. Workflow agents own end-to-end multi-step processes with a coherent knowledge base, consistent decision model, and well-defined tool surface; resource agents are shared capabilities (voice generation, enrichment, citation authority) that any workflow agent can call without duplicating their knowledge [[sources/docx-25c1bcf28fb8]].

## Key claims

- Decomposition follows the architectural axis (knowledge base + decision boundary), not the organizational axis (marketing function) [[sources/docx-25c1bcf28fb8]].
- A Marketing Operations Orchestrator coordinator agent sits between the human CMO and the workflow agents, maintaining calendar, priorities, cross-agent dependencies, and consolidated reporting [[sources/docx-25c1bcf28fb8]].
- Six workflow agents are specified: Market Intelligence, Pipeline, Engagement, Content Production, Customer Success, and Analytics — each scoped by its primary knowledge sources, decision authority, tool set, and cadence [[sources/docx-25c1bcf28fb8]].
- Three resource agents are specified: Brand Voice (voice-consistent copy generation), Enrichment (the existing /enrich skill generalized as a callable service), and Citation Authority (off-site placement and citation graph) [[sources/docx-25c1bcf28fb8]].
- The orchestrator coordinates but does not make marketing decisions — only sequencing decisions [[sources/docx-25c1bcf28fb8]].
- The CMO retains three decision classes: strategic direction, relationship judgment, and approval of high-stakes outputs (public content, pricing, major campaign launches) [[sources/docx-25c1bcf28fb8]].
- Each agent's tool surface is enumerated explicitly (e.g. Pipeline Agent: Apollo API + HubSpot MCP + PDL + ZeroBounce; Engagement Agent: HubSpot sequences + Gmail MCP + Google Calendar MCP) [[sources/docx-25c1bcf28fb8]].
- Resource agents are not workflow executors — they are quality gates and generative resources called by any workflow agent that needs the capability [[sources/docx-25c1bcf28fb8]].

## Sources

- [[sources/docx-92ec692fb0f8]]
- [[sources/docx-25c1bcf28fb8]]

## Related

- [[entities/orita]]
- [[entities/claude-code]]
- [[entities/hubspot]]
- [[entities/apollo]]
- [[concepts/agent-escalation-levels]]
- [[concepts/hubspot-data-hygiene]]
- [[concepts/aeo-geo]]
