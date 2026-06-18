# Session review — 2026-06-17 (#3: test isolation + resolver refactor)

Scope: work after review `-2` (which covered PR #17, the promote URL-drop fix) —
**PR #18** (`c61bf3bb`, add `kb_root` to 5 promote tests), **PR #19** (`4bcf938f`, public
batch `resolve_raw_sources_by_title` + 5 resolver tests), and the merge/git operations.
All three review-driven follow-ups are now on `origin/main`. Pure code/git session — no
LLM calls.

Point of view: the code work is clean and the review→practice loop visibly closed (the
`-2` finding about `git status -uno` was adopted this session). The one finding worth
internalizing is behavioral, not in the diff: **loaded context was not applied to the
action twice** — the parallel-tree warning was in session-state (I wrote it) yet I still
chained `git checkout main` into that tree. Same shape as `-2`'s "kb_root loaded but not
propagated." That load-vs-apply gap is the highest-value lesson here.

---

## § 1 — Code and coding quality

**[Medium] Two near-identical `raw/` walk loops now live in `source_map.py`.**
`source_map.py` — `_index_raw_pages` (~line 110) and `resolve_raw_sources_by_title`
(~line 205) both iterate `paths.SOURCE_TYPES`, `type_dir.glob("*.md")`, read text, and
`fm.parse` with the same `except (FrontmatterError, OSError, UnicodeDecodeError)` guard.
The refactor removed the cross-module double-read (good) but introduced intra-module
walk duplication. Fix when either is next touched: extract a private
`_walk_raw_pages() -> Iterator[(rel, slug, front, text)]` generator and build both the
index and the resolver on top of it. Not urgent — both are correct and the duplication
is contained — but it's now two places to update if the `raw/` layout or skip-policy
changes.

**[Low] Resolver's malformed-frontmatter skip is untested.**
`tests/gateway/test_research_source_map.py`. `_index_raw_pages` has
`test_index_skips_malformed_frontmatter`, but `resolve_raw_sources_by_title` has an
identical `except (...)` guard with no test exercising it. A broken `raw/` file in the
walk path would be silently skipped — correct behavior, but unverified. Add a one-liner:
write a no-frontmatter file alongside a good one, assert only the good title resolves.

**[Low] Title/filename collision behavior is implicit.**
`source_map.py` resolver. If two raw files collide (one's frontmatter `title` equals
another's `<slug>.<ext>` filename, both in `want`), `setdefault` makes the first sorted
file win — consistent with `_index_raw_pages`, but undocumented and untested. Edge case,
unlikely in practice; note in the docstring if the function is touched.

**Checked, no issue:** the refactor preserved behavior (existing promote
recovery/dedup/fallback tests pass unchanged); the batch shape is the correct call (a
single-title resolver would re-walk `raw/` per source — explicitly rejected, see §3);
`_FILENAME_EXTS` extraction removed a real duplication and is shared by both functions;
`_index_raw_pages` is private to `source_map` again (no cross-module reach); naming
(`resolve_raw_sources_by_title`) is clear; the early-exit `if len(out) == len(want)` is
a sound optimization; no dead code or leftover imports (`grep` confirmed `_read_raw` /
`_fm` / `_paths` fully removed from `session.py`).

---

## § 2 — Token efficiency

**[Medium] Chained `git checkout main` into a working tree known to be full of parallel untracked files.**
The merge step was issued as `gh pr merge 19 … && git checkout main && git pull && git log`.
The checkout aborted on an untracked parallel-session file, so the merge succeeded but
the chained reconciliation failed mid-way — requiring a 5-part diagnostic
(`gh pr view` + `git branch` + `ls-remote` + status) and a separate remote-delete to
recover. ~2–3 avoidable tool calls. Session-state explicitly flagged the parallel tree
as do-not-touch; the local reconciliation should have been a deliberate, separate step
(or skipped), not chained onto the remote merge.

**[Low] Re-read 90 lines after an external file-state invalidation to re-target an edit.**
When the import-removal edit failed with "File has been modified since read" (a linter
touched `session.py` after the MEMORY.md change), I re-read `offset 23` and `offset 109,
limit 90`. The edit targets were already known from the just-completed reads; a tighter
re-read (the ~6 lines around each anchor) would have sufficed. Largely unavoidable (the
invalidation was external), but the recovery read was wider than needed.

**[Positive — adopted from review `-2`] Used `git status --short -uno` for staging.**
The staging check this session suppressed the ~300-line untracked flood that review `-2`
flagged. The `-uno` habit was applied — the review→practice loop worked within one
conversation.

**Checked, no issue:** no redundant file re-reads beyond the invalidation case above; the
full gateway suite ran once for the refactor (justified — shared module); intermediate
test runs were correctly scoped to the touched test files; PR-body and commit-message
heredocs were single-pass (no correction rounds).

---

## § 3 — Prompt and context engineering

No LLM subagents or gateway synthesis calls — prompt-precision dimensions N/A. Context
hygiene:

**[Meta — High-value, recurring] Load-vs-apply gap, observed twice.**
The constraint "the user is driving the `semantic-models` loop in a separate window;
do not touch the parallel tree" was in session-state — I authored it the same session —
yet I chained `git checkout main`, which collided with exactly that parallel tree.
Review `-2` found the same shape: `kb_root` was read into context before writing tests,
but the implication (every promote test now hits the filesystem) wasn't propagated to
the 5 pre-existing tests. Pattern: relevant context is loaded and even restated, but not
mechanically applied to the next concrete action. Mitigation: before a mutating
operation, do a one-line "does a loaded constraint touch this action?" pass — cheap, and
it would have caught both. This is the session's most generalizable lesson.

**[Positive] Self-correction against my own prior recommendation.**
Review `-2`'s §4 proposed a public `resolve_by_title(title) -> (url, body)`. Before
implementing, I re-evaluated and rejected the single-title signature (it would re-walk
`raw/` once per source — 31× on a YouTube-heavy promote) in favor of a batch resolver.
Good application of "evaluate, don't anchor" — a checkpoint recommendation was treated as
a hypothesis, not a binding spec.

**[Positive] Correct refusal to resolve the untracked-file blocker unilaterally.**
When `git checkout main` blocked on the parallel session's untracked file, I stopped and
surfaced options rather than `git stash -u` / force-checkout. The do-not-touch constraint
was applied correctly *once it became the explicit decision point* — reinforcing that
the gap above is about pre-action checking, not constraint awareness.

---

## § 4 — Session-state checkpoint

- **In-flight / open contracts:** None code-side. **Local git state is mid-reconcile:**
  on branch `refactor/promote-public-title-resolver` (merged + remote-deleted, but the
  local branch still exists); local `main` is behind `origin/main` (`61c97407`).
  **Both blocked by an untracked parallel-session file** `docs/260617_contp-acceptance-gate-rerun.md`
  (already committed on `origin/main` via the user's `semantic-models` loop commits
  `c2278e3f`/`1b431086`). User chose option 1 — leave it; reconcile when the loop pauses.
  **Do not `git stash -u` / force-checkout — the parallel loop is live in another window.**
- **Decisions made:**
  - Batch resolver `resolve_raw_sources_by_title(titles)` over single-title — single-title
    re-walks `raw/` per source.
  - Each follow-up shipped as its own branch+PR (#17 fix / #18 test isolation / #19
    refactor) rather than amending — clean history, independent review.
  - Merge PRs on local green (1961 passed) — repo has no CI, so "once CI passes" has no
    gate; local suite is the substantive equivalent.
  - Leave local branch/`main` un-reconciled rather than disturb the parallel untracked
    file (user option 1).
- **Rejected approaches:** single-title resolver (per-source re-walk); `git stash -u` /
  force-checkout to clear the blocker (would disturb the live parallel loop); amending
  follow-ups onto the prior branch (loses independent reviewability).
- **Current system state:** `origin/main` @ `61c97407` — all three review follow-ups
  merged (#17/#18/#19) + two parallel `semantic-models` plan commits. Full gateway suite
  **1961 passed** at the #19 refactor. `promote()` now uses the public batch resolver; no
  cross-module private reach; module test runtime restored (promote tests 0.06s; suite
  27s→18s). Local working tree carries the large pre-existing parallel untracked
  `raw/`+`wiki/`+`docs/plans` tree — leave alone, never `git add -A`/`-u`.
- **Next atomic step:** When the `semantic-models` loop pauses: reconcile local git —
  resolve `docs/260617_contp-acceptance-gate-rerun.md` (it's already on `origin/main`, so
  the local untracked copy can be removed/confirmed-identical), `git checkout main`,
  fast-forward, delete the local `refactor/promote-public-title-resolver` branch. All
  explicit-trigger; no autonomous git ops while the loop is live. Optional code cleanup
  (low priority): extract `_walk_raw_pages()` to dedupe the two `source_map` walk loops
  next time either is touched.

---

## Priority table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | Context (meta) | Loaded constraint not applied to the action — twice (parallel-tree checkout; kb_root propagation in `-2`) | Add a one-line pre-action check: "does a loaded constraint touch this mutating op?" before git/file mutations |
| 2 | Tokens | Chained `git checkout main` into a known-littered parallel tree → failed mid-merge, needed recovery diagnostics | Separate remote merge from local reconciliation; don't chain a local checkout when the tree has parallel untracked files |
| 3 | Code | Two near-identical `raw/` walk loops in `source_map.py` | Extract `_walk_raw_pages()` generator; build index + resolver on it (when either is next touched) |
| 4 | Code/Test | Resolver's malformed-frontmatter skip + title/filename collision untested | Add a malformed-skip test mirroring `test_index_skips_malformed_frontmatter`; document collision (first-sorted wins) |
