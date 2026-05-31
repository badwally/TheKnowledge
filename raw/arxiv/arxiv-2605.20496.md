---
schema_version: 1
id: arxiv-2605.20496
type: arxiv
title: 'Platonic Representations in the Human Brain: Unsupervised Recovery of Universal
  Geometry'
url: https://arxiv.org/abs/2605.20496
authors:
- Pablo Marcos-Manchón
- Rishi Jha
- Lluís Fuentemilla
ingested_at: '2026-05-30T20:00:48Z'
content_hash: sha256:aa666618234306f88f1c9c58b573313e926769ff5ba2f0babd67ff99aea5882b
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2605.20496'
  categories:
  - q-bio.NC
  - cs.CV
  doi: ''
  primary_category: q-bio.NC
  journal_ref: ''
  comment: Code available at https://github.com/memory-formation/platonic-representations-fmri
  abstract_only: true
published_at: '2026-05-19'
filter:
  score: 0.75
---
The Strong Platonic Representation Hypothesis suggests that representational convergence in artificial neural networks can be harnessed constructively: embeddings can be translated across models through a universal latent space without paired data. We ask whether an analogous geometry can be recovered across human brains. Using fMRI data from the Natural Scenes Dataset, we propose a self-supervised encoder that learns subject-specific embeddings from brain data alone by exploiting repeated stimulus presentations. We show that these independently learned spaces can be translated across subjects using unsupervised orthogonal rotations, without paired cross-subject samples or intermediate model representations. Synchronizing pairwise rotations into a single shared latent space further improves cross-subject retrieval, indicating that subject-specific spaces are mutually compatible with a common coordinate system. These results provide evidence for a shared neural geometry in the human visual cortex: subject-specific fMRI representations are approximately isometric across individuals and can be translated through purely geometric transformations.
