---
id: arxiv-2404.13990
type: arxiv
title: 'QCore: Data-Efficient, On-Device Continual Calibration for Quantized Models
  -- Extended Version'
url: https://arxiv.org/abs/2404.13990
authors:
- David Campos
- Bin Yang
- Tung Kieu
- Miao Zhang
- Chenjuan Guo
- Christian S. Jensen
ingested_at: '2026-04-30T16:39:51Z'
content_hash: sha256:77b25c99c448dfb63a943107e5e0f76026618dcdd2b8cb5856ff95242493a3f7
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2404.13990'
  categories:
  - cs.LG
  - cs.DB
  doi: 10.14778/3681954.3681957
  primary_category: cs.LG
  journal_ref: Proceedings of the VLDB Endowment, 17, 11 (2024), 2708-2721
  comment: '15 pages. An extended version of "QCore: Data-Efficient, On-Device Continual
    Calibration for Quantized Models" accepted at PVLDB 2024'
  abstract_only: true
published_at: '2024-04-22'
---
We are witnessing an increasing availability of streaming data that may contain valuable information on the underlying processes. It is thus attractive to be able to deploy machine learning models on edge devices near sensors such that decisions can be made instantaneously, rather than first having to transmit incoming data to servers. To enable deployment on edge devices with limited storage and computational capabilities, the full-precision parameters in standard models can be quantized to use fewer bits. The resulting quantized models are then calibrated using back-propagation and full training data to ensure accuracy. This one-time calibration works for deployments in static environments. However, model deployment in dynamic edge environments call for continual calibration to adaptively adjust quantized models to fit new incoming data, which may have different distributions. The first difficulty in enabling continual calibration on the edge is that the full training data may be too large and thus not always available on edge devices. The second difficulty is that the use of back-propagation on the edge for repeated calibration is too expensive. We propose QCore to enable continual calibration on the edge. First, it compresses the full training data into a small subset to enable effective calibration of quantized models with different bit-widths. We also propose means of updating the subset when new streaming data arrives to reflect changes in the environment, while not forgetting earlier training data. Second, we propose a small bit-flipping network that works with the subset to update quantized model parameters, thus enabling efficient continual calibration without back-propagation. An experimental study, conducted with real-world data in a continual learning setting, offers insight into the properties of QCore and shows that it is capable of outperforming strong baseline methods.
