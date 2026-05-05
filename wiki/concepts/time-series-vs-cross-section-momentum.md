---
type: concept
slug: time-series-vs-cross-section-momentum
canonical_name: Time-series vs cross-section momentum
domains:
  - trading-and-markets
---

# Time-series vs cross-section momentum

## Summary

Two distinct constructions of the momentum risk premium: time-series momentum, which sizes long/short exposure on each asset based on its own past return, and cross-section momentum, which goes long winners and short losers within a cross-section of assets; the Amundi 2017 multivariate trend-following model formalizes the distinction within a single continuous-time framework [[sources/pdf-5a6062a63a4b]].

## Key claims

- The Amundi 2017 paper uses its multivariate extension of the Bruder-Gaussel (2011) trend-following model to draw a formal distinction between time-series momentum and cross-section momentum [[sources/pdf-5a6062a63a4b]].
- The distinction is grounded in the underlying academic literature: the equity-market cross-section momentum tradition originates with Jegadeesh and Titman (1993) — buying past three-to-twelve-month winners and selling losers — while time-series momentum across asset classes is associated with Moskowitz et al. (2012) and the carry/value/momentum cross-asset tradition of Asness et al. (2013) [[sources/pdf-5a6062a63a4b]].
- Three parameters drive the multi-asset momentum P&L in the Amundi framework — the vector of Sharpe ratios, the covariance matrix of asset returns, and the frequency matrix of the moving-average estimator — and these parameters interact differently in time-series versus cross-section constructions [[sources/pdf-5a6062a63a4b]].
- Diversification properties differ between time-series and cross-section momentum because the long/short construction has fundamentally different correlation structure than a long-only portfolio [[sources/pdf-5a6062a63a4b]].

## Sources

- [[sources/pdf-5a6062a63a4b]]

## Related

- [[concepts/momentum-risk-premium]]
- [[concepts/multivariate-trend-following]]
- [[concepts/trend-following-strategy]]
- [[concepts/bruder-gaussel-framework]]
