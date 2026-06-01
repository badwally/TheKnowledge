---
schema_version: 1
type: synthesis
slug: 2026-06-01-do-predictive-or-generative-training-objectives-predictive-contrastiv
title: Predictive, Contrastive, and Alternative Training Objectives — investigation
  (2026-06-01-do-predictive-or-generative-training-objectives)
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
- sources/yt-IWIiR6mjrXY
last_updated: '2026-06-01T20:10:50Z'
sources_count: 1
draft: true
draft_started_at: '2026-06-01T20:10:50Z'
draft_unresolved_claims: 8
---
# Predictive, Contrastive, and Alternative Training Objectives — investigation

**Origin question:** Do predictive or generative training objectives produce representations that align with biological neural data better than discriminative objectives at matched task performance? Compare self-supervised versus supervised models, next-token and masked prediction versus classification, contrastive learning, and what the evidence says about the training objective versus architecture or scale as the primary driver of brain-ANN representational alignment.
**Session:** 2026-06-01-do-predictive-or-generative-training-objectives
**Branch:** Predictive, Contrastive, and Alternative Training Objectives

## Synthesis

### Specifics

Based on the provided sources, several predictive, contrastive, and alternative training objectives demonstrate strong alignment with biological neural data, challenging the assumption that standard supervised classification is uniquely suited for generating brain-like representations.

**Next-Word Prediction Objective in Language Processing**
*   **Its name and the key claim or contribution:** The next-word prediction task acts as a powerful normative objective driving brain-like representation in language models.
*   **The core approach, mechanism, or supporting evidence:** Researchers evaluate models trained on predicting the next token in a sequence against human fMRI, ECoG, and MEG recordings to test their alignment with the biological language system [1-3].
*   **Concrete details:** Models optimized for next-word prediction, such as GPT-2-XL, exhibit exceptional alignment with human brain data across multiple datasets, closely approaching the measurements of the human language system [1, 2]. When testing MEG-driven encoding models, a text-to-MEG encoder utilizing GPT-2 and CLIP embeddings outperformed an audio-to-MEG encoder relying on wav2vec2 embeddings [3]. The text-to-MEG model demonstrated higher Pearson Correlation scores and specifically engaged higher-order frontal regions, like Broca's area, which are linked to semantic integration [3].

**Contrastive Learning and Pointwise Mutual Information (PMI)**
*   **Its name and the key claim or contribution:** Contrastive learning objectives mathematically converge on the pointwise mutual information (PMI) of co-occurring events, mirroring human perceptual similarity.
*   **The core approach, mechanism, or supporting evidence:** Contrastive models are trained by pulling co-occurring items (like adjacent image patches or words) together in embedding space while pushing non-co-occurring items apart, resulting in an embedding space where distance reflects real-world statistical co-occurrence [4, 5]. 
*   **Concrete details:** The Noise Contrastive Estimation (NCE) objective mathematically forces the inner product of representations to approximate the probability ratio of items co-occurring versus occurring by chance [5, 6]. In empirical tests, contrastive models naturally recover human-like color similarity kernels (e.g., grouping green and blue closely while separating red and blue) regardless of whether they are trained on pixel co-occurrences in images or word co-occurrences in text [7, 8].

**Spatial Latent Estimation as an Alternative Supervised Objective**
*   **Its name and the key claim or contribution:** Training Convolutional Neural Networks (CNNs) to estimate spatial latents generates ventral-stream-aligned representations that rival those produced by object categorization.
*   **The core approach, mechanism, or supporting evidence:** To test if the ventral visual stream might be optimized for spatial properties rather than solely object identity, researchers trained CNNs on synthetic 3D images to explicitly estimate spatial latents, such as object position and pose [9]. They then compared the neural alignment of these spatial models to standard category-trained models [9].
*   **Concrete details:** Models trained to estimate just a few spatial latents achieved neural alignment scores comparable to models trained to categorize hundreds of different objects [9]. The internal representations of spatial-latent models and category models were found to be highly similar in their early and middle layers, a convergence that researchers trace to the implicit learning of non-target latent variability in the training data [9].

**Self-Supervised and Masked Vision Objectives**
*   **Its name and the key claim or contribution:** Self-supervised vision models develop robust, cross-modally aligned representations without relying on labeled classification targets.
*   **The core approach, mechanism, or supporting evidence:** By evaluating self-supervised models like DINO (self-supervised images), MAE (Masked Autoencoders), and CLIP (contrastive vision-language) using kernel alignment, researchers measure how similarly these models structure their representational spaces compared to both human behavior and large language models [10, 11].
*   **Concrete details:** Unsupervised visual methods can achieve decent brain-score alignment even without any labeled training images [12]. Furthermore, purely self-supervised vision models like DINO show increasing kernel alignment with large language models (like LLaMA) as they scale up, with DINO-Giant demonstrating strictly higher alignment scores than DINO-Small [13, 14]. Other self-supervised approaches like Masked Autoencoders (MAE) and CLIP also demonstrate this upward trajectory of cross-modal alignment as their general competency improves [15].

[^1]: [[sources/yt-IWIiR6mjrXY]] [^2]: [[sources/yt-IWIiR6mjrXY]] [^3]: [[sources/yt-IWIiR6mjrXY]] [^4]: [[sources/yt-IWIiR6mjrXY]] [^5]: [[sources/yt-IWIiR6mjrXY]] [^6]: [[sources/yt-IWIiR6mjrXY]] [^7]: [[sources/yt-IWIiR6mjrXY]] [^8]: [[sources/yt-IWIiR6mjrXY]] [^9]: [[sources/yt-IWIiR6mjrXY]] [^10]: [[sources/yt-IWIiR6mjrXY]] [^11]: [[sources/yt-IWIiR6mjrXY]] [^12]: [[sources/yt-IWIiR6mjrXY]] [^13]: [[sources/yt-IWIiR6mjrXY]] [^14]: [[sources/yt-IWIiR6mjrXY]] [^15]: [[sources/yt-IWIiR6mjrXY]]

### Comparisons

## Comparing Predictive, Contrastive, and Alternative Training Objectives

Based on the provided sources, several predictive, contrastive, and alternative training objectives offer distinct advantages and trade-offs when aiming to reproduce biological representations, challenging the necessity of classic supervised categorization.

**Items Compared:**
*   Next-Word Prediction Models (e.g., GPT-2) vs. Audio Self-Supervised Models (e.g., wav2vec2)
*   Sequential Prediction vs. Contrastive Learning (Pointwise Mutual Information)
*   Unimodal Self-Supervised Vision (e.g., DINO, MAE) vs. Multimodal Contrastive Supervision (e.g., CLIP)
*   Spatial Latent Estimation vs. Classic Supervised Categorization

**Sequential Text Prediction vs. Audio Feature Representation**
The next-token prediction objective in language models (like GPT-2) provides exceptional alignment with fMRI and ECoG data from the human language network [1]. In direct comparisons predicting MEG signals, text-to-MEG models leveraging GPT-2 next-token embeddings outperform audio-to-MEG models that rely on self-supervised wav2vec2 embeddings [2]. A critical difference in outcome is that self-supervised audio features primarily map to lower-level lateral temporal regions responsible for sensory integration, whereas next-token text embeddings capture higher-order semantic processing in frontal regions like Broca's area [2]. This highlights a contextual trade-off: predictive language models excel at representing semantic meaning and cognitive control, while self-supervised audio models are better suited for mapping direct sensory auditory pathways [2].

**Sequential Prediction vs. Contrastive Co-occurrence**
While next-token prediction learns through temporal sequences, contrastive learning relies on statistical co-occurrence across spatial or cross-modal domains, mathematically converging to capture the Pointwise Mutual Information (PMI) of events [3]. A key strength of the contrastive objective is its ability to naturally recover human-like perceptual boundaries (such as color similarity) simply from data co-occurrences, whether trained on image pixels or text words [3]. The trade-off is that while contrastive models successfully capture associative semantic structures, they rely on identifying positives and negatives across views or pairings, unlike predictive models which solely require sequential continuous streams [3].

**Unimodal Self-Supervised vs. Multimodal Contrastive Vision**
Models supervised explicitly to align modalities, such as CLIP, are designed to pull vision and language representations into a shared space [3]. However, pure unimodal self-supervised models like DINO (trained without language labels) demonstrate a remarkable strength by achieving kernel alignments with large language models that are nearly as strong as CLIP's cross-modal alignments [3]. This evidence suggests that as self-supervised models scale up and improve at their general visual tasks, they independently converge toward language-aligned representations [3]. The stated claim from these outcomes is that explicit cross-modal supervision may not be strictly necessary to achieve brain-like or language-like representational structures, provided the self-supervised unimodal model is sufficiently performant [3]. 

**Spatial Latent Estimation vs. Categorical Classification**
Traditionally, the primate ventral visual stream is assumed to be uniquely optimized for object categorization, heavily relying on models trained to classify hundreds of discrete object classes to achieve high neural alignment [4]. When researchers trained Convolutional Neural Networks (CNNs) to estimate continuous spatial latents—such as 3D object pose and position—these alternative supervised models achieved neural alignment scores matching the massive categorization models [4]. A notable strength of this alternative approach is that it successfully builds aligned representations by implicitly learning the variability of non-target latents present in the training data, demonstrating similar internal geometries in early and middle network layers [4]. Consequently, this challenges the assumption that categorical supervision is uniquely capable of generating brain-like visual representations, proving that continuous spatial estimation is an equally viable evolutionary or developmental objective for the visual cortex [4].

[^1]: [[sources/yt-IWIiR6mjrXY]] [^2]: [[sources/yt-IWIiR6mjrXY]] [^3]: [[sources/yt-IWIiR6mjrXY]] [^4]: [[sources/yt-IWIiR6mjrXY]]

### Gaps

## Unresolved Questions and Limitations Regarding Predictive and Alternative Objectives

Based on the provided sources, several critical gaps, limitations, and unresolved tensions remain regarding how predictive, contrastive, and alternative training objectives map to biological neural representations. 

**The Bijective Assumption and Cross-Modal Ineffability**
The mathematical proof demonstrating that contrastive learning objectives converge on a shared Pointwise Mutual Information (PMI) kernel relies heavily on the assumption that observation functions are bijective, meaning each data modality contains the complete information of the underlying world events `[1]`. However, researchers acknowledge this is a "huge simplification" that is mathematically untrue in the real world, because language cannot easily capture ineffable visual experiences (like viewing a solar eclipse), and vision struggles to represent abstract textual concepts (like "freedom of speech") `[1]`. The corpus leaves unanswered how these fundamental, lossy bottlenecks in observation modalities impact the theoretical convergence of contrastive learning representations in practical scenarios `[1]`.

**Local versus Global Representational Structure**
A major limitation identified in the evidence for cross-modal convergence is that the alignment between predictive language models and self-supervised vision models currently only holds for local representational structures `[1]`. When researchers evaluated these models using metrics that measure global structure alignment—specifically Centered Kernel Alignment (CKA)—the models did not exhibit the expected increasing alignment `[1]`. The sources leave an unresolved tension regarding why alternative objectives successfully converge on local nearest-neighbor geometries but fail to globally align the overarching architecture of their representational spaces `[1]`.

**The Unexplained Marginal Benefit of Explicit Multimodal Supervision**
There is an unanswered tension regarding the expected superiority of explicit cross-modal contrastive learning `[1]`. Researchers note that CLIP, a model specifically trained via contrastive objectives to align visual and linguistic representations, is surprisingly only marginally more aligned with predictive language models than DINO, which is a purely unimodal self-supervised vision model `[1]`. The corpus does not successfully explain why explicit multimodal supervision fails to yield a massive advantage in cross-modal representational alignment over models trained solely on self-supervised visual objectives `[1]`.

**Internet Data Curation vs. Normative Objectives**
While predictive and contrastive objectives are credited with driving cross-modal alignment, researchers identify a gap in understanding how much of this convergence is actually an artifact of the training data distribution `[1]`. The datasets used to train these self-supervised and predictive models consist of highly curated internet data that captures remarkable, biased, or human-filtered events, rather than a true random sample of physical reality `[1]`. It remains an open question whether the neural alignment observed in models utilizing these alternative objectives stems from the normative value of the objectives themselves, or simply from the shared, biased statistics of internet curation `[1]`.

**The Unexplored Potential of Spiking Neural Networks**
Although the corpus discusses substituting classic supervised objectives with predictive or alternative ones, it highlights a major gap in evaluating the underlying biological dynamics of the units themselves `[2]`. Researchers note that, currently, large-scale benchmarks like Brain-Score have not evaluated models utilizing spiking neural network architectures, such as networks built on leaky integrate-and-fire neurons `[2]`. Consequently, the corpus does not address whether implementing predictive or contrastive objectives directly on biologically plausible spiking architectures would finally close the remaining variance gap to achieve perfect neural alignment `[2]`.

**Unexplained Variance and Non-Identical Convergence**
The corpus highlights that no current alternative objective captures the entirety of biological variance. For instance, when alternative objectives—such as training Convolutional Neural Networks (CNNs) to estimate continuous spatial latents—achieve neural alignment scores comparable to categorical supervision, the resulting internal representations are noted to be "very similar -- but not identical" `[3]`. Furthermore, across the predictive language models and contrastive vision models evaluated, researchers explicitly acknowledge that their kernel alignment metrics currently cap out around a score of 0.6, leaving a substantial amount of representational variance completely unexplained by current predictive and contrastive paradigms `[1]`.

[^1]: [[sources/yt-IWIiR6mjrXY]] [^2]: [[sources/yt-IWIiR6mjrXY]] [^3]: [[sources/yt-IWIiR6mjrXY]]

## Sources cited

- [[sources/yt-IWIiR6mjrXY]]

## Included works

- [[sources/yt-IWIiR6mjrXY]]
