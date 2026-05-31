---
schema_version: 1
id: arxiv-1905.00414
type: arxiv
title: Similarity of Neural Network Representations Revisited
url: https://arxiv.org/abs/1905.00414
authors:
- Simon Kornblith
- Mohammad Norouzi
- Honglak Lee
- Geoffrey Hinton
ingested_at: '2026-05-30T20:01:49Z'
content_hash: sha256:6430283eeda1d559914ccfcb5bfa4f4c615358965efc41f620ab7aea8299dd7d
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '1905.00414'
  categories:
  - cs.LG
  - q-bio.NC
  - stat.ML
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: ICML 2019
  abstract_only: true
published_at: '2019-05-01'
filter:
  score: 0.7
---
Recent work has sought to understand the behavior of neural networks by comparing representations between layers and between different trained models. We examine methods for comparing neural network representations based on canonical correlation analysis (CCA). We show that CCA belongs to a family of statistics for measuring multivariate similarity, but that neither CCA nor any other statistic that is invariant to invertible linear transformation can measure meaningful similarities between representations of higher dimension than the number of data points. We introduce a similarity index that measures the relationship between representational similarity matrices and does not suffer from this limitation. This similarity index is equivalent to centered kernel alignment (CKA) and is also closely connected to CCA. Unlike CCA, CKA can reliably identify correspondences between representations in networks trained from different initializations.
