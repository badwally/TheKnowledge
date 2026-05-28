# Session Review — 2026-05-27

## § 1 — Code and Coding Quality

**High — `_orphan_sources_for_domain` limit is not enforced across source types**
`src/gateway/ops/discharge_orphans.py:24–47`

The `break` on `len(results) >= limit` exits only the inner `for p in sorted(...)` loop. The outer `for source_type in paths.SOURCE_TYPES` loop continues, potentially accumulating up to `limit × len(SOURCE_TYPES)` results (5× with the current five types). A vault with 30 orphan `web` sources and 30 orphan `arxiv` sources, run with `--limit 10`, would issue 20 NLM `query()` calls instead of 10. This is the same bug present in `daily_review._collect_orphan_sources` (line 133), which the new code was modeled on.

Fix: add `if len(results) >= limit: break` as a guard at the outer loop level, or use an early return.

**Medium — `wiki_pages` imported but unused in `fix_wikilinks.py`**
`src/gateway/ops/fix_wikilinks.py:16`

`wiki_pages` is imported but never referenced. `walk_wiki_pages` comes from `gateway.lint._walk`, not from this import.

Fix: remove `wiki_pages` from the import line.

**Medium — `_parse_iso` is duplicated across at least five files**
`abandon_stale_drafts.py:27`, `stale_drafts.py:19`, `daily_review.py:78`, `wiki_digest.py:28`, `stale_verified.py:25`

Every ops or lint file that parses an ISO timestamp defines its own private `_parse_iso`. M98 added a fifth instance rather than extracting to `gateway.core`.

Fix: add `parse_iso(value: str) -> datetime | None` to `gateway.core` and import from there.

**Medium — `_build_inbound_index` does not exclude self-citations**
`src/gateway/ops/abandon_stale_drafts.py:47–57`

The canonical orphan check at `lint/orphans.py:56` explicitly skips self-references (`if target == identity: continue`). The `abandon_stale_drafts` inbound index does not. A draft page containing `[[concepts/my-draft]]` in its own body would be incorrectly spared. No test covers it.

Fix: skip entries where the referencing page's own target matches the wikilink target; add a self-citation test case.

**Medium — `discharge_orphans` does not write a log entry**
`src/gateway/ops/discharge_orphans.py`

All other batch ops in the session call `log.append(...)` after a successful run. `discharge_orphans` does not — no audit trail of domain processed, sources discharged, or timestamp.

Fix: import `log` and call `log.append(op="discharge-orphans", fields={...})` in the non-dry-run success path.

**Low — `_write_draft` helper computes `_NOW` at module load time**
`tests/gateway/test_abandon_stale_drafts.py:20`

`_NOW = datetime.now(timezone.utc)` at module level creates a flakiness vector if the module loads near midnight UTC.

Fix: pass `now` as a parameter to the op or use `freezegun` for deterministic time.

---

## § 2 — Token Efficiency

**Redundant read of `cli.py` line-offset probes**

Three sequential targeted reads of `cli.py` to locate insertion points (~135 lines total) where a single `grep -n` for anchor strings would have given all three line numbers in one shot, reducing to 1 grep + 1 targeted read.

**Sequential CLI + mcp_server reads that could have been parallel**

For M98 and M99, `cli.py` offset reads and `mcp_server.py` grep went out sequentially rather than in parallel — one unnecessary round-trip per milestone.

**Over-wide `git diff --stat` call**

`git diff dde7e74..HEAD --stat` returned 131.5 KB (truncated), most of it wiki content file changes from the live `fix-wikilinks` run. A targeted `git diff -- src/gateway/ops/` would have produced the same signal at ~10% of the token cost.

**Test assertion fix required a write-run-fix cycle for M99**

`test_skips_covered_sources` assertion was wrong at first write. The mismatch was predictable from a quick control-flow trace: a covered source means zero orphans → early-return path, not zero-filed path. No tool calls needed.

**`daily_review.py` read produced no reuse**

Read to understand the orphan-source pattern, then the same pattern was replicated rather than imported. Token cost paid, no reuse realized.

---

## § 3 — Prompt and Context Engineering

**`_synthesis_question` produces a content-free prompt**

`f"What does '{title}' contribute to this domain's understanding?"` gives the NLM corpus no signal about what the source actually says. A title-only question will produce generic responses that don't engage with the source's specific contribution — defeating the purpose of orphan discharge.

Improvement: incorporate source `domains` and abstract excerpt into the question. E.g.: `f"Summarize what '{title}' ({', '.join(domains)}) contributes on the topic of {domain}."`

**No context seeding before implementing `abandon_stale_drafts`' inbound index**

The inbound citation check used a hand-rolled regex (`_WIKILINK_TARGET_RE`) rather than the existing `citations.find_wikilinks()` that `fix_wikilinks.py` used for the same purpose one milestone earlier. Two different wikilink-parsing paths now exist in the codebase.

Improvement: grep for existing wikilink-parsing utilities as a precondition check before writing new parsers.

**`OperationResult` import path learned via test failure**

In M94 (pre-compaction), `OperationResult` was initially imported from `gateway.ops.gateway_op` instead of `gateway.core`, discovered only at test run time. A precondition grep for `class OperationResult` before the first import would have seeded the correct path.

**CLI usage string updated as a third separate edit**

`_run_routine_cmd`'s usage string was updated after parser and handler were already written. Treating the usage string as part of the parser block edit would have caught it in one pass.

---

## Priority Table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | Code quality | `_orphan_sources_for_domain` limit overshoots across source types — could issue 5× requested NLM calls | Add outer-loop limit guard in `discharge_orphans.py:24` |
| 2 | Code quality | `_synthesis_question` produces content-free prompt → generic NLM responses | Incorporate source domains + abstract excerpt before routine runs against live corpus |
| 3 | Code quality | `wiki_pages` unused import in `fix_wikilinks.py`; `_parse_iso` duplicated across 5 files | Remove unused import; extract `parse_iso` to `gateway.core` |
| 4 | Token efficiency | `_build_inbound_index` re-implements `citations.find_wikilinks` via raw regex | Pre-check for existing utilities; consider refactoring to `citations.find_wikilinks` |
| 5 | Prompt engineering | `_build_inbound_index` doesn't exclude self-citations, diverging from `lint/orphans.py` model | Add self-citation exclusion + test case |
