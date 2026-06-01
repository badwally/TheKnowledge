---
schema_version: 1
id: arxiv-2211.11665
type: arxiv
title: Representational dissimilarity metric spaces for stochastic neural networks
url: https://arxiv.org/abs/2211.11665
authors:
- Lyndon R. Duong
- Jingyang Zhou
- Josue Nassar
- Jules Berman
- Jeroen Olieslagers
- Alex H. Williams
ingested_at: '2026-06-01T19:55:21Z'
content_hash: sha256:761b4f78f18a1577ac27afdee1f715a5b16c6e8de28489d2a7840f1b9cf20165
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2211.11665'
  categories:
  - cs.LG
  - q-bio.NC
  doi: ''
  primary_category: cs.LG
  journal_ref: International Conference on Learning Representations 2023
  comment: Published as a conference paper at ICLR 2023
  abstract_only: true
published_at: '2022-11-21'
filter:
  score: 0.85
---
Quantifying similarity between neural representations -- e.g. hidden layer activation vectors -- is a perennial problem in deep learning and neuroscience research. Existing methods compare deterministic responses (e.g. artificial networks that lack stochastic layers) or averaged responses (e.g., trial-averaged firing rates in biological data). However, these measures of _deterministic_ representational similarity ignore the scale and geometric structure of noise, both of which play important roles in neural computation. To rectify this, we generalize previously proposed shape metrics (Williams et al. 2021) to quantify differences in _stochastic_ representations. These new distances satisfy the triangle inequality, and thus can be used as a rigorous basis for many supervised and unsupervised analyses. Leveraging this novel framework, we find that the stochastic geometries of neurobiological representations of oriented visual gratings and naturalistic scenes respectively resemble untrained and trained deep network representations. Further, we are able to more accurately predict certain network attributes (e.g. training hyperparameters) from its position in stochastic (versus deterministic) shape space.
