---
schema_version: 1
type: concept
slug: orchestrator-worker-pattern
canonical_name: Orchestrator-Worker Pattern (Multi-Agent)
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Orchestrator-Worker Pattern (Multi-Agent)

## Summary

A multi-agent architecture in which a lead agent coordinates the overall process — analyzing the user query, developing a strategy, and delegating bounded sub-tasks — while specialized worker subagents execute those sub-tasks in parallel and return findings to the lead; the architecture Anthropic adopted for the Claude Research feature [[sources/pdf-f478e5f11837]].

## Key claims

- Anthropic's Research system uses a multi-agent architecture with an orchestrator-worker pattern, where a lead agent coordinates the process while delegating to specialized subagents that operate in parallel [[sources/pdf-f478e5f11837]].
- When a user submits a query, the lead agent analyzes it, develops a strategy, and spawns subagents to explore different aspects simultaneously; the subagents act as intelligent filters by iteratively using search tools and returning findings to the lead agent so it can compile a final answer [[sources/pdf-f478e5f11837]].
- The lead agent saves its plan to a Memory tool to persist context, since if the context window exceeds 200,000 tokens it will be truncated and the plan must survive [[sources/pdf-f478e5f11837]].
- The lead agent decomposes queries into subtasks and describes them to subagents; each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries [[sources/pdf-f478e5f11837]].
- Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information; Anthropic observed early failures where one subagent explored the 2021 automotive chip crisis while two others duplicated work investigating 2025 supply chains [[sources/pdf-f478e5f11837]].
- After research subagents return, the system passes findings to a CitationAgent, which processes the documents and research report to identify specific locations for citations and ensure all claims are properly attributed [[sources/pdf-f478e5f11837]].

## Sources

- [[sources/pdf-f478e5f11837]]

## Related

- [[concepts/multi-agent-system]]
- [[concepts/subagent]]
- [[entities/anthropic]]
