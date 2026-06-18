---
schema_version: 1
id: arxiv-2207.11155
type: arxiv
title: 'CQE in OWL 2 QL: A "Longest Honeymoon" Approach (extended version)'
url: https://arxiv.org/abs/2207.11155
authors:
- Piero Bonatti
- Gianluca Cima
- Domenico Lembo
- Lorenzo Marconi
- Riccardo Rosati
- Luigi Sauro
- Domenico Fabio Savo
ingested_at: '2026-06-17T18:07:30Z'
content_hash: sha256:6e99fab296d79b862104fe8e8c090374e06a6a1cdceb3b76a4fe1c1c0792fbca
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2207.11155'
  categories:
  - cs.DB
  - cs.AI
  doi: 10.1007/978-3-031-19433-7_25
  primary_category: cs.DB
  journal_ref: ''
  comment: 'This paper is the extended version of "P.Bonatti, G.Cima, D.Lembo, L.Marconi,
    R.Rosati, L.Sauro, and D.F.Savo. Controlled query evaluation in OWL 2 QL: A "Longest
    Honeymoon" approach" accepted for publication at ISWC 2022'
  abstract_only: true
published_at: '2022-07-22'
filter:
  score: 0.85
---
Controlled Query Evaluation (CQE) has been recently studied in the context of Semantic Web ontologies. The goal of CQE is concealing some query answers so as to prevent external users from inferring confidential information. In general, there exist multiple, mutually incomparable ways of concealing answers, and previous CQE approaches choose in advance which answers are visible and which are not. In this paper, instead, we study a dynamic CQE method, namely, we propose to alter the answer to the current query based on the evaluation of previous ones. We aim at a system that, besides being able to protect confidential data, is maximally cooperative, which intuitively means that it answers affirmatively to as many queries as possible; it achieves this goal by delaying answer modifications as much as possible. We also show that the behavior we get cannot be intensionally simulated through a static approach, independent of query history. Interestingly, for OWL 2 QL ontologies and policy expressed through denials, query evaluation under our semantics is first-order rewritable, and thus in AC0 in data complexity. This paves the way for the development of practical algorithms, which we also preliminarily discuss in the paper.
