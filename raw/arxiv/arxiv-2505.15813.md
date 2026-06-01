---
schema_version: 1
id: arxiv-2505.15813
type: arxiv
title: Meta-Learning an In-Context Transformer Model of Human Higher Visual Cortex
url: https://arxiv.org/abs/2505.15813
authors:
- Muquan Yu
- Mu Nan
- Hossein Adeli
- Jacob S. Prince
- John A. Pyles
- Leila Wehbe
- Margaret M. Henderson
- Michael J. Tarr
- Andrew F. Luo
ingested_at: '2026-06-01T19:54:54Z'
content_hash: sha256:52c543ebf569a396bb99f6433f248d3f608590e62446d7cdb62a8dd31cd47e16
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2505.15813'
  categories:
  - cs.LG
  - q-bio.NC
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: 'Accepted to NeurIPS 2025. Website: https://github.com/leomqyu/BraInCoRL'
  abstract_only: true
published_at: '2025-05-21'
filter:
  score: 0.75
---
Understanding functional representations within higher visual cortex is a fundamental question in computational neuroscience. While artificial neural networks pretrained on large-scale datasets exhibit striking representational alignment with human neural responses, learning image-computable models of visual cortex relies on individual-level, large-scale fMRI datasets. The necessity for expensive, time-intensive, and often impractical data acquisition limits the generalizability of encoders to new subjects and stimuli. BraInCoRL uses in-context learning to predict voxelwise neural responses from few-shot examples without any additional finetuning for novel subjects and stimuli. We leverage a transformer architecture that can flexibly condition on a variable number of in-context image stimuli, learning an inductive bias over multiple subjects. During training, we explicitly optimize the model for in-context learning. By jointly conditioning on image features and voxel activations, our model learns to directly generate better performing voxelwise models of higher visual cortex. We demonstrate that BraInCoRL consistently outperforms existing voxelwise encoder designs in a low-data regime when evaluated on entirely novel images, while also exhibiting strong test-time scaling behavior. The model also generalizes to an entirely new visual fMRI dataset, which uses different subjects and fMRI data acquisition parameters. Further, BraInCoRL facilitates better interpretability of neural signals in higher visual cortex by attending to semantically relevant stimuli. Finally, we show that our framework enables interpretable mappings from natural language queries to voxel selectivity.
