---
schema_version: 1
type: synthesis
slug: 2026-05-20-risksystems-02-physics-informed-sciml-bayesian-uncertainty-quantification-and-model-updating
title: Bayesian Uncertainty Quantification and Model Updating — investigation (2026-05-20-risksystems-02-physics-informed-sciml)
domains:
- risksystems
question: 'Risksystems Q2 of 4 — state of the art in physics-informed machine learning

  (PINNs) and hybrid mechanistic-statistical models (SciML) for built-environment

  deterioration. Frame for Longspan: today the engine treats EUL as a pure cohort-

  Weibull draw blended with engineer judgement, with no first-principles

  deterioration kernel. The question is which mechanisms repay a physics-informed

  extension first (envelope WDR, plumbing-riser pitting, roof UV, parking-deck

  chloride). Specifically: PINNs and neural-ODE methods for chloride ingress in

  reinforced concrete (Fick''s second law + corrosion initiation, Tuutti model);

  carbonation depth modeling; freeze-thaw damage accumulation (Powers, Litvan);

  fatigue and stress-cycle prediction; moisture-transport and wind-driven-rain

  (WDR) penetration on building envelopes including face-sealed precast and EIFS

  (ASHRAE 160, WUFI, HAMFitPlus); corrosion-current modeling for plumbing risers

  (low-pH supply, copper / galvanized / PEX failure modes); EPDM / TPO / SBS

  roofing membrane life prediction from UV / thermal-cycling. Also: hybrid

  mechanistic-statistical (gray-box) models where a physics-based kernel is fit

  per-building from sparse inspection observations using Bayesian inference;

  differentiable physics simulators conditionable on work-order events;

  uncertainty propagation through coupled mechanism models. Relevant venues:

  RILEM TCs, Building and Environment, Cement and Concrete Research, JOSE,

  SciML / DeepXDE / NeuralPDE / NVIDIA Modulus literature.

  '
created_at: '2026-05-20T19:03:39Z'
synthesizes:
- sources/web-2025-10-14-bcb
draft: true
draft_started_at: '2026-05-20T19:03:39Z'
draft_unresolved_claims: 9
last_updated: '2026-05-20T19:03:39Z'
sources_count: 2
---
# Bayesian Uncertainty Quantification and Model Updating — investigation

**Origin question:** Risksystems Q2 of 4 — state of the art in physics-informed machine learning
(PINNs) and hybrid mechanistic-statistical models (SciML) for built-environment
deterioration. Frame for Longspan: today the engine treats EUL as a pure cohort-
Weibull draw blended with engineer judgement, with no first-principles
deterioration kernel. The question is which mechanisms repay a physics-informed
extension first (envelope WDR, plumbing-riser pitting, roof UV, parking-deck
chloride). Specifically: PINNs and neural-ODE methods for chloride ingress in
reinforced concrete (Fick's second law + corrosion initiation, Tuutti model);
carbonation depth modeling; freeze-thaw damage accumulation (Powers, Litvan);
fatigue and stress-cycle prediction; moisture-transport and wind-driven-rain
(WDR) penetration on building envelopes including face-sealed precast and EIFS
(ASHRAE 160, WUFI, HAMFitPlus); corrosion-current modeling for plumbing risers
(low-pH supply, copper / galvanized / PEX failure modes); EPDM / TPO / SBS
roofing membrane life prediction from UV / thermal-cycling. Also: hybrid
mechanistic-statistical (gray-box) models where a physics-based kernel is fit
per-building from sparse inspection observations using Bayesian inference;
differentiable physics simulators conditionable on work-order events;
uncertainty propagation through coupled mechanism models. Relevant venues:
RILEM TCs, Building and Environment, Cement and Concrete Research, JOSE,
SciML / DeepXDE / NeuralPDE / NVIDIA Modulus literature.

**Session:** 2026-05-20-risksystems-02-physics-informed-sciml
**Branch:** Bayesian Uncertainty Quantification and Model Updating

## Synthesis

### Specifics

## Bayesian Uncertainty Quantification and Model Updating

Based on the provided sources, the corpus documents several distinct implementations of Bayesian inference to update deterioration kernels, calibrate physical models, and quantify uncertainty.

**Bayesian Filters for Sequential Deterioration Updating**
*   **Name and Key Claim:** The "Off-line and On-line Bayesian Filtering" framework claims that a tailored on-line particle filter provides a computationally competitive alternative to highly demanding Markov chain Monte Carlo (MCMC) based filters for tracking structural deterioration. [1]
*   **Core Approach:** The method relies on sequentially updating knowledge regarding time-invariant deterioration parameters using continuous monitoring data within either batch (off-line) or recursive (on-line) Bayesian frameworks to quantify full parameter uncertainty. [1] A Gaussian mixture model is utilized across the evaluated filters to accurately approximate the posterior distribution during the resampling process. [1]
*   **Concrete Details:** The framework empirically compares an on-line particle filter, an on-line iterated batch importance sampling filter (utilizing MCMC move steps), and an off-line MCMC-based sequential Monte Carlo filter. [1] These are tested against two specific structural mechanisms: a low-dimensional, nonlinear, non-Gaussian probabilistic fatigue crack growth model updated via sequential crack monitoring, and a high-dimensional, linear, Gaussian random field model simulating corrosion across a beam that is updated with sequential sensor measurements. [1]

**Bayesian Uncertainty Updating for Coupled Heat and Moisture Transport**
*   **Name and Key Claim:** An "Uncertainty Updating" methodology for heterogeneous materials demonstrates that applying Bayesian inference to combine diverse sources of information provides more accurate estimations of heat and moisture fields, which are essential for assessing overall structural durability. [2]
*   **Core Approach:** The approach relies on establishing a probabilistic description of heterogeneous materials and updating the underlying physical models where heat and moisture transfer are evaluated as fundamentally coupled mechanisms. [2]
*   **Concrete Details:** This Bayesian mechanism is tailored to specifically account for uncertainties that consist of particular values associated with individual material characteristics, alongside the spatial fluctuations of those materials. [2]

**Degradation Model Correction via Recursive State Estimation**
*   **Name and Key Claim:** A protocol titled "Degradation Model Correction of Miter Gates Through Synthesis of Hybrid Modeling with Recursive Bayesian State Estimation" details a formal framework for correcting physics-based structural degradation models using observational data. [3]
*   **Core Approach:** The core mechanism centers on synthesizing hybrid deterioration modeling with recursive Bayesian state estimation to continuously update, correct, and refine structural condition predictions over time. [3]
*   **Concrete Details:** The methodology is specifically applied to the degradation of miter gate infrastructure and was documented at the 43rd IMAC Conference on Structural Dynamics as part of broader research advancing digital twins, surrogate modeling, and data-driven structural models. [3]

[^1]: [[sources/[2205.03478] On off-line and on-line Bayesian filtering for uncertainty quantification of structural deterioration]]
[^2]: [[sources/[1102.5239] Uncertainty Updating in the Description of Coupled Heat and Moisture Transport in Heterogeneous Materials]]
[^3]: [[sources/Model Validation and Uncertainty Quantification, Vol. 3]]

[^1]: [[sources/web-2025-10-14-bcb]] [^2]: [[sources/web-2025-10-14-bcb]] [^3]: [[sources/web-2025-10-14-bcb]]

### Comparisons

## Comparing Bayesian Uncertainty Quantification Approaches

Based on the provided sources, the application of Bayesian inference for model updating varies significantly across computational strategies, target deterioration mechanisms, and operational contexts.

**Items Compared:**
*   Off-line and On-line Bayesian Filtering (Particle filters vs. MCMC-based filters)
*   Bayesian Uncertainty Updating for Coupled Heat and Moisture Transport
*   Degradation Model Correction of Miter Gates via Recursive State Estimation

**Contexts of Application**
The evaluated Bayesian frameworks target distinctly different physical mechanisms and structural asset types [1-3]. Bayesian uncertainty updating for heat and moisture transport specifically addresses the durability of heterogeneous materials by modeling coupled environmental transfer processes [2]. This approach directly aligns with building-envelope durability concerns, utilizing probabilistic descriptions to manage uncertainties related to specific material characteristics and their spatial fluctuations [2]. In contrast, off-line and on-line Bayesian filtering approaches are tested on mechanical and structural deterioration, specifically applying these filters to a low-dimensional probabilistic fatigue crack growth model and a high-dimensional random field model for beam corrosion [3]. Alternatively, hybrid degradation model correction utilizes recursive Bayesian state estimation specifically tailored for heavy infrastructure, namely miter gates [1].

**Differences in Stated Claims and Outcomes**
The claims associated with each approach vary depending on whether the primary goal is computational efficiency or parameter accuracy [2, 3]. For coupled heat and moisture transport, the primary claim is that Bayesian inference synthesizes diverse sources of information regarding loading conditions and material parameters to yield a more reliable and accurate estimation of environmental fields [2]. Conversely, the study on off-line and on-line Bayesian filtering emphasizes algorithmic performance, claiming that a tailored implementation of an on-line particle filter successfully achieves competitive accuracy when estimating time-invariant deterioration parameters compared to more complex alternatives [3]. Furthermore, the miter gate research specifically positions recursive Bayesian state estimation as a method to synthesize observational data with hybrid modeling to correct underlying physics-based degradation estimates [1].

**Strengths, Weaknesses, and Trade-offs**
A central trade-off identified across the Bayesian methods is the tension between model dimensionality, predictive accuracy, and computational cost [3]. When sequentially updating structural deterioration models, off-line Markov chain Monte Carlo (MCMC) based sequential Monte Carlo filters are noted for their ability to quantify full parameter uncertainty but are limited by being highly computationally demanding [3]. To mitigate this weakness, the use of a tailored on-line particle filter is presented as a strong, computationally efficient alternative for tracking continuous sensor data [3]. Meanwhile, a core strength of applying Bayesian inference to heat and moisture transport is its rigorous capacity to not only estimate parameter values but to accompany that information with a corresponding evaluation of its credibility, successfully handling the spatial fluctuations inherent in heterogeneous materials [2].

[^1]: [[sources/Model Validation and Uncertainty Quantification, Vol. 3]]
[^2]: [[sources/[1102.5239] Uncertainty Updating in the Description of Coupled Heat and Moisture Transport in Heterogeneous Materials]]
[^3]: [[sources/[2205.03478] On off-line and on-line Bayesian filtering for uncertainty quantification of structural deterioration]]

[^1]: [[sources/web-2025-10-14-bcb]] [^2]: [[sources/web-2025-10-14-bcb]] [^3]: [[sources/web-2025-10-14-bcb]]

### Gaps

## Gaps, Limitations, and Unresolved Tensions in Bayesian Uncertainty Quantification

Based on the provided sources, several limitations, methodological trade-offs, and critical gaps emerge when applying current Bayesian model updating techniques to the specific built-environment deterioration mechanisms requested.

**Analysis Framework:**
*   **Mechanism and Domain Mismatches:** The absence of building-envelope physics and specific MEP mechanism applications.
*   **Continuous Monitoring vs. Sparse Work-Order Events:** The reliance on rich sequential sensor data rather than discrete maintenance logs.
*   **Computational Scalability and Dimensionality:** The unresolved tension between model complexity and processing cost in recursive Bayesian filters.

While Bayesian inference is successfully applied to model coupled heat and moisture transport in heterogeneous materials, the corpus lacks direct application to the specific simulation frameworks requested, such as ASHRAE 160 or WUFI [1]. Furthermore, empirical validations of Bayesian updating are restricted to heavy civil or mechanical infrastructure, such as miter gates, fatigue crack growth, and structural beam corrosion [2, 3]. A careful reader would note that the corpus completely omits how these Bayesian updating frameworks might map to building-specific deterioration mechanisms like plumbing-riser pitting, roof UV degradation, or parking-deck chloride ingress [1-3]. There is also no mention of integrating these Bayesian mechanisms with explicitly differentiable physics simulators, PINNs, or neural-ODEs to update chloride diffusion or carbonation depth [1-3]. 

While the target application seeks to fit models from sparse work-order events and visual inspections, the provided research on Bayesian filtering relies heavily on sequentially rich monitoring data [3]. Specifically, the evaluations of both off-line and on-line Bayesian filters rely on sequential crack monitoring measurements and continuous sensor data across structural beams [3]. The corpus does not address how these recursive Bayesian algorithms would perform or converge if conditioned strictly on highly sparse, irregular, qualitative work-order events instead of dedicated structural health sensor arrays [3].

The research highlights a major unresolved tension regarding the computational cost of Bayesian filtering, particularly when handling high-dimensional problems [3]. While off-line Markov chain Monte Carlo (MCMC) based sequential Monte Carlo filters successfully quantify full parameter uncertainty, they are explicitly noted to be highly computationally demanding [3]. Although a tailored on-line particle filter is proposed as a computationally competitive alternative for estimating time-invariant parameters, this demonstrates an ongoing trade-off between predictive rigor and processing power [3]. Consequently, the sources leave unanswered how scalable these Bayesian uncertainty quantification methods are if expanded to large, system-wide digital twins tracking multiple complex, coupled deterioration kernels simultaneously [3].

[^1]: [[sources/Model Validation and Uncertainty Quantification, Vol. 3]]
[^2]: [[sources/[1102.5239] Uncertainty Updating in the Description of Coupled Heat and Moisture Transport in Heterogeneous Materials]]
[^3]: [[sources/[2205.03478] On off-line and on-line Bayesian filtering for uncertainty quantification of structural deterioration]]

[^1]: [[sources/web-2025-10-14-bcb]] [^2]: [[sources/web-2025-10-14-bcb]] [^3]: [[sources/web-2025-10-14-bcb]]

## Sources cited

- [[sources/web-2025-10-14-bcb]]

## Included works

- [[sources/web-2025-10-14-bcb]]
