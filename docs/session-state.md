# Session state — 2026-06-09

Last updated: 2026-06-09 (RAG retrieval workstreams — M1 WS1+WS4 complete; executing in self-improving loop)

---

## Open contracts

**RAG retrieval build (this session) — M1 DONE, loop in progress.**
Executing the workstreams in `docs/reviews/2026-06-09-rag-retrieval-review.md`
in priority order, with an eval + test + state-analysis + re-plan checkpoint at
each stream boundary (the loop). Order (revised after M1): WS1+WS4 ✓ → WS2 →
**WS5 (promoted)** → WS3 → WS6 → WS8. WS7 (vectors) deferred behind trigger.

M1 shipped (all on working tree, not yet committed):
- `src/gateway/search_index.py` — SQLite FTS5 derived index at `.index/wiki.db`
  (gitignored). Section-level, BM25-weighted, self-healing (mtime/size diff per
  query, no write-path hook). Materializes wiki→wiki inbound link counts.
- `src/gateway/ops/search.py` — rewired onto the index; SRCH-1 tier contract
  preserved; added `order="bm25"`.
- `src/gateway/ops/ingest.py` — `_gather_existing_pages` index-ranked by source
  title (glob fallback); `search_index` import added.
- `src/gateway/ops/index_rebuild.py` — rebuilds FTS index alongside index.md.
- `src/gateway/evaluate/retrieval_eval.py` + `.knowledge/eval/retrieval/goldens.yaml`
  (27 goldens) + `wiki eval-retrieval` CLI (CLI-only; in mcp_server CLI_ONLY).
- `src/gateway/paths.py` — `index_dir()`, `search_db_path()`.
- `.gitignore` — `.index/`.
- Tests: `tests/gateway/test_ws1_search_index.py` (13), `test_ws4_retrieval_eval.py` (4).

**Full suite: 1971 passed.** Live eval: FTS recall@10 = 0.889 / recall@5 = 0.741
/ MRR = 0.480, vs grep baseline 0.000 across the board.

Carry-forward (gateway build — unchanged): schema-drift ~208; finalize-batch
~460 researcher pages; orphans (condo-capital-infra, glp1-reward-modulation,
ai-native-business); edge-ai notebook quota; `wiki migrate` stub.

Carry-forward (orita-cmo, iOS Shortcut, web-API hardening): unchanged from
2026-06-02 checkpoint — see git history of this file if needed.

---

## Files mid-edit

None. All M1 edits complete and tested. Working tree has the M1 changes
uncommitted plus the pre-existing untracked gateway-managed `nlm/`/`raw/`/`wiki/`
content from before this session (leave alone — gateway-owned).

---

## Decisions made this session

- **SQLite FTS5 over the May review's throwaway JSON keyword index.** TOK-4
  already closed the plan-context bottleneck that justified deferral; corpus has
  grown to ~5.2k pages; goal is now agent retrieval. Build the durable thing once.
- **Section-level rows, not whole-page.** Enables returning the relevant section
  (feeds WS2/WS3 budgets).
- **No write-path index hook.** Self-heal on read instead — an index failure must
  never break an ingest. Stat-scan cost (~5k stats) measured at 0.07s; acceptable.
- **Obsidian is not the RAG lever** (review §1) — the graph/frontmatter it
  visualizes are vault properties the gateway already owns; route retrieval there.
- **WS5 promoted to right-after-WS2** — M1 eval showed every miss is a canonical
  page out-ranked by mention pages; inbound-link authority boost is the fix and
  the data is already in the index.

---

## Next atomic step

1. **WS2** — `wiki retrieve "<question>" [--domain X] [--k N] [--budget CHARS]`:
   FTS5 section retrieval → filters → bounded (`~30-50KB`) context block with
   `<page path=... section=...>` wrapping and `[[sources/<id>]]` preserved.
   Consume `search_index.search_fts(order=...)` directly (not via `ops.search`)
   for bm25 ordering + raw section bodies. Expose MCP `wiki_retrieve`.
2. At WS2 conclusion: run `wiki eval-retrieval --compare`, full `pytest`,
   checkpoint here, append M2 to the review's Execution log, re-plan, then WS5.
3. **Commit M1** before/at start of WS2 (not yet committed): branch off main,
   structured commit, the search_index + eval + ingest-rewire as one logical unit.
