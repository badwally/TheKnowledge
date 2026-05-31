---
schema_version: 1
id: arxiv-2405.01012
type: arxiv
title: Correcting Biased Centered Kernel Alignment Measures in Biological and Artificial
  Neural Networks
url: https://arxiv.org/abs/2405.01012
authors:
- Alex Murphy
- Joel Zylberberg
- Alona Fyshe
ingested_at: '2026-05-30T20:40:47Z'
content_hash: sha256:8856c2254189e3c4324c27e88de05f621df4e76e7c99a33d23f4a88c41a16542
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2405.01012'
  categories:
  - q-bio.NC
  - cs.CV
  doi: ''
  primary_category: q-bio.NC
  journal_ref: ''
  comment: ICLR 2024 Re-Align Workshop
  abstract_only: true
published_at: '2024-05-02'
filter:
  score: 0.7
---
Centred Kernel Alignment (CKA) has recently emerged as a popular metric to compare activations from biological and artificial neural networks (ANNs) in order to quantify the alignment between internal representations derived from stimuli sets (e.g. images, text, video) that are presented to both systems. In this paper we highlight issues that the community should take into account if using CKA as an alignment metric with neural data. Neural data are in the low-data high-dimensionality domain, which is one of the cases where (biased) CKA results in high similarity scores even for pairs of random matrices. Using fMRI and MEG data from the THINGS project, we show that if biased CKA is applied to representations of different sizes in the low-data high-dimensionality domain, they are not directly comparable due to biased CKA's sensitivity to differing feature-sample ratios and not stimuli-driven responses. This situation can arise both when comparing a pre-selected area of interest (e.g. ROI) to multiple ANN layers, as well as when determining to which ANN layer multiple regions of interest (ROIs) / sensor groups of different dimensionality are most similar. We show that biased CKA can be artificially driven to its maximum value when using independent random data of different sample-feature ratios. We further show that shuffling sample-feature pairs of real neural data does not drastically alter biased CKA similarity in comparison to unshuffled data, indicating an undesirable lack of sensitivity to stimuli-driven neural responses. Positive alignment of true stimuli-driven responses is only achieved by using debiased CKA. Lastly, we report findings that suggest biased CKA is sensitive to the inherent structure of neural data, only differing from shuffled data when debiased CKA detects stimuli-driven alignment.
