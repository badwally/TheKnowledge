---
type: concept
slug: causal-filter
canonical_name: Causal filter
domains:
  - trading-and-markets
---

# Causal filter

## Summary

A causal filter is a linear time-series filter whose coefficients are constrained so that the trend estimate x̂_t depends only on past and present values of the observed signal y_t — the practical restriction that makes trend filters usable in trading because the bilateral convolution would otherwise require future values [[sources/pdf-5ef2018823c8]].

## Key claims

- The unrestricted bilateral convolution x̂_t = Σ_{i=−∞}^{∞} L_{t,t−i} y_{t−i} is generally not useful in trading because it uses future values of y_t, so practitioners impose a restriction on the coefficients L_{t,t−i} to use only past and present values, and the filter is then said to be causal [[sources/pdf-5ef2018823c8]].
- Adding time-invariance on top of causality reduces the filter to the finite-window convolution x̂_t = Σ_{i=0}^{n−1} L_i y_{t−i}, which is the form used to define the moving-average and crossover estimators in the paper [[sources/pdf-5ef2018823c8]].
- Causal moving-average estimates lag the observed signal: under a homogeneous trend, the average value of the n-window MA is located at t − (n−1)/2 by construction, meaning the filtered signal lags the observed signal by half the window [[sources/pdf-5ef2018823c8]].

## Sources

- [[sources/pdf-5ef2018823c8]]

## Related

- [[concepts/linear-filter-convolution]]
- [[concepts/trend-filtering]]
- [[concepts/moving-average-crossover]]
- [[concepts/denoising-bias-tradeoff]]
