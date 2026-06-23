---
schema_version: 1
type: entity
slug: rlm-qwen3-8b
canonical_name: RLM-Qwen3-8B
entity_kind: model
domains:
- ai-and-agents
created_at: '2026-06-23T16:16:06Z'
last_updated: '2026-06-23T16:16:06Z'
---

# RLM-Qwen3-8B

## Summary

The first natively recursive language model, post-trained by Zhang, Kraska, and Khattab (2026) from Qwen3-8B (Yang et al., 2025); outperforms the underlying Qwen3-8B model by a median of 28.3% across four long-context evaluation tasks and approaches the quality of vanilla GPT-5 on three of them [[sources/pdf-5c2f94fd33cd]].

## Key facts

- Identified by the authors as the first natively recursive language model, post-trained from Qwen3-8B [[sources/pdf-5c2f94fd33cd]].
- Outperforms the underlying Qwen3-8B model by a median of 28.3% across the four evaluation tasks [[sources/pdf-5c2f94fd33cd]].
- Approaches the quality of vanilla GPT-5 on three of the four long-context tasks [[sources/pdf-5c2f94fd33cd]].
- Trained using a simple general-purpose recipe that uses only 1,000 samples from unrelated domains [[sources/pdf-5c2f94fd33cd]].
- A small open model like Qwen3-8B struggles to solve long-context tasks even inside an RLM scaffold without this targeted training, motivating the post-training intervention [[sources/pdf-5c2f94fd33cd]].

## Sources

- [[sources/pdf-5c2f94fd33cd]]

## Related

- [[concepts/recursive-language-model]]
- [[entities/alex-l-zhang]]
- [[entities/mit-csail]]
