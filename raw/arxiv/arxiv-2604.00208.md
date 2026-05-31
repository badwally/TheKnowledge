---
schema_version: 1
id: arxiv-2604.00208
type: arxiv
title: Measuring the Representational Alignment of Neural Systems in Superposition
url: https://arxiv.org/abs/2604.00208
authors:
- Sunny Liu
- Habon Issa
- André Longon
- Liv Gorton
- Meenakshi Khosla
- David Klindt
ingested_at: '2026-05-30T20:40:27Z'
content_hash: sha256:7015e8baca2daedf5ce6942f3206ff326f1af1a0eb21ebaaa6b778fed8ddc47f
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2604.00208'
  categories:
  - cs.LG
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: 17 pages, 4 figures
  abstract_only: true
published_at: '2026-03-31'
filter:
  score: 0.7
---
Comparing the internal representations of neural networks is a central goal in both neuroscience and machine learning. Standard alignment metrics operate on raw neural activations, implicitly assuming that similar representations produce similar activity patterns. However, neural systems frequently operate in superposition, encoding more features than they have neurons via linear compression. We derive closed-form expressions showing that superposition systematically deflates Representational Similarity Analysis, Centered Kernel Alignment, and linear regression, causing networks with identical feature content to appear dissimilar. The root cause is that these metrics are dependent on cross-similarity between two systems' respective superposition matrices, which under assumption of random projection usually differ significantly, not on the latent features themselves: alignment scores conflate what a system represents with how it represents it. Under partial feature overlap, this confound can invert the expected ordering, making systems sharing fewer features appear more aligned than systems sharing more. Crucially, the apparent misalignment need not reflect a loss of information; compressed sensing guarantees that the original features remain recoverable from the lower-dimensional activity, provided they are sparse. We therefore argue that comparing neural systems in superposition requires extracting and aligning the underlying features rather than comparing the raw neural mixtures.
