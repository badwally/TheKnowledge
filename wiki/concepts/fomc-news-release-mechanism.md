---
schema_version: 1
type: concept
slug: fomc-news-release-mechanism
canonical_name: FOMC News Release Mechanism
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# FOMC News Release Mechanism

## Summary

The Federal Reserve uses two distinct mechanisms for releasing FOMC announcements to accredited news providers: the **lockup** release (news transformed into machine-readable format in a locked room in Washington DC and transmitted from there at the scheduled release time) and the **embargo** release (news pre-distributed to colocation centers nationwide and released simultaneously at the scheduled time from each location) [[sources/pdf-fa83c61dfa2d]]. Per the FIA PTG, the Fed changed from lockup to embargo in March 2013 [[sources/pdf-fa83c61dfa2d]]. The distinction is operationally critical because a lockup release from DC imposes a speed-of-light delay to remote data centers, while an embargo release eliminates that delay entirely [[sources/pdf-fa83c61dfa2d]].

## Key claims

- In the **lockup** mechanism, FOMC news is given to accredited news providers as text in a locked room before the release time; providers transform it into machine-readable format, and at exactly 2:00 pm the bits are transmitted from the gate of the lockup room through fiber or wireless to clients at colocation centers [[sources/pdf-fa83c61dfa2d]].
- In the **national embargo** mechanism, news agencies transport the information to various locations in the United States before 2:00 pm and then release it simultaneously at 2:00 pm from each location, including colocation centers [[sources/pdf-fa83c61dfa2d]].
- There can also be an **international embargo** where the news is released at 2:00 pm simultaneously all over the world [[sources/pdf-fa83c61dfa2d]].
- Per the FIA PTG, the Federal Reserve changed the release mechanism from lockup to embargo in March 2013, making simultaneous release in Chicago and New York at 2:00 pm the expected outcome [[sources/pdf-fa83c61dfa2d]].
- The distinction between lockup and embargo determines whether high-frequency traders at different colocation centers face a speed-of-light propagation delay or not: under lockup, a 2.34 ms delay separates Carteret (Nasdaq) from Aurora (CME) based on great-circle distance from DC; under embargo, both receive the information at the same instant [[sources/pdf-fa83c61dfa2d]].
- The Quincy Data paper's timestamp forensics on the September 18, 2013 FOMC "no taper" announcement rule out a lockup release from DC and are consistent with an embargoed release simultaneous at Aurora and Carteret at exactly 2:00:00 pm [[sources/pdf-fa83c61dfa2d]].
- Nasdaq GLD trades motivated by the no-taper information began at 14:00:00.000330613 — just 330 microseconds after 2:00 pm — ruling out a DC release since the information could not have traveled from Washington to Carteret that fast [[sources/pdf-fa83c61dfa2d]].
- CME Gold futures (GCZ3) first traded at a corrected timestamp of approximately 1.621 ms after 2:00 pm, while E-mini (ESZ3) first traded at approximately 2.070 ms — both consistent with local release plus matching-engine processing time [[sources/pdf-fa83c61dfa2d]].
- The Federal Reserve declined to answer CNBC reporter Eamon Javers's questions about whether organizations were allowed to transmit information out of the lockup room before 2:00 pm or not, and Market News International (owned by Deutsche Börse Group) responded only that "MNI follows the rules set by the Fed as we do with all data releases" [[sources/pdf-fa83c61dfa2d]].
- The paper argues that the rules governing FOMC news release "do not seem to be very clear and are not publicly available," making it difficult to determine definitively whether the embargo release was authorized [[sources/pdf-fa83c61dfa2d]].
- The paper recommends that whatever news release mechanism is used, it should be clearly documented, publicly available, and guarantee a level playing field [[sources/pdf-fa83c61dfa2d]].

## Sources

- [[sources/pdf-fa83c61dfa2d]]

## Related

- [[entities/quincy-data]]
- [[entities/nanex]]
- [[entities/fia-ptg]]
- [[entities/federal-reserve]]
- [[concepts/speed-of-light-latency-constraint]]
- [[concepts/winner-takes-all-microstructure]]
