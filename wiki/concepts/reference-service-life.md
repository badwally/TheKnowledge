---
schema_version: 1
type: concept
slug: reference-service-life
canonical_name: Reference Service Life (RSL)
domains:
- condo-capital-infra
draft: true
draft_started_at: '2026-05-11T23:28:20Z'
draft_unresolved_claims: 0
created_at: '2026-05-11T23:28:20Z'
last_updated: '2026-05-11T23:28:20Z'
---
# Reference Service Life (RSL)

## Summary

Reference Service Life (RSL) is the expected service-life value reported for a building material or component as a reference parameter for Life Cycle Assessment (LCA) and capital-renewal planning [[sources/web-2026-05-11-852]]. RSL of building materials — particularly non-structural components — is a key source of uncertainty in LCAs because the durability of non-structural components is generally less well-documented than that of structural ones [[sources/web-2026-05-11-852]]. The NRC Canada Construction Research Centre's 2025 Service Life Dataset for Non-Structural Building Envelope Materials is the federal-tier Canadian primary data source for RSL of envelope materials [[sources/web-2026-05-10-f34]] [[sources/web-2026-05-11-f34]] [[sources/web-2026-05-11-4ef]], and operates alongside provincial-tier sources such as BC Housing's Maintenance Matters series, which provides explicit service-life ranges for deck membranes, roofing, and related envelope components [[sources/pdf-bc-housing-2020-maintenance-matters-06]] [[sources/pdf-bc-housing-2020-maintenance-matters-02]]. The 2026 NRC methodology publication by Sadeghi documents material data-quality limitations in the underlying EPD-derived RSL values that constrain the reliability of RSL-based priors [[sources/web-2026-05-11-852]].

## Key claims

- RSL of building materials is a key source of uncertainty in LCAs, particularly for non-structural components whose durability is generally less well-documented than that of structural ones [[sources/web-2026-05-11-852]].
- Environmental Product Declarations (EPDs) are the primary industry source of published RSL values for non-structural building envelope materials available in North America [[sources/web-2026-05-11-852]].
- The NRC envelope-RSL compilation methodology proceeds in three stages: compile survey-based and experimentally derived service-life data from the literature; extract all available RSL values from EPDs for non-structural building envelope materials available in North America; organize findings into a detailed dataset and analyze the data to identify existing inconsistencies and knowledge gaps [[sources/web-2026-05-11-852]].
- Nearly half of EPDs reviewed by the NRC envelope-RSL methodology paper entirely ignore mentioning the RSL values for non-structural building envelope products, providing no basis for informed life-cycle analysis [[sources/web-2026-05-11-852]].
- Among EPDs that do include an RSL, many rely on a default 75-year building lifespan, often following standard assumptions, without any evidence or justification [[sources/web-2026-05-11-852]].
- Remaining EPDs that report RSL values present widely differing values for identical products, producing fragmented and inconsistent information that reduces the reliability of LCAs [[sources/web-2026-05-11-852]].
- More standardized and transparent RSL reporting in EPDs is required, particularly for non-structural components, as a precondition for improved environmental impact assessments and better-informed material selection [[sources/web-2026-05-11-852]].
- BC Housing's Maintenance Matters No. 2 (Maintaining Your Roof) provides a provincial-tier roof service-life range of 10 to over 30 years depending on design, exposure, construction, and materials [[sources/pdf-bc-housing-2020-maintenance-matters-02]].
- BC Housing's Maintenance Matters No. 6 (Decks and Balconies) provides explicit provincial-tier deck-membrane service-life ranges: liquid-applied urethane ~10 years; sheet-applied vinyl PVC 10-15 years; SBS bitumen modified torch-on framed as a stronger two-ply alternative [[sources/pdf-bc-housing-2020-maintenance-matters-06]].
- Implication for engine prior calibration: the NRC dataset is structurally easy to ingest (XLSX format, 56 KiB), but the underlying RSL values inherit the EPD source-quality issues — missing entries, unjustified 75-year defaults, and per-product variance — and therefore require provenance-aware handling (downweighting unjustified defaults, modeling product-level dispersion) rather than direct use as point priors [[sources/web-2026-05-11-852]].
- Federal-tier (NRC) and provincial-tier (BC Housing) RSL sources are methodologically distinct: BC Housing values are empirically derived from a consortium of building-envelope experts working with practical residential maintenance bulletins [[sources/pdf-bc-housing-2020-maintenance-matters-06]] [[sources/pdf-bc-housing-2020-maintenance-matters-02]], while NRC values inherit EPD source-quality issues and require provenance-aware weighting before use in prior calibration [[sources/web-2026-05-11-852]].

## Sources

- [[sources/web-2026-05-11-852]]
- [[sources/web-2026-05-10-f34]]
- [[sources/web-2026-05-11-f34]]
- [[sources/web-2026-05-11-4ef]]
- [[sources/pdf-bc-housing-2020-maintenance-matters-06]]
- [[sources/pdf-bc-housing-2020-maintenance-matters-02]]

## Related

- [[entities/nrc-service-life-dataset-envelope]]
- [[entities/nrc-construction-research-centre]]
- [[entities/bc-housing]]
- [[entities/bc-housing-maintenance-matters-series]]
- [[concepts/deck-balcony-component-priors]]
- [[concepts/six-probabilistic-components]]
- [[concepts/probabilistic-reserve-modeling]]
