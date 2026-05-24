---
id: arxiv-2204.12404
type: arxiv
title: Hierarchical Bayesian Modelling for Knowledge Transfer Across Engineering Fleets
  via Multitask Learning
url: https://arxiv.org/abs/2204.12404
authors:
- L. A. Bull
- D. Di Francesco
- M. Dhada
- O. Steinert
- T. Lindgren
- A. K. Parlikad
- A. B. Duncan
- M. Girolami
ingested_at: '2026-05-20T17:36:34Z'
content_hash: sha256:7c420c1ee1d1b92c728eb49ed4d5593bb7d7b609c13b8e056beedd249efdc4e2
domains: []
nlm_corpus_ids: []
wiki_pages:
- wiki/concepts/hierarchical-bayesian-modelling.md
- wiki/concepts/multitask-learning.md
- wiki/concepts/bayesian-transfer-learning.md
- wiki/concepts/partial-pooling.md
- wiki/concepts/population-level-analysis.md
- wiki/concepts/engineering-fleet-management.md
- wiki/entities/lawrence-bull.md
- wiki/entities/mark-girolami.md
- wiki/entities/ajith-parlikad.md
meta:
  arxiv_id: '2204.12404'
  categories:
  - stat.ML
  - cs.LG
  - eess.SP
  - stat.AP
  doi: 10.1111/mice.12901
  primary_category: stat.ML
  journal_ref: Hierarchical Bayesian modeling for knowledge transfer across engineering
    fleets via multitask learning (2022) Computer-Aided Civil and Infrastructure Engineering
    1-28
  comment: ''
  abstract_only: true
published_at: '2022-04-26'
---
A population-level analysis is proposed to address data sparsity when building predictive models for engineering infrastructure. Utilising an interpretable hierarchical Bayesian approach and operational fleet data, domain expertise is naturally encoded (and appropriately shared) between different sub-groups, representing (i) use-type, (ii) component, or (iii) operating condition. Specifically, domain expertise is exploited to constrain the model via assumptions (and prior distributions) allowing the methodology to automatically share information between similar assets, improving the survival analysis of a truck fleet and power prediction in a wind farm. In each asset management example, a set of correlated functions is learnt over the fleet, in a combined inference, to learn a population model. Parameter estimation is improved when sub-fleets share correlated information at different levels of the hierarchy. In turn, groups with incomplete data automatically borrow statistical strength from those that are data-rich. The statistical correlations enable knowledge transfer via Bayesian transfer learning, and the correlations can be inspected to inform which assets share information for which effect (i.e. parameter). Both case studies demonstrate the wide applicability to practical infrastructure monitoring, since the approach is naturally adapted between interpretable fleet models of different in situ examples.
