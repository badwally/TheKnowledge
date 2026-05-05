---
type: concept
slug: page-lifecycle
canonical_name: Page Lifecycle
domains:
- knowledge-management
draft: true
draft_started_at: '2026-05-05T00:22:49Z'
draft_unresolved_claims: 0
---

# Page Lifecycle

## Summary

WikiLoom assigns each page one of three lifecycle statuses — `active`, `dormant`, or `deprecated` — with optional permanent removal via purge, allowing stale or superseded pages to be retired without breaking inbound references [[sources/web-2026-04-11-879]].

## Key claims

- The lifecycle progression is `active → dormant (optional) → deprecated → purged (gone)` [[sources/web-2026-04-11-879]].
- `active` pages are current and surfaced everywhere [[sources/web-2026-04-11-879]].
- `dormant` pages are older than their time window but still visible and usable; the marking is informational ("you might want to refresh this") rather than a verdict on usefulness [[sources/web-2026-04-11-879]].
- Dormant marking is a user action via `wikiloom dormant <page>` [[sources/web-2026-04-11-879]].
- `deprecated` pages move to `wiki/archive/`, are hidden from most workflows, and are reached via `wikiloom merge` or `wikiloom deprecate` [[sources/web-2026-04-11-879]].
- Permanent removal via `wikiloom purge` requires prior deprecation and typed confirmation by default [[sources/web-2026-04-11-879]].
- `wikiloom deprecate <page> --superseded-by <other>` rewrites every inbound `[[X]]` wikilink across non-archived pages to the replacement [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
