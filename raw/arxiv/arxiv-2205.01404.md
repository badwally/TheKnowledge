---
schema_version: 1
id: arxiv-2205.01404
type: arxiv
title: 'Neural Language Taskonomy: Which NLP Tasks are the most Predictive of fMRI
  Brain Activity?'
url: https://arxiv.org/abs/2205.01404
authors:
- Subba Reddy Oota
- Jashn Arora
- Veeral Agarwal
- Mounika Marreddy
- Manish Gupta
- Bapi Raju Surampudi
ingested_at: '2026-05-30T20:40:30Z'
content_hash: sha256:f57dcae226b91c993f2dbd8794c2040f49b3e85c77b36c52aa3a06e925fcc0b8
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2205.01404'
  categories:
  - cs.CL
  - cs.AI
  - cs.LG
  - q-bio.NC
  doi: 10.18653/v1/2022.naacl-main.235
  primary_category: cs.CL
  journal_ref: ''
  comment: 18 pages, 18 figures
  abstract_only: true
published_at: '2022-05-03'
filter:
  score: 0.76
---
Several popular Transformer based language models have been found to be successful for text-driven brain encoding. However, existing literature leverages only pretrained text Transformer models and has not explored the efficacy of task-specific learned Transformer representations. In this work, we explore transfer learning from representations learned for ten popular natural language processing tasks (two syntactic and eight semantic) for predicting brain responses from two diverse datasets: Pereira (subjects reading sentences from paragraphs) and Narratives (subjects listening to the spoken stories). Encoding models based on task features are used to predict activity in different regions across the whole brain. Features from coreference resolution, NER, and shallow syntax parsing explain greater variance for the reading activity. On the other hand, for the listening activity, tasks such as paraphrase generation, summarization, and natural language inference show better encoding performance. Experiments across all 10 task representations provide the following cognitive insights: (i) language left hemisphere has higher predictive brain activity versus language right hemisphere, (ii) posterior medial cortex, temporo-parieto-occipital junction, dorsal frontal lobe have higher correlation versus early auditory and auditory association cortex, (iii) syntactic and semantic tasks display a good predictive performance across brain regions for reading and listening stimuli resp.
