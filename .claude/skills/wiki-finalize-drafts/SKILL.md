---
name: wiki-finalize-drafts
description: Review stale draft wiki pages and finalize them — fix missing citations, run validator, commit
triggers: [wiki-finalize-drafts, wiki finalize-drafts]
---

## What This Does

Surfaces stale draft pages, identifies what's blocking finalization (missing
citations, failing validator), fixes the blockers, and runs `wiki finalize`.

Reference conventions: WIKI.md § 8 (draft lifecycle), § 12.2 lint check `stale-drafts`.

## Usage

```
/wiki-finalize-drafts                  # Review all stale drafts
/wiki-finalize-drafts wiki/synthesis/foo.md   # Target one page
```

## Execution Steps

1. **Find drafts**: Run `wiki lint --scope stale-drafts` to list pages with
   `draft: true` older than 7 days.

2. **Prioritize**: For each draft, classify:
   - **Cat A** — has `## Sources cited` section with `[[sources/...]]` links → ready to finalize
   - **Cat B** — has claims but no citations → needs cite-suggest
   - **Cat C** — stub content → flag for user decision (finalize or abandon)

3. **Cat A — finalize directly**:
   ```
   .venv/bin/wiki finalize wiki/<type>/<slug>.md
   ```

4. **Cat B — add citations first**:
   Run `/wiki-cite wiki/<type>/<slug>.md` (or use `wiki cite-add`) to surface
   citation candidates. Then finalize.

5. **Cat C — present to user**: Show the slug and ask: finalize as-is, abandon, or skip?
   To abandon: `.venv/bin/wiki finalize wiki/<type>/<slug>.md --abandon`

6. **Report**: State how many pages were finalized, abandoned, skipped.

## Key constraints

- Never modify page body via direct Edit for citation purposes — use `wiki cite` or `wiki cite-add`.
- `wiki finalize` will fail if citation grounding is not met; fix citations, don't force.
- `draft: true` in frontmatter is the only authoritative source of draft status.
