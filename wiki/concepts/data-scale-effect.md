---
schema_version: 1
type: concept
slug: data-scale-effect
canonical_name: Data Scale Effect
domains:
- data-collectives
created_at: '2026-06-11T06:40:00Z'
last_updated: '2026-06-11T06:40:00Z'
draft: true
draft_started_at: '2026-06-11T06:40:00Z'
draft_unresolved_claims: 0
---

# Data Scale Effect

## Summary

A data scale effect is the dynamic in which more data improves a shared product (e.g. a recommendation engine, a customer-support chat bot) without requiring direct interaction between the nodes that contribute the data — what most commentators label a "data network effect" but which Casado and Lauten argue is structurally a scale effect, not a network effect [[sources/web-2019-05-09-487]].

## Key claims

- A data scale effect fits a looser definition of network effects in which there is no direct interaction between nodes — e.g. Netflix predicting that viewers of film X will enjoy show Y because of correlations across other viewers, even though those viewers do not interact [[sources/web-2019-05-09-487]].
- Unlike traditional economies of scale, where fixed-cost economics improve with scale over time, data scale effects often exhibit the opposite dynamic: the cost of adding unique data rises and the value of incremental data falls as the corpus grows [[sources/web-2019-05-09-487]].
- In a customer-support chat-bot example, an initial corpus of transcripts answers the common questions, but the long tail of one-off inquiries becomes harder to collect — after roughly 40% of the queries are captured in the illustrative case, additional collection yields no advantage [[sources/web-2019-05-09-487]].
- The point at which the data scale effect plateaus varies by domain, but the structural outcome is the same: the ability to stay ahead of the pack tends to slow down, not speed up, with data scale, and the moat erodes as competitors race to catch up [[sources/web-2019-05-09-487]].
- Casado and Lauten decompose the data scale effect into four lifecycle stages — minimum viable corpus, data acquisition cost, incremental data value, and data freshness — each of which works against durable defensibility as the corpus grows [[sources/web-2019-05-09-487]].

## Sources

- [[sources/web-2019-05-09-487]] — Casado & Lauten, "The Empty Promise of Data Moats" (a16z, 2019-05-09)

## Related

- [[concepts/data-moat]]
- [[concepts/data-network-effects]]
- [[concepts/minimum-viable-corpus]]
- [[entities/empty-promise-data-moats]]
