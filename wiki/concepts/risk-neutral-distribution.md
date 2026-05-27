---
schema_version: 1
type: concept
slug: risk-neutral-distribution
canonical_name: Risk-Neutral Distribution
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Risk-Neutral Distribution

## Summary

Probability distribution of a future asset price under the risk-neutral measure, recoverable from the cross-section of option prices at a single tenor; per Allan Malz (2014), it is the central object that option-based RND techniques try to estimate, and it differs in general from real-world probabilities because it is influenced — perhaps heavily — by risk preferences [[sources/pdf-a25e1c0d5f08]].

## Key claims

- Per Malz (2014), absent arbitrage the time-t value of a European call struck at X with tenor τ equals the discounted risk-neutral expectation of its terminal payoff: c(t,X,τ) = e^(−rτ) E[max(S_T − X, 0)] = e^(−rτ) ∫_X^∞ (s − X) π̃_t(s) ds, where π̃_t(·) is the time-t risk-neutral density of S_T [[sources/pdf-a25e1c0d5f08]].
- Malz emphasizes that RNDs "are not the same as real-world probabilities, or the ones in market participants' heads, but are influenced, perhaps heavily, by risk preferences," so a change in risk-neutral probabilities can be due to changes in real-world probabilities, risk preferences, or both [[sources/pdf-a25e1c0d5f08]].
- Per Malz, RNDs based on the option-implied volatility smile have been available to researchers in finance for decades, but the techniques are difficult to implement because rendering option data suitable for the purpose requires a great deal of processing and the algorithms that compute the RNDs are complex and hard to automate [[sources/pdf-a25e1c0d5f08]].
- Malz argues that this implementation difficulty is perhaps a major reason that option-based RNDs have been less widely applied and have become less standard than might have been expected given their potential value [[sources/pdf-a25e1c0d5f08]].
- Per Malz, surveys of techniques for extracting RNDs from option prices include Jackwerth (1999, 2004) and Mandler (2003), with the foundational result going back to Breeden and Litzenberger (1978) and Banz and Miller (1978) [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the work surveyed in Garcia, Ghysels, and Renault (2010) uses historical data on underlying asset prices alongside contemporaneous option price data to simultaneously estimate both risk-neutral and real-world probability distributions, and Ross (2013) presents a technique that, with suitable assumptions, identifies both risk-neutral and real-world probabilities of discrete price outcomes from option prices alone [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the option-based RND technique he describes is applied in Malz (2013) to the measurement of systemic risk, and is also used in the Federal Reserve Bank of New York's market monitoring [[sources/pdf-a25e1c0d5f08]].

## Sources

- [[sources/pdf-a25e1c0d5f08]]

## Related

- [[concepts/breeden-litzenberger-theorem]]
- [[concepts/option-implied-volatility-smile]]
- [[concepts/clamped-cubic-spline-interpolation]]
- [[concepts/no-arbitrage-restrictions-on-options]]
- [[entities/allan-malz]]
- [[entities/federal-reserve-bank-of-new-york]]
