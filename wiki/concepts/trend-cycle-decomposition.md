---
type: concept
slug: trend-cycle-decomposition
canonical_name: Trend-cycle decomposition
domains:
  - trading-and-markets
---

# Trend-cycle decomposition

## Summary

Trend-cycle decomposition is the econometric framing that motivates trend filtering: a non-stationary observed time series y_t is modelled as the sum of an unobservable smooth trend component x_t and a stochastic noise (or cyclical) process ε_t, identifying the permanent and transitory components and reducing trend extraction to a signal-filtering problem [[sources/pdf-5ef2018823c8]].

## Key claims

- In economics, trend-cycle decomposition plays an important role by identifying the permanent and transitory stochastic components in a non-stationary time series [[sources/pdf-5ef2018823c8]].
- Bruder, Dao, Richard, and Roncalli formalise it as y_t = x_t + ε_t, where x_t represents the trend (the permanent component, interpreted as a smooth function representing long-term movements) and ε_t is a stochastic noise (or stochastic-cycle) process [[sources/pdf-5ef2018823c8]].
- The smoothness assumption is operationalized as the volatility inequality σ(y_t − y_{t-1}) ≫ σ(x_t − x_{t-1}); estimating x_t from y_t is the subject of signal extraction and filtering (Pollock, 2009) [[sources/pdf-5ef2018823c8]].
- The first contribution of an n-period uniform moving average filter, when the noise ε_t is independent from x_t and centered, is the average trend x̂_t = (1/n) Σ_{i=0}^{n-1} x_{t-i}; for a homogeneous trend this average value is located at t − (n−1)/2, meaning the filtered signal lags the observed signal by half the window [[sources/pdf-5ef2018823c8]].
- The trend-cycle decomposition framing has been studied in finance on log-price not price: in the Black-Scholes model dS_t / S_t = µ_t dt + σ_t dW_t, the appropriate signal to be filtered is the logarithm of the price y_t = ln S_t [[sources/pdf-5ef2018823c8]].

## Sources

- [[sources/pdf-5ef2018823c8]]

## Related

- [[concepts/trend-filtering]]
- [[concepts/linear-filter-convolution]]
- [[concepts/denoising-bias-tradeoff]]
