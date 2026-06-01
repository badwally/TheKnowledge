---
schema_version: 1
type: synthesis
slug: 2026-06-01-do-predictive-or-generative-training-objectives-performance-and-scale
title: Performance and Scale as Primary Drivers of Alignment — investigation (2026-06-01-do-predictive-or-generative-training-objectives)
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
sources_count: 5
draft: true
draft_started_at: '2026-06-01T20:10:50Z'
draft_unresolved_claims: 6
---
# Performance and Scale as Primary Drivers of Alignment — investigation

**Origin question:** Do predictive or generative training objectives produce representations that align with biological neural data better than discriminative objectives at matched task performance? Compare self-supervised versus supervised models, next-token and masked prediction versus classification, contrastive learning, and what the evidence says about the training objective versus architecture or scale as the primary driver of brain-ANN representational alignment.
**Session:** 2026-06-01-do-predictive-or-generative-training-objectives
**Branch:** Performance and Scale as Primary Drivers of Alignment

## Synthesis

### Specifics

Based on the provided sources, several findings demonstrate that model scale, task competency, and the shared structure of the underlying physical world act as primary drivers of representational alignment, often superseding the specific training objectives or architectures used.

**Competency-Driven Kernel Convergence (The "Anna Karenina" Principle)**
*   **Its name and the key claim or contribution:** The "Anna Karenina" principle of representational convergence posits that as models become highly competent at general visual tasks, their internal representations converge to become highly similar, regardless of their specific training objectives or architectures [1]. Conversely, poorly performing models remain dissimilar from one another [1].
*   **The core approach, mechanism, or supporting evidence:** Researchers evaluated 78 different vision models—including Vision Transformers (ViTs) and Convolutional Neural Networks (CNNs) trained via diverse supervised and self-supervised objectives on various datasets—and bucketed them based on their general competency on the Visual Task Adaptation Benchmark (VTAB) [2]. They then measured the "kernel alignment," which quantifies the similarity of the nearest-neighbor structures within the representation spaces of these different models [3].
*   **Concrete details:** When plotted on a UMAP visualization, models in the highest-performing VTAB bins clustered tightly together, exhibiting highly similar representational kernels [4]. This convergence demonstrates that performance competency is the dominant factor controlling representational similarity, overriding differences in architecture or specific training data [5].

**Cross-Modal Alignment through Scale**
*   **Its name and the key claim or contribution:** Cross-modal kernel alignment demonstrates that as unimodal models scale up and improve at their specific tasks, their representations naturally converge with models from entirely different modalities, suggesting they are learning a shared "Platonic" model of the real world [6].
*   **The core approach, mechanism, or supporting evidence:** Researchers measured the kernel alignment between vision models (trained exclusively on images) and language models (trained exclusively on text) by using paired image-caption data (from Wikipedia) to bridge the domains [7]. They evaluated how the language models' next-word prediction competency correlated with their alignment to the vision models [8].
*   **Concrete details:** As language models scale up and improve their next-character prediction log-likelihood (measured in bits per byte), their kernel alignment with vision models reliably increases [9]. For example, the massive 65-billion parameter LLaMA language model exhibited strong representational alignment with the DINO self-supervised vision model [10]. This scaling effect applies to the vision models as well; the larger DINO-Giant model achieved strictly higher alignment with language models than the smaller DINO-Small model [11].

**Task Optimization as a Predictor of Brain-Score**
*   **Its name and the key claim or contribution:** Optimizing models for core categorization tasks serves as a strong initial predictor of their representational alignment with the primate ventral visual stream [12].
*   **The core approach, mechanism, or supporting evidence:** Researchers plotted models' Top-1 performance on the ImageNet object categorization benchmark against their average Brain-Score, an integrative metric measuring how well a model predicts neural spike rates across the visual hierarchy (V1, V2, V4, and IT) and matches human behavioral confusion matrices [13].
*   **Concrete details:** Standard deep learning models that achieve higher ImageNet classification accuracy (such as specific DenseNet and ResNet architectures) also generally yield higher average Brain-Scores, demonstrating that optimizing for a physical world task directly drives biological neural alignment [14]. However, this competency-driven alignment is not infinite; the sources note that at the very highest, state-of-the-art levels of ImageNet performance, this correlation eventually saturates or reverses, indicating an unresolved gap in extreme performance regimes [15].

**Task-Agnostic Feature Emergence and Model Stitching**
*   **Its name and the key claim or contribution:** Task-agnostic feature emergence illustrates that models trained on fundamentally different objectives develop identical intermediate semantic structures, proving that the underlying structure of the physical world shapes representations more than local task goals [16].
*   **The core approach, mechanism, or supporting evidence:** Researchers probed the internal units of deep networks trained on vastly different objectives to determine which input images maximally activated specific artificial neurons [17]. Furthermore, researchers utilized "model stitching" to quantitatively test if the representations learned under different objectives were compatible up to a simple linear transformation [18].
*   **Concrete details:** Networks trained explicitly for scene classification and networks trained for image colorization (predicting missing colors from black-and-white photos) independently developed identical "object detector" neurons that selectively fire for features like "dog faces" or "robins" [19]. In model stitching experiments, researchers proved that the bottom half of a network trained on one task (or dataset) can be linearly stitched to the top half of a network trained on a completely different task with virtually no loss in performance, proving the representations converge on identical underlying information [20].

[^1]: [[sources/8]], [[sources/9]]




[^6]: [[sources/8]], [[sources/9]]





[^12]: [[sources/4]], [[sources/5]]
[^13]: [[sources/4]], [[sources/5]]
[^14]: [[sources/4]], [[sources/5]]
[^15]: [[sources/4]], [[sources/5]]
[^16]: [[sources/8]], [[sources/9]]
[^17]: [[sources/8]], [[sources/9]]
[^18]: [[sources/8]], [[sources/9]]
[^19]: [[sources/8]], [[sources/9]]
[^20]: [[sources/8]], [[sources/9]]

[^1]: [[sources/yt-IWIiR6mjrXY]] [^2]: [[sources/yt-IWIiR6mjrXY]] [^3]: [[sources/yt-IWIiR6mjrXY]] [^4]: [[sources/yt-IWIiR6mjrXY]] [^5]: [[sources/yt-IWIiR6mjrXY]] [^6]: [[sources/yt-IWIiR6mjrXY]] [^7]: [[sources/yt-IWIiR6mjrXY]] [^8]: [[sources/yt-IWIiR6mjrXY]] [^9]: [[sources/yt-IWIiR6mjrXY]] [^10]: [[sources/yt-IWIiR6mjrXY]] [^11]: [[sources/yt-IWIiR6mjrXY]] [^12]: [[sources/yt-IWIiR6mjrXY]] [^13]: [[sources/yt-IWIiR6mjrXY]] [^14]: [[sources/yt-IWIiR6mjrXY]] [^15]: [[sources/yt-IWIiR6mjrXY]] [^16]: [[sources/yt-IWIiR6mjrXY]] [^17]: [[sources/yt-IWIiR6mjrXY]] [^18]: [[sources/yt-IWIiR6mjrXY]] [^19]: [[sources/yt-IWIiR6mjrXY]] [^20]: [[sources/yt-IWIiR6mjrXY]]

### Comparisons

## Comparing Performance and Scale as Drivers of Alignment

Based on the provided sources, the role of scale and performance in driving representational alignment reveals distinct tensions between narrow optimization, general competency, and the limitations of current training paradigms. 

**Items Compared:**
* Narrow Task Optimization (e.g., ImageNet classification) vs. General Task Competency (e.g., VTAB evaluation)
* Cross-Modal Kernel Alignment (Language vs. Vision) vs. Intramodal Model Stitching (Vision vs. Vision)
* The Benefits of Model Scaling vs. The Limitations of Internet Data Curation

**Narrow Task Optimization vs. General Task Competency**
The sources contrast the effects of optimizing for a specific task versus evaluating broad, general competency. Optimizing models for specific, core benchmarks—such as ImageNet top-1 performance in vision or next-word prediction in language—initially serves as a powerful and direct driver to improve alignment with brain data and human behavior [1, 2]. However, a major weakness of narrow task optimization is that this relationship eventually breaks down; at the highest, state-of-the-art levels of ImageNet performance, brain alignment plateaus or even becomes anti-correlated [1, 2]. In contrast, the "Anna Karenina" framework evaluates general visual competency across many diverse tasks (the VTAB benchmark), revealing that models achieving high general competency converge into tightly clustered, highly similar representational spaces regardless of their specific training objective or architecture [3, 4]. The trade-off is that while narrow optimization provides an easy engineering target for initial alignment, it ultimately risks overfitting to the task, whereas achieving general multi-task competency acts as a more robust driver of representational convergence [1-4].

**Cross-Modal Kernel Alignment vs. Intramodal Model Stitching**
To prove that representations converge based on the structure of the world, researchers utilize two distinct evaluation frameworks that offer different strengths and weaknesses [3, 4]. Intramodal model stitching offers a strong functional proof of convergence by demonstrating that the internal representations of models trained on completely different objectives (like image colorization versus scene classification) can be literally cut in half and linearly stitched together without losing performance [3, 4]. This approach proves that networks naturally develop identical intermediate semantic detectors (like "dog face" or "flower" units), but it is restricted to models with architecturally compatible dimensions [3, 4]. Conversely, cross-modal kernel alignment provides the advantage of comparing entirely disparate architectures and modalities—showing that as unimodal vision models (DINO) and language models (LLaMA) improve, their representational geometries converge [3, 4]. However, this cross-modal framework carries significant weaknesses: it requires paired data (like Wikipedia image-caption sets) to measure the alignment, and the convergence only holds for local nearest-neighbor geometries, completely failing to show increasing alignment when evaluated with global structural metrics like Centered Kernel Alignment (CKA) [3, 4].

**The Benefits of Scaling vs. The Biases of Curation**
While scaling up models consistently improves their alignment, the sources identify a critical tension regarding what exactly these scaled models are converging upon [3, 4]. Evidence shows a reliable scaling trajectory: as unimodal models grow larger and more performant (e.g., moving from DINO-Small to DINO-Giant, or scaling up language models to 65 billion parameters), they overlap more in their hypothesis space and their representational kernels become increasingly aligned [3, 4]. Despite these benefits, a major unresolved weakness is the reliance on internet-curated training data [3, 4]. Because these massive models are trained on photos and text downloaded from the internet—which capture biased, human-filtered, and remarkable events rather than a random sampling of physical reality—it remains an open question whether scaling drives models to learn a true "Platonic" representation of the physical world, or merely forces them to perfectly memorize the shared sociological biases of internet data [3, 4]. Furthermore, the alignment driven by current scaling is incomplete, as cross-modal kernel metrics currently cap out around 0.6, leaving a substantial amount of representational variance entirely unexplained [3, 4].

[^1]: [[sources/yt-IWIiR6mjrXY]] [^2]: [[sources/yt-IWIiR6mjrXY]] [^3]: [[sources/yt-IWIiR6mjrXY]] [^4]: [[sources/yt-IWIiR6mjrXY]]

### Gaps

## Unresolved Questions and Limitations Regarding Performance and Scale

Based on the provided sources, several unresolved tensions and critical gaps emerge regarding whether model scaling and task performance truly drive convergence toward biological representations and a "Platonic" model of the world. 

**Key Tensions and Gaps:**
*   The Reversal of Alignment at Extreme Performance
*   Internet Data Bias vs. Physical Reality
*   Local vs. Global Representational Convergence
*   The Ineffability Gap and Bijective Assumptions
*   The Lack of Causal Proof for Cross-Modal Improvement
*   The Failure to Capture Cross-Region Relational Patterns

**The Reversal of Alignment at Extreme Performance**
While early evidence suggested a strong, positive relationship between a model's core task performance (e.g., ImageNet categorization accuracy) and its alignment with brain data, a major unresolved tension exists regarding what happens at extreme scales [1, 2]. Researchers observe that as modern models achieve state-of-the-art performance on ImageNet, their alignment with human behavioral and neural metrics plateaus, falls off, or even becomes anti-correlated [1, 2]. The corpus does not explain the exact mechanisms behind this breakdown, leaving an unanswered question as to why pushing optimization beyond a certain threshold causes representations to diverge from biology rather than converge further [1, 2].

**Internet Data Bias vs. Physical Reality**
The "Platonic Representation Hypothesis" argues that diverse models converge because they are all learning about the same underlying physical world [3]. However, the sources identify a critical limitation: the models exhibiting this convergence are almost exclusively trained on highly curated internet datasets (like Wikipedia image-caption pairs), which selectively capture remarkable, human-filtered events rather than a true random sampling of physical reality [3, 4]. It remains an open, unanswered question whether the observed representational convergence is truly uncovering the fundamental statistical structure of the physical universe, or merely memorizing the shared sociological biases and curation artifacts inherent in internet data [3, 4].

**Local vs. Global Representational Convergence**
A significant technical gap in the scaling hypothesis is that increasing model competency currently only drives alignment in local representational structures, not global ones [5]. When researchers measure alignment using nearest-neighbor similarity metrics, scaled vision and language models appear to converge [5]. Yet, when evaluated using global structural metrics like Centered Kernel Alignment (CKA), the models do not exhibit the same increasing alignment trends [5, 6]. The corpus leaves unanswered why scaling up models successfully aligns their local neighborhoods but fails to converge the overarching, global architecture of their representation spaces [5, 6].

**The Ineffability Gap and Bijective Assumptions**
The theoretical proof demonstrating that contrastive models converge on a shared Pointwise Mutual Information (PMI) kernel relies on the mathematically convenient assumption that observation functions are bijective, meaning each data modality contains complete information about the underlying world events [7, 8]. The sources acknowledge this is a "huge simplification" that fails in practice, noting that language cannot adequately capture ineffable visual experiences (like a solar eclipse), and images struggle to represent abstract concepts (like "freedom of speech") [7, 9, 10]. A careful reader is left without an answer as to how deep models can truly converge on identical, "Platonic" representations of the world when their input modalities suffer from these fundamental, lossy informational bottlenecks [7, 9, 10].

**The Lack of Causal Proof for Cross-Modal Improvement**
While there is a strong correlation showing that language models with better downstream task performance also possess kernels that are more aligned with vision models, the causal direction remains an unresolved gap [11]. The sources explicitly note that researchers have not yet performed the causal experiment of actively fine-tuning a language model to artificially force its alignment with a vision model (like DINO) to see if that intervention directly improves its language modeling capabilities [11]. Consequently, it is unknown whether cross-modal representational alignment actually *causes* better intelligence, or is merely a byproduct of it [11].

**The Failure to Capture Cross-Region Relational Patterns**
Even when scaled models achieve top ranks on traditional alignment benchmarks, the corpus identifies a limitation in their ability to capture brain-wide structural relationships [12]. Standard benchmarking pipelines are criticized for lacking discriminative power, as diverse normative models often appear incorrectly equivalent in their brain alignment [12]. When tested using "Alignment Pattern Analysis"—which evaluates whether a model can reproduce the characteristic functional relationships that one brain region has with all other regions—even top-ranked, highly performant models frequently fail [12]. This exposes an unanswered tension regarding what is required to make models computationally or algorithmically similar to human cortices, as scaling alone does not seem to reliably reproduce these secondary structural alignment patterns [12].

[^1]: [[sources/yt-IWIiR6mjrXY]] [^2]: [[sources/yt-IWIiR6mjrXY]] [^3]: [[sources/yt-IWIiR6mjrXY]] [^4]: [[sources/yt-IWIiR6mjrXY]] [^5]: [[sources/yt-IWIiR6mjrXY]] [^6]: [[sources/yt-IWIiR6mjrXY]] [^7]: [[sources/yt-IWIiR6mjrXY]] [^8]: [[sources/yt-IWIiR6mjrXY]] [^9]: [[sources/yt-IWIiR6mjrXY]] [^10]: [[sources/yt-IWIiR6mjrXY]] [^11]: [[sources/yt-IWIiR6mjrXY]] [^12]: [[sources/yt-IWIiR6mjrXY]]

## Sources cited

- [[sources/yt-IWIiR6mjrXY]]

## Included works

- [[sources/yt-IWIiR6mjrXY]]
