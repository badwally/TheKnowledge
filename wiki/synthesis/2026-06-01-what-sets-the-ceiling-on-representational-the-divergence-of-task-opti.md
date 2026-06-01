---
schema_version: 1
type: synthesis
slug: 2026-06-01-what-sets-the-ceiling-on-representational-the-divergence-of-task-opti
title: The Divergence of Task Optimization and Brain Alignment — investigation (2026-06-01-what-sets-the-ceiling-on-representational)
domains:
- convergent-ai-brain
question: What sets the ceiling on representational alignment between biological brains
  and artificial neural networks? Examine reported alignment ceilings and noise-ceiling
  normalization, mutual-information bounds on cross-system alignment, the persistent
  gap between the best models and brain data, whether alignment saturates with model
  scale, and which architectural or objective differences prevent full convergence.
created_at: '2026-06-01T19:42:19Z'
synthesizes:
- sources/yt-em8lPQVtfFM
last_updated: '2026-06-01T19:42:21Z'
sources_count: 1
draft: true
draft_started_at: '2026-06-01T19:42:21Z'
draft_unresolved_claims: 10
---
# The Divergence of Task Optimization and Brain Alignment — investigation

**Origin question:** What sets the ceiling on representational alignment between biological brains and artificial neural networks? Examine reported alignment ceilings and noise-ceiling normalization, mutual-information bounds on cross-system alignment, the persistent gap between the best models and brain data, whether alignment saturates with model scale, and which architectural or objective differences prevent full convergence.
**Session:** 2026-06-01-what-sets-the-ceiling-on-representational
**Branch:** The Divergence of Task Optimization and Brain Alignment

## Synthesis

### Specifics

Based on the provided sources, the corpus documents several specific findings and frameworks demonstrating how optimizing models exclusively for task performance drives a wedge between artificial representations and biological reality.

**The ImageNet-to-IT Decoupling**
*   **Its name and the key claim or contribution:** The Performance-Alignment Trade-off. While it was long held that better object recognition models inherently serve as better models of primate inferotemporal (IT) cortex, recent data reveals this is no longer true; as modern deep neural networks (DNNs) have improved on ImageNet accuracy, they have become progressively *worse* at predicting IT neural responses. [1]
*   **The core approach, mechanism, or supporting evidence:** Researchers tested a "zoo" of 135 different DNNs against primate IT electrophysiology recordings that captured spatially resolved maps of neuronal activity elicited by natural images. [2] By analyzing feature relevance, researchers diagnosed why the models failed to align with biological vision as their task accuracy scaled. [3]
*   **Any concrete details:** The divergence occurs because highly accurate, unharmonized DNNs learn to rely on different visual features than the primate brain does. [4] Using a feature attribution tool called CRAFT, researchers demonstrated that standard ImageNet-trained models heavily exploit background contextual features to achieve high task accuracy, whereas IT neurons are highly selective for foreground semantic features, such as faces. [5]

**Logarithmic Diminishing Returns in Brain-AI Alignment**
*   **Its name and the key claim or contribution:** Diminishing Returns of Task Optimization. Across both vision and language modalities, pure task optimization follows a logarithmic trajectory with respect to brain alignment, where initial performance improvements yield massive alignment gains, but continued optimization leads to a plateau. [6]
*   **The core approach, mechanism, or supporting evidence:** Researchers analyzed 630 artificial models and tracked their representational evolution across training checkpoints, comparing model representations to human fMRI recordings from the Natural Scenes Dataset using Centered Kernel Alignment (CKA). [7] They fit both linear and logarithmic regression models to map the relationship between task benchmark scores and brain alignment. [8]
*   **Any concrete details:** For language models, the relationship between LLM Leaderboard 2 scores and brain alignment was significantly better characterized by a logarithmic fit ($R^2 = 0.80$) than a linear one ($R^2 = 0.78$). [9] Similarly, for vision models evaluated on ImageNet, a logarithmic fit ($R^2 = 0.33$) outperformed a linear fit ($R^2 = 0.28$). [10] This indicates a fundamental mathematical ceiling where models approach benchmark saturation and continue optimizing for the task without substantially increasing their biological alignment. [11]

**The Behavioral-Neural Feature Dissociation**
*   **Its name and the key claim or contribution:** The Dissociation of Functional and DNN Features. DNNs trained strictly for object recognition effectively model responses in scene-selective visual cortex but entirely fail to capture the functional, ecological features that humans actually use to categorize and understand visual scenes. [12]
*   **The core approach, mechanism, or supporting evidence:** Researchers used a variance partitioning analysis to test three distinct feature models against both human fMRI responses and behavioral data: a "functional" model (based on human-assigned labels of actions afforded by a scene), an "object" model, and an ImageNet-trained DNN feature model. [13] 
*   **Any concrete details:** In human behavioral multi-arrangement sorting tasks, the functional action model uniquely explained the largest portion of behavioral variance (37.6%), followed by DNN features (29.0%). [14] However, this behavioral reliance on functional features was completely absent in scene-selective brain regions; in the Parahippocampal Place Area (PPA) and Occipital Place Area (OPA), the DNN model eclipsed the functional model, uniquely explaining 71.1% and 68.9% of the fMRI variance, respectively, compared to a negligible 0.3% and 2.6% for the functional model. [15] This proves that standard DNNs map well to specific visual brain regions but lack the broader ecological and task-relevant representations present in human cognition. [16]

**Neural Harmonization to Correct Divergence**
*   **Its name and the key claim or contribution:** The Neural Harmonizer. Relying purely on different computer vision datasets or tasks is insufficient to reverse-engineer biological vision; the trade-off between task accuracy and neural alignment can be broken by explicitly aligning models with human behavioral psychophysics during training. [17]
*   **The core approach, mechanism, or supporting evidence:** Recognizing that models trained on ImageNet, Taskonomy, or Ecoset fail to reliably predict IT neural activity, researchers developed a plug-and-play training routine called the "neural harmonizer" that forces the DNN to align the representations it uses for object recognition with those that are diagnostic for human observers. [18]
*   **Any concrete details:** Harmonized DNNs proved more accurate at predicting actual primate neural responses than any of the 135 ImageNet-trained, 19 Taskonomy-trained, or 4 Ecoset-trained baseline DNNs tested. [19] Furthermore, harmonization reversed the progressive worsening seen in standard models, yielding a significant positive linear trend between ImageNet accuracy and neural prediction accuracy (e.g., $\rho = 0.37, p < 0.01$ for one monkey's recordings), confirming that aligning to human behavior corrects the divergence caused by pure task optimization. [20]

[^1]: [[sources/yt-em8lPQVtfFM]] [^2]: [[sources/yt-em8lPQVtfFM]] [^3]: [[sources/yt-em8lPQVtfFM]] [^4]: [[sources/yt-em8lPQVtfFM]] [^5]: [[sources/yt-em8lPQVtfFM]] [^6]: [[sources/yt-em8lPQVtfFM]] [^7]: [[sources/yt-em8lPQVtfFM]] [^8]: [[sources/yt-em8lPQVtfFM]] [^9]: [[sources/yt-em8lPQVtfFM]] [^10]: [[sources/yt-em8lPQVtfFM]] [^11]: [[sources/yt-em8lPQVtfFM]] [^12]: [[sources/yt-em8lPQVtfFM]] [^13]: [[sources/yt-em8lPQVtfFM]] [^14]: [[sources/yt-em8lPQVtfFM]] [^15]: [[sources/yt-em8lPQVtfFM]] [^16]: [[sources/yt-em8lPQVtfFM]] [^17]: [[sources/yt-em8lPQVtfFM]] [^18]: [[sources/yt-em8lPQVtfFM]] [^19]: [[sources/yt-em8lPQVtfFM]] [^20]: [[sources/yt-em8lPQVtfFM]]

### Comparisons

Based on the provided sources, several patterns emerge when comparing how different frameworks evaluate the divergence between task-optimized artificial models and biological brains.

## The Trajectory of Divergence: Strict Worsening vs. Logarithmic Plateau
The corpus presents contrasting mathematical frameworks for how biological alignment degrades or stalls as models are increasingly optimized for task performance.

**Items Compared:** The "ImageNet-to-IT Decoupling" framework versus the "Logarithmic Diminishing Returns" framework.
*   **Differences in Claims and Outcomes:** One framework claims a strict *worsening* of alignment, noting that as modern deep neural networks (DNNs) have improved in ImageNet accuracy, they have become progressively worse at predicting primate inferotemporal (IT) cortex responses [1]. Conversely, another framework models this relationship not as a strict worsening, but as a logarithmic plateau of diminishing returns [2]. Under this second framework, initial task improvements yield massive alignment gains, but as models approach benchmark saturation, they continue optimizing for the task without substantially increasing their biological alignment [2].
*   **Contexts where each applies:** The decoupling framework focuses strictly on primate IT electrophysiology and object recognition architectures [1]. The logarithmic diminishing returns framework applies more broadly to massive "zoos" of vision and language models (e.g., 630 models) evaluated against global human fMRI responses to natural scenes [2].

## Pinpointing the Missing Features: Foreground Semantics vs. Functional Affordances
When diagnosing *why* task-optimized models diverge from human cognition, researchers employ different approaches that highlight entirely distinct representational blind spots.

**Items Compared:** Feature attribution methods in object recognition versus variance partitioning in scene categorization.
*   **Differences in Evidence:** In object recognition contexts, feature attribution tools (like CRAFT) reveal that ImageNet-optimized DNNs diverge from biological brains because they heavily exploit background contextual features, whereas primate IT neurons are highly selective for foreground semantic features, such as faces [1]. In scene processing contexts, variance partitioning reveals a different missing component: standard DNNs completely fail to capture the "functional" action affordances (what a human can do in a scene) that humans heavily rely on to categorize visual environments [3].
*   **Strengths and Weaknesses:** A major weakness of relying solely on neural data for alignment is highlighted by the scene categorization framework: DNNs map remarkably well to scene-selective brain regions like the Parahippocampal Place Area (PPA) and Occipital Place Area (OPA), yet this high neural predictivity masks the fact that the models lack the broader ecological and behavioral representations that human cognition utilizes [3].

## Strategies for Correction: Unconstrained Task Optimization vs. Explicit Behavioral Harmonization
To close the persistent gap between models and brains, sources compare relying on diverse task distributions against explicitly forcing behavioral alignment.

**Items Compared:** Scaling diverse training tasks/datasets (e.g., ImageNet, Taskonomy, Ecoset) versus the "Neural Harmonizer" training routine.
*   **Differences in Outcomes:** Relying purely on diverse visual datasets or scaling computer vision tasks is insufficient to reverse-engineer biological vision, as models trained on Taskonomy or Ecoset remain far less effective at explaining neural activity than models explicitly harmonized to human behavior [1]. The Neural Harmonizer, which explicitly forces the DNN's internal representations to align with human behavioral psychophysics during training, successfully reverses the progressive worsening seen in standard models [1].
*   **Trade-offs:** While explicit harmonization successfully produces a positive linear trend between ImageNet accuracy and neural prediction accuracy, it requires the introduction of human psychophysics data during training [1]. This highlights a persistent weakness in the field: researchers have not yet found naturally biologically-plausible learning algorithms or generalized objective functions that achieve this alignment without explicit behavioral co-training [1].

[^1]: [[sources/yt-em8lPQVtfFM]] [^2]: [[sources/yt-em8lPQVtfFM]] [^3]: [[sources/yt-em8lPQVtfFM]]

### Gaps

Based on the provided sources, several patterns emerge regarding the unresolved questions, methodological gaps, and theoretical tensions surrounding why task-optimized models diverge from biological brains.

## The Contradictory Trajectories of Convergence vs. Divergence
The corpus fundamentally disagrees on whether task optimization actually leads to divergence, representing a massive unresolved tension in the literature.
*   While some frameworks report a progressive decoupling—where improved ImageNet accuracy leads to strictly worse predictions of primate inferotemporal (IT) cortex—other large-scale studies argue for convergent evolution, claiming that benchmark performance naturally drives artificial systems toward brain-like alignment [1, 2].
*   The sources suggest this unanswered tension may stem from the neural recording modalities used across different studies [2].
*   Researchers note that studies showing divergence often rely on precise electrophysiology, whereas studies demonstrating convergence often use functional magnetic resonance imaging (fMRI), which provides a very slow and indirect readout of neural populations [2].
*   Consequently, it remains an unresolved question whether the "divergence" phenomenon is a true algorithmic failure of task optimization, or merely a measurement artifact introduced by comparing models to fundamentally different types of biological signals [2].

## Out-of-Distribution (OOD) Vulnerabilities and Generalization
The corpus identifies a significant gap in evaluating how well task-optimized or explicitly "harmonized" models generalize to out-of-distribution (OOD) neural datasets.
*   Researchers note that publicly available neural datasets, such as those on Brain-Score, often consist of images that are out-of-distribution compared to the specific ImageNet data used to train artificial models [2].
*   It remains an open theoretical question whether the progressive divergence of deep neural networks (DNNs) from IT cortex is caused by models learning biologically implausible features, or if the divergence is simply an artifact of distribution shifts between the training data and the experimental stimuli [2].
*   Furthermore, while explicitly forcing models to align with human behavior (neural harmonization) can correct the performance-alignment trade-off on in-distribution data, researchers concede that the benefits of this harmonization drastically fall off for OOD stimuli [2].
*   The corpus leaves unanswered exactly *why* these distribution shifts cause models to fail so severely, identifying rigorous OOD testing as a necessary, missing step to fully resolve the performance-alignment gap [2].

## The "Dark Matter" of Missing Ecological Tasks
A persistent limitation highlighted in the corpus is the field's over-reliance on object recognition as the sole proxy for optimizing artificial vision.
*   Researchers point out that object recognition may not capture the full spectrum of ecological behaviors required by biological systems, referring to the "dark matter of vision" as the missing, undiscovered visual tasks that brains actually perform to create a rich visual experience [3].
*   For instance, task-optimized DNNs completely fail to capture functional action affordances, yet it remains an unresolved tension whether this failure occurs because the models need different training regimes, or because the specific brain regions measured (like scene-selective cortex) simply do not encode these affordances by default [4].
*   The corpus currently lacks a comprehensive exploration of alternative, biologically plausible learning tasks—such as unsupervised ecological exploration or navigation—that might prevent the representational divergence seen in standard supervised models [3, 4].

## Passive Viewing vs. Active Behavioral Engagement
The sources identify an unanswered methodological tension regarding the behavioral state of the biological subjects during neural data collection.
*   Task-optimized artificial models are explicitly trained to perform active classification, yet the neural data they are evaluated against is frequently collected while biological subjects passively view images [4].
*   It remains an unresolved question whether the apparent divergence between AI and brain representations occurs largely because the human or primate subjects are not actively engaged in a contrastive or categorization task during the fMRI or electrophysiology recordings [4].
*   While some researchers have attempted to control for this by giving subjects covert naming tasks, they note that fully unraveling why AI diverges from human cognition may require recording neural activity across multiple, explicit behavioral goals simultaneously—a feat which current datasets do not support [4].

[^1]: [[sources/yt-em8lPQVtfFM]] [^2]: [[sources/yt-em8lPQVtfFM]] [^3]: [[sources/yt-em8lPQVtfFM]] [^4]: [[sources/yt-em8lPQVtfFM]]

## Sources cited

- [[sources/yt-em8lPQVtfFM]]

## Included works

- [[sources/yt-em8lPQVtfFM]]
