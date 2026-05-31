---
schema_version: 1
type: synthesis
slug: 2026-05-30-what-is-the-empirical-evidence-that-impact-of-training-objectives-and
title: Impact of Training Objectives and Spatial Constraints — investigation (2026-05-30-what-is-the-empirical-evidence-that)
domains:
- convergent-ai-brain
question: What is the empirical evidence that representational alignment between biological
  brains and artificial neural networks scales with model competence and capacity?
  Cover encoding-model and RSA/CKA studies (e.g. Yamins, Schrimpf/Brain-Score, Goldstein
  ECoG, TopoLM), the role of training objective and scale, and any reported ceilings
  on alignment.
created_at: '2026-05-30T20:17:35Z'
synthesizes:
- sources/yt-tyYIuvbV2po
last_updated: '2026-05-30T20:17:37Z'
sources_count: 1
draft: true
draft_started_at: '2026-05-30T20:17:37Z'
draft_unresolved_claims: 20
---
# Impact of Training Objectives and Spatial Constraints — investigation

**Origin question:** What is the empirical evidence that representational alignment between biological brains and artificial neural networks scales with model competence and capacity? Cover encoding-model and RSA/CKA studies (e.g. Yamins, Schrimpf/Brain-Score, Goldstein ECoG, TopoLM), the role of training objective and scale, and any reported ceilings on alignment.
**Session:** 2026-05-30-what-is-the-empirical-evidence-that
**Branch:** Impact of Training Objectives and Spatial Constraints

## Synthesis

### Specifics

Based on the provided texts, the corpus documents several distinct ways that training objectives, datasets, and spatial constraints shape the representational alignment of artificial networks with biological brains. 

## Next-Word Prediction as the Key Driver of Language Alignment
Optimizing for next-word prediction specifically aligns model representations with the human language network, distinguishing it from general linguistic competence.
* **Name and key claim:** Predictive Processing Alignment. The core claim is that a model's performance on the specific task of next-word prediction selectively predicts its alignment with human brain activity during language comprehension.
* **Core approach, mechanism, or supporting evidence:** Researchers tested 43 different artificial neural network language models, varying from simple embedding models to complex bidirectional and unidirectional transformers. They compared how well these models predicted human functional magnetic resonance imaging (fMRI) and electrocorticography (ECoG) data against the models' behavioral performance on various computational language benchmarks.
* **Concrete details:** The analysis revealed that performance on the next-word prediction task (measured via perplexity on the WikiText-2 dataset) strongly correlated with brain scores across datasets. In contrast, performance on diverse downstream language tasks from the GLUE benchmark collection did not correlate with overall brain scores. While untrained network architectures showed some baseline ability to predict brain activity, optimizing them via training improved model brain scores by an average of 53%.

## The Necessity of Language-Specific Exposure
Alignment with the human language network relies strictly on exposure to human linguistic data, ruling out explanations based solely on architectural priors or generic sequence modeling.
* **Name and key claim:** Language Specificity of Neural Correlates. The claim is that significant brain-model correlations depend intrinsically on natural language training data, rather than just the self-supervised training objective or the transformer architecture.
* **Core approach, mechanism, or supporting evidence:** Investigators evaluated text-trained transformer language models against control models that utilized the exact same masked-language modeling objective and transformer architecture, but were trained exclusively on protein folding sequences (e.g., ProtBERT, ESM2). 
* **Concrete details:** Replacing natural language training data with non-linguistic protein sequences effectively abolished alignment with human fMRI responses. The non-linguistic control models obtained maximum brain scores of 0.03, whereas even the weakest text-trained baseline model (xlm-roberta) reached a score of 0.23, representing an approximate 8-fold reduction in variance explained (Wilcoxon p < 0.01).

## Topographic Organization and Spatial Smoothness
Incorporating physical, spatial constraints into transformer architectures allows them to develop brain-like functional clustering without heavily sacrificing task performance.
* **Name and key claim:** TopoLM (Topographic Language Model). The key contribution is extending the principle of spatial smoothness into the language domain to replicate the spatio-functional organization of the human cortex in silico.
* **Core approach, mechanism, or supporting evidence:** TopoLM modifies a standard 12-layer transformer by embedding the units of its attention and MLP layers into a 28x28 two-dimensional grid. During training on a 10-billion token subset of FineWeb-Edu, the model jointly optimizes a standard autoregressive cross-entropy task loss alongside a spatial correlation loss. This spatial loss penalizes neighboring units if their activation profiles differ, forcing nearby artificial units to develop similar functional responses.
* **Concrete details:** TopoLM successfully developed spatially clustered semantic responses, including distinct verb- and noun-selective clusters specifically for concrete words, successfully mirroring neuroimaging data. When mimicking the aggregated signal sampling of fMRI, TopoLM achieved a spatial autocorrelation score (Moran's I) of 0.81, compared to only 0.60 for a non-topographic baseline model. This spatial organization came at minimal cost to alignment and performance: while the overall Brain-Score dropped slightly by 2 points (0.78 vs 0.80) and BLiMP scores dropped by 5 points, downstream performance on GLUE actually improved by 3 points (0.68 vs 0.65). 

## Spatial Latent Estimation vs. Object Categorization
In the visual domain, the objective of estimating spatial properties yields representations as brain-like as those trained to categorize objects.
* **Name and key claim:** Spatial Latent Estimation Alignment. This framework challenges the assumption that the primate ventral visual stream is optimized exclusively for object categorization, proposing that estimating spatial latents is equally capable of generating brain-aligned representations.
* **Core approach, mechanism, or supporting evidence:** Researchers utilized 3D graphic engines to generate synthetic image datasets and trained convolutional neural networks (CNNs) to estimate combinations of spatial latents (such as an object's position and pose) versus optimizing them to classify object categories. They then evaluated how well these differently trained networks aligned with primate ventral stream data.
* **Concrete details:** The experiments demonstrated that models trained to estimate just a few spatial latents achieved neural alignment scores comparable to models trained to identify hundreds of distinct object categories. The internal representations of both category-trained and spatial-latent-trained models were highly similar in their early and middle layers, suggesting that non-target latent variability in training data drives convergence toward shared ventral-stream-aligned representations regardless of the explicit target objective.

## Visually Grounded Semantic Objectives
Combining text-based learning with visual grounding produces divergent alignment patterns depending on the proximity to visual or linguistic brain regions.
* **Name and key claim:** Visually Grounded Semantics. This approach asserts that grounding word meanings in visual properties alters encoding performance, revealing that semantic representations in the brain rely partly on visual contexts.
* **Core approach, mechanism, or supporting evidence:** Researchers created a "visually grounded" semantic feature space by pushing collections of images associated with specific words through an ImageNet-trained CNN to extract visual representations. They concatenated these visual features with traditional text-based distributional word embeddings, predicting fMRI responses of subjects listening to natural stories, and compared which feature space best predicted specific cortical areas.
* **Concrete details:** The visually grounded model significantly improved encoding predictions over purely text-based distributional models in regions bordering the visual cortex, such as the Parahippocampal Place Area and the Extrastriate Body Area. Conversely, in higher-order prefrontal language regions like Broca's area, the purely distributional text models maintained a slight predictive advantage over the visually grounded features.

### Comparisons

## Predictive Processing vs. General Task Competence
The corpus contrasts self-supervised language modeling objectives against general multi-task benchmarks to determine which training goal drives brain-likeness.
* **Items Compared:** Next-word prediction objectives (measured via perplexity) versus broad natural language processing competence (measured via the GLUE benchmark).
* **Differences in evidence, outcomes, or stated claims:** A model's performance on the next-word prediction task strongly correlates with its ability to predict human brain activity (brain scores) across multiple fMRI and ECoG datasets [1]. In contrast, a model's performance on diverse language tasks from the GLUE benchmark collection does not correlate at all with its neural alignment [1].
* **Trade-offs or contexts where each applies:** The next-word prediction objective is a contextually sequential task that mirrors the continuous, predictive nature of natural language comprehension in biological brains [1]. The GLUE benchmark applies when researchers want to evaluate an artificial model's competence on specialized, downstream AI tasks, such as entailment or sentiment analysis [1, 2].
* **Strengths and weaknesses:** A major strength of the next-word prediction objective is that optimizing for it selectively drives representations to become highly aligned with human neural processing mechanisms [1]. A weakness of utilizing general task benchmarks like GLUE is that they dissociate from biological reality, meaning that models optimized purely to score well on standard AI leaderboards do not necessarily develop brain-like representations [1].

## Object Categorization vs. Spatial Latent Estimation
In the visual domain, the sources compare different training objectives to challenge the assumption that the ventral visual stream is purely an object-recognition network.
* **Items Compared:** Convolutional neural networks (CNNs) trained to categorize objects versus CNNs trained to estimate spatial latents (such as object pose and position).
* **Differences in evidence, outcomes, or stated claims:** Models trained to estimate just a few spatial latents achieve neural alignment scores in the ventral stream that are comparable to networks trained on hundreds of object categories [3]. Furthermore, the internal representations of the spatial-latent models and the category-trained models are highly similar, particularly in their early and middle layers [3].
* **Trade-offs or contexts where each applies:** Categorization objectives are traditionally applied when modeling the semantic "what" pathway of the ventral stream [3]. Spatial latent estimation applies in contexts where researchers model the brain's ability to localize objects and understand spatial features, which has often been overlooked in ventral stream modeling [3].
* **Strengths and weaknesses:** A strength of comparing these two objectives is that it reveals how non-target latent variability in training data implicitly drives models toward shared, ventral-stream-aligned representations, regardless of the explicit target objective [3]. A weakness of relying solely on object categorization as a modeling objective is that it leads to the false assumption that the ventral stream is optimized exclusively for categorization, ignoring its role in spatial processing [3].

## Topographic Constraints vs. Unconstrained Architectures
The corpus compares language models modified with spatial embedding rules against standard, non-topographic architectures.
* **Items Compared:** The TopoLM architecture (which incorporates a spatial correlation loss on a 2D grid) versus standard, non-topographic transformer language models.
* **Differences in evidence, outcomes, or stated claims:** When trained on naturalistic text, TopoLM naturally develops spatially organized functional clusters that selectively respond to specific linguistic categories (e.g., verb- versus noun-selective regions, or concrete versus abstract word regions) [4]. Non-topographic baseline models completely fail to capture this spatial clustering [4, 5]. Despite this structural difference, both models achieve similar overall functional brain alignment scores on platforms like Brain-Score [4].
* **Trade-offs or contexts where each applies:** TopoLM applies when investigating the macro- and micro-organization of the human cortex, as its spatial smoothness loss acts as an efficiently computable proxy for the biological principle of minimizing neural wiring length [4, 6]. Non-topographic models apply when researchers are only concerned with global functional alignment or raw downstream performance on specific linguistic benchmarks (like BLiMP), where the non-topographic model slightly outperforms TopoLM [4, 7].
* **Strengths and weaknesses:** A key strength of TopoLM is that its spatial constraint successfully forces the emergence of brain-like spatio-functional clusters without sacrificing general task performance or overall neural predictivity, successfully extending visual topographic principles into the language domain [4, 8]. A weakness of standard, unconstrained architectures is their complete inability to predict the spatial topography of neural responses, severely limiting their utility as holistic models of the brain [4, 5].

## Purely Text-Based vs. Visually Grounded Modalities
The sources compare models trained exclusively on text corpora to those that integrate visual or distinct non-linguistic data, highlighting how modality shapes regional alignment.
* **Items Compared:** Distributional text-only embeddings versus visually grounded semantic embeddings (and non-linguistic protein sequence models).
* **Differences in evidence, outcomes, or stated claims:** Models trained on non-linguistic protein folding sequences with the exact same architecture and objective as text models completely fail to align with human brain activity (showing an 8-fold reduction in variance explained), proving that exposure to human language is required [9]. When comparing text-only models to visually grounded models, the visually grounded models significantly improve fMRI predictions in regions bordering the visual cortex (e.g., the Extrastriate Body Area and Parahippocampal Place Area) [10]. However, in higher-order prefrontal language regions like Broca's area, the purely text-based distributional models maintain a predictive advantage [10, 11].
* **Trade-offs or contexts where each applies:** Visually grounded training objectives apply best when modeling brain regions that integrate multisensory concepts and visual contexts with language [10]. Purely text-based objectives apply better when modeling abstract, syntactic, or higher-order semantic processing networks in the prefrontal cortex [11].
* **Strengths and weaknesses:** A strength of multimodal comparison is that it isolates the specific cause of alignment; substituting natural language data with protein data proves that alignment is not a generic architectural artifact but is strictly dependent on the training domain [9]. A weakness of text-only language models is their ecological invalidity; because humans learn language through multimodal interaction rather than just reading text, text-only models inherently fail to capture the visual components of semantic representation in the human brain [10, 12].

[^1]: [[sources/yt-tyYIuvbV2po]] [^2]: [[sources/yt-tyYIuvbV2po]] [^3]: [[sources/yt-tyYIuvbV2po]] [^4]: [[sources/yt-tyYIuvbV2po]] [^5]: [[sources/yt-tyYIuvbV2po]] [^6]: [[sources/yt-tyYIuvbV2po]] [^7]: [[sources/yt-tyYIuvbV2po]] [^8]: [[sources/yt-tyYIuvbV2po]] [^9]: [[sources/yt-tyYIuvbV2po]] [^10]: [[sources/yt-tyYIuvbV2po]] [^11]: [[sources/yt-tyYIuvbV2po]] [^12]: [[sources/yt-tyYIuvbV2po]]

### Gaps

## Equifinality and the Ambiguity of the True Biological Objective
The sources reveal a tension where fundamentally different training objectives can produce highly similar brain-aligned representations, obscuring the true computational goal of biological networks [1]. 
*   **Tension in Ventral Stream Modeling:** In the visual domain, models optimized to estimate spatial latents (such as an object's position and pose) achieve neural alignment scores comparable to those trained on hundreds of object categories [1].
*   **Unresolved Questions:** Because non-target latent variability in training data implicitly drives representations to align regardless of the explicit target objective, the corpus identifies an unresolved gap regarding what the primate ventral stream is actually optimized for [1]. The sources explicitly note that researchers can no longer safely assume the ventral stream is optimized exclusively for object categorization [1].

## Architectural Disconnects in Topographic Models
While topographic models like TopoLM successfully induce brain-like spatial clustering, the corpus identifies severe architectural limitations in how this physical space is simulated [2].
*   **Limitation in Simulating Tissue:** TopoLM relies on discrete, independent two-dimensional grids at each specific layer within a feed-forward architecture [2]. This completely fails to capture the "coherent tissue across the entire system" characteristic of biological brains [2]. 
*   **Gaps in Coverage and Application:** Because the model lacks continuous tissue, it cannot account for spatial transitions between clusters across different depths of processing, leaving researchers unable to accurately model physical brain perturbations such as micro-stimulation [2]. Furthermore, the authors note that the three datasets used to evaluate TopoLM are "far from capturing the topography of language in the brain," highlighting a significant gap in empirical validation that requires entirely new neuroimaging experiments to resolve [2].

## Missing Ecological Modalities and Discourse-Level Meaning
The corpus identifies a gap in how current training objectives fail to capture the full scope of human ecological learning and higher-order narrative comprehension [3].
*   **Unanswered Tensions in Multimodal Grounding:** Although researchers have successfully integrated visual grounding into semantic models to better predict certain cortical responses, they acknowledge an unanswered challenge regarding how to ground language in other critical modalities, such as tactile features [3]. The sources note that good mathematical techniques for extracting tactile features from words do not yet exist [3].
*   **Lack of Discourse-Level Objectives:** Current predictive models operate primarily on local context and word-level predictions, ignoring the "discourse level" of language where narratives involve recurring episodes, scenes, and complex event structures [3]. The corpus explicitly notes a lack of mathematical models or feature extraction methods capable of capturing these discourse-level elements, leaving it unresolved how to align artificial models with the brain's representation of long-form narrative meaning [3].

## The Flawed Assumption of Bijective Information in Convergence
Theoretical frameworks that attempt to explain why models trained on different objectives and modalities converge—such as the Platonic Representation Hypothesis—rely on mathematical proofs that assume "bijective" observation functions [4, 5].
*   **Tension in Cross-Modal Information:** The corpus explicitly highlights the bijective assumption as a major unresolved flaw, because different modalities do not contain perfectly overlapping information [4, 5]. 
*   **Unresolved Questions:** For instance, abstract concepts like "freedom of speech" lack direct visual equivalents, while profound visual experiences like a solar eclipse are "ineffable" and cannot be fully captured by text [4, 5]. Because the training data across distinct modalities is fundamentally lossy and non-bijective, the corpus does not mathematically resolve how models can truly converge on a perfectly shared statistical model of reality, leaving this a significant limitation in current alignment theory [4, 5].

[^1]: [[sources/yt-tyYIuvbV2po]] [^2]: [[sources/yt-tyYIuvbV2po]] [^3]: [[sources/yt-tyYIuvbV2po]] [^4]: [[sources/yt-tyYIuvbV2po]] [^5]: [[sources/yt-tyYIuvbV2po]]

## Sources cited

- [[sources/yt-tyYIuvbV2po]]

## Included works

- [[sources/yt-tyYIuvbV2po]]
