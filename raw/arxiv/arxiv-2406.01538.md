---
schema_version: 1
id: arxiv-2406.01538
type: arxiv
title: What Are Large Language Models Mapping to in the Brain? A Case Against Over-Reliance
  on Brain Scores
url: https://arxiv.org/abs/2406.01538
authors:
- Ebrahim Feghhi
- Nima Hadidi
- Bryan Song
- Idan A. Blank
- Jonathan C. Kao
ingested_at: '2026-05-30T21:59:04Z'
content_hash: sha256:9cae27d9ad01810c1625d1acf8bf43ab8e48380ebb39e07bc7e153dab69e1e01
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2406.01538'
  categories:
  - cs.CL
  - cs.AI
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: 10 pages, 4 figures in the main paper
  abstract_only: true
published_at: '2024-06-03'
filter:
  score: 0.75
---
Given the remarkable capabilities of large language models (LLMs), there has been a growing interest in evaluating their similarity to the human brain. One approach towards quantifying this similarity is by measuring how well a model predicts neural signals, also called "brain score". Internal representations from LLMs achieve state-of-the-art brain scores, leading to speculation that they share computational principles with human language processing. This inference is only valid if the subset of neural activity predicted by LLMs reflects core elements of language processing. Here, we question this assumption by analyzing three neural datasets used in an impactful study on LLM-to-brain mappings, with a particular focus on an fMRI dataset where participants read short passages. We first find that when using shuffled train-test splits, as done in previous studies with these datasets, a trivial feature that encodes temporal autocorrelation not only outperforms LLMs but also accounts for the majority of neural variance that LLMs explain. We therefore use contiguous splits moving forward. Second, we explain the surprisingly high brain scores of untrained LLMs by showing they do not account for additional neural variance beyond two simple features: sentence length and sentence position. This undermines evidence used to claim that the transformer architecture biases computations to be more brain-like. Third, we find that brain scores of trained LLMs on this dataset can largely be explained by sentence length, position, and pronoun-dereferenced static word embeddings; a small, additional amount is explained by sense-specific embeddings and contextual representations of sentence structure. We conclude that over-reliance on brain scores can lead to over-interpretations of similarity between LLMs and brains, and emphasize the importance of deconstructing what LLMs are mapping to in neural signals.
