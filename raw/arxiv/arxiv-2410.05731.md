---
schema_version: 1
id: arxiv-2410.05731
type: arxiv
title: Enhancing SPARQL Generation by Triplet-order-sensitive Pre-training
url: https://arxiv.org/abs/2410.05731
authors:
- Chang Su
- Jiexing Qi
- He Yan
- Kai Zou
- Zhouhan Lin
ingested_at: '2026-06-17T20:57:57Z'
content_hash: sha256:9186c688ea3ac98d058ecac704e03e72bbffdc855008296946e23b928dd2b06d
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2410.05731'
  categories:
  - cs.IR
  doi: ''
  primary_category: cs.IR
  journal_ref: ''
  comment: accepted by CIKM 2024
  abstract_only: true
published_at: '2024-10-08'
filter:
  score: 0.75
---
Semantic parsing that translates natural language queries to SPARQL is of great importance for Knowledge Graph Question Answering (KGQA) systems. Although pre-trained language models like T5 have achieved significant success in the Text-to-SPARQL task, their generated outputs still exhibit notable errors specific to the SPARQL language, such as triplet flips. To address this challenge and further improve the performance, we propose an additional pre-training stage with a new objective, Triplet Order Correction (TOC), along with the commonly used Masked Language Modeling (MLM), to collectively enhance the model's sensitivity to triplet order and SPARQL syntax. Our method achieves state-of-the-art performances on three widely-used benchmarks.
