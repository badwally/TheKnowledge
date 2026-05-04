---
type: concept
slug: breeden-litzenberger-theorem
canonical_name: Breeden-Litzenberger Theorem
domains:
  - trading-and-markets
---

# Breeden-Litzenberger Theorem

## Summary

Foundational no-arbitrage identity stating that the risk-neutral cumulative distribution and density of a future asset price are recoverable from the first and second derivatives of the European call price with respect to the exercise price; per Allan Malz (2014), this is the result that inspires methods for computing risk-neutral distributions from option prices, first stated in Breeden and Litzenberger (1978) and Banz and Miller (1978) [[sources/pdf-a25e1c0d5f08]].

## Key claims

- Per Malz (2014), in the absence of arbitrage "the mathematical derivative of the call option value with respect to the exercise price is closely related to the risk-neutral probability that the future asset price will be no higher than the exercise price at option maturity" [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the time-t risk-neutral cumulative distribution of the future asset price is given by Π̃_t(X) = 1 + e^(rτ) ∂c(t,X,τ)/∂X — "one plus the future value of the exercise-price delta of a European call struck at X" [[sources/pdf-a25e1c0d5f08]].
- Per Malz, differentiating again gives the time-t risk-neutral probability density as π̃_t(X) = e^(rτ) ∂²c(t,X,τ)/∂X² — "the future value of the second derivative of the call price with respect to the exercise price" [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the put-price formulation offers a more direct and intuitive statement: Π̃_t(X) = e^(rτ) ∂p(t,τ,X)/∂X, where p(t,X,τ) is the time-t value of a European put struck at X with tenor τ [[sources/pdf-a25e1c0d5f08]].
- Per Malz, Figlewski (2010) provides intuition for the put-price formulation: as exercise price varies from low to high, the put value's slope and value move from near zero to a slope of erτ near intrinsic value, and increasing the exercise price from X to X+Δ raises the risk-neutral expected payoff by Δ × Π̃(X+Δ) ≈ e^(rτ) [p(t,τ,X+Δ) − p(t,τ,X)] [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the theorem was first stated in Breeden and Litzenberger (1978) and Banz and Miller (1978) [[sources/pdf-a25e1c0d5f08]].

## Sources

- [[sources/pdf-a25e1c0d5f08]]

## Related

- [[concepts/risk-neutral-distribution]]
- [[concepts/option-implied-volatility-smile]]
- [[entities/stephen-figlewski]]
- [[entities/allan-malz]]
