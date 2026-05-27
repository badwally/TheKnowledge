---
schema_version: 1
type: entity
slug: cari-framework
canonical_name: CARI (Community Association Risk Index) Consent Framework
entity_kind: product
domains:
- condo-software
created_at: '2026-05-24T03:40:38Z'
last_updated: '2026-05-24T03:40:38Z'
---

# CARI (Community Association Risk Index) Consent Framework

## Summary

The Community Association Risk Index (CARI) is CommunityPay's consent and access-control framework governing programmatic access to association data through CommunityPay's APIs [[sources/web-2026-02-11-4eb]]. CARI is the access-control substrate underneath the CommunityPay Condo Questionnaire API: a lender, title company, or management company querying for Fannie Mae 1076 / Freddie Mac 1077 data must do so under CARI, the HOA must have authorized access, queries are scoped (e.g., questionnaire:read), and every query is metered (5 credits for Condo Questionnaire) and logged with a full audit trail [[sources/web-2026-02-11-4eb]].

## Key facts

- Full name: Community Association Risk Index [[sources/web-2026-02-11-4eb]].
- Acts as a consent-gating framework for programmatic access to association data through CommunityPay APIs [[sources/web-2026-02-11-4eb]].
- HOA authorization is required before a third party (lender, title company, management company) can query a given association's data [[sources/web-2026-02-11-4eb]].
- Uses named scopes for query authorization (the documented scope for the Condo Questionnaire API is questionnaire:read) [[sources/web-2026-02-11-4eb]].
- Uses a credit-based metering model (the Condo Questionnaire API is metered at 5 credits per query) [[sources/web-2026-02-11-4eb]].
- Every query is logged with a full audit trail [[sources/web-2026-02-11-4eb]].
- Positioned as the access-control substrate that lets CommunityPay's marketing copy frame programmatic data access as a no-phone-call, no-email-chain, no-manual-form workflow for lenders and title companies [[sources/web-2026-02-11-4eb]].

## Sources

- [[sources/web-2026-02-11-4eb]] — Scott Vuilleumier, "Fannie Mae 1076 Condo Questionnaire: Why Manual Completion Fails and How Auto-Fill Changes Everything" (communitypay.us blog, February 11, 2026)

## Related

- [[entities/communitypay]]
- [[entities/communitypay-condo-questionnaire-api]]
