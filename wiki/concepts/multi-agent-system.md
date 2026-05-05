---
type: concept
slug: multi-agent-system
canonical_name: Multi-Agent System (LLM)
domains:
  - ai-and-agents
---

# Multi-Agent System (LLM)

## Summary

A system in which multiple LLM agents — each autonomously using tools in a loop — work together on a task, with at least one agent coordinating the work of others; the architecture used by Anthropic's Claude Research feature, where parallel subagents explore different aspects of an open-ended query and return findings to a lead agent that compiles the answer [[sources/pdf-f478e5f11837]].

## Key claims

- A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together, and introduces new challenges in agent coordination, evaluation, and reliability [[sources/pdf-f478e5f11837]].
- Multi-agent systems excel especially for breadth-first queries that involve pursuing multiple independent directions simultaneously, by distributing work across agents with separate context windows to add capacity for parallel reasoning [[sources/pdf-f478e5f11837]].
- In Anthropic's BrowseComp analysis, three factors explained 95% of the performance variance: token usage alone explained 80% of the variance, with the number of tool calls and model choice as the remaining explanatory factors [[sources/pdf-f478e5f11837]].
- Multi-agent architectures effectively scale token usage for tasks that exceed the limits of single agents, and an Anthropic internal eval found a Claude Opus 4 lead with Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% [[sources/pdf-f478e5f11837]].
- Multi-agent systems use about 15× more tokens than chat interactions and about 4× more than single-agent loops, so they require tasks where the value justifies the increased cost [[sources/pdf-f478e5f11837]].
- Domains that require all agents to share the same context, or that involve many dependencies between agents, are not a good fit today; most coding tasks involve fewer truly parallelizable subtasks than research, and current LLM agents are not yet great at coordinating and delegating in real time [[sources/pdf-f478e5f11837]].
- Multi-agent systems excel at valuable tasks that involve heavy parallelization, information that exceeds single context windows, and interfacing with numerous complex tools [[sources/pdf-f478e5f11837]].

## Sources

- [[sources/pdf-f478e5f11837]]

## Related

- [[concepts/orchestrator-worker-pattern]]
- [[concepts/subagent]]
- [[concepts/parallel-tool-calling]]
- [[concepts/agentic-ai]]
- [[entities/anthropic]]
