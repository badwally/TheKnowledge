---
schema_version: 1
type: synthesis
slug: 2026-06-18-what-sets-the-ceiling-on-representational
title: What sets the ceiling on representational alignment between biological brains
  and artificial neural networks? Examine reported alignment ceilings and noise-ceiling
  normalization, mutual-information bounds on cross-system alignment, the persistent
  gap between the best models and brain data, whether alignment saturates with model
  scale, and which architectural or objective differences prevent full convergence.
domains:
- convergent-ai-brain
question: What sets the ceiling on representational alignment between biological brains
  and artificial neural networks? Examine reported alignment ceilings and noise-ceiling
  normalization, mutual-information bounds on cross-system alignment, the persistent
  gap between the best models and brain data, whether alignment saturates with model
  scale, and which architectural or objective differences prevent full convergence.
created_at: '2026-06-18T18:06:07Z'
last_updated: '2026-06-18T18:06:07Z'
sources_count: 14
nlm_notebook_id: 0997b925-a7b2-47d2-8dcc-e11fcecf953e
draft: true
draft_started_at: '2026-06-18T18:06:07Z'
draft_unresolved_claims: 15
---
# What sets the ceiling on representational alignment between biological brains and artificial neural networks? Examine reported alignment ceilings and noise-ceiling normalization, mutual-information bounds on cross-system alignment, the persistent gap between the best models and brain data, whether alignment saturates with model scale, and which architectural or objective differences prevent full convergence.

## Synthesis

**The ceiling on representational alignment between biological brains and artificial neural networks (ANNs) is constrained by a combination of inherent measurement noise, the limitations of model scaling, the divergence of training objectives, and theoretical bounds on shared information.** 

**Reported Alignment Ceilings and Noise-Ceiling Normalization**
Because neural measurements contain trial-to-trial noise and subject-level variability, a "noise ceiling" is used to estimate the maximum possible performance any true model could theoretically achieve [1, 2]. To isolate a model's true alignment from the constraints of data quality, alignment metrics are routinely normalized against this ceiling (e.g., dividing predictivity by the extrapolated reliability of the dataset) [3-5]. While some highly optimized models have achieved global similarity scores within $r=0.1$ of the high noise ceiling (which sits around $r=0.8$) for human occipitotemporal cortex [6, 7], this impressive global fit masks deeper functional discrepancies.

**The Persistent Gap Between the Best Models and Brain Data**
Even the most advanced brain-optimized encoding models leave significant portions of variance unexplained, capturing at most 78%—and sometimes as little as 37%—of the explainable variance in visual areas [8] [[sources/web-2023-06-07-3e0]]. Furthermore, **as deep neural networks have achieved state-of-the-art accuracy on tasks like ImageNet, they have paradoxically evolved into worse models of the primate inferotemporal (IT) visual cortex** [9-11]. This persistent gap is temporally and semantically structured. While DNNs successfully predict lower-level visual processing immediately after stimulus onset, they fail to account for the dynamic unfolding of higher-level visuo-semantic features (such as object parts and basic categories) that drive human brain activity milliseconds later [12-14].

**Mutual-Information Bounds on Cross-System Alignment**
Theoretical frameworks like the "Platonic Representation Hypothesis" propose that diverse models converge onto a shared statistical model of reality, where the optimal representational similarity kernel equals the pointwise mutual information (PMI) of the underlying generative events in the world [15, 16]. However, **cross-system alignment is theoretically bounded by the unique information contained in different modalities** [17, 18]. Because independent modalities contain unshared, unique signals (e.g., visual details ineffable in text), there is a mathematical cap on the maximum representational alignment that can be achieved between neural systems and artificial models processing fundamentally different sensory streams [18, 19]. 

**Saturation of Alignment with Model Scale**
In the language domain, alignment to brain activity demonstrates a distinct scaling law, improving as models grow from millions to billions of parameters (e.g., up to 65 billion) [20-22]. However, this is not an infinite trajectory: **model-brain alignment follows a logarithmic curve of diminishing returns**, where massive task-performance gains eventually yield only fractional alignment improvements [23, 24]. Regional brain analyses reveal that encoding performance plateaus in certain language areas once models reach around 13 billion parameters [25, 26]. For vision models, merely increasing the parameter count without radically diversifying the training data has no consistent, positive influence on brain predictivity, proving that scaling alone cannot force convergence [27-29].

**Architectural and Objective Differences Preventing Full Convergence**
Full representational convergence is ultimately prevented by several structural and algorithmic deviations from biology:
*   **The Generative–Discriminative Trade-off:** Standard AI models are typically optimized for pure discriminative categorization (e.g., object recognition), which distorts representational geometry away from biological norms [30, 31]. **Human alignment is maximized not at either extreme of generative or discriminative learning, but at a "sweet spot" that integrates both** [32-34]. Hybrid objectives better align with human uncertainty, shape-texture biases, and diagnostic feature attribution.
*   **Lack of Recurrent Dynamics:** Standard feedforward ANNs lack the recurrent signal flow and feedback loops characteristic of biological brains [35] [[sources/yt-tyYIuvbV2po]]. Without recurrence, ANNs fail to accurately predict the temporal dynamics of biological vision, particularly the neural activity that churns roughly 30 milliseconds after initial feedforward processing to resolve complex visual ambiguity [36, 37].
*   **Visual Diet:** Biological brains learn from a rich, continuous ecological environment, whereas ANNs are heavily constrained by their training datasets. Tightly constrained image diets limit alignment, but exposing models to massive, diverse datasets or explicitly fine-tuning them on human behavioral judgments (neural harmonization) dramatically improves their correspondence to the brain [10, 38, 39].

## Sources cited

- [[sources/yt-tyYIuvbV2po]]
- [[sources/web-2024-10-30-e9d]]
- [[sources/web-2023-08-23-16e]]
- [[sources/yt-eAstJe16ZUI]]
- [[sources/web-2023-06-07-3e0]]
- [[sources/web-2023-11-02-f24]]
- [[nlm:9c40b2b4-a687-4ca1-9086-d4a68bd7dd05]]
- [[sources/web-2015-07-01-04f]]
- [[sources/yt-0W-cRw-EBAc]]
- [[sources/web-2025-09-16-c0d]]
- [[sources/web-2013-05-20-a5c]]
- [[sources/web-2024-10-22-8f4]]
- [[sources/web-2026-01-31-ff3]]
- [[sources/yt-5kq7M6pcQ5g]]
