---
id: arxiv-2512.03383
type: arxiv
title: 'UniQL: Unified Quantization and Low-rank Compression for Adaptive Edge LLMs'
url: http://arxiv.org/abs/2512.03383v3
authors:
- Hung-Yueh Chiang
- Chi-Chih Chang
- Yu-Chen Lu
- Chien-Yu Lin
- Kai-Chiang Wu
- Mohamed S. Abdelfattah
- Diana Marculescu
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:7e56d49a497940cc2e810e1e6e9e7024746f3ced2ec4d2256e8cd8be6d1f0d8d
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2512.03383.md
  legacy_slug: arxiv_2512.03383
published_at: '2025-12-03'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# UniQL: Unified Quantization and Low-rank Compression for Adaptive Edge LLMs

**Authors:** Hung-Yueh Chiang, Chi-Chih Chang, Yu-Chen Lu, Chien-Yu Lin, Kai-Chiang Wu, Mohamed S. Abdelfattah, Diana Marculescu  
**Published:** 2025-12-03T02:33:39Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2512.03383v3.pdf

## Abstract

Deploying large language models (LLMs) on mobile platforms faces significant challenges due to the limited memory and shared computational resources of the device. Resource availability may be an issue as it is directly impacted by the current device workload, adding to the uncertainty of model deployment. We introduce UniQL, a unified post-training quantization and low-rank compression framework with on-device configurable pruning rates for edge LLMs. UniQL is a general framework that integrates quantization and low-rank compression for Transformers, State Space Models (SSMs), and hybrid models to support diverse edge applications. In our proposed joint framework, we introduce an efficient structured weight-sorting method that speeds up computation by 20x, quantization-aware singular value decomposition (SVD) to minimize quantization errors, state-aware weight sorting for SSMs, and a fused rotary positional embedding (RoPE) kernel for pruned models. Our framework performs weight-so...

## Relevance

**Score:** 4/5  
UniQL unifies quantization and low-rank compression for Transformers, SSMs, and hybrid models with on-device configurable pruning rates; introduces QA-SVD and fused RoPE kernels specifically for mobile/edge LLM deployment.
