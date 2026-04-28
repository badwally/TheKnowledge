---
id: arxiv-2505.19147
type: arxiv
title: Shifting AI Efficiency From Model-Centric to Data-Centric Compression
url: http://arxiv.org/abs/2505.19147v3
authors:
- Xuyang Liu
- Zichen Wen
- Shaobo Wang
- Junjie Chen
- Zhishan Tao
- Yubo Wang
- Tailai Chen
- Xiangqi Jin
- Chang Zou
- Yiyu Wang
- Chenfei Liao
- Xu Zheng
- Honggang Chen
- Weijia Li
- Xuming Hu
- Conghui He
- Linfeng Zhang
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:3fe7698e207f7d252f0d5eebfda2fb29f98571cc8c005d0f971ca828f96461d3
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2505.19147.md
  legacy_slug: arxiv_2505.19147
published_at: '2025-05-25'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# Shifting AI Efficiency From Model-Centric to Data-Centric Compression

**Authors:** Xuyang Liu, Zichen Wen, Shaobo Wang, Junjie Chen, Zhishan Tao, Yubo Wang, Tailai Chen, Xiangqi Jin, Chang Zou, Yiyu Wang, Chenfei Liao, Xu Zheng, Honggang Chen, Weijia Li, Xuming Hu, Conghui He, Linfeng Zhang  
**Published:** 2025-05-25T13:51:17Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2505.19147v3.pdf

## Abstract

The advancement of large language models (LLMs) and multi-modal LLMs (MLLMs) has historically relied on scaling model parameters. However, as hardware limits constrain further model growth, the primary computational bottleneck has shifted to the quadratic cost of self-attention over increasingly long sequences by ultra-long text contexts, high-resolution images, and extended videos. In this position paper, \textbf{we argue that the focus of research for efficient artificial intelligence (AI) is shifting from model-centric compression to data-centric compression}. We position data-centric compression as the emerging paradigm, which improves AI efficiency by directly compressing the volume of data processed during model training or inference. To formalize this shift, we establish a unified framework for existing efficiency strategies and demonstrate why it constitutes a crucial paradigm change for long-context AI. We then systematically review the landscape of data-centric compression...

## Relevance

**Score:** 3/5  
Position paper arguing for data-centric (input/context) compression over model-centric compression to address quadratic attention costs; directly applicable to reducing inference overhead in edge-deployed long-context agents.
