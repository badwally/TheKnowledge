---
schema_version: 1
type: concept
slug: chain-of-thought-prompting
canonical_name: Chain-of-Thought Prompting and Reasoning Models
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Chain-of-Thought Prompting and Reasoning Models

## Summary

A family of inference-time techniques — explicit chain-of-thought (CoT) prompts and reasoning-tuned models such as GPT-o1 — that improve LLM performance by encouraging step-by-step reasoning; the NoLiMa study shows these techniques help on latent-association tasks but cannot fully overcome long-context degradation beyond ~16K tokens [[sources/pdf-ali-modarressi-2025-nolima-long-context]].

## Key claims

- Chain-of-Thought prompting and reasoning-based models such as GPT-o1 (OpenAI et al., 2024) improve performance by encouraging step-by-step reasoning [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- However, these techniques fail to fully mitigate the long-context challenge surfaced by NoLiMa, particularly in contexts exceeding 16K tokens [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- The ceiling on CoT and reasoning-model effectiveness in long context is consistent with the NoLiMa finding that long contexts overwhelm the attention mechanism when surface-level cues are absent [[sources/pdf-ali-modarressi-2025-nolima-long-context]].

## Sources

- [[sources/pdf-ali-modarressi-2025-nolima-long-context]]

## Related

- [[concepts/long-context-llm-evaluation]]
- [[concepts/latent-associative-reasoning]]
- [[concepts/nolima-benchmark]]
