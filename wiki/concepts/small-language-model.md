---
schema_version: 1
type: concept
slug: small-language-model
canonical_name: Small Language Model
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Small Language Model

## Summary

A small language model (SLM) is a language model that fits onto a common consumer electronics device and performs inference with latency low enough to be practical when serving the agentic requests of one user; the Belcak et al. (NVIDIA Research, 2025) position paper argues that SLMs are sufficiently powerful, inherently more operationally suitable, and necessarily more economical than LLMs for the vast majority of language-model invocations in agentic systems [[sources/pdf-peter-belcak-2025-small-language-models]].

## Key claims

- Working definition (Belcak et al., 2025): an SLM is a language model that can fit onto a common consumer electronic device and perform inference with latency sufficiently low to be practical when serving the agentic requests of one user; an LLM is any LM that is not an SLM [[sources/pdf-peter-belcak-2025-small-language-models]].
- As of 2025, the authors note they would be comfortable considering most models below 10 billion parameters in size to be SLMs [[sources/pdf-peter-belcak-2025-small-language-models]].
- Capability claim (V1/A1): well-designed SLMs can meet or exceed task performance previously attributed only to much larger models, with the LM scaling curve becoming increasingly steep so that newer SLMs approach the capabilities of previous-generation LLMs [[sources/pdf-peter-belcak-2025-small-language-models]].
- Examples cited as evidence: Phi-2 (2.7B) reaches commonsense-reasoning and code-generation scores on par with 30B models while running 15× faster; Phi-3-small (7B) matches up to 70B contemporaries in language understanding and commonsense reasoning [[sources/pdf-peter-belcak-2025-small-language-models]].
- Toolformer (6.7B) outperforms GPT-3 (175B) via API use, and 1–3B models have rivaled 30B+ LLMs on math problems via structured reasoning, illustrating that capability — not parameter count — is the binding constraint [[sources/pdf-peter-belcak-2025-small-language-models]].
- Economic claim (V3/A2): serving a 7B SLM is 10–30× cheaper than a 70–175B LLM in latency, energy consumption, and FLOPs, enabling real-time agentic responses at scale [[sources/pdf-peter-belcak-2025-small-language-models]].
- Fine-tuning agility: parameter-efficient (LoRA, DoRA), low-resource, and full-parameter finetuning for SLMs require only a few GPU-hours, allowing behaviors to be added, fixed, or specialized overnight rather than over weeks [[sources/pdf-peter-belcak-2025-small-language-models]].
- Parameter-utilization observation: many embeddings passing through LLMs are very sparse, engaging only a fraction of their parameters for any single input, and this sparsity behavior appears more subdued in SLMs — suggesting SLMs may be fundamentally more efficient because a larger proportion of their parameters contribute to the inference cost [[sources/pdf-peter-belcak-2025-small-language-models]].

## Sources

- [[sources/pdf-peter-belcak-2025-small-language-models]] — Small Language Models are the Future of Agentic AI

## Related

- [[concepts/heterogeneous-agentic-system]]
- [[concepts/llm-to-slm-conversion]]
- [[entities/nemotron-h]]
- [[entities/hymba]]
- [[entities/smollm2]]
- [[entities/xlam-2-8b]]
- [[entities/peter-belcak]]
