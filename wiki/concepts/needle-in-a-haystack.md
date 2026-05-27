---
schema_version: 1
type: concept
slug: needle-in-a-haystack
canonical_name: Needle-in-a-Haystack (NIAH)
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Needle-in-a-Haystack (NIAH)

## Summary

Needle-in-a-Haystack is the most well-known and widely used long-context LLM benchmark family, in which a model must locate and retrieve a specific fact (the "needle") hidden within a long irrelevant context (the "haystack"); the Modarressi et al. 2025 NoLiMa paper documents both its variants and the structural reason it has saturated [[sources/pdf-ali-modarressi-2025-nolima-long-context]].

## Key claims

- NIAH tests a model's ability to search for and retrieve a specific fact (the needle) hidden within irrelevant information (the haystack) and is the most well-known and widely used long-context benchmark, originating with Mohtashami & Jaggi (2023) and Kamradt (2023) [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- The baseline NIAH task assesses surface-level retrieval capabilities; recent adaptations have increased complexity by introducing multiple needles, incorporating additional distractor material, and interconnecting facts to require in-context reasoning (fact-chaining) [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- NIAH-style and other long-context benchmarks (long-document QA, multi-document QA, long conversation understanding) share a common foundation: association recall — the ability to recall previously seen information [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- The attention mechanism underlying many LLMs is inherently adept at identifying and recalling associations present in the input, which is one reason NIAH variants tend to saturate quickly [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- Vanilla NIAH exhibits very high literal overlap between question and context (ROUGE precision R-1 0.905, R-2 0.789, R-L 0.855), so models can exploit existing literal matches between needle and haystack to simplify the task [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- Some NIAH-derived tasks add complexity to the point of being overly difficult even in short contexts: BABILong's counting task achieves only 28% accuracy with 0K of irrelevant context, and the Ancestral Tree Challenge (ATC) employs extensive fact-chaining that is overly complex even at <1K tokens [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- The NoLiMa paper argues that NIAH and its descendants either explicitly (synthetic / NIAH-based tasks) or implicitly (multi- or long-document QA) contain literal matches that confound long-context evaluation [[sources/pdf-ali-modarressi-2025-nolima-long-context]].

## Sources

- [[sources/pdf-ali-modarressi-2025-nolima-long-context]]

## Related

- [[concepts/nolima-benchmark]]
- [[concepts/long-context-llm-evaluation]]
- [[concepts/literal-matching-shortcut]]
