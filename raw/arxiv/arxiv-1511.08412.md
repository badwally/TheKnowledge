---
schema_version: 1
id: arxiv-1511.08412
type: arxiv
title: 'Beyond OWL 2 QL in OBDA: Rewritings and Approximations (Extended Version)'
url: https://arxiv.org/abs/1511.08412
authors:
- Elena Botoeva
- Diego Calvanese
- Valerio Santarelli
- Domenico Fabio Savo
- Alessandro Solimando
- Guohui Xiao
ingested_at: '2026-06-17T18:07:32Z'
content_hash: sha256:4e138a55eb14bbe1f267bc33f34148b6ae9d3d9b687b442c9f7072debaabe549
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '1511.08412'
  categories:
  - cs.AI
  doi: ''
  primary_category: cs.AI
  journal_ref: ''
  comment: 'The extended version of the AAAI 2016 paper "Beyond OWL 2 QL in OBDA:
    Rewritings and Approximations" by Elena Botoeva, Diego Calvanese, Valerio Santarelli,
    Domenico Fabio Savo, Alessandro Solimando,and Guohui Xiao'
  abstract_only: true
published_at: '2015-11-26'
filter:
  score: 0.85
---
Ontology-based data access (OBDA) is a novel paradigm facilitating access to relational data, realized by linking data sources to an ontology by means of declarative mappings. DL-Lite_R, which is the logic underpinning the W3C ontology language OWL 2 QL and the current language of choice for OBDA, has been designed with the goal of delegating query answering to the underlying database engine, and thus is restricted in expressive power. E.g., it does not allow one to express disjunctive information, and any form of recursion on the data. The aim of this paper is to overcome these limitations of DL-Lite_R, and extend OBDA to more expressive ontology languages, while still leveraging the underlying relational technology for query answering. We achieve this by relying on two well-known mechanisms, namely conservative rewriting and approximation, but significantly extend their practical impact by bringing into the picture the mapping, an essential component of OBDA. Specifically, we develop techniques to rewrite OBDA specifications with an expressive ontology to "equivalent" ones with a DL-Lite_R ontology, if possible, and to approximate them otherwise. We do so by exploiting the high expressive power of the mapping layer to capture part of the domain semantics of rich ontology languages. We have implemented our techniques in the prototype system OntoProx, making use of the state-of-the-art OBDA system Ontop and the query answering system Clipper, and we have shown their feasibility and effectiveness with experiments on synthetic and real-world data.
