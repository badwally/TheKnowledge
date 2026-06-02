---
schema_version: 1
id: arxiv-2511.21760
type: arxiv
title: 'fMRI-LM: Towards a Universal Foundation Model for Language-Aligned fMRI Understanding'
url: https://arxiv.org/abs/2511.21760
authors:
- Yuxiang Wei
- Yanteng Zhang
- Xi Xiao
- Chengxuan Qian
- Tianyang Wang
- Vince D. Calhoun
ingested_at: '2026-06-01T23:44:40Z'
content_hash: sha256:a8672c59c3d4622968ac78815cfb3f967686a9a166f123f1942a80a98e52cda2
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2511.21760'
  categories:
  - cs.CL
  - cs.AI
  doi: ''
  primary_category: cs.CL
  journal_ref: ''
  comment: 'Code are available: https://github.com/yuxiangwei0808/fMRI-LM'
  abstract_only: true
published_at: '2025-11-24'
filter:
  score: 0.8
---
Recent advances in multimodal large language models (LLMs) have enabled unified reasoning across images, audio, and video, but extending such capability to brain imaging remains largely unexplored. Bridging this gap is essential to link neural activity with semantic cognition and to develop cross-modal brain representations. To this end, we present fMRI-LM, a foundational model that bridges functional MRI (fMRI) and language through a three-stage framework. In Stage 1, we learn a neural tokenizer that maps fMRI into discrete tokens embedded in a language-consistent space. In Stage 2, a pretrained LLM is adapted to jointly model fMRI tokens and text, treating brain activity as a sequence that can be temporally predicted and linguistically described. To overcome the lack of natural fMRI-text pairs, we construct a large descriptive corpus that translates diverse imaging-based features into structured textual descriptors, capturing the low-level organization of fMRI signals. In Stage 3, we perform multi-task, multi-paradigm instruction tuning to endow fMRI-LM with high-level semantic understanding, supporting diverse downstream applications. Across various benchmarks, fMRI-LM achieves strong zero-shot and few-shot performance, and adapts efficiently with parameter-efficient tuning (LoRA), establishing a scalable pathway toward a language-aligned, universal model for structural and semantic understanding of fMRI.
