# gateway.lint

The lint package implements the health-check suite described in `WIKI.md § 12`. Each submodule exports a single `run() -> list[LintFinding]` function. The orchestrator in `ops/lint.py` composes them in a fixed order, aggregates findings, and writes a timestamped report to `.knowledge/lint/<UTC-timestamp>.md`. Findings carry a check name, a severity (`info` / `warning` / `error`), a message, an optional file path, and a metadata dict for structured detail. Checks never write to `wiki/` or `raw/`; they are read-only diagnostics.

See `ARCHITECTURE.md` for how lint fits into the operational lifecycle.

## Files

| File | Check slug | What it detects |
|------|-----------|-----------------|
| `__init__.py` | — | `LintFinding` dataclass; severity constants |
| `_walk.py` | — | Shared `walk_wiki_pages()` and `walk_raw_sources()` iterators |
| `orphans.py` | `orphans` | Raw sources with no inbound `[[sources/<id>]]` citation |
| `stale_drafts.py` | `stale-drafts` | Draft pages older than 7 days |
| `stale_claims.py` | `stale-claims` | Claims not re-confirmed since their source was last updated |
| `contradictions.py` | `contradictions` | Source pairs with conflicting claims |
| `missing_pages.py` | `missing-pages` | Wikilinks pointing to non-existent pages |
| `citation_density.py` | `citation-density` | Pages with claim-to-citation ratio below threshold |
| `citation_chains.py` | `citation-chains` | Citation paths that exceed maximum depth |
| `schema_drift.py` | `schema-drift` | Pages with frontmatter not matching current schema |
| `filter_calibration.py` | `filter-calibration` | Domains where filter precision/recall has drifted |
| `inbox_pending.py` | `inbox-pending` | Items in the raw inbox not yet ingested |
| `nlm_pending.py` | `nlm-pending` | Sources tagged for a domain corpus but not yet synced to NotebookLM |
| `untagged_sources.py` | `untagged-sources` | Raw sources with no `domains:` tag |
| `idempotency.py` | `idempotency` | Raw sources whose wiki/sources page is missing or stale |
| `broken_wikilinks.py` | `broken-wikilinks` | `[[wikilinks]]` in wiki pages that resolve to no file |
| `long_slugs.py` | `long-slugs` | Source or page slugs exceeding the recommended length |
| `contradiction_pages.py` | `contradiction-pages` | Contradiction pages missing required resolution fields |

## Worked example: running a targeted lint check

```
Input:  $ wiki lint --scope orphans
Call:   ops.lint.run_lint(scope="orphans")

1. ops/lint.py._CHECKS is filtered to [("orphans", orphans.run)]
2. orphans.run() calls lint._walk.walk_raw_sources()
   → yields (source_type, path, front, body) for every file in raw/
3. For each source, checks whether any wiki page body contains [[sources/<id>]]
4. Sources with no inbound citations → LintFinding(
       check="orphans",
       severity="warning",
       message="no wiki page cites raw/web/my-article.md",
       path="raw/web/my-article.md",
       metadata={"source_id": "web-my-article"}
   )
5. ops/lint.py aggregates findings, writes .knowledge/lint/2026-05-25T09-00-00Z.md
6. Returns OperationResult(success=True, data={"findings": [...], "report_path": "..."})

Running all checks:
   $ wiki lint
   → all 16 check runners execute in _CHECKS order
   → report groups by severity; errors printed first

Failure modes:
- walk_raw_sources() finds malformed frontmatter → that file is skipped;
  schema-drift check reports it separately
- A check raises unexpectedly → ops/lint.py catches, records as a
  LintFinding(severity="error", message="check crashed: ...") and continues
```
