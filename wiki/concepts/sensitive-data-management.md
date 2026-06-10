---
schema_version: 1
type: concept
slug: sensitive-data-management
canonical_name: Sensitive Data Management in Shared Ledgers
domains:
- data-collectives
created_at: '2026-06-10T21:24:20Z'
last_updated: '2026-06-10T21:24:20Z'
draft: true
draft_started_at: '2026-06-10T21:24:20Z'
draft_unresolved_claims: 0
---

# Sensitive Data Management in Shared Ledgers

## Summary

A network-design family of mitigations that limits which participants can see commercially sensitive data on a shared blockchain, reducing the antitrust risk that distributed transaction data enable collusion between competitors [[sources/web-2021-03-07-5c3]].

## Key claims

- Selective encryption: particularly sensitive data on a blockchain can be encrypted and made visible only to users with a special key, limiting what unkeyed participants can observe [[sources/web-2021-03-07-5c3]].
- Firewall-managed access: network administrators can use firewalls to control which users have access to data stored on the network [[sources/web-2021-03-07-5c3]].
- Off-chain storage: forward-thinking designers can keep the most sensitive data off the blockchain entirely and store it on privately managed non-blockchain servers [[sources/web-2021-03-07-5c3]].
- Inclusion principle: only mission-critical data should be placed on the chain; data without a specific and important business requirement should be excluded as a safeguard [[sources/web-2021-03-07-5c3]].

## Sources

- [[sources/web-2021-03-07-5c3]]

## Related

- [[concepts/antitrust-risks-data-sharing]]
- [[concepts/blockchain-data-sharing]]
- [[concepts/centralized-blockchain-governance]]
- [[concepts/regulator-transparency]]
