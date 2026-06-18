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
created_at: '2026-06-18T19:53:00Z'
last_updated: '2026-06-18T19:53:17Z'
sources_count: 16
nlm_notebook_id: 0997b925-a7b2-47d2-8dcc-e11fcecf953e
finalized_at: '2026-06-18T19:53:17Z'
---
# What sets the ceiling on representational alignment between biological brains and artificial neural networks? Examine reported alignment ceilings and noise-ceiling normalization, mutual-information bounds on cross-system alignment, the persistent gap between the best models and brain data, whether alignment saturates with model scale, and which architectural or objective differences prevent full convergence.

## Synthesis

**The ceiling on representational alignment between biological brains and artificial neural networks (ANNs) is dictated by measurement noise constraints, theoretical limits of information sharing, the diminishing returns of scale, and fundamental algorithmic deviations in current AI architectures.**

**Reported Alignment Ceilings and Noise-Ceiling Normalization**
To quantify the true alignment between an ANN and a brain, researchers must account for the inherent trial-to-trial noise and inter-subject variability present in neuroimaging measurements (e.g., fMRI or EEG) [1] [[sources/web-2024-10-30-e9d]], [2] [[sources/web-2023-08-23-16e]]. A "noise ceiling" is calculated to estimate the maximum predictive performance any theoretical model could achieve given the data's reliability [1] [[sources/web-2024-10-30-e9d]], [2] [[sources/web-2023-08-23-16e]], [3] [[sources/web-2023-08-23-16e]]. Alignment metrics are normalized against this ceiling to isolate the model's true explanatory power [2] [[sources/web-2023-08-23-16e]], [3] [[sources/web-2023-08-23-16e]]. For example, in the human occipitotemporal cortex (OTC), the noise ceiling is highly reliable (around $r \approx 0.8$) [4] [[sources/web-2024-10-30-e9d]], [5] [[sources/web-2024-10-30-e9d]]. While some models achieve voxel-encoding predictivity scores within $r=0.1$ of this ceiling [6] [[sources/web-2024-10-30-e9d]], this highly inflated global similarity is heavily dependent on the chosen metric [7] [[sources/web-2024-10-30-e9d]], [8] [[sources/web-2024-10-30-e9d]]. When using strict Classical Representational Similarity Analysis (cRSA) without flexible feature re-weighting, the best models explain only about 31% of the variance, whereas flexible voxel-encoding RSA (veRSA) inflates this to nearly 80% [7] [[sources/web-2024-10-30-e9d]], [8] [[sources/web-2024-10-30-e9d]].

**The Persistent Gap Between the Best Models and Brain Data**
Despite advances, even models directly optimized to predict brain activity leave significant variance unexplained, capturing at most 78%—and sometimes as little as 37%—of the explainable variance in human visual areas [9] [[sources/web-2023-06-07-3e0]]. Crucially, **as modern DNNs have scaled to achieve state-of-the-art accuracy on computer vision benchmarks like ImageNet, they have paradoxically evolved into worse models of the primate inferotemporal (IT) cortex** [10] [[sources/web-2023-11-02-f24]], [11] [[sources/web-2023-11-02-f24]], [12] [[sources/web-2023-11-02-f24]]. This persistent gap is also highly structured in time. While DNNs excel at predicting early, lower-level visual representations around 66 milliseconds after stimulus onset, they systematically fail to capture higher-level cortical dynamics that unfold later (around 146 ms) [13] [[nlm:9c40b2b4-a687-4ca1-9086-d4a68bd7dd05]], [14] [[nlm:9c40b2b4-a687-4ca1-9086-d4a68bd7dd05]]. Instead, these later dynamics are best explained by visuo-semantic models that encode readily nameable object parts and basic categories, proving that standard DNNs and human brains rely on partially divergent features for recognition [13] [[nlm:9c40b2b4-a687-4ca1-9086-d4a68bd7dd05]], [15] [[nlm:9c40b2b4-a687-4ca1-9086-d4a68bd7dd05]], [14] [[nlm:9c40b2b4-a687-4ca1-9086-d4a68bd7dd05]].

**Mutual-Information Bounds on Cross-System Alignment**
Frameworks like the "Platonic Representation Hypothesis" propose that ANNs trained across different modalities and architectures converge on a shared statistical model of reality [16] [[sources/web-2015-07-01-04f]], [17] [[sources/web-2015-07-01-04f]]. However, **cross-system alignment is mathematically bounded by the unique information inherent to different modalities** [18] [[sources/yt-0W-cRw-EBAc]], [19] [[sources/yt-0W-cRw-EBAc]]. Because independent modalities carry unshared, unique signals (e.g., visual phenomena that are ineffable in text, or textual abstractions absent in images), there is a strict cap on the maximum representational alignment that can be achieved between models trained on different sensory streams [18] [[sources/yt-0W-cRw-EBAc]], [19] [[sources/yt-0W-cRw-EBAc]]. 

**Saturation of Alignment with Model Scale**
While scaling model parameters from millions to billions systematically improves their alignment with human brain representations, this trajectory follows a logarithmic curve of diminishing returns rather than infinite improvement [20] [[sources/web-2013-05-20-a5c]], [21] [[sources/web-2013-05-20-a5c]], [22] [[sources/web-2013-05-20-a5c]], [23] [[sources/web-2024-10-22-8f4]]. In the language domain, encoding performance predictably rises with model scale but eventually plateaus around 13 billion parameters for certain cortical regions, such as Brodmann area 45 (BA45) and the temporal pole [24] [[sources/web-2024-10-22-8f4]], [25] [[sources/web-2024-10-22-8f4]]. Furthermore, **instruction-tuning and fine-tuning do not meaningfully improve a model's brain or behavioral alignment beyond what base scaling achieves** [26] [[sources/web-2025-09-16-c0d]], [27] [[sources/web-2025-09-16-c0d]], [28] [[sources/web-2025-09-16-c0d]], even though these methods improve the model's world-knowledge representations and downstream task performance [29] [[sources/web-2024-07-10-57e]]. 

**Architectural and Objective Differences Preventing Full Convergence**
Full convergence between ANNs and biological brains is ultimately prevented by several key architectural and objective misalignments:
*   **The Generative–Discriminative Trade-off:** Standard AI models optimized purely for discriminative tasks (like ImageNet classification) distort representational geometry away from biological norms [30] [[sources/web-2026-01-31-ff3]], [31] [[sources/web-2026-01-31-ff3]]. Conversely, pure generative models lack necessary categorical structure [31] [[sources/web-2026-01-31-ff3]], [32] [[sources/web-2026-01-31-ff3]]. **The "human alignment sweet spot" consistently emerges in hybrid regimes** that balance generative world-modeling with discriminative categorization [30] [[sources/web-2026-01-31-ff3]], [33] [[sources/web-2026-01-31-ff3]], [34] [[sources/web-2026-01-31-ff3]], [35] [[sources/web-2026-01-31-ff3]].
*   **The Absence of Recurrent Dynamics:** Most standard DNNs are purely feedforward, lacking the dense recurrent circuits of biological cortices [36] [[sources/yt-5kq7M6pcQ5g]], [37] [[sources/yt-ysv2g9M3ong]], [38] [[sources/yt-ysv2g9M3ong]]. These missing feedback loops prevent ANNs from capturing the extra ~30 milliseconds of temporal "churning" that the primate brain utilizes to resolve complex, ambiguous visual recognition tasks [36] [[sources/yt-5kq7M6pcQ5g]], [39] [[sources/yt-5kq7M6pcQ5g]], [38] [[sources/yt-ysv2g9M3ong]].
*   **Suboptimal Visual Diets and Objectives:** The image diet provided to ANNs often lacks ecological validity [40] [[sources/web-2024-10-30-e9d]], [41] [[sources/web-2024-10-30-e9d]]. However, when deep recurrent convolutional networks are trained to map visual inputs directly to Large Language Model (LLM) embeddings of scene captions, they vastly outperform traditional models [42] [[sources/web-2025-08-07-3cb]], [43] [[sources/web-2025-08-07-3cb]], [44] [[sources/web-2025-08-07-3cb]]. This indicates that integrating rich, complex contextual information—rather than simple categorical labels—produces much more brain-aligned representations [42] [[sources/web-2025-08-07-3cb]], [45] [[sources/web-2025-08-07-3cb]], [46] [[sources/web-2025-08-07-3cb]].
*   **The Predictive-Accuracy vs. Identifiability Trade-off:** The flexible linear transformations currently used to evaluate models artificially inflate predictive scores by aggressively morphing representations to fit brain data [47] [[sources/web-2008-09-08-c5e]], [48] [[sources/web-2008-09-08-c5e]]. While this increases apparent alignment, it obscures profound geometric misalignments, rendering the best-fitting models structurally dissimilar to the brain representations they claim to mirror [47] [[sources/web-2008-09-08-c5e]], [49] [[sources/web-2008-09-08-c5e]], [50] [[sources/web-2008-09-08-c5e]].

## Sources cited

- [[sources/web-2024-10-30-e9d]]
- [[sources/web-2023-08-23-16e]]
- [[sources/web-2023-06-07-3e0]]
- [[sources/web-2023-11-02-f24]]
- [[nlm:9c40b2b4-a687-4ca1-9086-d4a68bd7dd05]]
- [[sources/web-2015-07-01-04f]]
- [[sources/yt-0W-cRw-EBAc]]
- [[sources/web-2013-05-20-a5c]]
- [[sources/web-2024-10-22-8f4]]
- [[sources/web-2025-09-16-c0d]]
- [[sources/web-2024-07-10-57e]]
- [[sources/web-2026-01-31-ff3]]
- [[sources/yt-5kq7M6pcQ5g]]
- [[sources/yt-ysv2g9M3ong]]
- [[sources/web-2025-08-07-3cb]]
- [[sources/web-2008-09-08-c5e]]
