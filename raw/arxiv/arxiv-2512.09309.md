---
id: arxiv-2512.09309
type: arxiv
title: A Distributed Framework for Privacy-Enhanced Vision Transformers on the Edge
url: http://arxiv.org/abs/2512.09309v1
authors:
- Zihao Ding
- Mufeng Zhu
- Zhongze Tang
- Sheng Wei
- Yao Liu
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:56e87152cc597097325c19bc4fe6ac24dc83628d87de9581f6dafb14e9931175
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2512.09309.md
  legacy_slug: arxiv_2512.09309
published_at: '2025-12-10'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# A Distributed Framework for Privacy-Enhanced Vision Transformers on the Edge

**Authors:** Zihao Ding, Mufeng Zhu, Zhongze Tang, Sheng Wei, Yao Liu  
**Published:** 2025-12-10T04:37:07Z  
**Venue:** Proceedings of the Tenth ACM/IEEE Symposium on Edge Computing (SEC '25), 2025, Article 8, pp. 1-16  
**PDF:** http://arxiv.org/pdf/2512.09309v1.pdf

## Abstract

Nowadays, visual intelligence tools have become ubiquitous, offering all kinds of convenience and possibilities. However, these tools have high computational requirements that exceed the capabilities of resource-constrained mobile and wearable devices. While offloading visual data to the cloud is a common solution, it introduces significant privacy vulnerabilities during transmission and server-side computation. To address this, we propose a novel distributed, hierarchical offloading framework for Vision Transformers (ViTs) that addresses these privacy challenges by design. Our approach uses a local trusted edge device, such as a mobile phone or an Nvidia Jetson, as the edge orchestrator. This orchestrator partitions the user's visual data into smaller portions and distributes them across multiple independent cloud servers. By design, no single external server possesses the complete image, preventing comprehensive data reconstruction. The final data merging and aggregation computati...

## Relevance

**Score:** 4/5  
Distributed ViT inference framework using NVIDIA Jetson as edge orchestrator, partitioning data across cloud servers for privacy-by-design; published at ACM/IEEE SEC '25 with full system architecture and privacy/latency results.
