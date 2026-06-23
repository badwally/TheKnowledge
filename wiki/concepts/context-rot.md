---
schema_version: 1
type: concept
slug: context-rot
canonical_name: Context Rot
domains:
- ai-and-agents
created_at: '2026-06-23T16:16:03Z'
last_updated: '2026-06-23T16:16:03Z'
---

# Context Rot

## Summary

A phenomenon named by Hong et al. (2025) and invoked by Zhang, Kraska, and Khattab (2026) in which frontier reasoning models, even within their advertised context limits, exhibit steep quality degradation as prompts get longer [[sources/pdf-5c2f94fd33cd]].

## Key claims

- Frontier reasoning models have limited context windows and, even within their limits, tend to exhibit context rot — a phenomenon where quality degrades steeply as prompts get longer [[sources/pdf-5c2f94fd33cd]].
- The phenomenon is illustrated by GPT-5 performance degrading significantly as a function of both input length and task complexity across S-NIAH, OOLONG, and OOLONG-Pairs benchmarks [[sources/pdf-5c2f94fd33cd]].
- Context rot is increasingly urgent as LLMs are widely adopted for long-horizon tasks in which they must routinely process tens if not hundreds of millions of tokens [[sources/pdf-5c2f94fd33cd]].
- The effective context window of an LLM cannot be understood independently of the specific task — more complex problems exhibit degradation at even shorter lengths than simpler ones [[sources/pdf-5c2f94fd33cd]].
- GPT-5 scales effectively on the S-NIAH task, where the needle size is constant despite longer prompts, but shows faster degradation at increasingly shorter context lengths on the linear-complexity OOLONG and quadratic-complexity OOLONG-Pairs [[sources/pdf-5c2f94fd33cd]].

## Sources

- [[sources/pdf-5c2f94fd33cd]]

## Related

- [[concepts/recursive-language-model]]
- [[concepts/long-context-llm-evaluation]]
- [[concepts/context-compaction]]
