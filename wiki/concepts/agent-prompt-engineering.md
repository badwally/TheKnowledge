---
type: concept
slug: agent-prompt-engineering
canonical_name: Prompt Engineering for LLM Agents
domains:
  - ai-and-agents
---

# Prompt Engineering for LLM Agents

## Summary

The discipline of shaping LLM agent behavior through prompts, treated by Anthropic as the primary lever for controlling multi-agent coordination complexity; their lessons emphasize building accurate mental models of the agent, teaching the orchestrator to delegate clearly, scaling effort to query complexity, careful tool design, agent self-improvement, broad-then-narrow search strategy, and explicit guardrails over rigid rules [[sources/pdf-f478e5f11837]].

## Key claims

- Multi-agent systems have key differences from single-agent systems, including a rapid growth in coordination complexity; since each agent is steered by a prompt, prompt engineering was Anthropic's primary lever for improving agent behavior [[sources/pdf-f478e5f11837]].
- "Think like your agents": to iterate on prompts, you must understand their effects, so Anthropic built simulations using the exact prompts and tools from their system and watched agents work step-by-step, which immediately revealed failure modes such as continuing past sufficient results, using overly verbose queries, and selecting incorrect tools [[sources/pdf-f478e5f11837]].
- "Teach the orchestrator how to delegate": each subagent needs an objective, an output format, guidance on tools and sources, and clear task boundaries — without these, agents duplicate work, leave gaps, or misinterpret tasks [[sources/pdf-f478e5f11837]].
- "Scale effort to query complexity": Anthropic embedded scaling rules in prompts so simple fact-finding uses one agent with 3–10 tool calls, comparisons use 2–4 subagents with 10–15 calls each, and complex research uses more than 10 subagents with clearly divided responsibilities [[sources/pdf-f478e5f11837]].
- "Let agents improve themselves": Claude 4 models can be excellent prompt engineers — given a prompt and a failure mode, they can diagnose why an agent is failing and suggest improvements [[sources/pdf-f478e5f11837]].
- "Start wide, then narrow down": agents often default to overly long, specific queries that return few results, so Anthropic prompts agents to start with short, broad queries, evaluate what's available, then progressively narrow focus, mirroring expert human research [[sources/pdf-f478e5f11837]].
- Anthropic's prompting strategy focuses on instilling good heuristics rather than rigid rules — strategies like decomposing difficult questions, evaluating source quality, adjusting search approaches based on new information, and recognizing when to focus on depth vs. breadth [[sources/pdf-f478e5f11837]].
- Anthropic also proactively mitigates unintended side effects with explicit guardrails to prevent agents from spiraling out of control, alongside a fast iteration loop with observability and test cases [[sources/pdf-f478e5f11837]].

## Sources

- [[sources/pdf-f478e5f11837]]

## Related

- [[concepts/multi-agent-system]]
- [[concepts/extended-thinking]]
- [[concepts/tool-design-for-agents]]
- [[concepts/subagent]]
