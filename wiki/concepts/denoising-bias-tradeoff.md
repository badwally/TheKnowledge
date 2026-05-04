---
type: concept
slug: denoising-bias-tradeoff
canonical_name: Denoising-bias trade-off in trend filtering
domains:
  - trading-and-markets
---

# Denoising-bias trade-off in trend filtering

## Summary

In moving-average trend filtering, the choice of the lag-window width T = n∆ is governed by a trade-off between maximising denoising — which improves with n via the central limit theorem — and minimising bias, which worsens with n because the n-period average estimator is itself biased and converges to the average value of the trend in the long-window limit [[sources/pdf-5ef2018823c8]].

## Key claims

- The main advantage of using a moving-average filter is the reduction of noise due to the central limit theorem [[sources/pdf-5ef2018823c8]].
- For the limit case n → ∞, the signal is completely denoised but corresponds to the average value of the trend, and the estimator is biased [[sources/pdf-5ef2018823c8]].
- In trend filtering practitioners face a trade-off between denoising maximisation and bias minimisation, and the calibration problem is the choice of the lag window T = n∆ [[sources/pdf-5ef2018823c8]].
- Bruder, Dao, Richard, and Roncalli identify two main calibration solutions: the first based on prediction error and the second using a benchmark estimator; another way to determine the optimal parameter T* is to take into account the dynamics of the trend [[sources/pdf-5ef2018823c8]].
- Even within the bias-aware framework, µ̂_t (the rate-of-change estimator) is itself a biased estimator of µ_t, with bias that increases with the volatility of the process σ_t; the unbiased version is µ̂_t = (1/2) σ_t^2 + (1/∆) Σ_{i=0}^{n-1} L_i R_{t-i} [[sources/pdf-5ef2018823c8]].
- Statistical inference (the variance of x̂ and µ̂) is generally not addressed in finance and trading strategies, but the paper argues it is a crucial factor in designing a successful momentum strategy [[sources/pdf-5ef2018823c8]].

## Sources

- [[sources/pdf-5ef2018823c8]]

## Related

- [[concepts/trend-filtering]]
- [[concepts/moving-average-crossover]]
- [[concepts/linear-filter-convolution]]
- [[concepts/causal-filter]]
