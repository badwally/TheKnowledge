---
schema_version: 1
type: synthesis
slug: 2026-06-01-do-predictive-or-generative-training-objectives-the-role-of-noise-and
title: The Role of Noise and Robustness in Alignment — investigation (2026-06-01-do-predictive-or-generative-training-objectives)
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
last_updated: '2026-06-01T20:10:51Z'
sources_count: 3
draft: true
draft_started_at: '2026-06-01T20:10:51Z'
draft_unresolved_claims: 3
---
# The Role of Noise and Robustness in Alignment — investigation

**Origin question:** Do predictive or generative training objectives produce representations that align with biological neural data better than discriminative objectives at matched task performance? Compare self-supervised versus supervised models, next-token and masked prediction versus classification, contrastive learning, and what the evidence says about the training objective versus architecture or scale as the primary driver of brain-ANN representational alignment.
**Session:** 2026-06-01-do-predictive-or-generative-training-objectives
**Branch:** The Role of Noise and Robustness in Alignment

## Synthesis

### Specifics

Based on the provided sources, several patterns emerge regarding how inducing noise or adversarial robustness acts as a mechanism to force artificial representations into closer alignment with biological perception.

**Representational Straightening via Noise Robustness**
*   **Its name and the key claim or contribution:** Representational Straightening in Robust Feedforward Networks demonstrates that adding noise robustness to models naturally produces brain-like temporal representations without requiring explicit predictive training objectives [1].
*   **The core approach, mechanism, or supporting evidence:** Rather than explicitly optimizing networks to predict future frames in a sequence, researchers utilized Adversarial Training (AT) and Random Smoothing (RS) to simulate bio-plausible noise in sensory input stages [1]. They found that these noise-robust networks naturally developed "representational straightening"—a decrease in the curvature of feature trajectories across a sequence of natural movie frames, which is a hallmark of primate primary visual cortex (V1) and human perceptual behavior [1].
*   **Concrete details:** The AT and RS trained models yielded improved predictions of actual primate V1 neural data compared to baseline models [1]. Furthermore, because their feature codes were remarkably straightened, researchers could successfully generate intervening movie frames by performing simple linear interpolation in the model's feature space, despite the models never being explicitly trained on temporal video trajectories [1].

**Improved Metamer Recognizability through Adversarial Training**
*   **Its name and the key claim or contribution:** The Adversarial Metamers framework reveals that explicitly training models to resist adversarial examples forces their deep-layer invariances to become significantly more recognizable and aligned with human perception [2, 3].
*   **The core approach, mechanism, or supporting evidence:** Standard neural networks produce deep-layer "metamers"—synthetic stimuli that elicit identical deep-layer activations to a natural seed stimulus—that appear or sound like completely unintelligible noise to humans [4, 5]. To bridge this gap, researchers generated metamers from models that underwent adversarial training, a process where small, human-imperceptible perturbations are added to the training data to force the model to learn more robust decision boundaries [2, 6].
*   **Concrete details:** When applied to both visual networks and audio networks, the deep-layer metamers synthesized from these robustly trained models were far more recognizable to human subjects in behavioral experiments than those from standardly trained models [3, 7]. However, researchers explicitly noted that while this architectural modification improves perceptual alignment, it does not completely close the recognition gap, and the exact reasons why adversarial robustness improves metamer recognizability remain not fully understood [7].

**Adjudicating Robust Models via Controversial Stimuli**
*   **Its name and the key claim or contribution:** Controversial Stimuli Generation highlights that while adversarial training provides a partial corrective toward human alignment, it fails to fully replicate human perceptual geometry when pushed to its absolute limits [8, 9].
*   **The core approach, mechanism, or supporting evidence:** Researchers optimized synthetic images to elicit confident but contradictory class predictions from pairs of distinct models, testing out-of-distribution generalization by seeing which model's prediction human subjects agreed with [10, 11]. They specifically pitted adversarially trained, robust models against standard discriminative networks to adjudicate their perceptual alignment [12].
*   **Concrete details:** When an adversarially trained ResNet-50 was pitted against a standard Inception model, the resulting controversial stimulus (predicted as a Weimaraner by the robust model and a Persian cat by the standard model) possessed visually identifiable dog-like features, indicating the robust model's dominance in perceptual alignment [12, 13]. However, when researchers pitted two different adversarially robust models directly against each other (e.g., a robust ResNet-50 versus a robust Wide ResNet-50), the optimization produced completely unrecognizable "monster-looking" patterns [8, 14]. This outcome proved that adversarial robustness alone does not fully replicate the human visual system's generative-discriminative perception [8].

**V1-like Architectures and Inherent Robustness**
*   **Its name and the key claim or contribution:** The "v1net" model demonstrates a bidirectional relationship between biological alignment and noise robustness, claiming that models structured to mimic the primate primary visual cortex (V1) are inherently more robust to attacks [15].
*   **The core approach, mechanism, or supporting evidence:** Researchers engineered a model utilizing a biologically-constrained, classic neuroscience model of V1 as its fixed front-end, followed by standard deep neural network layers trained on standard ImageNet classification tasks [15]. They then evaluated how well a model's alignment with V1 brain scores correlated with its ability to resist image manipulations [15].
*   **Concrete details:** The study found a general correlation where models that are more aligned with V1 data also tend to be more robust [15]. Specifically, the v1net model, without requiring any explicit adversarial training, demonstrated superior robustness to whitebox adversarial attacks and standard image corruptions compared to standardly trained models, suggesting that early biological alignment naturally induces noise robustness [15].

[^1]: [[sources/yt-IWIiR6mjrXY]] [^2]: [[sources/yt-IWIiR6mjrXY]] [^3]: [[sources/yt-IWIiR6mjrXY]] [^4]: [[sources/yt-IWIiR6mjrXY]] [^5]: [[sources/yt-IWIiR6mjrXY]] [^6]: [[sources/yt-IWIiR6mjrXY]] [^7]: [[sources/yt-IWIiR6mjrXY]] [^8]: [[sources/yt-IWIiR6mjrXY]] [^9]: [[sources/yt-IWIiR6mjrXY]] [^10]: [[sources/yt-IWIiR6mjrXY]] [^11]: [[sources/yt-IWIiR6mjrXY]] [^12]: [[sources/yt-IWIiR6mjrXY]] [^13]: [[sources/yt-IWIiR6mjrXY]] [^14]: [[sources/yt-IWIiR6mjrXY]] [^15]: [[sources/yt-IWIiR6mjrXY]]

### Comparisons

## Comparing Approaches to Noise and Robustness in Alignment

Based on the provided sources, comparing different approaches to noise and robustness reveals that while inducing robustness artificially forces models toward biological alignment, it remains an incomplete substitute for true generative perception and early biological architecture.

**Items Compared:**
* Induced Noise Robustness (Adversarial Training/Random Smoothing) vs. Explicit Temporal Predictive Training
* Standard Discriminative Models vs. Adversarially Robust Models (Evaluated via Metamers)
* Robust Models vs. Standard Models vs. Other Robust Models (Evaluated via Controversial Stimuli)
* Explicit Adversarial Training vs. Inherent Biologically-Constrained Architecture (v1net)

**Induced Noise Robustness vs. Explicit Temporal Predictive Training**
Researchers found that representational straightening—a biological hallmark of primate V1 and human perception—can be successfully achieved in feed-forward networks via Adversarial Training (AT) and Random Smoothing (RS) without ever needing explicit predictive optimization on natural movie sequences [1]. This demonstrates that simulating bio-plausible noise at sensory input stages acts as a highly effective, parsimonious alternative to temporal prediction objectives for producing representations aligned with the early visual cortex [1]. A key strength of this approach is that it yields representations capable of generating intervening movie frames through simple linear interpolation, despite the networks never being explicitly trained on temporal trajectories [1].

**Standard Models vs. Adversarially Robust Models (Metamer Evaluation)**
When using the synthesis of deep-layer metamers to evaluate models, standard discriminative visual and auditory networks consistently fail, yielding synthetic stimuli that are completely unintelligible to human observers [2]. In contrast, models explicitly trained for adversarial robustness yield deep-layer metamers that are significantly more recognizable to humans, indicating that optimizing for noise robustness actively bridges a critical gap in perceptual alignment across multiple sensory modalities [2]. However, the sources note significant weaknesses to this approach: the improvement in alignment is incomplete, leaving a substantial recognition gap, and researchers explicitly acknowledge they do not fully understand the exact theoretical mechanisms by which adversarial training produces this perceptual improvement [2].

**Robust Models vs. Standard and Robust Models (Controversial Stimuli)**
The controversial stimuli framework further exposes the limitations and trade-offs of adversarial training by directly pitting models against one another [3]. When an adversarially robust network is contrasted with a standard network, the generated controversial stimuli generally align visually with the robust model's class predictions (e.g., generating dog-like shapes or cat-like textures), showing a clear advantage over standard classification baselines [3]. Yet, a severe limitation is exposed when two distinctly trained robust models are pitted directly against *each other*; the resulting optimization yields completely unrecognizable "monster-looking" patterns [3]. This specific outcome highlights that while adversarial robustness shifts decision boundaries to be more human-like than standard models, it fundamentally fails to fully replicate human perceptual geometry when pushed to its limits [3].

**Explicit Adversarial Training vs. Biologically-Constrained Architecture (v1net)**
While AT and RS artificially induce robustness by modifying the training data or objective with noise, the "v1net" approach demonstrates that robustness can emerge naturally from direct architectural alignment [4]. By incorporating a fixed, biologically constrained classical neuroscience model of V1 at the front-end of the network, v1net achieves superior resistance to white-box adversarial attacks and standard image corruptions compared to standardly trained models [4]. The key trade-off here is computational and procedural: explicitly training models with adversarial examples is a targeted but often opaque optimization process, whereas architectural mimicry of early visual areas inherently confers both high Brain-Score alignment and noise robustness without ever requiring an explicit adversarial training phase [4].



[^4]: [[sources/4]], [[sources/5]]

[^1]: [[sources/yt-IWIiR6mjrXY]] [^2]: [[sources/yt-IWIiR6mjrXY]] [^3]: [[sources/yt-IWIiR6mjrXY]] [^4]: [[sources/yt-IWIiR6mjrXY]]

### Gaps

## Unresolved Questions and Limitations Regarding Noise and Robustness

Based on the provided sources, while inducing noise robustness improves model-brain alignment, several significant gaps and unexplained tensions remain regarding its efficacy and underlying mechanisms.

**The Unexplained Mechanism of Improvement**
The corpus explicitly notes that researchers do not fully understand why making a model robust to adversarial attacks causes its internal representations to become more aligned with human perception [1]. Although robust auditory and visual models yield deep-layer metamers that are significantly more recognizable to human observers than those from standard models, the theoretical or mechanistic reasons linking adversarial noise training to improved perceptual alignment remain an open question [1].

**The Incomplete Resolution of the Recognition Gap**
While adversarial training acts as a partial corrective for representational divergence, the sources identify a clear limitation: it does not completely fix the misalignment problem [1]. A substantial "recognition gap" persists, meaning that even in robust models, deep-layer metamers still deviate from true human perception and are not perfectly recognizable [1]. The corpus leaves unanswered what additional biological constraints or training objectives are required to fully close this gap [1].

**Catastrophic Failure Between Robust Models**
A major unresolved tension is exposed when the controversial stimuli framework is applied to compare two robust models directly against one another [2]. While a robust model produces somewhat human-aligned images when pitted against a standard model, optimizing a stimulus to be controversial between *two different adversarially robust models* yields completely unrecognizable, "monster-looking" patterns [2]. The corpus highlights this as evidence that adversarial training fails to fully replicate human perceptual geometry when pushed to its limits, but it does not address how to overcome this specific failure mode [2].

**The Complex Relationship Between Metamers and Adversarial Vulnerability**
The exact theoretical link between adversarial examples (which fool classifiers) and deep-layer metamers (which reveal representational invariances) is identified as an unresolved complexity [1]. While it is tempting to view metamers as simply the converse of adversarial examples, researchers note this is an incomplete explanation because metamers can be generated independently of any explicit classifier, such as in unsupervised models [1]. The corpus indicates that exploring this relationship in unsupervised contexts is an ongoing area of research, leaving the fundamental connection between noise vulnerability and representational invariance partially unaddressed [1].

[^1]: [[sources/yt-IWIiR6mjrXY]] [^2]: [[sources/yt-IWIiR6mjrXY]]

## Sources cited

- [[sources/yt-IWIiR6mjrXY]]

## Included works

- [[sources/yt-IWIiR6mjrXY]]
