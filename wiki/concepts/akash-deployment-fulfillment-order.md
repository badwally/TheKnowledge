---
schema_version: 1
type: concept
slug: akash-deployment-fulfillment-order
canonical_name: Akash Deployment / Fulfillment Order Matching
domains:
- trading-and-markets
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Akash Deployment / Fulfillment Order Matching

## Summary

Market mechanism specified by the 2018 Akash Network position paper for procuring compute resources: a public blockchain-anchored orderbook holds open deployment orders (client buy intents) against which providers post fulfillment orders (sell intents); the lowest-priced eligible fulfillment order matches, ties broken by time priority, and the resulting lease is the binding agent for fulfilling the deployment [[sources/pdf-c9b8f466ea39]].

## Key claims

- A deployment order contains a specification of the client's service needs, the maximum price the client is willing to pay, the bundle of compute units (memory, cpu, storage, bandwidth), and the duration [[sources/pdf-c9b8f466ea39]].
- A fulfillment order is the provider's bid declaring the price at which it will provide the requested resources [[sources/pdf-c9b8f466ea39]].
- A fulfillment order is eligible to match with a deployment order if it satisfies all minimum specifications of the deployment order [[sources/pdf-c9b8f466ea39]].
- Among eligible fulfillment orders, "the fulfilment order offering the lowest price will be matched with the deployment order" [[sources/pdf-c9b8f466ea39]].
- If multiple fulfillment orders are eligible at the same price, "the fulfilment order placed first will be matched with the deployment order" — explicit price-then-time priority [[sources/pdf-c9b8f466ea39]].
- A match creates a lease, which contains references to the deployment and fulfillment orders and is the binding agent for fulfilling the deployment [[sources/pdf-c9b8f466ea39]].
- A homomorphic-encryption layer is added because "businesses and individual consumers will want and need to protect how they are publicly displaying their use of compute power," guarding against competitor data mining and other attack vectors [[sources/pdf-c9b8f466ea39]].
- Settlement in AKASH tokens is paid by the tenant to the network at match time, then "subsequently paid to the provider according to the terms of the lease" [[sources/pdf-c9b8f466ea39]].

## Sources

- [[sources/pdf-c9b8f466ea39]]

## Related

- [[entities/akash-network]]
- [[concepts/decentralized-cloud-marketplace]]
- [[concepts/cloud-spot-market]]
- [[concepts/manifest-based-deployment]]
