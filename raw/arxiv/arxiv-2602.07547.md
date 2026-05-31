---
schema_version: 1
id: arxiv-2602.07547
type: arxiv
title: 'Linguistic properties and model scale in brain encoding: from small to compressed
  language models'
url: https://arxiv.org/abs/2602.07547
authors:
- Subba Reddy Oota
- Vijay Rowtula
- Satya Sai Srinath Namburi
- Khushbu Pahwa
- Anant Khandelwal
- Manish Gupta
- Tanmoy Chakraborty
- Bapi S. Raju
ingested_at: '2026-05-30T20:01:55Z'
content_hash: sha256:6057cae9a2b172ab9ef97ea46d36f099caed9cb523c75432804cc38773add399
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2602.07547'
  categories:
  - q-bio.NC
  - cs.AI
  - cs.CL
  - cs.LG
  doi: ''
  primary_category: q-bio.NC
  journal_ref: ''
  comment: 40 pages, 33 figures
  abstract_only: true
published_at: '2026-02-07'
filter:
  score: 0.8
---
Recent work has shown that scaling large language models (LLMs) improves their alignment with human brain activity, yet it remains unclear what drives these gains and which representational properties are responsible. Although larger models often yield better task performance and brain alignment, they are increasingly difficult to analyze mechanistically. This raises a fundamental question: what is the minimal model capacity required to capture brain-relevant representations? To address this question, we systematically investigate how constraining model scale and numerical precision affects brain alignment. We compare full-precision LLMs, small language models (SLMs), and compressed variants (quantized and pruned) by predicting fMRI responses during naturalistic language comprehension. Across model families up to 14B parameters, we find that 3B SLMs achieve brain predictivity indistinguishable from larger LLMs, whereas 1B models degrade substantially, particularly in semantic language regions. Brain alignment is remarkably robust to compression: most quantization and pruning methods preserve neural predictivity, with GPTQ as a consistent exception. Linguistic probing reveals a dissociation between task performance and brain predictivity: compression degrades discourse, syntax, and morphology, yet brain predictivity remains largely unchanged. Overall, brain alignment saturates at modest model scales and is resilient to compression, challenging common assumptions about neural scaling and motivating compact models for brain-aligned language modeling.
