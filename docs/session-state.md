# Session state — 2026-06-09

Last updated: 2026-06-09 (RAG retrieval build COMPLETE — all 6 workstreams landed on branch feat/rag-retrieval-fts)

---

## Open contracts

**RAG retrieval build — DONE and MERGED to main.** All workstreams from
`docs/reviews/2026-06-09-rag-retrieval-review.md` executed in a self-improving
loop (eval + tests + state-analysis + re-plan at each boundary). Fast-forward
merged to `main` (branch `feat/rag-retrieval-fts` deleted). **Not pushed** —
`main` is 9 commits ahead of `origin/main`; push is the user's call.

Commits (6, each green):
- `d9ff3850` WS1+WS4 — FTS5 index + ranked search + eval harness
- `ad9f13cf` WS2 — `wiki retrieve` composite RAG primitive
- `9202ed7d` WS5 — graph-aware authority ranking + `wiki related`
- `1370e08a` WS3 — budget-aware `wiki context`
- `2031f4cc` WS6 — `wiki answer` local grounded synthesis
- (WS8 docs + eval alignment — committing now)

Final state: **2002 tests pass** (1945 at session start, +57). Retrieval eval
(authority order, live corpus): recall@5 0.889, recall@10 0.926, MRR 0.722.

**Next decision for the user:** merge `feat/rag-retrieval-fts` → main (PR or
fast-forward), then optionally `wiki index --rebuild` on the canonical tree to
build `.index/wiki.db` (gitignored; ~34s, ~86 MB). The index self-heals on read
so this is optional — first `wiki search`/`retrieve` call builds it lazily.

Deferred (unchanged trigger): WS7 hybrid vector retrieval — revive when golden
recall@10 < ~0.8 after authority ranking, or at ~10k pages. Trigger unmet.

Carry-forward (pre-existing, untouched this session): schema-drift ~208;
finalize-batch ~460; orphans (condo-capital-infra, glp1-reward-modulation,
ai-native-business); edge-ai notebook quota; `wiki migrate` stub; orita-cmo R3/R2;
iOS Shortcut completion; web-API hardening (all from 2026-06-02 checkpoint).

---

## Files mid-edit

None. All RAG work committed on `feat/rag-retrieval-fts` except the in-flight WS8
docs commit. Working tree otherwise carries pre-existing untracked gateway-managed
`nlm/`/`raw/`/`wiki/` content (leave alone — gateway-owned).

---

## New retrieval surface (reference)

- `gateway/search_index.py` — FTS5 derived index (`.index/wiki.db`), `search_fts`
  (orders: tiered/bm25/authority), `section_text`, `inbound_counts`,
  `related_pages`, `top_pages_for_domain`.
- `gateway/ops/retrieve.py` — `retrieve()`/`retrieve_op()` (WS2), `related_op()` (WS5).
- `gateway/ops/answer.py` — `answer()`/`answer_op()` (WS6), injectable LLM client.
- `gateway/ops/context_op.py` — budget-aware (WS3).
- `gateway/evaluate/retrieval_eval.py` + `.knowledge/eval/retrieval/goldens.yaml` (WS4).
- CLI: `wiki retrieve|answer|related|search|context|eval-retrieval`.
- MCP: `wiki_retrieve`, `wiki_answer`, `wiki_related` (+ updated `wiki_context`,
  `wiki_search`). `eval-retrieval` is CLI_ONLY.

---

## Next atomic step

1. Optional: `git push` (`main` is 9 ahead of `origin/main`).
2. Optional: `wiki index --rebuild` on the canonical tree to materialize
   `.index/wiki.db` (else it builds lazily on first retrieve/search).
