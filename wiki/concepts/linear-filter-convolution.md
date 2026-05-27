---
schema_version: 1
type: concept
slug: linear-filter-convolution
canonical_name: Linear-filter convolution representation
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Linear-filter convolution representation

## Summary

The convolution representation of a linear trend filter expresses the trend estimator x̂_t as a weighted sum of present and past observations y_{t−i} via a window kernel L_i; under the time-invariance and causality restrictions used in practice, this collapses to a finite sum that fully characterizes a linear filter by its kernel and its support [[sources/pdf-5ef2018823c8]].

## Key claims

- For a linear filter applied to an ordered sequence of observations y, the trend estimator satisfies x̂ = Ly with the normalisation 1 = L1, and for a regularly sampled signal x̂_t = Σ_{i=−∞}^{∞} L_{t,t−i} y_{t−i}, so linear filtering may be viewed as a convolution [[sources/pdf-5ef2018823c8]].
- A causal restriction on the coefficients L_{t,t−i} is generally imposed so the filter uses only past and present values of the signal [[sources/pdf-5ef2018823c8]].
- Restricting further to time-invariant filters yields the simple convolution x̂_t = Σ_{i=0}^{n−1} L_i y_{t−i}, so a linear filter is characterised by its window kernel L_i and its support; the kernel defines the type of filtering, the support defines the range of the filter [[sources/pdf-5ef2018823c8]].
- The square-window kernel L_i = (1/n) 1{i<n} on the compact support [0, T] with T = n∆ recovers the well-known moving-average filter [[sources/pdf-5ef2018823c8]].
- The same filter can be re-expressed via the lag operator as x̂_t = Σ_{i=0}^{n−1} L_i L^i y_t, with L y_t = y_{t−1} [[sources/pdf-5ef2018823c8]].
- Filtering the trend and filtering its derivative are related by µ̂_t ≃ d/dt x̂_t, with the derivative kernel ℓ_i obtained from the primitive L_i via ℓ_0 = L_0, ℓ_i = L_i − L_{i−1} for i = 1,…,n−1, and ℓ_n = −L_{n−1} [[sources/pdf-5ef2018823c8]].

## Sources

- [[sources/pdf-5ef2018823c8]]

## Related

- [[concepts/trend-filtering]]
- [[concepts/causal-filter]]
- [[concepts/moving-average-crossover]]
- [[concepts/denoising-bias-tradeoff]]
