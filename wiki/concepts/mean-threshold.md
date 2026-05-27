---
schema_version: 1
type: concept
slug: mean-threshold
canonical_name: Mean threshold
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Mean threshold

## Summary

The mean threshold is the 50% level of any order block, used in breaker block setups as a refined entry reference inside the breaker block range [[sources/pdf-042302b20a5d]].

## Key claims

- The mean threshold is defined as 50% of any order block [[sources/pdf-042302b20a5d]].
- In one bearish breaker block example, the entry is taken at the mean threshold of the bullish order block sitting inside the breaker block (purple box) [[sources/pdf-042302b20a5d]].
- For an entry at the mean threshold of a bullish order block inside a bearish breaker block, stops are placed above that order block, since price should not trade higher than that point until sell-side liquidity is taken [[sources/pdf-042302b20a5d]].

## Sources

- [[sources/pdf-042302b20a5d]]

## Related

- [[concepts/order-block]]
- [[concepts/breaker-block]]
- [[concepts/youtube-2022-model]]
