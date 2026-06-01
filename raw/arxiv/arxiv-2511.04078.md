---
schema_version: 1
id: arxiv-2511.04078
type: arxiv
title: Unveiling Deep Semantic Uncertainty Perception for Language-Anchored Multi-modal
  Vision-Brain Alignment
url: https://arxiv.org/abs/2511.04078
authors:
- Zehui Feng
- Chenqi Zhang
- Mingru Wang
- Minuo Wei
- Shiwei Cheng
- Cuntai Guan
- Ting Han
ingested_at: '2026-06-01T19:55:18Z'
content_hash: sha256:d44e3bdbf46ef6a53e1d7718a9fb8bf8b079f071b499842ef4af9d615e566cc4
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2511.04078'
  categories:
  - cs.CV
  doi: ''
  primary_category: cs.CV
  journal_ref: ''
  comment: 30 pages, 16 figures, under review as a conference paper
  abstract_only: true
published_at: '2025-11-06'
filter:
  score: 0.85
---
Unveiling visual semantics from neural signals such as EEG, MEG, and fMRI remains a fundamental challenge due to subject variability and the entangled nature of visual features. Existing approaches primarily align neural activity directly with visual embeddings, but visual-only representations often fail to capture latent semantic dimensions, limiting interpretability and deep robustness. To address these limitations, we propose Bratrix, the first end-to-end framework to achieve multimodal Language-Anchored Vision-Brain alignment. Bratrix decouples visual stimuli into hierarchical visual and linguistic semantic components, and projects both visual and brain representations into a shared latent space, enabling the formation of aligned visual-language and brain-language embeddings. To emulate human-like perceptual reliability and handle noisy neural signals, Bratrix incorporates a novel uncertainty perception module that applies uncertainty-aware weighting during alignment. By leveraging learnable language-anchored semantic matrices to enhance cross-modal correlations and employing a two-stage training strategy of single-modality pretraining followed by multimodal fine-tuning, Bratrix-M improves alignment precision. Extensive experiments on EEG, MEG, and fMRI benchmarks demonstrate that Bratrix improves retrieval, reconstruction, and captioning performance compared to state-of-the-art methods, specifically surpassing 14.3% in 200-way EEG retrieval task. Code and model are available.
