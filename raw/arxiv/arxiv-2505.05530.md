---
id: arxiv-2505.05530
type: arxiv
title: 'Low-bit Model Quantization for Deep Neural Networks: A Survey'
url: http://arxiv.org/abs/2505.05530v1
authors:
- Kai Liu
- Qian Zheng
- Kaiwen Tao
- Zhiteng Li
- Haotong Qin
- Wenbo Li
- Yong Guo
- Xianglong Liu
- Linghe Kong
- Guihai Chen
- Yulun Zhang
- Xiaokang Yang
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:fa0f9ef66ca82a7eb2b1f6bc08598e2875040794c0bf7d53542399fbd4c0c76a
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2505.05530.md
  legacy_slug: arxiv_2505.05530
published_at: '2025-05-08'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Low-bit Model Quantization for Deep Neural Networks: A Survey

**Authors:** Kai Liu, Qian Zheng, Kaiwen Tao, Zhiteng Li, Haotong Qin, Wenbo Li, Yong Guo, Xianglong Liu, Linghe Kong, Guihai Chen, Yulun Zhang, Xiaokang Yang  
**Published:** 2025-05-08T13:26:19Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2505.05530v1.pdf

## Abstract

With unprecedented rapid development, deep neural networks (DNNs) have deeply influenced almost all fields. However, their heavy computation costs and model sizes are usually unacceptable in real-world deployment. Model quantization, an effective weight-lighting technique, has become an indispensable procedure in the whole deployment pipeline. The essence of quantization acceleration is the conversion from continuous floating-point numbers to discrete integer ones, which significantly speeds up the memory I/O and calculation, i.e., addition and multiplication. However, performance degradation also comes with the conversion because of the loss of precision. Therefore, it has become increasingly popular and critical to investigate how to perform the conversion and how to compensate for the information loss. This article surveys the recent five-year progress towards low-bit quantization on DNNs. We discuss and compare the state-of-the-art quantization methods and classify them into 8 m...

## Relevance

**Score:** 4/5  
Comprehensive five-year survey of low-bit quantization for DNNs across eight method categories; directly foundational for understanding on-device model compression techniques required for edge deployment.
