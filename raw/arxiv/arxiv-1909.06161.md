---
schema_version: 1
id: arxiv-1909.06161
type: arxiv
title: Brain-Like Object Recognition with High-Performing Shallow Recurrent ANNs
url: https://arxiv.org/abs/1909.06161
authors:
- Jonas Kubilius
- Martin Schrimpf
- Kohitij Kar
- Ha Hong
- Najib J. Majaj
- Rishi Rajalingham
- Elias B. Issa
- Pouya Bashivan
- Jonathan Prescott-Roy
- Kailyn Schmidt
- Aran Nayebi
- Daniel Bear
- Daniel L. K. Yamins
- James J. DiCarlo
ingested_at: '2026-06-01T23:44:43Z'
content_hash: sha256:954d78af23f62c4975b2e8bf71f6d119ca045d4fa2a6f16c40d26eb4ced2177b
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '1909.06161'
  categories:
  - cs.CV
  - cs.LG
  - cs.NE
  - eess.IV
  - q-bio.NC
  doi: ''
  primary_category: cs.CV
  journal_ref: ''
  comment: NeurIPS 2019 (Oral). Code available at https://github.com/dicarlolab/neurips2019
  abstract_only: true
published_at: '2019-09-13'
filter:
  score: 1.0
---
Deep convolutional artificial neural networks (ANNs) are the leading class of candidate models of the mechanisms of visual processing in the primate ventral stream. While initially inspired by brain anatomy, over the past years, these ANNs have evolved from a simple eight-layer architecture in AlexNet to extremely deep and branching architectures, demonstrating increasingly better object categorization performance, yet bringing into question how brain-like they still are. In particular, typical deep models from the machine learning community are often hard to map onto the brain's anatomy due to their vast number of layers and missing biologically-important connections, such as recurrence. Here we demonstrate that better anatomical alignment to the brain and high performance on machine learning as well as neuroscience measures do not have to be in contradiction. We developed CORnet-S, a shallow ANN with four anatomically mapped areas and recurrent connectivity, guided by Brain-Score, a new large-scale composite of neural and behavioral benchmarks for quantifying the functional fidelity of models of the primate ventral visual stream. Despite being significantly shallower than most models, CORnet-S is the top model on Brain-Score and outperforms similarly compact models on ImageNet. Moreover, our extensive analyses of CORnet-S circuitry variants reveal that recurrence is the main predictive factor of both Brain-Score and ImageNet top-1 performance. Finally, we report that the temporal evolution of the CORnet-S "IT" neural population resembles the actual monkey IT population dynamics. Taken together, these results establish CORnet-S, a compact, recurrent ANN, as the current best model of the primate ventral visual stream.
