---
schema_version: 1
id: arxiv-2605.14025
type: arxiv
title: Do Language Models Align with Brains? Prediction Scores Are Not Enough
url: https://arxiv.org/abs/2605.14025
authors:
- Xiao Jia
ingested_at: '2026-05-30T21:59:01Z'
content_hash: sha256:ad6a41ab5fde4afa2fa3894867be73e49f1c5e5d1dca092437ca0ba5d199193b
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2605.14025'
  categories:
  - q-bio.NC
  - cs.AI
  doi: ''
  primary_category: q-bio.NC
  journal_ref: ''
  comment: 39 pages, 4 main figures, 6 supplementary figures
  abstract_only: true
published_at: '2026-05-13'
filter:
  score: 0.9
---
Brain-language model comparisons often interpret neural prediction scores as evidence that model representations capture brain-relevant language computation. We asked whether language models align with brains, and whether prediction scores are enough to support that claim, using L-PACT, a source-audited framework that evaluates predictive, relational, mechanism-stripping, and reliability-bounded evidence. Across primary naturalistic language neural datasets and derived language-model representations, L-PACT compared real model features with nuisance baselines and severe controls, tested whether model-to-brain profiles reproduced brain-to-brain patterns, recomputed held-out scores after mechanism stripping, and normalized evidence against brain-brain ceilings. The locked analysis set contains 414 predictive-control rows, 2304 relational profile rows, 4320 mechanism-stripping rows, 420 brain-brain ceiling rows, and 146 integrated decision rows. Assay-sensitivity checks showed that brain-brain reliability, brain-as-model run-to-run relational profiles, independent low-level neural and WAV-derived acoustic-envelope gates, and a deterministic implanted-signal simulation can produce positive evidence when expected. Nevertheless, no real model row passed the predictive, relational, mechanism-stripping, or operational Turing-bounded reliability gates; all 146 integrated rows were control-explained. Less stringent single-criterion rules would have counted raw positive predictive, relational, stripping-delta, and ceiling-normalized effects, but L-PACT downgraded them because controls explained the apparent evidence. In the analyzed derived artifact set, the tested language-model representations do not satisfy L-PACT alignment gates; apparent positives are converted into an auditable control-explained taxonomy rather than treated as structural alignment.
