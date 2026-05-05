---
id: arxiv-2511.13023
type: arxiv
title: SLMQuant:Benchmarking Small Language Model Quantization for Practical Deployment
url: http://arxiv.org/abs/2511.13023v1
authors:
- Jiacheng Wang
- Yejun Zeng
- Jinyang Guo
- Yuqing Ma
- Aishan Liu
- Xianglong Liu
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:d62fb0562c6a98f17a7785c4e61581e982be02f6749c90dadf790b5867cf1f34
domains:
- edge-ai-agentic
nlm_corpus_ids:
- e7f21255-0787-4091-ab69-5f79669e1501
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2511.13023.md
  legacy_slug: arxiv_2511.13023
published_at: '2025-11-17'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# SLMQuant:Benchmarking Small Language Model Quantization for Practical Deployment

**Authors:** Jiacheng Wang, Yejun Zeng, Jinyang Guo, Yuqing Ma, Aishan Liu, Xianglong Liu  
**Published:** 2025-11-17T06:20:33Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2511.13023v1.pdf

## Abstract

Despite the growing interest in Small Language Models (SLMs) as resource-efficient alternatives to Large Language Models (LLMs), their deployment on edge devices remains challenging due to unresolved efficiency gaps in model compression. While quantization has proven effective for LLMs, its applicability to SLMs is significantly underexplored, with critical questions about differing quantization bottlenecks and efficiency profiles. This paper introduces SLMQuant, the first systematic benchmark for evaluating LLM compression techniques when applied to SLMs. Through comprehensive multi-track evaluations across diverse architectures and tasks, we analyze how state-of-the-art quantization methods perform on SLMs. Our findings reveal fundamental disparities between SLMs and LLMs in quantization sensitivity, demonstrating that direct transfer of LLM-optimized techniques leads to suboptimal results due to SLMs' unique architectural characteristics and training dynamics. We identify key fac...

## Relevance

**Score:** 4/5  
SLMQuant is the first systematic benchmark of LLM quantization techniques applied to small language models for edge deployment; reveals fundamental SLM-vs-LLM quantization sensitivity differences with practical implications for edge model selection.
