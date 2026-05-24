---
type: synthesis
slug: 2026-05-20-risksystems-01-bayesian-hierarchical-survival-expert-judgement-and-prior-elicitation
title: Expert Judgement and Prior Elicitation — investigation (2026-05-20-risksystems-01-bayesian-hierarchical-survival)
domains:
- risksystems
question: 'Risksystems Q1 of 4 — state of the art in Bayesian hierarchical and survival

  models for infrastructure deterioration and capital-asset reliability. Map

  the methodological frontier against the Longspan v1.1 architecture: a

  Bayesian / Weibull / lognormal / Monte Carlo engine with structure-type

  cohort calibration (60-building BC concrete-frame highrise sample, 108-816

  observations per component class), engineer''s point estimate blended 1:1

  with the cohort Weibull EUL draw, cost drawn from the cohort lognormal,

  fallback chain POOLED → jurisdiction → structure-family → structure-type,

  10,000 MC simulations per building. Specifically: partial-pooling

  architectures for sparse multi-jurisdiction component data; engineer-

  judgement-as-prior elicitation (SHELF, Cooke, Hora); Weibull / lognormal /

  Cox PH / gamma-process survival under right-censoring; mixed-effects

  survival with engineering covariates (WDR load, chloride exposure, freeze-

  thaw cycles); posterior predictive checks and calibration diagnostics that

  hold up under licensed-professional sign-off. Seminal authors: Madanat,

  Mishalani, Golabi (DOT pavement/bridge); Frangopol, Faber, Sundararajan

  (structural reliability + LCC); Cooke (expert elicitation); Gelman, Hoffman

  (Bayesian hierarchical practice). Reference systems: HDM-4, AASHTO TAMP,

  Pontis, KANEW, AWARE-P. Recent (2020-2026) refinements explicitly in scope.

  '
created_at: '2026-05-20T17:49:04Z'
synthesizes:
- sources/web-2012-01-01-57d
draft: true
draft_started_at: '2026-05-20T17:49:05Z'
draft_unresolved_claims: 7
---
# Expert Judgement and Prior Elicitation — investigation

**Origin question:** Risksystems Q1 of 4 — state of the art in Bayesian hierarchical and survival
models for infrastructure deterioration and capital-asset reliability. Map
the methodological frontier against the Longspan v1.1 architecture: a
Bayesian / Weibull / lognormal / Monte Carlo engine with structure-type
cohort calibration (60-building BC concrete-frame highrise sample, 108-816
observations per component class), engineer's point estimate blended 1:1
with the cohort Weibull EUL draw, cost drawn from the cohort lognormal,
fallback chain POOLED → jurisdiction → structure-family → structure-type,
10,000 MC simulations per building. Specifically: partial-pooling
architectures for sparse multi-jurisdiction component data; engineer-
judgement-as-prior elicitation (SHELF, Cooke, Hora); Weibull / lognormal /
Cox PH / gamma-process survival under right-censoring; mixed-effects
survival with engineering covariates (WDR load, chloride exposure, freeze-
thaw cycles); posterior predictive checks and calibration diagnostics that
hold up under licensed-professional sign-off. Seminal authors: Madanat,
Mishalani, Golabi (DOT pavement/bridge); Frangopol, Faber, Sundararajan
(structural reliability + LCC); Cooke (expert elicitation); Gelman, Hoffman
(Bayesian hierarchical practice). Reference systems: HDM-4, AASHTO TAMP,
Pontis, KANEW, AWARE-P. Recent (2020-2026) refinements explicitly in scope.

**Session:** 2026-05-20-risksystems-01-bayesian-hierarchical-survival
**Branch:** Expert Judgement and Prior Elicitation

## Synthesis

### Specifics

## Expert Judgement and Prior Elicitation

The corpus identifies several specific frameworks and mechanisms that illustrate how expert judgment is systematically translated into prior probability distributions and structural constraints for infrastructure reliability models.

**Sheffield Elicitation Framework (SHELF)**
*   **Name and key claim:** The Sheffield Elicitation Framework (SHELF) is a standardized package of documents, templates, and software designed to elicit probability distributions for uncertain quantities when hard empirical data are sparse [1].
*   **Core approach:** The framework focuses on eliciting information from a group of experts to synthesize the broader knowledge and opinions of the expert community, though it notes it can be trivially modified for use with a single expert [2]. By providing standardized documentation and guidelines, it aims to enable even untrained facilitators to conduct competent and structured expert elicitations [3].
*   **Concrete details:** SHELF was developed by Tony O'Hagan and Jeremy Oakley at the University of Sheffield [4]. The framework provides computational tools to support the elicitation process, explicitly including a dedicated R software package recently updated to version 1.13.0 [5].

**Expert-Informed Half-Normal Priors for Defect Arrival Models**
*   **Name and key claim:** Expert-parameterized Homogeneous Poisson Processes (HPP) leverage subjective domain knowledge to address severe data scarcity in predicting rail surface defect arrivals [6].
*   **Core approach:** When historical visual inspection data provides only indirect information about defect rates, epistemic uncertainty is explicitly modeled by consulting experts to define the mathematical shape of the prior distribution [7]. 
*   **Concrete details:** In a Hierarchical Bayesian Model (HBM) analyzing 21 Australian railway tracks, engineers utilized expert knowledge to specifically set the scale parameter of a Half-Normal prior distribution [8]. Furthermore, the framework explicitly combined this elicited expert knowledge with statistical estimates of the "oldest unobserved defect" to approximate defect severity risk, ultimately using this blend to optimize the frequency of annual visual inspections [9].

**Domain Expertise Encoding via Multitask Learning**
*   **Name and key claim:** Hierarchical Bayesian Multitask Learning translates engineering domain expertise into mathematical constraints to improve survival analyses across highly heterogeneous vehicle and infrastructure fleets [10].
*   **Core approach:** Rather than relying purely on data-driven inference, this methodology exploits operational domain expertise to constrain the statistical model via targeted assumptions and structured prior distributions [11].
*   **Concrete details:** By naturally encoding this domain knowledge, the model forces different sub-groups—specifically categorized by use-type, component, or operating condition—to appropriately share statistical information [12]. This prior-driven constraint allowed data-poor assets in commercial truck fleets and wind farms to automatically borrow statistical strength from data-rich groups within the hierarchy [13].

**Qualitative Prior Knowledge in Weibull-Tailored Neural Networks (WTNN)**
*   **Name and key claim:** The WTNN architecture utilizes qualitative prior knowledge to enhance Weibull survival modeling when only right-censored observations and proxy indicators are available [14].
*   **Core approach:** The deep neural network is explicitly engineered to incorporate qualitative prior knowledge regarding which time-dependent covariates are the most influential on asset survival [15].
*   **Concrete details:** Designed for analyzing fleets of military vehicles operating in highly variable environments, the WTNN framework incorporates this qualitative prior information in a manner strictly consistent with the mathematical shape and structure of the underlying Weibull distribution, yielding robust and interpretable survival predictions that improve upon traditional regression-based methods [16].

[^1]: [[sources/12]]
[^2]: [[sources/12]]
[^3]: [[sources/12]]
[^4]: [[sources/12]]
[^5]: [[sources/12]]
[^6]: [[sources/8]]
[^7]: [[sources/8]]
[^8]: [[sources/8]]
[^9]: [[sources/8]]
[^10]: [[sources/14]]
[^11]: [[sources/14]]
[^12]: [[sources/14]]
[^13]: [[sources/14]]
[^14]: [[sources/16]]
[^15]: [[sources/16]]
[^16]: [[sources/16]]

[^1]: [[sources/web-2012-01-01-57d]] [^2]: [[sources/web-2012-01-01-57d]] [^3]: [[sources/web-2012-01-01-57d]] [^4]: [[sources/web-2012-01-01-57d]] [^5]: [[sources/web-2012-01-01-57d]] [^6]: [[sources/web-2012-01-01-57d]] [^7]: [[sources/web-2012-01-01-57d]] [^8]: [[sources/web-2012-01-01-57d]] [^9]: [[sources/web-2012-01-01-57d]] [^10]: [[sources/web-2012-01-01-57d]] [^11]: [[sources/web-2012-01-01-57d]] [^12]: [[sources/web-2012-01-01-57d]] [^13]: [[sources/web-2012-01-01-57d]] [^14]: [[sources/web-2012-01-01-57d]] [^15]: [[sources/web-2012-01-01-57d]] [^16]: [[sources/web-2012-01-01-57d]]

### Comparisons

## Comparison of Expert Elicitation and Prior Knowledge Approaches

Based on the provided sources, a comparison of expert elicitation methodologies reveals a spectrum ranging from formal procedural frameworks designed for group synthesis to specific mathematical architectures that directly encode domain knowledge into machine learning and survival models.

**Items Compared:**
*   Sheffield Elicitation Framework (SHELF)
*   Expert-Informed Half-Normal Priors (Homogeneous Poisson Processes)
*   Domain Expertise Encoding via Multitask Learning
*   Qualitative Prior Knowledge in Weibull-Tailored Neural Networks (WTNN)

**Procedural Frameworks vs. Mathematical Encoding**
SHELF operates as a purely procedural and software-supported framework explicitly designed to synthesize the opinions of a group of experts into general probability distributions when hard empirical data are sparse [1]. In contrast, the Half-Normal Prior, Multitask Learning, and WTNN approaches represent specific mathematical encoding strategies where expert judgment is already embedded into the architecture of a statistical or machine learning model [2-4]. A major strength of SHELF is its democratization of the elicitation process; its standardized documentation claims to enable even untrained facilitators to carry out competent, defensible elicitations for difficult policy decisions [1]. However, a fundamental limitation is that SHELF is an elicitation tool rather than a predictive engine; it does not inherently dictate how those elicited distributions must mathematically interact with right-censored data or complex time-dependent covariates [1].

**Parameter-Specific Elicitation vs. Structural Constraint**
When expert knowledge is applied to mathematical models, there is a distinct trade-off between defining specific prior boundaries and defining the overall hierarchy of the system. In the Homogeneous Poisson Process (HPP) rail defect model, expert judgment is used narrowly to quantify epistemic uncertainty by setting the scale parameter of a Half-Normal prior distribution [2]. This acts as a straightforward, interpretable bound based on the maximum expected number of defects per kilometer when historical visual inspection data is indirect [2]. Conversely, Hierarchical Bayesian Multitask Learning leverages domain expertise not just to shape individual parameters, but to define the structural hierarchy itself [3]. Rather than simply bounding a defect rate, the multitask framework uses operational domain expertise to group assets by use-type or operating condition, explicitly forcing those sub-groups to share correlated statistical functions [3]. A key strength of this multitask approach over simple prior parameterization is that it enables automated Bayesian transfer learning, allowing data-poor assets within highly heterogeneous engineering fleets to dynamically borrow statistical strength from data-rich groups [3]. 

**Qualitative vs. Quantitative Prior Knowledge under Censoring**
In demanding operational contexts where only right-censored observation data and proxy indicators are available, the Weibull-Tailored Neural Network (WTNN) offers a fundamentally different application of domain expertise compared to traditional Bayesian frameworks [4]. Instead of eliciting precise quantitative probability distributions (as SHELF aims to do) or quantitative scale parameters (as in the HPP model), the WTNN architecture is explicitly engineered to incorporate *qualitative* prior knowledge regarding which time-dependent covariates are the most influential on asset survival [1, 2, 4]. A documented strength of the WTNN is its ability to preserve the mathematical shape of the Weibull distribution while learning complex covariate relationships that traditional regression-based methods cannot handle [4]. However, this introduces a methodological trade-off: while the HBM and Multitask frameworks rely on transparent Bayesian inference where engineers can explicitly track parameter uncertainty and statistical correlations between sub-groups, the WTNN trades this strict Bayesian interpretability for the flexibility of deep neural networks to produce robust predictions from highly censored proxy data [2-4].

[^1]: [[sources/12]]
[^2]: [[sources/8]]
[^3]: [[sources/14]]
[^4]: [[sources/16]]

[^1]: [[sources/web-2012-01-01-57d]] [^2]: [[sources/web-2012-01-01-57d]] [^3]: [[sources/web-2012-01-01-57d]] [^4]: [[sources/web-2012-01-01-57d]]

### Gaps

## Limitations and Unresolved Tensions in Expert Judgement and Prior Elicitation

Based on the provided sources, several limitations and unanswered questions exist regarding how expert judgment is formally translated into structural reliability models, particularly when mapped against the specific mechanical requirements of the target architecture.

**Absence of Formal Posterior Blending Mechanisms**
While the target Longspan v1.1 architecture requires an engineer's point estimate to be blended 1:1 with a cohort Weibull estimated useful life draw, the provided literature entirely omits any statistical methodology for executing this specific quantitative synthesis [1]. The Sheffield Elicitation Framework (SHELF) provides standardized templates to extract broad probability distributions from groups of experts when hard empirical data are sparse, but it functions primarily as a procedural elicitation tool [2]. It does not document how to mathematically reconcile or dynamically blend these elicited prior distributions with posterior machine-learning outputs [3]. Consequently, a careful reader is left without a formal framework for how to resolve statistical conflicts when an elicited engineer's point estimate diverges significantly from a cohort's empirical survival predictions [4].

**Qualitative vs. Quantitative Constraints Under Censoring**
When dealing with highly right-censored observation data, advanced survival models such as the Weibull-Tailored Neural Network (WTNN) are explicitly designed to incorporate only qualitative prior knowledge regarding which covariates most influence asset survival [5]. The corpus does not document how to inject precise quantitative expert judgments—such as exact survival shape parameters or rigid boundary constraints—into these complex, covariate-driven neural architectures [6]. Similarly, while hierarchical multitask learning leverages domain expertise to group engineering fleets into sub-groups, it uses this knowledge primarily to define the structural topology so data-poor assets can automatically borrow statistical strength, rather than to elicit and set exact quantitative survival parameters [7].

**Lack of Hierarchical Elicitation Protocols**
The sources demonstrate using expert judgment to set simple scale parameters, such as defining the bounds for a Half-Normal prior in single-level point-process models for rail defect arrivals [8]. However, the literature fails to address the cognitive and mathematical complexities of eliciting expert priors across deep, multi-level hierarchical fallback chains like the proposed POOLED → jurisdiction → structure-family → structure-type architecture [9]. The corpus leaves unanswered how an expert or panel of experts utilizing tools like SHELF should practically quantify and distribute their epistemic uncertainty across these deeply nested structural levels [10].

**Validation Limitations Due to Proxy Reliance**
Because current models often lack empirical, non-destructive testing data tracking the continuous time-evolution of physical defect severity, experts are forced to parameterize models using crude statistical proxies [11]. For example, expert-informed Bayesian models currently estimate the expected age of the oldest unobserved defect as a mathematical substitute for measuring actual physical severity risks [12]. The corpus explicitly acknowledges that this reliance on proxies is a temporary stopgap, leaving an unresolved tension regarding how to objectively validate these expert assumptions until true non-destructive testing data can replace them with physics-based severity models [13].

[^1]: [[sources/12]]
[^2]: [[sources/12]]
[^3]: [[sources/12]]
[^4]: [[sources/12]]
[^5]: [[sources/16]]
[^6]: [[sources/16]]
[^7]: [[sources/14]]
[^8]: [[sources/8]]
[^9]: [[sources/12]]
[^10]: [[sources/12]]
[^11]: [[sources/8]]
[^12]: [[sources/8]]
[^13]: [[sources/8]]

[^1]: [[sources/web-2012-01-01-57d]] [^2]: [[sources/web-2012-01-01-57d]] [^3]: [[sources/web-2012-01-01-57d]] [^4]: [[sources/web-2012-01-01-57d]] [^5]: [[sources/web-2012-01-01-57d]] [^6]: [[sources/web-2012-01-01-57d]] [^7]: [[sources/web-2012-01-01-57d]] [^8]: [[sources/web-2012-01-01-57d]] [^9]: [[sources/web-2012-01-01-57d]] [^10]: [[sources/web-2012-01-01-57d]] [^11]: [[sources/web-2012-01-01-57d]] [^12]: [[sources/web-2012-01-01-57d]] [^13]: [[sources/web-2012-01-01-57d]]

## Sources cited

- [[sources/web-2012-01-01-57d]]

## Included works

- [[sources/web-2012-01-01-57d]]
