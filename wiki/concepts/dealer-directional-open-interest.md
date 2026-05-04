---
type: concept
slug: dealer-directional-open-interest
canonical_name: Dealer directional open interest (DDOI)
domains:
  - trading-and-markets
---

# Dealer directional open interest (DDOI)

## Summary

Dealer directional open interest (DDOI) is a measurement of whether option dealers are net short or long any particular option expiration, strike, and type; because publicly reported open interest only shows the total number of contracts outstanding, DDOI requires analyzing transaction-level data to assess the direction (buy/sell) of every SPX option trade, binning it by how it ought to affect open interest, and verifying trade direction by tracking subsequent actual changes in OI [[sources/pdf-sqzme-2020-the-implied-order]].

## Key claims

- Publicly reported open interest (OI) only shows the number of contracts in existence on any given day — it does not reveal whether dealers are long or short those contracts [[sources/pdf-sqzme-2020-the-implied-order]].
- To derive DDOI, every SPX option trade must be assessed for direction (buy/sell), binned according to how it ought to affect open interest, and then verified against the subsequent actual change in OI [[sources/pdf-sqzme-2020-the-implied-order]].
- Every option contract must be tracked through time to maintain an accurate picture of dealers' option exposures [[sources/pdf-sqzme-2020-the-implied-order]].
- DDOI is the necessary intermediate step before computing gamma exposure (GEX) and vanna exposure (VEX) — without knowing whether the dealer is long or short each contract, the direction of the hedging flow cannot be determined [[sources/pdf-sqzme-2020-the-implied-order]].
- With the benefit of DDOI and a Black-Scholes delta function, one can compute the current delta of every existing SPX option and calculate exactly how those deltas will change as implied vol and index price change [[sources/pdf-sqzme-2020-the-implied-order]].
- The difficulty of constructing DDOI is what makes the implied order book uniquely information-rich — it requires sustained, granular tracking of transaction-level data that most market participants do not undertake [[sources/pdf-sqzme-2020-the-implied-order]].

## Sources

- [[sources/pdf-sqzme-2020-the-implied-order]]

## Related

- [[entities/squeezemetrics]]
- [[concepts/implied-order-book]]
- [[concepts/gamma-exposure-gex]]
- [[concepts/vanna-exposure-vex]]
