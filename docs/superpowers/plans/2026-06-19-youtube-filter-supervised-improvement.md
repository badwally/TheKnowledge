# YouTube filter/prompt supervised-improvement — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a reusable `wiki filter-eval` subcommand that scores a YouTube candidate pool against human gold labels, then run it on `semantic-models` to produce a gold set and a measurable before/after precision@10 figure.

**Architecture:** A new gateway op (`src/gateway/ops/filter_eval.py`) with two modes. **Mode `pool`** runs the YouTube search + per-candidate filter scoring (no transcript fetch, no writes to `raw/`/`wiki/`) and emits a *blind* pool (for human labeling) plus a *scored* pool (for analysis). **Mode `score`** is a pure function over the scored pool + the user's labels that reports precision@10 and three disagreement buckets. The op reuses the existing research-pipeline internals (`_fan_out_search`, `gateway.filter.score`) through injectable seams so the network/model paths are stubbable in tests. CLI wiring follows the existing nested-subparser precedent (`wiki question new|list`).

**Tech Stack:** Python 3, argparse CLI (`src/gateway/cli.py`), `gateway.core.OperationResult`, `gateway.filter` (semantic filter + policy + example bank), `gateway.research` (search adapters + fan-out), pytest with dependency-injected stubs (no live network/model in unit tests). YAML for the queries/labels files, Markdown + JSON for pool artifacts.

## Global Constraints

- **Python env:** run everything via the gateway venv — `.venv/bin/python -m pytest`, `.venv/bin/wiki <subcommand>`. **The worktree has no `.venv`**; the executor must either symlink/point at the main repo's interpreter or create a venv in the worktree before running tests. Never use system `python` (it lacks the gateway package and yields misleading `ModuleNotFoundError`). (CLAUDE.md § Python environment; spec §11.)
- **No writes to `raw/` or `wiki/` from `filter-eval`.** It only reads candidates and writes scratch artifacts under an eval path. This keeps hard rule #1 intact and means no transcript fetch is invoked (spec §4).
- **Domain is a positional arg — vertical-agnostic.** No `semantic-models` string hardcoded in the op or CLI (spec §4, §10). The domain only appears as data in the queries/labels files and CLI invocations.
- **Scratch output path is NOT gitignored today.** `.knowledge/eval/` holds *tracked* golden sets (`.knowledge/eval/embedding/`, `.knowledge/eval/dedup/golden.yaml`). The plan adds `.knowledge/eval/filter/` to `.gitignore` (Task A1) so timestamped scratch pools don't pollute git status. Verify with `git check-ignore` before relying on it.
- **Mode `score` must be a pure function** over the scored pool + labels — no network, no adapter, no model call — and unit-tested in isolation (spec §4, contp).
- **YouTube adapter key idle precondition** for the *operational* Phase C only (the `pool` mode hits YouTube *search*). Do not run Phase C concurrently with another adapter-hitting research session (spec §11; analogous to `[[feedback_s2_shared_key_concurrency]]`). Phase A unit tests never hit the network.
- **Build discipline (gate):** independent reviewer ≠ author; adversarial tests with **named negative controls**; **realistic CandidateItem payloads** (full title/channel/description/`source_metadata`), never minimal stubs — minimal fixtures hide silent-corruption/inertness on transform paths (`[[feedback_inert_in_production_pattern]]`, `[[feedback_gate_tests_what_ships]]`). Read `docs/MULTI-AGENT-BUILD-PLAYBOOK.md` (on `main`, not this branch) before fanning out the build.

---

## File Structure

| File | Responsibility | Tasks |
|---|---|---|
| `.gitignore` | Add `.knowledge/eval/filter/` so scratch pools are untracked | A1 |
| `src/gateway/ops/filter_eval.py` | The op: `score_pool` (pure, Mode 2), `build_pool` (Mode 1), artifact writers (`write_blind_pool`, `write_scored_pool`), and the two op entrypoints (`pool_op`, `score_op`) returning `OperationResult` | A1–A3 |
| `src/gateway/cli.py` | Register `filter-eval` with nested `pool`/`score` subparsers; handler `_run_filter_eval_cmd`; dispatch line | A4 |
| `tests/gateway/test_filter_eval.py` | Unit tests for all of the above, using stub `search_fn` + stub `FilterClient` (no network/model) | A1–A4 |
| `docs/research/youtube-filter-sl/queries-train.yaml` | 8 train subtopics → YouTube query strings | B1 |
| `docs/research/youtube-filter-sl/queries-validate.yaml` | 4 held-out validate subtopics → query strings | B1 |
| `docs/research/youtube-filter-sl/prompts.md` | The 12 research prompts (8 train / 4 validate) + the planner's emitted `youtube:` queries captured per prompt | B1 |
| `docs/research/youtube-filter-sl/labels-train.yaml` | User's gold labels (10 best-fit URLs + per-subtopic missing flags) | C2 (user-authored) |
| `docs/research/youtube-filter-sl/results.md` | Before/after precision write-up + disagreement buckets + which lever each fix addressed | C5 |

---

## Phase A — `wiki filter-eval` subcommand (TDD, pure code)

Build order is dependency-driven: the **pure Mode-2 scorer first** (no deps, easiest to TDD — per the contp), then the Mode-1 pool builder (injectable seams), then artifact writers + op entrypoints, then CLI wiring.

### Task A1: gitignore + Mode-2 pure scorer (`score_pool`)

**Files:**
- Modify: `.gitignore` (add `.knowledge/eval/filter/`)
- Create: `src/gateway/ops/filter_eval.py`
- Test: `tests/gateway/test_filter_eval.py`

**Interfaces:**
- Consumes: nothing (pure function over plain dicts/lists).
- Produces: `score_pool(scored_pool: list[dict], labels: dict, *, k: int = 10) -> dict`. Each `scored_pool` item is a dict with at least `{"url": str, "title": str, "channel": str, "subtopic": str, "score": float, "tier": str}`. `labels` is `{"best_fit": list[str-urls], "missing": {subtopic: [str]}}`. Returns `{"precision_at_k": float, "k": int, "hits": list[str], "filter_false_positives": list[dict], "filter_false_negatives": list[dict], "query_coverage_gaps": dict, "label_warnings": list[str]}`.

- [ ] **Step 1: Add the gitignore entry**

Append to `.gitignore` (under the existing `.knowledge/` derived-state block):

```
# Filter-eval scratch pools (derived; golden sets elsewhere in .knowledge/eval are tracked)
.knowledge/eval/filter/
```

- [ ] **Step 2: Verify it is ignored**

Run: `git check-ignore -v .knowledge/eval/filter/x/pool-scored.json`
Expected: prints a `.gitignore:<line>:.knowledge/eval/filter/` match (non-empty output, exit 0).

- [ ] **Step 3: Write the failing test for `score_pool`**

```python
# tests/gateway/test_filter_eval.py
from gateway.ops import filter_eval


def _pool_item(url, score, *, subtopic="kg-construction", title=None, channel="ACME Talks"):
    return {
        "url": url,
        "item_id": "yt:" + url[-4:],
        "title": title or f"Talk {url[-4:]}",
        "channel": channel,
        "description": "A conference talk about knowledge graphs.",
        "subtopic": subtopic,
        "score": score,
        "tier": "accept" if score >= 0.7 else "review" if score >= 0.4 else "reject",
    }


def test_score_pool_precision_and_buckets():
    # 12 candidates, scores descending by url suffix number.
    pool = [_pool_item(f"https://yt/v{i:02d}", 0.95 - i * 0.05) for i in range(12)]
    # User's 10 best-fit: 8 of them are in the filter top-10 (v00..v09),
    # 2 are outside it (v10, v11 — filter false-negatives).
    best_fit = [f"https://yt/v{i:02d}" for i in range(8)] + ["https://yt/v10", "https://yt/v11"]
    labels = {"best_fit": best_fit, "missing": {"kg-construction": ["A keynote by X that is absent"]}}

    report = filter_eval.score_pool(pool, labels, k=10)

    assert report["k"] == 10
    assert report["precision_at_k"] == 0.8  # 8 of the user's 10 are in filter top-10
    # filter top-10 = v00..v09; user did NOT pick v08, v09 -> false positives
    fp_urls = {c["url"] for c in report["filter_false_positives"]}
    assert fp_urls == {"https://yt/v08", "https://yt/v09"}
    # user picked v10, v11 which are ranked 11th/12th -> false negatives
    fn_urls = {c["url"] for c in report["filter_false_negatives"]}
    assert fn_urls == {"https://yt/v10", "https://yt/v11"}
    assert report["query_coverage_gaps"] == {"kg-construction": ["A keynote by X that is absent"]}
    assert report["label_warnings"] == []


def test_score_pool_warns_when_best_fit_url_not_in_pool():
    pool = [_pool_item("https://yt/v00", 0.9)]
    labels = {"best_fit": ["https://yt/NOT-IN-POOL"], "missing": {}}
    report = filter_eval.score_pool(pool, labels, k=10)
    assert any("NOT-IN-POOL" in w for w in report["label_warnings"])


def test_score_pool_is_deterministic_under_score_ties():
    # Two candidates tie on score; ranking must break ties by url so the
    # top-k membership is stable (no nondeterministic precision).
    pool = [_pool_item("https://yt/vB", 0.5), _pool_item("https://yt/vA", 0.5)]
    pool += [_pool_item(f"https://yt/p{i}", 0.1) for i in range(20)]
    labels = {"best_fit": ["https://yt/vA"], "missing": {}}
    r1 = filter_eval.score_pool(pool, labels, k=1)
    r2 = filter_eval.score_pool(list(reversed(pool)), labels, k=1)
    assert r1["hits"] == r2["hits"]  # tie-break stable regardless of input order
```

- [ ] **Step 4: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter_eval.py -v`
Expected: FAIL — `AttributeError: module 'gateway.ops.filter_eval' has no attribute 'score_pool'` (module does not exist yet).

- [ ] **Step 5: Implement `score_pool`**

```python
# src/gateway/ops/filter_eval.py
"""`wiki filter-eval` — score a candidate pool against human gold labels.

Two modes:
  pool  — run YouTube search + per-candidate filter scoring (no transcript
          fetch, no writes to raw/ or wiki/); emit a blind pool (for the
          user to label) + a scored pool (for analysis).
  score — pure function over the scored pool + the user's labels; report
          precision@k and the three disagreement buckets.

Vertical-agnostic: domain is always a parameter, never hardcoded.
"""

from __future__ import annotations


def score_pool(scored_pool: list[dict], labels: dict, *, k: int = 10) -> dict:
    """Pure: precision@k + disagreement buckets. No I/O, no network.

    `scored_pool` items need at least {"url", "score"}; `labels` is
    {"best_fit": [url, ...], "missing": {subtopic: [str, ...]}}.
    Join key between labels and pool is the canonical `url`.
    """
    best_fit = list(labels.get("best_fit") or [])
    best_fit_set = set(best_fit)
    missing = labels.get("missing") or {}

    pool_urls = {c["url"] for c in scored_pool}
    label_warnings: list[str] = []
    for url in best_fit:
        if url not in pool_urls:
            label_warnings.append(
                f"best_fit url not present in scored pool (label error?): {url}"
            )
    if len(best_fit) != k:
        label_warnings.append(
            f"best_fit has {len(best_fit)} entries; precision@{k} denominator is {k}"
        )

    # Deterministic ranking: score desc, tie-break url asc.
    ranked = sorted(scored_pool, key=lambda c: (-float(c["score"]), c["url"]))
    top_k = ranked[:k]
    top_k_urls = {c["url"] for c in top_k}

    hits = best_fit_set & top_k_urls
    precision_at_k = len(hits) / k if k else 0.0

    false_positives = [c for c in top_k if c["url"] not in best_fit_set]
    false_negatives = [
        c for c in scored_pool
        if c["url"] in best_fit_set and c["url"] not in top_k_urls
    ]

    return {
        "precision_at_k": precision_at_k,
        "k": k,
        "hits": sorted(hits),
        "filter_false_positives": false_positives,
        "filter_false_negatives": false_negatives,
        "query_coverage_gaps": missing,
        "label_warnings": label_warnings,
    }
```

- [ ] **Step 6: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter_eval.py -v`
Expected: PASS (3 tests).

- [ ] **Step 7: Commit**

```bash
git add .gitignore src/gateway/ops/filter_eval.py tests/gateway/test_filter_eval.py
git commit -m "feat(filter-eval): Mode-2 pure precision scorer + gitignore scratch path"
```

---

### Task A2: Mode-1 pool builder (`build_pool`) with injectable seams

**Files:**
- Modify: `src/gateway/ops/filter_eval.py`
- Test: `tests/gateway/test_filter_eval.py`

**Interfaces:**
- Consumes: `gateway.research.adapters.base.CandidateItem`; `gateway.research.orchestrator._fan_out_search`; `gateway.research.adapters.enabled_adapters`; `gateway.filter.{load_policy, policy_exists, load_all, select, score as filter_score}`; `gateway.filter.semantic.{FilterClient, FilterError}`.
- Produces:
  - `FilterEvalError(RuntimeError)`.
  - `default_youtube_search(queries: list[str], *, max_results: int, session_id: str = "filter-eval") -> list[CandidateItem]` — the real network seam (youtube-only fan-out).
  - `build_pool(domain: str, queries_by_subtopic: dict[str, list[str]], *, max_results_per_query: int = 15, search_fn=None, filter_client: FilterClient | None = None) -> list[dict]` — returns the **scored pool** (list of dicts, the same shape `score_pool` consumes), one entry per deduped candidate, tagged with its `subtopic`, `score`, and `tier`. `search_fn(queries, *, max_results)` is the injectable search seam (defaults to `default_youtube_search`); `filter_client` is the injectable model seam (defaults to the real `ClaudeCLIFilterClient` inside `filter_score`).

- [ ] **Step 1: Write the failing test for `build_pool` (with stubs — no network/model)**

```python
# add to tests/gateway/test_filter_eval.py
from gateway.research.adapters.base import CandidateItem


def _yt_candidate(vid, title, channel, desc):
    # Realistic payload: full title/channel/description + source_metadata,
    # matching the real YouTubeAdapter shape (NOT a minimal stub).
    return CandidateItem(
        item_id=f"yt:{vid}",
        source_type="youtube",
        url=f"https://www.youtube.com/watch?v={vid}",
        title=title,
        authors=[channel],
        publish_date="2024-05-01T00:00:00Z",
        description=desc,
        content_type="video",
        source_metadata={"video_id": vid, "channel_name": channel, "view_count": 4200},
    )


class _StubFilterClient:
    """Returns a fixed score keyed by video title substring. No model call."""
    def __init__(self, scores_by_title):
        self._scores = scores_by_title

    # gateway.filter.semantic.score() falls back to .call(prompt) for
    # stubs that don't implement call_split. Return the rationale+score
    # text the parser expects.
    def call(self, prompt: str) -> str:
        for needle, sc in self._scores.items():
            if needle in prompt:
                return f"SCORE: {sc}\nRATIONALE: stub decision for {needle}"
        return "SCORE: 0.0\nRATIONALE: stub default"


def test_build_pool_scores_and_tags_every_candidate(tmp_path, monkeypatch):
    # Two subtopics; subtopic A surfaces a strong + a weak video, B a mid one.
    pool_by_subtopic = {
        "kg-construction": [
            _yt_candidate("AAA1", "Building Knowledge Graphs at Scale (KGC keynote)", "KGConf", "Keynote on KG construction pipelines."),
            _yt_candidate("AAA2", "10 SEO tricks for 2024", "GrowthHacks", "Clickbait marketing video."),
        ],
        "query-languages": [
            _yt_candidate("BBB1", "SPARQL 1.2 deep dive (Connected Data London)", "CDL", "Conference talk on SPARQL engines."),
        ],
    }

    def fake_search(queries, *, max_results):
        # The op calls search_fn once per subtopic; route by the query text.
        for sub, items in pool_by_subtopic.items():
            if any(sub in q for q in queries):
                return items
        return []

    stub_client = _StubFilterClient({
        "Building Knowledge Graphs": 0.9,
        "10 SEO tricks": 0.1,
        "SPARQL 1.2": 0.6,
    })

    # build_pool must NOT need a real policy file for these tests if we point
    # the domain at a fixture policy; reuse an existing test domain helper.
    # (See conftest: `semantic-models` policy exists in the repo.)
    scored = filter_eval.build_pool(
        "semantic-models",
        {"kg-construction": ["kg-construction talks"], "query-languages": ["query-languages talks"]},
        max_results_per_query=15,
        search_fn=fake_search,
        filter_client=stub_client,
    )

    by_url = {c["url"]: c for c in scored}
    assert len(scored) == 3  # all candidates scored, none dropped
    assert by_url["https://www.youtube.com/watch?v=AAA1"]["subtopic"] == "kg-construction"
    assert by_url["https://www.youtube.com/watch?v=AAA1"]["channel"] == "KGConf"
    assert by_url["https://www.youtube.com/watch?v=AAA1"]["tier"] == "accept"
    assert by_url["https://www.youtube.com/watch?v=AAA2"]["tier"] == "reject"
    assert by_url["https://www.youtube.com/watch?v=BBB1"]["subtopic"] == "query-languages"


def test_build_pool_dedups_across_subtopics_first_subtopic_wins():
    shared = _yt_candidate("DUP1", "Ontology alignment survey (ISWC)", "ISWC", "Survey talk.")

    def fake_search(queries, *, max_results):
        return [shared]  # same video surfaces for every subtopic query

    stub_client = _StubFilterClient({"Ontology alignment": 0.8})
    scored = filter_eval.build_pool(
        "semantic-models",
        {"alignment": ["alignment q"], "ontology-engineering": ["onto q"]},
        search_fn=fake_search,
        filter_client=stub_client,
    )
    assert len(scored) == 1  # deduped by url
    assert scored[0]["subtopic"] == "alignment"  # first subtopic in file order wins


def test_build_pool_raises_when_no_youtube_adapter(monkeypatch):
    # Negative control: the real default search path must fail loudly when
    # the youtube adapter is unavailable, not silently return an empty pool.
    monkeypatch.setattr(filter_eval, "enabled_adapters", lambda **_: [])
    import pytest
    with pytest.raises(filter_eval.FilterEvalError):
        filter_eval.default_youtube_search(["q"], max_results=5)
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter_eval.py -k build_pool -v`
Expected: FAIL — `AttributeError: module 'gateway.ops.filter_eval' has no attribute 'build_pool'`.

- [ ] **Step 3: Implement `build_pool`, `default_youtube_search`, `FilterEvalError`, and the tier helper**

```python
# add to src/gateway/ops/filter_eval.py (top-level imports)
from gateway.filter import (
    load_all,
    load_policy,
    policy_exists,
    score as filter_score,
    select,
)
from gateway.filter.policy import Policy
from gateway.filter.semantic import FilterClient, FilterError
from gateway.research.adapters import enabled_adapters
from gateway.research.adapters.base import CandidateItem
from gateway.research.orchestrator import _fan_out_search


class FilterEvalError(RuntimeError):
    """Raised when the eval cannot run (missing adapter, missing policy)."""


def _tier(score: float, policy: Policy) -> str:
    if score >= policy.threshold_include:
        return "accept"
    if score >= policy.threshold_review:
        return "review"
    return "reject"


def _front(item: CandidateItem, domain: str) -> dict:
    """Frontmatter-shaped dict for the filter prompt (mirrors
    orchestrator._candidate_front so scores match the live pipeline)."""
    return {
        "type": item.source_type,
        "title": item.title,
        "url": item.url,
        "authors": item.authors,
        "published_at": item.publish_date or "",
        "domains": [domain],
        "meta": dict(item.source_metadata or {}),
    }


def default_youtube_search(
    queries: list[str], *, max_results: int, session_id: str = "filter-eval"
) -> list[CandidateItem]:
    """Real network seam: youtube-only fan-out. Raises if the adapter is gone."""
    adapters = [a for a in enabled_adapters() if a.name == "youtube"]
    if not adapters:
        raise FilterEvalError(
            "youtube adapter unavailable (is YOUTUBE_API_KEY set?)"
        )
    return _fan_out_search(
        adapters,
        {"youtube": queries},
        max_results_per_adapter=max_results,
        session_id=session_id,
    )


def build_pool(
    domain: str,
    queries_by_subtopic: dict[str, list[str]],
    *,
    max_results_per_query: int = 15,
    search_fn=None,
    filter_client: FilterClient | None = None,
) -> list[dict]:
    """Run search per subtopic, dedup across subtopics (first wins), score
    every candidate. Returns the scored pool (the shape score_pool consumes)."""
    if not policy_exists(domain):
        raise FilterEvalError(f"no policy file for domain {domain!r}")
    policy = load_policy(domain)
    examples = select(load_all(domain), policy)
    search = search_fn or default_youtube_search

    seen: set[str] = set()
    tagged: list[tuple[str, CandidateItem]] = []  # (subtopic, item)
    for subtopic, queries in queries_by_subtopic.items():
        items = search(queries, max_results=max_results_per_query)
        for item in items:
            if item.url in seen:
                continue
            seen.add(item.url)
            tagged.append((subtopic, item))

    scored: list[dict] = []
    for subtopic, item in tagged:
        front = _front(item, domain)
        body_head = item.description or item.title
        try:
            result = filter_score(front, body_head, policy, examples, client=filter_client)
        except FilterError:
            # Score failures are recorded as reject-tier with score 0 so the
            # candidate stays visible in the pool rather than vanishing.
            scored.append(_pool_row(item, subtopic, 0.0, "reject"))
            continue
        scored.append(_pool_row(item, subtopic, result.score, _tier(result.score, policy)))
    return scored


def _pool_row(item: CandidateItem, subtopic: str, score: float, tier: str) -> dict:
    return {
        "item_id": item.item_id,
        "url": item.url,
        "title": item.title,
        "channel": (item.source_metadata or {}).get("channel_name", "")
                   or (item.authors[0] if item.authors else ""),
        "description": item.description,
        "subtopic": subtopic,
        "score": round(float(score), 4),
        "tier": tier,
    }
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter_eval.py -k build_pool -v`
Expected: PASS (3 tests). If the `_StubFilterClient.call` return format does not parse, read `gateway/filter/semantic.py` `score()` → its response parser and match the exact `SCORE:`/`RATIONALE:` shape it expects (verify before adjusting the stub — do not guess).

- [ ] **Step 5: Commit**

```bash
git add src/gateway/ops/filter_eval.py tests/gateway/test_filter_eval.py
git commit -m "feat(filter-eval): Mode-1 pool builder with injectable search + filter seams"
```

---

### Task A3: artifact writers + op entrypoints (`pool_op`, `score_op`)

**Files:**
- Modify: `src/gateway/ops/filter_eval.py`
- Test: `tests/gateway/test_filter_eval.py`

**Interfaces:**
- Consumes: `gateway.core.OperationResult`; `gateway.paths.knowledge_root`; `build_pool`/`score_pool` from Tasks A1–A2.
- Produces:
  - `write_blind_pool(scored: list[dict], path: Path, *, seed: int = 0) -> None` — Markdown grouped by subtopic, shuffled within group (seeded), **no scores**.
  - `write_scored_pool(scored: list[dict], path: Path) -> None` — JSON list (the analysis artifact).
  - `pool_op(domain, queries_by_subtopic, *, out_dir: Path, max_results_per_query=15, seed=0, search_fn=None, filter_client=None) -> OperationResult` (writes `pool-blind.md` + `pool-scored.json` under `out_dir`).
  - `score_op(scored_pool_path: Path, labels_path: Path, *, k=10) -> OperationResult` (loads JSON + YAML, calls `score_pool`, puts the formatted report in `OperationResult.summary`).
  - `default_out_dir(domain: str, timestamp: str) -> Path` → `.knowledge/eval/filter/<domain>/<timestamp>/` (caller supplies `timestamp`; the op never calls `datetime.now()` itself so it stays testable — the CLI handler stamps it).

- [ ] **Step 1: Write the failing tests for the writers + entrypoints**

```python
# add to tests/gateway/test_filter_eval.py
import json
import yaml
from pathlib import Path


def test_write_blind_pool_groups_by_subtopic_and_hides_scores(tmp_path):
    scored = [
        {"item_id": "yt:A", "url": "https://yt/A", "title": "Alpha talk", "channel": "C1",
         "description": "d", "subtopic": "kg-construction", "score": 0.9, "tier": "accept"},
        {"item_id": "yt:B", "url": "https://yt/B", "title": "Beta talk", "channel": "C2",
         "description": "d", "subtopic": "query-languages", "score": 0.2, "tier": "reject"},
    ]
    out = tmp_path / "pool-blind.md"
    filter_eval.write_blind_pool(scored, out, seed=0)
    text = out.read_text()
    assert "## kg-construction" in text and "## query-languages" in text
    assert "Alpha talk" in text and "https://yt/A" in text and "C1" in text
    assert "0.9" not in text and "accept" not in text  # NO scores/tiers leaked


def test_pool_op_writes_both_artifacts(tmp_path):
    def fake_search(queries, *, max_results):
        return [_yt_candidate("ZZ1", "Reasoning over ontologies (DL lecture)", "Uni", "OWL DL reasoning.")]
    stub = _StubFilterClient({"Reasoning over ontologies": 0.85})
    out = tmp_path / "run1"
    result = filter_eval.pool_op(
        "semantic-models",
        {"reasoning": ["reasoning q"]},
        out_dir=out,
        search_fn=fake_search,
        filter_client=stub,
    )
    assert result.success
    blind = out / "pool-blind.md"
    scored_json = out / "pool-scored.json"
    assert blind.exists() and scored_json.exists()
    data = json.loads(scored_json.read_text())
    assert data[0]["tier"] == "accept" and data[0]["subtopic"] == "reasoning"
    assert {Path(p) for p in result.paths_touched} >= {blind, scored_json}


def test_score_op_reports_precision(tmp_path):
    scored = [{"url": f"https://yt/v{i:02d}", "title": f"t{i}", "channel": "c",
               "description": "d", "subtopic": "s", "score": 0.9 - i * 0.05,
               "tier": "accept", "item_id": f"yt:{i}"} for i in range(12)]
    (tmp_path / "pool-scored.json").write_text(json.dumps(scored))
    labels = {"best_fit": [f"https://yt/v{i:02d}" for i in range(10)], "missing": {}}
    (tmp_path / "labels.yaml").write_text(yaml.safe_dump(labels))
    result = filter_eval.score_op(tmp_path / "pool-scored.json", tmp_path / "labels.yaml", k=10)
    assert result.success
    assert "precision@10" in result.summary
    assert "1.0" in result.summary or "1.00" in result.summary  # all 10 in top-10
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter_eval.py -k "blind_pool or pool_op or score_op" -v`
Expected: FAIL — missing `write_blind_pool` / `pool_op` / `score_op`.

- [ ] **Step 3: Implement the writers + entrypoints**

```python
# add to src/gateway/ops/filter_eval.py
import json
import random
from itertools import groupby
from pathlib import Path

import yaml

from gateway import paths
from gateway.core import OperationResult


def default_out_dir(domain: str, timestamp: str) -> Path:
    return paths.knowledge_root() / ".knowledge" / "eval" / "filter" / domain / timestamp


def write_scored_pool(scored: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(scored, indent=2, ensure_ascii=False))


def write_blind_pool(scored: list[dict], path: Path, *, seed: int = 0) -> None:
    """Markdown grouped by subtopic, shuffled within group, NO scores/tiers."""
    path.parent.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed)
    lines = ["# Blind candidate pool", "",
             "Pick the 10 best-fit videos overall (across subtopics). Per subtopic,",
             "note any 'expected but missing' talks/channels. Scores are hidden.", ""]
    # Preserve subtopic file order; shuffle within each subtopic.
    ordered_subtopics = list(dict.fromkeys(c["subtopic"] for c in scored))
    for sub in ordered_subtopics:
        group = [c for c in scored if c["subtopic"] == sub]
        rng.shuffle(group)
        lines.append(f"## {sub}")
        lines.append("")
        for c in group:
            lines.append(f"- **{c['title']}** — {c['channel']}")
            lines.append(f"  - {c['url']}")
            desc = (c.get("description") or "").strip().replace("\n", " ")
            if desc:
                lines.append(f"  - {desc[:300]}")
        lines.append("")
    path.write_text("\n".join(lines))


def pool_op(
    domain: str,
    queries_by_subtopic: dict[str, list[str]],
    *,
    out_dir: Path,
    max_results_per_query: int = 15,
    seed: int = 0,
    search_fn=None,
    filter_client: FilterClient | None = None,
) -> OperationResult:
    try:
        scored = build_pool(
            domain, queries_by_subtopic,
            max_results_per_query=max_results_per_query,
            search_fn=search_fn, filter_client=filter_client,
        )
    except FilterEvalError as e:
        return OperationResult(success=False, errors=[str(e)])
    if not scored:
        return OperationResult(success=True, no_op=True,
                               summary="no candidates returned for any subtopic")
    blind = out_dir / "pool-blind.md"
    scored_json = out_dir / "pool-scored.json"
    write_scored_pool(scored, scored_json)
    write_blind_pool(scored, blind, seed=seed)
    n_accept = sum(1 for c in scored if c["tier"] == "accept")
    return OperationResult(
        success=True,
        paths_touched=[blind, scored_json],
        summary=(f"pool: {len(scored)} candidates across "
                 f"{len({c['subtopic'] for c in scored})} subtopics "
                 f"({n_accept} accept-tier). Label {blind.name}, then "
                 f"`wiki filter-eval score {domain} --scored {scored_json.name} --labels <labels.yaml>`"),
    )


def score_op(scored_pool_path: Path, labels_path: Path, *, k: int = 10) -> OperationResult:
    try:
        scored = json.loads(Path(scored_pool_path).read_text())
        labels = yaml.safe_load(Path(labels_path).read_text()) or {}
    except (OSError, json.JSONDecodeError, yaml.YAMLError) as e:
        return OperationResult(success=False, errors=[f"load inputs: {e}"])
    report = score_pool(scored, labels, k=k)
    return OperationResult(success=True, summary=_format_report(report))


def _format_report(report: dict) -> str:
    k = report["k"]
    out = [f"precision@{k} = {report['precision_at_k']:.2f}  "
           f"({len(report['hits'])}/{k} of the user's best-fit in filter top-{k})"]
    out.append(f"  filter false-positives (in top-{k}, not user-picked): "
               + ", ".join(c["url"] for c in report["filter_false_positives"]) or "  (none)")
    out.append(f"  filter false-negatives (user-picked, ranked outside top-{k}): "
               + ", ".join(c["url"] for c in report["filter_false_negatives"]) or "  (none)")
    gaps = report["query_coverage_gaps"]
    out.append("  query-coverage gaps: "
               + (", ".join(f"{s}: {len(v)}" for s, v in gaps.items()) if gaps else "(none)"))
    for w in report["label_warnings"]:
        out.append(f"  WARNING: {w}")
    return "\n".join(out)
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter_eval.py -v`
Expected: PASS (all Phase-A unit tests so far).

- [ ] **Step 5: Commit**

```bash
git add src/gateway/ops/filter_eval.py tests/gateway/test_filter_eval.py
git commit -m "feat(filter-eval): artifact writers + pool_op/score_op entrypoints"
```

---

### Task A4: CLI registration (`wiki filter-eval pool|score`)

**Files:**
- Modify: `src/gateway/cli.py` (SUBCOMMANDS dict; new subparser block; handler `_run_filter_eval_cmd`; dispatch line)
- Test: `tests/gateway/test_filter_eval.py`

**Interfaces:**
- Consumes: `pool_op`, `score_op`, `default_out_dir` from Task A3; `_emit_result` (existing in `cli.py`).
- Produces: CLI surface `wiki filter-eval pool <domain> --queries <path> [--max-results N] [--out <dir>] [--seed N]` and `wiki filter-eval score <domain> --scored <path> --labels <path> [--k N]`.

- [ ] **Step 1: Write a failing CLI test (argparse wiring + dispatch)**

```python
# add to tests/gateway/test_filter_eval.py
from gateway import cli


def test_cli_filter_eval_score_end_to_end(tmp_path, capsys):
    scored = [{"url": f"https://yt/v{i:02d}", "title": f"t{i}", "channel": "c",
               "description": "d", "subtopic": "s", "score": 0.9 - i * 0.05,
               "tier": "accept", "item_id": f"yt:{i}"} for i in range(12)]
    (tmp_path / "pool-scored.json").write_text(json.dumps(scored))
    labels = {"best_fit": [f"https://yt/v{i:02d}" for i in range(10)], "missing": {}}
    (tmp_path / "labels.yaml").write_text(yaml.safe_dump(labels))
    rc = cli.main([
        "filter-eval", "score", "semantic-models",
        "--scored", str(tmp_path / "pool-scored.json"),
        "--labels", str(tmp_path / "labels.yaml"),
    ])
    assert rc == 0
    assert "precision@10" in capsys.readouterr().out


def test_cli_filter_eval_pool_parses_queries_file(tmp_path, monkeypatch):
    qfile = tmp_path / "queries.yaml"
    qfile.write_text(yaml.safe_dump({"subtopics": {"reasoning": ["reasoning talk"]}}))

    def fake_search(queries, *, max_results):
        return [_yt_candidate("Q1", "Reasoning lecture", "Uni", "desc")]
    monkeypatch.setattr(filter_eval, "default_youtube_search", fake_search)
    # Force a deterministic stub model so no live call happens.
    monkeypatch.setattr(filter_eval, "build_pool",
                        lambda *a, **k: [filter_eval._pool_row(_yt_candidate("Q1","Reasoning lecture","Uni","desc"),"reasoning",0.8,"accept")])
    rc = cli.main(["filter-eval", "pool", "semantic-models",
                   "--queries", str(qfile), "--out", str(tmp_path / "out")])
    assert rc == 0
    assert (tmp_path / "out" / "pool-scored.json").exists()
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter_eval.py -k cli -v`
Expected: FAIL — argparse exits with "invalid choice: 'filter-eval'" (subcommand not registered).

- [ ] **Step 3: Register the subcommand**

In `src/gateway/cli.py`, add to the `SUBCOMMANDS` dict (near line 49, alongside `"filter-correct"`):

```python
    "filter-eval": "Score a candidate pool against human gold labels (pool | score)",
```

After the `filter-correct` parser block (around line 276), add the nested-subparser block (mirror the `question` precedent at lines 637–672):

```python
    # filter-eval: supervised filter/prompt improvement loop (pool | score)
    p_feval = subparsers.add_parser(
        "filter-eval",
        help=SUBCOMMANDS["filter-eval"],
        epilog=(
            "Examples:\n"
            "  wiki filter-eval pool semantic-models --queries docs/research/youtube-filter-sl/queries-train.yaml\n"
            "  wiki filter-eval score semantic-models --scored pool-scored.json --labels labels-train.yaml"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p_feval_sub = p_feval.add_subparsers(dest="filter_eval_action", required=True)

    p_feval_pool = p_feval_sub.add_parser("pool", help="Generate + score a candidate pool from a queries file")
    p_feval_pool.add_argument("domain", help="Domain slug (e.g. semantic-models)")
    p_feval_pool.add_argument("--queries", required=True, help="YAML: {subtopics: {name: [query, ...]}}")
    p_feval_pool.add_argument("--max-results", type=int, default=15, dest="max_results",
                              help="Per-query YouTube candidate cap (default 15)")
    p_feval_pool.add_argument("--out", default=None, help="Output dir (default .knowledge/eval/filter/<domain>/<ts>/)")
    p_feval_pool.add_argument("--seed", type=int, default=0, help="Blind-pool shuffle seed (default 0)")

    p_feval_score = p_feval_sub.add_parser("score", help="Score the filter against gold labels")
    p_feval_score.add_argument("domain", help="Domain slug (for reporting context)")
    p_feval_score.add_argument("--scored", required=True, help="Path to pool-scored.json")
    p_feval_score.add_argument("--labels", required=True, help="Path to labels YAML")
    p_feval_score.add_argument("--k", type=int, default=10, help="precision@k cutoff (default 10)")
```

- [ ] **Step 4: Add the handler + dispatch line**

Add the dispatch line in the `ns.subcommand == ...` chain (near line 1451, after `filter-correct`):

```python
    if ns.subcommand == "filter-eval":
        return _run_filter_eval_cmd(ns)
```

Add the handler function (near the other `_run_*` handlers):

```python
def _run_filter_eval_cmd(ns: argparse.Namespace) -> int:
    import datetime as _dt
    import yaml as _yaml
    from pathlib import Path as _Path
    from gateway.ops import filter_eval

    action = ns.filter_eval_action
    if action == "pool":
        try:
            spec = _yaml.safe_load(_Path(ns.queries).read_text()) or {}
        except (OSError, _yaml.YAMLError) as e:
            print(f"error: read queries file: {e}", file=sys.stderr)
            return 2
        queries_by_subtopic = spec.get("subtopics") or {}
        if not queries_by_subtopic:
            print("error: queries file has no `subtopics:` mapping", file=sys.stderr)
            return 2
        if ns.out:
            out_dir = _Path(ns.out)
        else:
            ts = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")  # stamped here, not in the op
            out_dir = filter_eval.default_out_dir(ns.domain, ts)
        return _emit_result(filter_eval.pool_op(
            ns.domain, queries_by_subtopic,
            out_dir=out_dir, max_results_per_query=ns.max_results, seed=ns.seed,
        ))

    if action == "score":
        return _emit_result(filter_eval.score_op(
            _Path(ns.scored), _Path(ns.labels), k=ns.k,
        ))

    print(f"error: unknown filter-eval action: {action}", file=sys.stderr)
    return 2
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/gateway/test_filter_eval.py -v`
Expected: PASS (all Phase-A tests). The `pool` CLI test monkeypatches `build_pool` so no live search/model runs.

- [ ] **Step 6: Run the full gateway suite — no regressions**

Run: `.venv/bin/python -m pytest tests/gateway/ -q`
Expected: PASS at the prior baseline + the new `test_filter_eval.py` tests. If any unrelated test fails, it is a pre-existing flake only if it also fails on a clean `exp/youtube-filter-supervised` checkout — confirm before dismissing.

- [ ] **Step 7: Verify the CLI surfaces in `--help`**

Run: `.venv/bin/wiki filter-eval --help` and `.venv/bin/wiki filter-eval pool --help`
Expected: both print usage with the documented flags (no traceback).

- [ ] **Step 8: Commit**

```bash
git add src/gateway/cli.py tests/gateway/test_filter_eval.py
git commit -m "feat(filter-eval): CLI registration (pool|score) + handler + dispatch"
```

---

### Phase A gate (independent review ≠ author)

- [ ] Dispatch an independent reviewer subagent (reviewer ≠ implementer) with the **inert-in-production hunt list** (`docs/MULTI-AGENT-BUILD-PLAYBOOK.md`). Specifically verify, against real-data behavior:
  - `build_pool` actually scores **every** candidate (accept/review/reject all present), not just accept-tier — confirm with a payload containing a known reject (the `10 SEO tricks` negative control).
  - The blind pool **never** leaks scores/tiers (the `0.9 not in text` assertion is a real gate, not tautological).
  - Dedup is keyed on `url` and first-subtopic-wins (transform-path correctness with a realistic shared-video payload, not a minimal stub).
  - `score_pool` tie-break is deterministic (negative control: reversed input → same `hits`).
  - The youtube-adapter-missing path raises `FilterEvalError` (loud failure), not a silent empty pool.
- [ ] Fix any blocking findings TDD (RED before GREEN), re-review, then proceed.

---

## Phase B — prompt set + queries files

### Task B1: author the 12 prompts (8 train / 4 validate) + queries files

**Files:**
- Create: `docs/research/youtube-filter-sl/prompts.md`
- Create: `docs/research/youtube-filter-sl/queries-train.yaml`
- Create: `docs/research/youtube-filter-sl/queries-validate.yaml`

**Interfaces:**
- Consumes: the `wiki filter-eval pool --queries` file shape `{subtopics: {name: [query, ...]}}`.
- Produces: 8 train + 4 validate subtopic→query mappings; validate held out from all tuning (spec §5, §9).

- [ ] **Step 1: Choose the 12 subtopics** (spec §5 list): **train (8)** — KG construction; query languages/engines; reasoning/inference; SHACL/shape validation; storage architectures; KG embeddings; ontology engineering methodologies; the semantic layer. **validate (4, held out)** — ontology design patterns; alignment/matching; upper/foundational ontologies; OBDA. (Foundational formalisms folds into reasoning/inference.) If a subtopic is thin, swap from the spec's full candidate list — but keep the 8/4 split and never reuse a validate subtopic in training.

- [ ] **Step 2: Write the prompts + capture the planner's YouTube queries.** For each of the 12, write the research prompt, then derive its `youtube:` queries. Use the **institution / conference / researcher-anchored register** the YouTube-aware filter fix established (KGC, ISWC, Connected Data London, Stanford, NeurIPS, named researchers), not tutorial register (`[[feedback_filter_source_type_awareness]]`). Optionally capture the live planner output via `wiki research "<prompt>" --domain semantic-models --review` (writes the query plan only, no fan-out — returns at `orchestrator.py:1167`), then copy the emitted `youtube:` queries into the queries file. Validate `wiki research --review` does not consume YouTube quota before relying on it.

- [ ] **Step 3: Write `queries-train.yaml`** — 8 subtopics, ~2–4 queries each, targeting ~12 candidates/subtopic after dedup → ~100-item pool (spec §6). Shape:

```yaml
subtopics:
  kg-construction:
    - "knowledge graph construction KGC keynote"
    - "building enterprise knowledge graphs conference talk"
  query-languages:
    - "SPARQL engine internals Connected Data London"
    - "graph query language lecture"
  # ... 6 more train subtopics
```

- [ ] **Step 4: Write `queries-validate.yaml`** — the 4 held-out subtopics, same shape (target ~50-item validate pool, spec §9).

- [ ] **Step 5: Commit** (these are docs, not code — no test cycle):

```bash
git add docs/research/youtube-filter-sl/
git commit -m "docs(filter-eval): 12 semantic-models prompts + train/validate query files"
```

---

## Phase C — run → label → derive → validate (operational, checkpointed)

> **Preconditions (spec §11):** YouTube adapter key idle — no concurrent live research session. Use `.venv/bin/wiki` only. These tasks hit the live YouTube search API and the filter model; they are **not** unit tests. Each ends with a human-in-the-loop checkpoint.

### Task C1: generate the train pool

- [ ] Run: `.venv/bin/wiki filter-eval pool semantic-models --queries docs/research/youtube-filter-sl/queries-train.yaml --max-results 15`
- [ ] Confirm the pool size lands near ~100 after dedup. If far under, raise `--max-results` (spec §6) and re-run. Note the scratch dir printed in the `touched:` lines.
- [ ] Hand `pool-blind.md` to the user for labeling. **STOP — checkpoint:** the user labels the exact pool this run produced (no independent re-run — spec §12 nondeterminism control).

### Task C2: collect labels + score the filter (train)

- [ ] User authors `docs/research/youtube-filter-sl/labels-train.yaml`:

```yaml
best_fit:            # exactly 10 best-fit video URLs, copied from pool-blind.md
  - https://www.youtube.com/watch?v=...
  # ... 10 total
missing:             # per-subtopic "expected but absent" flags (or [] = "coverage complete")
  kg-construction:
    - "Expected a KGC 2023 keynote by <name>, absent from pool"
  query-languages: []
```

- [ ] Run: `.venv/bin/wiki filter-eval score semantic-models --scored <scratch>/pool-scored.json --labels docs/research/youtube-filter-sl/labels-train.yaml`
- [ ] Record **precision@10 (train, before)** + the three buckets. Copy `labels-train.yaml` into `docs/` as the durable gold set (spec §10). Resolve any `label_warnings` (e.g. a best-fit URL not in the pool = a copy error) before trusting the number.

### Task C3: derive + apply improvements

Map each disagreement bucket to its lever (spec §8):

- [ ] **Filter false-positives** → add negative examples + tighten `exclusion_criteria` / negative quality signals in `.knowledge/policies/semantic-models/policy.yaml`.
- [ ] **Filter false-negatives** → add positive examples + strengthen `inclusion_criteria` / positive quality signals.
- [ ] **Query-coverage gaps** → revise the `query_planner` YouTube register (institution/conference/researcher templates) and/or the prompt wording for the affected subtopics.
- [ ] **KNOWN FRICTION — resolve before invoking `wiki filter-correct`:** `wiki filter-correct <source_id> --include/--exclude` operates on an **ingested** source (a `yt-<id>` page in the wiki), but the pool candidates are **not** ingested (filter-eval writes nothing to `raw/`). Two valid resolutions — pick one and record it: (a) ingest the specific labeled best-fit + false-positive videos first (`wiki ingest --force-include`) so `filter-correct` has real `source_id`s to pin; or (b) append examples directly to the example bank via the example-pinning path (`gateway.filter.examples.pin`) / `wiki backfill-examples`, bypassing `filter-correct`. Do **not** assume `filter-correct` works on un-ingested URLs.
- [ ] All changes land via PR (gateway-authored where an op exists; `policy.yaml` edits minimal + reviewed — spec §8).

### Task C4: held-out validation

- [ ] Run: `.venv/bin/wiki filter-eval pool semantic-models --queries docs/research/youtube-filter-sl/queries-validate.yaml --max-results 15` **with the improvements applied** (~50-item validate pool).
- [ ] User does a lighter judgment on the new filter top-k → `labels-validate.yaml`.
- [ ] Run `wiki filter-eval score` on the validate pool → **precision@10 (validate, before vs after on data not used for tuning)** (spec §9 — guards against overfitting the 10 train labels).

### Task C5: results write-up

- [ ] Create `docs/research/youtube-filter-sl/results.md`: precision@10 train (before→after), precision@10 validate (before→after), the disagreement buckets, and which lever each fix addressed (spec §10). Keep claims qualitative ("precision moved X→Y on held-out"), not statistical — the gold set is only 10 labels (spec §12).
- [ ] Commit the write-up + gold set.

---

## Deliverables checklist (spec §10)

- [ ] `wiki filter-eval` subcommand — op + CLI + tests (Phase A). **The durable artifact.**
- [ ] Gold set (`labels-train.yaml` + `labels-validate.yaml` + missing-flags) under `docs/research/youtube-filter-sl/`.
- [ ] `policy.yaml` + example-bank + `query_planner` changes (PR).
- [ ] Results write-up (`results.md`): precision@10 train + validate, before/after, buckets, levers.

## Self-review notes (spec coverage)

- §1 goal / §10 deliverables → Phase A (subcommand) + C5 (precision figure + write-up). ✓
- §2 non-goals (NLM under-attribution, transcript throttle, resurrecting drafts) → explicitly out; the op does no transcript fetch (Global Constraints). ✓
- §3 two levers → C3 maps false-pos/neg to the filter lever, coverage gaps to the query lever. ✓
- §4 two-mode interface, no transcript fetch, no `raw/`/`wiki/` writes, standard op pattern, domain positional, Mode-2 pure → Tasks A1–A4. ✓
- §5 12 prompts 8/4 split → Task B1. ✓
- §6 pool generation, blind grouped+shuffled / scored artifacts → Tasks A2–A3, C1. ✓
- §7 precision@10 + buckets → Task A1 (`score_pool`). ✓
- §8 improvement levers + (resolved) filter-correct friction → C3. ✓
- §9 held-out validation → C4. ✓
- §11 preconditions (key idle, venv) → Global Constraints + Phase C preamble. ✓
- §12 risks (small gold set, nondeterminism via shared pool, overfitting) → C2 checkpoint, C4 held-out, C5 qualitative claims. ✓
