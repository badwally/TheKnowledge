---
type: concept
slug: speed-of-light-latency-constraint
canonical_name: Speed-of-Light Latency Constraint
domains:
  - trading-and-markets
---

# Speed-of-Light Latency Constraint

## Summary

The physical limit on information propagation between geographically separated data centers, imposed by the speed of light over great-circle distance; in the context of FOMC news release analysis, the constraint sets a minimum delay of approximately 2.34 milliseconds between a lockup release in Washington DC and reception at the CME colocation center in Aurora versus the Nasdaq colocation center in Carteret, based on the difference in distance (624 miles DC-to-Aurora versus 188 miles DC-to-Carteret) divided by the speed of light [[sources/pdf-fa83c61dfa2d]].

## Key claims

- The difference in arrival time between Carteret (Nasdaq) and Aurora (CME) for a signal originating in Washington DC is estimated at 2.34 milliseconds, computed as the difference in great-circle distance divided by the speed of light [[sources/pdf-fa83c61dfa2d]].
- DC to Aurora (CME) distance is approximately 624 miles; DC to Carteret (Nasdaq) is approximately 188 miles, with the reference point being the K Street data center in Washington DC [[sources/pdf-fa83c61dfa2d]].
- The existence of fully functional microwave networks between DC and Chicago and between DC and New Jersey is "highly probable," supported by FCC registered microwave path data identified by McKay Brothers [[sources/pdf-fa83c61dfa2d]].
- Microwave networks achieve near-speed-of-light propagation, but different networks on the DC-to-CME and DC-to-NJ routes could have different quality, introducing approximately 100 microseconds of additional uncertainty [[sources/pdf-fa83c61dfa2d]].
- For the September 18, 2013 FOMC announcement, if information was released in DC, the first CME trade should have occurred no earlier than 2:00:00.000 + 0.330 ms (Nasdaq first trade) + 2.34 ms (propagation difference) = 2.67 ms after 2:00 pm [[sources/pdf-fa83c61dfa2d]].
- The corrected CME E-mini timestamp of 2.070 ms after 2:00 pm leaves an inconsistency of 0.600 ms (2.67 - 2.070) — "too large to be explained by the uncertainty in our assumptions or by measurement errors," ruling out a DC lockup release [[sources/pdf-fa83c61dfa2d]].
- The constraint is what makes the lockup-versus-embargo question empirically testable: if release is from a single point (DC), the speed of light creates a detectable inter-city delay; if release is embargoed at each colocation center, the delay vanishes [[sources/pdf-fa83c61dfa2d]].

## Sources

- [[sources/pdf-fa83c61dfa2d]]

## Related

- [[entities/quincy-data]]
- [[entities/nanex]]
- [[concepts/fomc-news-release-mechanism]]
- [[concepts/winner-takes-all-microstructure]]
