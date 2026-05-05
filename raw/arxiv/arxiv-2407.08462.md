---
id: arxiv-2407.08462
type: arxiv
title: Distributed Deep Reinforcement Learning Based Gradient Quantization for Federated
  Learning Enabled Vehicle Edge Computing
url: http://arxiv.org/abs/2407.08462v2
authors:
- Cui Zhang
- Wenjun Zhang
- Qiong Wu
- Pingyi Fan
- Qiang Fan
- Jiangzhou Wang
- Khaled B. Letaief
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:7a8699aa19ab87fd9a9d44b034dadc3c55c82531517272095e9465c838855835
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2407.08462.md
  legacy_slug: arxiv_2407.08462
published_at: '2024-07-11'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Distributed Deep Reinforcement Learning Based Gradient Quantization for Federated Learning Enabled Vehicle Edge Computing

**Authors:** Cui Zhang, Wenjun Zhang, Qiong Wu, Pingyi Fan, Qiang Fan, Jiangzhou Wang, Khaled B. Letaief  
**Published:** 2024-07-11T12:58:47Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2407.08462v2.pdf

## Abstract

Federated Learning (FL) can protect the privacy of the vehicles in vehicle edge computing (VEC) to a certain extent through sharing the gradients of vehicles' local models instead of local data. The gradients of vehicles' local models are usually large for the vehicular artificial intelligence (AI) applications, thus transmitting such large gradients would cause large per-round latency. Gradient quantization has been proposed as one effective approach to reduce the per-round latency in FL enabled VEC through compressing gradients and reducing the number of bits, i.e., the quantization level, to transmit gradients. The selection of quantization level and thresholds determines the quantization error, which further affects the model accuracy and training time. To do so, the total training time and quantization error (QE) become two key metrics for the FL enabled VEC. It is critical to jointly optimize the total training time and QE for the FL enabled VEC. However, the time-varying chan...

## Relevance

**Score:** 3/5  
Distributed DRL-based gradient quantization for federated learning in vehicle edge computing; combines FL, edge computing, and multi-agent coordination with empirical latency results.
