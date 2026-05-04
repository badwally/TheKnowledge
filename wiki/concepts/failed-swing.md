---
type: concept
slug: failed-swing
canonical_name: Failed Swing
domains:
  - trading-and-markets
---

# Failed Swing

## Summary

Failed Swing is a price-action variation in which price approaches a prior swing high or low but fails to take it out before reversing; TTrades names it as one of two explicit variations (alongside SMT) of his Models 1–4, where it substitutes for the standard upstream liquidity-grab leg while leaving the rest of the entry sequence intact — first published in the 2022 4-model reference card [[sources/pdf-c57b9a32c399]] and preserved in the 2023 5-model expansion [[sources/pdf-3a510f58854c]].

## Key claims

- "Failed swing" is one of the two named variations of every TTrades trigger-stack model — Model 1 Variation: Failed swing, Model 2 Variation: Failed swing, Model 3 (Model 1 + OTE) Failed swing, Model 4 (Model 2 + OTE) Failed swing — present in both the 2022 [[sources/pdf-c57b9a32c399]] and 2023 [[sources/pdf-3a510f58854c]] reference cards.
- In the Failed Swing variation the structural ingredients downstream of the HTF POI — FVG, BOS (and IDM/OTE where applicable) — remain unchanged; what is replaced is the liquidity-grab confirmation upstream of the entry trigger [[sources/pdf-c57b9a32c399]] [[sources/pdf-3a510f58854c]].
- Failed Swing variations are diagrammed for both bullish and bearish setups, with the same HTF POI / FVG / BOS scaffolding mirrored across direction [[sources/pdf-c57b9a32c399]] [[sources/pdf-3a510f58854c]].
- The presence of Failed Swing as a first-class variation indicates that TTrades treats inability-to-take-liquidity as an equally valid premise to a liquidity grab — i.e., the absence of a sweep is as informative as a sweep when downstream confirmation (BOS + displacement + FVG) follows [[sources/pdf-c57b9a32c399]] [[sources/pdf-3a510f58854c]].
- In the 2022 OTE-extended models (3 and 4), the variations are explicitly labeled "Model 1 Variation : Failed swing" and "Model 2 Variation : Failed swing" respectively, signaling that the Failed Swing variant was inherited from the parent rather than re-defined for the OTE refinement [[sources/pdf-c57b9a32c399]].

## Sources

- [[sources/pdf-c57b9a32c399]]
- [[sources/pdf-3a510f58854c]]

## Related

- [[concepts/ttrades-entry-models]]
- [[concepts/liquidity-grab]]
- [[concepts/break-of-structure]]
- [[concepts/fair-value-gap]]
- [[concepts/htf-poi]]
- [[concepts/smt-divergence]]
- [[entities/ttrades]]
