---
type: concept
slug: clamped-cubic-spline-interpolation
canonical_name: Clamped Cubic Spline Interpolation
domains:
  - trading-and-markets
---

# Clamped Cubic Spline Interpolation

## Summary

Variant of cubic-spline interpolation that fixes the slope at the boundary knot points to a specified value, used by Allan Malz (2014) — with a boundary slope of zero — to interpolate and extrapolate the option-implied volatility smile so that extrapolation beyond the input data does not induce violations of no-arbitrage restrictions on the volatility smile [[sources/pdf-a25e1c0d5f08]].

## Key claims

- Per Malz (2014), a cubic spline is constructed to have continuous first and second derivatives at all its knot points, with additional conditions imposed at the first and last (boundary) knots to complete the linear system that determines the spline coefficients [[sources/pdf-a25e1c0d5f08]].
- Per Malz, a natural cubic spline is constructed so that the second derivatives at the boundary knots equal zero, which makes extrapolation beyond the boundary linear but generally with a non-zero slope — "precisely the behavior that may induce violations of the no-arbitrage bounds on the volatility smile" [[sources/pdf-a25e1c0d5f08]].
- Per Malz, a clamped cubic spline is instead constructed so its slope takes specific values at the boundary knot points; the Malz technique sets that slope to zero, using the implied-volatility data points themselves as the spline knots [[sources/pdf-a25e1c0d5f08]].
- Per Malz, with zero-slope clamping the slope of the fitted spline is zero at the highest and lowest exercise prices in the data, and the spline remains smooth at those transitions because continuity of the second derivatives is still imposed; extrapolated spline values beyond those points are then equal to the observed implied volatilities for the highest and lowest exercise prices [[sources/pdf-a25e1c0d5f08]].
- Per Malz, this is tantamount to assuming that implied volatilities for very deep out-of-the-money calls and puts are identical to those for the furthest in- and out-of-the-money strikes in the input data [[sources/pdf-a25e1c0d5f08]].
- Per Malz, the clamped-spline choice is motivated primarily by avoiding processing-induced violations of no-arbitrage restrictions: "if the input implied volatility data don't violate no-arbitrage restrictions, why should the interpolating function?" [[sources/pdf-a25e1c0d5f08]].

## Sources

- [[sources/pdf-a25e1c0d5f08]]

## Related

- [[concepts/option-implied-volatility-smile]]
- [[concepts/risk-neutral-distribution]]
- [[concepts/no-arbitrage-restrictions-on-options]]
- [[entities/allan-malz]]
