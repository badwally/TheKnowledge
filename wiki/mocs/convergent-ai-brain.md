---
schema_version: 1
type: moc
slug: convergent-ai-brain
domain: convergent-ai-brain
last_updated: '2026-06-02T03:28:40Z'
draft: true
draft_started_at: '2026-06-02T03:28:40Z'
draft_unresolved_claims: 19
---
# convergent-ai-brain — Map of Content

## Overview

Auto-generated from the corpus-constructive research loop. Anchored on the most recent `wiki research` run.

## Key entities

- [[sources/web-2026-05-10-a11]] — Brain-Score Meets Representational Similarity Analysis: a Methodological Convergence in Model-Brain Alignment
- [[sources/pubmed-33595764]] — Comparison of neuronal responses in primate inferior-temporal cortex and feed-forward deep neural network model with regard to information processing of faces
- [[sources/pubmed-40832215]] — Evaluating scientific theories as predictive models in language neuroscience
- [[sources/pubmed-40800971]] — Alignment of auditory artificial networks with massive individual fMRI brain data leads to generalisable improvements in brain encoding and downstream tasks
- [[sources/web-2012-01-01-af2]] — How aligned are different alignment metrics? - arXiv
- [[sources/web-2024-10-30-d27]] — Brain-Score | The MIT Siegel Family Quest for Intelligence
- [[sources/web-2026-06-02-7ba]] — Brain-Score
- [[sources/web-2015-07-01-04f]] — The Platonic Representation Hypothesis - Phillip Isola
- [[sources/web-2025-09-23-25b]] — A Python Toolbox for Representational Similarity Analysis - eLife
- [[sources/web-2024-04-01-307]] — Artificial Neural Network Language Models Predict Human Brain ...

## Key concepts

- **Scaling Laws in Representational Alignment (Competence and Capacity)** — The corpus provides extensive empirical evidence that increasing the parameter count and expressivity (competence) of artificial neural networks systematically improves their alignment with human brain activity and behavior [1, 2].
  - Log-Linear Scaling with Brain Activity: Electrocorticography (ECoG) recordings taken during naturalistic podcast listening demonstrate a log-linear relationship between a model's size (evaluated across the GPT-Neo family from 125M to 20B parameters) and its brain encoding performance, heavily correlating with a larger model's lower perplexity [2]., Expanding language models systematically increases their structural alignment with fMRI data, significantly matching activation in a bilateral temporal-parietal network during naturalistic reading tasks [1].
  - Layer-Specific Structural Shifts: Peak encoding performance for smaller language models occurs in their middle-to-later layers, whereas larger models (e.g., GPT-NeoX-20B) achieve peak encoding performance in relatively earlier layers closer to the input [2]., Different brain regions map to different layers within a model, reflecting a processing hierarchy where encoding in early auditory regions (like the mSTG) peaks before encoding in higher-level semantic/syntactic regions (like BA44 and BA45) [2].
  - Alignment with Behavioral Metrics: Scaling LLaMA models from 7 billion to 65 billion parameters yields significant improvements in predicting human regressive eye saccades during sentence-by-sentence reading [1]., Larger models exhibit reduced sensitivity to "trivial" attention patterns—such as attending exclusively to the immediately preceding word—which do not reflect human cognitive processing or eye movements [1].
- **Methodologies for Measuring Representational Alignment** — Researchers employ diverse computational techniques, such as direct encoding models, geometric similarity analyses, and integrative benchmarks, to evaluate how closely AI representations mirror biological ones [3-5].
  - Encoding Models: Using continuous embeddings from the Whisper speech-to-text model, Goldstein et al. mapped model representations to ECoG data, revealing that "speech" embeddings predict auditory activity in the superior temporal gyrus (STG) while "language" embeddings predict meaning-level activity in Broca's area (IFG) [5]., A novel "Question Answering" encoding approach uses LLMs to score stimuli against 35 qualitative, theory-driven questions, successfully outperforming standard LLM hidden-state baselines at predicting fMRI and ECoG responses [6].
  - Representational Similarity Analysis (RSA) and Centered Kernel Alignment (CKA): CKA measures similarities between the principal components of representational spaces and serves as a sanity check by successfully recovering architectural correspondences between neural networks trained from entirely different random initializations [7]., Standardized Python toolboxes implement RSA using advanced distance metrics—like cross-validated Mahalanobis (crossnobis) or Poisson symmetrized-KL divergence—to reliably handle noise when comparing machine representations to neural data [3].
  - Brain-Score Benchmarking: Brain-Score compares models against dozens of primate visual areas (V1, V2, V4, IT) and behavioral choices, confirming foundational work by Yamins and Schrimpf showing that optimizing deep hierarchical models for behavioral tasks natively generates representations predictive of neural responses in higher visual cortex [4, 8, 9].
- **The Impact of Training Objectives, Architecture, and Fine-Tuning** — A model’s core pre-training objective and spatial constraints strongly drive its eventual alignment to biological brains, whereas post-hoc instruction tuning yields minimal benefits for cognitive plausibility [1, 10, 11].
  - Base Statistical Learning vs. Instruction Fine-Tuning: Fine-tuning base LLMs (like LLaMA) into instruction-tuned variants (such as Alpaca or Vicuna) yields no significant improvement in predicting human fMRI activity or eye-tracking patterns compared to base models of the identical parameter size [1]., While instruction fine-tuning heavily alters a model's internal attention mechanisms when given explicit prompts (e.g., "translate this"), this task-specific sensitivity does not make the model more human-like during naturalistic comprehension [1].
  - Spatial Constraints and Topography: TopoLM modifies a standard transformer language model by introducing a 2D spatial representation for its units combined with a spatial smoothness loss, which acts as a proxy for the biological constraint of minimizing neural wiring length [11]., Through this spatial objective, TopoLM spontaneously develops localized functional clusters corresponding to semantic and syntactic features, closely matching the actual topographical organization of the human cortical language system [11].
  - Convergence and the Platonic Representation Hypothesis: As vision and language models increase in capacity, their kernel representations become increasingly aligned with one another [10]., Theoretical analysis suggests that converging models learn a kernel representation where spatial similarity aligns with the pointwise mutual information (PMI) of the underlying real-world events [10].
- **Limitations, Ceilings, and Discrepancies in Alignment** — Despite remarkable scaling progress, there are empirical ceilings where artificial networks fail to capture specific biological dynamics or exhibit extreme inconsistencies across different evaluation metrics [2, 9, 12].
  - Plateaus in Language Network Scaling: While mSTG and aSTG encoding performance continually scales with model size, empirical ECoG studies show that improvement in encoding performance plateaus around the 13-billion parameter mark for Brodmann area 45 and the temporal pole [2].
  - Missing Visuo-Semantic Features in Higher-Level Vision: While DNNs accurately predict early visual processing (V1-V3) dynamics starting around 66ms, they fail to fully explain human magnetoencephalography (MEG) responses in the higher-level visual cortex (IT/PHC) starting around 146 milliseconds [9]., Human-generated visuo-semantic labels, specifically "object parts" and "basic categories", explain unique variance in higher-level visual cortex that state-of-the-art DNNs entirely miss, highlighting a gap in the features machines and humans rely on for object recognition [9].
  - Inconsistencies Across Alignment Metrics: An extensive evaluation of 80 models across 69 different Brain-Score alignment metrics revealed an average pairwise correlation of only 0.198 between the metrics [12]., Integrating metrics via arithmetic averages masks structural alignment failures, as models with superior behavioral performance (e.g., ImageNet accuracy) can sometimes exhibit worse alignment with actual neural data from the inferior temporal (IT) cortex [12].

## Synthesis pages

_(populated as `wiki research` and `wiki query` runs file syntheses)_
