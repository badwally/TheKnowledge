---
schema_version: 1
id: arxiv-2605.22401
type: arxiv
title: Cross-Species RSA Reveals Conserved Early Visual Alignment but Divergent Higher-Area
  Rankings Across Human fMRI and Macaque Electrophysiology
url: https://arxiv.org/abs/2605.22401
authors:
- Nils Leutenegger
ingested_at: '2026-05-30T20:40:15Z'
content_hash: sha256:6ac40caed82883fdbd323a7bb4020e46e49e8ed6fc76898503fd78e7624973d1
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  arxiv_id: '2605.22401'
  categories:
  - cs.LG
  - cs.NE
  - q-bio.NC
  doi: ''
  primary_category: cs.LG
  journal_ref: ''
  comment: 9 pages, 6 figures
  abstract_only: true
published_at: '2026-05-21'
filter:
  score: 0.88
---
Does the relationship between learning rules and brain alignment generalize across species? We extend our prior finding that untrained CNNs match backpropagation at human V1 by testing the same five learning rules against macaque electrophysiology. The rules are backpropagation (BP), feedback alignment (FA), predictive coding (PC), spike-timing-dependent plasticity (STDP), and an untrained random-weights baseline. The macaque data come from two datasets: MajajHong2015 (V4/IT, 3,200 stimulus presentations, 88/168 neurons) and FreemanZiemba2013 (V1/V2, 135 stimuli, 102/103 neurons). Using RSA with identical model weights from our human study, we find: (1) all models achieve higher alignment with macaque early visual cortex (rho = 0.15-0.30 at V1/V2) than with human fMRI (rho = 0.01-0.08), consistent with the higher signal-to-noise ratio of electrophysiology; (2) STDP and PC produce the highest macaque V1/V2 alignment (rho ~ 0.30 and 0.28), consistent with their leading position among trained rules in human V1; (3) at IT, learning rule rankings show no detectable correlation across species (Kendall's tau = 0.00, p = 1.00), though this null result is expected given that n = 5 provides power only at tau = +/-1.0, and is further confounded by stimulus set differences; (4) a pretrained ResNet-50 (ImageNet) achieves rho = 0.25 at macaque IT, substantially above all custom CNN conditions (rho = 0.07-0.14), suggesting IT alignment is limited by model capacity and training data rather than by the learning rule. Noise ceilings, multi-seed variability (5 seeds), and a stimulus-control analysis are reported. These results demonstrate that early visual alignment is robust across species, while higher-area alignment is modulated by model capacity and stimulus domain.
