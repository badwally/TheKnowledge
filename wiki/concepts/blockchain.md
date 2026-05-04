---
type: concept
slug: blockchain
canonical_name: Blockchain
domains:
  - ai-and-agents
---

# Blockchain

## Summary

A data-structure and protocol pattern in which a chain of records is maintained on a public ledger via chained nonlinear transformations using cryptographic hash functions; combined with a Merkle tree and proof of work, it allows storage of activities on a public ledger to facilitate peer-to-peer commerce, transactions, and settlements without a custodian [[sources/pdf-752c8824b750]].

## Key claims

- Taleb describes the concept as intuitive to early practitioners of quantitative finance, who used analogous methods to generate pseudorandom variables via chained nonlinear transformations "in the spirit of Von Neumann's original idea"; knowledge of the seed allowed replication of the entire sequence, "probabilistically mimicking the arrow of time" while disallowing easy reverse engineering [[sources/pdf-752c8824b750]].
- The blockchain's contribution beyond ordinary chained pseudorandom variables is the requirement, via the hash function, that the transformation r(.) be functionally and probabilistically bijective: no two seeds should produce the same output, with vanishingly low collision probability [[sources/pdf-752c8824b750]].
- The blockchain stores activities on a public ledger and allows for serial record keeping, supporting "a purely peer-to-peer version of electronic cash" that "would allow online payments to be sent directly from one party to another without going through a financial institution" [[sources/pdf-752c8824b750]].
- Bitcoin's blockchain combines three pre-existing technologies — the hash function, the Merkle tree (to chain blocks of transactions tagged by the hash function), and the concept of proof of work [[sources/pdf-752c8824b750]].
- By the very nature of the blockchain, transactions are irreversible, no matter the reason [[sources/pdf-752c8824b750]].

## Sources

- [[sources/pdf-752c8824b750]]

## Related

- [[entities/bitcoin]]
- [[concepts/proof-of-work]]
- [[concepts/byzantine-generals-problem]]
