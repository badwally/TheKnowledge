---
type: concept
slug: cooperative-edge-caching
canonical_name: Cooperative edge caching
domains:
  - ai-and-agents
---

# Cooperative edge caching

## Summary

Cooperative edge caching is the design pattern in which neighboring base stations or edge servers share content rather than each fetching independently from the remote CDN, exploiting cross-edge similarity to compensate for the much smaller per-edge storage budget [[sources/pdf-f4016087ee51]].

## Key claims

- Because base stations are far denser than CDN servers — China had only several hundred CDN nodes versus 3.72 million base stations by 2018 — cooperative edge caching has been proposed as a way to better afford the much less abundant storage capacity of each individual edge server [[sources/pdf-f4016087ee51]].
- In 5G networks, base stations can communicate with neighboring base stations rather than work individually, retrieving requested video content from a neighbor via fronthaul links instead of always falling back to the remote CDN [[sources/pdf-f4016087ee51]].
- The empirical case for cooperation rests on cross-edge content similarity: the MacoCache iQiYi trace analysis finds non-trivial content overlap between neighboring 1 km × 1 km edge areas in Beijing, formalized as a content similarity ratio comparing each area's requests to those of its neighbors [[sources/pdf-f4016087ee51]].
- However, that similarity is itself highly diverse and dynamic — content similarity varies substantially across edges and across hours of the week — which the authors argue can compromise the benefits of traditional cooperative-caching schemes that were largely designed against the more uniform CDN environment [[sources/pdf-f4016087ee51]].
- This dynamism is what drives MacoCache's choice to make cooperation adaptive: each edge agent learns its own caching policy while exchanging policy fingerprints with neighbors, rather than relying on a fixed cooperative rule [[sources/pdf-f4016087ee51]].

## Sources

- [[sources/pdf-f4016087ee51]]

## Related

- [[entities/macocache]]
- [[concepts/mobile-edge-caching]]
- [[concepts/multi-agent-deep-reinforcement-learning]]
- [[concepts/policy-fingerprint]]
