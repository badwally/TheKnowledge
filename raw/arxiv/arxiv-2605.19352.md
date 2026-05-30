---
schema_version: 1
id: arxiv-2605.19352
type: arxiv
title: Brain alignment of reasoning and action representations from vision-language
  and action models during naturalistic gameplay
url: https://arxiv.org/abs/2605.19352
authors:
- Subba Reddy Oota
- Anant Khandelwal
- Khushbu Pahwa
- Satya Sai Srinath Namburi
- Tanmoy Chakraborty
- Bapi S. Raju
- Manish Gupta
ingested_at: '2026-05-30T20:40:33Z'
content_hash: sha256:f8f0577dee31ca1eee2342c9cf20fd3614382f4b0970c6c863a351732b67e5f4
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2605.19352'
  categories:
  - q-bio.NC
  - cs.AI
  - cs.LG
  doi: ''
  primary_category: q-bio.NC
  journal_ref: ''
  comment: 21 pages, 11 figures
  abstract_only: true
published_at: '2026-05-19'
filter:
  score: 0.8
---
Understanding how humans and artificial intelligence systems predict and plan by interacting with their environment is a fundamental challenge at the intersection of neuroscience and machine learning. Most brain-encoding studies focus on aligning artificial models with brain activity during language comprehension or passive visual processing, while interactive brain-alignment studies have to date been largely limited to reinforcement-learning (RL) agents and theory-based models. To address this gap, we study brain alignment of representative models from two foundation-model families, namely vision-language models (VLMs) and large-action models (LAMs), using fMRI recordings from participants playing naturalistic Atari-style video games. Specifically, we examine how action-focused and reasoning-focused prompts shape model's internal representations and align with fMRI brain activity. First, we find that both VLMs and LAMs exhibit significantly exhibit voxel-wise encoding performance than RL baselines, with the advantage holding even under matched feature dimensionality. Second, prompt-driven gains scale with the cortical processing hierarchy: the largest improvements appear in frontal-parietal and motor-planning regions, while early visual cortex gains roughly half as much. Third, variance partitioning reveals a qualitatively different representational organization: VLM is prompt-symmetric (12.5% unique action vs. 13.6% unique reasoning), whereas LAM is prompt-asymmetric (27% unique action vs. -5% unique reasoning), with the asymmetry strongest in frontal-motor cortex. Together, these results demonstrate that action-specialized fine-tuning reorganizes multimodal representations toward action-relevant neural computations even when whole-brain prediction accuracy is statistically equivalent between VLM and LAM.
