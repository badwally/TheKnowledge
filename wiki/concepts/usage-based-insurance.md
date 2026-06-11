---
schema_version: 1
type: concept
slug: usage-based-insurance
canonical_name: Usage-Based Insurance (UBI)
domains:
- data-collectives
created_at: '2026-06-11T06:35:01Z'
last_updated: '2026-06-11T06:35:01Z'
draft: true
draft_started_at: '2026-06-11T06:35:01Z'
draft_unresolved_claims: 0
---

# Usage-Based Insurance (UBI)

## Summary

Usage-based insurance (UBI) is a class of auto insurance pricing in which vehicle telematics data — capturing real-world driving behavior — is used by carriers to assess risk and price premiums at point of quote, underwriting, and renewal [[sources/web-2026-01-01-dec]]. Telematics data is positioned as highly predictive of driving risk and intended to be used alongside standard rating variables such as claims history and credit-based insurance scores, not as a replacement for them [[sources/web-2026-01-01-dec]].

## Key claims

- Vehicle telematics data is highly predictive of driving risk and is best used alongside other standard rating variables, including claims history and credit-based insurance scores [[sources/web-2026-01-01-dec]].
- UBI can be insurer-led (a program the carrier itself runs) or accessed via third-party data exchanges that let carriers participate without operating their own telematics program [[sources/web-2026-01-01-dec]].
- Telematics-driven pricing applies across the policy lifecycle: point of quote, underwriting, and renewal [[sources/web-2026-01-01-dec]].
- Scaling UBI faces a "many-to-many challenge": telematics data sources differ across automotive brand, vehicle, and device, and each insurer would otherwise have to build its own scoring methodology and ingestion pipeline per source [[sources/web-2026-01-01-dec]].
- Intermediary platforms such as the LexisNexis Telematics Exchange solve the many-to-many challenge by normalizing data from multiple sources into a single insurer-consumable feed [[sources/web-2026-01-01-dec]].
- UBI is positioned by vendors as a vehicle for offering consumers more personalized insurance products and potentially reducing total cost of vehicle ownership [[sources/web-2026-01-01-dec]].
- Telematics data integration into the insurance workflow is framed as enabling a more transparent insurer-consumer relationship [[sources/web-2026-01-01-dec]].

## Sources

- [[sources/web-2026-01-01-dec]] — LexisNexis Telematics Exchange product page

## Related

- [[entities/lexisnexis-telematics-exchange]] — exchange platform supporting UBI at scale
- [[entities/lexisnexis-telematics-ondemand]] — UBI-enabling insurer product
- [[concepts/telematics-data-aggregation]] — upstream mechanism that feeds UBI
