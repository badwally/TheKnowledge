---
type: concept
slug: extended-thinking
canonical_name: Extended Thinking and Interleaved Thinking
domains:
  - ai-and-agents
---

# Extended Thinking and Interleaved Thinking

## Summary

Modes of Claude in which the model emits additional tokens in a visible thinking process, used as a controllable scratchpad — extended thinking up front for planning, and interleaved thinking after tool results to evaluate quality and refine the next action; Anthropic reports that these modes improved instruction-following, reasoning, and efficiency in their multi-agent Research feature [[sources/pdf-f478e5f11837]].

## Key claims

- Extended thinking mode leads Claude to output additional tokens in a visible thinking process, which can serve as a controllable scratchpad [[sources/pdf-f478e5f11837]].
- The lead agent in Anthropic's Research feature uses extended thinking to plan its approach — assessing which tools fit the task, determining query complexity and subagent count, and defining each subagent's role [[sources/pdf-f478e5f11837]].
- Anthropic's testing showed that extended thinking improved instruction-following, reasoning, and efficiency [[sources/pdf-f478e5f11837]].
- Subagents also plan with extended thinking, then use interleaved thinking after tool results to evaluate quality, identify gaps, and refine their next query, which makes subagents more effective at adapting to any task [[sources/pdf-f478e5f11837]].

## Sources

- [[sources/pdf-f478e5f11837]]

## Related

- [[concepts/subagent]]
- [[concepts/agent-prompt-engineering]]
- [[concepts/multi-agent-system]]
