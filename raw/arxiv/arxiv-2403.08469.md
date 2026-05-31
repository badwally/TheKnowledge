---
schema_version: 1
id: arxiv-2403.08469
type: arxiv
title: An Analysis of Human Alignment of Latent Diffusion Models
url: https://arxiv.org/abs/2403.08469
authors:
- Lorenz Linhardt
- Marco Morik
- Sidney Bender
- Naima Elosegui Borras
ingested_at: '2026-05-30T20:40:00Z'
content_hash: sha256:84a8a06806d3603750ce22677812fc66d7d954fa26d9315ed65b8974328b1b3c
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2403.08469'
  categories:
  - cs.LG
  - cs.HC
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: Accepted at the ICLR 2024 Workshop on Representational Alignment
  abstract_only: true
published_at: '2024-03-13'
filter:
  score: 0.7
---
Diffusion models, trained on large amounts of data, showed remarkable performance for image synthesis. They have high error consistency with humans and low texture bias when used for classification. Furthermore, prior work demonstrated the decomposability of their bottleneck layer representations into semantic directions. In this work, we analyze how well such representations are aligned to human responses on a triplet odd-one-out task. We find that despite the aforementioned observations: I) The representational alignment with humans is comparable to that of models trained only on ImageNet-1k. II) The most aligned layers of the denoiser U-Net are intermediate layers and not the bottleneck. III) Text conditioning greatly improves alignment at high noise levels, hinting at the importance of abstract textual information, especially in the early stage of generation.
