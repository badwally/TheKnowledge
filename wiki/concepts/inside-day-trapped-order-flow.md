---
type: concept
slug: inside-day-trapped-order-flow
canonical_name: Inside Day (Trapped Order Flow)
domains:
  - trading-and-markets
---

# Inside Day (Trapped Order Flow)

## Summary

A daily-timeframe pattern in which the current bar's range sits inside the previous day's range; AMtrades reads the inside bar as trapped order flow at the previous day's high and low and uses it as a participation filter — set alerts at the prior high and low, and avoid trading the internal range when no H1-or-higher PD array is present [[sources/pdf-46c6dd54d41e]].

## Key claims

- The pattern is defined as a daily inside bar contained within the previous day's high and low [[sources/pdf-46c6dd54d41e]].
- The previous day's high and low are treated as the actionable boundaries — alerts are set there and the chart can be closed otherwise [[sources/pdf-46c6dd54d41e]].
- The internal portion of the inside-day range is treated as high-resistance and avoided unless an H1-or-higher PD array sits inside it [[sources/pdf-46c6dd54d41e]].
- When the inside-day internal range is lacking H1-or-higher PD arrays, AMtrades' personal-rules summary instructs the trader to avoid trading within the previous day's range entirely and to set alerts at the previous-day high and low [[sources/pdf-46c6dd54d41e]].
- The structural reason given is trapped order flow: orders accumulated inside the prior day's range await release at the external boundary, which is why the prior high/low — not the internal range — is the actionable level [[sources/pdf-46c6dd54d41e]].

## Sources

- [[sources/pdf-46c6dd54d41e]]

## Related

- [[entities/amtrades]]
- [[concepts/overnight-range-expansion]]
- [[concepts/daily-consolidation-profile]]
- [[concepts/external-vs-internal-range-participation]]
