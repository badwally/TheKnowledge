---
type: concept
slug: trend-following-trading-rule
canonical_name: Trend-following trading rule
domains:
  - trading-and-markets
---

# Trend-following trading rule

## Summary

A trend-following trading rule is a strategy that tries to capture market trends by buying when prices advance and exiting at the first sign of a bear market; Dai, Yang, Zhang, and Zhu (2015) provide a rigorous mathematical justification of such a rule in a bull-bear regime-switching market with partial information [[sources/pdf-05df32dcb03e]].

## Key claims

- Trading strategies can be classified into three categories — buy-and-hold, contra-trend, and trend-following — and the trend-following category tries to capture market trends, in contrast to the contra-trend approach which bets on mean reversion [[sources/pdf-05df32dcb03e]].
- A trend-following trader purchases shares when prices advance to a certain level and closes the position at the first sign of an upcoming bear market [[sources/pdf-05df32dcb03e]].
- In practice, trend-following traders often use moving averages to determine the general direction of the market and to generate trading signals; Faber (2007) is cited as a representative statistical analysis of moving-average rules [[sources/pdf-05df32dcb03e]].
- Dai et al. (2015) prove via thorough theoretical analysis that, in a bull-bear regime-switching market with hidden Markov state, the optimal trading strategy is trend-following — characterized by the conditional probability of a bull market and its up- and down-crossings of two threshold curves [[sources/pdf-05df32dcb03e]].
- The thresholds are obtained by solving a system of associated Hamilton-Jacobi-Bellman (HJB) equations, and the resulting strategy generates entry and exit stopping times [[sources/pdf-05df32dcb03e]].
- The paper proves that the optimal trading strategy incurs only a finite number of trades almost surely (Lemma 2), which removes a technical condition imposed in the earlier Dai et al. [5] companion paper [[sources/pdf-05df32dcb03e]].
- Numerical simulations and market backtests are reported as empirical support for the theoretical findings [[sources/pdf-05df32dcb03e]].
- The paper's broader motivation is to design and justify an alternative "all in - all out" strategy that is analogous to moving-average trading but admits rigorous theoretical analysis [[sources/pdf-05df32dcb03e]].

## Sources

- [[sources/pdf-05df32dcb03e]]

## Related

- [[concepts/bull-bear-switching-model]]
- [[concepts/wonham-filter]]
- [[concepts/all-in-all-out-strategy]]
- [[concepts/contra-trend-strategy]]
- [[concepts/optimal-trading-thresholds]]
- [[entities/min-dai]]
