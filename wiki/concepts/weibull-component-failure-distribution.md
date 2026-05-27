---
schema_version: 1
type: concept
slug: weibull-component-failure-distribution
canonical_name: Weibull Component Failure Distribution
domains:
- condo-capital-infra
created_at: '2026-05-11T22:04:18Z'
last_updated: '2026-05-11T22:04:18Z'
---
# Weibull Component Failure Distribution

## Summary

The Weibull distribution is a two-parameter continuous probability distribution from reliability engineering used to model the time-to-failure of capital components in condominium reserve-fund planning [[sources/docx-818ed0a0ce55]]. It replaces the deterministic Estimated Useful Life (EUL) convention — in which a component's replacement is scheduled as `YearOfInstallation + EUL` — with a probability-density function over failure time whose shape parameter captures the failure-mode regime (infant mortality, random failures, wear-out) and whose scale parameter captures the characteristic life [[sources/docx-818ed0a0ce55]]. In the condo-capital-infra engine architecture, the Weibull is the statistical primitive that turns scalar EUL outputs into probability scores such as "75% probability that Elevator A will require major modernization within the next 48 months" — the methodological core distinguishing the engine from CAI-deterministic vendor practice [[sources/docx-818ed0a0ce55]].

## Key claims

- The probability density function (PDF) for a component's failure over time `t` under the Weibull distribution is `f(t; λ, k) = (k/λ) · (t/λ)^(k−1) · exp(−(t/λ)^k)`, where `λ` is the scale parameter (the characteristic life of the component) and `k` is the shape parameter (indicating the failure mode) [[sources/docx-818ed0a0ce55]].
- The shape parameter `k` controls the failure-mode regime: `k > 1` corresponds to wear-out failures (the probability of failure increases as the asset ages); a shape parameter `k ≈ 3.5` corresponds to a strongly age-dependent wear-out regime in which failure becomes significantly more likely as the asset approaches its characteristic life `λ` [[sources/docx-818ed0a0ce55]].
- The scale parameter `λ` is the characteristic life of the component — the time at which 63.2% of components are expected to have failed under the Weibull cumulative distribution [[sources/docx-818ed0a0ce55]].
- Building components do not fail on a fixed schedule but rather follow a probability distribution influenced by usage patterns, maintenance quality, and environmental stresses, making the Weibull's hazard-rate framing more representative of empirical failure behavior than the deterministic EUL convention [[sources/docx-818ed0a0ce55]].
- The Weibull is frequently employed in reliability engineering to describe the life of building components, and a software solution utilizing this distribution can provide condo boards with a probability score (e.g., "75% probability that Elevator A will require a major modernization within the next 48 months") rather than a binary deterministic replacement date [[sources/docx-818ed0a0ce55]].
- For an HVAC asset such as a rooftop unit with shape parameter `k ≈ 3.5`, the probability of failure increases sharply as the asset's age approaches the characteristic life `λ` — a hazard-rate signature directly usable for component-level prior calibration in the condo-capital-infra engine [[sources/docx-818ed0a0ce55]].
- The Weibull replaces a deterministic EUL point estimate with a full failure-time distribution, providing the statistical primitive on which Monte Carlo aggregation and reserve-fund confidence intervals are built [[sources/docx-818ed0a0ce55]].

## Sources

- [[sources/docx-818ed0a0ce55]]

## Related

- [[concepts/probabilistic-reserve-modeling]]
- [[concepts/six-probabilistic-components]]
- [[concepts/monte-carlo-reserve-confidence-intervals]]
- [[concepts/reserve-fund-contribution-smoothing]]
- [[concepts/ml-fault-detection-mechanical-systems]]
- [[concepts/tech-enabled-reserve-study-firm]]
- [[entities/cai-reserve-study-standards]]
