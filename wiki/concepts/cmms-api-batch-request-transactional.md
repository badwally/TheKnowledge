---
schema_version: 1
type: concept
slug: cmms-api-batch-request-transactional
canonical_name: CMMS API Transactional Batch Requests
domains:
- condo-software
created_at: '2026-05-24T02:57:32Z'
last_updated: '2026-05-24T02:57:32Z'
---

# CMMS API Transactional Batch Requests

## Summary

Transactional batch requests are a CMMS API design pattern in which multiple individual API operations (CRUD or RPC) are bundled into a single network request and executed together with all-or-nothing semantics. The Fiix CMMS API documents this pattern as a first-class capability with three named advantages: bandwidth reduction, transactionality (rollback on any single-request failure), and asynchronous callback-based completion handling [[sources/web-2025-01-01-880]].

## Key claims

- The Fiix CMMS API supports executing several requests as a single batch request through a `fiixCmmsClient.batch({"requests": [...], "callback": fn})` entrypoint [[sources/web-2025-01-01-880]].
- Individual requests are pre-built using `prepare*` methods (e.g., `prepareFindById`, `prepareAdd`) and then passed to the batch executor as an array [[sources/web-2025-01-01-880]].
- The Fiix documentation enumerates three advantages of batch requests: (i) less bandwidth is used; (ii) batch requests are transactional — if one request inside the batch fails, everything is rolled back; (iii) the call can be asynchronous with a callback fired once the whole batch has been executed [[sources/web-2025-01-01-880]].
- Batch responses are aggregated into a `responses` array on the callback's return object, in the same order as the input request array, with each element preserving the per-request response shape (e.g., `ret.responses[0].object`) [[sources/web-2025-01-01-880]].
- Errors from the server side are communicated via the `error` field of the response object; in batch contexts, errors are batched together just as the requests are batched together [[sources/web-2025-01-01-880]].
- Batching replaces a synchronous chain of three `findById` calls (asset → location → category) with a single network round-trip while preserving the same result shape [[sources/web-2025-01-01-880]].
- The pattern is offered both for read aggregation (multiple `prepareFindById` calls executed together) and for write aggregation (multiple `prepareAdd` calls creating several assets transactionally in one round-trip) [[sources/web-2025-01-01-880]].

## Sources

- [[sources/web-2025-01-01-880]] — Fiix CMMS API Developer's Guide (fiixlabs.github.io/api-documentation/guide.html, January 1, 2025)

## Related

- [[entities/fiix-cmms]]
- [[concepts/cmms-api-crud-rpc-dual-pattern]]
- [[concepts/cmms-asset-work-order-data-model]]
