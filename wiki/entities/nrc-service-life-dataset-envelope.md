---
schema_version: 1
type: entity
slug: nrc-service-life-dataset-envelope
canonical_name: NRC Service Life Dataset for Non-Structural Building Envelope Materials
entity_kind: dataset
domains:
- condo-capital-infra
created_at: '2026-05-11T23:25:03Z'
last_updated: '2026-05-27T19:12:45Z'
finalized_at: '2026-05-27T19:12:45Z'
---
# NRC Service Life Dataset for Non-Structural Building Envelope Materials

## Summary

The NRC Service Life Dataset for Non-Structural Building Envelope Materials is a Reference Service Life (RSL) dataset published in October 2025 by the National Research Council Canada Construction Research Centre, providing service-life data for non-structural building envelope materials with Environmental Product Declarations (EPDs) named in the subject scope [[sources/web-2026-05-10-f34]] [[sources/web-2026-05-11-f34]] [[sources/web-2026-05-11-4ef]]. It is an authoritative Canadian national-laboratory primary data source for prior calibration of the building-envelope component in the condo-capital-infra probabilistic reserve engine — federal-scope and analogous in role to the BC Housing provincial Maintenance Matters precedent [[sources/web-2026-05-10-f34]]. A companion 2026 methodology publication by Sadeghi (DOI 10.4224/40003911) documents how the dataset was compiled and surfaces material data-quality limitations in the underlying EPD-derived RSL values [[sources/web-2026-05-11-852]].

## Key facts

### Dataset record (DOI 10.4224/40003877)

- Publisher: National Research Council Canada, Construction Research Centre [[sources/web-2026-05-10-f34]] [[sources/web-2026-05-11-f34]] [[sources/web-2026-05-11-4ef]].
- Authors (all affiliated with NRC Canada Construction): Sara Sadeghi (ORCID 0009-0007-6981-0166), Marzieh Riahinezhad (ORCID 0000-0002-8971-7790), Elnaz Esmizadeh (ORCID 0000-0002-0611-4717), Michael A. Lacasse (ORCID 0000-0001-7640-3701) [[sources/web-2026-05-10-f34]] [[sources/web-2026-05-11-f34]] [[sources/web-2026-05-11-4ef]].
- Publication date: October 2025; record created 2025-11-18 and last modified 2025-11-28 in the NRC Digital Repository [[sources/web-2026-05-10-f34]] [[sources/web-2026-05-11-f34]] [[sources/web-2026-05-11-4ef]].
- DOI: 10.4224/40003877 [[sources/web-2026-05-10-f34]] [[sources/web-2026-05-11-f34]] [[sources/web-2026-05-11-4ef]].
- Record identifier: 36cc8588-5b2c-4f0a-b2e8-505a2037460f [[sources/web-2026-05-10-f34]] [[sources/web-2026-05-11-f34]] [[sources/web-2026-05-11-4ef]].
- Format: Text / Dataset distributed as a 56 KiB XLSX file; language English [[sources/web-2026-05-10-f34]] [[sources/web-2026-05-11-f34]] [[sources/web-2026-05-11-4ef]].
- Subject keywords as published: Reference Service Life (RSL); non-structural building envelope materials; Environmental Product Declarations (EPDs); Service Life Dataset [[sources/web-2026-05-10-f34]] [[sources/web-2026-05-11-f34]] [[sources/web-2026-05-11-4ef]].
- Hosted in the NRC Research Data collection of the NRC Digital Repository [[sources/web-2026-05-10-f34]] [[sources/web-2026-05-11-f34]] [[sources/web-2026-05-11-4ef]].
- The dataset is accessible via the NRC Digital Repository canonical record-view URL (`https://nrc-digital-repository.canada.ca/eng/view/object/?id=36cc8588-5b2c-4f0a-b2e8-505a2037460f`) — a third URL access path alongside the two previously catalogued NRC repository URLs that resolve to the same record [[sources/web-2026-05-11-4ef]].

### Companion methodology paper (DOI 10.4224/40003911, 2026)

- A companion 2026 NRC publication by Sara Sadeghi (DOI 10.4224/40003911) documents the methodology used to compile the dataset and analyzes the state of RSL reporting in the underlying source materials [[sources/web-2026-05-11-852]].
- The compilation methodology proceeds in three stages: (1) compile survey-based and experimentally derived service-life data from the literature; (2) extract all available RSL values from Environmental Product Declarations (EPDs) for non-structural building envelope materials available in North America; (3) organize findings into a detailed dataset and analyze the data to identify existing inconsistencies and knowledge gaps [[sources/web-2026-05-11-852]].
- Stated motivation: support more reliable Life Cycle Assessment (LCA) of buildings, which evaluates environmental impacts across material extraction, construction, operation, and demolition, in the context of Canada's Emissions Reduction Plan targeting a 40% reduction in greenhouse-gas emissions from 2005 to 2030 [[sources/web-2026-05-11-852]].
- The methodology paper frames RSL of non-structural building envelope materials as a key source of uncertainty in LCAs because the durability of non-structural components is generally less well-documented than that of structural ones [[sources/web-2026-05-11-852]].

### Data-quality findings (from the companion methodology paper)

- Nearly half of the EPDs reviewed entirely ignore mentioning the RSL values for non-structural building envelope products, providing no basis for informed life-cycle analysis [[sources/web-2026-05-11-852]].
- Among EPDs that do include an RSL, many rely on a default 75-year building lifespan, often following standard assumptions, without any evidence or justification [[sources/web-2026-05-11-852]].
- Remaining EPDs present widely differing RSL values for identical products, producing fragmented and inconsistent information that reduces the reliability of LCAs [[sources/web-2026-05-11-852]].
- The methodology paper calls for more standardized and transparent RSL reporting in EPDs, particularly for non-structural components, as a precondition for improved environmental impact assessments and better-informed material selection [[sources/web-2026-05-11-852]].
- Implication for engine prior calibration: the dataset's XLSX is structurally easy to ingest, but the underlying RSL values inherit the EPD source-quality issues — missing entries, unjustified 75-year defaults, and per-product variance — and therefore require provenance-aware handling (downweighting unjustified defaults, modeling product-level dispersion) rather than direct use as point priors [[sources/web-2026-05-11-852]].

## Sources

- [[sources/web-2026-05-10-f34]]
- [[sources/web-2026-05-11-f34]]
- [[sources/web-2026-05-11-4ef]]
- [[sources/web-2026-05-11-852]]

## Related

- [[entities/nrc-construction-research-centre]]
- [[entities/bc-housing]]
- [[entities/bc-housing-maintenance-matters-series]]
- [[concepts/reference-service-life]]
- [[concepts/deck-balcony-component-priors]]
- [[concepts/six-probabilistic-components]]
- [[concepts/probabilistic-reserve-modeling]]
