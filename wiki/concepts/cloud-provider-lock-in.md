---
type: concept
slug: cloud-provider-lock-in
canonical_name: Cloud Provider Lock-In
domains:
  - trading-and-markets
---

# Cloud Provider Lock-In

## Summary

The dynamic, as argued in the 2018 Akash Network position paper, by which the major cloud providers' product portfolios — particularly white-labeled, fully-managed open-source PaaS services and inter-region pricing penalties — restrict customers' ability to migrate, multi-region, or innovate, with the providers acting as "middle-men that set the rules of engagement for the industry while making no contribution to society on the whole" [[sources/pdf-c9b8f466ea39]].

## Key claims

- Cloud-provider products "are overpriced, complicated, and lock clients into ecosystems that limit their ability to innovate, compete, and have sovereignty over their infrastructure needs" [[sources/pdf-c9b8f466ea39]].
- Cloud providers earn most of their margin via cross-selling fully-managed backend services (databases, caches, API gateways) — analogous to "the old burgers-and-fries model where a restaurant needs to sell burgers at a loss so that they can sell the more addictive fries at a high margin" [[sources/pdf-c9b8f466ea39]].
- Example: as of the writing of the paper, a managed Redis server (AWS ElastiCache) on r3.8xlarge in US East (Ohio) was priced at $31,449/yr versus $18,385/yr for the same instance without Redis — a $13,064 premium "just for a 'piece of mind' to the customer," with neither Redis author Salvatore Sanfilippo nor Redis Labs incentivized for their efforts [[sources/pdf-c9b8f466ea39]].
- Providers prefer customers to deploy in a single datacenter and penalize cross-regional or multi-zonal deployments "usually through hefty bandwidth fees and variable regional pricing," which is why "AWS' pricing model is different for each region for the same exact resource" [[sources/pdf-c9b8f466ea39]].
- Increasing service availability and codification using non-standard APIs lock customers in, "preventing clients from exploring other better options in the marketplace while inhibiting innovation" [[sources/pdf-c9b8f466ea39]].
- Hyper-scale consolidation lets providers oversubscribe customers and drive higher margins, but "creates single-points for failures" [[sources/pdf-c9b8f466ea39]].
- The model "stifles innovation as it dramatically reduces the chance of an open source project from succeeding," with cloud providers acting as middle-men that set the rules of engagement while making no contribution to society on the whole [[sources/pdf-c9b8f466ea39]].

## Sources

- [[sources/pdf-c9b8f466ea39]]

## Related

- [[entities/akash-network]]
- [[concepts/decentralized-cloud-marketplace]]
- [[concepts/server-underutilization]]
