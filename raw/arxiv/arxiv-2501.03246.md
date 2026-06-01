---
schema_version: 1
id: arxiv-2501.03246
type: arxiv
title: Bridging Auditory Perception and Language Comprehension through MEG-Driven
  Encoding Models
url: https://arxiv.org/abs/2501.03246
authors:
- Matteo Ciferri
- Matteo Ferrante
- Nicola Toschi
ingested_at: '2026-06-01T19:55:06Z'
content_hash: sha256:a16efb56ca8dffcf7d4c1bbd1f05889288755a5adfe8f0a4397a4a984abd1197
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2501.03246'
  categories:
  - q-bio.NC
  - cs.CL
  - cs.LG
  - cs.SD
  - eess.AS
  - eess.SP
  doi: ''
  primary_category: q-bio.NC
  journal_ref: ''
  comment: 10 pages, 4 figures, Accepted at ICLR2024 Workshop TS4H
  abstract_only: true
published_at: '2024-12-22'
filter:
  score: 0.8
---
Understanding the neural mechanisms behind auditory and linguistic processing is key to advancing cognitive neuroscience. In this study, we use Magnetoencephalography (MEG) data to analyze brain responses to spoken language stimuli. We develop two distinct encoding models: an audio-to-MEG encoder, which uses time-frequency decompositions (TFD) and wav2vec2 latent space representations, and a text-to-MEG encoder, which leverages CLIP and GPT-2 embeddings. Both models successfully predict neural activity, demonstrating significant correlations between estimated and observed MEG signals. However, the text-to-MEG model outperforms the audio-based model, achieving higher Pearson Correlation (PC) score. Spatially, we identify that auditory-based embeddings (TFD and wav2vec2) predominantly activate lateral temporal regions, which are responsible for primary auditory processing and the integration of auditory signals. In contrast, textual embeddings (CLIP and GPT-2) primarily engage the frontal cortex, particularly Broca's area, which is associated with higher-order language processing, including semantic integration and language production, especially in the 8-30 Hz frequency range. The strong involvement of these regions suggests that auditory stimuli are processed through more direct sensory pathways, while linguistic information is encoded via networks that integrate meaning and cognitive control. Our results reveal distinct neural pathways for auditory and linguistic information processing, with higher encoding accuracy for text representations in the frontal regions. These insights refine our understanding of the brain's functional architecture in processing auditory and textual information, offering quantitative advancements in the modelling of neural responses to complex language stimuli.
