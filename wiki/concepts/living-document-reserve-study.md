---
type: concept
slug: living-document-reserve-study
canonical_name: Living-Document Reserve Study
domains:
  - condo-software
---

# Living-Document Reserve Study

## Summary

A "living document" reserve study is one that updates automatically whenever the underlying inputs change in the source system, rather than being delivered as a static PDF artifact at the end of a periodic consulting engagement [[sources/web-2024-11-01-fc2]]. The model is structurally distinct from traditional reserve-study delivery: in CommunityPay's framing, consultant-produced studies "become outdated immediately" because consultants visit once, estimate useful lives, and deliver a static PDF — by year two the numbers no longer reflect reality [[sources/web-2024-11-01-fc2]]. The living-document model resolves that staleness by binding the reserve study to the same platform that holds the ledger, the asset registry, and the payment system, so that every component replacement, balance change, or useful-life adjustment recalculates the study in place [[sources/web-2024-11-01-fc2]].

## Key claims

- A living-document reserve study updates automatically when relevant data changes in the source system, in contrast to static PDF deliverables [[sources/web-2024-11-01-fc2]].
- The model requires the reserve-study module to be integrated with the source accounting / asset registry / payment system, so that there is no duplicate data entry and no manual reconciliation [[sources/web-2024-11-01-fc2]].
- The claimed cadence advantage is that reserve analysis reflects reality "updated continuously, not every three years" [[sources/web-2024-11-01-fc2]].
- The model's defining structural feature is automatic recalculation on a defined set of trigger events (balance changes, component replacements, registry additions, contribution-rate changes, useful-life adjustments) rather than scheduled periodic recomputation [[sources/web-2024-11-01-fc2]].
- A worked example of the model: when a roof is replaced, posting the expense to the ledger updates the component registry, resets useful life, recalculates projections, and adjusts percent funded — all automatically [[sources/web-2024-11-01-fc2]].

## Sources

- [[sources/web-2024-11-01-fc2]] — CommunityPay, "Automated Reserve Studies" product page (communitypay.us/features/reserve-studies/, November 1, 2024)

## Related

- [[entities/communitypay]]
- [[concepts/level-3-reserve-study]]
- [[concepts/reserve-study-automatic-triggers]]
- [[concepts/percent-funded]]
