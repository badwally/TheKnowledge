---
schema_version: 1
id: arxiv-1406.3047
type: arxiv
title: 'Tree-like Queries in OWL 2 QL: Succinctness and Complexity Results'
url: https://arxiv.org/abs/1406.3047
authors:
- Meghyn Bienvenu
- Stanislav Kikot
- Vladimir Podolskii
ingested_at: '2026-06-17T18:07:35Z'
content_hash: sha256:f8d60ea3cfc6ead8d1466f07f8a616b5b451e3600948a6ba1af3e71433fa66d9
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '1406.3047'
  categories:
  - cs.AI
  - cs.CC
  - cs.DB
  doi: ''
  primary_category: cs.AI
  journal_ref: ''
  comment: This is an extended version of a paper accepted at LICS'15. It contains
    both succinctness and complexity results and adopts FOL notation. The appendix
    contains proofs that had to be omitted from the conference version for lack of
    space. The previous arxiv version (a long version of our DL'14 workshop paper)
    only contained the succinctness results and used description logic notation
  abstract_only: true
published_at: '2014-06-11'
filter:
  score: 0.95
---
This paper investigates the impact of query topology on the difficulty of answering conjunctive queries in the presence of OWL 2 QL ontologies. Our first contribution is to clarify the worst-case size of positive existential (PE), non-recursive Datalog (NDL), and first-order (FO) rewritings for various classes of tree-like conjunctive queries, ranging from linear queries to bounded treewidth queries. Perhaps our most surprising result is a superpolynomial lower bound on the size of PE-rewritings that holds already for linear queries and ontologies of depth 2. More positively, we show that polynomial-size NDL-rewritings always exist for tree-shaped queries with a bounded number of leaves (and arbitrary ontologies), and for bounded treewidth queries paired with bounded depth ontologies. For FO-rewritings, we equate the existence of polysize rewritings with well-known problems in Boolean circuit complexity. As our second contribution, we analyze the computational complexity of query answering and establish tractability results (either NL- or LOGCFL-completeness) for a range of query-ontology pairs. Combining our new results with those from the literature yields a complete picture of the succinctness and complexity landscapes for the considered classes of queries and ontologies.
