# M42 — Review Consoles (Design)

**Status:** Brainstormed and locked. Ready for implementation planning.
**Date:** 2026-05-04
**Scope:** Four review consoles: drafts, contradictions, orphans, filter-band. NLM artifact triggers (briefing/audio/slides/revise) deferred to M43.

---

## Goal

Add a Review sidebar entry to `wiki serve` that surfaces pending curation decisions across four tabs. Drafts and filter-band consoles support inline actions (Finalize/Abandon, Include/Exclude). Contradictions and orphans are read-only with click-through to source pages. To make contradictions queryable, M42 also adds structured persistence: `apply_plan` writes contradiction records to an append-only JSONL log on every plan that includes contradictions.

---

## § 1. Architecture

Adds:
- `.knowledge/contradictions/log.jsonl` — append-only structured log written by `gateway.ops.apply_plan` on every plan that has contradictions
- `gateway.web.routes.review` — 4 GET endpoints (drafts/contradictions/orphans/filter-band) returning structured lists
- Single Review sidebar entry → `/review` page with 4 tabs
- Inline actions reuse existing M40 sync endpoints (`/api/ops/finalize`, `/api/ops/filter-correct`)

No new long-running ops, no TaskStore use, no orchestrator changes. Pure read + click-through-to-existing-action.

---

## § 2. Backend endpoints + persistence

### Endpoints

```
GET  /api/review/drafts           → [{path, type, slug, draft_started_at, draft_unresolved_claims, age_days}, ...]
GET  /api/review/contradictions   → [{source_id, existing_page, existing_claim, new_claim, severity, recorded_at}, ...]
GET  /api/review/orphans          → [{source_id, source_type, title, ingested_at}, ...]
GET  /api/review/filter-band      → [{source_id, source_type, title, score, threshold_review, threshold_include, domain}, ...]
```

### `apply_plan` change (M38 contradiction persistence)

When `plan.contradictions` is non-empty, after the validator passes and inside the existing `with file_lock(_LOCK_NAME)` block (Phase 2), append one JSONL record per contradiction to `.knowledge/contradictions/log.jsonl` before the existing `log.append("wiki-author", ...)` call. Each record:

```json
{"source_id": "yt-newSource_AB",
 "existing_page": "wiki/concepts/existing-mechanism.md",
 "existing_claim": "Effect is permanent",
 "new_claim": "Partial reversal observed after 12 weeks",
 "severity": "major",
 "recorded_at": "2026-05-04T22:30:00Z"}
```

The file is created on first write. Atomic line-append: open with `'a'` mode, write `json.dumps(record) + "\n"`, close. POSIX guarantees lines under 4KB are atomic — these records are well under that.

### Drafts data source

Glob `wiki/{entities,concepts,synthesis,mocs}/*.md`, parse frontmatter, filter `draft: true`. Extract `draft_started_at`, `draft_unresolved_claims`, `slug`, `type`. Compute `age_days = now - draft_started_at`. Sort by `age_days` descending (oldest first to flag stale drafts).

### Orphans data source

Walk `raw/<type>/*.md` for sources where `wiki_pages` frontmatter field is empty or missing. Each result includes `source_id`, `source_type`, `title`, `ingested_at`. Sort by `ingested_at` descending.

(Alternative: call `gateway.ops.lint.lint(scope="orphans")` and parse its report. Direct walk is simpler and avoids re-running the lint.)

### Filter-band data source

Walk `raw/<type>/*.md`. For each source, parse frontmatter, extract `filter.score`, `domains`. For each domain, load the policy via `gateway.filter.policy.load_policy(domain)` to get `threshold_review` and `threshold_include`. Include the source if `threshold_review <= score < threshold_include` for any of its domains. Sort by `score` ascending (lowest first — most likely to need correction).

Cache loaded policies within the request to avoid repeated YAML parses.

### Contradictions data source

Read `.knowledge/contradictions/log.jsonl`, one record per line. Parse JSON. Sort by `recorded_at` descending (most recent first). Tolerate malformed lines (skip with a warning log entry).

---

## § 3. Frontend

```
web/src/pages/review/
├── Review.tsx              # tabs container, URL-state for active tab
├── DraftsTab.tsx           # table + per-row Finalize/Abandon
├── ContradictionsTab.tsx   # table; click row expands inline detail
├── OrphansTab.tsx          # table; click row → obsidian:// link
└── FilterBandTab.tsx       # table + per-row Include/Exclude (rationale prompt)
```

### Routing

- `/review` → defaults to drafts tab
- `/review/drafts`, `/review/contradictions`, `/review/orphans`, `/review/filter-band` → direct tab links

### Sidebar

New "Review" group above System group. Single entry "Review" → `/review`. The group label sits at the same hierarchy level as Wiki/Research/Domains/System.

### Tab behavior

Each tab is independent: fetches data on mount and on a Refresh button click. Inline actions (Finalize/Abandon, Include/Exclude) post to the existing sync endpoints and refresh the tab on success. Errors render in an inline error panel above the table.

### DraftsTab

Table columns: Path · Type · Age · Unresolved claims · Actions

Actions per row:
- **Finalize** button — calls `api.finalize(path, false)`. On success, removes row from list (or refreshes).
- **Abandon** button (with confirm prompt: "Delete this draft permanently?") — calls `api.finalize(path, true)`. On success, removes row.

Stale drafts (`age_days > 7`) get an amber row tint.

### ContradictionsTab

Table columns: Recorded · Source · Affected page · Severity · Existing claim (truncated) · New claim (truncated)

Clicking a row toggles an accordion-style expanded section directly beneath that row, showing both claim texts in full plus the source_id and existing_page paths as monospace text. Only one row expanded at a time. No actions in M42 — contradictions are informational; the user resolves by editing the affected page in their editor.

Severity gets a colored badge: minor (gray), moderate (amber), major (red).

### OrphansTab

Table columns: Source ID · Type · Title · Ingested · Actions

Actions per row: a single "Discharge via query" button. Clicking it navigates to `/ops/query?source_id=<id>&domain=<first-domain>` (the M40 Query page is extended in M42 to read these search params and prefill the form). M42 keeps the orphan→query handoff simple: the user lands on the Query page with the source's primary domain prefilled and an empty question textarea, types a question that draws on the source, and submits. No in-page query execution from the orphans tab.

This requires a small extension to `web/src/pages/Query.tsx` (M40): read `useSearchParams()` on mount and prefill `domain` (and optionally `question` from a `?question=` param, though M42 only uses `?domain=`).

### FilterBandTab

Table columns: Source ID · Type · Title · Score · Domain · Actions

Actions per row:
- **Include** button — opens a modal with rationale textarea, calls `api.filterCorrect(source_id, "include", rationale)`.
- **Exclude** button — same modal, decision="exclude".

Sort by score ascending (lowest scores first — most ambiguous, most worth deciding).

---

## § 4. Out of scope

- Bulk actions (select multiple drafts, finalize all). M43 candidate.
- Filtering/searching within a tab (search by source_id, filter by domain). YAGNI for M42.
- Pagination. 173 drafts and ~60 sources fit fine in a single scroll view.
- Editing wiki pages from the consoles. Doctrine: filesystem-as-database, edit in your editor.
- Aggregating contradictions by affected page (e.g., "page X has 5 unresolved contradictions"). M43 candidate.
- Backfill of pre-M42 contradictions from `log.md`. The JSONL log starts empty and accumulates from M42 onward; old contradictions are visible only in `log.md` summaries.

---

## § 5. Risks & tradeoffs

1. **Contradictions JSONL accumulates without rotation.** At current rates, ~1 contradiction per `wiki ingest --with-plan`. ~100s/year. Negligible. Add `wiki contradictions-prune` only if it grows to MB-scale.

2. **Orphans count is currently 215+** per M25 memory. The console will be busy. Still useful — it tells you which sources to discharge via `wiki query`. Sort makes recent ingests rise to the top.

3. **Filter-band may be empty for most domains** if filters are well-calibrated. An empty list is still informative.

4. **Drafts tab and 173 entries.** A single scrollable table works but feels heavy. Mitigation: stale (>7 days) drafts get visual prominence (amber tint) so the eye gravitates to them. If 173 still feels heavy in practice, M42.1 adds a "show only stale" filter.

5. **JSONL line atomicity.** POSIX guarantees writes < `PIPE_BUF` (typically 4KB) appended via `O_APPEND` are atomic. Each contradiction record is well under 4KB. We don't need a lock around the JSONL append. The `apply_plan` lock is for `wiki/` writes; the JSONL is internal state.

6. **Filter-band requires loading policies per source domain.** Worst case: 6 domains × N sources, each policy load reads 1 YAML. Cache policies per request — load once on first encounter. ~6 YAML reads per request, negligible.

---

## § 6. Acceptance criteria

M42 is shipped when:

1. `apply_plan` writes one JSONL record per contradiction to `.knowledge/contradictions/log.jsonl` when `plan.contradictions` is non-empty. Existing `apply_plan` tests pass; one new test verifies the JSONL append.
2. Four GET endpoints (`/api/review/drafts`, `/api/review/contradictions`, `/api/review/orphans`, `/api/review/filter-band`) return structured lists. Each has a TestClient test asserting shape and basic filter logic.
3. Review sidebar entry navigates to `/review`; tabs work; URL routing for direct tab links works.
4. DraftsTab Finalize/Abandon buttons round-trip to `/api/ops/finalize`. Stale drafts (>7d) get amber tint.
5. ContradictionsTab renders the JSONL log; click expands claim text; severity badge colored.
6. OrphansTab lists orphans; "Discharge via wiki query" routes to `/ops/query` with prefill.
7. FilterBandTab Include/Exclude (with rationale) round-trip to `/api/ops/filter-correct`.
8. BUILD.md has an M42 delivery record.
9. CLAUDE.md / TUTORIAL.md mention `/review` in the operation table.
10. Hand-test: open `wiki serve`, browse all 4 tabs, verify counts match independent inspection (`wiki lint` orphans count, manual draft count).
