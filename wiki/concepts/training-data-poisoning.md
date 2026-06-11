---
schema_version: 1
type: concept
slug: training-data-poisoning
canonical_name: Training Data Poisoning
domains:
- data-collectives
created_at: '2026-06-10T22:24:13Z'
last_updated: '2026-06-10T22:24:13Z'
draft: true
draft_started_at: '2026-06-10T22:24:13Z'
draft_unresolved_claims: 0
---

# Training Data Poisoning

## Summary

Training data poisoning is a class of attack on machine learning in which an adversary manipulates the training data — directly or by controlling a contributing client — so that the resulting model behaves incorrectly at inference time [[sources/arxiv-2409.13004]]. In federated learning, where a global model is trained from updates contributed by many clients, poisoning is one of the two dominant security threats alongside training-data privacy intrusion [[sources/arxiv-2409.13004]].

## Key claims

- Data poisoning operates on the *input* side of training: an attacker corrupts examples (labels, features, or both) so the learned model encodes the attacker's objective alongside, or in place of, the legitimate task [[sources/arxiv-2409.13004]].
- In federated learning, poisoning is delivered by one or more compromised participating clients rather than by centralized data tampering, because clients never expose raw data to the aggregator [[sources/arxiv-2409.13004]].
- A particularly damaging realization is model Trojan installation, where poisoned training data embeds a backdoor that fires on attacker-chosen triggers [[sources/arxiv-2409.13004]].
- Mitigation effectiveness is attack-specific: the Wei et al. (2024) chapter categorizes representative poisoning attacks against the effectiveness of their respective defenses rather than proposing a single universal mitigation [[sources/arxiv-2409.13004]].
- Dynamic model perturbation is proposed as a defense that targets poisoning resilience jointly with privacy protection and model utility [[sources/arxiv-2409.13004]].

## Sources

- [[sources/arxiv-2409.13004]] — Data Poisoning and Leakage Analysis in Federated Learning (2024)

## Related

- [[concepts/model-trojan-attack]]
- [[concepts/dynamic-model-perturbation]]
- [[concepts/cross-silo-federated-learning]]
- [[concepts/gradient-inversion-attack]]
- [[entities/data-poisoning-leakage-fl-chapter]]
