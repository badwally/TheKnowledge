---
type: concept
slug: auto-commit-pattern
canonical_name: Auto-Commit Pattern
domains:
- knowledge-management
draft: true
draft_started_at: '2026-05-05T00:22:50Z'
draft_unresolved_claims: 0
---

# Auto-Commit Pattern

## Summary

The auto-commit pattern is a discipline in which every state-modifying tool operation is automatically committed to git with a classifying prefix in the commit message, eliminating the need for manual `git` invocation and producing a fully auditable history of LLM- and human-driven changes [[sources/web-2026-04-11-879]].

## Key claims

- Every WikiLoom command that modifies state auto-commits with a classifying prefix such as `ingest:`, `lint:`, `merge:`, etc., so the user never has to type `git` [[sources/web-2026-04-11-879]].
- Defined prefixes include `init:`, `ingest:`, `lint:`, `relink:`, `review:`, `related:`, `merge:`, `deprecate:`, `dormant:`, and `human-edit:` [[sources/web-2026-04-11-879]].
- The `human-edit:` prefix is created when the user runs `wikiloom save` after editing pages, `wikiloom.toml`, or prompts by hand [[sources/web-2026-04-11-879]].
- Writer commands block on uncommitted edits under `wiki/`, telling the user to run `wikiloom save` first so manual edits never land inside an `ingest:` commit [[sources/web-2026-04-11-879]].
- Dirty `wikiloom.toml` or prompt edits produce a passive nudge but do not block, since they cannot collide with an auto-commit's output [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/human-edit-protection]]
