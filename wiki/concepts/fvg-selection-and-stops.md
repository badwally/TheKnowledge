---
schema_version: 1
type: concept
slug: fvg-selection-and-stops
canonical_name: FVG Selection and Stop Placement Rules
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# FVG Selection and Stop Placement Rules

## Summary

When multiple Fair Value Gaps (FVGs) are present in an ICT-style trade plan, Trader Theory's recap of ICT's 2022 mentorship prescribes selecting the FVG that gives the worst risk/reward — on the theory that price may not trade as far as the best-R/R FVG — and pairing FVG size with stop placement: large FVGs take a stop above/below the high/low of the candle the FVG is formed in, while small FVGs take a stop above/below the swing high/low [[sources/pdf-a98b496e5936]].

## Key claims

- Multi-FVG selection rule: "If there are a few FVGs when trading your model use the one that gives the worst risk/reward because the price may not trade to the best FVG" [[sources/pdf-a98b496e5936]].
- Stop placement for large FVGs: "If the FVG is big then place SL above/below the high/low of the candle the FVG is formed in" [[sources/pdf-a98b496e5936]].
- Stop placement for small FVGs: "If the FVG is small then place SL above/below the swing high/low" [[sources/pdf-a98b496e5936]].
- The selection rule is conservative under uncertainty: by taking the closer (worse-R/R) FVG, the trader maximizes the probability of fill at the cost of expected reward per trade — a deliberate trade-off given that the better-R/R fill may never occur [[sources/pdf-a98b496e5936]].
- Pairs with the broader Time + Price = Optimal Setups equation Trader Theory uses to summarize ICT, since FVGs are the price-delivery component of the optimal-setup ingredients (Old High/Low Sweeps + MSS + Displacement + FVG) [[sources/pdf-a98b496e5936]].

## Sources

- [[sources/pdf-a98b496e5936]]

## Related

- [[concepts/optimal-trade-entry]]
- [[concepts/scaled-stop-trailing]]
- [[concepts/halving-risk-after-loss]]
- [[entities/trader-theory]]
- [[entities/inner-circle-trader]]
