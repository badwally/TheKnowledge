---
id: arxiv-2508.03332
type: arxiv
title: Exploring Layer-wise Information Effectiveness for Post-Training Quantization
  in Small Language Models
url: http://arxiv.org/abs/2508.03332v2
authors:
- He Xiao
- Qingyao Yang
- Dirui Xie
- Wendong Xu
- Zunhai Su
- Runming yang
- Wenyong Zhou
- Haobo Liu
- Zhengwu Liu
- Ngai Wong
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:e6c2941a76f917e7706d58a604d4a82ee3839b2c22bc3f136f056f5154ce0817
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2508.03332.md
  legacy_slug: arxiv_2508.03332
published_at: '2025-08-05'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Exploring Layer-wise Information Effectiveness for Post-Training Quantization in Small Language Models

**Authors:** He Xiao, Qingyao Yang, Dirui Xie, Wendong Xu, Zunhai Su, Runming yang, Wenyong Zhou, Haobo Liu, Zhengwu Liu, Ngai Wong  
**Published:** 2025-08-05T11:17:04Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2508.03332v2.pdf

## Abstract

Large language models with billions of parameters are often over-provisioned: many layers contribute little unique information yet dominate the memory and energy footprint during inference. We present LieQ Layer-wise information effectiveness Quantization, a hardware-native, metric-driven post-training quantization framework that addresses the critical challenge of maintaining accuracy in sub-8B models, model parameters less than 8B, under extreme low-bit compression. LieQ keeps uniform bit-width within each layer while mixing precision across layers, preserving standard multiplication kernels and avoiding irregular memory access, codebooks, or irregular formats at inference time. Our method uncovers a strong correlation between layer-wise functional saliency and representational compactness, revealing that layers with higher training-induced energy concentration are functionally irreplaceable. Leveraging this insight, we propose a purely geometry-driven sensitivity proxy that enabl...

## Relevance

**Score:** 3/5  
LieQ is a hardware-native mixed-precision PTQ framework for sub-8B models using geometry-driven sensitivity to assign per-layer precision; targets edge-relevant memory and energy footprint with standard multiplication kernels.
