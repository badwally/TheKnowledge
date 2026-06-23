# Continuation prompt — RAG draft-visibility fix (paste into a fresh session after /clear)

```
Objective: implement the Hole 1 fix for `wiki retrieve` — stop hard-excluding draft pages so the curated concept/entity/synthesis layer is reachable by the default agent retrieval path — without degrading citation fidelity. Critical project: this brings the knowledge system to high utility and is the prerequisite for any later embedding/hybrid-retrieval work.

Read first (full context lives here; do not re-derive):
- docs/260622_rag-retrieval-draft-visibility-brief.md   ← the diagnosis, pinned mechanism, fix options, open design questions, and the probe goldens (Appendix A) + triage script (Appendix B)
- src/gateway/ops/retrieve.py  (lines 160, 282 — include_drafts default)
- src/gateway/search_index.py  (lines 356, 385-386 — the WHERE p.draft=0 filter; 461 — _authority_key / _DRAFT_PENALTY)

Pinned root cause: retrieve() defaults include_drafts=False → search_fts adds `WHERE p.draft = 0` → drafts removed from the candidate pool BEFORE ranking. ~30% of concepts, ~30% of entities, 92% of synthesis are perma-draft (legacy migration), so ~1,100 curated pages are invisible to `wiki retrieve`. `wiki search` (include_drafts=True) ranks the same pages #1 — that divergence is the whole bug.

Next atomic step: settle three design questions (in the brief), then implement option A. 
  (1) A alone vs A+D: demote drafts via existing _DRAFT_PENALTY vs also content-gate out `_(needs population...)_` stub sections.
  (2) Annotate draft provenance on the <page> block tag (draft="true") so consumers know it's unfinalized? (leaning yes)
  (3) Persist the probe goldens as a permanent fixture .knowledge/eval/retrieval/semantic_mismatch.yaml wired into the gate? (leaning yes)
Then: implement demote-not-exclude in retrieve.py/search_index.py, persist the goldens fixture, and validate.

Validate with BOTH (the eval harness only tests the FTS layer, NOT the retrieve assembly):
- before/after: run the Appendix-B triage script (scores the real `wiki retrieve --json` path). Current ~2/21; target: 3 controls flip to HIT and overall climbs toward the FTS ceiling ~0.33.
- regression: `.venv/bin/wiki eval-retrieval --compare --k 10` must not regress recall@10 ≥ 0.90 on the existing easy goldens.
- pre-merge gate: `.venv/bin/python -m gateway.scripts.gate`.

Constraints / gotchas (un-carried, these get re-broken):
- This is a citation-grounding BEHAVIOR change → keep the design pass; do NOT blind-flip include_drafts=True (that's blunt option B). The brainstorming flow was started for this and paused for the handoff.
- A concurrent session shares this working tree on branch `fix/authorship-loop-comprehensive`. Do NOT edit docs/session-state.md (owned by the other session). Verify `git branch --show-current` before ANY commit; never commit to main; if committing, push a branch + PR. Recover orphaned work via `git show <sha>:<path>`.
- Always use `.venv/bin/python` and `.venv/bin/wiki`, never system python.
- No direct writes to wiki/ or raw/ (gateway-only hard rule). This work is src/gateway + docs + eval fixtures, which is fine.

Non-goals (stay scoped to Hole 1):
- Do NOT start Hole 2 (embedding / hybrid retrieval) — re-baseline the probe AFTER this fix first.
- Do NOT start Hole 3 (finalize/cull the ~1,100 perma-draft backlog) — parallel curation track, separate.
- NotebookLM is orthogonal; leave it.
```

Left out deliberately: the embedding-model option comparison (EmbeddingGemma/Qwen3/Voyage) and the full three-hole sequencing — both live in the brief, and both belong to Hole 2, which is out of scope for the next session.
