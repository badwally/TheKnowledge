---
schema_version: 1
type: concept
slug: margin-call-cascade
canonical_name: Margin-call cascade
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Margin-call cascade

## Summary

The self-reinforcing mechanism by which margin calls from one counterparty trigger additional margin calls from other counterparties, as each silo marks positions against the troubled party to market and bids up replacement risk; Constan identifies this dynamic as a key lesson from the 1997 Niederhoffer liquidation, the 1998 LTCM crisis, and the 2021 Archegos collapse, arguing that "mark to markets determine maintenance margin" and that "when you are in positions that are levered and crowded there is no fair value — otherwise perfectly safe positions can get margin called" [[sources/pdf-f139d7bd1924]].

## Key claims

- The speed at which margin calls by one counterparty result in other counterparties calling for more margin was "an important lesson that is now well understood by most users of derivatives but was relatively new at the time" of the 1997 Asian Financial Crisis [[sources/pdf-f139d7bd1924]].
- In 1997, margin calls on Victor Niederhoffer's OTC Thai swaps quickly caused his U.S. clearing broker REFCO to liquidate his short SPX put spreads, with immediate impact on U.S. markets [[sources/pdf-f139d7bd1924]].
- During the 1998 LTCM crisis, Constan's equity derivatives desk at Salomon held 5 million vega of 4-year straddles purchased from LTCM; uncertainty about whether the hedge would survive an LTCM bankruptcy forced Salomon to bid up long-term implied volatility to replace the exposure, which required LTCM to place more collateral — "this created a vicious circle" [[sources/pdf-f139d7bd1924]].
- Every exposure LTCM had was "also bid up against them as each silo looked to find a source to replace LTCM risk" [[sources/pdf-f139d7bd1924]].
- The general principle: "Mark to markets determine maintenance margin. When you are in positions that are levered and crowded there is no fair value. Otherwise perfectly safe positions can get margin called" [[sources/pdf-f139d7bd1924]].
- Constan describes this lesson as "key to survival" during the 2007–2009 Global Financial Crisis [[sources/pdf-f139d7bd1924]].
- LTCM, Victor Niederhoffer (1997), and Bill Hwang at Archegos are named as instances of this mass margin-call dynamic [[sources/pdf-f139d7bd1924]].

## Sources

- [[sources/pdf-f139d7bd1924]]

## Related

- [[entities/long-term-capital-management]]
- [[entities/victor-niederhoffer]]
- [[entities/andrew-constan]]
- [[concepts/deleveraging-framework]]
