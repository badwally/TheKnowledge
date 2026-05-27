---
schema_version: 1
type: concept
slug: deck-balcony-component-priors
canonical_name: Deck and Balcony Component Priors
domains:
- condo-capital-infra
draft: true
draft_started_at: '2026-05-11T23:28:20Z'
draft_unresolved_claims: 0
created_at: '2026-05-11T23:28:20Z'
last_updated: '2026-05-11T23:28:20Z'
---
# Deck and Balcony Component Priors

## Summary

Deck and balcony component priors are the distributional service-life, failure-mode, and inspection-cadence assumptions used to calibrate the probabilistic envelope-component model within the condo-capital-infra reserve engine for deck membranes, balcony membranes, guardrails / guardwalls, drainage components, soffits, and vents [[sources/pdf-bc-housing-2020-maintenance-matters-06]]. The primary provincial-tier Canadian source for these priors is BC Housing's Maintenance Matters bulletin series — specifically Bulletin No. 6 (Decks and Balconies) and Bulletin No. 2 (Maintaining Your Roof, applicable where decks sit over enclosed space) [[sources/pdf-bc-housing-2020-maintenance-matters-06]] [[sources/pdf-bc-housing-2020-maintenance-matters-02]]. The federal-tier Canadian source is the NRC Canada Construction Research Centre's 2025 Service Life Dataset for Non-Structural Building Envelope Materials, which provides Reference Service Life (RSL) values across non-structural envelope materials including those used in deck and balcony assemblies [[sources/web-2026-05-10-f34]] [[sources/web-2026-05-11-f34]] [[sources/web-2026-05-11-4ef]]. The NRC methodology findings on EPD data-quality limitations directly constrain the reliability of the federal-tier priors for deck and balcony components [[sources/web-2026-05-11-852]].

## Key claims

- BC Housing's Maintenance Matters No. 6 distinguishes decks (over enclosed space, therefore also roofs) from balconies (projecting from the building, not over enclosed living space) — a definitional split that determines which BC Housing bulletin applies to each component [[sources/pdf-bc-housing-2020-maintenance-matters-06]].
- Deck-membrane service-life priors from BC Housing MM-06: liquid-applied urethane ~10 years; sheet-applied vinyl PVC 10-15 years; SBS bitumen modified torch-on framed as a stronger two-ply alternative [[sources/pdf-bc-housing-2020-maintenance-matters-06]].
- Inspection-cadence priors from BC Housing MM-06: biennial inspection for membranes and guardrails; annual inspection for scupper attachments; twice-yearly surface cleaning [[sources/pdf-bc-housing-2020-maintenance-matters-06]].
- Step-up inspection trigger from BC Housing MM-06: increased inspection frequency at 15+ years of membrane age [[sources/pdf-bc-housing-2020-maintenance-matters-06]].
- BC Housing MM-06 covers failure modes across membranes, guardrails / guardwalls, drainage, soffits, and vents — defining the component-level taxonomy used for deck and balcony prior calibration [[sources/pdf-bc-housing-2020-maintenance-matters-06]].
- The roof service-life range from BC Housing MM-02 (10 to over 30 years depending on design, exposure, construction, and materials) applies to deck-over-enclosed-space assemblies that are structurally also roofs [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- The NRC Service Life Dataset for Non-Structural Building Envelope Materials provides federal-tier Reference Service Life (RSL) values for envelope materials, distributed as a 56 KiB XLSX file via the NRC Digital Repository under DOI 10.4224/40003877 [[sources/web-2026-05-10-f34]] [[sources/web-2026-05-11-f34]] [[sources/web-2026-05-11-4ef]].
- The NRC RSL dataset is sourced primarily from Environmental Product Declarations (EPDs) and the published literature; the methodology paper documents that nearly half of reviewed EPDs entirely ignore mentioning RSL, many rely on unjustified 75-year defaults, and remaining values vary widely for identical products [[sources/web-2026-05-11-852]].
- Federal-tier (NRC) and provincial-tier (BC Housing) priors must be reconciled with provenance-aware weighting: NRC values inherit EPD source-quality issues and require downweighting unjustified defaults plus modeling product-level dispersion; BC Housing values are empirically derived from a building-envelope-expert consortium tied to BC Housing's Maintenance Matters bulletin series [[sources/web-2026-05-11-852]] [[sources/pdf-bc-housing-2020-maintenance-matters-06]] [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- Deck and balcony priors feed the building-envelope component of the six-component probabilistic reserve engine and operate alongside roof priors (where decks sit over enclosed space) and the long-tail deterministic coverage required for CAI-compliant deliverables [[sources/pdf-bc-housing-2020-maintenance-matters-06]] [[sources/pdf-bc-housing-2020-maintenance-matters-02]].

## Sources

- [[sources/pdf-bc-housing-2020-maintenance-matters-06]]
- [[sources/pdf-bc-housing-2020-maintenance-matters-02]]
- [[sources/web-2026-05-10-f34]]
- [[sources/web-2026-05-11-f34]]
- [[sources/web-2026-05-11-4ef]]
- [[sources/web-2026-05-11-852]]

## Related

- [[entities/bc-housing]]
- [[entities/bc-housing-maintenance-matters-series]]
- [[entities/nrc-service-life-dataset-envelope]]
- [[entities/nrc-construction-research-centre]]
- [[concepts/reference-service-life]]
- [[concepts/six-probabilistic-components]]
- [[concepts/probabilistic-reserve-modeling]]
