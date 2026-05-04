---
type: concept
slug: option-greeks
canonical_name: Option Greeks
domains:
  - trading-and-markets
---

# Option Greeks

## Summary

The set of partial derivatives of an option's value with respect to its inputs — most prominently delta (sensitivity to the underlying), gamma (convexity / second derivative w.r.t. the underlying), vega (sensitivity to volatility), theta (time decay), and rho (sensitivity to interest rates) — used to manage option risk by decomposing P&L into independent factor exposures [[sources/pdf-4b87a8059b38]].

## Key claims

- Delta ranges from 0% (deep out-of-the-money) to 100% (deep in-the-money) for a long call, capturing the option's sensitivity to changes in the underlying [[sources/pdf-4b87a8059b38]].
- Gamma is a "second-order Greek" that captures the rate of change of delta with respect to the underlying — i.e., the convexity of the option's payoff [[sources/pdf-4b87a8059b38]].
- Long-gamma trading on a Lehman call option produces a P&L profile in which delta-hedging an option produces income as the underlying oscillates — illustrated in the manual's "P&L on Gamma Hedging Example" [[sources/pdf-4b87a8059b38]].
- Second-order Greeks beyond gamma — including effects of cross-derivatives — are catalogued separately from first-order Greeks in the manual [[sources/pdf-4b87a8059b38]].
- A "factors and their effects on option value" table summarizes how spot, strike, time to expiration, volatility, and interest rates each affect option value [[sources/pdf-4b87a8059b38]].

## Sources

- [[sources/pdf-4b87a8059b38]]

## Related

- [[entities/lehman-brothers]]
- [[concepts/fx-vanilla-option]]
- [[concepts/exotic-fx-options]]
- [[concepts/gamma-reflexivity]]
- [[concepts/short-gamma-hedging]]
- [[concepts/negative-gamma-exposure]]
