---
schema_version: 1
type: entity
slug: iqiyi
canonical_name: iQiYi
entity_kind: organization
domains:
- ai-and-agents
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# iQiYi

## Summary

Chinese online video service provider that supplied the real-world video-watching trace used as the empirical foundation for MacoCache's analysis of edge caching dynamics [[sources/pdf-f4016087ee51]].

## Key facts

- Described in the MacoCache paper as one of the largest video service providers in China in 2019 [[sources/pdf-f4016087ee51]].
- Collaborated with the MacoCache authors to provide a video-watching trace covering mobile users in Beijing over two weeks in May, comprising about 17 million sessions and recording user ID, timestamp, video content name, and GPS location of each request [[sources/pdf-f4016087ee51]].
- The trace served as the basis for analyses of request workload heterogeneity, content-popularity dynamics, and cross-edge content similarity that motivate the MacoCache framework [[sources/pdf-f4016087ee51]].

## Sources

- [[sources/pdf-f4016087ee51]]

## Related

- [[entities/macocache]]
- [[concepts/mobile-edge-caching]]
- [[concepts/cooperative-edge-caching]]
