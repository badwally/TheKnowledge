---
id: arxiv-2110.15362
type: arxiv
title: 'BitTrain: Sparse Bitmap Compression for Memory-Efficient Training on the Edge'
url: http://arxiv.org/abs/2110.15362v1
authors:
- Abdelrahman Hosny
- Marina Neseem
- Sherief Reda
ingested_at: '2026-04-28T15:31:58Z'
content_hash: sha256:a269df22d6d75479e04dfa1a4a2495a9a79d6237c2b4ae96190ee3241e915bd9
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
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2110.15362.md
  legacy_slug: arxiv_2110.15362
published_at: '2021-10-29'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:58Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# BitTrain: Sparse Bitmap Compression for Memory-Efficient Training on the Edge

**Authors:** Abdelrahman Hosny, Marina Neseem, Sherief Reda  
**Published:** 2021-10-29T16:30:57Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2110.15362v1.pdf

## Abstract

Training on the Edge enables neural networks to learn continuously from new data after deployment on memory-constrained edge devices. Previous work is mostly concerned with reducing the number of model parameters which is only beneficial for inference. However, memory footprint from activations is the main bottleneck for training on the edge. Existing incremental training methods fine-tune the last few layers sacrificing accuracy gains from re-training the whole model. In this work, we investigate the memory footprint of training deep learning models, and use our observations to propose BitTrain. In BitTrain, we exploit activation sparsity and propose a novel bitmap compression technique that reduces the memory footprint during training. We save the activations in our proposed bitmap compression format during the forward pass of the training, and restore them during the backward pass for the optimizer computations. The proposed method can be integrated seamlessly in the computation ...

## Relevance

**Score:** 3/5  
BitTrain introduces bitmap compression for activation memory during on-device training, enabling full model retraining on memory-constrained edge devices; published at ACM/IEEE SEC 2021.
