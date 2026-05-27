---
schema_version: 1
type: concept
slug: subagent
canonical_name: Subagent (LLM Multi-Agent System)
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Subagent

## Summary

A worker LLM agent within a multi-agent system that operates with its own context window, tools, and prompt, executing a bounded sub-task delegated by a lead agent and returning a compressed result; in Anthropic's Research feature, subagents perform parallel web searches and act as intelligent filters that condense findings before reporting back [[sources/pdf-f478e5f11837]].

## Key claims

- Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of a question simultaneously before condensing the most important tokens for the lead research agent [[sources/pdf-f478e5f11837]].
- Each subagent provides separation of concerns — distinct tools, prompts, and exploration trajectories — which reduces path dependency and enables thorough, independent investigations [[sources/pdf-f478e5f11837]].
- Each subagent independently performs web searches, evaluates tool results using interleaved thinking, and returns findings to the lead researcher [[sources/pdf-f478e5f11837]].
- Anthropic embeds explicit scaling rules in prompts to allocate subagent effort: simple fact-finding requires 1 agent with 3–10 tool calls, direct comparisons might need 2–4 subagents with 10–15 calls each, and complex research can use more than 10 subagents with clearly divided responsibilities [[sources/pdf-f478e5f11837]].
- Early failure modes included spawning 50 subagents for simple queries, scouring the web endlessly for nonexistent sources, and distracting each other with excessive updates [[sources/pdf-f478e5f11837]].
- Subagents plan with extended thinking and then use interleaved thinking after tool results to evaluate quality, identify gaps, and refine their next query [[sources/pdf-f478e5f11837]].

## Sources

- [[sources/pdf-f478e5f11837]]

## Related

- [[concepts/multi-agent-system]]
- [[concepts/orchestrator-worker-pattern]]
- [[concepts/extended-thinking]]
- [[concepts/parallel-tool-calling]]
