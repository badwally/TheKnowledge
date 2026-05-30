---
schema_version: 1
id: arxiv-2507.19956
type: arxiv
title: Predicting Brain Responses To Natural Movies With Multimodal LLMs
url: https://arxiv.org/abs/2507.19956
authors:
- Cesar Kadir Torrico Villanueva
- Jiaxin Cindy Tu
- Mihir Tripathy
- Connor Lane
- Rishab Iyer
- Paul S. Scotti
ingested_at: '2026-05-30T20:40:42Z'
content_hash: sha256:f1f6a788213319a075037a4f0e8c280ee2a8dac02801e7aadf867b4cadd035bd
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2507.19956'
  categories:
  - cs.CV
  - cs.AI
  - q-bio.NC
  doi: ''
  primary_category: cs.CV
  journal_ref: ''
  comment: Code available at https://github.com/MedARC-AI/algonauts2025
  abstract_only: true
published_at: '2025-07-26'
filter:
  score: 0.75
---
We present MedARC's team solution to the Algonauts 2025 challenge. Our pipeline leveraged rich multimodal representations from various state-of-the-art pretrained models across video (V-JEPA2), speech (Whisper), text (Llama 3.2), vision-text (InternVL3), and vision-text-audio (Qwen2.5-Omni). These features extracted from the models were linearly projected to a latent space, temporally aligned to the fMRI time series, and finally mapped to cortical parcels through a lightweight encoder comprising a shared group head plus subject-specific residual heads. We trained hundreds of model variants across hyperparameter settings, validated them on held-out movies and assembled ensembles targeted to each parcel in each subject. Our final submission achieved a mean Pearson's correlation of 0.2085 on the test split of withheld out-of-distribution movies, placing our team in fourth place for the competition. We further discuss a last-minute optimization that would have raised us to second place. Our results highlight how combining features from models trained in different modalities, using a simple architecture consisting of shared-subject and single-subject components, and conducting comprehensive model selection and ensembling improves generalization of encoding models to novel movie stimuli. All code is available on GitHub.
