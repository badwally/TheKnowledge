---
schema_version: 1
id: arxiv-2410.11516
type: arxiv
title: 'TopoLM: brain-like spatio-functional organization in a topographic language
  model'
url: https://arxiv.org/abs/2410.11516
authors:
- Neil Rathi
- Johannes Mehrer
- Badr AlKhamissi
- Taha Binhuraib
- Nicholas M. Blauch
- Martin Schrimpf
ingested_at: '2026-05-30T20:01:46Z'
content_hash: sha256:dce52cfce1330a77b394b9db5928f9fd08bc2800f238c66554c5402afc560891
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2410.11516'
  categories:
  - cs.CL
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2024-10-15'
filter:
  score: 0.85
---
Neurons in the brain are spatially organized such that neighbors on tissue often exhibit similar response profiles. In the human language system, experimental studies have observed clusters for syntactic and semantic categories, but the mechanisms underlying this functional organization remain unclear. Here, building on work from the vision literature, we develop TopoLM, a transformer language model with an explicit two-dimensional spatial representation of model units. By combining a next-token prediction objective with a spatial smoothness loss, representations in this model assemble into clusters that correspond to semantically interpretable groupings of text and closely match the functional organization in the brain's language system. TopoLM successfully predicts the emergence of the spatio-functional organization of a cortical language system as well as the organization of functional clusters selective for fine-grained linguistic features empirically observed in human cortex. Our results suggest that the functional organization of the human language system is driven by a unified spatial objective, and provide a functionally and spatially aligned model of language processing in the brain.
