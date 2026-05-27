---
schema_version: 1
type: concept
slug: reserve-study-automatic-triggers
canonical_name: Reserve Study Automatic Update Triggers
domains:
- condo-software
created_at: '2026-05-24T03:18:38Z'
last_updated: '2026-05-24T03:18:38Z'
---

# Reserve Study Automatic Update Triggers

## Summary

Automatic update triggers are the defined set of source-system events that cause a platform-native reserve study to recompute in place, without a scheduled periodic re-run or a consultant engagement. The CommunityPay reserve-studies module enumerates five trigger events and five downstream recalculations — together constituting the structural mechanism behind the platform's "living document" positioning [[sources/web-2024-11-01-fc2]]. The trigger / recalculation taxonomy is the operational bridge between the platform's accounting / asset-registry / payments integration and the user-facing claim that reserve analysis is "updated continuously, not every three years" [[sources/web-2024-11-01-fc2]].

## Key claims

- The five named trigger events on the CommunityPay platform are: reserve fund balance changes, component replaced (expenditure posted), new component added to registry, contribution rate changed, and useful life adjustment [[sources/web-2024-11-01-fc2]].
- The five named downstream recalculations on each trigger are: percent funded recalculates, 30-year projections refresh, funding recommendations adjust, deficit warnings update, board reports regenerate [[sources/web-2024-11-01-fc2]].
- A worked example of the trigger / recalculation chain: a roof replacement posted to the ledger updates the component registry, resets the useful life, recalculates the projections, and adjusts percent funded — all automatically [[sources/web-2024-11-01-fc2]].
- The trigger model is structurally dependent on the reserve-study module sharing a database with the source ledger, asset registry, and payment platform — "no duplicate data entry. No manual reconciliation." [[sources/web-2024-11-01-fc2]]
- The trigger-based model is positioned by CommunityPay as the operational answer to the staleness problem of consultant-produced static PDFs, which the company argues become outdated by year two of a typical three-year refresh cycle [[sources/web-2024-11-01-fc2]].

## Sources

- [[sources/web-2024-11-01-fc2]] — CommunityPay, "Automated Reserve Studies" product page (communitypay.us/features/reserve-studies/, November 1, 2024)

## Related

- [[entities/communitypay]]
- [[concepts/living-document-reserve-study]]
- [[concepts/percent-funded]]
- [[concepts/30-year-cash-flow-projection]]
