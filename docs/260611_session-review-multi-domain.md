# Session review — 2026-06-11 (multi-domain balanced retrieval, gateway)

Scope: 7 commits (`19173bc3..71149f38` + merge `089dac39`), ~201 lines app code
across 6 files, TDD throughout. Brainstorm → spec → plan → inline execution →
PR #15 merged. One LLM call (smoke test). No prior-session rework.

Separate file from `docs/260611_session-review.md` (that brief covers a different
session — data-collectives foundation + Stage 2, written 06:33; not overwritten).

## § 1 — Code and coding quality

**[High] `_merge_domains` under-fills `k` on asymmetric domains — no test, no
documented tradeoff.** `src/gateway/ops/retrieve.py:60-77`. With
`quota = ceil(k/N)`, a domain returning fewer than `quota` hits leaves slots
unfilled even when another named domain has more available results. Example:
`k=12, N=2, quota=6`; domain A has 10 matching pages (only 6 fetched), B has 1 →
merged returns 7, not 12, despite A having 4 more. The single-domain path would
return up to 12. Real balance-vs-fill tradeoff, possibly the right default, but
neither documented nor tested; a caller asking `k=12` silently gets fewer. **Fix:**
add a backfill second pass over domains that still have hits to top up to `k`, OR
document the tradeoff in the docstring and add a test asserting the
asymmetric-underfill is intentional. All current multi-domain fixtures use
symmetric domain sizes, so the suite cannot catch this.

**[Medium] DRY: comma-split parsing duplicated across 4 call sites.** `cli.py`
(retrieve + answer), `mcp_server.py` (retrieve + answer) each carry
`[d.strip() for d in raw.split(",") if d.strip()] if raw else None`; plus
`",".join(...)` as `domain_label` in both ops. Six copies of two idioms. **Fix:**
one shared helper (e.g. `parse_domains(s) -> list[str] | None`) referenced
everywhere — a future change to the separator or empty-handling touches one site.

**[Medium] `data["domain"]` field overloaded with a comma-joined string.**
`retrieve_op` and `answer_op` set `data["domain"] = domain_label or None`, where
`domain_label` is `"a,b"` for multi-domain. The field was a single slug; any
consumer parsing it as one slug now receives `"a,b"`. **Fix:** keep
`data["domain"]` single-valued and add a distinct `data["domains"]: list[str]`.

**[Low] Imprecise type annotation.** `_merge_domains(...) -> list:` — bare `list`
where the codebase uses precise element types. Should be
`list[search_index.IndexHit]`.

**Convention adherence — positive:** new code matches the file's posture (pure
`retrieve()` stays LLM-free; `order="authority"` preserved; docstrings updated in
place; single/global branch byte-identical, which protects the golden set). No
dead code, no commented blocks.

## § 2 — Token efficiency

**[Medium] `wiki eval-retrieval --compare` run 3×.** Ran once (output truncated to
the golden list), again with `grep`, a third with `grep -v`. Each run re-executes
retrieval over all 27 goldens. **Saved by:** one run piped to a file, then grep
the file — ~2 redundant eval executions avoided (heaviest command of the session).

**[Low] Edit-after-heredoc collision.** Appended a test via Bash heredoc, then
tried `Edit` on the same file → "File has been modified since read" → forced
re-`Read` + retry. ~2 wasted calls. **Saved by:** not mixing heredoc-append and
`Edit` on one file in the same turn.

**[Low] Task 2 budget-arithmetic miss.** First dedup/truncation test set
`budget_chars=1800` against ~1900-char pages → only 1 section fit → diagnose +
rewrite. ~2 calls. **Saved by:** sizing the budget to admit ≥3 sections up front.

**Positive:** reads were disciplined — `search_fts` read targeted (90 lines), CLI
read by section, continuation + session-state read in parallel. The inline
domain-balance verification (Counter by `page_domains`) was high-value proof, not
waste.

## § 3 — Prompt and context engineering

**[Positive] Precondition check prevented a wasted RED cycle.** Before the MCP
test I read `_serialize` and found it exposes `summary`, not `data` — so the test
asserts on the block's `domain="..."` attributes instead of a nonexistent
`data["section_count"]`. The plan specified the wrong shape; catching it pre-run
saved a failed cycle.

**[Positive] Context seeding matched the work.** Reading `search_fts` before
designing surfaced that `page_domains` is already many-to-many — de-risking the
frontmatter change (index already supported multi-domain pages; only the authoring
op was single-valued). Constraint discovered before the design.

**[Low] Surface-anchor leakage — the `domain_label` idiom propagated by copy.**
Written in `retrieve_op`, copied verbatim into `answer_op`; comma-split copied
into 4 CLI/MCP sites. Structural decisions (interleave vs re-rank) reasoned
freshly; this surface idiom duplicated silently — the pattern the global
anti-pattern guard names. Centralizing it (§1 #2) closes the leak.

**[Positive] One LLM call, right-sized.** The smoke test used the real handoff
question against the default Sonnet grounded-synthesis model; balanced
cross-domain output first try, no correction round. Brainstorming asked exactly
one genuine fork (surface choice).

## Priority table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | Code (High) | `_merge_domains` under-fills `k` on asymmetric domains; untested | Add backfill pass to top up to `k`, or document tradeoff + add a test |
| 2 | Code (Medium) | Comma-split parsing duplicated 6× across CLI/MCP/ops | Extract one `parse_domains` helper; reference everywhere |
| 3 | Code (Medium) | `data["domain"]` overloaded with `"a,b"` string | Add separate `data["domains"]: list`; keep `domain` single-valued |
| 4 | Tokens (Medium) | `eval-retrieval --compare` run 3× to parse output | Pipe once to a file, grep the file |
| 5 | Prompt (Low) | `domain_label`/comma-split surface idiom copied, not shared | Fixing #2 also closes the leak |
