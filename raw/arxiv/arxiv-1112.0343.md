---
schema_version: 1
id: arxiv-1112.0343
type: arxiv
title: 'Ontological Queries: Rewriting and Optimization (Extended Version)'
url: https://arxiv.org/abs/1112.0343
authors:
- Georg Gottlob
- Giorgio Orsi
- Andreas Pieris
ingested_at: '2026-06-17T23:25:03Z'
content_hash: sha256:b5d371f75447ab1720b86e404bd231f1c1255a2e6dd17dec44d92aa312da2199
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '1112.0343'
  categories:
  - cs.DB
  - cs.LO
  doi: ''
  primary_category: cs.DB
  journal_ref: ''
  comment: 'Extended version of "Ontological Queries: Rewriting and Optimization"
    presented at ICDE 2011'
  abstract_only: true
published_at: '2011-12-01'
filter:
  score: 0.9
---
Ontological queries are evaluated against an ontology rather than directly on a database. The evaluation and optimization of such queries is an intriguing new problem for database research.
  In this paper we discuss two important aspects of this problem: query rewriting and query optimization. Query rewriting consists of the compilation of an ontological query into an equivalent query against the underlying relational database. The focus here is on soundness and completeness. We review previous results and present a new rewriting algorithm for rather general types of ontological constraints.
  In particular, we show how a conjunctive query against an ontology can be compiled into a union of conjunctive queries against the underlying database. Ontological query optimization, in this context, attempts to improve this process so to produce possibly small and cost-effective UCQ rewritings for an input query. We review existing optimization methods, and propose an effective new method that works for linear Datalog+/-, a class of Datalog-based rules that encompasses well-known description logics of the DL-Lite family.
