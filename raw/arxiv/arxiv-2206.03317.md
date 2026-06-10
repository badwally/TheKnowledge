---
schema_version: 1
id: arxiv-2206.03317
type: arxiv
title: Subject Membership Inference Attacks in Federated Learning
url: https://arxiv.org/abs/2206.03317
authors:
- Anshuman Suri
- Pallika Kanani
- Virendra J. Marathe
- Daniel W. Peterson
ingested_at: '2026-06-10T22:23:53Z'
content_hash: sha256:94a53118b3a576469531ed6e5689612835dc2bb5dd96e9031170a80a28710bcb
domains:
- data-collectives
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2206.03317'
  categories:
  - cs.LG
  - cs.AI
  - cs.CR
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: ''
  abstract_only: true
published_at: '2022-06-07'
filter:
  score: 0.2
  policy_version: data-collectives-v1
  rationale: While the paper addresses federated learning, it is a technical privacy-attack
    paper focused on membership inference threats, not on the governance, incentive
    design, legal frameworks, or economic structures of data collectives. It does
    not analyze any named consortium, cooperative, or collective data arrangement,
    nor does it address how competing or complementary stakeholders would organize
    to pool proprietary data. The mention of differential privacy is only as a defense
    mechanism under evaluation, not as part of a collective data arrangement design.
    Falls outside the domain scope as pure ML security research.
  decided_at: '2026-06-10T22:24:12Z'
  user_correction: null
---
Privacy attacks on Machine Learning (ML) models often focus on inferring the existence of particular data points in the training data. However, what the adversary really wants to know is if a particular individual's (subject's) data was included during training. In such scenarios, the adversary is more likely to have access to the distribution of a particular subject than actual records. Furthermore, in settings like cross-silo Federated Learning (FL), a subject's data can be embodied by multiple data records that are spread across multiple organizations. Nearly all of the existing private FL literature is dedicated to studying privacy at two granularities -- item-level (individual data records), and user-level (participating user in the federation), neither of which apply to data subjects in cross-silo FL. This insight motivates us to shift our attention from the privacy of data records to the privacy of data subjects, also known as subject-level privacy. We propose two novel black-box attacks for subject membership inference, of which one assumes access to a model after each training round. Using these attacks, we estimate subject membership inference risk on real-world data for single-party models as well as FL scenarios. We find our attacks to be extremely potent, even without access to exact training records, and using the knowledge of membership for a handful of subjects. To better understand the various factors that may influence subject privacy risk in cross-silo FL settings, we systematically generate several hundred synthetic federation configurations, varying properties of the data, model design and training, and the federation itself. Finally, we investigate the effectiveness of Differential Privacy in mitigating this threat.
