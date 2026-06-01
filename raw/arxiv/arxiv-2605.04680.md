---
schema_version: 1
id: arxiv-2605.04680
type: arxiv
title: Multi-Level Bidirectional Biomimetic Learning for EEG-Based Visual Decoding
url: https://arxiv.org/abs/2605.04680
authors:
- Jingtao Liu
- Peiliang Gong
- Chuhang Zheng
- Yiheng Liu
- Qi Zhu
ingested_at: '2026-06-01T19:55:00Z'
content_hash: sha256:cc4fa2b145a5b01eb9100c542724ad5b121d205e93c653336b5531423bd363dd
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2605.04680'
  categories:
  - cs.CV
  - cs.AI
  doi: ''
  primary_category: cs.CV
  journal_ref: ''
  comment: 20 pages, 13 figures, 15 tables
  abstract_only: true
published_at: '2026-05-06'
filter:
  score: 0.75
---
EEG-based visual neural decoding aims to align neural responses with visual stimuli for tasks such as image retrieval. However, limited paired data and a fundamental mismatch between high-fidelity digital images and biological visual perception - distorted by retinotopic mapping and subject-specific neuroanatomy - severely impede cross-modal alignment. To address this, we propose MB2L, a Multi-Level Bidirectional Biomimetic Learning framework that incorporates structured physiological inductive biases into representation learning. Specifically, we propose Adaptive Blur with Visual Priors to mitigate perceptual-structural mismatch by reweighting visual inputs according to retinotopic priors. We further propose Biomimetic Visual Feature Extraction to learn multi-level visual representations consistent with hierarchical cortical processing, enhancing subject-invariant encoding. These modules are jointly optimized via Multi-level Bidirectional Contrastive Learning, which aligns EEG and visual features in a shared semantic space through bidirectional contrastive objectives. Experiments show MB2L achieves 80.5% Top-1 and 97.6% Top-5 accuracy on zero-shot EEG-to-image retrieval, significantly outperforming prior methods and demonstrating strong generalization across subjects and experimental settings.
