---
schema_version: 1
type: concept
slug: long-context-llm-evaluation
canonical_name: Long-Context LLM Evaluation
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-06-23T16:16:06Z'
---

# Long-Context LLM Evaluation

## Summary

The set of methods for measuring whether large language models that advertise context windows of 128K–1M tokens can actually use that capacity; the Modarressi et al. 2025 NoLiMa study finds that performance of 12 leading models — including GPT-4o, Gemini 1.5 Pro, and Llama 3.3 70B — degrades sharply as context grows once literal-match shortcuts are removed [[sources/pdf-ali-modarressi-2025-nolima-long-context]].

## Key claims

- Recent LLMs support contexts ranging from 128K to 1M tokens, unlocking applications such as long- or multi-document QA, summarization, and many-shot in-context learning [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- Several benchmarks have been developed to evaluate these models' effectiveness in handling long contexts, including NIAH and its extensions, multi-document and long-document QA, and long-conversation understanding [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- The NoLiMa study evaluates 12 popular LLMs that claim to support contexts of at least 128K tokens, including GPT-4o, Gemini 1.5 Pro, and Llama 3.3 70B [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- While these models perform well in short contexts (<1K), performance degrades significantly as context length increases [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- At 32K tokens, 10 of the 12 evaluated models drop below 50% of their strong short-length baselines; even GPT-4o, one of the top-performing exceptions, falls from an almost-perfect baseline of 99.3% to 69.7% [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- Considerable performance drops appear even at 2K–8K tokens, well within nominal context limits [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- The authors attribute these declines to the increased difficulty the attention mechanism faces in longer contexts when literal matches are absent, making it harder to retrieve relevant information [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- The NoLiMa aligned-depth analysis shows that as latent reasoning complexity grows, performance depends more on context length than on needle position — without surface-level cues, longer contexts overwhelm the attention mechanism [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- Zhang, Kraska, and Khattab (2026) extend this evaluation literature with four tasks of varying complexity scaling — S-NIAH, OOLONG, OOLONG-Pairs, and BrowseComp-Plus — designed to distinguish needle-extraction tasks where information complexity stays constant from tasks where the answer depends explicitly on almost every chunk of the input [[sources/pdf-5c2f94fd33cd]].
- The Zhang et al. evaluation argues that the effective context window of an LLM cannot be understood independently of the specific task: more complex problems exhibit degradation at even shorter lengths than simpler ones [[sources/pdf-5c2f94fd33cd]].
- They report that frontier models can now reliably solve constant-complexity NIAH tasks in the 1M+ token setting on RULER but struggle at far shorter lengths on OOLONG, where the answer depends explicitly on almost every line in the prompt [[sources/pdf-5c2f94fd33cd]].
- A Recursive Language Model scaffold over GPT-5 maintains strong performance on S-NIAH, OOLONG, and OOLONG-Pairs even as inputs scale from 8K to 1M tokens, while direct GPT-5 calls degrade significantly with both input length and task complexity [[sources/pdf-5c2f94fd33cd]].
- Inputs beyond GPT-5's 272K-token context window cannot be processed directly by the base model but are handled effectively by the RLM scaffold over the same model [[sources/pdf-5c2f94fd33cd]].

## Sources

- [[sources/pdf-ali-modarressi-2025-nolima-long-context]]
- [[sources/pdf-5c2f94fd33cd]]

## Related

- [[concepts/nolima-benchmark]]
- [[concepts/needle-in-a-haystack]]
- [[concepts/literal-matching-shortcut]]
- [[concepts/latent-associative-reasoning]]
- [[concepts/recursive-language-model]]
- [[concepts/context-rot]]
- [[concepts/context-compaction]]
