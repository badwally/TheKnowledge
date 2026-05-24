---
type: concept
slug: cmms-asset-work-order-data-model
canonical_name: CMMS Asset and Work Order Data Model
domains:
  - condo-software
  - condo-capital-infra
---

# CMMS Asset and Work Order Data Model

## Summary

The CMMS asset and work-order data model is a recurring schema pattern in maintenance-management systems organized around Asset, AssetCategory, Site/Location, WorkOrder, and WorkOrderStatus as first-class objects, with integer foreign keys linking related records and a display-value convention (prefix-coded fields like `dv_intAssetLocationID`) for resolving foreign keys into human-readable strings inside a single response payload. The Fiix CMMS API documents this pattern explicitly across its CRUD examples [[sources/web-2025-01-01-880]].

## Key claims

- The Fiix CMMS API exposes Asset, AssetCategory, and WorkOrder as first-class objects with integer foreign keys linking them: an Asset references its category via `intCategoryID` and its location via `intAssetLocationID`; a WorkOrder requires `intSiteID` and `intWorkOrderStatusId` [[sources/web-2025-01-01-880]].
- Asset fields documented in the Fiix create/read examples include `id`, `strName`, `strDescription`, `strSerialNumber`, `strInventoryCode`, `qtyStockCount`, `strModel`, `strMake`, `strBarcode`, `strCity`, `strProvince`, `strNotes`, and `intSiteID`, with a naming convention of type-prefixed columns (`str` for strings, `int` for integer foreign keys, `qty` for quantities) [[sources/web-2025-01-01-880]].
- Site is a required parent for both Assets (`intSiteID`) and Work Orders (`intSiteID`), making Site the top-level location anchor in the Fiix object hierarchy [[sources/web-2025-01-01-880]].
- The `dv_` ("display value") prefix convention surfaces a human-readable display string for a foreign-keyed object alongside the integer ID without requiring a separate `findById` call; display values are returned in the response's `extraFields` property rather than in the top-level object [[sources/web-2025-01-01-880]].
- Filters on `find` queries use a SQL-like fragment language (`{"ql": "intAssetLocationID = ?", "parameters": [<value>]}`) that parameterizes integer foreign-key lookups [[sources/web-2025-01-01-880]].
- Partial updates via `change` are field-scoped: only fields listed in the `changeFields` parameter are mutated, even if the `object` payload carries additional values; the returned-field set is controlled independently via the `fields` parameter [[sources/web-2025-01-01-880]].
- WorkOrder requires both site (`intSiteID`) and work-order status (`intWorkOrderStatusId`) at creation time, meaning every Fiix work order is anchored to a physical site and a discrete lifecycle state before it can be persisted [[sources/web-2025-01-01-880]].

## Sources

- [[sources/web-2025-01-01-880]] — Fiix CMMS API Developer's Guide (fiixlabs.github.io/api-documentation/guide.html, January 1, 2025)

## Related

- [[entities/fiix-cmms]]
- [[concepts/cmms-api-crud-rpc-dual-pattern]]
- [[concepts/cmms-api-batch-request-transactional]]
