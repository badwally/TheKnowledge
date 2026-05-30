---
schema_version: 1
id: arxiv-2505.20029
type: arxiv
title: Correlating instruction-tuning (in multimodal models) with vision-language
  processing (in the brain)
url: https://arxiv.org/abs/2505.20029
authors:
- Subba Reddy Oota
- Akshett Jindal
- Ishani Mondal
- Khushbu Pahwa
- Satya Sai Srinath Namburi
- Manish Shrivastava
- Maneesh Singh
- Bapi S. Raju
- Manish Gupta
ingested_at: '2026-05-30T20:40:39Z'
content_hash: sha256:98f54dac98923218f3c436b3532b959c8b5d0dc769b4b69568b7210020965da3
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2505.20029'
  categories:
  - q-bio.NC
  - cs.AI
  - cs.LG
  doi: ''
  primary_category: q-bio.NC
  journal_ref: ICLR-2025, Singapore
  comment: 30 pages, 22 figures, The Thirteenth International Conference on Learning
    Representations, ICLR-2025, Singapore. https://openreview.net/pdf?id=xkgfLXZ4e0
  abstract_only: true
published_at: '2025-05-26'
filter:
  score: 0.8
---
Transformer-based language models, though not explicitly trained to mimic brain recordings, have demonstrated surprising alignment with brain activity. Progress in these models-through increased size, instruction-tuning, and multimodality-has led to better representational alignment with neural data. Recently, a new class of instruction-tuned multimodal LLMs (MLLMs) have emerged, showing remarkable zero-shot capabilities in open-ended multimodal vision tasks. However, it is unknown whether MLLMs, when prompted with natural instructions, lead to better brain alignment and effectively capture instruction-specific representations. To address this, we first investigate brain alignment, i.e., measuring the degree of predictivity of neural visual activity using text output response embeddings from MLLMs as participants engage in watching natural scenes. Experiments with 10 different instructions show that MLLMs exhibit significantly better brain alignment than vision-only models and perform comparably to non-instruction-tuned multimodal models like CLIP. We also find that while these MLLMs are effective at generating high-quality responses suitable to the task-specific instructions, not all instructions are relevant for brain alignment. Further, by varying instructions, we make the MLLMs encode instruction-specific visual concepts related to the input image. This analysis shows that MLLMs effectively capture count-related and recognition-related concepts, demonstrating strong alignment with brain activity. Notably, the majority of the explained variance of the brain encoding models is shared between MLLM embeddings of image captioning and other instructions. These results suggest that enhancing MLLMs' ability to capture task-specific information could lead to better differentiation between various types of instructions, and thereby improving their precision in predicting brain responses.
