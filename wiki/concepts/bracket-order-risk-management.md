---
type: concept
slug: bracket-order-risk-management
canonical_name: Bracket order risk management
domains:
  - trading-and-markets
---

# Bracket order risk management

## Summary

Matthew Ryan's bracket-order risk management is a tick-based, mechanical loss-and-profit framework: enter with a stop-loss at -10 ticks below entry, take 3/4ths of position off at +20-30 ticks above entry, and let the remaining 1/4th run with a trailing stop, governed by hard non-negotiable rules including a 20% maximum loss on any options position and never lowering a stop [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].

## Key claims

- Stop loss is set at -10 ticks below entry; take profit triggers at +20-30 ticks above entry where 3/4ths of the position is sold (leaving 1/4th as runners with a trailing stop), unless the market offers otherwise [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Hard rule: "NEVER HOLD A LOSS FOR MORE THAN 20%. DO NOT COMPROMISE THIS." — codified as non-negotiable [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- For options 2DTE or shorter, Ryan recommends not holding a loss over 15% [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- 0DTE rule: do not buy 0DTE options after 11:00am EST because of theta burn [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Out-of-the-money options without volatility are likely to expire worthless [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Stop-discipline rule: never lower a stop, only move stops up — codified as non-negotiable [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Trailing stops are useful for securing profit but can drastically skew the risk-to-reward ratio [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Consider moving a stop loss to breakeven once price moves in favor, but watch for theta or implied-volatility swings that can trigger stops on pullbacks when trading options [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Take-profit targets are subjective to the trader and should match the trade type — for reversals VWAP or HOD are sufficient targets; when fading VWAP, LOD is a practical target; previous supply/demand zones or higher-timeframe EMAs can also be used [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].
- Anti-FOMO rules: avoid anticipatory entries (attempting to maximize profit), oversizing cheap OTM contracts (cheaper is not necessarily better), and buying 0DTE after 11:00am EST [[sources/pdf-2248d6cdc39f]] [[sources/pdf-6ba2dc608ac8]].

## Sources

- [[sources/pdf-2248d6cdc39f]]
- [[sources/pdf-6ba2dc608ac8]]

## Related

- [[concepts/scale-out-profit-taking]]
- [[concepts/stochastic-momentum-signal]]
- [[concepts/process-oriented-trading]]
- [[entities/matthew-ryan]]
