---
schema_version: 1
id: arxiv-2407.10414
type: arxiv
title: Teaching CORnet Human fMRI Representations for Enhanced Model-Brain Alignment
url: https://arxiv.org/abs/2407.10414
authors:
- Zitong Lu
- Yile Wang
ingested_at: '2026-06-01T19:55:15Z'
content_hash: sha256:50f7e7a9cc74800b498b06373490b02a83e393d577b162554edbf1126fe8e9b9
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2407.10414'
  categories:
  - eess.IV
  - cs.CV
  - cs.LG
  - q-bio.NC
  doi: ''
  primary_category: eess.IV
  journal_ref: ''
  comment: 'arXiv admin note: text overlap with arXiv:2401.17231'
  abstract_only: true
published_at: '2024-07-15'
filter:
  score: 0.88
---
Deep convolutional neural networks (DCNNs) have demonstrated excellent performance in object recognition and have been found to share some similarities with brain visual processing. However, the substantial gap between DCNNs and human visual perception still exists. Functional magnetic resonance imaging (fMRI) as a widely used technique in cognitive neuroscience can record neural activation in the human visual cortex during the process of visual perception. Can we teach DCNNs human fMRI signals to achieve a more brain-like model? To answer this question, this study proposed ReAlnet-fMRI, a model based on the SOTA vision model CORnet but optimized using human fMRI data through a multi-layer encoding-based alignment framework. This framework has been shown to effectively enable the model to learn human brain representations. The fMRI-optimized ReAlnet-fMRI exhibited higher similarity to the human brain than both CORnet and the control model in within-and across-subject as well as within- and across-modality model-brain (fMRI and EEG) alignment evaluations. Additionally, we conducted an in-depth analyses to investigate how the internal representations of ReAlnet-fMRI differ from CORnet in encoding various object dimensions. These findings provide the possibility of enhancing the brain-likeness of visual models by integrating human neural data, helping to bridge the gap between computer vision and visual neuroscience.
