---
type: concept
slug: intraday-leverage-constraint
canonical_name: Intraday Leverage Constraint
domains:
  - trading-and-markets
---

# Intraday Leverage Constraint

## Summary

The FINRA-imposed maximum 4x intraday leverage limit applied by most US brokers materially suppresses the realized returns of high-asymmetry day-trading strategies that would otherwise size each trade to a fixed percentage of capital — Zarattini and Aziz (2023) document that an unconstrained ORB QQQ strategy would have grown ~1,630% over January 2016 to February 2023, roughly 2x the constrained version's 675% return, with an estimated 60% of trades sized 40% below the optimal exposure under the constraint [[sources/pdf-e63407c2b4f4]].

## Key claims

- US FINRA-regulated brokers enforce a maximum intraday leverage of 4x the net liquidation value of the trading account [[sources/pdf-e63407c2b4f4]].
- This rule means most ORB trades cannot put the prescribed 1% of portfolio value at risk per trade — exposure is capped before reaching the size implied by `$R` [[sources/pdf-e63407c2b4f4]].
- The cap is enforced in the share-sizing formula via the `min(A·0.01/$R, 4·A/P)` term — the second argument is the leverage cap, which binds when `$R` is small relative to `P` [[sources/pdf-e63407c2b4f4]].
- Zarattini and Aziz estimate that 60% of ORB QQQ trades over 2016–2023 were conducted with exposure 40% below the optimal exposure given by the unconstrained leverage version [[sources/pdf-e63407c2b4f4]].
- The unconstrained-leverage version of the ORB QQQ strategy would have grown approximately 1,630% over the sample period — roughly 2x the growth of the constrained version (675%) [[sources/pdf-e63407c2b4f4]].
- Empirical evidence: losses in the constrained version were typically a fraction of 1R rather than a full 1R, exposing the binding constraint [[sources/pdf-e63407c2b4f4]].
- The leverage constraint is the principal motivation for Zarattini and Aziz's introduction of leveraged ETFs (TQQQ) as a workaround that reproduces the desired exposure while respecting broker leverage limits [[sources/pdf-e63407c2b4f4]].

## Sources

- [[sources/pdf-e63407c2b4f4]]

## Related

- [[concepts/opening-range-breakout-strategy]]
- [[concepts/leveraged-etf-amplification]]
