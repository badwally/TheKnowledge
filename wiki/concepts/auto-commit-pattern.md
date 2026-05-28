---
schema_version: 1
type: concept
slug: auto-commit-pattern
canonical_name: Auto-Commit Pattern
domains:
- knowledge-systems
created_at: '2026-05-28T20:24:04Z'
last_updated: '2026-05-28T20:24:04Z'
---

# Auto-Commit Pattern

## Summary

The auto-commit pattern makes every state-modifying command automatically produce a git commit with a classifying prefix, removing the user's need to invoke git directly and creating an audit trail that distinguishes machine and human edits [[sources/web-2026-04-11-879]].

## Key claims

- Every WikiLoom command that modifies wiki content auto-commits with a classifying prefix (e.g. `init:`, `ingest:`, `lint:`, `relink:`, `review:`, `related:`, `merge:`, `deprecate:`, `dormant:`, `human-edit:`) so the user never has to type `git` [[sources/web-2026-04-11-879]].
- The `human-edit:` prefix is created when the user runs `wikiloom save` after editing pages, `wikiloom.toml`, or prompts by hand [[sources/web-2026-04-11-879]].
- Writer commands block if there are uncommitted edits under `wiki/`, telling the user to run `wikiloom save` first so manual page edits never accidentally land inside an `ingest:` commit [[sources/web-2026-04-11-879]].
- Dirty `wikiloom.toml` or prompt edits produce a passive nudge but don't block, since they can't collide with an auto-commit's output [[sources/web-2026-04-11-879]].
- `wikiloom edits [-n N]` lists recent human edits committed via `wikiloom save` (date, author, subject, hash), complementing `wikiloom log` for multi-user audit [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/human-edit-protection]]
- [[concepts/page-lifecycle]]
