---
schema_version: 1
id: arxiv-2206.07284
type: arxiv
title: 'A Survey on Gradient Inversion: Attacks, Defenses and Future Directions'
url: https://arxiv.org/abs/2206.07284
authors:
- Rui Zhang
- Song Guo
- Junxiao Wang
- Xin Xie
- Dacheng Tao
ingested_at: '2026-06-10T22:23:15Z'
content_hash: sha256:ff2da05d0fee93cc6fc14edbccf71a2de317175ba74ccb97c9d5eb3a66f8b708
domains:
- data-collectives
nlm_corpus_ids: []
wiki_pages:
- wiki/entities/gradient-inversion-survey.md
- wiki/concepts/gradient-inversion-attack.md
- wiki/concepts/gradient-inversion-defense.md
meta:
  arxiv_id: '2206.07284'
  categories:
  - cs.LG
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: Accepted by IJCAI-ECAI 2022
  abstract_only: true
published_at: '2022-06-15'
filter:
  score: 0.35
  policy_version: data-collectives-v1
  rationale: Technical survey on gradient inversion attacks and defenses in federated
    learning; addresses privacy-preservation mechanisms but lacks engagement with
    governance structures, incentive design, economic theory, or real-world data-collective
    case studies that form the editorial domain's core focus.
  decided_at: '2026-06-10T22:23:52Z'
  user_correction:
    decided_at: '2026-06-11T02:19:15Z'
    score: 1.0
    rationale: Survey of gradient-inversion attacks in federated learning — documents
      the privacy threat model of the core architecture for pooling proprietary data
      without centralization (criterion 2).
---
Recent studies have shown that the training samples can be recovered from gradients, which are called Gradient Inversion (GradInv) attacks. However, there remains a lack of extensive surveys covering recent advances and thorough analysis of this issue. In this paper, we present a comprehensive survey on GradInv, aiming to summarize the cutting-edge research and broaden the horizons for different domains. Firstly, we propose a taxonomy of GradInv attacks by characterizing existing attacks into two paradigms: iteration- and recursion-based attacks. In particular, we dig out some critical ingredients from the iteration-based attacks, including data initialization, model training and gradient matching. Second, we summarize emerging defense strategies against GradInv attacks. We find these approaches focus on three perspectives covering data obscuration, model improvement and gradient protection. Finally, we discuss some promising directions and open problems for further research.
