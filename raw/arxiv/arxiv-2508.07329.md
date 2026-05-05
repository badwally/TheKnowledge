---
id: arxiv-2508.07329
type: arxiv
title: Efficient Edge LLMs Deployment via HessianAware Quantization and CPU GPU Collaborative
url: http://arxiv.org/abs/2508.07329v1
authors:
- Tuo Zhang
- Ning Li
- Xin Yuan
- Wenchao Xu
- Quan Chen
- Song Guo
- Haijun Zhang
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:cbf01a3141c7aa3492c2bac5439e60590cbf7a91b7037deaa53c05bb8fed7484
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2508.07329.md
  legacy_slug: arxiv_2508.07329
published_at: '2025-08-10'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Efficient Edge LLMs Deployment via HessianAware Quantization and CPU GPU Collaborative

**Authors:** Tuo Zhang, Ning Li, Xin Yuan, Wenchao Xu, Quan Chen, Song Guo, Haijun Zhang  
**Published:** 2025-08-10T12:59:57Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2508.07329v1.pdf

## Abstract

With the breakthrough progress of large language models (LLMs) in natural language processing and multimodal tasks, efficiently deploying them on resource-constrained edge devices has become a critical challenge. The Mixture of Experts (MoE) architecture enhances model capacity through sparse activation, but faces two major difficulties in practical deployment: (1) The presence of numerous outliers in activation distributions leads to severe degradation in quantization accuracy for both activations and weights, significantly impairing inference performance; (2) Under limited memory, efficient offloading and collaborative inference of expert modules struggle to balance latency and throughput. To address these issues, this paper proposes an efficient MoE edge deployment scheme based on Hessian-Aware Quantization (HAQ) and CPU-GPU collaborative inference. First, by introducing smoothed Hessian matrix quantization, we achieve joint 8-bit quantization of activations and weights, which si...

## Relevance

**Score:** 4/5  
Proposes Hessian-Aware Quantization with CPU-GPU collaborative inference for MoE models on edge devices; addresses both quantization accuracy (joint 8-bit weight/activation) and memory-constrained expert offloading with latency measurements.
