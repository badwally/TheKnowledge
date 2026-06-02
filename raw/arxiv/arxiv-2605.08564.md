---
schema_version: 1
id: arxiv-2605.08564
type: arxiv
title: Biological Plausibility and Representational Alignment of Feedback Alignment
  in Convolutional Networks
url: https://arxiv.org/abs/2605.08564
authors:
- Jake Lance
- Larry Kieu
ingested_at: '2026-06-01T23:44:52Z'
content_hash: sha256:1f5a44097793fd5a006678919c7829495708f442a5e3fbb15d7062e53e7fcac1
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2605.08564'
  categories:
  - cs.AI
  - cs.CV
  - cs.LG
  doi: ''
  primary_category: cs.AI
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2026-05-08'
filter:
  score: 0.72
---
The feedback alignment (FA) algorithm offers a biologically plausible alternative to backpropagation (BP) for training neural networks yet notably fails to scale to convolutional architectures. Modifications have been proposed to address this limitation, but at questionable cost to biological plausibility. In this paper, we evaluate five learning algorithms including modified FA and standard BP, applied to the same convolutional architecture with the CIFAR-10 dataset. We provide a tripartite comparative analysis focusing on biological plausibility, interpretability, and computational complexity. Our results indicate that modified FA algorithms converge on internal representations that are structurally similar to those produced by backpropagation. In particular, it appears the functional success of modified FA algorithms may be rooted in their ability to mimic the representational geometry of backpropagation, converging on similar representations despite relying on fundamentally different weight update mechanisms.
