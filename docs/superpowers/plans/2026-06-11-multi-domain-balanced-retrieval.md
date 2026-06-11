# Multi-domain Balanced Retrieval Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let `wiki retrieve` and `wiki answer` assemble a per-domain-balanced grounding context across ≥2 named domains and tag the filed page to all of them.

**Architecture:** A new multi-domain branch in `retrieve()` runs one `search_fts` per domain at quota `ceil(k/N)`, round-robin-interleaves the per-domain hit lists by rank, de-dups by path, and assembles under the existing budget caps. The single-domain/global path is byte-for-byte unchanged, so the retrieval golden set cannot regress. `answer()`/`_file_draft` thread the domain list through and write list-valued `domains:` frontmatter.

**Tech Stack:** Python 3, argparse CLI, SQLite FTS5 (`gateway.search_index`), pytest. Use `.venv/bin/python` / `.venv/bin/wiki` exclusively.

---

## File Structure

- `src/gateway/ops/retrieve.py` — add `domains` param + quota-merge helper `_merge_domains`. Core change.
- `src/gateway/ops/answer.py` — thread `domains` through `answer`, `answer_op`, `_file_draft`; list-valued frontmatter.
- `src/gateway/cli.py` — `--domains` on the `retrieve` and `answer` subparsers; parse comma-separated; pass through in `_run_retrieve_cmd` / `_run_answer_cmd`.
- `tests/gateway/test_ws2_retrieve.py` — multi-domain retrieve tests.
- `tests/gateway/test_ws6_answer.py` — multi-domain answer + frontmatter tests.
- `WIKI.md`, `CLAUDE.md` — docs.

**Staging discipline (every commit):** never `git add -u` or `git add wiki/`. The working tree carries a pre-existing condo backlog. Stage only the explicit paths shown in each commit step.

---

## Task 1: Multi-domain `retrieve()` quota balance (RED first)

**Files:**
- Test: `tests/gateway/test_ws2_retrieve.py`
- Modify: `src/gateway/ops/retrieve.py`

- [ ] **Step 1: Write the failing test**

Append to `tests/gateway/test_ws2_retrieve.py`. The `_page(slug, title, body, domain=...)` helper already exists at the top of the file. We seed a domain `alpha` whose pages dominate lexically (more matching pages) and a domain `beta` with fewer, then assert a `domains=` retrieve surfaces both.

```python
def test_retrieve_multi_domain_balances_quota(kb_root: Path):
    # alpha dominates lexically (5 matching pages); beta has 2.
    for i in range(5):
        _page(f"a{i}", f"Alpha {i}", f"## S\n\nshared signal token alpha-{i}.\n", domain="alpha")
    for i in range(2):
        _page(f"b{i}", f"Beta {i}", f"## S\n\nshared signal token beta-{i}.\n", domain="beta")
    search_index.refresh(rebuild=True)

    # Single global call collapses toward the dominant domain...
    _block_single, single = retrieve("shared signal token", k=4)
    assert {s.domain for s in single} == {"alpha"}, "precondition: global call collapses to alpha"

    # ...multi-domain quota merge must surface BOTH named domains.
    _block, sections = retrieve("shared signal token", domains=["alpha", "beta"], k=4)
    doms = {s.domain for s in sections}
    assert "alpha" in doms and "beta" in doms, f"expected both domains, got {doms}"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py::test_retrieve_multi_domain_balances_quota -v`
Expected: FAIL — `TypeError: retrieve() got an unexpected keyword argument 'domains'`.

- [ ] **Step 3: Add the `domains` param and quota-merge branch**

In `src/gateway/ops/retrieve.py`, add a helper above `retrieve()` and a `domains` parameter. Add `import math` to the top-of-file imports (after `from dataclasses import dataclass`).

```python
def _merge_domains(
    query: str, domains: list[str], k: int, *, order: str, include_drafts: bool, scope: str,
) -> list:
    """Per-domain quota + round-robin interleave, de-duped by rel_path.

    Runs one search per named domain at quota ceil(k/N), then interleaves by
    per-domain rank so byte-budget truncation downstream preserves balance
    rather than collapsing toward the lexically-dominant domain.
    """
    n = len(domains)
    quota = math.ceil(k / n)
    per_domain = [
        search_index.search_fts(
            query, scope=scope, domain=d, limit=quota,
            order=order, include_drafts=include_drafts,
        )
        for d in domains
    ]
    merged: list = []
    seen: set[str] = set()
    for rank in range(quota):
        for hits in per_domain:
            if rank < len(hits) and hits[rank].rel_path not in seen:
                seen.add(hits[rank].rel_path)
                merged.append(hits[rank])
    return merged[:k]
```

Then change the `retrieve()` signature and the hit-fetch. Replace the signature line and the `hits = search_index.search_fts(...)` block:

```python
def retrieve(
    query: str,
    *,
    domain: str | None = None,
    domains: list[str] | None = None,
    k: int = _DEFAULT_K,
    budget_chars: int = _DEFAULT_BUDGET_CHARS,
    max_section_chars: int = _DEFAULT_MAX_SECTION_CHARS,
    scope: str = "wiki",
    include_drafts: bool = False,
) -> tuple[str, list[RetrievedSection]]:
```

Replace the existing `hits = search_index.search_fts(...)` call with:

```python
    multi = [d for d in (domains or []) if d and d.strip()]
    if len(multi) >= 2:
        hits = _merge_domains(
            query.strip(), multi, k,
            order="authority", include_drafts=include_drafts, scope=scope,
        )
    else:
        single = multi[0] if multi else domain
        hits = search_index.search_fts(
            query.strip(),
            scope=scope,
            domain=single,
            limit=k,
            order="authority",
            include_drafts=include_drafts,
        )
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py::test_retrieve_multi_domain_balances_quota -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/gateway/ops/retrieve.py tests/gateway/test_ws2_retrieve.py
git commit -m "feat(retrieve): multi-domain quota-merge balances grounding context

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 2: Dedup of a dual-tagged page + balance survives budget truncation

**Files:**
- Test: `tests/gateway/test_ws2_retrieve.py`
- (No new implementation — asserts the Task 1 code's dedup and interleave guarantees.)

- [ ] **Step 1: Write the failing test**

A page in BOTH domains must appear once; and when the budget truncates, both domains must still be represented (interleave guarantee). The `_page` helper writes single-domain frontmatter, so write a dual-tagged page inline.

```python
def test_retrieve_multi_domain_dedups_and_survives_budget(kb_root: Path):
    # One page tagged to BOTH domains.
    d = paths.wiki_dir() / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    both = {
        "type": "concept", "slug": "dual", "title": "Dual tagged",
        "domains": ["alpha", "beta"],
        "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z",
    }
    (d / "dual.md").write_text(fm.serialize(both, "## S\n\nshared signal token dual.\n"))
    # Plus large single-domain pages so the budget truncates.
    for i in range(3):
        _page(f"a{i}", f"Alpha {i}", "## S\n\nshared signal token " + ("alpha " * 300), domain="alpha")
    for i in range(3):
        _page(f"b{i}", f"Beta {i}", "## S\n\nshared signal token " + ("beta " * 300), domain="beta")
    search_index.refresh(rebuild=True)

    _block, sections = retrieve(
        "shared signal token", domains=["alpha", "beta"], k=6, budget_chars=1800,
    )
    paths_seen = [s.rel_path for s in sections]
    assert len(paths_seen) == len(set(paths_seen)), "no page should appear twice"
    assert len(sections) < 6, "budget should truncate"
    assert {s.domain for s in sections} >= {"alpha", "beta"}, "balance survives truncation"
```

- [ ] **Step 2: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py::test_retrieve_multi_domain_dedups_and_survives_budget -v`
Expected: PASS (the Task 1 interleave + `seen` set already provide these guarantees).

> Note: this is a characterization test confirming Task 1's design holds under truncation and dual-tagging. If it fails, the bug is in Task 1's `_merge_domains` — fix there, do not weaken the assertions.

- [ ] **Step 3: Commit**

```bash
git add tests/gateway/test_ws2_retrieve.py
git commit -m "test(retrieve): multi-domain dedup + balance survives budget truncation

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 3: Thread `domains` through `retrieve_op` + CLI `--domains`

**Files:**
- Modify: `src/gateway/ops/retrieve.py` (`retrieve_op`)
- Modify: `src/gateway/cli.py` (`p_retrieve` subparser, `_run_retrieve_cmd`)
- Test: `tests/gateway/test_ws2_retrieve.py`

- [ ] **Step 1: Write the failing test**

```python
def test_retrieve_op_accepts_domains(kb_root: Path):
    for i in range(3):
        _page(f"a{i}", f"Alpha {i}", f"## S\n\nshared signal token a{i}.\n", domain="alpha")
    _page("b0", "Beta 0", "## S\n\nshared signal token b0.\n", domain="beta")
    search_index.refresh(rebuild=True)
    res = retrieve_op("shared signal token", domains=["alpha", "beta"], k=4)
    assert res.success
    doms = {s["path"].split("/")[1] for s in res.data["sources"]}  # sanity: not empty
    assert res.data["section_count"] >= 2
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py::test_retrieve_op_accepts_domains -v`
Expected: FAIL — `TypeError: retrieve_op() got an unexpected keyword argument 'domains'`.

- [ ] **Step 3: Add `domains` to `retrieve_op`**

In `src/gateway/ops/retrieve.py`, edit `retrieve_op`'s signature and its `retrieve(...)` call and log fields:

```python
def retrieve_op(
    query: str,
    *,
    domain: str | None = None,
    domains: list[str] | None = None,
    k: int = _DEFAULT_K,
    budget_chars: int = _DEFAULT_BUDGET_CHARS,
    caller: str | None = None,
) -> OperationResult:
```

Change the `retrieve(...)` call to pass `domains=domains`:

```python
    block, sections = retrieve(
        query, domain=domain, domains=domains, k=k, budget_chars=budget_chars
    )
```

In the `log.append` `fields` dict and `summary`, replace the `"domain": domain or ""` usage with a combined label so multi-domain runs are legible:

```python
    domain_label = ",".join(domains) if domains else (domain or "")
```

Then use `domain_label` in both the `fields["domain"]` value and the `summary` f-string (replace `domain or '-'` with `domain_label or '-'`). Also set `data["domain"]` to `domain_label or None`.

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py::test_retrieve_op_accepts_domains -v`
Expected: PASS.

- [ ] **Step 5: Wire the CLI `--domains` flag**

In `src/gateway/cli.py`, after the `p_retrieve.add_argument("--domain", ...)` line (≈1278), add:

```python
    p_retrieve.add_argument(
        "--domains", default=None,
        help="Comma-separated domains for a per-domain-balanced block (e.g. a,b). "
             "Takes precedence over --domain.",
    )
```

In `_run_retrieve_cmd` (≈2602), parse and pass it:

```python
    raw_domains = getattr(ns, "domains", None)
    domains = [d.strip() for d in raw_domains.split(",") if d.strip()] if raw_domains else None
    result = retrieve_op(
        ns.query,
        domain=getattr(ns, "domain", None),
        domains=domains,
        k=ns.k,
        budget_chars=ns.budget_chars,
        caller=getattr(ns, "caller", "cli"),
    )
```

- [ ] **Step 6: Verify CLI end-to-end (LLM-free)**

Run: `.venv/bin/wiki retrieve "data collective reserve study" --domains data-collectives,condo-capital-infra --k 8 --json`
Expected: JSON with `section_count ≥ 2` and `sources` drawn from both domains (not all one domain). This is the real cross-domain query from the handoff — confirms the fix on live content.

- [ ] **Step 7: Commit**

```bash
git add src/gateway/ops/retrieve.py src/gateway/cli.py tests/gateway/test_ws2_retrieve.py
git commit -m "feat(cli): wiki retrieve --domains for balanced cross-domain blocks

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 4: `answer()` threads `domains`; `_file_draft` writes list-valued frontmatter

**Files:**
- Modify: `src/gateway/ops/answer.py`
- Test: `tests/gateway/test_ws6_answer.py`

- [ ] **Step 1: Write the failing test**

Append to `tests/gateway/test_ws6_answer.py`. Uses the existing `_StubClient` and `_page` helpers. Assert the filed draft's frontmatter lists BOTH domains.

```python
def test_answer_files_multi_domain_frontmatter(kb_root: Path):
    _page("widget", "Widget protocol",
          "## Spec\n\nHandshake [[sources/web-2026-01-01-abc]].\n", domain="alpha")
    _page("gadget", "Gadget protocol",
          "## Spec\n\nGadget handshake [[sources/web-2026-01-01-def]].\n", domain="beta")
    search_index.refresh(rebuild=True)
    client = _StubClient(
        "Both use handshakes [[sources/web-2026-01-01-abc]] "
        "[[sources/web-2026-01-01-def]]."
    )
    res = answer_op(
        "compare widget and gadget handshakes",
        domains=["alpha", "beta"], file_draft=True, client=client,
    )
    assert res.success
    filed = res.data["filed_path"]
    text = (paths.knowledge_root() / filed).read_text()
    front, _body = fm.parse(text)
    assert front["domains"] == ["alpha", "beta"], front["domains"]
```

> Verify the frontmatter parse helper name first: `grep -n "^def parse\|^def split" src/gateway/frontmatter.py`. If it is not `fm.parse` returning `(front, body)`, adjust the two lines above to the actual API (e.g. `fm.split`).

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws6_answer.py::test_answer_files_multi_domain_frontmatter -v`
Expected: FAIL — `TypeError: answer_op() got an unexpected keyword argument 'domains'`.

- [ ] **Step 3: Thread `domains` through `answer`, `answer_op`, `_file_draft`**

In `src/gateway/ops/answer.py`:

`answer()` — add `domains` param and pass to `retrieve`:

```python
def answer(
    question: str,
    *,
    domain: str | None = None,
    domains: list[str] | None = None,
    k: int = 12,
    budget_chars: int = 40_000,
    client=None,
    model: str | None = None,
) -> AnswerResult:
```

Change its `retrieve(...)` call to: `block, sections = retrieve(question, domain=domain, domains=domains, k=k, budget_chars=budget_chars)`.

`answer_op()` — add `domains` param, pass to `answer()` and `_file_draft()`, and use a combined label in the log:

```python
def answer_op(
    question: str,
    *,
    domain: str | None = None,
    domains: list[str] | None = None,
    k: int = 12,
    budget_chars: int = 40_000,
    file_draft: bool = False,
    client=None,
    model: str | None = None,
    caller: str | None = None,
) -> OperationResult:
```

Inside, change the `answer(...)` call to pass `domains=domains`; add `domain_label = ",".join(domains) if domains else (domain or "")` and use it in the `log.append` `fields["domain"]` and `summary`. Change the `_file_draft(question, domain, res)` call to `_file_draft(question, domain, res, domains=domains)`.

`_file_draft()` — accept `domains` and write list-valued frontmatter:

```python
def _file_draft(
    question: str, domain: str | None, res: AnswerResult,
    *, domains: list[str] | None = None,
) -> OperationResult:
```

Replace the frontmatter `"domains"` line:

```python
        "domains": list(domains) if domains else ([domain] if domain else []),
```

And update the `Plan.rationale` cross-domain label to use `",".join(domains)` when present:

```python
        rationale=f"wiki answer (local grounded synthesis) for "
                  f"{','.join(domains) if domains else (domain or 'cross-domain')}",
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws6_answer.py::test_answer_files_multi_domain_frontmatter -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/gateway/ops/answer.py tests/gateway/test_ws6_answer.py
git commit -m "feat(answer): multi-domain retrieval + list-valued domains frontmatter

Fixes single-valued domains: at answer.py:222 for cross-domain pages.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 5: CLI `--domains` on `wiki answer`

**Files:**
- Modify: `src/gateway/cli.py` (`p_answer` subparser, `_run_answer_cmd`)

- [ ] **Step 1: Add the flag**

In `src/gateway/cli.py`, after `p_answer.add_argument("--domain", ...)` (≈1288), add:

```python
    p_answer.add_argument(
        "--domains", default=None,
        help="Comma-separated domains for a balanced cross-domain grounded answer "
             "(e.g. a,b). Takes precedence over --domain; files list-valued domains:.",
    )
```

- [ ] **Step 2: Parse and pass in `_run_answer_cmd`**

In `_run_answer_cmd` (≈2622), before the `answer_op(...)` call:

```python
    raw_domains = getattr(ns, "domains", None)
    domains = [d.strip() for d in raw_domains.split(",") if d.strip()] if raw_domains else None
    result = answer_op(
        ns.question,
        domain=getattr(ns, "domain", None),
        domains=domains,
        k=ns.k,
        budget_chars=ns.budget_chars,
        file_draft=getattr(ns, "file_draft", False),
        caller=getattr(ns, "caller", "cli"),
    )
```

- [ ] **Step 3: Run the full retrieve+answer test files (no LLM cost — answer tests stub the client)**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py tests/gateway/test_ws6_answer.py -q`
Expected: all PASS.

- [ ] **Step 4: Commit**

```bash
git add src/gateway/cli.py
git commit -m "feat(cli): wiki answer --domains for cross-domain grounded synthesis

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 6: MCP surface — `domains` on `wiki_retrieve` / `wiki_answer`

**Files:**
- Modify: `src/gateway/mcp_server.py` (`wiki_retrieve`, `wiki_answer`)
- Test: `tests/gateway/test_ws2_retrieve.py` (a thin MCP-tool test, or extend an existing MCP test file if one targets `mcp_server` — `grep -rln "mcp_server" tests/` first)

Both MCP tools expose `domain`; mirror with a comma-separated `domains` string to match the CLI convention (FastMCP tool params stay flat strings, no list schema).

- [ ] **Step 1: Write the failing test**

Append to `tests/gateway/test_ws2_retrieve.py`:

```python
def test_mcp_wiki_retrieve_accepts_domains(kb_root: Path):
    from gateway.mcp_server import wiki_retrieve
    for i in range(3):
        _page(f"a{i}", f"Alpha {i}", f"## S\n\nshared signal token a{i}.\n", domain="alpha")
    _page("b0", "Beta 0", "## S\n\nshared signal token b0.\n", domain="beta")
    search_index.refresh(rebuild=True)
    res = wiki_retrieve("shared signal token", domains="alpha,beta", k=4)
    assert res["success"]
    assert res["data"]["section_count"] >= 2
```

> If `wiki_retrieve` returns the `_serialize`d dict under different keys, adjust the assertions to the actual shape (`grep -n "_serialize" src/gateway/mcp_server.py` and check an existing MCP test). Do not weaken the cross-domain intent.

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py::test_mcp_wiki_retrieve_accepts_domains -v`
Expected: FAIL — `TypeError: wiki_retrieve() got an unexpected keyword argument 'domains'`.

- [ ] **Step 3: Add `domains` to both MCP tools**

In `src/gateway/mcp_server.py`, `wiki_retrieve`: add `domains: str | None = None` after `domain`, parse it, and pass through:

```python
def wiki_retrieve(
    query: str,
    domain: str | None = None,
    domains: str | None = None,
    k: int = 12,
    budget_chars: int = 40_000,
    caller: str | None = None,
) -> dict[str, Any]:
```

Replace the body's `retrieve_op(...)` call:

```python
    from gateway.ops.retrieve import retrieve_op

    dom_list = [d.strip() for d in domains.split(",") if d.strip()] if domains else None
    return _serialize(
        retrieve_op(query, domain=domain, domains=dom_list,
                    k=k, budget_chars=budget_chars, caller=caller)
    )
```

`wiki_answer`: add `domains: str | None = None` after `domain` and mirror:

```python
def wiki_answer(
    question: str,
    domain: str | None = None,
    domains: str | None = None,
    k: int = 12,
    budget_chars: int = 40_000,
    file_draft: bool = False,
    caller: str | None = None,
) -> dict[str, Any]:
```

```python
    from gateway.ops.answer import answer_op

    dom_list = [d.strip() for d in domains.split(",") if d.strip()] if domains else None
    return _serialize(answer_op(
        question, domain=domain, domains=dom_list, k=k, budget_chars=budget_chars,
        file_draft=file_draft, caller=caller,
    ))
```

Add a one-line `domains:` note to each tool's docstring (comma-separated; precedence over `domain`).

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py::test_mcp_wiki_retrieve_accepts_domains -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/gateway/mcp_server.py tests/gateway/test_ws2_retrieve.py
git commit -m "feat(mcp): domains param on wiki_retrieve/wiki_answer

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 7: Golden-set guard + one live smoke test

**Files:** none (verification only).

- [ ] **Step 1: Run the retrieval golden-set comparison**

Run: `.venv/bin/wiki eval-retrieval --compare`
Expected: recall@5 ≥ 0.889, recall@10 ≥ 0.926, MRR ≥ 0.722 — i.e. NO regression. The single/global path is unchanged, so the expected delta is zero. If anything regressed, stop and investigate `_merge_domains` for accidental leakage into the single path.

- [ ] **Step 2: Full gateway test sweep**

Run: `.venv/bin/python -m pytest tests/gateway -q`
Expected: all PASS (no collateral breakage).

- [ ] **Step 3: One live cross-domain smoke test (single small LLM call — spend cap is live)**

Run:
```bash
.venv/bin/wiki answer "Is a reserve-study data collective feasible given pooled-data incentives?" \
  --domains data-collectives,condo-capital-infra --k 8
```
Expected: a grounded answer citing `[[sources/...]]` from BOTH domains (not a refusal, not single-domain). Do NOT pass `--file` here — this is a read-only smoke test; no draft is filed. Keep to this one call.

- [ ] **Step 4: No commit** (verification only).

---

## Task 8: Documentation

**Files:**
- Modify: `WIKI.md` (Gateway operations)
- Modify: `CLAUDE.md` (Retrieval ladder section)

- [ ] **Step 1: Document `--domains` in WIKI.md**

Find the `wiki retrieve` / `wiki answer` rows in `WIKI.md` § Gateway operations (`grep -n "wiki retrieve\|wiki answer" WIKI.md`). Add a sentence to each describing `--domains a,b`: "balanced cross-domain block via per-domain quota (ceil(k/N) each) + round-robin interleave; `--domains` takes precedence over `--domain`; `wiki answer --domains` files list-valued `domains:` frontmatter."

- [ ] **Step 2: Add the invariant note to CLAUDE.md**

In `CLAUDE.md` § "Retrieval ladder (RAG)", after the `wiki retrieve` bullet, add one line:

```markdown
   - **Cross-domain:** `wiki retrieve "<q>" --domains a,b` balances the block by per-domain quota (ceil(k/N) each, round-robin-interleaved) instead of a single global k-window that collapses toward the lexically-dominant domain. `wiki answer --domains a,b` files a page tagged to all named domains.
```

- [ ] **Step 3: Append to log.md (append-only)**

Add a single dated line to `log.md` noting the capability shipped (match the existing log line format — `grep -n "" log.md | tail -3` to see the format first).

- [ ] **Step 4: Commit**

```bash
git add WIKI.md CLAUDE.md log.md docs/superpowers/plans/2026-06-11-multi-domain-balanced-retrieval.md
git commit -m "docs: --domains multi-domain balanced retrieval (WIKI/CLAUDE/log)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Done criteria

- `wiki retrieve --domains a,b` returns sections from each named domain, balanced; dedups dual-tagged pages; balance survives budget truncation.
- `wiki answer --domains a,b --file` files a synthesis page tagged to all named domains with correct `sources_count`.
- `wiki eval-retrieval --compare` shows no regression (recall@5 0.889 / recall@10 0.926 / MRR 0.722).
- Full `tests/gateway` suite passes.
- WIKI.md, CLAUDE.md, log.md updated.
