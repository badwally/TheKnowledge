---
schema_version: 1
type: concept
slug: moving-average-crossover
canonical_name: Moving-average crossover
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Moving-average crossover

## Summary

A moving-average crossover estimates the price trend µ_t from the difference between two uniform moving averages of the log-price computed over different horizons n_1 > n_2 — with the sign of the trend changing when the short-horizon moving average crosses the long-horizon moving average; in Bruder, Dao, Richard, and Roncalli's framework this is reinterpreted as a triangle-weighted moving average of asset returns [[sources/pdf-5ef2018823c8]].

## Key claims

- An average price does not estimate the trend µ_t; the trend is estimated from the difference between two moving averages of the log-price y_t over horizons n_1 > n_2 via µ̂_t ≃ (2 / ((n_1 − n_2)∆)) (ŷ_t^{n_2} − ŷ_t^{n_1}) [[sources/pdf-5ef2018823c8]].
- The estimated trend is positive when the short-term moving average is higher than the long-term moving average, and the sign of the trend changes when the short-term average crosses the long-term average [[sources/pdf-5ef2018823c8]].
- When the short-term horizon n_1 is one, the short-term moving average is just the current asset price [[sources/pdf-5ef2018823c8]].
- The scaling term 2(n_1 − n_2)^{−1} is justified by interpreting the estimator as a weighted moving average of asset returns; inverting the kernel/derivative relation L_i = ℓ_0 if i=0, L_i = ℓ_i + L_{i−1} for i = 1,…,n−1, and L_i = −ℓ_{n+1} at the right boundary recovers the underlying return-weighted form [[sources/pdf-5ef2018823c8]].
- The weighting profile of each return in the crossover estimator forms a triangle, with the biggest weighting given at the horizon of the smallest moving average [[sources/pdf-5ef2018823c8]].
- Many practitioners and individual investors use moving averages of the price itself as a trend indication rather than moving averages of returns; the paper considers the average of the log-price for consistency with its other estimators [[sources/pdf-5ef2018823c8]].

## Sources

- [[sources/pdf-5ef2018823c8]]

## Related

- [[concepts/linear-filter-convolution]]
- [[concepts/trend-filtering]]
- [[concepts/causal-filter]]
- [[concepts/denoising-bias-tradeoff]]
- [[concepts/trend-following-strategy]]
