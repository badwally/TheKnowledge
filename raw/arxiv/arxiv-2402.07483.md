---
id: arxiv-2402.07483
type: arxiv
title: 'T-RAG: Lessons from the LLM Trenches'
url: https://arxiv.org/abs/2402.07483
authors:
- Masoomali Fatehkia
- Ji Kim Lucas
- Sanjay Chawla
ingested_at: '2026-04-30T16:39:48Z'
content_hash: sha256:48aa5f94fc065c50b73c6ff284754de8f78528d18a1f50ce2f5026bb7670081d
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2402.07483'
  categories:
  - cs.AI
  - cs.CL
  doi: ''
  primary_category: cs.AI
  journal_ref: ''
  comment: Added Needle in a Haystack analysis for T-RAG
  abstract_only: true
published_at: '2024-02-12'
---
Large Language Models (LLM) have shown remarkable language capabilities fueling attempts to integrate them into applications across a wide range of domains. An important application area is question answering over private enterprise documents where the main considerations are data security, which necessitates applications that can be deployed on-prem, limited computational resources and the need for a robust application that correctly responds to queries. Retrieval-Augmented Generation (RAG) has emerged as the most prominent framework for building LLM-based applications. While building a RAG is relatively straightforward, making it robust and a reliable application requires extensive customization and relatively deep knowledge of the application domain. We share our experiences building and deploying an LLM application for question answering over private organizational documents. Our application combines the use of RAG with a finetuned open-source LLM. Additionally, our system, which we call Tree-RAG (T-RAG), uses a tree structure to represent entity hierarchies within the organization. This is used to generate a textual description to augment the context when responding to user queries pertaining to entities within the organization's hierarchy. Our evaluations, including a Needle in a Haystack test, show that this combination performs better than a simple RAG or finetuning implementation. Finally, we share some lessons learned based on our experiences building an LLM application for real-world use.
