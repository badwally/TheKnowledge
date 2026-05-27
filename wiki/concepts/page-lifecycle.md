---
schema_version: 1
type: concept
slug: page-lifecycle
canonical_name: Page Lifecycle
domains:
- knowledge-management
draft: true
draft_started_at: '2026-05-05T00:22:49Z'
draft_unresolved_claims: 0
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Page Lifecycle

## Summary

WikiLoom assigns each page one of three lifecycle statuses — `active`, `dormant`, or `deprecated` — with optional permanent removal via purge, allowing stale or superseded pages to be retired without breaking inbound references .

## Key claims

- The lifecycle progression is `active → dormant (optional) → deprecated → purged (gone)` .
- `active` pages are current and surfaced everywhere .
- `dormant` pages are older than their time window but still visible and usable; the marking is informational ("you might want to refresh this") rather than a verdict on usefulness .
- Dormant marking is a user action via `wikiloom dormant <page>` .
- `deprecated` pages move to `wiki/archive/`, are hidden from most workflows, and are reached via `wikiloom merge` or `wikiloom deprecate` .
- Permanent removal via `wikiloom purge` requires prior deprecation and typed confirmation by default .
- `wikiloom deprecate <page> --superseded-by <other>` rewrites every inbound `[[X]]` wikilink across non-archived pages to the replacement .

## Sources

- — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
