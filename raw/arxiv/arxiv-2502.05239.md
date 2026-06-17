---
schema_version: 1
id: arxiv-2502.05239
type: arxiv
title: 'Enhancing Knowledge Graph Construction: Evaluating with Emphasis on Hallucination,
  Omission, and Graph Similarity Metrics'
url: https://arxiv.org/abs/2502.05239
authors:
- Hussam Ghanem
- Christophe Cruz
ingested_at: '2026-06-17T18:52:21Z'
content_hash: sha256:b587521679e018ddc8bd2c0939be750c47c163ecaa5e20341b7a57dd07e6241a
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2502.05239'
  categories:
  - cs.CL
  - cs.AI
  doi: ''
  primary_category: cs.CL
  journal_ref: Sixth International Knowledge Graph and Semantic Web Conference (KGSWC
    2024), Dec 2024, Paris, France
  comment: ''
  abstract_only: true
published_at: '2025-02-07'
filter:
  score: 0.8
---
Recent advancements in large language models have demonstrated significant potential in the automated construction of knowledge graphs from unstructured text. This paper builds upon our previous work [16], which evaluated various models using metrics like precision, recall, F1 score, triple matching, and graph matching, and introduces a refined approach to address the critical issues of hallucination and omission. We propose an enhanced evaluation framework incorporating BERTScore for graph similarity, setting a practical threshold of 95% for graph matching. Our experiments focus on the Mistral model, comparing its original and fine-tuned versions in zero-shot and few-shot settings. We further extend our experiments using examples from the KELM-sub training dataset, illustrating that the fine-tuned model significantly improves knowledge graph construction accuracy while reducing the exact hallucination and omission. However, our findings also reveal that the fine-tuned models perform worse in generalization tasks on the KELM-sub dataset. This study underscores the importance of comprehensive evaluation metrics in advancing the state-of-the-art in knowledge graph construction from textual data.
