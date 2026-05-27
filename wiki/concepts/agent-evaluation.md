---
schema_version: 1
type: concept
slug: agent-evaluation
canonical_name: Multi-Agent System Evaluation
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Multi-Agent System Evaluation

## Summary

The practice of judging whether agents reach correct outcomes via reasonable processes, given that agents starting from identical inputs may take different valid paths; Anthropic recommends starting with small samples (~20 queries) early in development when effect sizes are large, and using LLM-as-judge for free-form outputs [[sources/pdf-f478e5f11837]].

## Key claims

- Traditional evaluations often assume the AI follows the same steps each time — given input X, follow path Y to produce output Z — but multi-agent systems do not work this way, since different agents may take completely different valid paths to reach a goal [[sources/pdf-f478e5f11837]].
- Because we usually do not know what the right steps are, evaluation cannot just check whether agents followed prescribed steps; instead it must judge whether agents achieved the right outcomes while also following a reasonable process [[sources/pdf-f478e5f11837]].
- In early agent development, changes tend to have dramatic impacts because there is abundant low-hanging fruit — a prompt tweak might boost success rates from 30% to 80%, and effect sizes this large can be detected with just a few test cases [[sources/pdf-f478e5f11837]].
- Anthropic started with about 20 queries representing real usage patterns and found that testing these queries often allowed them to clearly see the impact of changes [[sources/pdf-f478e5f11837]].
- Anthropic argues against delaying eval creation until large evals with hundreds of test cases are available — small-scale testing right away with a few examples is preferable to waiting [[sources/pdf-f478e5f11837]].
- LLM-as-judge evaluation is used to grade free-form outputs against rubric criteria and scales when done well [[sources/pdf-f478e5f11837]].

## Sources

- [[sources/pdf-f478e5f11837]]

## Related

- [[concepts/llm-as-judge-evaluation]]
- [[concepts/multi-agent-system]]
