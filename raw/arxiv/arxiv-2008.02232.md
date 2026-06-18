---
schema_version: 1
id: arxiv-2008.02232
type: arxiv
title: 'DaRLing: A Datalog rewriter for OWL 2 RL ontological reasoning under SPARQL
  queries'
url: https://arxiv.org/abs/2008.02232
authors:
- Alessio Fiorentino
- Jessica Zangari
- Marco Manna
ingested_at: '2026-06-17T23:25:00Z'
content_hash: sha256:c66ebef57fa5b28e4ecb93cfe06bf37f37d74bb283905161d59f8f21472fb1fd
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2008.02232'
  categories:
  - cs.AI
  - cs.LO
  doi: ''
  primary_category: cs.AI
  journal_ref: ''
  comment: Paper presented at the 36th International Conference on Logic Programming
    (ICLP 2020), University Of Calabria, Rende (CS), Italy, September 2020, 16 pages
  abstract_only: true
published_at: '2020-08-05'
filter:
  score: 1.0
---
The W3C Web Ontology Language (OWL) is a powerful knowledge representation formalism at the basis of many semantic-centric applications. Since its unrestricted usage makes reasoning undecidable already in case of very simple tasks, expressive yet decidable fragments have been identified. Among them, we focus on OWL 2 RL, which offers a rich variety of semantic constructors, apart from supporting all RDFS datatypes. Although popular Web resources - such as DBpedia - fall in OWL 2 RL, only a few systems have been designed and implemented for this fragment. None of them, however, fully satisfy all the following desiderata: (i) being freely available and regularly maintained; (ii) supporting query answering and SPARQL queries; (iii) properly applying the sameAs property without adopting the unique name assumption; (iv) dealing with concrete datatypes. To fill the gap, we present DaRLing, a freely available Datalog rewriter for OWL 2 RL ontological reasoning under SPARQL queries. In particular, we describe its architecture, the rewriting strategies it implements, and the result of an experimental evaluation that demonstrates its practical applicability. This paper is under consideration in Theory and Practice of Logic Programming (TPLP).
