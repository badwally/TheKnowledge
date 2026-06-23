---
schema_version: 1
type: concept
slug: context-compaction
canonical_name: Context Compaction
domains:
- ai-and-agents
created_at: '2026-06-23T16:16:04Z'
last_updated: '2026-06-23T16:16:04Z'
---

# Context Compaction

## Summary

The most popular general inference-time approach for handling long contexts, in which context from user requests or agent trajectories is repeatedly summarized once it exceeds a length threshold; Zhang, Kraska, and Khattab (2026) critique compaction as rarely expressive enough for tasks that require dense access throughout the prompt [[sources/pdf-5c2f94fd33cd]].

## Key claims

- Context condensation or compaction is described by the RLM authors as the most popular general approach for dealing with long context, citing Khattab et al. (2021), Smith (2025), OpenAI (2025b), and Wu et al. (2025) [[sources/pdf-5c2f94fd33cd]].
- In compaction, context from user requests or agent trajectories is repeatedly summarized once it exceeds a length threshold [[sources/pdf-5c2f94fd33cd]].
- The RLM authors argue compaction is rarely expressive enough for tasks that require dense access throughout the prompt, since it presumes that some details that appear early in the prompt can safely be forgotten to make room for new content [[sources/pdf-5c2f94fd33cd]].
- A summary-agent baseline in the RLM evaluation iteratively accumulates documents and summarizes when the model context is full; for single documents exceeding the model window, the agent chunks them and applies the same strategy recursively [[sources/pdf-5c2f94fd33cd]].
- The Zhang et al. evaluation finds that summary-agent compaction is dominated by RLM scaffolds across S-NIAH, OOLONG, OOLONG-Pairs, BrowseComp-Plus, and LongBench-v2 CodeQA benchmarks [[sources/pdf-5c2f94fd33cd]].

## Sources

- [[sources/pdf-5c2f94fd33cd]]

## Related

- [[concepts/recursive-language-model]]
- [[concepts/context-rot]]
- [[concepts/long-context-llm-evaluation]]
