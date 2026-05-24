---
type: concept
slug: maintainx-work-order-schema
canonical_name: MaintainX Work Order Schema (Form Fields)
domains:
  - condo-software
---

# MaintainX Work Order Schema (Form Fields)

## Summary

The MaintainX work order schema is the named-field taxonomy that defines the data model for a single work order in the MaintainX CMMS platform [[sources/web-2026-01-01-ec1]]. The schema enumerates 19 named fields, of which only the title field ("What needs to be done?") is mandatory; all other fields are optional at creation and editable later [[sources/web-2026-01-01-ec1]]. The schema is available across MaintainX's Web and Mobile platforms, all four plan tiers (Basic, Essential, Premium, Enterprise), and all three user types (Requester, Full User, Administrator) [[sources/web-2026-01-01-ec1]].

## Key claims

### Mandatory and length-limited fields

- The title field ("What needs to be done?") is the only mandatory field on a new work order [[sources/web-2026-01-01-ec1]].
- The title can be up to 255 characters long [[sources/web-2026-01-01-ec1]].
- The Description field accepts up to 4,096 characters of detailed work description [[sources/web-2026-01-01-ec1]].

### Asset and Location coupling rule

- A work order can only have one assigned Location, chosen from any of the organization's configured locations [[sources/web-2026-01-01-ec1]].
- The Location chosen should be the location associated with the Asset specified in the Asset field [[sources/web-2026-01-01-ec1]].
- If the Asset is associated with a Location different from the one initially chosen, MaintainX automatically sets the Location field to the Asset's location — meaning Asset is the authoritative source for Location when the two disagree [[sources/web-2026-01-01-ec1]].
- The Asset field accepts any asset configured for the organization and is the anchor for asset-specific maintenance work [[sources/web-2026-01-01-ec1]].
- The Asset Status field allows the asset's status to be updated when the work order is created (e.g., set Offline immediately for unplanned maintenance) [[sources/web-2026-01-01-ec1]].

### Sub-work orders (parent/child structure)

- Adding sub-work orders converts the work order to a parent work order, which displays only a subset of fields [[sources/web-2026-01-01-ec1]].
- When sub-work orders are added, the Asset field disappears from the parent work order — assets must be specified at the sub-work-order level instead [[sources/web-2026-01-01-ec1]].
- Procedures on a parent work order with sub-work orders must be added through the Sub-Work Orders table at the sub-work-order level [[sources/web-2026-01-01-ec1]].
- Asset Status updates on a parent with sub-work orders can only occur after the sub-work orders are created [[sources/web-2026-01-01-ec1]].

### Scheduling fields and defaults

- Due Date is the date the work is due to be completed [[sources/web-2026-01-01-ec1]].
- Due Time defaults to 12:00 PM on the Due Date if not explicitly set [[sources/web-2026-01-01-ec1]].
- Start Date is the date the work is scheduled to start [[sources/web-2026-01-01-ec1]].
- Start Time defaults to 12:00 AM on the Start Date if not explicitly set [[sources/web-2026-01-01-ec1]].
- Recurrence sets the repeat frequency (weekly, monthly, etc.) or the value "Does not recur" for one-off (non-recurring) work orders [[sources/web-2026-01-01-ec1]].
- Estimated Time captures the approximate work duration in hours and minutes [[sources/web-2026-01-01-ec1]].

### Work Type taxonomy

- Work Type is the field that classifies the kind of maintenance the work order represents [[sources/web-2026-01-01-ec1]].
- Preventive work orders are recurring [[sources/web-2026-01-01-ec1]].
- Reactive work orders are non-recurring [[sources/web-2026-01-01-ec1]].
- Work orders generated from maintenance plans are non-recurring but have their Work Type set to Preventive to indicate they are part of a preventive maintenance plan — an explicit exception to the "Preventive ⇒ recurring" rule [[sources/web-2026-01-01-ec1]].

### Assignment and resource fields

- Assign To accepts one or more users or teams [[sources/web-2026-01-01-ec1]].
- Priority is a settable field on every work order (the source does not enumerate the available priority values) [[sources/web-2026-01-01-ec1]].
- Parts accepts any part configured for the organization, allowing parts consumption to be tracked against the work order [[sources/web-2026-01-01-ec1]].
- Vendors accepts one or more vendors from the organization's configured vendor list [[sources/web-2026-01-01-ec1]].
- Categories accepts one or more categories per work order, drawn from built-in categories (e.g., Safety, Standard Operating Procedure) and custom categories configured by the organization [[sources/web-2026-01-01-ec1]].
- Procedure adds checklist-style procedures to the work order, with preview and edit capability [[sources/web-2026-01-01-ec1]].

### Attachment fields

- "Add or drag pictures" attaches images to the work order, with thumbnails displayed inline [[sources/web-2026-01-01-ec1]].
- Files attaches arbitrary files of supported formats to the work order [[sources/web-2026-01-01-ec1]].

### Platform, plan, and user-type availability

- The work order schema is available on both Web and Mobile platforms [[sources/web-2026-01-01-ec1]].
- The schema is available across all four MaintainX plan tiers: Basic, Essential, Premium, and Enterprise [[sources/web-2026-01-01-ec1]].
- The schema is available to all three user types: Requester, Full User, and Administrator [[sources/web-2026-01-01-ec1]].

## Sources

- [[sources/web-2026-01-01-ec1]] — MaintainX Help Center, "Work Order Form Fields" (help.getmaintainx.com)

## Related

- [[entities/maintainx]]
- [[entities/bessemer-venture-partners]]
- [[entities/byron-deeter]]
