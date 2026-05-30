---
schema_version: 1
id: arxiv-2507.01098
type: arxiv
title: Proof of a perfect platonic representation hypothesis
url: https://arxiv.org/abs/2507.01098
authors:
- Liu Ziyin
- Isaac Chuang
ingested_at: '2026-05-30T20:01:03Z'
content_hash: sha256:f73506c031a43a00f170f49879de5d3feaee061202fa8c52c989514b38a6f544
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2507.01098'
  categories:
  - cs.LG
  - cond-mat.dis-nn
  - q-bio.NC
  - stat.ML
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: A note
  abstract_only: true
published_at: '2025-07-01'
filter:
  score: 0.75
---
In this note, we elaborate on and explain in detail the proof given by Ziyin et al. (2025) of the ``perfect" Platonic Representation Hypothesis (PRH) for the embedded deep linear network model (EDLN). We show that if trained with the stochastic gradient descent (SGD), two EDLNs with different widths and depths and trained on different data will become Perfectly Platonic, meaning that every possible pair of layers will learn the same representation up to a rotation. Because most of the global minima of the loss function are not Platonic, that SGD only finds the perfectly Platonic solution is rather extraordinary. The proof also suggests at least six ways the PRH can be broken. We also show that in the EDLN model, the emergence of the Platonic representations is due to the same reason as the emergence of progressive sharpening. This implies that these two seemingly unrelated phenomena in deep learning can, surprisingly, have a common cause. Overall, the theory and proof highlight the importance of understanding emergent "entropic forces" due to the irreversibility of SGD training and their role in representation learning. The goal of this note is to be instructive while avoiding jargon and lengthy technical details.
