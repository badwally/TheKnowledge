---
schema_version: 1
type: entity
slug: subject-membership-inference-paper
canonical_name: Subject Membership Inference Attacks in Federated Learning (Suri et
  al., 2022)
entity_kind: paper
domains:
- data-collectives
created_at: '2026-06-10T22:23:53Z'
last_updated: '2026-06-10T22:23:53Z'
draft: true
draft_started_at: '2026-06-10T22:23:53Z'
draft_unresolved_claims: 0
---

# Subject Membership Inference Attacks in Federated Learning (Suri et al., 2022)

## Summary

"Subject Membership Inference Attacks in Federated Learning" is a 2022 arXiv preprint (2206.03317) by Anshuman Suri, Pallika Kanani, Virendra J. Marathe, and Daniel W. Peterson that introduces the notion of subject-level privacy in cross-silo federated learning and proposes two black-box attacks that infer whether a particular individual (data subject) was represented in the training data, even when the subject's records are distributed across multiple participating organizations [[sources/arxiv-2206.03317]].

## Key facts

- Authors: Anshuman Suri, Pallika Kanani, Virendra J. Marathe, Daniel W. Peterson [[sources/arxiv-2206.03317]].
- Published as an arXiv preprint on 2022-06-07 under primary category cs.LG (also cs.AI, cs.CR) [[sources/arxiv-2206.03317]].
- Argues that existing private federated-learning literature only addresses item-level privacy (individual records) and user-level privacy (participating federation members), neither of which captures the privacy of a data subject whose records are spread across multiple organizations in cross-silo federated learning [[sources/arxiv-2206.03317]].
- Proposes two novel black-box subject-membership-inference attacks; one variant assumes the adversary observes the model after each training round [[sources/arxiv-2206.03317]].
- Reports the attacks to be "extremely potent" without access to the subject's exact training records, using only knowledge of membership for a handful of other subjects [[sources/arxiv-2206.03317]].
- Systematically generates several hundred synthetic federation configurations, varying data, model design and training, and federation properties, to estimate how each factor influences subject-membership-inference risk [[sources/arxiv-2206.03317]].
- Empirically investigates Differential Privacy as a mitigation against the subject-membership-inference threat [[sources/arxiv-2206.03317]].

## Sources

- [[sources/arxiv-2206.03317]]

## Related

- [[concepts/subject-membership-inference-attack]]
- [[concepts/subject-level-privacy]]
- [[concepts/cross-silo-federated-learning]]
- [[concepts/gradient-inversion-attack]]
- [[entities/gradient-inversion-survey]]
