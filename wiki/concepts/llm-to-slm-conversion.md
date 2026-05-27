---
schema_version: 1
type: concept
slug: llm-to-slm-conversion
canonical_name: LLM-to-SLM Conversion
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# LLM-to-SLM Conversion

## Summary

LLM-to-SLM conversion refers to the migration of an existing agentic application from a generalist large language model invocation pattern to one in which scoped, repetitive subtasks are routed to specialized small language models; Belcak et al. (NVIDIA Research, 2025) outline a general conversion algorithm and frame it as a remedy for the now-legacy praxis of routing every agent request to a single generalist LLM endpoint [[sources/pdf-peter-belcak-2025-small-language-models]].

## Key claims

- The paper recognizes the dominance of the standard "single generalist LLM behind an API endpoint" operational model and verbally challenges the custom that agents' simpler, comparatively narrow requests are handled by singleton LLM choices [[sources/pdf-peter-belcak-2025-small-language-models]].
- The current LLM-centric operational model forms the foundation of substantial capital investment in hosting cloud infrastructure — estimated at USD 57bn — and is anticipated to deliver returns comparable to traditional software within 3–4 years [[sources/pdf-peter-belcak-2025-small-language-models]].
- The paper attributes the present LLM-dominant state to business commitment and now-legacy praxis rather than to functional necessity, and proposes a conversion algorithm as the remedy [[sources/pdf-peter-belcak-2025-small-language-models]].
- The paper attaches case studies estimating the potential extent of LLM-to-SLM replacement in selected popular open-source agents to concretize its stance [[sources/pdf-peter-belcak-2025-small-language-models]].
- Insisting on LLMs for all agentic subtasks is described as a misallocation of computational resources that is economically inefficient and environmentally unsustainable at scale; conversion is framed as both a technical refinement and, to many, a Humean moral ought [[sources/pdf-peter-belcak-2025-small-language-models]].

## Sources

- [[sources/pdf-peter-belcak-2025-small-language-models]] — Small Language Models are the Future of Agentic AI

## Related

- [[concepts/small-language-model]]
- [[concepts/heterogeneous-agentic-system]]
- [[entities/nvidia-research]]
- [[entities/peter-belcak]]
