# Multi-domain balanced retrieval — design

Date: 2026-06-11
Status: approved (brainstorming), pending implementation plan

## Problem

There is no way to produce a grounded synthesis page that draws a *balanced*
grounding context from — and is correctly tagged to — more than one domain.
Verified 2026-06-11 while filing the data-collectives Stage 2 page, which
legitimately cites both `data-collectives` and `condo-capital-infra` sources but
had to be hand-assembled.

Three concrete failures:

1. `wiki answer --domain X` hard-excludes every other domain. Filing with
   `--domain data-collectives` made auto-synthesis refuse, because condo sources
   live in `condo-capital-infra` and were never retrieved.
2. Omitting `--domain` retrieves globally, but a single ranked k-window collapses
   toward the lexically-dominant domain. Evidence (LLM-free `wiki retrieve`, no
   `--domain`): cross-domain query → 2 sections both `data-collectives`, 0 condo;
   balanced query at k=12 → 3 sections all `data-collectives`. The corpus is
   reachable; one call never assembles a per-domain-balanced context.
3. `wiki answer` writes single-valued domain frontmatter
   (`src/gateway/ops/answer.py:222`: `"domains": [domain] if domain else []`). A
   page spanning two domains cannot be tagged to both via the gateway.

Net: the only current path is a manual scaffold-then-replace workaround
(`wiki answer --file` → `wiki edit --section` hand-cited body → `wiki finalize`,
then patch frontmatter by direct Edit) — undiscoverable and error-prone.

## Decision

Expose the capability as a **flag on existing ops** (not a new `wiki synthesize`
op). Least surface area; reuses the retrieval ladder; nothing new to learn.
Confirmed with user 2026-06-11.

## Design

### 1. Retrieval core — `retrieve()` in `src/gateway/ops/retrieve.py`

Add a `domains: list[str] | None` parameter alongside the existing `domain`.

- **`domains` is `None` / empty / single entry → unchanged.** One `search_fts`
  call, existing `order="authority"` ranking, existing budget assembly. This is
  what guarantees the golden set cannot regress: the multi-domain path is new
  code that `eval-retrieval` never exercises.
- **`domains` has ≥2 entries → quota merge:**
  1. Per-domain quota `q = ceil(k / N)` where `N = len(domains)`. Run
     `search_fts(query, domain=d, limit=q, order="authority")` once per domain.
  2. **Round-robin interleave** the per-domain hit lists by per-domain rank
     (domain A rank-1, domain B rank-1, A rank-2, B rank-2, …). Interleaving —
     not a global re-rank — is the load-bearing choice: if the byte budget
     truncates the block, per-domain balance survives. A global re-rank would let
     the lexically-dominant domain refill the front of the list and re-collapse,
     which is the exact bug being fixed.
  3. De-dup by `rel_path`: a page tagged to both domains appears once, at its
     first-seen (highest) position. Assemble blocks under the same
     `budget_chars` / `max_section_chars` caps as the single path.

Returns the same `(block, sections)` tuple. No change to `RetrievedSection`.

`retrieve_op` gains a `domains` passthrough and logs the domain list.

### 2. Authoring op — `answer()` / `answer_op()` in `src/gateway/ops/answer.py`

- Thread `domains: list[str] | None` through `answer()` → `retrieve()` and
  through `answer_op()` → `answer()` → `_file_draft()`.
- `_file_draft` writes `domains: list(domains)` when multi-domain (fixing
  `answer.py:222`); falls back to `[domain] if domain else []` for the single
  case. `sources_count` already derives from `res.source_ids` — correct as-is.
- Log line includes the domain list.

### 3. CLI surface — `src/gateway/cli.py` (retrieve + answer subparsers)

- Add `--domains` accepting a comma-separated string; parse to `list[str]`
  (strip whitespace, drop empties).
- `--domain` (single) stays for back-compat. If both are passed, `--domains`
  wins; document that precedence.

### 4. MCP surface

Mirror the `domains` parameter on the `wiki_retrieve` / `wiki_answer` MCP tools
if they expose `domain` (verify during implementation; add only if present).

## Merge strategy — worked example

`k=12`, `domains=[data-collectives, condo-capital-infra]`, `N=2`, `q=6`.

- search_fts(domain=data-collectives, limit=6) → [DC1..DC6]
- search_fts(domain=condo-capital-infra, limit=6) → [CC1..CC6]
- interleave → [DC1, CC1, DC2, CC2, DC3, CC3, …] → assemble under budget.

If the budget truncates after 8 sections, the block still holds 4 DC + 4 CC —
balanced — instead of 8 DC + 0 CC.

## Testing

**RED test first** (TDD, superpowers): assert that a multi-domain `retrieve`
over a cross-domain query returns sections from *each* named domain
(quota-balanced), not just the dominant one. Must fail against current behavior
(no `domains` param) before implementing.

Test layers:
- `retrieve()` unit: multi-domain returns ≥1 section per named domain on a query
  the single-call path collapses; round-robin order; dedup of a dual-tagged page;
  budget-truncation preserves balance.
- `answer()` / `_file_draft`: multi-domain frontmatter is list-valued with all
  named domains; `sources_count` matches cited ids.
- One small end-to-end `wiki answer --domains a,b` smoke test (the only
  token-spending test — keep the call minimal; Anthropic spend cap is live).

**Golden-set guard:** run `wiki eval-retrieval --compare` before and after. Do
not regress baseline recall@5 0.889 / recall@10 0.926 / MRR 0.722. Expected
delta: zero, because the single/global paths are untouched.

## Constraints

- Gateway-only writes to `wiki/` / `raw/`.
- `.venv/bin/python` / `.venv/bin/wiki` only.
- Staging discipline: never `git add -u` / `git add wiki/` — the working tree
  carries a pre-existing condo backlog of modified/untracked `wiki/`/`raw/`/`nlm/`
  files. Stage `src/`, `tests/`, `docs/`, `WIKI.md`, append-only `log.md`
  explicitly.

## Documentation

- `WIKI.md` § Gateway operations: document `--domains` on `retrieve` and `answer`,
  the quota-merge behavior, and `--domains`-wins precedence.
- `CLAUDE.md` § Retrieval ladder: one-line invariant note that multi-domain
  retrieval balances by per-domain quota (not a single global k-window).

## Out of scope (YAGNI)

- Quota-merging the global (no-domain) path. Risk: changes default ranking,
  golden-set-gated. Deferred — revival trigger: a verified need to balance an
  *un-named* multi-domain query.
- A dedicated `wiki synthesize` op. Rejected: duplicates `wiki answer`.
- Per-domain *weighted* quotas (e.g. 70/30). Equal quota until a real asymmetric
  case appears.
