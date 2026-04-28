---
id: arxiv-2104.03042
type: arxiv
title: On-device Federated Learning with Flower
url: http://arxiv.org/abs/2104.03042v1
authors:
- Akhil Mathur
- Daniel J. Beutel
- Pedro Porto Buarque de Gusmão
- Javier Fernandez-Marques
- Taner Topal
- Xinchi Qiu
- Titouan Parcollet
- Yan Gao
- Nicholas D. Lane
ingested_at: '2026-04-28T15:31:58Z'
content_hash: sha256:cc536cbd51971874ee08cf058b97a133cf7b336843a0a72b1a141c47e940a3a8
domains:
- edge-ai-agentic
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: legacy-research-notebook
  legacy_recovery: summary-only
legacy_provenance:
  imported_at: '2026-04-28T15:31:58Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian_edge_ai/sources/arxiv_2104.03042.md
  legacy_slug: arxiv_2104.03042
published_at: '2021-04-07'
filter:
  score: 0.8
  policy_version: edge-ai-agentic-legacy-v1
  rationale: (legacy filter score)
  decided_at: '2026-04-28T15:31:58Z'
  user_correction: null
---
_(legacy import — body is the original summary; full source content is not re-fetched in v1)_

# On-device Federated Learning with Flower

**Authors:** Akhil Mathur, Daniel J. Beutel, Pedro Porto Buarque de Gusmão, Javier Fernandez-Marques, Taner Topal, Xinchi Qiu, Titouan Parcollet, Yan Gao, Nicholas D. Lane  
**Published:** 2021-04-07T10:42:14Z  
**Venue:** On-device Intelligence Workshop at the Fourth Conference on Machine Learning and Systems (MLSys), April 9, 2021  
**PDF:** http://arxiv.org/pdf/2104.03042v1.pdf

## Abstract

Federated Learning (FL) allows edge devices to collaboratively learn a shared prediction model while keeping their training data on the device, thereby decoupling the ability to do machine learning from the need to store data in the cloud. Despite the algorithmic advancements in FL, the support for on-device training of FL algorithms on edge devices remains poor. In this paper, we present an exploration of on-device FL on various smartphones and embedded devices using the Flower framework. We also evaluate the system costs of on-device FL and discuss how this quantification could be used to design more efficient FL algorithms.

## Relevance

**Score:** 4/5  
Demonstrates on-device federated learning on smartphones and embedded devices using the Flower framework, evaluating system costs (memory, compute, battery) on real hardware. Published at MLSys On-device Intelligence Workshop 2021 — directly addresses on-device training for edge FL with concrete hardware benchmarks.
