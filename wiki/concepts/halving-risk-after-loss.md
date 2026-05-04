---
type: concept
slug: halving-risk-after-loss
canonical_name: Halving Risk After a Loss (Anti-Martingale Drawdown Rule)
domains:
  - trading-and-markets
---

# Halving Risk After a Loss

## Summary

A discrete anti-martingale risk rule taught in ICT's 2022 mentorship and recapped by Trader Theory: after each loss, halve the risk used on the next trade, halve again if a second loss follows, and only return to the original % risk once half of the previously-used risk has been recovered — designed to compress drawdown depth during losing streaks rather than to accelerate recovery [[sources/pdf-a98b496e5936]].

## Key claims

- Trader Theory states the rule directly: "If a trade is lost, half your risk you used on the next trade. If you lose again, half the risk again. Example: From 1% risk go to 0.5%, then go to 0.25%" [[sources/pdf-a98b496e5936]].
- Recovery condition: "If you make back half of the previous risk then you are permitted to go back to your original % risk" [[sources/pdf-a98b496e5936]].
- Anti-martingale by construction: bet size shrinks after losses and is restored only on partial recovery, the inverse of doubling-up after losses [[sources/pdf-a98b496e5936]].
- Rule operates on per-trade % risk, not absolute dollar amount — making it scale-invariant across account sizes [[sources/pdf-a98b496e5936]].

## Sources

- [[sources/pdf-a98b496e5936]]

## Related

- [[concepts/scaled-stop-trailing]]
- [[concepts/fvg-selection-and-stops]]
- [[entities/trader-theory]]
- [[entities/inner-circle-trader]]
