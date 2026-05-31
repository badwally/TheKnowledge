---
schema_version: 1
id: arxiv-2305.11863
type: arxiv
title: Scaling laws for language encoding models in fMRI
url: https://arxiv.org/abs/2305.11863
authors:
- Richard Antonello
- Aditya Vaidya
- Alexander G. Huth
ingested_at: '2026-05-30T20:00:42Z'
content_hash: sha256:965bfa1f028c1fee0ca58981aa358b2a6298d64b5c4bf3ef3db5e2f3b869a67d
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2305.11863'
  categories:
  - cs.CL
  - cs.AI
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: Accepted to the Thirty-seventh Annual Conference on Neural Information
    Processing Systems (NeurIPS 2023). Please cite NeurIPS version
  abstract_only: true
published_at: '2023-05-19'
filter:
  score: 0.85
---
Representations from transformer-based unidirectional language models are known to be effective at predicting brain responses to natural language. However, most studies comparing language models to brains have used GPT-2 or similarly sized language models. Here we tested whether larger open-source models such as those from the OPT and LLaMA families are better at predicting brain responses recorded using fMRI. Mirroring scaling results from other contexts, we found that brain prediction performance scales logarithmically with model size from 125M to 30B parameter models, with ~15% increased encoding performance as measured by correlation with a held-out test set across 3 subjects. Similar logarithmic behavior was observed when scaling the size of the fMRI training set. We also characterized scaling for acoustic encoding models that use HuBERT, WavLM, and Whisper, and we found comparable improvements with model size. A noise ceiling analysis of these large, high-performance encoding models showed that performance is nearing the theoretical maximum for brain areas such as the precuneus and higher auditory cortex. These results suggest that increasing scale in both models and data will yield incredibly effective models of language processing in the brain, enabling better scientific understanding as well as applications such as decoding.
