---
schema_version: 1
type: moc
slug: ai-temporal-video
title: ai-temporal-video — Map of Content
domain: ai-temporal-video
created_at: '2026-06-18T19:05:29Z'
last_updated: '2026-06-18T19:05:29Z'
draft: true
draft_started_at: '2026-06-18T19:05:29Z'
---
## Overview

`ai-temporal-video` covers AI methods for **temporal understanding of video** —
recognizing, localizing, grounding, tracking, and reasoning about actions, events,
and objects as they unfold over time. It explicitly excludes video *generation*
(text-to-video, diffusion), static single-image understanding, and text-only
temporal reasoning.

The corpus is 86 YouTube sources — predominantly conference-paper walkthroughs
(CVPR/ECCV/WACV/ICCV/NeurIPS) and workshop/lecture talks — synced to the domain's
NotebookLM notebook for corpus synthesis. Backbone methods span 3D CNNs,
temporal/spatio-temporal transformers, graph networks (ST-GCN, ST-GNN), recurrent
models (LSTM), and recent video-LLMs for long-horizon reasoning.

## Synthesis pages

**Cross-cutting**
- [[synthesis/2026-06-18-what-are-the-dominant-method-families]] — dominant method
  families across the four tasks and how their shared temporal-modeling mechanisms
  evolved toward long-horizon, language-grounded understanding (corpus-grounded, 27 sources)
- [[synthesis/shared-architectures]] — backbone mechanisms recurring across tasks
- [[synthesis/recurring-trade-offs]] — speed/accuracy and locality/context trade-offs
- [[synthesis/common-datasets]] — benchmark datasets across the sub-areas

**By task**
- [[synthesis/temporal-action-detection-in-video-methods]] — TAD methods, benchmarks (ActivityNet, THUMOS), SOTA
- [[synthesis/video-language-understanding-and-grounding-cross]] — cross-modal alignment, VQA, text-conditioned localization
- [[synthesis/video-object-tracking-and-trajectory-prediction]] — MOT, motion modeling, cross-frame prediction
- [[synthesis/long-form-video-understanding-reasoning-across]] — reasoning across extended time, beyond-clip context

## Key entities

None yet — this domain's corpus is method/paper walkthroughs; entity pages (named
people, organizations) have not been authored.

## Key concepts

**Temporal action detection & localization**
- [[concepts/g-tad-sub-graph-localization]]
- [[concepts/gcan-graph-based-class-level-attention-network]]
- [[concepts/graph-based-localization]]
- [[concepts/self-feedback-detr]]
- [[concepts/tridet-relative-boundary-modeling]]
- [[concepts/transformer-and-attention-based-detectors]]
- [[concepts/boundary-refinement-and-post-processing]]
- [[concepts/gaussian-approximated-post-processing-gap]]
- [[concepts/temporal-aware-embedding-network-taen]]

**Video grounding & video-language**
- [[concepts/spatio-temporal-video-grounding]]
- [[concepts/tubedetr]]
- [[concepts/text-visual-prompting-tvp]]
- [[concepts/collaborative-static-and-dynamic-vision-language-streams]]
- [[concepts/large-vision-language-models-vlms]]
- [[concepts/video-captioning-and-question-answering]]
- [[concepts/iperceive-common-sense-reasoning-architecture]]
- [[concepts/multimodal-pretraining-via-masked-sequence-to-sequence-mass]]
- [[concepts/molmo2-open-weights-video-grounding]]
- [[concepts/revisionllm-recursive-vlm-for-hour-long-videos]]
- [[concepts/videochat-r1-reinforcement-fine-tuning-with-grpo]]

**Tracking & trajectory prediction**
- [[concepts/multi-object-tracking-mot]]
- [[concepts/transmot-spatial-temporal-graph-transformer]]
- [[concepts/tubetk-bounding-tube-regression]]
- [[concepts/fairmot-joint-detection-and-re-id-via-centernet]]
- [[concepts/recurrent-autoregressive-networks-ran]]
- [[concepts/trajectory-and-movement-forecasting]]
- [[concepts/graphtcn-graph-attention-with-temporal-convolutional-networks]]
- [[concepts/object-level-warping-loss-for-cell-tracking]]
- [[concepts/autotrack-spatio-temporal-regularization-for-uavs]]
- [[concepts/specialized-domain-tracking]]

**Action recognition & temporal backbones**
- [[concepts/3d-cnns-with-spatio-temporal-filter-analysis-i3d-resnet]]
- [[concepts/spatial-temporal-graph-convolutional-networks-st-gcn]]
- [[concepts/spatio-temporal-relation-modeling-strm]]
- [[concepts/convolutional-and-recurrent-architectures]]
- [[concepts/videolstm-convolutional-attention-lstm]]
- [[concepts/recurrent-pose-attention-network-rpan]]
- [[concepts/skeleton-based-and-pose-guided-methods]]
- [[concepts/few-shot-and-unsupervised-learning]]
- [[concepts/video-playback-rate-perception-prp]]
- [[concepts/motion-vector-flow-instance-mvfi-with-pca-lda]]
- [[concepts/fourier-phase-correlation-with-log-polar-transformation]]
- [[concepts/signal-processing-and-stabilization]]

**Neuromorphic / spiking approaches**
- [[concepts/neucube-3d-brain-inspired-architecture]]
- [[concepts/spiking-neural-networks-snns]]
- [[concepts/spike-time-dependent-plasticity-stdp-learning]]

**Applied**
- [[concepts/yolov8-csrnet-hybrid-stampede-risk-prediction]]

## Open threads

- The 86 corpus sources are legacy-migration summaries (~60-word descriptions);
  full transcripts live NLM-side (fetched via URL at sync). Concept/synthesis pages
  are migration drafts authored before the NLM corpus existed.
- Concept pages carry empty `title` frontmatter (migration artifact) — a separate cleanup.
- NLM-synthesis drafts are not finalize-compatible yet (citations.py footnote-mapping gap).
- Fresh-discovery expansion beyond the 86 is gated behind any live YouTube-adapter session
  (shared adapter key).
