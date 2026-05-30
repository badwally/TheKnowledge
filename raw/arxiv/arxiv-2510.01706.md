---
schema_version: 1
id: arxiv-2510.01706
type: arxiv
title: Representational Alignment Across Model Layers and Brain Regions with Multi-Level
  Optimal Transport
url: https://arxiv.org/abs/2510.01706
authors:
- Shaan Shah
- Meenakshi Khosla
ingested_at: '2026-05-30T20:01:01Z'
content_hash: sha256:fba505d18d3fd79b7d1e3df623e2db6e33f2c2e8df8ef629733f543090d1743e
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2510.01706'
  categories:
  - cs.LG
  - cs.AI
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2025-10-02'
filter:
  score: 0.75
---
Standard representational similarity methods align each layer of a network to its best match in another independently, producing asymmetric results, lacking a global alignment score, and struggling with networks of different depths. These limitations arise from ignoring global activation structure and restricting mappings to rigid one-to-one layer correspondences. We propose Multi-Level Optimal Transport (MOT), a unified framework that jointly infers soft, globally consistent layer-to-layer couplings and neuron-level transport plans. MOT allows source neurons to distribute mass across multiple target layers while minimizing total transport cost under marginal constraints. This yields both a single alignment score for the entire network comparison and a soft transport plan that naturally handles depth mismatches through mass distribution. We evaluate MOT on vision models, large language models, and human visual cortex recordings. Across all domains, MOT matches or surpasses standard pairwise matching in alignment quality. Moreover, it reveals smooth, fine-grained hierarchical correspondences: early layers map to early layers, deeper layers maintain relative positions, and depth mismatches are resolved by distributing representations across multiple layers. These structured patterns emerge naturally from global optimization without being imposed, yet are absent in greedy layer-wise methods. MOT thus enables richer, more interpretable comparisons between representations, particularly when networks differ in architecture or depth. We further extend our method to a three-level MOT framework, providing a proof-of-concept alignment of two networks across their training trajectories and demonstrating that MOT uncovers checkpoint-wise correspondences missed by greedy layer-wise matching.
