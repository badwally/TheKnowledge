---
schema_version: 1
type: concept
slug: subject-level-privacy
canonical_name: Subject-Level Privacy
domains:
- data-collectives
created_at: '2026-06-10T22:23:53Z'
last_updated: '2026-06-10T22:23:53Z'
draft: true
draft_started_at: '2026-06-10T22:23:53Z'
draft_unresolved_claims: 0
---

# Subject-Level Privacy

## Summary

Subject-level privacy is a granularity of privacy protection that targets the privacy of an individual data subject — all records about one person — rather than the privacy of a single record (item-level) or of a participating federation member (user-level) [[sources/arxiv-2206.03317]]. Suri et al. (2022) argue it is the natural privacy unit in cross-silo federated learning, where one subject's data can be distributed across multiple participating organizations' silos [[sources/arxiv-2206.03317]].

## Key claims

- The existing private federated learning literature studies privacy at two granularities — item-level (individual data records) and user-level (participating user in the federation) — neither of which applies to data subjects in cross-silo federated learning [[sources/arxiv-2206.03317]].
- In cross-silo federated learning a single subject's data can be embodied by multiple records spread across multiple participating organizations, so neither item-level nor user-level protections grant the subject a meaningful privacy guarantee [[sources/arxiv-2206.03317]].
- Shifting from record-centric to subject-centric privacy motivates new threat models such as subject membership inference [[sources/arxiv-2206.03317]].

## Sources

- [[sources/arxiv-2206.03317]]

## Related

- [[concepts/subject-membership-inference-attack]]
- [[concepts/cross-silo-federated-learning]]
- [[entities/subject-membership-inference-paper]]
