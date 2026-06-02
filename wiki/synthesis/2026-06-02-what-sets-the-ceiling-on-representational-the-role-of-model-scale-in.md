---
schema_version: 1
type: synthesis
slug: 2026-06-02-what-sets-the-ceiling-on-representational-the-role-of-model-scale-in
title: The Role of Model Scale in Alignment — investigation (2026-06-02-what-sets-the-ceiling-on-representational)
domains:
- convergent-ai-brain
question: What sets the ceiling on representational alignment between biological brains
  and artificial neural networks? Examine reported alignment ceilings and noise-ceiling
  normalization, mutual-information bounds on cross-system alignment, the persistent
  gap between the best models and brain data, whether alignment saturates with model
  scale, and which architectural or objective differences prevent full convergence.
created_at: '2026-06-02T01:01:17Z'
synthesizes:
- sources/web-2002-01-25-43f
- sources/web-2015-07-01-04f
- sources/web-2024-07-10-57e
- sources/web-2024-10-30-e9d
- sources/web-2025-01-22-a81
- sources/web-2025-09-16-c0d
- sources/yt-1_xH2mUFpZw
- sources/yt-FC-m7NRIKRM
last_updated: '2026-06-02T01:01:18Z'
sources_count: 8
draft: true
draft_started_at: '2026-06-02T01:01:18Z'
draft_unresolved_claims: 8
---
# The Role of Model Scale in Alignment — investigation

**Origin question:** What sets the ceiling on representational alignment between biological brains and artificial neural networks? Examine reported alignment ceilings and noise-ceiling normalization, mutual-information bounds on cross-system alignment, the persistent gap between the best models and brain data, whether alignment saturates with model scale, and which architectural or objective differences prevent full convergence.
**Session:** 2026-06-02-what-sets-the-ceiling-on-representational
**Branch:** The Role of Model Scale in Alignment

## Synthesis

### Specifics

Based on the provided sources, the corpus documents several distinct findings regarding how model scale impacts representational alignment, revealing a stark divergence in scaling laws depending on the specific modality being modeled.

**The Language Model Scaling Law for Neural and Behavioral Alignment**
*   **Name and Key Claim:** The Language Model Scaling Law demonstrates that increasing the parameter count of large language models (LLMs) reliably and continuously improves their alignment with human brain activity and naturalistic reading behaviors [1, 2]. 
*   **Core Approach:** Researchers test this by extracting the hidden states or attention matrices from LLMs of varying sizes and using ridge regression to align them with human fMRI activity and eye-tracking patterns—specifically, the number of regressive eye saccades readers make when revisiting earlier text [2-4]. 
*   **Concrete Details:** Evaluations evaluating models ranging from 774 million to 65 billion parameters (incorporating the GPT-2 and LLaMA families) show a clear scaling trend where alignment continuously increases with model size, without apparent diminishing returns [1, 2, 5]. One study reports a near-perfect positive correlation ($r = 0.95$) between an LLM's parameter scale and its brain alignment score [6]. Furthermore, fMRI contrasts demonstrate that larger LLMs consistently account for significantly more activation in a bilateral temporal-parietal brain network compared to their smaller counterparts [7]. This scaling effect also held true when models were evaluated on a different language and modality, successfully predicting fMRI activity for subjects listening to a Chinese audiobook [8].

**Parameter Count Saturation and Divergence in Vision Models**
*   **Name and Key Claim:** The Parameter Count Divergence finding reveals that, unlike in language processing, scaling up the total number of trainable parameters in artificial vision models does *not* consistently improve their ability to predict human high-level visual brain responses [9]. 
*   **Core Approach:** Researchers extracted features from hundreds of trained vision models of varying sizes and measured their alignment to human fMRI responses in the occipitotemporal cortex (OTC) [10, 11]. They evaluated this alignment using both classical representational similarity analysis (cRSA) and a feature-reweighted voxel-encoding RSA (veRSA) [12, 13].
*   **Concrete Details:** Across a massive evaluation of diverse vision architectures, increasing parameter counts in trained models actually produced a significant decrease in strict cRSA alignment ($r_{Spearman} = -0.45$) [9]. Under the more flexible veRSA metric, scaling parameters only yielded a non-significant bump in alignment ($r_{Spearman} = 0.14$) [9]. Consequently, researchers concluded that the raw quantity of trainable parameters has no consistent positive influence on emergent visual brain predictivity [9, 14].

**Scale-Driven Cross-Modal Kernel Alignment**
*   **Name and Key Claim:** The Platonic Representation Hypothesis proposes that as different foundation models increase in parameter scale and general competency, their internal representational geometries systematically converge toward a shared statistical model of reality, even across fundamentally different modalities like text and vision [15, 16].
*   **Core Approach:** To measure this convergence, researchers compute the "kernel alignment" between different models by taking paired multi-modal data (e.g., an image of an apple and the text word "apple") [17]. They then test whether the nearest-neighbor similarity distances between data points in the language model's embedding space match the distances in the vision model's embedding space [18, 19].
*   **Concrete Details:** Empirical tests evaluated language models ranging from a 560-million parameter Bloom model up to 65-billion and 70-billion parameter LLaMA models, plotting their text-embeddings against the visual embeddings of the DINO vision model [16, 20]. The results demonstrated a steady, upward-trending alignment slope: as language models scale up and achieve better next-character prediction scores, their representational kernels become continuously more aligned with the kernels of large vision models, and vice versa [16, 21].

[^1]: [[sources/web-2025-09-16-c0d]] [^2]: [[sources/web-2025-09-16-c0d]] [^3]: [[sources/web-2025-09-16-c0d]] [^4]: [[sources/web-2025-09-16-c0d]] [^5]: [[sources/web-2025-09-16-c0d]] [^6]: [[sources/web-2024-07-10-57e]] [^7]: [[sources/web-2025-09-16-c0d]] [^8]: [[sources/web-2025-09-16-c0d]] [^9]: [[sources/web-2024-10-30-e9d]] [^10]: [[sources/web-2024-10-30-e9d]] [^11]: [[sources/web-2024-10-30-e9d]] [^12]: [[sources/web-2024-10-30-e9d]] [^13]: [[sources/web-2024-10-30-e9d]] [^14]: [[sources/yt-FC-m7NRIKRM]] [^15]: [[sources/web-2015-07-01-04f]] [^16]: [[sources/yt-1_xH2mUFpZw]] [^17]: [[sources/yt-1_xH2mUFpZw]] [^18]: [[sources/web-2015-07-01-04f]] [^19]: [[sources/yt-1_xH2mUFpZw]] [^20]: [[sources/web-2015-07-01-04f]] [^21]: [[sources/yt-1_xH2mUFpZw]]

### Comparisons

Based on the provided sources, a stark divergence emerges regarding how different frameworks observe the effects of model scale on representational alignment.

## Uninterrupted Scaling in Language vs. Saturation in Vision

A primary tension in the literature is how the relationship between parameter scale and brain alignment differs fundamentally depending on the sensory modality being modeled. 

**Items Compared:** The Language Model Scaling Law versus Parameter Count Saturation and Divergence in Vision Models.

In language processing, evidence demonstrates a robust scaling law where increasing a large language model's (LLM) size from 774 million to 65 billion parameters continuously improves its alignment with human fMRI activity and regressive eye-tracking behaviors [1]. Researchers report a near-perfect positive correlation ($r = 0.95$) between an LLM's parameter scale and its neural predictivity score, showing no apparent diminishing returns as models grow [1]. Conversely, in vision models, scaling up the total number of trainable parameters actually produces a significant decrease in classical representational similarity analysis (cRSA) alignment ($r_{Spearman} = -0.45$), accompanied by only a non-significant increase in feature-reweighted veRSA alignment [2]. 

The contexts and trade-offs for these findings are rooted in how the different domains extract representations. The language scaling observations apply to sequential, naturalistic comprehension tasks where larger models naturally acquire better contextual representations that mirror human reading [1]. By contrast, the vision observations derive from static object-recognition tasks mapped to the occipitotemporal cortex [2]. The resulting trade-off is that while sheer parameter scale serves as a reliable proxy for emergent biological similarity in language networks, it acts as a weak or even negative predictor of native geometric alignment in vision networks [1, 2]. Consequently, researchers evaluating vision models must prioritize other inductive biases—such as the diversity of the visual training diet—rather than relying on raw capacity to drive alignment [2].

## Direct Biological Prediction vs. Model-to-Model Convergence

Frameworks also differ in whether they measure scale by explicitly fitting models to biological recordings or by observing how artificial models converge with each other as they grow.

**Items Compared:** Direct Neural Predictivity versus Cross-Modal Kernel Alignment under the Platonic Representation Hypothesis.

Direct neural predictivity measures the impact of scale by tracking how much variance an LLM explains in actual biological signals, establishing that scaled models significantly increase activation coverage in bilateral temporal-parietal brain networks [1]. In contrast, cross-modal kernel alignment evaluates scale without ever measuring a brain, demonstrating that as text-only models scale from 560 million to 70 billion parameters, their nearest-neighbor similarity structures naturally align with the kernels of massive vision models like DINO [3, 4]. 

A major strength of direct biological prediction is its explicit grounding in human cognitive mechanisms, proving that scale directly corresponds to realistic human temporal processing and behavioral reading patterns [1]. A noted weakness of this direct approach, however, is its reliance on limited neuroimaging datasets and sluggish biological proxies, such as fMRI blood flow, which inherently restrict the ceiling of measurable alignment [1, 2]. Alternatively, a strength of cross-modal kernel alignment is that it avoids biological noise limitations entirely, cleanly demonstrating that scaling pushes diverse, unimodal AI models toward a shared statistical structure of reality [3, 4]. However, a critical weakness of the model-to-model approach is that it strictly measures convergence between artificial systems, assuming that this shared space reflects a true "platonic" reality without directly verifying it against biological brains or accounting for modality-specific boundaries, such as ineffable visual phenomena that text-based models cannot natively capture [3, 4].

[^1]: [[sources/yt-FC-m7NRIKRM]] [^2]: [[sources/yt-FC-m7NRIKRM]] [^3]: [[sources/yt-FC-m7NRIKRM]] [^4]: [[sources/yt-FC-m7NRIKRM]]

### Gaps

Based on the provided sources, several patterns emerge regarding unresolved questions, methodological limitations, and gaps in coverage when evaluating the role of model scale in representational alignment.

## The Extreme Limits of Scale and the Risk of Overfitting

While current research demonstrates clear scaling laws up to tens of billions of parameters in language models, the literature identifies an unresolved tension regarding what happens at the extreme limits of scale. 

Reviewers of current alignment studies explicitly note a gap in coverage, questioning whether the correlation between brain alignment and model size holds when pushed to its absolute limits with massive, state-of-the-art models like Nemotron-4 (340B parameters) or Grok-1 (314B parameters) [1]. Furthermore, researchers advancing the Platonic Representation Hypothesis openly question whether the observed cross-modal convergence will continue indefinitely as models scale [2]. They note an unanswered tension that massive models might eventually over-optimize to the superficial statistics of their specific training modality—for example, overfitting entirely to text—causing their cross-modal and biological alignment to suddenly "fall off a cliff" rather than continuously improving [2].

## Confounded Variables in "Off-the-Shelf" Scaling

A major methodological limitation in the current corpus is that studies of scale rely almost entirely on pre-trained foundation models pulled from the internet, forcing researchers to make "confounded comparisons" [3, 4]. 

Because larger models in families like LLaMA or GPT inherently feature different architectural tweaks and are exposed to vastly larger and more curated datasets during training, it is difficult to cleanly isolate the effect of parameter count from the effect of data richness [5, 6]. The corpus notes that resolving this gap would require training an entire suite of massive models from scratch with perfectly controlled datasets and compute budgets—a scientifically ideal scenario that remains practically impossible because it would cost billions of dollars [4]. Consequently, a careful reader is left without a definitive answer as to whether raw parameter scale or the sheer volume of ingested internet data is the true underlying driver of biological alignment. 

## Strict Biological Gating for Massive Models

There is a significant gap regarding whether massive-scale models actually achieve true structural and mechanistic alignment with the brain, or if scale merely inflates flexible prediction scores. 

The L-PACT framework demonstrates that apparent predictive alignment in language models is entirely explained away by severe controls (such as temporal shifts and lexical autocorrelations) when subjected to strict gates for relational profiles and mechanism-specific necessity [7-9]. However, the L-PACT analysis only included small-to-medium models (up to 1.7B parameters, such as Qwen3-1.7B), explicitly excluding massive models like the 70B parameter variants because they exceeded inclusion criteria or lacked validated feature rows [10, 11]. This creates a critical gap in coverage: the corpus does not address whether massive 70B+ models possess the emergent structural properties necessary to finally pass strict reliability-bounded and mechanism-stripping gates, leaving it unresolved whether scale eventually breeds true biological equivalence or simply produces more powerful statistical confounders [10, 12].

## The Unexplained Modality Divergence

While the corpus clearly documents *that* model scaling impacts modalities differently, it leaves a major gap regarding *why* this divergence exists. 

Empirical evidence shows that increasing parameter count reliably and continuously improves brain alignment in language models [13, 14]. Conversely, scaling up total trainable parameters in vision models produces a significant decrease in strict classical alignment and no consistent benefit in feature-reweighted alignment [15]. The corpus does not resolve the root cause of this discrepancy. While researchers hypothesize that identifying visual scaling laws might simply require novel, untested metrics for evaluating neural manifolds [16, 17], the corpus fails to address whether vision models are inherently disadvantaged by static image-recognition objectives, and whether training vision models on continuous, naturalistic video might unlock the same scaling laws currently enjoyed by text-based language models [18].

[^1]: [[sources/web-2024-07-10-57e]] [^2]: [[sources/yt-1_xH2mUFpZw]] [^3]: [[sources/yt-FC-m7NRIKRM]] [^4]: [[sources/yt-FC-m7NRIKRM]] [^5]: [[sources/web-2024-10-30-e9d]] [^6]: [[sources/web-2024-10-30-e9d]] [^7]: [[sources/web-2002-01-25-43f]] [^8]: [[sources/web-2002-01-25-43f]] [^9]: [[sources/web-2002-01-25-43f]] [^10]: [[sources/web-2002-01-25-43f]] [^11]: [[sources/web-2002-01-25-43f]] [^12]: [[sources/web-2002-01-25-43f]] [^13]: [[sources/web-2025-09-16-c0d]] [^14]: [[sources/web-2025-09-16-c0d]] [^15]: [[sources/web-2024-10-30-e9d]] [^16]: [[sources/web-2024-10-30-e9d]] [^17]: [[sources/web-2024-10-30-e9d]] [^18]: [[sources/web-2025-01-22-a81]]

## Sources cited

- [[sources/web-2025-09-16-c0d]]
- [[sources/web-2024-07-10-57e]]
- [[sources/web-2024-10-30-e9d]]
- [[sources/yt-FC-m7NRIKRM]]
- [[sources/web-2015-07-01-04f]]
- [[sources/yt-1_xH2mUFpZw]]
- [[sources/web-2002-01-25-43f]]
- [[sources/web-2025-01-22-a81]]

## Included works

- [[sources/web-2002-01-25-43f]]
- [[sources/web-2015-07-01-04f]]
- [[sources/web-2024-07-10-57e]]
- [[sources/web-2024-10-30-e9d]]
- [[sources/web-2025-01-22-a81]]
- [[sources/web-2025-09-16-c0d]]
- [[sources/yt-1_xH2mUFpZw]]
- [[sources/yt-FC-m7NRIKRM]]
