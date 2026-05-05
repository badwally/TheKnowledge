---
id: arxiv-2108.11898
type: arxiv
title: Supervised Compression for Resource-Constrained Edge Computing Systems
url: http://arxiv.org/abs/2108.11898v3
authors:
- Yoshitomo Matsubara
- Ruihan Yang
- Marco Levorato
- Stephan Mandt
ingested_at: '2026-04-28T15:31:58Z'
content_hash: sha256:48a7c6eb169f94cc2757d32c335f565b078fdbc9b569b272bb666d1ca568c6c9
domains:
- edge-ai-agentic
nlm_corpus_ids:
- e7f21255-0787-4091-ab69-5f79669e1501
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:58Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2108.11898.md
  legacy_slug: arxiv_2108.11898
published_at: '2021-08-21'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:58Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Supervised Compression for Resource-Constrained Edge Computing Systems

**Authors:** Yoshitomo Matsubara, Ruihan Yang, Marco Levorato, Stephan Mandt  
**Published:** 2021-08-21T11:10:29Z  
**Venue:** IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) 2022  
**PDF:** http://arxiv.org/pdf/2108.11898v3.pdf

## Abstract

There has been much interest in deploying deep learning algorithms on low-powered devices, including smartphones, drones, and medical sensors. However, full-scale deep neural networks are often too resource-intensive in terms of energy and storage. As a result, the bulk part of the machine learning operation is therefore often carried out on an edge server, where the data is compressed and transmitted. However, compressing data (such as images) leads to transmitting information irrelevant to the supervised task. Another popular approach is to split the deep network between the device and the server while compressing intermediate features. To date, however, such split computing strategies have barely outperformed the aforementioned naive data compression baselines due to their inefficient approaches to feature compression. This paper adopts ideas from knowledge distillation and neural image compression to compress intermediate feature representations more efficiently. Our supervised ...

## Relevance

**Score:** 3/5  
Proposes supervised feature compression for split computing between on-device and edge server, using knowledge distillation to compress intermediate representations; addresses core split-inference architecture for resource-constrained devices (WACV 2022).
