---
schema_version: 1
type: concept
slug: multivariate-trend-following
canonical_name: Multivariate trend-following (multi-asset)
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Multivariate trend-following (multi-asset)

## Summary

The extension of the Bruder-Gaussel (2011) continuous-time trend-following model to a multi-asset universe, contributed by Jusselin, Lezmi, Malongo, Masselin, Roncalli, and Dao (2017); the multivariate framework allows analysis of the impact of asset correlations and the moving-average estimator on the risk/return profile of trend-following, and grounds the formal distinction between time-series and cross-section momentum [[sources/pdf-5a6062a63a4b]].

## Key claims

- The Amundi 2017 paper extends Bruder and Gaussel (2011) to the multivariate case, recovering the main properties found in academic literature and obtaining new theoretical findings on the momentum risk premium [[sources/pdf-5a6062a63a4b]].
- Three parameters govern the behavior of the multivariate momentum risk premium: the vector of Sharpe ratios, the covariance matrix of asset returns, and the frequency matrix of the moving-average estimator [[sources/pdf-5a6062a63a4b]].
- Diversification in a long/short approach is different and more complex than for a long-only portfolio: the concept of diversification has to be reconsidered when the strategy is allowed to short [[sources/pdf-5a6062a63a4b]].
- The multivariate model allows the paper to draw a formal distinction between time-series momentum and cross-section momentum [[sources/pdf-5a6062a63a4b]].
- The multivariate framework also enables the cross-hedging analysis in Section Four, where one asset's long-only exposure is hedged by trend-following on another asset [[sources/pdf-5a6062a63a4b]].
- Some of the multivariate formulas were derived by Tung-Lam Dao during his 2011 internship at Amundi, justifying his co-authorship on the paper [[sources/pdf-5a6062a63a4b]].

## Sources

- [[sources/pdf-5a6062a63a4b]]

## Related

- [[concepts/trend-following-strategy]]
- [[concepts/bruder-gaussel-framework]]
- [[concepts/momentum-risk-premium]]
- [[concepts/time-series-vs-cross-section-momentum]]
- [[concepts/trend-following-hedging-properties]]
- [[entities/thierry-roncalli]]
- [[entities/tung-lam-dao]]
