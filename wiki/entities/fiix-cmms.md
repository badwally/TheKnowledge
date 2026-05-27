---
schema_version: 1
type: entity
slug: fiix-cmms
canonical_name: Fiix CMMS
entity_kind: product
domains:
- condo-software
created_at: '2026-05-24T02:57:32Z'
last_updated: '2026-05-24T02:57:32Z'
---

# Fiix CMMS

## Summary

Fiix CMMS is a cloud-hosted Computerized Maintenance Management System with an instance-specific developer API designed to let third-party tools leverage data from a customer's Fiix CMMS instance [[sources/web-2025-01-01-880]]. The API exposes both CRUD operations against first-class objects (assets, work orders, asset categories, sites, work-order statuses) and remote procedure calls, and is consumable either through Fiix-published Java and JavaScript SDKs or directly without an SDK [[sources/web-2025-01-01-880]]. Customer-facing API endpoints follow the pattern `https://<subdomain>.macmms.com/api` for production with a separate sandbox tenant URL for development, indicating an underlying multi-tenant SaaS topology with per-customer subdomains [[sources/web-2025-01-01-880]].

## Key facts

### API authentication and key management

- API access requires three credentials issued via the customer's CMMS Settings > Connect Management > MA Connect API Application Settings page: Application Key, Access Key, and Secret Key [[sources/web-2025-01-01-880]].
- The Secret Key is non-retrievable after initial issuance and must be stored securely by the integrator on first display [[sources/web-2025-01-01-880]].
- API keys are bound to a backing user account; all access via that key inherits whatever the backing account can see or has permission to do [[sources/web-2025-01-01-880]].
- Fiix recommends reassigning the API user from "administrators" to a less-privileged user group (e.g., "technicians") to scope the integration's blast radius [[sources/web-2025-01-01-880]].
- Separate developer Sandbox and production CMMS instances are provided; API Application registration happens in whichever instance the keys are intended for [[sources/web-2025-01-01-880]].

### SDK and client surface

- Official SDKs ship for Java (`com.ma.cmms.api.client.FiixCmmsClient`) and JavaScript [[sources/web-2025-01-01-880]].
- The Java SDK exposes configurable connection timeout and socket timeout via the `ConnectionParams` interface [[sources/web-2025-01-01-880]].
- The Java SDK exposes proxy server configuration (host, port, Basic or NTLM auth scheme, user, password, srcHost, domain) via the `ProxyCredentials` interface [[sources/web-2025-01-01-880]].
- The JavaScript SDK exposes socket timeout via `fiixCmmsClient.setTimeoutMs(milliseconds)` [[sources/web-2025-01-01-880]].
- The API is also consumable directly without using an SDK [[sources/web-2025-01-01-880]].

### Object and operation model

- Core first-class objects documented in the developer guide include Asset, AssetCategory, and WorkOrder, with site (`intSiteID`) and work-order status (`intWorkOrderStatusId`) treated as required foreign keys on related operations [[sources/web-2025-01-01-880]].
- CRUD operations are exposed as `find`, `findById`, `add`, `change`, and remove [[sources/web-2025-01-01-880]].
- The `find` operation supports field selection via a `fields` parameter and SQL-like filters via `filters` with parameterized queries (e.g., `"ql": "intAssetLocationID = ?", "parameters": [408608]`) [[sources/web-2025-01-01-880]].
- The `change` operation requires the object's `id` and only the fields listed in `changeFields` are updated; the `fields` parameter independently controls which fields are returned [[sources/web-2025-01-01-880]].
- Display-value extra fields prefixed with `dv_` (e.g., `dv_intAssetLocationID`, `dv_intCategoryID`) return human-readable display strings for related objects without requiring a separate `findById` call; values are surfaced in the response's `extraFields` property [[sources/web-2025-01-01-880]].
- RPC calls are surfaced alongside CRUD via `fiixCmmsClient.rpc({"name": "<ProcedureName>", ...})`; documented examples include `Ping` and `getDaysOfMonth` [[sources/web-2025-01-01-880]].

### Tenancy and endpoint topology

- Production API endpoints follow the pattern `https://<subdomain>.macmms.com/api`, with each customer assigned a tenant-specific subdomain [[sources/web-2025-01-01-880]].
- A separate sandbox tenant URL is provided for developer testing [[sources/web-2025-01-01-880]].
- Error responses are communicated via an `error` field on the response object, carrying both an error code (for programmatic dispatch) and a brief explanation of the cause [[sources/web-2025-01-01-880]].

## Sources

- [[sources/web-2025-01-01-880]] — Fiix CMMS API Developer's Guide (fiixlabs.github.io/api-documentation/guide.html, January 1, 2025)

## Related

- [[concepts/cmms-api-crud-rpc-dual-pattern]]
- [[concepts/cmms-api-batch-request-transactional]]
- [[concepts/cmms-asset-work-order-data-model]]
- [[concepts/cmms-api-key-authentication]]
