---
type: concept
slug: nolima-benchmark
canonical_name: NoLiMa Benchmark
domains:
  - ai-and-agents
---

# NoLiMa Benchmark

## Summary

NoLiMa ("No Literal Matching") is a long-context LLM benchmark that extends the Needle-in-a-Haystack paradigm with a carefully designed needle set in which questions and needles share minimal lexical overlap, forcing models to rely on latent associative reasoning rather than surface-level keyword matching to retrieve the relevant fact [[sources/pdf-ali-modarressi-2025-nolima-long-context]].

## Key claims

- NoLiMa is introduced to address the observation that existing long-context benchmarks — both synthetic NIAH-based tasks and downstream multi-document or long-document QA — explicitly or implicitly contain literal matches between the question and the relevant context, which simplifies retrieval [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- A needle in NoLiMa is a single key piece of information placed within a long irrelevant text (a haystack of book snippets), and the model is tested on its ability to answer a question whose keywords are connected to the needle only through associative links such as real-world knowledge or commonsense facts [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- Each needle template pairs a unique character with specific information about them; the question keyword W_q (e.g., "Dresden") and the needle keyword W_n (e.g., "Semper Opera House") have no literal overlap, so the model must infer the latent association to retrieve the correct character [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- NoLiMa includes both default and inverted needle orderings and a two-hop variant (e.g., asking about the state of Saxony rather than Dresden) to escalate the difficulty of identifying the latent association between W_q and W_n [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- ROUGE precision scores between input document and question show NoLiMa exhibits dramatically less literal overlap than other long-context datasets — R-1 0.069, R-2 0.002, R-L 0.067, versus e.g. vanilla NIAH at R-1 0.905 and BABILong at R-1 0.553 [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- Three constraints govern the needle set: keywords must be simple enough that the association is clear without irrelevant context; character names are randomized from a diverse pool to mitigate tokenization artifacts and ethnic bias; and W_n must be uniquely associated with W_q, with preface phrases isolating needles from preceding context [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- A haystack-filtering pipeline removes both distractors with extreme literal or high semantic similarity to question keywords (using Contriever embeddings and dot-product similarity over the top-20 closest words, manually inspected) and any passage that could explicitly or inferentially supply a false answer [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- Conflicting-information removal uses Llama 3.3 70B prompted on text chunks with a four-shot template (two answer / two N/A examples) and is repeated until no further removals are needed; flagged examples are manually checked [[sources/pdf-ali-modarressi-2025-nolima-long-context]].
- The benchmark configuration uses 5 groups of needles, each with two fact-order variations (default and inverted), enabling clean ablations over needle position and fact direction [[sources/pdf-ali-modarressi-2025-nolima-long-context]].

## Sources

- [[sources/pdf-ali-modarressi-2025-nolima-long-context]]

## Related

- [[concepts/needle-in-a-haystack]]
- [[concepts/long-context-llm-evaluation]]
- [[concepts/latent-associative-reasoning]]
- [[concepts/literal-matching-shortcut]]
