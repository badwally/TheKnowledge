---
schema_version: 1
type: entity
slug: squeezemetrics
canonical_name: SqueezeMetrics
entity_kind: organization
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# SqueezeMetrics

## Summary

Options-analytics firm publishing under the editorial name "GEX Ed." and the handle "sqzme"; author of the July 2020 paper "The Implied Order Book," which introduces a framework for constructing an information-rich implied limit order book from SPX option data by combining dealer directional open interest (DDOI) with Black-Scholes delta to measure gamma exposure (GEX) and vanna exposure (VEX) as dollar-denominated liquidity proxies [[sources/pdf-sqzme-2020-the-implied-order]]; provider of the negative gamma exposure data used by Baltussen, Da, Lammers, and Martens (2020) to empirically link hedging demand to market intraday momentum [[sources/pdf-2742492120a8]].

## Key facts

- Published "The Implied Order Book" on July 6, 2020 under the editorial name "GEX Ed." [[sources/pdf-sqzme-2020-the-implied-order]].
- The paper presents a method for building an "implied order book" from SPX option data that shows where option-originated liquidity is abundant and where it is scarce [[sources/pdf-sqzme-2020-the-implied-order]].
- Introduces three core measurements: Dealer Directional Open Interest (DDOI), Gamma Exposure (GEX), and Vanna Exposure (VEX), each derived from transaction-level SPX option data and the Black-Scholes delta function [[sources/pdf-sqzme-2020-the-implied-order]].
- Thanked by Baltussen, Da, Lammers, and Martens (2020) "for providing the data" underlying their empirical tests of negative gamma exposure and market intraday momentum [[sources/pdf-2742492120a8]].

## Sources

- [[sources/pdf-sqzme-2020-the-implied-order]]
- [[sources/pdf-2742492120a8]]

## Related

- [[concepts/implied-order-book]]
- [[concepts/gamma-exposure-gex]]
- [[concepts/vanna-exposure-vex]]
- [[concepts/dealer-directional-open-interest]]
- [[concepts/negative-gamma-exposure]]
