---
schema_version: 1
type: concept
slug: query-output-controls
canonical_name: Clean-Room Query Output Controls (allowedFields, Pre-Conditions, Post-Filters)
domains:
- data-collectives
created_at: '2026-06-10T22:30:00Z'
last_updated: '2026-06-10T22:30:00Z'
draft: true
draft_started_at: '2026-06-10T22:30:00Z'
draft_unresolved_claims: 0
---

# Clean-Room Query Output Controls (allowedFields, Pre-Conditions, Post-Filters)

## Summary

Clean-room query output controls are the schema-level and statistical-suppression mechanisms a clean room uses to limit what query authors can extract from collaborators' data: a per-dataset column whitelist (`allowedFields`), a minimum-input-row pre-condition that rejects queries operating on too few rows, and a minimum-group-size post-filter that suppresses small aggregated groups in the output [[sources/web-2026-06-03-4ff]]. Together these controls aim to prevent individual-level re-identification through query results without relying on output noise [[sources/web-2026-06-03-4ff]].

## Key claims

- `allowedFields`: each contributed dataset declares a column whitelist; only those columns are exposed to clean-room queries, and every other column in the source storage is excluded from access [[sources/web-2026-06-03-4ff]].
- Pre-conditions: each published query can declare a minimum row count per input view, under which the query is rejected before execution [[sources/web-2026-06-03-4ff]].
- Post-filters: each published query can declare a minimum count under which aggregated groups in the output are dropped, suppressing low-count groups that could re-identify individuals [[sources/web-2026-06-03-4ff]].
- The query composer sets pre-conditions and post-filters, and other collaborators review and approve them before the query executes [[sources/web-2026-06-03-4ff]].

## Sources

- [[sources/web-2026-06-03-4ff]] — Microsoft Learn: Perform Protected Multiparty Data Collaboration on Azure (2026-06-03)

## Related

- [[concepts/data-clean-room]]
- [[concepts/differential-privacy]]
- [[concepts/privacy-utility-tradeoff]]
- [[entities/azure-confidential-clean-rooms]]
