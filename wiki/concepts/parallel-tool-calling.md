---
type: concept
slug: parallel-tool-calling
canonical_name: Parallel Tool Calling
domains:
  - ai-and-agents
---

# Parallel Tool Calling

## Summary

The technique of having an LLM agent invoke multiple tool calls concurrently rather than sequentially, applied in Anthropic's Claude Research feature at two levels — the lead agent spawning subagents in parallel and individual subagents issuing several tool calls in parallel — yielding up to a 90% reduction in research time on complex queries [[sources/pdf-f478e5f11837]].

## Key claims

- Complex research tasks naturally involve exploring many sources, and Anthropic's early agents executed sequential searches that were painfully slow [[sources/pdf-f478e5f11837]].
- For speed, Anthropic introduced two kinds of parallelization: (1) the lead agent spins up 3–5 subagents in parallel rather than serially, and (2) the subagents use 3+ tools in parallel [[sources/pdf-f478e5f11837]].
- These changes cut research time by up to 90% for complex queries, allowing the Research feature to do more work in minutes instead of hours while covering more information than other systems [[sources/pdf-f478e5f11837]].
- Anthropic frames parallel tool calling as a transformation of speed and performance — one of the principles they identified as load-bearing for production multi-agent systems [[sources/pdf-f478e5f11837]].

## Sources

- [[sources/pdf-f478e5f11837]]

## Related

- [[concepts/multi-agent-system]]
- [[concepts/subagent]]
- [[concepts/orchestrator-worker-pattern]]
