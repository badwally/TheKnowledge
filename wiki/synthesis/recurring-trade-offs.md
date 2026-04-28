---
type: synthesis
slug: recurring-trade-offs
title: Recurring Trade Offs
domains:
- ai-temporal-video
question: '(legacy synthesis: recurring-trade-offs)'
draft: true
draft_started_at: '2026-04-28T15:21:51Z'
legacy_provenance:
  imported_at: '2026-04-28T15:21:51Z'
  legacy_path: /Users/andrewgrant/code/research-notebook/data/obsidian/synthesis/recurring-trade-offs.md
  legacy_slug: recurring-trade-offs
---

# Recurring Trade-offs

*Cross-cutting analysis across all research branches.*

## Related Branches

- [[mocs/action-recognition-classification|Action Recognition & Classification]]
- [[mocs/temporal-action-detection-localization|Temporal Action Detection & Localization]]
- [[mocs/video-object-tracking-trajectory-prediction|Video Object Tracking & Trajectory Prediction]]
- [[mocs/video-language-understanding-grounding|Video-Language Understanding & Grounding]]
- [[mocs/biologically-inspired-advanced-spatio-temporal-computing|Biologically Inspired & Advanced Spatio-Temporal Computing]]

## Analysis

**Accuracy vs. Computational Efficiency**
*   **Transformers vs. Linear Models:** In temporal action detection, Transformers achieve state-of-the-art accuracy by capturing long-range dependencies across distant frames, but they suffer from a quadratic computational cost that slows them down drastically on long, untrimmed videos [1, 2]. To trade a negligible amount of accuracy for massive efficiency gains, architectures like **MS-Tamba** utilize Mamba (State Space Models) to achieve linear complexity, matching or exceeding Transformer performance with significantly fewer resources [3, 4].
*   **Knowledge Distillation:** In multi-object tracking, large models are accurate but slow, while small models are fast but fail to detect distant or occluded objects [5]. **AttTrack** balances this by training a heavy "teacher" model to process only keyframes accurately, and transferring its attention heatmaps to a lightweight "student" model that efficiently tracks interim frames using simple linear kinematics [5]. 
*   **Filter Design in 3D CNNs:** 3D CNNs are notoriously parameter-heavy and data-hungry [6]. Researchers found that using standard 3-frame filters everywhere wastes compute; by placing 1-frame filters in shallow layers (which only extract static appearance) and progressively enlarging filters up to 5 frames in deep layers, models can simultaneously improve classification accuracy and reduce computational costs [7-9].

**Local Temporal Modeling vs. Global Temporal Modeling**
*   **Temporal Action Detection Boundaries:** Models must balance capturing the broad context of an action (global) with identifying its exact start and end points (local). Segment-level prediction captures great global context but ignores fine instant-level details, while instant-level prediction misses the relationship between adjacent instances [10, 11]. **TriDet** resolves this trade-off using a "Trident head," combining a start boundary branch with a center offset branch to evaluate relative probability within a local bin set [11]. 
*   **Video-Language Grounding:** To solve grounding efficiently, **TubeDETR** splits its architecture into two branches: a "slow" multi-modal branch that sparsely samples frames to model deep global spatial-linguistic interactions, and a "fast" visual-only branch that preserves the full frame rate to recover local temporal cues without using heavy attention layers [12, 13].
*   **Action Recognition:** Relying on short clips captures local motion but misses the plot, while looking at the whole video makes modeling raw motion difficult. **Temporal Difference Networks (TDN)** integrate both by using Eulerian motion (simple differences): they use raw RGB image differences to capture local, low-level motion, and CNN feature differences to capture global, high-level temporal relations across frames that are further apart [14, 15].

**Supervised vs. Self-Supervised/Weakly-Supervised Approaches**
*   **Annotation Cost vs. Precision:** Fully supervised temporal action localization models require exact frame-by-frame boundaries, which are prohibitively expensive to annotate and impossible to scale to every real-world category [16, 17]. To avoid this, weakly supervised models like **METAL** trade explicit boundary data for scalability, relying only on video-level labels and Similarity Pyramid Networks to competitively localize unseen activities [16]. Similarly, an unsupervised approach utilizes spectral clustering to generate pseudo-labels, trading away human precision to operate without any boundary or class annotations [18, 19].
*   **Data Generation:** Open-weight Vision-Language Models (VLMs) often trade true open science for easy data by distilling proprietary models like GPT-4, which inherently limits them to the teacher's capability ceiling [20-22]. **Molmo2** refuses this trade-off, investing in highly expensive, painstaking human annotation for its "Video Point" dataset, resulting in superior spatial-temporal grounding that beats distilled models [23-25].
*   **Representation Learning:** **ActionFlowNet** trades the accuracy of models pre-trained on massive supervised datasets (like ImageNet or Kinetics) for a self-supervised approach, learning motion representations by jointly predicting optical flow and actions directly from raw pixels [26, 27].

**Model Complexity vs. Generalization**
*   **Catastrophic Forgetting in VLMs:** When a complex VLM like **Molmo2** is heavily fine-tuned specifically to track visual pixels and output precise spatial coordinates, the gradients pull the network weights in conflicting directions [28]. This creates a trade-off where the model achieves state-of-the-art grounding but suffers "catastrophic forgetting," degrading its generalization capabilities in general NLP tasks like Python coding [28].
*   **Observational Bias:** Complex models often "cheat" by memorizing dataset-specific contexts rather than generalizing. If a model only sees a keyboard and mouse on a desk, it will generalize poorly and fail to recognize them in a novel environment [29]. **iPerceive** forces the model to learn true causal relationships using "do-calculus" and a common-sense reasoning loss, trading simpler pattern-matching for robust generalization against cognitive errors [29, 30].
*   **Zero-Shot Training-Free Generalization:** Highly tuned models frequently suffer performance drops in out-of-distribution (OOD) settings [31]. A **training-free grounding method** trades the precision of a fine-tuned model for the broad generalizability of frozen LLMs and VLMs [31]. By explicitly prompting the LLM to score "dynamic transitions" and "static states," it achieves better zero-shot generalization on complex multi-event videos than some fully supervised methods [32-34].

**Real-Time Capability vs. Offline Accuracy**
*   **Access to Future Frames:** In video detection, offline systems have the luxury of using both past and future frames to analyze an action's context, yielding high accuracy [35]. Real-time (online) systems are blind to the future and must predict immediately using only past frames, naturally leading to a degradation in accuracy [35, 36]. 
*   **Mitigating the Real-Time Penalty:** The **A\* (Atrous Spatial Temporal Action Recognition)** architecture minimizes this online performance degradation [37]. Built on a fast YOLO-based network, it uses an Atrous Spatial Temporal Pyramid Pooling (ASPP) module to capture global situational context strictly from past frames, and employs proxy-anchor contrastive learning to successfully distinguish highly confusing, opposing actions (like standing vs. sitting) in real-time [38, 39]. 
*   **Online Multi-Object Tracking:** Similar to action detection, tracking models struggle when objects disappear in real-time without future frames to confirm their trajectory [40]. **Recurrent Autoregressive Networks (RAN)** compensate for this by coupling an internal memory (RNN hidden layer) with an external memory template [40]. If a tracked object is occluded in real-time, the model shifts its autoregressive weights to older tracking history to predict the object's future appearance and motion, achieving state-of-the-art online tracking accuracy [40, 41].

## Synthesis

_(needs population from legacy import)_

## Sources cited

_(needs population from legacy import)_
