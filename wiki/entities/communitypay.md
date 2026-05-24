---
type: entity
slug: communitypay
canonical_name: CommunityPay
entity_kind: organization
domains:
  - condo-software
---

# CommunityPay

## Summary

CommunityPay is a bootstrapped, pre-funding community association management (CAM) software vendor positioning its platform as a system of record whose live general ledger can answer regulatory and lender-driven disclosure questions programmatically [[sources/web-2026-02-11-4eb]]. The company's load-bearing product surface is the Condo Questionnaire API, which auto-fills all 8 sections of the Fannie Mae 1076 / Freddie Mac 1077 questionnaire from live ledger data and is positioned as the structural fix to the closing-delay problem that arises when boards manually gather data from disparate insurance, financial, AR, governance, and legal sources [[sources/web-2026-02-11-4eb]]. Access to the API is consent-gated through CommunityPay's Community Association Risk Index (CARI) consent framework and is metered at 5 credits per query with full audit-trail logging [[sources/web-2026-02-11-4eb]]. The company runs a state-by-state resale certificate product line on the same live-ledger infrastructure (Washington, California Civil Code §4525, Oregon) and tracks 548 statutes across 51 states in a Living Legal Corpus authored by Scott Vuilleumier [[sources/web-2026-02-11-4eb]].

## Key facts

- Operates the communitypay.us web domain and publishes technical product content under the communitypay.us/blog/ path [[sources/web-2026-02-11-4eb]].
- Bootstrapped and pre-funding as of February 2026: no SEC filings, analyst coverage, or independent corroboration of customer count or ARR exist; the company's own technical blog is the canonical primary source [[sources/web-2026-02-11-4eb]].
- Product positioning frames CommunityPay as the system of record whose live general ledger directly answers Fannie Mae 1076 / Freddie Mac 1077 questionnaire fields, eliminating the manual data-gathering bottleneck [[sources/web-2026-02-11-4eb]].
- Markets the Condo Questionnaire API as the product surface that auto-fills all 8 sections of the Form 1076 from live ledger data at the moment of the API call (not from a cached export) [[sources/web-2026-02-11-4eb]].
- API queries are consent-gated through the CARI (Community Association Risk Index) consent framework requiring HOA authorization and full audit-trail logging per query [[sources/web-2026-02-11-4eb]].
- API metering: 5 credits per Condo Questionnaire query under the questionnaire:read scope [[sources/web-2026-02-11-4eb]].
- Weighted data completeness score returned with each query: delinquency and reserves weighted at 20% each; budget and insurance weighted at 15% each [[sources/web-2026-02-11-4eb]].
- Named API data models referenced in the Form 1076 auto-fill workflow: HOAInsurancePolicy, Budget, Fund, Unit, SpecialAssessmentRecord, AR Invoice, ReserveComponentService, BoardMemberTenure, GovernanceAttestation [[sources/web-2026-02-11-4eb]].
- Operates a parallel state-by-state resale-certificate product line on the same live-ledger infrastructure, with documented coverage of Washington (20–26 statutory disclosure items), California (15-item Civil Code §4525 framework), and Oregon [[sources/web-2026-02-11-4eb]].
- Tracks 548 statutes across 51 U.S. states in a "Living Legal Corpus" attributed to Scott Vuilleumier [[sources/web-2026-02-11-4eb]].
- Filed two named patents authored by Scott Vuilleumier: PAT-002 (Enforcement Dispatcher) and PAT-003 (Living Legal Corpus) [[sources/web-2026-02-11-4eb]].
- GTM channels named in the marketing copy: lenders, title companies, management companies, and boards — addressed as distinct API and product audiences [[sources/web-2026-02-11-4eb]].

## Sources

- [[sources/web-2026-02-11-4eb]] — Scott Vuilleumier, "Fannie Mae 1076 Condo Questionnaire: Why Manual Completion Fails and How Auto-Fill Changes Everything" (communitypay.us blog, February 11, 2026)

## Related

- [[entities/scott-vuilleumier]]
- [[entities/communitypay-condo-questionnaire-api]]
- [[entities/cari-framework]]
- [[entities/fannie-mae-form-1076]]
- [[entities/freddie-mac-form-1077]]
- [[concepts/fannie-mae-condo-project-eligibility]]
- [[concepts/fannie-mae-15-percent-delinquency-threshold]]
- [[concepts/live-ledger-auto-fill-pattern]]
