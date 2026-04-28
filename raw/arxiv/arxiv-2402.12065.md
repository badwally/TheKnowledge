---
id: arxiv-2402.12065
type: arxiv
title: 'WKVQuant: Quantizing Weight and Key/Value Cache for Large Language Models
  Gains More'
url: http://arxiv.org/abs/2402.12065v2
authors:
- Yuxuan Yue
- Zhihang Yuan
- Haojie Duanmu
- Sifan Zhou
- Jianlong Wu
- Liqiang Nie
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:2a4e4725a6e404e0cd0697745be391bdb653760a6946634d817a5b7454f0a7c0
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2402.12065.md
  legacy_slug: arxiv_2402.12065
published_at: '2024-02-19'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# WKVQuant: Quantizing Weight and Key/Value Cache for Large Language Models Gains More

**Authors:** Yuxuan Yue, Zhihang Yuan, Haojie Duanmu, Sifan Zhou, Jianlong Wu, Liqiang Nie  
**Published:** 2024-02-19T11:33:21Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2402.12065v2.pdf

## Abstract

Large Language Models (LLMs) face significant deployment challenges due to their substantial memory requirements and the computational demands of auto-regressive text generation process. This paper addresses these challenges by focusing on the quantization of LLMs, a technique that reduces memory consumption by converting model parameters and activations into low-bit integers. We critically analyze the existing quantization approaches, identifying their limitations in balancing the accuracy and efficiency of the quantized LLMs. To advance beyond these limitations, we propose WKVQuant, a PTQ framework especially designed for quantizing weights and the key/value (KV) cache of LLMs. Specifically, we incorporates past-only quantization to improve the computation of attention. Additionally, we introduce two-dimensional quantization strategy to handle the distribution of KV cache, along with a cross-block reconstruction regularization for parameter optimization. Experiments show that WKVQ...

## Relevance

**Score:** 3/5  
WKVQuant proposes joint quantization of weights and KV cache for LLMs, reducing memory footprint and inference latency — both critical constraints for edge deployment. Introduces past-only quantization and 2D quantization strategy for KV cache distributions with experimental results.
