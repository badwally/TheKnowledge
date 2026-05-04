---
type: concept
slug: heterogeneous-agentic-system
canonical_name: Heterogeneous Agentic System
domains:
  - ai-and-agents
---

# Heterogeneous Agentic System

## Summary

A heterogeneous agentic system is an agent that invokes multiple different language models — typically using small language models (SLMs) by default for scoped, repetitive subtasks and reaching for large language models (LLMs) selectively when general reasoning or open-domain dialogue is required; Belcak et al. (NVIDIA Research, 2025) argue this composition is the natural choice when general-purpose conversational abilities are essential and is already being incorporated into major software-development frameworks [[sources/pdf-peter-belcak-2025-small-language-models]].

## Key claims

- An agentic system is a piece of software with some agency built as a sum of components; not all language models in such a system are replaceable by SLMs, motivating composition over uniformity [[sources/pdf-peter-belcak-2025-small-language-models]].
- In cases where general reasoning or open-domain dialogue is essential, the paper advocates for heterogeneous agentic systems where SLMs are used by default and LLMs are invoked selectively and sparingly [[sources/pdf-peter-belcak-2025-small-language-models]].
- Modular composition combining the precision and efficiency of SLMs with the generality of LLMs enables the construction of agents that are both cost-effective and capable [[sources/pdf-peter-belcak-2025-small-language-models]].
- The approach of leveraging several models of varying sizes aligns with the real-world heterogeneity of agentic tasks and is being incorporated into major software-development frameworks [[sources/pdf-peter-belcak-2025-small-language-models]].
- A "Lego-like" composition — scaling out by adding small, specialized experts instead of scaling up monolithic models — yields systems that are cheaper, faster to debug, easier to deploy, and better aligned with the operational diversity of real-world agents [[sources/pdf-peter-belcak-2025-small-language-models]].
- When combined with tool calling, caching, and fine-grained routing, SLM-first heterogeneous architectures appear to offer the best path forward for cost-effective, modular, and sustainable agentic AI [[sources/pdf-peter-belcak-2025-small-language-models]].

## Sources

- [[sources/pdf-peter-belcak-2025-small-language-models]] — Small Language Models are the Future of Agentic AI

## Related

- [[concepts/small-language-model]]
- [[concepts/llm-to-slm-conversion]]
- [[entities/nvidia-research]]
- [[entities/peter-belcak]]
