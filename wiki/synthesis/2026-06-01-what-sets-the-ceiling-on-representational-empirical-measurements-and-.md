---
schema_version: 1
type: synthesis
slug: 2026-06-01-what-sets-the-ceiling-on-representational-empirical-measurements-and-
title: Empirical Measurements and the Persistent Alignment Gap — investigation (2026-06-01-what-sets-the-ceiling-on-representational)
domains:
- convergent-ai-brain
question: What sets the ceiling on representational alignment between biological brains
  and artificial neural networks? Examine reported alignment ceilings and noise-ceiling
  normalization, mutual-information bounds on cross-system alignment, the persistent
  gap between the best models and brain data, whether alignment saturates with model
  scale, and which architectural or objective differences prevent full convergence.
created_at: '2026-06-01T19:42:19Z'
synthesizes:
- sources/web-2016-06-13-621
- sources/web-2023-06-07-3e0
- sources/web-2023-08-23-16e
- sources/web-2024-10-10-2c8
- sources/yt-em8lPQVtfFM
last_updated: '2026-06-01T19:42:20Z'
sources_count: 5
draft: true
draft_started_at: '2026-06-01T19:42:20Z'
draft_unresolved_claims: 11
---
# Empirical Measurements and the Persistent Alignment Gap — investigation

**Origin question:** What sets the ceiling on representational alignment between biological brains and artificial neural networks? Examine reported alignment ceilings and noise-ceiling normalization, mutual-information bounds on cross-system alignment, the persistent gap between the best models and brain data, whether alignment saturates with model scale, and which architectural or objective differences prevent full convergence.
**Session:** 2026-06-01-what-sets-the-ceiling-on-representational
**Branch:** Empirical Measurements and the Persistent Alignment Gap

## Synthesis

### Specifics

Based on the provided sources, several patterns emerge regarding how biological noise and data acquisition limits constrain model-to-brain alignment. 

**Noise-Ceiling Normalization and the Persistent Variance Gap**
*   **Name and Key Claim:** Noise-Ceiling Normalization. The inherent noise in biological recordings dictates that model performance must be evaluated against the maximum predictable variance (the noise ceiling), yet even the best models leave a substantial portion of this explainable variance unaccounted for [1, 2].
*   **Core Approach/Mechanism:** To isolate true model performance from data noise, researchers present the same stimulus multiple times to estimate the internal consistency of the neural responses [1, 3]. Model predictions are then normalized by this noise ceiling, producing a metric that reflects the proportion of true signal the model captures [4]. 
*   **Concrete Details:** In human fMRI language studies, a test story is repeated five times to calculate a regularized noise ceiling ($CC_{max}$) and a normalized correlation score ($CC_{norm}$) [1, 3, 4]. A regularization floor of 0.3 is enforced to prevent poorly-modeled voxels from artificially surpassing a correlation of 1.0 [4]. Despite these normalizations, the most accurate brain-optimized deep neural networks (GNets) capture at most 78% of the explainable variance in human visual areas V1-V4, and as little as 37% on average, demonstrating that a large gap of unmodeled variance persists [2]. Similarly, in primate inferotemporal cortex electrophysiology, early deep neural networks explained roughly 50% of the explainable variance [5, 6]. Researchers note that the absolute upper bound for this metric may be capped by a "species limit," suggesting a model only needs to match an individual primate's neural responses as well as another primate's brain would [7, 8].

**Hemodynamic Blurring and Feedforward/Feedback Confounding**
*   **Name and Key Claim:** Limitations of fMRI Temporal Resolution. The slow temporal dynamics of the blood-oxygenation-level-dependent (BOLD) signal obscure rapid neural events, preventing artificial models from perfectly aligning with the true chronological processing of the brain [9, 10].
*   **Core Approach/Mechanism:** fMRI acts as a low-pass filter, recording a delayed and sluggish representation of local neural activity [9]. To align high-speed artificial network processing with this slow signal, researchers must collapse complex, time-varying neural activity into single static values [10, 11].
*   **Concrete Details:** In fMRI studies of the visual cortex, time-varying BOLD responses to images are condensed into a single "beta value" representing overall activation amplitude [10]. This poor temporal resolution unavoidably mixes rapid feedforward signals with slower top-down feedback effects, fundamentally limiting the ability of strictly feedforward neural networks to perfectly match the data [10]. Furthermore, when modeling continuous stimuli like natural speech, researchers must downsample high-frequency stimulus features (e.g., approximately six words spoken every two seconds) to match the sluggish fMRI acquisition rate (one volume per two seconds) by applying a low-pass antialiasing Lanczos filter [11].

**Signal-to-Noise Ratio (SNR) Challenges in EEG Data**
*   **Name and Key Claim:** EEG Noise Constraints. Human non-invasive EEG recordings suffer from severe signal-to-noise ratio challenges and transient artifacts, requiring modified alignment metrics and limiting the theoretical precision of representational alignment [12-14].
*   **Core Approach/Mechanism:** Standard distance metrics (like Pearson correlation) are highly unstable over the short time windows used in EEG due to high signal noise [14]. Instead, researchers employ classification-based decoding algorithms that focus on task-relevant features to mitigate noise and uncover true representational differences between stimuli [14].
*   **Concrete Details:** EEG alignment studies often replace standard correlation metrics with decoding accuracy derived from a linear SVM classifier (e.g., using 5-fold cross-validation on 80 trials per image across 17 channels) to construct stable Representational Dissimilarity Matrices (RDMs) [14]. However, even with these robust metrics, researchers warn that the combination of high signal noise and relatively small EEG sample sizes inherently limits the maximum precision achievable when aligning artificial models to human brain activity [13].

[^1]: [[sources/web-2023-08-23-16e]] [^2]: [[sources/web-2023-06-07-3e0]] [^3]: [[sources/web-2023-08-23-16e]] [^4]: [[sources/web-2023-08-23-16e]] [^5]: [[sources/yt-em8lPQVtfFM]] [^6]: [[sources/yt-em8lPQVtfFM]] [^7]: [[sources/yt-em8lPQVtfFM]] [^8]: [[sources/yt-em8lPQVtfFM]] [^9]: [[sources/web-2023-08-23-16e]] [^10]: [[sources/web-2023-06-07-3e0]] [^11]: [[sources/web-2023-08-23-16e]] [^12]: [[sources/web-2016-06-13-621]] [^13]: [[sources/web-2016-06-13-621]] [^14]: [[sources/web-2016-06-13-621]]

### Comparisons

Based on the provided sources, several patterns emerge when comparing how different empirical methods and frameworks constrain, measure, and define the persistent alignment gap between artificial models and biological brains.

### Modality Constraints: fMRI vs. EEG vs. Electrophysiology
The choice of neural recording modality imposes distinct trade-offs between temporal precision, spatial coverage, and signal-to-noise ratios, which fundamentally constrain how alignment is measured and interpreted.

**Items Compared:** Functional Magnetic Resonance Imaging (fMRI), Electroencephalography (EEG), and direct electrophysiology (spikes).
*   **fMRI Strengths and Weaknesses:** fMRI provides excellent whole-brain spatial coverage, making it highly suitable for capturing a diversity of representations across multiple visual and semantic areas simultaneously [1]. However, its sluggish hemodynamic response imposes a severe temporal bottleneck, forcing researchers to collapse complex time-varying neural responses into a single static activation value [2]. This temporal blurring mixes rapid feedforward signals with slower top-down feedback effects, inherently limiting the ability of strictly feedforward artificial networks to perfectly match the biological data [2]. Despite these limitations and the use of sophisticated brain-optimized networks, current state-of-the-art models still leave a massive gap, explaining at most 78% of the explainable variance in human visual areas, and often as little as 37% [3].
*   **EEG Strengths and Weaknesses:** In contrast, EEG offers high temporal resolution in the millisecond range, enabling researchers to align models with the rapid chronologies of visual processing, such as early sensory features peaking around 100ms and later semantic features around 150-200ms [4, 5]. The critical trade-off is that non-invasive human EEG suffers from extremely low signal-to-noise ratios, rapid transient artifacts, and a limited number of trials, which restrict the absolute precision of model-to-brain alignment [6, 7].
*   **Electrophysiology:** Direct spike recordings in primates offer high resolution in both space and time, avoiding the hemodynamic blurring of fMRI, yet early deep convolutional models still only captured roughly 50% of the explainable variance in the inferotemporal (IT) cortex [8].

### Metric Adaptations to Data Noise: Linear Mapping vs. Decoding
To cope with the unique noise profiles and temporal properties of different acquisition methods, researchers employ contrasting mathematical approaches to measure representational similarity.

**Items Compared:** Linear regression (used in fMRI and electrophysiology) and classification-based decoding (used in EEG).
*   **Linear Regression:** For relatively stable signals like fMRI BOLD responses or averaged spike counts, researchers typically fit linear regression models to map artificial features directly onto neural activity [9, 10]. Because fMRI feature matrices often exhibit high collinearity and contain many more features than data points, researchers must rely on regularized approaches, like ridge regression, to stabilize the parameter estimates [11].
*   **Classification-based Decoding:** Standard distance metrics like Pearson correlation are highly unstable over the short, noisy time windows typical of EEG recordings [7]. To circumvent this weakness, EEG alignment frameworks replace direct correlation with classification-based decoding [7]. By using algorithms like linear Support Vector Machines (SVMs) to decode representations, researchers force the metric to focus strictly on task-relevant features, effectively mitigating the severe noise inherent to EEG and extracting more stable representational differences between stimuli [7].

### Defining the Upper Bound: Noise Ceilings vs. Species Limits
The theoretical upper limit of expected alignment—the "ceiling"—is framed differently depending on whether researchers focus on internal data reliability or biological variability.

**Items Compared:** Internal noise-ceiling normalization versus the cross-animal "species limit."
*   **Noise Ceilings:** To isolate a model's true performance from the inherent noise of biological recordings, researchers present the exact same stimulus multiple times (e.g., repeating a test story five times in fMRI or showing images 50 times in primate electrophysiology) to calculate an internal consistency score [12, 13]. Model predictions are then normalized against this empirical noise ceiling to reflect the proportion of true, explainable signal the model captures [14, 15]. Because severe noise can cause poorly modeled voxels to produce mathematically impossible normalized correlations above 1.0, researchers must impose artificial regularization floors (e.g., 0.3) to cap the ceiling [15].
*   **The Species Limit:** Alternatively, some researchers argue that variance calculations based purely on single-subject repetitions are insufficient because they ignore natural cross-subject differences [16]. Under this framework, the absolute ceiling for alignment is dictated by the "species limit" [17]. This proposes that an artificial model should only be expected to predict an individual primate's neural responses as accurately as a different primate's brain would, acknowledging that inter-subject biological variation represents an unbridgeable gap for any single universal model [17].

[^1]: [[sources/web-2023-06-07-3e0]] [^2]: [[sources/web-2023-06-07-3e0]] [^3]: [[sources/web-2023-06-07-3e0]] [^4]: [[sources/web-2016-06-13-621]] [^5]: [[sources/web-2016-06-13-621]] [^6]: [[sources/web-2016-06-13-621]] [^7]: [[sources/web-2016-06-13-621]] [^8]: [[sources/yt-em8lPQVtfFM]] [^9]: [[sources/yt-em8lPQVtfFM]] [^10]: [[sources/web-2023-08-23-16e]] [^11]: [[sources/web-2023-08-23-16e]] [^12]: [[sources/yt-em8lPQVtfFM]] [^13]: [[sources/web-2023-08-23-16e]] [^14]: [[sources/web-2023-08-23-16e]] [^15]: [[sources/web-2023-08-23-16e]] [^16]: [[sources/yt-em8lPQVtfFM]] [^17]: [[sources/yt-em8lPQVtfFM]]

### Gaps

Based on the provided sources, several unresolved questions, methodological limitations, and gaps in coverage persist regarding empirical measurements and the alignment gap.

**The Unquantified "Species Limit"**
While researchers can calculate an internal "noise ceiling" by showing the same subject repeated stimuli to measure internal variance, the corpus identifies a major unresolved tension regarding cross-subject and cross-animal variance. 
*   It remains an open question whether models hitting a plateau of roughly 50% explained variance in primate electrophysiology are actually hitting the absolute "species limit" [1]. 
*   The exact mathematical ceiling for how well one biological primate's brain can predict another primate's brain is not yet known, leaving researchers unable to determine if current artificial networks have already reached the maximum biologically realistic alignment score possible [1].

**Disentangling Feedforward vs. Feedback Signals in fMRI**
A persistent limitation in measuring the alignment gap is the inability of functional magnetic resonance imaging (fMRI) to separate distinct temporal processing stages. 
*   Because fMRI tracks sluggish blood-oxygen-level-dependent (BOLD) signals, it unavoidably blurs rapid feedforward neural sweeps together with slower, top-down feedback signals into a single activation value [2]. 
*   Consequently, it remains an unanswered question whether the persistent gap in explainable variance (which leaves up to 22-63% of variance unmodeled in state-of-the-art networks) is due to models lacking proper recurrent feedback mechanisms, or if the data itself is just too temporally blurred to accurately capture representational hierarchies [2-4]. 
*   The corpus notes that researchers must eventually apply these alignment methods to faster brain activity measures, such as direct spike rates, to resolve how representational hierarchies vary dynamically over time [4].

**The Directionality and Mechanics of Cross-Modal Consistency**
While aligning artificial models to human EEG data has been shown to improve the model's ability to predict fMRI data, the exact mechanics of this cross-modal transfer are not fully understood.
*   The corpus points out a gap in testing the reverse direction: researchers acknowledge they have not yet demonstrated whether aligning a model to fMRI data will improve its generalization to EEG data [5].
*   It is currently an unresolved question whether joint training on both EEG and fMRI data simultaneously would establish full bidirectionality and close the alignment gap further [5]. 
*   Additionally, the precise representational dimensions that remain consistent across both the high-temporal-resolution of EEG and the high-spatial-resolution of fMRI have yet to be systematically identified [5].
*   Researchers caution that the high noise floors and relatively small sample sizes inherent to EEG datasets fundamentally cap the precision of model-to-brain alignment, creating methodological ceilings that may obscure true representational similarities [6].

**Unmodeled Non-Neuronal Biological Components**
The corpus highlights an interesting gap in what is actually measured and modeled when evaluating biological brains. 
*   Current empirical measurements and alignment frameworks operate on the fundamental assumption that neuronal spikes are the sole processing units of visual intelligence [7]. 
*   However, discussions in the corpus point out that other brain cells, such as astrocytes, have been found to possess narrower visual receptive fields than neurons and undergo complex state changes conditioned by local glia [7, 8]. 
*   Whether these non-neuronal cells contribute to the "dark" or unmodeled variance in biological representation remains entirely unaddressed by current artificial encoding models, which focus exclusively on approximating neuronal spike rates [7].

**The Theoretical Neglect of Biological Stochasticity**
While the corpus provides mathematical frameworks demonstrating that various representational similarity metrics (like RSA, CKA, and CCA) are equivalent under certain conditions, these proofs rely on an idealized premise.
*   Theoretical proofs of metric equivalence currently treat neural responses as deterministic, noise-free matrices [9]. 
*   Because biological neural networks are highly stochastic, the corpus identifies a theoretical gap regarding how these similarity metrics should be adapted to properly account for biological noise without simply filtering it out, an area that requires further integration between theoreticians and experimental neuroscientists [9].

[^1]: [[sources/yt-em8lPQVtfFM]] [^2]: [[sources/web-2023-06-07-3e0]] [^3]: [[sources/web-2023-06-07-3e0]] [^4]: [[sources/web-2023-06-07-3e0]] [^5]: [[sources/web-2016-06-13-621]] [^6]: [[sources/web-2016-06-13-621]] [^7]: [[sources/yt-em8lPQVtfFM]] [^8]: [[sources/yt-em8lPQVtfFM]] [^9]: [[sources/web-2024-10-10-2c8]]

## Sources cited

- [[sources/web-2023-08-23-16e]]
- [[sources/web-2023-06-07-3e0]]
- [[sources/yt-em8lPQVtfFM]]
- [[sources/web-2016-06-13-621]]
- [[sources/web-2024-10-10-2c8]]

## Included works

- [[sources/web-2016-06-13-621]]
- [[sources/web-2023-06-07-3e0]]
- [[sources/web-2023-08-23-16e]]
- [[sources/web-2024-10-10-2c8]]
- [[sources/yt-em8lPQVtfFM]]
