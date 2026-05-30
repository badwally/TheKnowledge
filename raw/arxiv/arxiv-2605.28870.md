---
schema_version: 1
id: arxiv-2605.28870
type: arxiv
title: Representation Alignment Rests on Linear Structure
url: https://arxiv.org/abs/2605.28870
authors:
- Kiril Bangachev
- Guy Bresler
- Yury Polyanskiy
ingested_at: '2026-05-30T21:59:22Z'
content_hash: sha256:0ce2e70b6b34ed3485c2fb3c0e9a3228f14572aed94dde2b77837596d5264c33
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2605.28870'
  categories:
  - cs.LG
  - cs.AI
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2026-05-22'
filter:
  score: 0.82
---
We investigate the Platonic Representation Hypothesis (PRH) through a tripartite statistical framework of representations: signal, bias, and noise. {1) Signal:} We propose that Platonic alignment arises from the universal relationship between objects and attributes, which is encoded linearly in representations according to the Linear Representation Hypothesis (LRH). We provide evidence that LRH helps explain PRH by extracting linear object-attribute features with sparse autoencoders and showing that these sparse representations often exhibit stronger cross-modal alignment than their dense counterparts. {2) Bias:} Models have different implicit biases due to the diverse architectures and training procedures used. We show that this difference can be partially mitigated. Centering and normalization consistently improve cross-model alignment. {3) Noise:} Finite-sample training leads to noise in representations. We provide evidence that representational noise is driven by data scarcity by revealing a strong and consistent positive correlation between word frequency and alignment in LLMs and text embedding models. Synthesizing signal, bias, and noise, we propose a statistical model that refines the Linear Representation Hypothesis and explains further phenomena related to the alignment of representations emerging from diverse modern AI architectures.
