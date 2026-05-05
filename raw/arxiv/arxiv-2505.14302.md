---
id: arxiv-2505.14302
type: arxiv
title: Scaling Law for Quantization-Aware Training
url: http://arxiv.org/abs/2505.14302v1
authors:
- Mengzhao Chen
- Chaoyi Zhang
- Jing Liu
- Yutao Zeng
- Zeyue Xue
- Zhiheng Liu
- Yunshui Li
- Jin Ma
- Jie Huang
- Xun Zhou
- Ping Luo
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:d1a515ddab31e2ef086423bf4d850ed6daa761aeca808b935309facc9bfa02ca
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2505.14302.md
  legacy_slug: arxiv_2505.14302
published_at: '2025-05-20'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Scaling Law for Quantization-Aware Training

**Authors:** Mengzhao Chen, Chaoyi Zhang, Jing Liu, Yutao Zeng, Zeyue Xue, Zhiheng Liu, Yunshui Li, Jin Ma, Jie Huang, Xun Zhou, Ping Luo  
**Published:** 2025-05-20T12:54:43Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2505.14302v1.pdf

## Abstract

Large language models (LLMs) demand substantial computational and memory resources, creating deployment challenges. Quantization-aware training (QAT) addresses these challenges by reducing model precision while maintaining performance. However, the scaling behavior of QAT, especially at 4-bit precision (W4A4), is not well understood. Existing QAT scaling laws often ignore key factors such as the number of training tokens and quantization granularity, which limits their applicability. This paper proposes a unified scaling law for QAT that models quantization error as a function of model size, training data volume, and quantization group size. Through 268 QAT experiments, we show that quantization error decreases as model size increases, but rises with more training tokens and coarser quantization granularity. To identify the sources of W4A4 quantization error, we decompose it into weight and activation components. Both components follow the overall trend of W4A4 quantization error, b...

## Relevance

**Score:** 3/5  
Unified QAT scaling law across 268 experiments modeling quantization error as a function of model size, training tokens, and group size at W4A4; directly informs deployment decisions for edge-quantized LLMs.
