---
schema_version: 1
type: concept
slug: implied-order-book
canonical_name: Implied order book
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Implied order book

## Summary

The implied order book is a framework for reconstructing market liquidity from SPX option positioning data rather than from the fragmented, bluff-laden visible limit order book; it treats options as complex order types whose delta-hedging schedules create predictable, high-quality, guaranteed liquidity flows that can be measured in dollars per index point using gamma exposure (GEX) and vanna exposure (VEX) [[sources/pdf-sqzme-2020-the-implied-order]].

## Key claims

- The traditional limit order book has become so fragmented across tens of venues, hundreds of order types, and limitless algorithmic routing systems that the information content of a visible quote with respect to market liquidity is "either zero or less than zero" [[sources/pdf-sqzme-2020-the-implied-order]].
- Extracting an edge from dark liquidity or exchange order-type complexity would require roughly $50 million in data, research, and market access, which "barely gets you a seat at the table" [[sources/pdf-sqzme-2020-the-implied-order]].
- Options function as a "sort of complex order type" — when a customer sells an option, the dealer's delta-hedging indirectly adds liquidity to the underlying market; when a customer buys an option, the dealer's hedging effectively places stop-loss orders that take liquidity and destabilize the market [[sources/pdf-sqzme-2020-the-implied-order]].
- SPX options are the largest, most transparent part of the broad market's implied order book [[sources/pdf-sqzme-2020-the-implied-order]].
- Dealers' actual option positions can be measured by analyzing transaction data, and the Black-Scholes model can then calculate in dollar terms where delta-hedges must occur [[sources/pdf-sqzme-2020-the-implied-order]].
- The implied order book is constructed by computing dealer directional open interest (DDOI) for every SPX option contract, then computing how each contract's delta changes with underlying price (GEX) and implied volatility (VEX), converting these delta changes to dollar terms, and summing across the entire option universe [[sources/pdf-sqzme-2020-the-implied-order]].
- The resulting implied order book is "uniquely information-rich" because the hedging schedule is "necessary to the survival of the dealer and fundamentally predictable in its disposition" — unlike HFT market-maker liquidity, this is high-quality, guaranteed liquidity [[sources/pdf-sqzme-2020-the-implied-order]].

## Sources

- [[sources/pdf-sqzme-2020-the-implied-order]]

## Related

- [[entities/squeezemetrics]]
- [[concepts/gamma-exposure-gex]]
- [[concepts/vanna-exposure-vex]]
- [[concepts/dealer-directional-open-interest]]
- [[concepts/gamma-reflexivity]]
- [[concepts/market-fragility]]
