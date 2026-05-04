---
type: concept
slug: asymmetric-risk-reward-ratio
canonical_name: Asymmetric Risk/Reward Ratio in Day Trading
domains:
  - trading-and-markets
---

# Asymmetric Risk/Reward Ratio in Day Trading

## Summary

A position-management design in which the maximum loss per trade is hard-capped (typically at one unit of risk, `1R`) while the profit target is set at a much larger multiple of `R` — Zarattini and Aziz's 5-minute ORB strategy on QQQ uses a 10R target and a 1R stop, which makes the strategy profitable in expectation despite a 24% win rate, producing an average PnL per trade of 0.13R [[sources/pdf-e63407c2b4f4]].

## Key claims

- Zarattini and Aziz cap losses at –1R via the first-candle stop and target gains at 10R, with end-of-day liquidation if the target is not reached [[sources/pdf-e63407c2b4f4]].
- The maximum daily loss in their backtest was capped at –1R (slightly larger due to commissions) — the stop discipline is empirically respected [[sources/pdf-e63407c2b4f4]].
- Profits were often below the 10R cap because the position was liquidated at market closure before the target was reached [[sources/pdf-e63407c2b4f4]].
- The strategy's win rate was 24%, but the asymmetry between gains and losses produced an average PnL per trade of 0.13R [[sources/pdf-e63407c2b4f4]].
- Zarattini and Aziz state explicitly: "A low accuracy was compensated by the asymmetry between gains and losses" — the design principle that asymmetric payoff geometry can make low-hit-rate systems viable [[sources/pdf-e63407c2b4f4]].

## Sources

- [[sources/pdf-e63407c2b4f4]]

## Related

- [[concepts/opening-range-breakout-strategy]]
