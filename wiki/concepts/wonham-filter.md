---
type: concept
slug: wonham-filter
canonical_name: Wonham filter
domains:
  - trading-and-markets
---

# Wonham filter

## Summary

The Wonham filter is the nonlinear filter that converts a partially observed continuous-time hidden-Markov regime model into an equivalent fully observed problem in terms of the conditional probability of the hidden state; Dai, Yang, Zhang, and Zhu (2015) use it to recast their bull-bear switching trading problem as a standard control problem in observed variables [[sources/pdf-05df32dcb03e]].

## Key claims

- Because the market regime α_r is not directly observable, the trading problem must be converted into one that is observable, and the paper uses the Wonham (1965) filter to do so [[sources/pdf-05df32dcb03e]].
- The conditional probability of being in a bull market given the observed stock-price filtration, p_r = P(α_r = 1 | S_r), satisfies the stochastic differential equation dp_r = [−(λ_1+λ_2)p_r + λ_2]dr + ((μ_1−μ_2)p_r(1−p_r)/σ) dB̂_r, where B̂_r is the innovation process [[sources/pdf-05df32dcb03e]].
- The innovation process B̂_r is a standard Brownian motion defined by dB̂_r = (d log S_r − [(μ_1−μ_2)p_r + μ_2 − σ²/2]dr)/σ [[sources/pdf-05df32dcb03e]].
- In terms of the innovation process, the stock-price dynamics become dS_r = S_r[(μ_1−μ_2)p_r + μ_2]dr + S_r σ dB̂_r [[sources/pdf-05df32dcb03e]].
- A separation principle therefore holds: the partially observed optimization problem is converted to a fully observable one in the state p_r, which is the conditional probability of being in a bull market and which can be computed from the stock price up to time r [[sources/pdf-05df32dcb03e]].
- The conditional probability p_r is the state variable that the optimal trend-following rule's threshold curves are defined over; buy and sell decisions correspond to up- and down-crossings of two thresholds in p [[sources/pdf-05df32dcb03e]].

## Sources

- [[sources/pdf-05df32dcb03e]]

## Related

- [[concepts/bull-bear-switching-model]]
- [[concepts/trend-following-trading-rule]]
- [[concepts/optimal-trading-thresholds]]
