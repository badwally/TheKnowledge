---
schema_version: 1
type: moc
slug: convergent-ai-brain
domain: convergent-ai-brain
last_updated: '2026-06-02T01:01:17Z'
draft: true
draft_started_at: '2026-06-02T01:01:17Z'
draft_unresolved_claims: 21
---
# convergent-ai-brain — Map of Content

## Overview

Auto-generated from the corpus-constructive research loop. Anchored on the most recent `wiki research` run.

## Key entities

- [[sources/pubmed-33234544]] — Correspondence between Monkey Visual Cortices and Layers of a Saliency Map Model Based on a Deep Convolutional Neural Network for Representations of Natural Images.
- [[sources/pubmed-25521294]] — Deep neural networks rival the representation of primate IT cortex for core visual object recognition.
- [[sources/arxiv-2603.00793]] — Neural Functional Alignment Space: Brain-Referenced Representation of Artificial Neural Networks
- [[sources/arxiv-2307.10246]] — Deep Neural Networks and Brain Alignment: Brain Encoding and Decoding (Survey)
- [[sources/pubmed-34272948]] — Diverse Deep Neural Networks All Predict Human Inferior Temporal Cortex Well, After Training and Fitting
- [[sources/arxiv-2310.13018]] — Getting aligned on representational alignment
- [[sources/web-2010-07-01-6fa]] — Scaling laws for language encoding models in fMRI - PMC - NIH
- [[sources/web-2025-01-22-a81]] — Multi-modal brain encoding models for multi-modal stimuli
- [[sources/web-2024-04-24-a8b]] — Achieving more human brain-like vision via human EEG ...
- [[sources/web-2026-02-20-ed0]] — Achieving more human brain-like vision via human EEG ...

## Key concepts

- **Alignment Ceilings and Normalization Metrics** — The theoretical and empirical upper bounds for brain-model alignment are dictated by the inherent noise and reliability of biological data. Researchers use these limits to establish how close artificial systems are to perfectly matching human neural activity.
  - Noise-Ceiling Estimation and Normalization: In the Natural Scenes Dataset, the **within-subject noise ceiling for the occipitotemporal cortex (OTC) is approximately $r = 0.8$**, which represents the maximum possible similarity score given the inherent variability in fMRI measurements [1, 2]., Because all neural recordings contain noise, researchers must **normalize model alignment scores by dividing the raw predictivity by this estimated noise ceiling** to understand true representational correspondence [3, 4].
  - Empirical Saturation Near the Ceiling: In a large-scale evaluation of artificial vision systems, **126 different vision models achieved voxel-encoding RSA (veRSA) scores within $r=0.1$ of the human visual noise ceiling**, indicating they are brushing against the maximum possible predictivity [2, 5].
  - Brain-Brain Reliability as an Alignment Gate: The L-PACT framework evaluates "reliability-bounded adequacy" by strictly testing whether **model evidence can approach the actual variability observed among different brain measurements** (e.g., split-half or run-to-run reliability) [4, 6].
- **Mutual-Information Bounds and Convergence Limits** — The Platonic Representation Hypothesis explores the mathematical drivers pushing divergent AI models toward a shared representational space with biological brains, alongside the modality-specific limitations bounding this convergence.
  - Convergence to Pointwise Mutual Information (PMI): When trained via contrastive learning, representations converge to the **Pointwise Mutual Information (PMI) of the underlying latent causes of the environment** [7, 8]., Empirical tests demonstrate that calculating the **PMI over pixel colors recovers a representational kernel that closely matches human color perception** as well as the color kernels learned by text-only large language models [9, 10].
  - Modality-Specific Information Loss: Cross-system alignment is bounded by **ineffable visual experiences, such as witnessing a total solar eclipse**, which cannot be perfectly or entirely translated into text [11]., Highly **abstract verbal concepts, such as "freedom of speech," lack a direct visual equivalent**, preventing a perfect bijective mapping between vision models and language models [12].
- **The Role of Model Scale in Alignment** — The relationship between increasing model parameters and representational alignment with the brain differs significantly depending on the modality being modeled.
  - Scaling Laws in Language Models: Studies reveal a **strong scaling law where alignment with human fMRI and regressive eye-tracking patterns consistently improves as LLMs increase from 774M to 65B parameters**, showing no apparent diminishing returns [13-15]., Research notes a **near-perfect positive correlation ($r = 0.95$) between an LLM's parameter scale and its brain alignment score** [16].
  - Scale Saturation and Divergence in Vision Models: **Scaling up total trainable parameters in vision models produces a significant decrease in classical RSA alignment**, accompanied by only a non-significant bump in feature-reweighted (veRSA) alignment [17]., Geometric properties like **effective dimensionality and ImageNet classification accuracy act as weak or null predictors** of brain alignment across fully trained vision models [18, 19].
- **Architectural and Objective Inductive Biases** — Specific model design choices, training data diets, and learning objectives dictate the degree to which models replicate brain-like processing.
  - Visual Training Diet vs. Architecture: Architectures as different as **Convolutional Networks (CNNs) and Vision Transformers (ViTs) achieve near-equivalent brain predictivity** when trained on the exact same data and task [20, 21]., Models trained on **impoverished visual diets (e.g., exclusively indoor scenes or exclusively faces) suffer massive brain-alignment penalties** compared to models exposed to diverse sets like ImageNet [22-24].
  - Conflicting Evidence on Instruction-Tuning: One study argues **instruction-tuning enhances brain alignment by roughly 6%** because it improves the model's encoding of world knowledge and reasoning [16, 25]., A conflicting study found **no significant difference between base and instruction-tuned LLMs of matching sizes in brain-encoding during naturalistic reading**, arguing that scale is the true driver of alignment [13, 26].
  - Multimodal Integration: **Multimodal models jointly pre-trained on video and audio exhibit significantly improved alignment in human language and high-level visual brain regions** compared to unimodal models, indicating that the brain processes integrated information beyond unimodal capabilities [27, 28].
- **The Persistent Gap Between Best Models and Brain Data** — Current alignment metrics frequently mask fundamental structural and mechanistic divergences between AI representations and the brain's native geometry.
  - Flexibility of Feature Reweighting: When evaluated with strict classical RSA, vision models explain only ~31% of brain variance, but **after applying linear feature reweighting (veRSA), explainable variance artificially jumps to nearly 80%** [29-31].
  - Lack of Structural and Mechanistic Alignment: Under the strict L-PACT evaluation framework, **apparent positive brain-model correspondences are entirely explained away by severe controls**, such as temporal shifts and lexical autocorrelations [32, 33]., In rigorous testing, **no tested language model passed the gates for true relational profile alignment or mechanism-specific necessity** when counterfactually stripped of specific properties [34-36].
  - The Need for Explicit Biological Grounding: The **ReAlnet framework bridges this gap by directly optimizing representations using noninvasive human EEG signals** combined with contrastive learning, enabling the model to learn specific human-like temporal dynamics [37-39]., This explicit neural alignment allows models to **capture specific object dimension refinements (e.g., electronic/technology-related or long-thin shapes) that pure image-training diets fail to naturally capture** [40, 41].

## Synthesis pages

_(populated as `wiki research` and `wiki query` runs file syntheses)_
