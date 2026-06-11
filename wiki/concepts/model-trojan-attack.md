---
schema_version: 1
type: concept
slug: model-trojan-attack
canonical_name: Model Trojan Attack
domains:
- data-collectives
created_at: '2026-06-10T22:24:13Z'
last_updated: '2026-06-10T22:24:13Z'
draft: true
draft_started_at: '2026-06-10T22:24:13Z'
draft_unresolved_claims: 0
---

# Model Trojan Attack

## Summary

A model Trojan attack is a backdoor attack on a machine learning model induced by training-data poisoning: the attacker injects poisoned samples so that the model behaves normally on clean inputs but produces attacker-chosen outputs when a specific trigger pattern is present at inference time [[sources/arxiv-2409.13004]]. Wei et al. (2024) treat model Trojans as a high-impact category of data-poisoning outcomes in federated learning [[sources/arxiv-2409.13004]].

## Key claims

- Model Trojan attacks are realized through training-data poisoning rather than direct manipulation of model parameters [[sources/arxiv-2409.13004]].
- When poisoning is sufficient to embed the Trojan, the damage to the global model's performance in federated learning can be detrimental [[sources/arxiv-2409.13004]].
- Whether and when poisoning escalates into a model Trojan is a function of the attack design — not every poisoned contribution yields a successful backdoor [[sources/arxiv-2409.13004]].

## Sources

- [[sources/arxiv-2409.13004]] — Data Poisoning and Leakage Analysis in Federated Learning (2024)

## Related

- [[concepts/training-data-poisoning]]
- [[concepts/dynamic-model-perturbation]]
- [[concepts/cross-silo-federated-learning]]
- [[entities/data-poisoning-leakage-fl-chapter]]
