---
schema_version: 1
type: entity
slug: crewai
canonical_name: CrewAI
entity_kind: product
domains:
- orita-cmo
created_at: '2026-05-28T02:00:18Z'
last_updated: '2026-05-28T02:00:18Z'
---

# CrewAI

## Summary

CrewAI is a multi-agent orchestration framework offering hierarchical and sequential process modes [[sources/docx-b90a5e5fdcc4]]. Orita's architecture analysis treats CrewAI as a weaker fit than LangGraph for Level 2 routing because its manager-LLM has documented coordination-quality issues and adds latency and cost without corresponding routing intelligence [[sources/docx-b90a5e5fdcc4]].

## Key facts

- Hierarchical mode adds a manager LLM call that routes tasks to worker agents; in practice the manager does not reliably route, with documented coordination-quality issues [[sources/docx-b90a5e5fdcc4]].
- Sequential process: each agent refines the previous agent's output in a fixed order — simple but rigid; evaluated as a Level 4 collaborative-reasoning option [[sources/docx-b90a5e5fdcc4]].
- Stability concern: CrewAI has broken backward compatibility multiple times, cited as a reason to avoid system-wide framework adoption [[sources/docx-b90a5e5fdcc4]].
- Orita verdict: not the recommended framework for Level 2 (LangGraph wins) or Level 3 (event bus, not a multi-agent framework, is the right abstraction) [[sources/docx-b90a5e5fdcc4]].

## Sources

- [[sources/docx-b90a5e5fdcc4]] — Orita Agent Architecture Analysis (2026-04-03)

## Related

- [[concepts/agent-escalation-levels]]
- [[entities/langgraph]]
- [[entities/autogen]]
