---
schema_version: 1
type: concept
slug: subject-membership-inference-attack
canonical_name: Subject Membership Inference Attack
domains:
- data-collectives
created_at: '2026-06-10T22:23:53Z'
last_updated: '2026-06-10T22:23:53Z'
draft: true
draft_started_at: '2026-06-10T22:23:53Z'
draft_unresolved_claims: 0
---

# Subject Membership Inference Attack

## Summary

A subject membership inference (subject-MI) attack is a privacy attack against a machine learning model that infers whether any data belonging to a particular individual (data subject) was used to train the model, as opposed to item-level membership inference which asks whether a specific record was used [[sources/arxiv-2206.03317]]. The attack class is motivated by cross-silo federated learning, where one subject's data can be embodied by multiple records distributed across several participating organizations [[sources/arxiv-2206.03317]].

## Key claims

- In subject-MI threat models, the adversary typically has access only to the distribution of a particular subject (not exact training records) and infers subject membership via black-box queries to the model [[sources/arxiv-2206.03317]].
- Suri et al. (2022) propose two novel black-box subject-MI attacks; one variant assumes the adversary can observe the model after each training round of the federated learning protocol [[sources/arxiv-2206.03317]].
- The attacks are reported to be "extremely potent" even when the adversary lacks exact training records and only knows the subject-membership status of a small number of other subjects [[sources/arxiv-2206.03317]].
- Subject-MI risk is influenced by data properties, model design, training procedure, and federation configuration; Suri et al. quantify these effects across several hundred synthetic cross-silo federation setups [[sources/arxiv-2206.03317]].
- Differential Privacy is evaluated as a candidate mitigation against subject-MI [[sources/arxiv-2206.03317]].

## Sources

- [[sources/arxiv-2206.03317]]

## Related

- [[concepts/subject-level-privacy]]
- [[concepts/cross-silo-federated-learning]]
- [[concepts/gradient-inversion-attack]]
- [[concepts/gradient-inversion-defense]]
- [[entities/subject-membership-inference-paper]]
