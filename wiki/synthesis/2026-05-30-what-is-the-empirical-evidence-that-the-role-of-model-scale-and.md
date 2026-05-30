---
schema_version: 1
type: synthesis
slug: 2026-05-30-what-is-the-empirical-evidence-that-the-role-of-model-scale-and
title: The Role of Model Scale and Competence in Alignment — investigation (2026-05-30-what-is-the-empirical-evidence-that)
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
last_updated: '2026-05-30T20:17:36Z'
sources_count: 3
draft: true
draft_started_at: '2026-05-30T20:17:36Z'
draft_unresolved_claims: 14
---
# The Role of Model Scale and Competence in Alignment — investigation

**Origin question:** What is the empirical evidence that representational alignment between biological brains and artificial neural networks scales with model competence and capacity? Cover encoding-model and RSA/CKA studies (e.g. Yamins, Schrimpf/Brain-Score, Goldstein ECoG, TopoLM), the role of training objective and scale, and any reported ceilings on alignment.
**Session:** 2026-05-30-what-is-the-empirical-evidence-that
**Branch:** The Role of Model Scale and Competence in Alignment

## Synthesis

### Specifics

Based on the provided sources, several patterns emerge regarding how the physical scale, parameter count, and task competence of artificial neural networks dictate their representational alignment with biological brains. 

## Logarithmic Scaling Laws for Brain Encoding
Scaling up the parameter count of language models yields continuous, logarithmic improvements in their ability to predict human brain activity.
* **Name and key claim:** Logarithmic Scaling Laws for Language Encoding. This framework demonstrates that brain prediction performance improves logarithmically as a language model's size increases [1].
* **Core approach, mechanism, or supporting evidence:** Researchers tested open-source language models from the OPT and LLaMA families, evaluating their ability to predict functional magnetic resonance imaging (fMRI) responses to natural language [1]. 
* **Concrete details:** By scaling models from 125 million to 30 billion parameters, the researchers observed a roughly 15% increase in encoding performance across three human subjects [1]. These highly scaled models reached performance levels nearing the theoretical noise ceiling in specific brain areas, such as the precuneus and higher auditory cortex [1].

## Model Capacity Thresholds and Compression Resilience
While larger models generally align better with the brain, this alignment saturates at modest parameter counts and is highly robust to model compression techniques.
* **Name and key claim:** Saturation of Brain Alignment / Small Language Model (SLM) Equivalence. This finding argues that the minimal model capacity required to capture brain-relevant representations is relatively modest, and that heavy compression does not inherently destroy neural alignment [2].
* **Core approach, mechanism, or supporting evidence:** The study compared the fMRI predictivity of full-precision large language models (up to 14 billion parameters) against small language models (SLMs) and compressed variants subjected to quantization and pruning [2]. 
* **Concrete details:** The experiments revealed that 3 billion parameter SLMs achieved brain predictivity that was indistinguishable from larger LLMs [2]. However, scaling down further to 1 billion parameters caused a substantial degradation in alignment, particularly in semantic language regions [2]. Furthermore, neural predictivity was remarkably robust to compression, with most pruning and quantization methods preserving alignment, except for the GPTQ method which consistently degraded it [2].

## Next-Word Prediction Competence
A model's alignment with human neural processing is driven specifically by its competence at next-word prediction, rather than its general linguistic capabilities.
* **Name and key claim:** Predictive Processing Alignment. This framework posits that performance on next-word prediction tasks selectively predicts a model's "brain score," providing evidence that predictive processing fundamentally shapes human language comprehension [3].
* **Core approach, mechanism, or supporting evidence:** Investigators evaluated 43 different computational models against human fMRI and electrocorticography (ECoG) datasets, and then correlated these models' neural and behavioral alignment scores against their performance on various natural language processing tasks [3].
* **Concrete details:** Model competence at next-word prediction (measured via perplexity on the WikiText-2 dataset) strongly correlated with neural brain scores [3]. Conversely, a model's performance on diverse downstream language tasks from the GLUE benchmark collection showed no correlation with brain scores, indicating a dissociation between general task performance and biological alignment [3].

## Task-Driven Visual Optimization
In the visual domain, a model's competence at core object recognition directly influences its alignment with the primate ventral visual stream.
* **Name and key claim:** Task-Driven Ventral Stream Alignment. This finding claims that artificial neural networks optimized to solve categorization tasks naturally develop internal representations that mimic those found in primate visual cortices [4].
* **Core approach, mechanism, or supporting evidence:** Researchers plotted the categorization accuracy of various deep convolutional neural networks on computer vision benchmarks against their "explained variance" when predicting biological neural responses [4].
* **Concrete details:** Models that achieved higher accuracy on the ImageNet challenge systematically aligned better internally with neural data from the macaque inferior temporal (IT) cortex and area V4 [4]. This optimization-driven competence enabled researchers to map linear combinations of artificial neurons directly to biological firing rates, forming the basis for the 2013-2014 breakthrough in visual encoding models [4].

## The Platonic Representation Hypothesis (PRH)
As models scale in size and competence across different modalities, their representational spaces converge toward a shared mathematical structure.
* **Name and key claim:** The Platonic Representation Hypothesis. This hypothesis claims that neural networks trained on different data and modalities are converging toward a shared, objective statistical model of reality in their representation spaces [5].
* **Core approach, mechanism, or supporting evidence:** Researchers measured convergence across modalities by comparing the kernel alignment (how networks measure distance between data points) of highly competent vision models and language models [6]. 
* **Concrete details:** As language models scale from 7 billion to 70 billion parameters (e.g., the LLaMA family) and improve their language modeling score, their internal kernels become increasingly aligned with the kernels of vision models like DINOv2 [6]. Theoretical analyses suggest the endpoint of this convergence is a representation where spatial similarity perfectly equals the pointwise mutual information (PMI) of the underlying physical events generating the data [7].

## The Aristotelian Representation Hypothesis (Critique of PRH)
The apparent global convergence of highly scaled models may be a statistical artifact caused by the physical size of the networks.
* **Name and key claim:** The Aristotelian View / Scale Confounding. This framework argues that existing metrics used to measure representational similarity are artificially inflated by network scale, masking the true nature of model alignment [8].
* **Core approach, mechanism, or supporting evidence:** The study introduced a permutation-based null-calibration framework to correct spectral measures of representational similarity that are confounded by increases in a model's width and depth [8].
* **Concrete details:** After applying this calibration, the global convergence reported by the Platonic Representation Hypothesis largely disappeared [8]. Instead, the calibrated scores revealed that representations in neural networks are actually converging on shared *local neighborhood relationships*, rather than universal global geometries [8].





[^6]: [[sources/28]], [[sources/29]]

[^1]: [[sources/yt-tyYIuvbV2po]] [^2]: [[sources/yt-tyYIuvbV2po]] [^3]: [[sources/yt-tyYIuvbV2po]] [^4]: [[sources/yt-tyYIuvbV2po]] [^5]: [[sources/yt-tyYIuvbV2po]] [^6]: [[sources/yt-tyYIuvbV2po]] [^7]: [[sources/yt-tyYIuvbV2po]] [^8]: [[sources/yt-tyYIuvbV2po]]

### Comparisons

## Continuous Scaling vs. Capacity Saturation
The provided sources present contrasting evidence regarding whether increasing a model's parameter count continuously yields better brain alignment or if it eventually hits a saturation point.

*   **Items Compared:** Logarithmic scaling laws for language encoding models versus the saturation and compression resilience of small language models (SLMs).
*   **Differences in evidence and outcomes:** Research on scaling laws demonstrates that a language model's ability to predict fMRI brain responses improves logarithmically as its parameter count scales continuously from 125 million to 30 billion parameters [1]. Conversely, other empirical evaluations find that brain alignment actually saturates at modest model capacities; 3 billion parameter SLMs achieve neural predictivity indistinguishable from larger models up to 14 billion parameters [2]. 
*   **Trade-offs and contexts:** The continuous scaling framework suggests that researchers must rely on increasingly massive models to reach theoretical noise ceilings in regions like the precuneus and auditory cortex [1]. The saturation framework, however, applies to contexts where computational efficiency is required, suggesting that highly compressed models can serve as perfectly viable proxies for brain alignment [2].
*   **Strengths and weaknesses:** A strength of the logarithmic scaling approach is its demonstration of robust predictive gains at the 30 billion parameter scale, but it carries the weakness of assuming that massive parameter counts are strictly necessary for biological alignment [1]. The SLM saturation approach reveals the strength of alignment resilience to most quantization and pruning methods [2]. However, it also identifies a critical lower-bound weakness: extreme compression down to 1 billion parameters causes substantial degradation in predicting semantic language regions, and specific compression techniques like GPTQ consistently destroy neural predictivity [2].

## Language Prediction vs. Visual Categorization Competence
The corpus highlights how alignment scales with task competence across different modalities, contrasting self-supervised predictive language objectives with supervised visual categorization.

*   **Items Compared:** Next-word predictive processing in language models versus task-driven object categorization in vision models.
*   **Differences in claims and mechanisms:** In the language domain, a model's competence specifically at predicting the next word (perplexity) strongly correlates with its neural alignment to human fMRI and ECoG data, whereas its competence on other broad downstream NLP tasks (like the GLUE benchmark) does not [3]. In the visual domain, performance accuracy on core object recognition tasks (such as ImageNet) systematically predicts how well a model aligns with neural data from the primate ventral visual stream (e.g., IT and V4 cortex) [4, 5].
*   **Trade-offs and contexts:** The language framework requires models to be trained using a self-supervised, sequential objective that mirrors the continuous nature of natural speech and text comprehension [3]. The visual framework has historically relied on supervised, categorically labeled datasets (like ImageNet) to force models to learn task-relevant spatial and semantic features [4]. 
*   **Strengths and weaknesses:** A major strength in both domains is the normative finding that optimizing an artificial network for a specific behavioral competence naturally forces its internal representations to resemble biological mechanisms [3, 4]. A noted weakness of the visual categorization approach is its reliance on supervised labels, which lacks ecological validity compared to how biological organisms learn; however, this is being addressed by newer unsupervised task-driven models [4, 6]. A specific weakness noted in the language domain is that while next-word prediction is highly predictive of brain alignment, performance on curated NLP benchmarks completely dissociates from brain scores, meaning standard AI benchmarks do not accurately reflect biological competence [3].

## Global Platonic Convergence vs. Local Aristotelian Neighborhoods
The sources contrast two theoretical hypotheses regarding what happens to representational geometry as models scale in competence and capacity.

*   **Items Compared:** The Platonic Representation Hypothesis (PRH) versus the Aristotelian Representation Hypothesis.
*   **Differences in evidence and stated claims:** The PRH claims that as neural networks scale in capacity and competence across different modalities (such as vision and language), their internal representations globally converge toward a shared, objective statistical model of reality [7, 8]. The Aristotelian view challenges this, claiming that the apparent global convergence measured by spectral metrics is an illusion artificially inflated by increases in model width and depth [9]. 
*   **Trade-offs and contexts:** The PRH is used to explain cross-modal phenomena, such as why the geometric kernel of a highly competent vision model (like DINOv2) increasingly aligns with the kernel of a large language model (like LLaMA) as both models scale up [7, 8]. The Aristotelian framework is applied as a rigorous statistical correction context, utilizing a permutation-based null-calibration tool to evaluate whether representations are truly converging or merely benefiting from scale confounds [9].
*   **Strengths and weaknesses:** The primary strength of the PRH is that it provides a unified mathematical theory for alignment, proposing that all competent learners converge on representations where spatial similarity equals the pointwise mutual information (PMI) of underlying physical events [7, 10]. Its critical weakness, however, is its reliance on uncalibrated global spectral measures like Centered Kernel Alignment (CKA), which are highly sensitive to raw parameter scale [9]. The Aristotelian hypothesis resolves this weakness by applying a calibration framework, concluding that true representational convergence does not occur at the global geometric level, but is instead restricted strictly to shared local neighborhood relationships [9].

[^1]: [[sources/yt-tyYIuvbV2po]] [^2]: [[sources/yt-tyYIuvbV2po]] [^3]: [[sources/yt-tyYIuvbV2po]] [^4]: [[sources/yt-tyYIuvbV2po]] [^5]: [[sources/yt-tyYIuvbV2po]] [^6]: [[sources/yt-tyYIuvbV2po]] [^7]: [[sources/yt-tyYIuvbV2po]] [^8]: [[sources/yt-tyYIuvbV2po]] [^9]: [[sources/yt-tyYIuvbV2po]] [^10]: [[sources/yt-tyYIuvbV2po]]

### Gaps

## The Tension Between Continuous Scaling and Capacity Saturation
The provided sources reveal a direct empirical contradiction regarding whether brain alignment improves continuously with model scale or if it hits a hard capacity ceiling early on.
* **Tensions in Scaling Trajectories:** On one hand, researchers report logarithmic scaling laws where fMRI encoding performance continuously improves as language models scale from 125 million to 30 billion parameters [1]. On the other hand, separate evaluations demonstrate that alignment saturates at much smaller scales, showing that 3 billion parameter small language models (SLMs) achieve neural predictivity identical to 14 billion parameter models [2].
* **Unresolved Questions:** The sources do not resolve why a 3 billion parameter threshold is sufficient for alignment in some studies while others show continued gains up to 30 billion parameters [1, 2]. Furthermore, the corpus does not explain the mechanistic changes that occur within the network when capacity drops below 1 billion parameters, which causes a sudden, steep degradation in predicting semantic language regions [2].

## The Dissociation Between Task Competence and Brain Alignment
A major tension exists in how "competence" is defined, as the corpus highlights a severe dissociation between a model's performance on artificial intelligence benchmarks and its alignment with human neural activity.
* **Tensions in Task Competence:** While a model's competence at self-supervised next-word prediction strongly correlates with its brain score, its performance on broad downstream language tasks (such as the GLUE benchmark) shows no correlation with neural alignment [3]. This dissociation is further complicated by model compression; techniques like quantization degrade a model's competence in discourse, syntax, and morphology, yet its brain predictivity remains largely unchanged [2].
* **Unresolved Questions:** The corpus leaves it completely unanswered why human neural recordings fail to reflect the loss of higher-order linguistic competencies (like discourse and complex syntax) that are clearly degraded in compressed models [2]. It remains an open question whether standard neural alignment metrics are simply blind to these advanced cognitive competencies, or if current brain recording techniques like fMRI lack the resolution to capture them [2, 3].

## The Illusion of Convergence vs. True Representational Alignment
Theoretical debates in the sources reveal that the mathematical metrics used to claim that larger models converge on brain-like representations may be fundamentally flawed.
* **The Convergence Illusion:** The Platonic Representation Hypothesis relies on spectral metrics like Centered Kernel Alignment (CKA) to argue that as models scale in capacity, their representations globally converge toward a shared statistical reality [4, 5]. However, the Aristotelian critique identifies a critical flaw, demonstrating that these representational similarity scores are artificially inflated by the sheer width and depth of scaled models [6].
* **Unresolved Questions:** Because global spectral measures are confounded by network scale, it remains entirely unresolved whether scaling actually drives neural networks to form a universal, platonic geometry, or if this is merely a statistical artifact of measuring massive parameter spaces [5, 6]. The corpus does not provide a consensus on a scale-invariant metric that can definitively prove global convergence without being biased by parameter count [6].

## What the Corpus Does NOT Address
Beyond explicit contradictions, the sources leave several critical gaps regarding the absolute limits of scaling and ecological validity.
* **Gaps in Multimodal and Ecological Scaling:** The sources extensively evaluate the scaling of models trained on massive text corpora or static images independently [1, 4, 5]. However, the corpus does not address how scaling would affect brain alignment for models trained on ecologically valid, multimodal, and embodied data, which represents how human brains actually develop and learn [7].
* **Unanswered Ceilings on Alignment:** While highly scaled 30 billion parameter models approach the theoretical noise ceiling in specific regions like the precuneus and higher auditory cortex, the corpus does not address whether continued scaling will ever close the performance gap in all other language and cognitive regions [1]. A careful reader is left wondering if raw parameter scaling has a hard upper bound for biological alignment, necessitating fundamentally different, spatiotemporal architectures to fully match the temporal dynamics of human brain activity [1, 7].

[^1]: [[sources/yt-tyYIuvbV2po]] [^2]: [[sources/yt-tyYIuvbV2po]] [^3]: [[sources/yt-tyYIuvbV2po]] [^4]: [[sources/yt-tyYIuvbV2po]] [^5]: [[sources/yt-tyYIuvbV2po]] [^6]: [[sources/yt-tyYIuvbV2po]] [^7]: [[sources/yt-tyYIuvbV2po]]

## Sources cited

- [[sources/yt-tyYIuvbV2po]]

## Included works

- [[sources/yt-tyYIuvbV2po]]
