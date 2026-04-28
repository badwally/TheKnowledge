---
id: arxiv-2509.16989
type: arxiv
title: 'PTQTP: Post-Training Quantization to Trit-Planes for Large Language Models'
url: http://arxiv.org/abs/2509.16989v3
authors:
- He Xiao
- Runming Yang
- Qingyao Yang
- Wendong Xu
- Zhen Li
- Yupeng Su
- Zhengwu Liu
- Hongxia Yang
- Ngai Wong
ingested_at: '2026-04-28T15:31:59Z'
content_hash: sha256:d16aa6ea46da19f107ca5cf0a4a9f733f7cc6bfb81909dc6ee1a4088363b4b13
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:59Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2509.16989.md
  legacy_slug: arxiv_2509.16989
published_at: '2025-09-21'
filter:
  score: 0.6
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:59Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# PTQTP: Post-Training Quantization to Trit-Planes for Large Language Models

**Authors:** He Xiao, Runming Yang, Qingyao Yang, Wendong Xu, Zhen Li, Yupeng Su, Zhengwu Liu, Hongxia Yang, Ngai Wong  
**Published:** 2025-09-21T09:07:20Z  
**Venue:** Preprint  
**PDF:** http://arxiv.org/pdf/2509.16989v3.pdf

## Abstract

Post-training quantization (PTQ) of large language models (LLMs) to extremely low bit-widths remains challenging due to the fundamental trade-off between computational efficiency and representational capacity. While existing ultra-low-bit methods rely on binary approximations or quantization-aware training(QAT), they often suffer from either limited representational capacity or huge training resource overhead. We introduce PTQ to Trit-Planes (PTQTP), a structured PTQ framework that decomposes weight matrices into dual ternary {-1, 0, 1} trit-planes. This approach achieves multiplication-free additive inference by decoupling weights into discrete topology (trit-planes) and continuous magnitude (scales), effectively enabling high-fidelity sparse approximation. PTQTP provides: (1) a theoretically grounded progressive approximation algorithm ensuring global weight consistency; (2) model-agnostic deployment without architectural modifications; and (3) uniform ternary operations that elim...

## Relevance

**Score:** 3/5  
PTQTP decomposes LLM weights into dual ternary planes enabling multiplication-free additive inference without architectural changes; enables constrained-hardware deployment but lacks explicit edge device benchmarks.
