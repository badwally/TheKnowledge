---
schema_version: 1
type: synthesis
slug: 2026-06-02-what-sets-the-ceiling-on-representational-mutual-information-bounds-a
title: Mutual-Information Bounds and Convergence Limits — investigation (2026-06-02-what-sets-the-ceiling-on-representational)
domains:
- convergent-ai-brain
question: What sets the ceiling on representational alignment between biological brains
  and artificial neural networks? Examine reported alignment ceilings and noise-ceiling
  normalization, mutual-information bounds on cross-system alignment, the persistent
  gap between the best models and brain data, whether alignment saturates with model
  scale, and which architectural or objective differences prevent full convergence.
created_at: '2026-06-02T01:01:17Z'
synthesizes:
- sources/web-2015-07-01-04f
- sources/yt-1_xH2mUFpZw
- sources/yt-FC-m7NRIKRM
last_updated: '2026-06-02T01:01:18Z'
sources_count: 3
draft: true
draft_started_at: '2026-06-02T01:01:18Z'
draft_unresolved_claims: 5
---
# Mutual-Information Bounds and Convergence Limits — investigation

**Origin question:** What sets the ceiling on representational alignment between biological brains and artificial neural networks? Examine reported alignment ceilings and noise-ceiling normalization, mutual-information bounds on cross-system alignment, the persistent gap between the best models and brain data, whether alignment saturates with model scale, and which architectural or objective differences prevent full convergence.
**Session:** 2026-06-02-what-sets-the-ceiling-on-representational
**Branch:** Mutual-Information Bounds and Convergence Limits

## Synthesis

### Specifics

Based on the provided sources, the corpus documents several specific mechanisms and findings regarding the mutual-information bounds and convergence limits of artificial and biological systems.

**The Platonic Representation Hypothesis (PRH) and Kernel Alignment**
*   **Name and Key Claim:** The Platonic Representation Hypothesis posits that neural networks trained with different objectives, on different data, and across entirely different modalities are continuously converging toward a shared statistical model of reality in their representation spaces [1-3]. 
*   **Core Approach:** To mathematically measure this convergence across dissimilar systems, researchers analyze the "kernels" of the models, which define how a specific network measures the distance or similarity between inputs [2]. Researchers calculate alignment by testing whether the kernels of two different models induce the same nearest-neighbor structures for paired data points [2]. 
*   **Concrete Details:** When researchers compared language models to a dedicated computer vision model (DINO) using paired stimuli (e.g., an image of an apple versus the text word "apple"), they found a clear trend of increasing alignment [2]. As language models scaled in size and competency—from a 560-million parameter Bloom model up to a 65-billion parameter LLaMA model—their representational kernels systematically became more aligned with the vision model's kernel [2]. 

**Convergence to Pointwise Mutual Information (PMI)**
*   **Name and Key Claim:** The Convergence to Pointwise Mutual Information framework mathematically demonstrates how contrastive learning objectives force models to recover the shared statistical structure of the latent world [2].
*   **Core Approach:** In an idealized theoretical model where observation functions are bijective and the world is discrete, contrastive learning (using a Noise Contrastive Estimation objective) converges to learning an embedding space where similarity exactly equals the Pointwise Mutual Information (PMI) between observations [2]. Because the observation functions are bijective, the PMI over the observations mathematically equals the PMI over the underlying causal events, meaning any system extracting these causes will ultimately align on identical PMI structures [2]. 
*   **Concrete Details:** To empirically test this, researchers calculated the PMI over pixel color co-occurrences and found it recovered a representational kernel that closely mimics human color perception, such as the LAB color space [2]. This pixel-derived color kernel was also shown to be highly similar to the color kernels learned by completely separate text-only contrastive and predictive language models [2]. 

**Modality-Specific Information Loss (The Ineffability Bound)**
*   **Name and Key Claim:** Modality-specific information loss establishes a theoretical upper bound on cross-system alignment, recognizing that perfect convergence is prevented by concepts that cannot be fully translated across different sensory modalities [2].
*   **Core Approach:** The mathematical proof for perfect PMI convergence relies on the strict assumption that observation functions are bijective, which is not true in the real world [2]. Because information is fundamentally lost or abstracted when the world is projected into a single modality like text or vision, models cannot perfectly align on concepts that one modality lacks the capacity to fully express [2].
*   **Concrete Details:** The sources document specific examples of this limitation, noting that the "ineffable" visual experience of witnessing a total solar eclipse cannot be perfectly captured in text, while highly abstract verbal concepts like "freedom of speech" lack direct visual equivalents [2]. However, the corpus notes that this informational gap shrinks with descriptive density; empirical measurements show that alignment between sentence embeddings and image embeddings is mediocre for short 5-word sentences but substantially increases for detailed 30-word sentences [2].

[^1]: [[sources/yt-FC-m7NRIKRM]] [^2]: [[sources/yt-FC-m7NRIKRM]] [^3]: [[sources/yt-FC-m7NRIKRM]]

### Comparisons

Based on the provided sources, several patterns emerge regarding how different frameworks model the theoretical limits of alignment and the convergence between systems.

## Theoretical PMI Convergence vs. Empirical Kernel Alignment

Different approaches attempt to explain representational convergence either by defining its exact mathematical endpoint or by measuring its relative progress in state-of-the-art models.

**Items Compared:** The mathematical Pointwise Mutual Information (PMI) convergence framework versus the empirical kernel alignment method.

The PMI framework mathematically models the convergence endpoint, demonstrating that contrastive learning objectives over observations naturally converge to the pointwise mutual information of the underlying latent events [1-5]. Empirical kernel alignment, by contrast, evaluates how models practically measure distance between data points by comparing the shared nearest-neighbor structures across their representations [6-8]. 

The primary trade-off between these approaches is the balance of idealized mathematical rigor versus real-world applicability [5]. A key strength of the PMI framework is its ability to formally explain *why* different systems align—namely, that they are recovering the exact same statistical structure of reality [1, 3, 9]. However, a noted weakness is that it relies on strict "toy world" assumptions, such as bijective observation functions and a discrete world, which rarely hold true for complex, real-world sensory inputs [5, 10]. Conversely, empirical kernel alignment has the strength of being directly measurable across vastly different models (such as comparing a 65-billion parameter language model to a vision transformer) without requiring idealized assumptions [11-13]. The weakness of the empirical approach is that it only measures relative convergence between systems—showing that alignment increases alongside model scale and competency—but it cannot definitively prove that the models are arriving at an absolute, "true" platonic representation [14, 15].

## Idealized Cross-System Convergence vs. Modality-Specific Information Bounds

A core tension exists between the hypothesis that systems will perfectly align and the mathematical reality that different senses capture distinct forms of information.

**Items Compared:** The Platonic Representation Hypothesis's claim of continuous, multi-modal convergence versus the theoretical limits of "ineffability" (modality-specific information loss).

The Platonic Representation Hypothesis asserts that disparate AI models and biological systems, despite utilizing entirely different architectures and learning from distinct sensory modalities, will continuously converge upon a shared, unified statistical model of reality [11, 13, 16-18]. In tension with this, the modality-specific information bound argues that perfect convergence is fundamentally impossible because unique information is inevitably lost or abstracted when reality is projected into a single modality [10, 19, 20]. 

This tension is contextualized by the types of concepts being represented [20-22]. The convergence claim excels in contexts where information is easily shared across domains, correctly predicting that scaling up text-only models naturally increases their alignment with vision-only models (like DINO) without the need for explicit multi-modal training [11, 13, 23]. However, a stated weakness of assuming perfect convergence is its failure to account for experiences that cannot be bijectively translated, such as the "ineffable" visual experience of witnessing a total solar eclipse or abstract verbal concepts like "freedom of speech" that lack a direct visual equivalent [19, 20, 22]. A strength of the ineffability bound is that it provides a realistic ceiling on cross-system alignment, explicitly acknowledging that a text representation can never contain the exact same sensory information as an image [20, 22, 24]. Yet, the sources reveal a trade-off regarding context limits: this informational gap is not static, as empirical evidence shows that alignment substantially improves as "descriptive density" increases, with 30-word descriptive paragraphs aligning much better with visual geometries than short 5-word sentences [25, 26].

[^1]: [[sources/web-2015-07-01-04f]] [^2]: [[sources/web-2015-07-01-04f]] [^3]: [[sources/yt-1_xH2mUFpZw]] [^4]: [[sources/yt-1_xH2mUFpZw]] [^5]: [[sources/yt-1_xH2mUFpZw]] [^6]: [[sources/web-2015-07-01-04f]] [^7]: [[sources/yt-1_xH2mUFpZw]] [^8]: [[sources/yt-1_xH2mUFpZw]] [^9]: [[sources/yt-1_xH2mUFpZw]] [^10]: [[sources/yt-1_xH2mUFpZw]] [^11]: [[sources/web-2015-07-01-04f]] [^12]: [[sources/yt-1_xH2mUFpZw]] [^13]: [[sources/yt-1_xH2mUFpZw]] [^14]: [[sources/web-2015-07-01-04f]] [^15]: [[sources/yt-1_xH2mUFpZw]] [^16]: [[sources/web-2015-07-01-04f]] [^17]: [[sources/yt-1_xH2mUFpZw]] [^18]: [[sources/yt-1_xH2mUFpZw]] [^19]: [[sources/web-2015-07-01-04f]] [^20]: [[sources/yt-1_xH2mUFpZw]] [^21]: [[sources/web-2015-07-01-04f]] [^22]: [[sources/yt-1_xH2mUFpZw]] [^23]: [[sources/yt-1_xH2mUFpZw]] [^24]: [[sources/yt-1_xH2mUFpZw]] [^25]: [[sources/yt-1_xH2mUFpZw]] [^26]: [[sources/yt-1_xH2mUFpZw]]

### Gaps

Based on the provided sources, several unresolved tensions, methodological limitations, and theoretical gaps emerge regarding the mutual-information bounds and convergence limits between AI models and biological brains.

## The Bijective Assumption vs. Real-World Ineffability
The theoretical proof of multi-modal convergence relies on strict mathematical assumptions that directly conflict with real-world sensory limitations. The mathematical argument—that contrastive learning models converge to the Pointwise Mutual Information (PMI) of latent causal events—requires the "observation functions" mapping the world to sensory inputs to be strictly bijective [1]. In reality, information is fundamentally lost or abstracted when the physical world is projected into a single modality like text, creating a theoretical boundary to perfect convergence known as modality-specific information loss [1]. The sources highlight this limitation by noting that "ineffable" visual experiences, such as a solar eclipse, cannot be fully translated into words, and highly abstract verbal concepts lack direct visual equivalents [1]. The corpus leaves an unanswered tension regarding how to mathematically quantify this gap, leaving a careful reader to wonder whether disparate systems can ever achieve true platonic alignment if their native modalities are permanently bounded by these non-bijective projection limits [1].

## Converging to Reality vs. Converging to Internet Bias
There is an unresolved tension regarding what exactly the shared representation space actually represents in practice. While the Platonic Representation Hypothesis argues that models are converging toward a shared statistical model of the physical reality, researchers acknowledge the competing possibility that models are simply converging to whatever biases and superficial statistics are reflected on the internet [1]. If the training data lacks true coverage of the physical world and instead primarily contains human sociotechnical biases, the convergent representation might just result in shared "BS machines" rather than an ideal platonic truth [1]. The corpus does not provide a definitive empirical method for disentangling whether increasing model alignment is driven by a genuine physical understanding of the universe or merely the homogenizing effect of massive, shared web-scraping practices [1].

## Metric Dependency and the Illusion of Convergence
A significant methodological gap exists regarding whether cross-system convergence is an objective reality or an artifact of the specific similarity metrics used to measure it. Researchers demonstrate convergence primarily using a specific nearest-neighbor kernel alignment metric, which measures the percentage of shared nearest neighbors between two model embeddings [1]. However, researchers explicitly concede that other standard representational alignment metrics, such as Centered Kernel Alignment (CKA), "work less well" and do not show these convergence trends cleanly [1]. This creates an unanswered tension regarding whether the observed alignment represents a fundamental structural truth about the models, or if the researchers simply "hacked the metric" to find the one evaluation method that produces the desired convergence trend [1]. 

## Unaddressed Theoretical Generalizations
The theoretical bounds and mathematical proofs provided for convergence leave several technical questions unanswered regarding how broadly they apply. The proof demonstrating that models converge to the PMI of underlying latent causes relies on a highly simplified "toy world" model that assumes a strictly discrete set of events generates the observations [1]. The corpus does not address how this theoretical PMI convergence holds up in continuous, highly dimensional real-world environments [1]. Additionally, the theoretical framework explicitly relies on the mathematical properties of the Noise Contrastive Estimation (NCE) objective used in contrastive learning [1]. While empirical tests show that predictive language models also learn similar kernels to contrastive models, a careful reader would want to know if predictive or generative objectives are mathematically guaranteed to converge to this exact same PMI structure, as the specific formal proof provided applies strictly to contrastive learners [1]. Finally, the hypothesis questions but does not resolve the behavior of "specialist systems" that do not require general-purpose representations of the world, leaving a gap in understanding whether convergence only applies to massive foundation models or to specialized architectures as well [2].

[^1]: [[sources/yt-FC-m7NRIKRM]] [^2]: [[sources/yt-FC-m7NRIKRM]]

## Sources cited

- [[sources/yt-FC-m7NRIKRM]]
- [[sources/web-2015-07-01-04f]]
- [[sources/yt-1_xH2mUFpZw]]

## Included works

- [[sources/web-2015-07-01-04f]]
- [[sources/yt-1_xH2mUFpZw]]
- [[sources/yt-FC-m7NRIKRM]]
