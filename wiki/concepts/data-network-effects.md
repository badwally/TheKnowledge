---
schema_version: 1
type: concept
slug: data-network-effects
canonical_name: Data Network Effects
domains:
- data-collectives
created_at: '2026-06-11T06:40:00Z'
last_updated: '2026-06-11T06:40:00Z'
draft: true
draft_started_at: '2026-06-11T06:40:00Z'
draft_unresolved_claims: 0
---

# Data Network Effects

## Summary

A "data network effect" is the popular claim that a system in which more data improves a shared product (e.g. a recommendation engine) exhibits the same self-reinforcing dynamic as a classical network effect, in which the value of joining the network rises as more nodes join [[sources/web-2019-05-09-487]]. Casado and Lauten argue that the term is usually misapplied: in most enterprise-software cases there is no direct interaction between nodes over a defined interface or protocol — the necessary precondition for a true network effect — and what is actually being described is a data scale effect [[sources/web-2019-05-09-487]].

## Key claims

- Systems exhibiting true network effects share the property of direct interactions between nodes over a defined interface or protocol; joining the network requires conforming to a standard, which increases direct interaction for all nodes and makes those interactions increasingly stickier [[sources/web-2019-05-09-487]].
- The popular narrative around "data network effects" typically does not exhibit sticky direct interaction between nodes, let alone mechanical interdependencies due to protocols or interfaces, so the label is a misnomer in most enterprise cases [[sources/web-2019-05-09-487]].
- The Netflix recommendation engine is a frequently cited "data network effect" but is actually a data scale effect: predictions improve because more viewing histories make recommendations more accurate, not because viewers interact with each other [[sources/web-2019-05-09-487]].
- With true network effects, user-acquisition costs tend to fall over time (the value of joining the network rises) and the network exhibits inherent virality; neither property holds for data effects, where the cost of acquiring incremental useful data rises and the marginal value of that data falls [[sources/web-2019-05-09-487]].

## Sources

- [[sources/web-2019-05-09-487]] — Casado & Lauten, "The Empty Promise of Data Moats" (a16z, 2019-05-09)

## Related

- [[concepts/data-moat]]
- [[concepts/data-scale-effect]]
- [[concepts/minimum-viable-corpus]]
- [[entities/empty-promise-data-moats]]
