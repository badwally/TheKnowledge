---
id: arxiv-2509.25689
type: arxiv
title: Collaborative Compression for Large-Scale MoE Deployment on Edge
url: http://arxiv.org/abs/2509.25689v1
authors:
- Yixiao Chen
- Yanyue Xie
- Ruining Yang
- Wei Jiang
- Wei Wang
- Yong He
- Yue Chen
- Pu Zhao
- Yanzhi Wang
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:8e454a7cdbfc43eb74186b8cb0adb55fa6fbcfc9daeeb46557c3e34d709c9dd1
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2509.25689.md
  legacy_slug: arxiv_2509.25689
published_at: '2025-09-30'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Collaborative Compression for Large-Scale MoE Deployment on Edge

**Authors:** Yixiao Chen, Yanyue Xie, Ruining Yang, Wei Jiang, Wei Wang, Yong He, Yue Chen, Pu Zhao, Yanzhi Wang  
**Published:** 2025-09-30T02:46:03Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2509.25689v1.pdf

## Abstract

The Mixture of Experts (MoE) architecture is an important method for scaling Large Language Models (LLMs). It increases model capacity while keeping computation cost low. However, the ultra-large MoE models still have hundreds of billions of parameters, requiring massive memory/storage and leading to difficulties for deployment on resource-constrained edge platforms. Pruning or quantization alone can hardly address the issue, because of the super-aggressive compression ratio with significantly degraded accuracy and output quality. To facilitate the deployment of ultra-large MoEs on edge platforms, we propose a collaborative compression framework by combining expert pruning, mixed-precision quantization, and activation optimization. It can effectively reduce the storage footprint of the ultra-large MoE DeepSeek-V3 from 1.3TB to 103GB, while preserving high output quality with better accuracy than traditional uniform low-bit quantization methods. To the best of our knowledge, we are t...

## Relevance

**Score:** 4/5  
Collaborative compression framework combining expert pruning, mixed-precision quantization, and activation optimization to reduce DeepSeek-V3 from 1.3TB to 103GB for edge platforms; first reported MoE edge deployment at this scale.
