---
schema_version: 1
type: concept
slug: mobile-edge-caching
canonical_name: Mobile edge caching
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Mobile edge caching

## Summary

Mobile edge caching (MEC) is a network paradigm in which video and other content are pushed to caches co-located with cellular base stations rather than served exclusively from remote CDN servers, reducing content access latency and core-network traffic at the cost of much tighter, more dynamic per-edge storage budgets [[sources/pdf-f4016087ee51]].

## Key claims

- Mobile edge caching pushes video content closer to viewers at the network edge as an alternative to remote CDN servers, in order to reduce both content access latency and redundant backbone-network traffic [[sources/pdf-f4016087ee51]].
- In emerging 5G deployments, base stations are naturally equipped with edge servers — for example, the Nvidia Jetson TX2 — that provide both storage and compute capacity for caching service [[sources/pdf-f4016087ee51]].
- Mobile edge caching is motivated by the rise of video traffic on the backbone: global video accounted for 75% of internet traffic in 2017 and was projected to grow roughly four-fold by 2022, while quality-of-experience demands (e.g., low latency for immersive 360° video) keep tightening [[sources/pdf-f4016087ee51]].
- The capacity of an edge server is usually less abundant for video caching than a CDN server, so performance depends heavily on carefully designed caching strategies; commercial deployments still mostly use simple rule-based policies such as Least Recently Used (LRU) and Least Frequently Used (LFU) for ease of implementation [[sources/pdf-f4016087ee51]].
- Edge caching environments are substantially more complicated than CDN caching environments: large-scale trace analysis on iQiYi data shows massive heterogeneity and dynamics in request workload and content features across both temporal and geographic dimensions, particularly at finer spatial granularity [[sources/pdf-f4016087ee51]].
- Existing rule-based and model-based caching solutions, which often presume known content popularity, can fail to adapt across the diversified, distributed edge context, motivating learning-based approaches like MacoCache [[sources/pdf-f4016087ee51]].

## Sources

- [[sources/pdf-f4016087ee51]]

## Related

- [[entities/macocache]]
- [[concepts/cooperative-edge-caching]]
- [[concepts/multi-agent-deep-reinforcement-learning]]
