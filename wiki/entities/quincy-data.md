---
schema_version: 1
type: entity
slug: quincy-data
canonical_name: Quincy Data
entity_kind: organization
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Quincy Data

## Summary

Market-data firm that collects raw exchange feeds at colocation centers in Aurora (CME) and Carteret (Nasdaq); publisher of the December 2013 paper "The Fed Robbery Revisited," which uses exchange-embedded timestamps and proprietary pcap timestamps to forensically reconstruct the information-propagation sequence of the September 18, 2013 FOMC "no taper" announcement and concludes that the data was released under embargo simultaneously at both colocation centers at exactly 2:00:00 pm [[sources/pdf-fa83c61dfa2d]].

## Key facts

- Collects raw feed data from the CME at its Aurora colocation center and from Nasdaq at its Carteret colocation center [[sources/pdf-fa83c61dfa2d]].
- Records data with microsecond-granularity pcap timestamps using servers synchronized via NTP to approximately one-millisecond accuracy [[sources/pdf-fa83c61dfa2d]].
- Authors Riadh Zaatour and Stéphane Tyč used the firm's data to revisit the "Fed Robbery" controversy started by Nanex, which alleged that the September 18, 2013 FOMC announcement reached Chicago and New York simultaneously — incompatible with speed-of-light propagation from Washington DC [[sources/pdf-fa83c61dfa2d]].
- The paper's methodology combines exchange-embedded timestamps (1 ms resolution at CME, 1 ns at Nasdaq) with the firm's own pcap timestamps to reconstruct microsecond-precision corrected timestamps for CME trade publications [[sources/pdf-fa83c61dfa2d]].
- Concludes that the most likely scenario is that the FOMC data was released under embargo at 2:00 pm exactly at both Aurora and Carteret, not from a lockup facility in Washington DC [[sources/pdf-fa83c61dfa2d]].
- Also analyzed the October 30, 2013 FOMC announcement, for which the Fed reportedly made changes to the release mechanism [[sources/pdf-fa83c61dfa2d]].

## Sources

- [[sources/pdf-fa83c61dfa2d]]

## Related

- [[entities/riadh-zaatour]]
- [[entities/stephane-tyc]]
- [[entities/nanex]]
- [[concepts/fomc-news-release-mechanism]]
- [[concepts/speed-of-light-latency-constraint]]
- [[concepts/winner-takes-all-microstructure]]
