---
schema_version: 1
id: arxiv-2302.08589
type: arxiv
title: Syntactic Structure Processing in the Brain while Listening
url: https://arxiv.org/abs/2302.08589
authors:
- Subba Reddy Oota
- Mounika Marreddy
- Manish Gupta
- Bapi Raju Surampud
ingested_at: '2026-06-01T19:54:51Z'
content_hash: sha256:7ccf57da8de5842c44411a539f195da9b1819c5ea0059cd3e3858196694222d4
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2302.08589'
  categories:
  - cs.CL
  - q-bio.NC
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: 21 pages, 22 figures
  abstract_only: true
published_at: '2023-02-16'
filter:
  score: 0.7
---
Syntactic parsing is the task of assigning a syntactic structure to a sentence. There are two popular syntactic parsing methods: constituency and dependency parsing. Recent works have used syntactic embeddings based on constituency trees, incremental top-down parsing, and other word syntactic features for brain activity prediction given the text stimuli to study how the syntax structure is represented in the brain's language network. However, the effectiveness of dependency parse trees or the relative predictive power of the various syntax parsers across brain areas, especially for the listening task, is yet unexplored. In this study, we investigate the predictive power of the brain encoding models in three settings: (i) individual performance of the constituency and dependency syntactic parsing based embedding methods, (ii) efficacy of these syntactic parsing based embedding methods when controlling for basic syntactic signals, (iii) relative effectiveness of each of the syntactic embedding methods when controlling for the other. Further, we explore the relative importance of syntactic information (from these syntactic embedding methods) versus semantic information using BERT embeddings. We find that constituency parsers help explain activations in the temporal lobe and middle-frontal gyrus, while dependency parsers better encode syntactic structure in the angular gyrus and posterior cingulate cortex. Although semantic signals from BERT are more effective compared to any of the syntactic features or embedding methods, syntactic embedding methods explain additional variance for a few brain regions.
