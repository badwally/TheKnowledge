---
schema_version: 1
type: concept
slug: cmms-api-crud-rpc-dual-pattern
canonical_name: CMMS API Dual CRUD/RPC Surface
domains:
- condo-software
created_at: '2026-05-24T02:57:32Z'
last_updated: '2026-05-24T02:57:32Z'
---

# CMMS API Dual CRUD/RPC Surface

## Summary

The dual CRUD/RPC surface is a CMMS API design pattern in which the same client exposes both standard CRUD operations against first-class objects (assets, work orders, asset categories) and remote procedure calls for cross-cutting or computation-style operations (connectivity tests, period summaries). The Fiix CMMS API documents this pattern explicitly, exposing CRUD via `find`, `findById`, `add`, `change`, and remove methods, and RPC via a single `rpc({"name": "<ProcedureName>", ...})` entrypoint [[sources/web-2025-01-01-880]].

## Key claims

- CMMS APIs that target operational integration expose two parallel call categories: CRUD operations on first-class domain objects, and RPC calls for cross-cutting operations that don't map cleanly onto a single object's lifecycle [[sources/web-2025-01-01-880]].
- In the Fiix CMMS API, CRUD operations are named `find`, `findById`, `add`, `change`, and remove [[sources/web-2025-01-01-880]].
- In the Fiix CMMS API, RPC calls are invoked through a single client method (`fiixCmmsClient.rpc(...)`) parameterized by a `name` field naming the procedure [[sources/web-2025-01-01-880]].
- The Fiix RPC surface includes `Ping` (connectivity test) and `getDaysOfMonth` (returns a summary of upcoming events for the specified user) as documented examples; the full RPC catalog is published in the API Reference [[sources/web-2025-01-01-880]].
- The CRUD/RPC split lets integrators model write-side operations (asset creation, work-order updates) as object mutations while routing query-style or computation operations through RPC without forcing them into a CRUD frame [[sources/web-2025-01-01-880]].
- Both surfaces share the same response envelope conventions: a top-level `object` for single results, `objects` for multi-result returns, and an `error` field carrying server-side error code and explanation [[sources/web-2025-01-01-880]].

## Sources

- [[sources/web-2025-01-01-880]] — Fiix CMMS API Developer's Guide (fiixlabs.github.io/api-documentation/guide.html, January 1, 2025)

## Related

- [[entities/fiix-cmms]]
- [[concepts/cmms-api-batch-request-transactional]]
- [[concepts/cmms-asset-work-order-data-model]]
