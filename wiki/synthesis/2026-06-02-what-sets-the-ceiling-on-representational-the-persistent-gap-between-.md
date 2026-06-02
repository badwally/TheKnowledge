---
schema_version: 1
type: synthesis
slug: 2026-06-02-what-sets-the-ceiling-on-representational-the-persistent-gap-between-
title: The Persistent Gap Between Best Models and Brain Data — investigation (2026-06-02-what-sets-the-ceiling-on-representational)
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
- sources/web-2024-10-30-e9d
- sources/web-2026-02-20-ed0
- sources/yt-FC-m7NRIKRM
last_updated: '2026-06-02T01:01:19Z'
sources_count: 4
draft: true
draft_started_at: '2026-06-02T01:01:19Z'
draft_unresolved_claims: 10
---
# The Persistent Gap Between Best Models and Brain Data — investigation

**Origin question:** What sets the ceiling on representational alignment between biological brains and artificial neural networks? Examine reported alignment ceilings and noise-ceiling normalization, mutual-information bounds on cross-system alignment, the persistent gap between the best models and brain data, whether alignment saturates with model scale, and which architectural or objective differences prevent full convergence.
**Session:** 2026-06-02-what-sets-the-ceiling-on-representational
**Branch:** The Persistent Gap Between Best Models and Brain Data

## Synthesis

### Specifics

Based on the provided sources, the corpus documents several specific mechanisms, frameworks, and evaluations demonstrating that impressive prediction scores frequently mask profound divergences between artificial and biological systems.

**The Discrepancy Between Classical and Feature-Reweighted RSA**
*   **Name and Key Claim:** The discrepancy between classical representational similarity analysis (cRSA) and feature-reweighted voxel-encoding RSA (veRSA) demonstrates that raw, emergent AI representations remain highly misaligned with the brain's native geometry [1]. 
*   **Core Approach:** Researchers tested model alignment using two differing strictness levels: cRSA, which forces the model's raw population geometry to directly correspond to the brain's geometry, versus veRSA, a flexible method that allows independent linear reweighting of the model's features to fit individual brain voxels [2-4]. The approach additionally evaluated the internal representations of 124 top models against each other, comparing how similar the models were before and after this reweighting was applied [5].
*   **Concrete Details:** When constrained by classical RSA, models explained a meager ~31% of the explainable variance in human occipitotemporal cortex (OTC) responses [1, 6]. However, applying linear feature reweighting (veRSA) artificially inflated the explainable variance to roughly 79.5% [1, 6]. Model-to-model comparisons further proved that this reweighting acts as a deceptive compressor: while the top models exhibited massively varied raw cRSA geometries (spanning a correlation range of $r = -0.107$ to $0.983$, mean $0.448$), their feature-reweighted veRSA geometries clustered together almost identically (mean $0.881$, SD $0.0313$) [7]. This proves that standard reweighting methods squeeze fundamentally mismatched AI representations into a deceptively uniform subspace [1, 7].

**The L-PACT Framework and Control-Explained Evidence**
*   **Name and Key Claim:** The L-PACT (Language Predictive, Alignment-pattern, Causal, and Turing-bounded Test) framework establishes that high neural prediction scores are fundamentally insufficient to prove mechanistic alignment between language models and the brain [8-10].
*   **Core Approach:** Rather than accepting raw neural predictions, L-PACT subjects language models to a conjunctive hierarchy of stringent gates: predictive adequacy against severe controls, relational pattern adequacy relative to brain-to-brain profiles, counterfactual mechanism-stripping (removing a specific mechanism from a model to verify a selective neural drop), and reliability-bounded ceiling normalizations [9, 11]. Severe controls include shifting temporal sequences, randomizing token orders, layer-label permutations, and generating autocorrelation-matched random features [12].
*   **Concrete Details:** In a large-scale evaluation of models including GPT-2, Pythia, and Qwen variants across datasets like MEG-MASC and Brain Treebank, 196 rows of seemingly positive predictive improvements were downgraded because they were entirely explained away by severe controls (such as circular-shifted features or token-order shuffles) [13-15]. Ultimately, out of 146 integrated decision rows, exactly zero rows passed the required gates for structural or mechanism-specific alignment, and all 146 instances were labeled as purely control-explained [9, 16]. 

**Direct Biological Grounding via the ReAlnet Framework**
*   **Name and Key Claim:** The ReAlnet framework asserts that standard task-optimized artificial vision models inherently lack specific dynamic and hierarchical characteristics of the human brain, necessitating the direct injection of neural data during training to close the persistent representational gap [17, 18].
*   **Core Approach:** Recognizing that simply increasing depth or layer counts fails to emulate human complexity, researchers augmented a standard deep convolutional network (CORnet-S) with a multi-layer encoding module [19, 20]. The network is jointly optimized to perform object classification alongside a generation loss (incorporating Mean Squared Error and a contrastive loss) that forces the model to predict subject-specific human EEG time-series signals [20, 21]. 
*   **Concrete Details:** By explicitly learning brain dynamics, individualized ReAlnets achieved up to a 6% absolute similarity improvement and a 40% relative improvement ratio over the baseline CORnet model at the similarity peak timepoint [22]. Unlike baseline networks, ReAlnets successfully replicated the specific hierarchical individual variability observed in human brains—which naturally increases from layer V1 to layer IT—proving that basic image-training cannot natively capture this biological structure [23, 24]. Furthermore, strict ablation models isolating purely visual training (ReAlnet $\beta=0$) and models trained on temporally scrambled EEG confirmed that true, paired neural alignment is mechanistically necessary to acquire specialized human-like refinements for object features like "electronic/technology-related" and "long-thin" shapes [25, 26].

[^1]: [[sources/web-2024-10-30-e9d]] [^2]: [[sources/yt-FC-m7NRIKRM]] [^3]: [[sources/web-2024-10-30-e9d]] [^4]: [[sources/web-2024-10-30-e9d]] [^5]: [[sources/web-2024-10-30-e9d]] [^6]: [[sources/yt-FC-m7NRIKRM]] [^7]: [[sources/web-2024-10-30-e9d]] [^8]: [[sources/web-2002-01-25-43f]] [^9]: [[sources/web-2002-01-25-43f]] [^10]: [[sources/web-2002-01-25-43f]] [^11]: [[sources/web-2002-01-25-43f]] [^12]: [[sources/web-2002-01-25-43f]] [^13]: [[sources/web-2002-01-25-43f]] [^14]: [[sources/web-2002-01-25-43f]] [^15]: [[sources/web-2002-01-25-43f]] [^16]: [[sources/web-2002-01-25-43f]] [^17]: [[sources/web-2026-02-20-ed0]] [^18]: [[sources/web-2026-02-20-ed0]] [^19]: [[sources/web-2026-02-20-ed0]] [^20]: [[sources/web-2026-02-20-ed0]] [^21]: [[sources/web-2026-02-20-ed0]] [^22]: [[sources/web-2026-02-20-ed0]] [^23]: [[sources/web-2026-02-20-ed0]] [^24]: [[sources/web-2026-02-20-ed0]] [^25]: [[sources/web-2026-02-20-ed0]] [^26]: [[sources/web-2026-02-20-ed0]]

### Comparisons

Based on the provided sources, several distinct tensions emerge regarding how evaluation frameworks reveal or conceal the persistent gap between AI models and biological brains.

## Rigid Geometry vs. Flexible Mapping

To measure how far models diverge from true brain representations, researchers employ distinct mathematical linking techniques that fundamentally alter the apparent alignment.

**Items Compared:** Classical Representational Similarity Analysis (cRSA) versus Feature-Reweighted Voxel-Encoding RSA (veRSA).

In large-scale evaluations of visual models, cRSA and veRSA produce starkly different assessments of model-brain alignment [1]. When using cRSA—which forces the raw, unweighted population geometry of the model to directly correspond to the brain's geometry—models explain only about 31% of the explainable variance in the human occipitotemporal cortex [1]. Conversely, applying the highly flexible linear feature reweighting of veRSA artificially inflates the explainable variance to roughly 79.5% [1]. A direct model-to-model comparison reveals that raw cRSA geometries across top models vary wildly (with correlations ranging from -0.107 to 0.983), yet when evaluated through the lens of veRSA, these same models cluster together almost identically (mean correlation 0.881) [2]. 

The primary trade-off between these approaches centers on their strictness regarding native representational structures [1, 2]. A core strength of veRSA is its flexibility to identify any usable predictive features that correlate with individual brain voxels, making it highly effective for building predictive encoding models [1]. However, a severe weakness of this flexibility is that veRSA acts as a deceptive compressor, squeezing fundamentally mismatched and widely varied AI representations into a uniform subspace that masks how structurally different the models are from each other and the brain [1, 2]. The strength of cRSA is that it exposes this native geometric divergence, highlighting that the raw representational formats learned by deep neural networks do not naturally mirror the brain's geometry [1, 2].

## Predictive Utility vs. Structural and Mechanistic Necessity

Frameworks also differ sharply in whether they interpret raw prediction scores as evidence of true biological alignment, or if they require models to pass strict counterfactual tests.

**Items Compared:** Standard Predictive Encoding Scores versus the L-PACT Evaluation Framework.

Standard predictive evaluations frequently yield positive, conventional-looking correlations that suggest models successfully capture brain-relevant linguistic structures [3]. The L-PACT framework challenges this by explicitly separating standard predictive adequacy from relational, mechanism-stripping, and reliability-bounded adequacy [4]. When 146 decision rows of apparent model-brain correspondences were subjected to L-PACT's rigorous gates, exactly zero rows survived to prove structural or mechanism-specific alignment [3, 5]. Instead, 100% of these apparent positive predictions were entirely "control-explained" by severe nuisance variables [5].

A major trade-off exists between the sensitivity of an evaluation and its interpretability [6]. Standard prediction scores have the strength of high sensitivity, making them useful for establishing baseline statistical associations and annotating experimental data [4]. However, their critical weakness is an inability to distinguish true biological computation from nuisance variables; a model might yield high prediction scores merely because it carries basic temporal autocorrelations, contextual regularities, or lexical frequencies rather than true relational organization [4]. The strength of L-PACT is that it actively filters out these false positives by subjecting models to severe controls like circular temporal shifts, randomized token orders, and layer-label permutations [7]. The trade-off for this rigorous, conjunctive gating is that it is highly conservative; it downgrades all current apparent successes into control-explained failures, proving that raw prediction scores alone make models seem far more biologically informative than the structural evidence actually supports [3, 8].

## Task-Optimized Emergence vs. Direct Biological Grounding

Researchers also disagree on whether models can bridge the representational gap purely by training on massive external datasets, or if they require direct biological grounding.

**Items Compared:** Purely Image-Trained Architectures versus Neural-Aligned Architectures (the ReAlnet framework).

Standard deep convolutional neural networks optimized purely for object recognition struggle to emulate the complexity and dynamic information processing of the human visual system [9]. To address this gap, the ReAlnet framework takes a direct alignment approach, augmenting a standard model with a multi-layer encoding module that forces it to simultaneously perform image classification and predict subject-specific human EEG signals [10]. This explicit biological grounding allows ReAlnets to capture specific hierarchical structures—such as individual variability that naturally increases from layer V1 to V4 and then decreases in the LOC output layer—that pure image-trained models fail to capture on their own [11]. Furthermore, neural alignment allows the model to refine specific object feature dimensions (e.g., "electronic/technology-related" or "long-thin" shapes) beyond what its visual diet naturally instills [12].

The trade-offs between these approaches revolve around data scalability and alignment fidelity [10, 13]. A major strength of pure task-optimization is its ability to scale effortlessly with virtually infinite, highly varied internet image datasets, which drives baseline representation quality [12, 13]. By contrast, the weakness of direct biological grounding is its strict reliance on physiological recordings [10, 13]. Human noninvasive recordings like EEG and fMRI suffer from low data quality, high signal noise, and small sample sizes, which can ultimately constrain the precision and fidelity of the model-to-brain alignment [13, 14]. However, the unique strength of the ReAlnet approach is its ability to transcend these limitations to extract dynamic, human-like representational patterns that successfully generalize across novel object categories and even alternate neuroimaging modalities like fMRI [10, 15].

[^1]: [[sources/yt-FC-m7NRIKRM]] [^2]: [[sources/yt-FC-m7NRIKRM]] [^3]: [[sources/yt-FC-m7NRIKRM]] [^4]: [[sources/yt-FC-m7NRIKRM]] [^5]: [[sources/yt-FC-m7NRIKRM]] [^6]: [[sources/yt-FC-m7NRIKRM]] [^7]: [[sources/yt-FC-m7NRIKRM]] [^8]: [[sources/yt-FC-m7NRIKRM]] [^9]: [[sources/yt-FC-m7NRIKRM]] [^10]: [[sources/yt-FC-m7NRIKRM]] [^11]: [[sources/yt-FC-m7NRIKRM]] [^12]: [[sources/yt-FC-m7NRIKRM]] [^13]: [[sources/yt-FC-m7NRIKRM]] [^14]: [[sources/yt-FC-m7NRIKRM]] [^15]: [[sources/yt-FC-m7NRIKRM]]

### Gaps

Based on the provided sources, several unresolved questions, methodological limitations, and gaps in coverage obscure a complete understanding of the persistent representational gap between AI models and biological brains.

## The "Ground Truth" Metric Dilemma

While researchers document a massive discrepancy between strict classical evaluations and flexible feature-reweighting, there is no consensus on which method constitutes the true measure of biological alignment. 

Evaluations show that when using classical representational similarity analysis (cRSA), models explain only ~31% of visual brain variance, but this jumps to nearly 80% when using the flexible voxel-encoding RSA (veRSA) [1]. While veRSA is highly effective for building predictive encoding models, it compresses fundamentally mismatched AI representations into a shared sub-space, masking their structural deviations from each other and the brain [2-4]. The corpus notes an unresolved tension here: the field has yet to cohere around principles of mechanistic interpretability that would logically dictate whether strict mapping (cRSA) or flexible mapping (veRSA) is the "correct" way to evaluate the true representational gap [1]. 

## Bridging the Gap in Massive Language Models

A critical gap exists regarding whether massive-scale foundation models can bridge the structural divergences identified by rigorous evaluation frameworks. 

The L-PACT framework reveals that all apparent predictive successes in its tested language models were entirely "control-explained" by nuisance variables like temporal shifts or lexical autocorrelations [5-7]. However, the corpus explicitly bounds this negative finding by acknowledging a lack of coverage for massive, state-of-the-art models [8]. The L-PACT analysis exclusively evaluated small-to-medium models (e.g., up to 1.7B parameters), explicitly excluding larger registry models (such as 7B or 70B parameter variants) because they exceeded study inclusion criteria or lacked validated feature rows [8, 9]. Consequently, the corpus does not answer whether the persistent gap observed under these strict relational and mechanism-stripping gates is a fundamental limitation of the transformer paradigm itself, or if models at the 70B+ scale eventually acquire the emergent properties necessary to pass these hurdles [8].

## Limitations of Direct Biological Grounding

Attempts to directly close the gap by training models on human neural data face significant methodological and physiological limitations that the current corpus does not resolve. 

Frameworks like ReAlnet successfully improve model alignment by directly injecting human EEG signals during training, but researchers acknowledge that this process is severely hindered by the high signal noise and small sample sizes inherent to noninvasive EEG data [10]. Furthermore, the alignment methodology itself relies on relatively simple learning objectives (like mean squared error and contrastive loss) combined with shallow encoding modules that assume a direct mapping between model features and neural activity [10]. The corpus identifies an unanswered question of whether these simple, direct mapping strategies overlook complex, non-linear, and multi-stage biological transformations, thereby artificially limiting the model's capacity to learn truly abstract and hierarchically structured neural patterns [10].

## The Masking Effect of Naturalistic Stimuli

There is an unresolved tension regarding whether standard naturalistic datasets are simply too "easy" to properly expose the mechanistic gap between AI models and the brain. 

Researchers caution that widely sampled, ecologically rich natural image datasets (like the Natural Scenes Dataset) may actively obscure fine-scale representational differences because practically all highly performant models can successfully capture the large-scale representational distinctions present in natural visual stimuli [11]. The corpus suggests that to truly expose the persistent gap, the field needs to utilize "controversial stimuli"—synthetic images explicitly optimized to differentiate one model from another—or targeted psychophysical comparisons (e.g., line drawings or inverted faces) [11]. However, the provided corpus relies predominantly on natural scenes and does not implement these controversial stimuli at scale, leaving a careful reader to wonder how much larger the measured gap would be if models were aggressively stress-tested against the human brain's native edge cases.

[^1]: [[sources/web-2024-10-30-e9d]] [^2]: [[sources/web-2024-10-30-e9d]] [^3]: [[sources/web-2024-10-30-e9d]] [^4]: [[sources/web-2024-10-30-e9d]] [^5]: [[sources/web-2002-01-25-43f]] [^6]: [[sources/web-2002-01-25-43f]] [^7]: [[sources/web-2002-01-25-43f]] [^8]: [[sources/web-2002-01-25-43f]] [^9]: [[sources/web-2002-01-25-43f]] [^10]: [[sources/web-2026-02-20-ed0]] [^11]: [[sources/web-2024-10-30-e9d]]

## Sources cited

- [[sources/web-2024-10-30-e9d]]
- [[sources/yt-FC-m7NRIKRM]]
- [[sources/web-2002-01-25-43f]]
- [[sources/web-2026-02-20-ed0]]

## Included works

- [[sources/web-2002-01-25-43f]]
- [[sources/web-2024-10-30-e9d]]
- [[sources/web-2026-02-20-ed0]]
- [[sources/yt-FC-m7NRIKRM]]
