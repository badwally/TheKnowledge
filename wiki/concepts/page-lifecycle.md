---
schema_version: 1
type: concept
slug: page-lifecycle
canonical_name: Page Lifecycle
domains:
- knowledge-systems
created_at: '2026-05-28T20:24:02Z'
last_updated: '2026-05-28T20:24:02Z'
---

# Page Lifecycle

## Summary

Page lifecycle is the explicit state machine — active → dormant (optional) → deprecated → purged — that governs how knowledge-base pages age, retire, and are permanently removed [[sources/web-2026-04-11-879]].

## Key claims

- Every WikiLoom page has one of three statuses: `active` (current, surfaced everywhere), `dormant` (older than its time window but still visible and usable), or `deprecated` (retired and moved to `wiki/archive/`, hidden from most workflows) [[sources/web-2026-04-11-879]].
- The dormant status is informational rather than a verdict on usefulness — it is a "you might want to refresh this" signal and is set by the user via `wikiloom dormant <page>` [[sources/web-2026-04-11-879]].
- Deprecation is reached via `wikiloom merge` or `wikiloom deprecate`; permanent removal is via `wikiloom purge`, which requires the page to already be deprecated [[sources/web-2026-04-11-879]].
- The full lifecycle is `active → dormant (optional) → deprecated → purged (gone)` [[sources/web-2026-04-11-879]].
- `wikiloom merge <loser> <winner>` unions bodies (preserving human regions), rewrites inbound `[[loser]]` wikilinks to `[[winner]]`, and deprecates the loser page [[sources/web-2026-04-11-879]].
- `wikiloom deprecate <page> --superseded-by <other>` rewrites every inbound `[[X]]` wikilink across non-archived pages to the replacement [[sources/web-2026-04-11-879]].
- `wikiloom purge` deletes both the archive file and the manifest entry and requires typed confirmation by default [[sources/web-2026-04-11-879]].
- Dormant time windows are configurable per page type and can be inspected via `wikiloom dormant --windows` [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/human-edit-protection]]
- [[concepts/auto-commit-pattern]]
