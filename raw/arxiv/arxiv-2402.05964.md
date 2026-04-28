---
id: arxiv-2402.05964
type: arxiv
title: A Survey on Transformer Compression
url: http://arxiv.org/abs/2402.05964v2
authors:
- Yehui Tang
- Yunhe Wang
- Jianyuan Guo
- Zhijun Tu
- Kai Han
- Hailin Hu
- Dacheng Tao
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:6c0365dc2b028cc75c37db5e5fe8b65e3600625b488695ab40e0bf474e916fca
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2402.05964.md
  legacy_slug: arxiv_2402.05964
published_at: '2024-02-05'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# A Survey on Transformer Compression

**Authors:** Yehui Tang, Yunhe Wang, Jianyuan Guo, Zhijun Tu, Kai Han, Hailin Hu, Dacheng Tao  
**Published:** 2024-02-05T12:16:28Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2402.05964v2.pdf

## Abstract

Transformer plays a vital role in the realms of natural language processing (NLP) and computer vision (CV), specially for constructing large language models (LLM) and large vision models (LVM). Model compression methods reduce the memory and computational cost of Transformer, which is a necessary step to implement large language/vision models on practical devices. Given the unique architecture of Transformer, featuring alternative attention and feedforward neural network (FFN) modules, specific compression techniques are usually required. The efficiency of these compression methods is also paramount, as retraining large models on the entire training dataset is usually impractical. This survey provides a comprehensive review of recent compression methods, with a specific focus on their application to Transformer-based models. The compression methods are primarily categorized into pruning, quantization, knowledge distillation, and efficient architecture design (Mamba, RetNet, RWKV, et...

## Relevance

**Score:** 3/5  
Comprehensive survey of transformer compression (pruning, quantization, distillation, Mamba/RetNet alternatives); covers the core compression toolkit needed for edge LLM deployment.
