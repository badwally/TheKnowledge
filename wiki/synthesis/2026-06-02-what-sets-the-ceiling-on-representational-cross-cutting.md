---
schema_version: 1
type: synthesis
slug: 2026-06-02-what-sets-the-ceiling-on-representational-cross-cutting
title: Cross-cutting themes (2026-06-02-what-sets-the-ceiling-on-representational)
domains:
- convergent-ai-brain
question: What sets the ceiling on representational alignment between biological brains
  and artificial neural networks? Examine reported alignment ceilings and noise-ceiling
  normalization, mutual-information bounds on cross-system alignment, the persistent
  gap between the best models and brain data, whether alignment saturates with model
  scale, and which architectural or objective differences prevent full convergence.
created_at: '2026-06-02T01:01:17Z'
synthesizes:
- synthesis/2026-06-02-what-sets-the-ceiling-on-representational-alignment-ceilings-and-norm
- synthesis/2026-06-02-what-sets-the-ceiling-on-representational-architectural-and-objective
- synthesis/2026-06-02-what-sets-the-ceiling-on-representational-mutual-information-bounds-a
- synthesis/2026-06-02-what-sets-the-ceiling-on-representational-the-persistent-gap-between-
- synthesis/2026-06-02-what-sets-the-ceiling-on-representational-the-role-of-model-scale-in
last_updated: '2026-06-02T01:01:20Z'
sources_count: 5
draft: true
draft_started_at: '2026-06-02T01:01:20Z'
draft_unresolved_claims: 8
---
# Cross-cutting themes — 2026-06-02-what-sets-the-ceiling-on-representational

**Origin question:** What sets the ceiling on representational alignment between biological brains and artificial neural networks? Examine reported alignment ceilings and noise-ceiling normalization, mutual-information bounds on cross-system alignment, the persistent gap between the best models and brain data, whether alignment saturates with model scale, and which architectural or objective differences prevent full convergence.

## Synthesis

### Recurring Patterns

Based on the provided sources, several powerful frameworks and principles transcend individual sub-areas to establish how researchers evaluate, limit, and interpret representational alignment.

## Representational Similarity Analysis (RSA) and Feature Reweighting

**Themes Used In:** Alignment Ceilings and Normalization Metrics, The Role of Model Scale in Alignment, Architectural and Objective Inductive Biases, The Persistent Gap Between Best Models and Brain Data.

Representational Similarity Analysis (RSA) is an organizing mathematical framework that researchers adapt into two distinct metrics—classical RSA (cRSA) and feature-reweighted voxel-encoding RSA (veRSA)—to test competing alignment claims. Within the study of architectural biases, researchers apply veRSA to reveal that distinct mesoscale architectures, such as Convolutional Neural Networks and Vision Transformers, achieve near-equivalent human brain predictivity when their tasks and data are held constant [1-3]. When evaluating the role of model scale, this framework exposes a divergence: scaling up vision model parameters significantly decreases raw cRSA alignment while producing only a non-significant bump in veRSA alignment [4]. This dichotomy in the RSA framework ultimately characterizes the persistent gap between models and brains: cRSA reveals that the native, unweighted geometries of AI representations only explain roughly 31% of brain variance, whereas the flexible linear reweighting of veRSA artificially inflates this to nearly 80% [5-8]. Consequently, RSA serves as the cross-cutting tool to show how mathematical reweighting compresses fundamentally mismatched AI representations into a deceptively shared subspace [8, 9].

## Cross-Modal Kernel Alignment

**Themes Used In:** Mutual-Information Bounds and Convergence Limits, The Role of Model Scale in Alignment.

The principle of evaluating representations by their internal "kernels"—specifically how a model measures the nearest-neighbor similarity distances between data points—unites theoretical convergence hypotheses with empirical scaling laws. Under the theme of mutual-information bounds, this kernel framework is used to mathematically demonstrate that models attempting to learn data co-occurrences naturally converge to the Pointwise Mutual Information (PMI) of the underlying latent events generating the observations [10-13]. This exact same kernel measurement is then adapted to track the role of model scale without relying on direct brain recordings [14, 15]. By comparing paired stimuli (like the image of an apple and the text word "apple"), researchers apply kernel alignment to show that as text-only language models scale from 560 million to 70 billion parameters, their representational geometries systematically converge toward the kernels of massive vision models like DINO [16-19].

## Reliability-Bounded Rigor and Severe Controls

**Themes Used In:** Alignment Ceilings and Normalization Metrics, The Persistent Gap Between Best Models and Brain Data.

The requirement to constrain raw model prediction scores against severe empirical bounds is formalized by strict evaluation architectures, such as the L-PACT framework. In the context of alignment ceilings, this principle adapts brain-to-brain reliability from a mere descriptive normalizer into a prescriptive operational gate, demanding that model evidence reach a configured fraction of valid empirical brain-brain estimates (like split-half or run-to-run reliability) to be considered valid [20-23]. This same principle of severe control is applied to expose the persistent gap between models and brains, proving that high neural prediction scores are fundamentally insufficient to claim mechanistic alignment [20, 24, 25]. When models are subjected to rigorous controls—including circular temporal shifts, randomized token orders, or layer-label permutations—apparent "brain-aligned" predictive effects are downgraded because they are entirely explained away by these nuisance variables rather than demonstrating true relational structure [25-28].

## The Primacy of Input Diet and Data Diversity

**Themes Used In:** Architectural and Objective Inductive Biases, Mutual-Information Bounds and Convergence Limits, The Role of Model Scale in Alignment.

The principle that the diversity of training data dictates representational structure far more than model architecture or sheer size cuts across multiple domains. When evaluating inductive biases, researchers discovered that models trained on impoverished visual diets (such as exclusively indoor scenes or strictly faces) suffer massive brain-alignment penalties compared to models trained on diverse sets, regardless of whether the architecture is convolutional or attention-based [29-31]. Within the context of model scaling, this principle explains why simply increasing the raw quantity of training images (e.g., scaling from ImageNet1K to ImageNet21K) without a corresponding increase in true data diversity fails to consistently improve brain predictivity in vision models [32, 33]. Finally, this focus on data limitations governs the theoretical bounds of cross-system convergence, as models cannot align on concepts that are naturally absent from their specific modality diet, such as "ineffable" visual experiences that text data fundamentally lacks the capacity to capture [34-36].

[^1]: [[sources/web-2024-10-30-e9d]] [^2]: [[sources/web-2024-10-30-e9d]] [^3]: [[sources/web-2024-10-30-e9d]] [^4]: [[sources/web-2024-10-30-e9d]] [^5]: [[sources/yt-FC-m7NRIKRM]] [^6]: [[sources/web-2024-10-30-e9d]] [^7]: [[sources/web-2024-10-30-e9d]] [^8]: [[sources/web-2024-10-30-e9d]] [^9]: [[sources/web-2024-10-30-e9d]] [^10]: [[sources/web-2015-07-01-04f]] [^11]: [[sources/web-2015-07-01-04f]] [^12]: [[sources/yt-1_xH2mUFpZw]] [^13]: [[sources/yt-1_xH2mUFpZw]] [^14]: [[sources/web-2015-07-01-04f]] [^15]: [[sources/yt-1_xH2mUFpZw]] [^16]: [[sources/web-2015-07-01-04f]] [^17]: [[sources/yt-1_xH2mUFpZw]] [^18]: [[sources/yt-1_xH2mUFpZw]] [^19]: [[sources/yt-1_xH2mUFpZw]] [^20]: [[sources/web-2002-01-25-43f]] [^21]: [[sources/web-2002-01-25-43f]] [^22]: [[sources/web-2002-01-25-43f]] [^23]: [[sources/web-2002-01-25-43f]] [^24]: [[sources/web-2002-01-25-43f]] [^25]: [[sources/web-2002-01-25-43f]] [^26]: [[sources/web-2002-01-25-43f]] [^27]: [[sources/web-2002-01-25-43f]] [^28]: [[sources/web-2002-01-25-43f]] [^29]: [[sources/web-2024-10-30-e9d]] [^30]: [[sources/web-2024-10-30-e9d]] [^31]: [[sources/web-2024-10-30-e9d]] [^32]: [[sources/yt-FC-m7NRIKRM]] [^33]: [[sources/web-2024-10-30-e9d]] [^34]: [[sources/web-2015-07-01-04f]] [^35]: [[sources/yt-1_xH2mUFpZw]] [^36]: [[sources/yt-1_xH2mUFpZw]]

### Shared Anchors

Based on the provided sources, several primary datasets, frameworks, and benchmarks act as the empirical and theoretical foundations for multi-theme inquiries into brain-AI alignment. 

## The Natural Scenes Dataset (NSD)
**What it is and what it contains:** The Natural Scenes Dataset is a massive, high-resolution 7T fMRI dataset containing human brain responses to tens of thousands of natural images drawn from the Microsoft COCO dataset [1]. 

**Themes Used In:** Alignment Ceilings and Normalization Metrics, Architectural and Objective Inductive Biases, The Persistent Gap Between Best Models and Brain Data.

**Why it is foundational:** NSD provides the necessary signal-to-noise ratio and trial-to-trial reliability required to calculate empirical noise ceilings for the human occipitotemporal cortex [1]. Researchers use this pristine data to perform over 1.8 billion regressions, enabling controlled comparisons that prove mesoscale architecture matters far less than visual diet [1, 2]. Furthermore, the dataset acts as the primary testbed for exposing the representational gap between AI and the brain, demonstrating that standard feature-reweighting techniques (veRSA) compress fundamentally mismatched AI features into a deceptively shared subspace when trying to predict NSD voxel activity [1].

## ImageNet (1K and 21K)
**What it is and what it contains:** ImageNet is a canonical, large-scale computer vision dataset consisting of millions of images categorized into thousands of object classes [1]. 

**Themes Used In:** The Role of Model Scale in Alignment, Architectural and Objective Inductive Biases.

**Why it is foundational:** ImageNet serves as the indispensable control variable for defining a model's "visual diet" [1]. By restricting diverse models (such as Convolutional Neural Networks and Vision Transformers) to the exact same ImageNet training data, researchers can isolate the true drivers of brain alignment [1, 2]. Furthermore, comparing models trained on the 1.2-million-image ImageNet-1K versus the 14-million-image ImageNet-21K provides the foundational evidence that simply scaling up raw image quantity without fundamentally altering dataset diversity fails to improve a model's alignment with human brain representations [1, 2].

## The L-PACT Framework and its Core Datasets
**What it is and what it contains:** L-PACT (Language Predictive, Alignment-pattern, Causal, and Turing-bounded Test) is a stringent, multi-level evaluation framework applied to primary neural datasets like Brain Treebank, MEG-MASC, and Podcast ECoG [3]. 

**Themes Used In:** Alignment Ceilings and Normalization Metrics, The Persistent Gap Between Best Models and Brain Data.

**Why it is foundational:** The L-PACT framework and its associated datasets redefine the boundaries of alignment claims by demanding that raw neural prediction scores survive severe controls, relational profiling, and counterfactual mechanism-stripping [3]. It acts as the load-bearing proof that apparent high-performing language models are actually failing to capture true biological computation, demonstrating that 100% of tested predictive successes across these datasets are entirely "control-explained" by nuisance variables like lexical autocorrelations or temporal shifts [3].

## The Brain-Score Platform
**What it is and what it contains:** Brain-Score is an integrative benchmarking platform that evaluates and ranks artificial neural networks based on how closely their internal representations and outputs match primate and human neural and behavioral visual responses [1, 4]. 

**Themes Used In:** Alignment Ceilings and Normalization Metrics, The Persistent Gap Between Best Models and Brain Data.

**Why it is foundational:** Brain-Score provides the standardized behavioral benchmarks (such as error consistency and out-of-distribution shape bias tasks) necessary to measure whether models align with human cognitive behavior [4, 5]. It is utilized to prove that models directly aligned with human EEG signals (like the ReAlnet framework) successfully translate their neural-level alignments into quantifiable, human-like behavioral improvements [5]. Additionally, critiques of Brain-Score's arithmetic averaging expose how high-variance behavioral metrics can artificially mask persistent mechanistic gaps in neural predictivity [4].

## The THINGS and THINGS EEG2 Datasets
**What it is and what it contains:** THINGS is a large-scale database of object concepts and naturalistic images, while THINGS EEG2 provides high-temporal-resolution human EEG recordings paired with those images [5]. 

**Themes Used In:** The Persistent Gap Between Best Models and Brain Data, Alignment Ceilings and Normalization Metrics.

**Why it is foundational:** This dataset provides the non-invasive human temporal dynamics required to train models to actively mimic the human brain [5]. By utilizing the distinct training and test sets of THINGS EEG2, researchers can actively optimize AI models to predict individual human EEG signals, and then track 49 specific object feature dimensions (such as "electronic" or "food-related") to prove that these neural-aligned models successfully capture refined human semantics that pure image-training fails to learn [5].

[^1]: [[sources/yt-FC-m7NRIKRM]] [^2]: [[sources/yt-FC-m7NRIKRM]] [^3]: [[sources/yt-FC-m7NRIKRM]] [^4]: [[sources/yt-FC-m7NRIKRM]] [^5]: [[sources/yt-FC-m7NRIKRM]]

### Recurring Tradeoffs

Based on the provided sources, several recurring trade-offs and tensions dictate how researchers evaluate and interpret the alignment between artificial intelligence and biological brains.

## Rigid Structural Mapping vs. Flexible Predictive Utility
Researchers face a constant tension between utilizing highly sensitive, flexible methods to maximize predictive utility and enforcing strict, rigid constraints to prove true structural alignment.

**Themes Used In:** The Persistent Gap Between Best Models and Brain Data, Alignment Ceilings and Normalization Metrics
**Items Compared:** Classical RSA (cRSA) vs. Feature-Reweighted Voxel-Encoding RSA (veRSA); Standard Predictive Encoding vs. The L-PACT Framework

When evaluating the similarity between AI models and brains, flexible methods like veRSA allow researchers to independently reweight model features to fit individual brain voxels, artificially inflating explainable variance to nearly 80% [1]. However, this flexibility acts as a deceptive compressor that squeezes fundamentally mismatched AI representations into a deceptively shared subspace [1]. Conversely, strict metrics like cRSA force the model's raw, unweighted population geometry to directly correspond to the brain's geometry, revealing that these raw AI geometries only explain roughly 31% of the neural variance [1]. A parallel tension exists in establishing mechanistic necessity, where standard predictive encoding yields high prediction scores that are useful for baseline annotations, but are highly susceptible to nuisance variables like temporal autocorrelation [2]. Stricter frameworks like L-PACT trade this sensitivity for extreme interpretability, proving that under rigorous controls, apparent positive predictions are entirely control-explained, resulting in a zero percent pass rate for true structural or mechanism-specific alignment claims [2].

## Idealized Mathematical Convergence vs. Modality-Specific Reality
Theoretical proofs of cross-system alignment frequently rely on idealized mathematical conditions that clash with the messy, constrained reality of biological senses and diverse modalities.

**Themes Used In:** Mutual-Information Bounds and Convergence Limits
**Items Compared:** Pointwise Mutual Information (PMI) Convergence vs. The Ineffability Bound

The Platonic Representation Hypothesis mathematically argues that contrastive learners naturally converge to the Pointwise Mutual Information (PMI) of the underlying causal events that generate observations, creating a shared statistical model of reality across vision and text [3]. However, this formal mathematical proof relies on the strict assumption that observation functions are completely bijective [3]. In empirical reality, information is fundamentally lost or abstracted when the physical world is projected into a single sensory modality, imposing an "ineffability bound" on cross-system alignment [3, 4]. Because visual experiences like witnessing a total solar eclipse cannot be perfectly translated into text, and highly abstract verbal concepts like "freedom of speech" lack direct visual equivalents, systems cannot achieve the perfect convergence promised by the idealized mathematics [4].

## Controlled Experimental Rigor vs. Uncontrolled Massive Scale
The exorbitant computational cost of training foundation models forces researchers into a severe trade-off between controlled, unconfounded experiments on small datasets and studying massive, state-of-the-art models with heavily confounded variables.

**Themes Used In:** Architectural and Objective Inductive Biases, The Role of Model Scale in Alignment
**Items Compared:** The SLIP Controlled Framework vs. Massive "Off-the-Shelf" Model Evaluations

To definitively prove which inductive biases drive brain alignment, researchers must train models from scratch holding compute budgets and datasets strictly constant, an endeavor that would practically cost billions of dollars [5]. Because of this prohibitive cost, researchers are generally forced to evaluate pre-trained models pulled from the internet, which inherently confounds architectural changes with the massive, unstandardized proprietary datasets those models were originally trained on [1, 5]. For instance, when researchers ran tightly controlled experiments training different architectures on the exact same 15-million image dataset (SLIP), they found that the language-alignment objective actually performed slightly worse at predicting the visual brain than pure visual self-supervision [1]. Yet, because OpenAI's state-of-the-art CLIP model was trained on an inaccessible 400-million image-text pair dataset, researchers cannot definitively separate whether its exceptional brain predictivity is strictly due to its massive data scale, or if language-alignment objectives uniquely provide synergistic benefits only at that extreme scale [1].

## Direct Biological Grounding vs. Infinite Task-Optimized Scaling
There is an ongoing tension regarding whether brain-like AI is best achieved by infinitely scaling models on internet tasks or by explicitly grounding models in noisy, limited biological recordings.

**Themes Used In:** The Persistent Gap Between Best Models and Brain Data
**Items Compared:** Task-Optimized Architectures vs. Neural-Aligned Architectures (ReAlnet)

Purely task-optimized models scale effortlessly with virtually infinite internet image datasets, driving massive baseline representational capabilities [6]. However, these purely task-optimized models fail to natively capture the complex, dynamic hierarchical variability observed in the human visual system, such as increasing individual variability from layer V1 to V4 [6]. To bypass this limitation, frameworks like ReAlnet directly ground the model by injecting non-invasive human EEG recordings into the training process via a signal-generation loss [6]. This explicit neural alignment forces the network to learn specific biological refinements, such as distinct tuning for "electronic/technology-related" object shapes that standard image diets naturally miss [6]. The severe trade-off for this direct grounding approach is that it relies on biological measurements like EEG, which inherently suffer from low signal-to-noise ratios, rapid transient artifacts, and extremely small sample sizes, directly constraining the precision of the resulting alignment compared to internet-scale pre-training [6].

## Quantitative Nuance vs. Stable Rank Ordering in Metric Aggregation
When researchers must compress dozens of disparate alignment metrics into a single leaderboard score, they face trade-offs between retaining quantitative magnitude differences and ensuring stable, scaled rankings.

**Themes Used In:** Alignment Ceilings and Normalization Metrics
**Items Compared:** Arithmetic Averaging vs. Z-Transformed and Rank-Mean Aggregation

Benchmarks like Brain-Score aggregate many diverse behavioral and neural tests into a single overall score using a simple arithmetic mean [7]. A key weakness of this approach is that because behavioral scores possess much higher variance and maximum values (e.g., ~0.6) compared to neural scores (e.g., ~0.5), the final leaderboard is overwhelmingly dominated by behavioral variance, allowing models with mediocre neural alignment to achieve top overall ranks [7]. To resolve this imbalance, researchers can apply z-transforms or calculate the mean rank order across metrics to artificially level the playing field [7]. The trade-off is that while these transformations successfully prevent behavioral scores from overshadowing neural scores, they either discard the absolute quantitative magnitude of the differences between models (in rank averaging) or produce scores that are completely unstable over time because they depend entirely on the performance of other models in the current pool (in z-transforming) [7].

[^1]: [[sources/yt-FC-m7NRIKRM]] [^2]: [[sources/yt-FC-m7NRIKRM]] [^3]: [[sources/yt-FC-m7NRIKRM]] [^4]: [[sources/yt-FC-m7NRIKRM]] [^5]: [[sources/yt-FC-m7NRIKRM]] [^6]: [[sources/yt-FC-m7NRIKRM]] [^7]: [[sources/yt-FC-m7NRIKRM]]

## Sources cited

- [[sources/web-2024-10-30-e9d]]
- [[sources/yt-FC-m7NRIKRM]]
- [[sources/web-2015-07-01-04f]]
- [[sources/yt-1_xH2mUFpZw]]
- [[sources/web-2002-01-25-43f]]

## Included works

- [[synthesis/2026-06-02-what-sets-the-ceiling-on-representational-alignment-ceilings-and-norm]]
- [[synthesis/2026-06-02-what-sets-the-ceiling-on-representational-architectural-and-objective]]
- [[synthesis/2026-06-02-what-sets-the-ceiling-on-representational-mutual-information-bounds-a]]
- [[synthesis/2026-06-02-what-sets-the-ceiling-on-representational-the-persistent-gap-between-]]
- [[synthesis/2026-06-02-what-sets-the-ceiling-on-representational-the-role-of-model-scale-in]]
