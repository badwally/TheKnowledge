---
schema_version: 1
type: entity
slug: autogen
canonical_name: AutoGen
entity_kind: product
domains:
- orita-cmo
created_at: '2026-05-28T02:00:18Z'
last_updated: '2026-05-28T02:00:18Z'
---

# AutoGen

## Summary

AutoGen is a conversation-driven multi-agent framework whose GroupChat mode is the most natural fit for the “agents challenge each other” pattern at Level 4 of Orita's escalation framework [[sources/docx-b90a5e5fdcc4]]. It is also identified as the hardest to control and most expensive option among Level 4 candidates because every turn is an LLM call [[sources/docx-b90a5e5fdcc4]].

## Key facts

- Primary primitive: GroupChat — conversation-driven multi-agent interaction [[sources/docx-b90a5e5fdcc4]].
- Strengths: most natural framework for adversarial / complementary reasoning loops where agents challenge each other's claims [[sources/docx-b90a5e5fdcc4]].
- Weaknesses: hardest to control of the Level 4 candidates and most expensive because every turn is an LLM call [[sources/docx-b90a5e5fdcc4]].
- Orita verdict: deferred behind single-pass LLM synthesis as the default for collaborative reasoning tasks (e.g., CMO briefing synthesis, campaign strategy development) until single-pass is demonstrably insufficient [[sources/docx-b90a5e5fdcc4]].

## Sources

- [[sources/docx-b90a5e5fdcc4]] — Orita Agent Architecture Analysis (2026-04-03)

## Related

- [[concepts/agent-escalation-levels]]
- [[entities/langgraph]]
- [[entities/crewai]]
