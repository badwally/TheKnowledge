---
schema_version: 1
id: arxiv-2409.13004
type: arxiv
title: Data Poisoning and Leakage Analysis in Federated Learning
url: https://arxiv.org/abs/2409.13004
authors:
- Wenqi Wei
- Tiansheng Huang
- Zachary Yahn
- Anoop Singhal
- Margaret Loper
- Ling Liu
ingested_at: '2026-06-10T22:24:13Z'
content_hash: sha256:12325cbebda2c69758514e64003c93e353cb5846871845a4074b74c0880db5be
domains:
- data-collectives
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2409.13004'
  categories:
  - cs.LG
  doi: 10.1007/978-3-031-58923-2_3
  primary_category: cs.LG
  journal_ref: ''
  comment: Chapter of Handbook of Trustworthy Federated Learning
  abstract_only: true
published_at: '2024-09-19'
filter:
  score: 0.1
  policy_version: data-collectives-v1
  rationale: 'This is a rigorous peer-reviewed security analysis of federated learning''s
    threat landscape (data poisoning, privacy leakage, model robustness). However,
    it addresses zero of the six inclusion criteria: no discussion of data collective
    governance, incentive/valuation structures, named industry consortia, economic
    theory of data pooling, legal frameworks, or policy interventions. It treats federated
    learning as a generic technical infrastructure for distributed training, not as
    a mechanism enabling competitive stakeholders to pool proprietary data. Clearly
    off-topic for the domain.'
  decided_at: '2026-06-10T22:24:43Z'
  user_correction: null
---
Data poisoning and leakage risks impede the massive deployment of federated learning in the real world. This chapter reveals the truths and pitfalls of understanding two dominating threats: {\em training data privacy intrusion} and {\em training data poisoning}. We first investigate training data privacy threat and present our observations on when and how training data may be leaked during the course of federated training. One promising defense strategy is to perturb the raw gradient update by adding some controlled randomized noise prior to sharing during each round of federated learning. We discuss the importance of determining the proper amount of randomized noise and the proper location to add such noise for effective mitigation of gradient leakage threats against training data privacy. Then we will review and compare different training data poisoning threats and analyze why and when such data poisoning induced model Trojan attacks may lead to detrimental damage on the performance of the global model. We will categorize and compare representative poisoning attacks and the effectiveness of their mitigation techniques, delivering an in-depth understanding of the negative impact of data poisoning. Finally, we demonstrate the potential of dynamic model perturbation in simultaneously ensuring privacy protection, poisoning resilience, and model performance. The chapter concludes with a discussion on additional risk factors in federated learning, including the negative impact of skewness, data and algorithmic biases, as well as misinformation in training data. Powered by empirical evidence, our analytical study offers some transformative insights into effective privacy protection and security assurance strategies in attack-resilient federated learning.
