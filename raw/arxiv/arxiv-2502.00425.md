---
id: arxiv-2502.00425
type: arxiv
title: 'MQuant: Unleashing the Inference Potential of Multimodal Large Language Models
  via Full Static Quantization'
url: http://arxiv.org/abs/2502.00425v2
authors:
- JiangYong Yu
- Sifan Zhou
- Dawei Yang
- Shuo Wang
- Shuoyu Li
- Xing Hu
- Chen Xu
- Zukang Xu
- Changyong Shu
- Zhihang Yuan
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:3e7eabfe66f46cb51de484853451b09f31be17bbd6a687abfbea8570397e817b
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2502.00425.md
  legacy_slug: arxiv_2502.00425
published_at: '2025-02-01'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# MQuant: Unleashing the Inference Potential of Multimodal Large Language Models via Full Static Quantization

**Authors:** JiangYong Yu, Sifan Zhou, Dawei Yang, Shuo Wang, Shuoyu Li, Xing Hu, Chen Xu, Zukang Xu, Changyong Shu, Zhihang Yuan  
**Published:** 2025-02-01T13:08:02Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2502.00425v2.pdf

## Abstract

Multimodal large language models (MLLMs) have garnered widespread attention due to their ability to understand multimodal input. However, their large parameter sizes and substantial computational demands severely hinder their practical deployment and application.While quantization is an effective way to reduce model size and inference latency, its application to MLLMs remains underexplored. In this paper, we propose MQuant, a post-training quantization (PTQ) framework designed to tackle the unique challenges of multimodal large language models (MLLMs). Conventional quantization often struggles with MLLMs because of (a) high inference latency from large visual token counts, (b) distributional disparities between visual and textual tokens, and (c) extreme outliers introduced by Hadamard-based transformations. To address these issues, MQuant introduces: Modality-Specific Static Quantization (MSQ), assigning distinct static scales for visual vs. textual tokens; Attention-Invariant Flexi...

## Relevance

**Score:** 3/5  
Introduces MQuant, a post-training quantization framework for multimodal LLMs addressing high inference latency and token distribution challenges. Quantization for reduced inference latency is a core edge optimization technique, and the work presents novel modality-specific static quantization with experimental results across five MLLMs.
