---
schema_version: 1
type: concept
slug: human-edit-protection
canonical_name: Human-Edit Protection
domains:
- knowledge-management
draft: true
draft_started_at: '2026-05-05T00:22:49Z'
draft_unresolved_claims: 0
created_at: '2026-05-05T04:01:32Z'
last_updated: '2026-05-05T04:01:32Z'
---

# Human-Edit Protection

## Summary

Human-edit protection is a two-tier mechanism in WikiLoom that distinguishes between LLM-authored regions of a page and human-authored regions, ensuring manual edits are not silently overwritten by subsequent automated operations [[sources/web-2026-04-11-879]].

## Key claims

- A `human-edit:` commit prefix provides soft, short-term protection: `lint --fix` skips human-edited pages and the protection is cleared by the next auto-action (e.g. a re-ingest) [[sources/web-2026-04-11-879]].
- A durable `<!-- wikiloom:auto -->` HTML-comment marker partitions the page into a protected region above and an auto-managed region below [[sources/web-2026-04-11-879]].
- Anything above the marker survives every operation, including `wikiloom ingest <file> --force` (the only command that wipes the auto region) [[sources/web-2026-04-11-879]].
- For normal updates (re-ingesting a different source that updates the page), new content is appended to the auto region rather than replacing it, so edits anywhere on the page survive [[sources/web-2026-04-11-879]].
- Writer commands block on uncommitted edits under `wiki/`, requiring `wikiloom save` first so manual edits never accidentally land inside an `ingest:` commit [[sources/web-2026-04-11-879]].
- Dirty `wikiloom.toml` or prompt edits produce a passive nudge but don't block, since they cannot collide with an auto-commit's output [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/auto-commit-pattern]]
