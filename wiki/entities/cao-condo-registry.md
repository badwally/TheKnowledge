---
schema_version: 1
type: entity
slug: cao-condo-registry
canonical_name: CAO Condo Registry
entity_kind: dataset
domains:
- condo-capital-infra
draft: true
draft_started_at: '2026-05-19T14:54:36Z'
draft_unresolved_claims: 0
created_at: '2026-05-19T14:56:13Z'
last_updated: '2026-05-19T14:56:13Z'
---
# CAO Condo Registry

## Summary

The CAO Condo Registry is the free searchable database of Ontario condominium corporations operated by the Condominium Authority of Ontario (CAO), populated from corporations' filings with the CAO and exposing per-corporation address for service, number of voting units, board director names, management company, and other corporation-level fields [[sources/web-2025-11-06-4cc]]. Use of the Registry is explicitly restricted to personal purposes — making the personal-use prohibition the load-bearing legal constraint for any automated Ontario-condo-seed-list adapter in the condo-capital-infra Year-2 ON expansion arm under ADR-0004, exactly analogous in role to the BC Assessment Search Service's private/personal/non-commercial Terms of Use restriction governing the BC strata-property covariate adapter [[sources/web-2025-11-06-4cc]] [[sources/web-2026-05-19-00f]]. The Registry is the authoritative free-tier counterpart to the CAO-administered survey infrastructure documented in the September 2024 CAO Report on Reserve Fund Survey Findings, which characterized the CAO as having distributed a unique survey link to each of the 12,000+ Ontario condominium corporations in its database — anchoring the CAO Registry as the operative population frame for any Ontario-condo addressable-market sizing under the project's Canada-first GTM sequence [[sources/web-2025-11-06-4cc]] [[sources/pdf-condominium-authority-2024-report-on-resrve]].

## Key facts

### Service identity and access

- Operated by the Condominium Authority of Ontario (CAO) [[sources/web-2025-11-06-4cc]].
- Self-described on its landing page as "a free searchable database of condo corporations in Ontario based on those corporation's filings with the Condo Authority" [[sources/web-2025-11-06-4cc]].
- Hosted at the CAO domain under the path /condo-registry-search/ on www.condoauthorityontario.ca [[sources/web-2025-11-06-4cc]].
- Access is free of charge at the registry-search surface — distinguishing the CAO Registry from fee-gated provincial corporate registries [[sources/web-2025-11-06-4cc]].
- Search interface is a structured form with mandatory fields marked with an asterisk (*); the landing page lists the search dimensions under the heading "Search by the Condominium Corporation's:" [[sources/web-2025-11-06-4cc]].
- The landing page is a JavaScript-rendered single-page application — trafilatura extraction captured only the descriptive front-matter text and not the rendered search form or per-corporation result schema, surfacing the JS-rendering NLM-sync gap pattern previously documented for the NS Active Condo Corporations Dataset [[sources/web-2025-11-06-4cc]].

### Per-corporation data fields exposed (as enumerated on the landing page)

- Address for service [[sources/web-2025-11-06-4cc]].
- Number of voting units [[sources/web-2025-11-06-4cc]].
- Board director names [[sources/web-2025-11-06-4cc]].
- Management company [[sources/web-2025-11-06-4cc]].
- The landing-page enumeration closes with "and more," indicating the surfaced field set extends beyond the four explicitly named categories without enumerating the additional fields at the landing-page level [[sources/web-2025-11-06-4cc]].

### Use restriction (personal-purposes-only ToS surface)

- The Condo Registry can only be used for personal purposes — the load-bearing legal constraint on Registry use [[sources/web-2025-11-06-4cc]].
- The personal-use restriction is the operative legal posture that determines whether any automated Ontario-condo-seed-list adapter can use Registry data — under the restriction, an automated bulk scrape is non-compliant on its face, and the compliant paths are (a) individual personal-purpose lookups, (b) a CAO data-sharing agreement negotiated directly with CAO, or (c) substitution from another lawful Ontario-condo data surface [[sources/web-2025-11-06-4cc]].

### Cross-jurisdictional ToS-surface parallel (BC Assessment Search Service)

- The CAO Registry's personal-purposes-only restriction is the Ontario analog to the BC Assessment Search Service's Terms of Use restricting use to "private, personal, non-commercial use" — both operate as per-property/per-corporation data surfaces governed by a use-class prohibition that forces commercial-access negotiations through direct contact with the data publisher [[sources/web-2025-11-06-4cc]] [[sources/web-2026-05-19-00f]].
- The structural parallel between the two ToS surfaces — both publicly-available, both governed by a non-commercial use restriction, both gating commercial access behind a direct-contact path with the public-sector publisher — establishes a two-province ToS-restriction pattern across the project's two highest-priority Canadian expansion jurisdictions (BC and ON) that the can-pilot tos.py adapter must encode for defensible compliance under ADR-0004's Canada-first sequence [[sources/web-2025-11-06-4cc]] [[sources/web-2026-05-19-00f]].

### Population-frame anchor (Ontario condo universe)

- The CAO 2024 Report on Reserve Fund Survey Findings characterized the CAO as having provided a unique survey link to each of the 12,000+ condo corporations in its database — making the CAO database (of which the Registry is the free searchable surface) the operative population frame for the entire Ontario condominium-corporation universe [[sources/pdf-condominium-authority-2024-report-on-resrve]].
- The 12,000+ corporation count anchors the CAO Registry as the load-bearing seed-list source for any Ontario-condo addressable-market sizing or wave-seed-list construction in the condo-capital-infra Year-2 ON expansion arm under ADR-0004 [[sources/web-2025-11-06-4cc]] [[sources/pdf-condominium-authority-2024-report-on-resrve]].

### Companion product (Condo Calendar Tool)

- The same CAO surface also exposes the Condo Calendar Tool, framed as helping condo corporations understand their important legal deadlines, such as holding the AGM, director training deadlines, and sending information certificates [[sources/web-2025-11-06-4cc]].
- The Condo Calendar Tool is personalized based on the information provided by the condo corporation through condo returns and notices of change [[sources/web-2025-11-06-4cc]].
- The Calendar Tool draws on the same upstream filings data set (condo returns and notices of change) that populates the Registry — surfacing the CAO's filings repository as a multi-product back-end serving both the Registry's public-lookup surface and the Calendar's corporation-private deadline-tracking surface [[sources/web-2025-11-06-4cc]].

### Implication for condo-capital-infra GTM

- The personal-use restriction makes the CAO Registry non-addressable via automated bulk scrape for the project's Ontario Year-2 wave seed-list construction; the operative compliant paths are individual personal-purpose lookups, a CAO data-sharing agreement, or substitution from another lawful Ontario-condo data surface — the same three-option compliance perimeter the project already encodes for BC Assessment under the can-pilot tos.py adapter logic [[sources/web-2025-11-06-4cc]] [[sources/web-2026-05-19-00f]].
- The four explicitly named Registry fields (address for service, number of voting units, board director names, management company) define the minimum Ontario covariate ingest schema available from the CAO surface without commercial-access negotiation — covering the corporation-level identification and management-channel fields needed to seed an Ontario condominium-corporation outreach pipeline, but not the funding-adequacy, reserve-fund-balance, or contribution-rate fields needed for capital-renewal targeting (which remain corporation-held records, consistent with the CAO 2024 survey's reliance on direct corporation responses rather than registry queries) [[sources/web-2025-11-06-4cc]] [[sources/pdf-condominium-authority-2024-report-on-resrve]].
- The management-company field is the highest-leverage Registry field for the project's Ontario channel strategy because it surfaces the property-management firms operating across multiple corporations — directly analogous to how the NS Active Condo Corporations Dataset's `declarant` column surfaces developer concentration; both fields enable management-firm channel referral strategies as a leverage path against the per-corporation-acquisition cost [[sources/web-2025-11-06-4cc]].
- The JS-rendered SPA architecture surfaces the same NLM-sync gap pattern previously accepted under ADR-0005 for the NS Active Condo Corporations Dataset's Socrata landing page — trafilatura captures the descriptive text but not the dynamic data surface, so the Registry is citable from the wiki source page but not synthesizable through NLM queries that require the underlying searchable data [[sources/web-2025-11-06-4cc]].

## Sources

- [[sources/web-2025-11-06-4cc]]
- [[sources/web-2026-05-19-00f]]
- [[sources/pdf-condominium-authority-2024-report-on-resrve]]

## Related

- [[entities/condominium-authority-ontario]]
- [[entities/cao-2024-reserve-fund-survey]]
- [[entities/ontario-condominium-act-1998]]
- [[entities/bc-assessment-search-service]]
- [[entities/ns-active-condo-corporations-dataset]]
