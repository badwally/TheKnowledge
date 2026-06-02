---
schema_version: 1
type: moc
slug: convergent-ai-brain
domain: convergent-ai-brain
last_updated: '2026-06-02T01:33:48Z'
draft: true
draft_started_at: '2026-06-02T01:33:48Z'
draft_unresolved_claims: 17
---
# convergent-ai-brain — Map of Content

## Overview

Auto-generated from the corpus-constructive research loop. Anchored on the most recent `wiki research` run.

## Key entities

- [[sources/pubmed-31103784]] — Variational Autoencoder: An Unsupervised Model for Encoding and Decoding fMRI Activity in Visual Cortex
- [[sources/web-2026-05-10-f09]] — Define–Align–Fuse: Dual-Stream EEG-Vision Alignment using Hierarchical CLIP Representation
- [[sources/pubmed-19528002]] — Predictive coding under the free-energy principle
- [[sources/web-2024-10-30-d27]] — Brain-Score | The MIT Siegel Family Quest for Intelligence
- [[sources/web-2026-01-31-ff3]] — Not Too Generative, Not Too Discriminative: The Human Alignment ...
- [[sources/web-2015-07-01-04f]] — The Platonic Representation Hypothesis - Phillip Isola
- [[sources/web-2025-09-16-a8c]] — Brain Image Decoding with Multi-Layer feature Fusion of CLIP - arXiv
- [[sources/web-2016-06-10-350]] — Comparison of deep neural networks to spatio-temporal cortical ...
- [[sources/web-2026-02-20-748]] — Achieving more human brain-like vision via human EEG ... - PMC - NIH
- [[sources/web-2017-01-01-d2f]] — BrainAlign: Leveraging EEG Foundation Models for Symmetric ...

## Key concepts

- **The Generative vs. Discriminative Trade-Off** — The sources investigate whether purely generative or purely discriminative training objectives produce more brain-like representations, revealing that neither extreme is optimal on its own.
  - The Human Alignment Sweet Spot: Purely discriminative training provides categorical structure, while generative training forces sensitivity to input structure; a balance of both maximizes alignment across benchmarks testing low-level perceptual similarity, uncertainty, and diagnostic features [1, 2]., While earlier studies suggested generative models excel at mid-level gloss perception, JEMs reveal that a purely discriminative objective actually outperforms a purely generative one when architecture is controlled, but a hybrid generative-discriminative objective surpasses both [3, 4]., Introducing generative pressure actively shifts models away from local texture cues and promotes global shape-based generalization, more closely matching human visual processing biases [5, 6].
  - Limitations of Pure Generative Objectives in Vision: Among the Taskonomy models, pure autoencoding (a generative task) yields the lowest overall brain-predictivity scores for human occipitotemporal cortex compared to discriminative object classification [7]., Variational Autoencoders (VAEs) predict fMRI video-evoked responses comparably to CNNs in early visual areas, but demonstrate relatively lower accuracy and representation matching in higher-order visual areas [8].
- **The Impact of Self-Supervised and Rich Predictive Targets** — The exact nature of self-supervised learning algorithms and the semantic richness of the predictive target strongly dictate a model's correspondence with biological neural data.
  - Contrastive vs. Non-Contrastive Self-Supervision: Self-supervised models utilizing instance-level contrastive learning (e.g., SimCLR, BarlowTwins) produce representations that match the brain-predictive capacity of category-supervised models [9, 10]., Non-contrastive self-supervised tasks, such as predicting image rotations, clustering, or unscrambling images (Jigsaw), yield visual representations that are significantly less predictive of human brain activity [9, 10].
  - Rich Semantic Targets vs. Discrete Classification: Recurrent Convolutional Neural Networks (RCNNs) trained to predict LLM embeddings of scene captions significantly outperform structurally identical models trained on discrete multi-hot object categories across high-level visual regions [11, 12]., The superior biological alignment of LLM embedding targets stems from their ability to integrate complex contextual relations and world knowledge across entire scene captions, outperforming isolated category words or noun/verb-only representations [13-15].
- **Next-Token Prediction vs. Instruction Tuning in Language** — In the language domain, cognitive plausibility is deeply tied to base predictive objectives and scale, rather than specialized fine-tuning for task execution.
  - The Primacy of Autoregressive Scaling: As autoregressive LLMs scale from 774 million to 65 billion parameters, their alignment with human eye-tracking and fMRI BOLD signals linearly improves without diminishing returns [16-18]., As models scale in size, their self-attention mechanisms exhibit reduced sensitivity to trivial patterns (e.g., focusing heavily on just the first or preceding word), contributing to greater cognitive plausibility [19].
  - The Ineffectiveness of Instruction Tuning for Brain Alignment: Regressing the self-attention of instruction-tuned models (e.g., Alpaca, Vicuna) against human eye movements and fMRI data reveals no significant alignment improvements over base predictive models of the exact same size [17, 18, 20]., Fine-tuned LLMs show a heightened sensitivity and representational divergence when processing specific instruction prompts—a behavior that does not correspond to naturalistic human reading mechanisms [21].
- **Inductive Biases: Objective vs. Architecture, Scale, and Data** — Different modalities exhibit fundamentally different primary drivers of brain-ANN alignment, with data diversity dominating vision and scale dominating language.
  - The Dominance of Data Diversity in Vision: A massive empirical comparison of 224 models demonstrated that variation across visual training diets exerts a much larger effect on brain predictivity than varying architectural motifs [22-25]., Highly constrained visual diets, such as training exclusively on faces (VGGFace2) or exclusively on indoor scenes (Taskonomy), lead to substantially lower capacity to predict responses in human occipitotemporal cortex [7, 24].
  - The Secondary Role of Architecture: Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) trained on the same data achieve near-equivalent brain predictivity scores [23]., While architecture alone (e.g., untrained networks with random weights) can induce some baseline similarity to the brain, training on ecologically relevant tasks is absolutely necessary to enforce a topographically ordered, hierarchical match with the brain's ventral and dorsal streams [26-28].
- **Direct Neural Alignment and Methodological Limitations** — Efforts to actively align AI with neural data face unique challenges related to evaluation methodologies and the interpretability of representational similarity metrics.
  - Actively Aligning Models to Biological Data: The ReAlnet and BrainAlign frameworks explicitly optimize deep neural networks using human EEG data via multi-layer encoding and contrastive learning objectives [29-31]., Vision models actively aligned with individual human EEG patterns generalize remarkably well, showing enhanced similarity across other neuroimaging modalities (fMRI) and capturing distinct behavioral features like food and electronic-related representations [32-34].
  - The Identifiability Trade-Off in Model Evaluation: Large-scale model recovery simulations using the THINGS odd-one-out behavioral dataset demonstrate that flexible linear probing frequently fails to identify the true data-generating model, plateauing below 80% accuracy even with millions of trials [35, 36]., Flexible alignment metrics induce substantial shifts in representational geometry and inflate effective dimensionality, creating a sharp trade-off where increasing apparent predictive accuracy diminishes the true identifiability of the model [37-39].

## Synthesis pages

_(populated as `wiki research` and `wiki query` runs file syntheses)_
