---
schema_version: 1
type: synthesis
slug: 2026-06-01-do-predictive-or-generative-training-objectives-cross-cutting
title: Cross-cutting themes (2026-06-01-do-predictive-or-generative-training-objectives)
domains:
- convergent-ai-brain
question: Do predictive or generative training objectives produce representations
  that align with biological neural data better than discriminative objectives at
  matched task performance? Compare self-supervised versus supervised models, next-token
  and masked prediction versus classification, contrastive learning, and what the
  evidence says about the training objective versus architecture or scale as the primary
  driver of brain-ANN representational alignment.
created_at: '2026-06-01T20:10:49Z'
synthesizes:
- synthesis/2026-06-01-do-predictive-or-generative-training-objectives-performance-and-scale
- synthesis/2026-06-01-do-predictive-or-generative-training-objectives-predictive-contrastiv
- synthesis/2026-06-01-do-predictive-or-generative-training-objectives-the-impact-of-generat
- synthesis/2026-06-01-do-predictive-or-generative-training-objectives-the-role-of-noise-and
last_updated: '2026-06-01T20:10:51Z'
sources_count: 1
draft: true
draft_started_at: '2026-06-01T20:10:51Z'
draft_unresolved_claims: 11
---
# Cross-cutting themes — 2026-06-01-do-predictive-or-generative-training-objectives

**Origin question:** Do predictive or generative training objectives produce representations that align with biological neural data better than discriminative objectives at matched task performance? Compare self-supervised versus supervised models, next-token and masked prediction versus classification, contrastive learning, and what the evidence says about the training objective versus architecture or scale as the primary driver of brain-ANN representational alignment.

## Synthesis

### Recurring Patterns

Based on the provided sources, several overarching frameworks and patterns bridge the different themes, serving as shared methodological or theoretical foundations for evaluating model-brain alignment.

## Synthetic Stimulus Optimization (Falsification by Synthesis)

This framework involves using gradient-descent optimization to synthesize artificial stimuli that expose the hidden representational gaps between computational models and biological perception.

**Themes Used In:**
*   The Impact of Generative and Discriminative Objectives on Brain Alignment
*   The Role of Noise and Robustness in Alignment

Across these themes, researchers deploy synthetic optimization as an out-of-distribution falsification tool rather than relying on natural datasets, which often fail to expose model flaws. In the evaluation of generative versus discriminative objectives, this approach manifests as "controversial stimuli": images explicitly optimized to elicit highly confident but contradictory classification predictions from a pair of distinct models [1]. By presenting these controversial images to humans, researchers can adjudicate which model's decision boundaries truly align with human perception, demonstrating that hybrid generative-discriminative models generally win [1]. In the context of noise and robustness, the approach is adapted to generate "metamers"—stimuli optimized to produce identical activations in the deep layers of a single target network rather than contrasting two models [2]. This application reveals that while standard networks produce unrecognizable metamers, models trained to be robust to adversarial noise yield synthetic stimuli that are far more recognizable to humans [2]. In both cases, pushing models to synthesize or respond to boundary-case stimuli exposes their true inductive biases [1, 2].

## Representational Similarity and Kernel Alignment

This mathematical approach evaluates alignment not by comparing specific network parameters or neurons, but by measuring the geometric distances between data points within a representation space.

**Themes Used In:**
*   Performance and Scale as Primary Drivers of Alignment
*   Predictive, Contrastive, and Alternative Training Objectives

This framework is applied as a universal translator, allowing researchers to compare entirely disparate systems—such as vision models, language models, and biological brains—by evaluating their similarity matrices or "kernels." In the study of performance and scale, kernel alignment is used to demonstrate cross-modal convergence, proving that as language models (like LLaMA) and self-supervised vision models (like DINO) scale up, the nearest-neighbor structures of their embeddings become increasingly aligned [3, 4]. Within the predictive and alternative objectives theme, this same mathematical framework is used to explain why contrastive learning works [3, 4]. Contrastive models mathematically converge on the pointwise mutual information (PMI) of co-occurring events, naturally recovering human-like similarity structures simply by mapping statistical associations in the training data [3, 4]. Furthermore, this approach serves as the basis for Representational Similarity Analysis (RSA), which calculates the distances between different stimuli within fMRI voxel spaces to establish a structural bridge between biological measurements and artificial activations [5]. 

## Competency and Constraint-Driven Convergence 

This theoretical pattern posits that adding functional constraints or demanding higher generalized competency forces diverse architectures to abandon idiosyncratic solutions and converge toward a shared, biologically plausible representational space.

**Themes Used In:**
*   Performance and Scale as Primary Drivers of Alignment
*   The Role of Noise and Robustness in Alignment

This principle operates on the idea that there are many ways to be wrong, but very few ways to be perfectly right in a complex physical world. Under the performance theme, this is articulated as the "Anna Karenina" principle: models that achieve high competency across a broad suite of general visual tasks cluster tightly together with highly similar representational kernels, effectively overriding the differences between their specific training objectives or architectures [3, 4]. In the robustness theme, the constraint applied is resistance to noise rather than broad task competency [2, 6]. By explicitly forcing feed-forward networks to resist adversarial attacks or simulated sensory noise, the models naturally develop "representational straightening" of natural movies (mimicking primate V1) and produce more human-aligned metamers [2, 6]. In both themes, restricting a model's hypothesis space through severe functional constraints—whether general task competency or noise robustness—acts as a primary driver of biological alignment [2-4, 6].

## Linear Neural Predictivity and Standardized Benchmarking

This framework evaluates artificial networks by literally stitching them to biological data, testing whether a linear transformation can accurately map an artificial layer's activations to recorded brain activity.

**Themes Used In:**
*   Performance and Scale as Primary Drivers of Alignment
*   Predictive, Contrastive, and Alternative Training Objectives

This approach is operationalized to objectively rank competing artificial hypotheses against vast datasets of biological recordings. In the performance and scale theme, the "Brain-Score" platform utilizes this approach to test models against primate ventral stream recordings (V1 through IT), revealing a historical correlation where optimizing for ImageNet categorization initially improved linear neural predictivity [7, 8]. When applied to predictive and alternative objectives, this identical regression-based approach is adapted to evaluate language and auditory modalities [9]. For example, researchers use linear encoding models on MEG data to discover that next-token text embeddings (from GPT-2) successfully predict activity in higher-order frontal regions like Broca's area, whereas self-supervised audio embeddings primarily predict lower-level temporal regions [9]. Across these diverse sub-areas, the core assumption remains consistent: a model is considered aligned with biology if its internal state space can be linearly decoded to predict real neural spikes or voxel activations in response to the same stimuli [7-9].

[^1]: [[sources/yt-IWIiR6mjrXY]] [^2]: [[sources/yt-IWIiR6mjrXY]] [^3]: [[sources/yt-IWIiR6mjrXY]] [^4]: [[sources/yt-IWIiR6mjrXY]] [^5]: [[sources/yt-IWIiR6mjrXY]] [^6]: [[sources/yt-IWIiR6mjrXY]] [^7]: [[sources/yt-IWIiR6mjrXY]] [^8]: [[sources/yt-IWIiR6mjrXY]] [^9]: [[sources/yt-IWIiR6mjrXY]]

### Shared Anchors

Based on the provided sources, several primary datasets, benchmarking platforms, and foundational architectures serve as shared conceptual anchors across the corpus. 

## The ImageNet Dataset

**What it is and what it contains:**
ImageNet is a massive, large-scale computer vision database containing millions of natural images labeled across thousands of distinct object categories, traditionally used to train and benchmark standard feed-forward classification networks [1, 2].

**Themes Used In:**
* Performance and Scale as Primary Drivers of Alignment
* The Impact of Generative and Discriminative Objectives on Brain Alignment
* The Role of Noise and Robustness in Alignment

**Why it is treated as foundational:**
ImageNet serves as the standard proxy metric for "core visual categorization competency" across the literature [1, 2]. Within the performance and scale theme, researchers treat optimization on ImageNet as a fundamental starting point, demonstrating a historical correlation where early improvements in a model's ImageNet accuracy reliably predicted better alignment with primate ventral stream brain data [1, 2]. However, it also acts as the load-bearing foundation for uncovering the limits of pure discrimination; researchers note that pushing models to extreme, state-of-the-art ImageNet performance eventually causes their brain alignment to plateau or even reverse [1, 2]. In the generative and robustness themes, scaling experiments from toy datasets up to ImageNet is treated as the ultimate test of perceptual alignment [3]. When evaluated at the ImageNet scale using controversial stimuli, standard discriminative models catastrophically fail to match human perception, generating unintelligible "rubbish" images, which prompts researchers to test adversarially robust models as a necessary corrective [3]. 

## The Brain-Score Platform

**What it is and what it contains:**
Brain-Score is an integrative, standardized benchmarking platform that houses a vast collection of biological data—including neural spike rates recorded across the primate ventral visual hierarchy (V1, V2, V4, and IT), human behavioral confusion matrices, and human language system fMRI data [1, 2]. 

**Themes Used In:**
* Performance and Scale as Primary Drivers of Alignment
* Predictive, Contrastive, and Alternative Training Objectives
* The Role of Noise and Robustness in Alignment

**Why it is treated as foundational:**
Brain-Score provides the unified, quantitative metric utilized to objectively rank the biological plausibility of competing artificial hypotheses [1, 2]. It is foundational to the performance and scale theme because it allows researchers to prove that as models become more competent at tasks, they naturally achieve higher Brain-Scores, acting as a guard against overfitting by evaluating models on held-out past, present, and future experimental data [1, 2]. Within the alternative objectives theme, this same platform is used to validate that alternative training methods—such as training CNNs on continuous spatial latent estimation—can achieve neural alignment scores that match or rival those of classic categorical classification models [4]. Finally, in the robustness theme, Brain-Score serves as the biological anchor to demonstrate that mimicking early visual architecture (like in the "v1net" model) yields high alignment with V1 neural data while simultaneously conferring inherent robustness to adversarial noise [1, 2].

## Wikipedia Image-Caption Pairs and Internet Corpora

**What it is and what it contains:**
These are massive, curated datasets scraped from the internet, consisting of text and paired image-caption data (such as photos from Wikipedia matched with their human-written descriptions) [5, 6]. 

**Themes Used In:**
* Performance and Scale as Primary Drivers of Alignment
* Predictive, Contrastive, and Alternative Training Objectives

**Why it is treated as foundational:**
Internet-derived paired data is the methodological foundation for the "Platonic Representation Hypothesis" [5, 6]. To evaluate whether distinctly trained vision and language models converge on a shared representation of the world, researchers rely entirely on paired Wikipedia images and captions to bridge the modalities, testing whether a vision model's kernel distance between two photos matches a language model's kernel distance between their corresponding captions [5, 6]. Furthermore, this dataset anchors a critical unresolved tension regarding what exactly predictive and contrastive training objectives are optimizing toward [5, 6]. The corpus relies on the nature of this internet data to ask whether models are truly converging on the physical and statistical reality of the natural world, or if they are simply memorizing the shared sociological biases and remarkable events curated by humans on the internet [5, 6].

## Autoregressive Next-Token Language Models (e.g., GPT-2, LLaMA)

**What it is and what it contains:**
These are foundational, deep transformer-based neural networks trained via self-supervision on massive text corpora explicitly to predict the next word or character in a sequence [1, 2, 5, 6].

**Themes Used In:**
* Predictive, Contrastive, and Alternative Training Objectives
* Performance and Scale as Primary Drivers of Alignment
* The Impact of Generative and Discriminative Objectives on Brain Alignment

**Why it is treated as foundational:**
Next-token language models serve as the gold-standard computational proxies for higher-order semantic processing across multiple themes. In the predictive objectives theme, researchers rely on GPT-2 embeddings as highly effective text-to-MEG encoders, demonstrating that next-token predictive objectives successfully capture semantic integration and cognitive control in human frontal brain regions like Broca's area, far outperforming audio-based encoders [7]. In the performance and scale theme, the competency of massive autoregressive models (like the 65-billion parameter LLaMA) directly serves as the x-axis for proving cross-modal convergence; as a model's next-token log-likelihood improves, its kernel alignment with self-supervised vision models reliably increases [5, 6]. Finally, within the generative and discriminative alignment theme, GPT-2 and other language models are used to synthesize "controversial sentences"—statements optimized to be highly likely to one model but unlikely to another—proving that while predictive next-token models capture human judgments of sentence-likeliness better than older N-gram models, they still fail to fully match human perception [3].

[^1]: [[sources/yt-IWIiR6mjrXY]] [^2]: [[sources/yt-IWIiR6mjrXY]] [^3]: [[sources/yt-IWIiR6mjrXY]] [^4]: [[sources/yt-IWIiR6mjrXY]] [^5]: [[sources/yt-IWIiR6mjrXY]] [^6]: [[sources/yt-IWIiR6mjrXY]] [^7]: [[sources/yt-IWIiR6mjrXY]]

### Recurring Tradeoffs

## Ecological Validity vs. Discriminative Power (Natural vs. Synthetic Stimuli)

A central tension exists between testing models under naturalistic conditions and designing experiments with enough power to separate competing computational hypotheses.

**Themes Used In:**
* The Impact of Generative and Discriminative Objectives on Brain Alignment
* The Role of Noise and Robustness in Alignment

Natural images are ecologically valid and effectively test models under the realistic conditions in which biological brains function [1]. However, because highly parameterized deep networks act as universal approximators, they frequently make similar predictions on standard natural images, meaning these stimuli lack the discriminative power to reveal which model's internal mechanism is actually correct [1]. Conversely, synthetic "controversial stimuli" and "metamers" explicitly force models to make divergent predictions or expose their hidden invariances, providing strong adjudicative power to scientists [1, 2]. The strict trade-off is that these highly optimized synthetic images are completely unnatural, they depend on gradient-based optimization that restricts evaluation strictly to differentiable models, and they run the risk of exposing trivial out-of-distribution failure modes rather than meaningful biological differences [1, 2].

## Narrow Task Optimization vs. Biological Alignment and General Competency

Researchers document a recurring tension where driving an artificial model to achieve state-of-the-art accuracy on a specific task eventually degrades its alignment with biological brains.

**Themes Used In:**
* Performance and Scale as Primary Drivers of Alignment

In the Brain-Score framework, early improvements in a model's top-1 performance on the ImageNet classification task strongly correlated with improved linear predictions of primate ventral stream neural activity [3, 4]. However, this relationship represents a severe trade-off at extreme scales; as models are pushed to state-of-the-art ImageNet performance, their brain alignment plateaus and eventually becomes anti-correlated [3, 4]. This indicates that hyper-optimizing for a narrow, isolated objective eventually sacrifices the model's fidelity to human-like perceptual mechanisms [3, 4]. In contrast, models that trade away peak narrow performance for broad, general visual competency across many diverse tasks—such as those evaluated on the VTAB benchmark—converge into tightly clustered, highly similar representational spaces that override idiosyncratic training differences [5, 6].

## Computational Efficiency vs. Human-Like Generative Perception

The sources highlight a fundamental trade-off between the speed and efficiency of purely discriminative architectures and the robust, human-aligned perception of generative or hybrid models.

**Themes Used In:**
* The Impact of Generative and Discriminative Objectives on Brain Alignment

Standard feed-forward discriminative models are computationally efficient, straightforward to train, and highly successful at core categorization tasks [1]. However, their internal inductive biases diverge significantly from biological perception, which is evidenced by their generation of unintelligible deep-layer metamers and their failure to match human judgments on controversial stimuli [1, 2]. In contrast, models that explicitly incorporate generative inference—such as the Shot Analysis by Synthesis model or the Joint Energy Model—treat incoming images as evidence to be evaluated against a learned prior, yielding representations that dominate purely discriminative networks in aligning with human perception [1]. The explicit cost of this biological alignment is massive computational complexity, as well as the fact that pure generative models often fail to scale effectively to complex natural datasets like CIFAR-10 without incorporating hybrid discriminative components [1].

## High-Dimensional Granularity vs. Low-Dimensional Shared Structure

When aligning data across different biological individuals or artificial networks, researchers face a trade-off between preserving granular, high-dimensional data and finding stable, shared low-dimensional manifolds.

**Themes Used In:**
* Representational Alignment across Individuals and Systems

Attempting to map neural activity directly in high-dimensional voxel or sensor space is heavily complicated by individual differences in anatomy, representational drift over time, and mismatched layer sizes across different artificial networks [7]. To circumvent this mismatch, researchers utilize low-dimensional alignment methods, such as the Shared Response Model, which learn a stable joint factorization across multiple individuals [7]. The trade-off is that selecting the optimal lower-dimensional feature subspace relies on highly sensitive hyperparameters that significantly alter downstream results, and unmatched idiosyncratic information must be actively discarded to force the alignment [7].

## Curated Data Scale vs. True Physical Reality

A theoretical tension exists regarding whether scaling models on massive datasets forces them to learn the true physical structure of the world or merely memorize sociological biases.

**Themes Used In:**
* Performance and Scale as Primary Drivers of Alignment

The "Platonic Representation Hypothesis" posits that distinct computational models converge because they are all trained on data sampled from the exact same underlying physical reality [5, 6]. However, a major trade-off in achieving the scale necessary for this convergence is the heavy reliance on internet-curated datasets, such as Wikipedia image-caption pairs, to train massive foundation models [5, 6]. Because these internet datasets selectively capture remarkable, human-filtered, and sociologically biased events rather than a true random sampling of physical reality, researchers face a tension in distinguishing true platonic convergence from the mere memorization of shared human curation artifacts [5, 6].

[^1]: [[sources/yt-IWIiR6mjrXY]] [^2]: [[sources/yt-IWIiR6mjrXY]] [^3]: [[sources/yt-IWIiR6mjrXY]] [^4]: [[sources/yt-IWIiR6mjrXY]] [^5]: [[sources/yt-IWIiR6mjrXY]] [^6]: [[sources/yt-IWIiR6mjrXY]] [^7]: [[sources/yt-IWIiR6mjrXY]]

## Sources cited

- [[sources/yt-IWIiR6mjrXY]]

## Included works

- [[synthesis/2026-06-01-do-predictive-or-generative-training-objectives-performance-and-scale]]
- [[synthesis/2026-06-01-do-predictive-or-generative-training-objectives-predictive-contrastiv]]
- [[synthesis/2026-06-01-do-predictive-or-generative-training-objectives-the-impact-of-generat]]
- [[synthesis/2026-06-01-do-predictive-or-generative-training-objectives-the-role-of-noise-and]]
