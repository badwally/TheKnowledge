---
schema_version: 1
type: concept
slug: tool-design-for-agents
canonical_name: Tool Design for LLM Agents
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Tool Design for LLM Agents

## Summary

The practice of designing the tools an LLM agent invokes — their selection, descriptions, and ergonomics — treated by Anthropic as on par with human-computer interface design; bad tool descriptions can send agents down completely wrong paths, while a tool-testing agent that iteratively rewrites tool descriptions cut downstream task completion time by 40% [[sources/pdf-f478e5f11837]].

## Key claims

- Agent-tool interfaces are as critical as human-computer interfaces, and using the right tool is often strictly necessary — for instance, an agent searching the web for context that only exists in Slack is doomed from the start [[sources/pdf-f478e5f11837]].
- The proliferation of MCP servers exposes agents to unseen tools with descriptions of wildly varying quality, which compounds the cost of poor tool design [[sources/pdf-f478e5f11837]].
- Anthropic gives agents explicit heuristics: examine all available tools first, match tool usage to user intent, search the web for broad external exploration, and prefer specialized tools over generic ones [[sources/pdf-f478e5f11837]].
- Bad tool descriptions can send agents down completely wrong paths, so each tool needs a distinct purpose and a clear description [[sources/pdf-f478e5f11837]].
- Anthropic created a tool-testing agent that, when given a flawed MCP tool, attempts to use the tool and then rewrites the tool description to avoid failures; by testing the tool dozens of times, the agent finds key nuances and bugs [[sources/pdf-f478e5f11837]].
- This process for improving tool ergonomics resulted in a 40% decrease in task completion time for future agents using the new description, because they were able to avoid most mistakes [[sources/pdf-f478e5f11837]].

## Sources

- [[sources/pdf-f478e5f11837]]

## Related

- [[concepts/agent-prompt-engineering]]
- [[concepts/multi-agent-system]]
- [[concepts/subagent]]
