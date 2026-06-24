# Hole 2 — Hybrid Retrieval Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a local neural-embedding dense retriever, fused with BM25 (RRF), to `wiki retrieve` so paraphrased/lay queries find the right page — lifting the `semantic_mismatch` probe from recall@10 0.381 toward ~0.85+ without regressing lexical-easy retrieval or the dedup/merge-map gates.

**Architecture:** A *separate* neural embedding index (own db path, own encoder) serves the retrieve path only; the existing lexical `EmbeddingIndex` (entity/question/section-for-lint) is byte-unchanged so the Phase-3 merge-map gate and fragmentation lint stay stable. `retrieve()` gains a hybrid path: BM25 candidates (existing `search_fts`) ∪ dense candidates (`nn("section", query, k)`) fused by Reciprocal Rank Fusion, then assembled by the existing Hole-1 block builder (placeholder gate + `draft="true"` + budget). Encoder, dimension, fusion constant, and an optional rerank stage are config so a bake-off can sweep them and the winner gets locked.

**Tech Stack:** Python 3.11, numpy, SQLite (existing `embedding_index.py`), the existing FTS5 index (`search_index.py`). Local neural encoder via MLX (`mlx-community` Qwen3-Embedding builds) with a GGUF/llama.cpp alternative; both local. Tests use a deterministic stub encoder — **no model download in CI**.

**Spec:** `docs/260624_hole2-hybrid-retrieval-design.md`. **Source-of-truth interfaces** (verified 2026-06-24): `Encoder` Protocol = `model_version: str`, `dim: int`, `embed(texts: Sequence[str]) -> list[list[float]]`; `EmbeddingIndex(encoder, db_path)`; `EmbeddingIndex.nn(namespace, text, k=5) -> list[NNHit(key, distance)]`; section key format = `f"{rel_path}#{heading}"`; `NAMESPACES = ("section","entity","question")`; `search_index.search_fts(...) -> list[IndexHit]` (fields: `rel_path, slug, title, page_type, domain, heading, snippet, score, rank, inbound_count, draft, last_updated, trust`); `search_index.section_text(rel_path, heading) -> str`; `retrieve()` lives at `src/gateway/ops/retrieve.py`.

## Global Constraints

- **Python interpreter:** always `.venv/bin/python` / `.venv/bin/pytest` (never system python). The worktree venv is `uv`-created.
- **No direct writes to `wiki/` or `raw/`** — gateway-only hard rule. This work is `src/gateway` + `docs` + eval fixtures + a derived index. Fine.
- **Local-on-ingest:** no hosted API on ingest or query. Neural model runs locally (MLX/GGUF). Model weights are a one-time local download, never a runtime API call.
- **Second encoder, retrieve-path only:** do NOT change the encoder of the existing `EmbeddingIndex` / the `entity` or `question` namespaces. The Phase-3 dedup/merge-map gates are calibrated to `lexical-fallback-v1` and MUST NOT move.
- **Derived index:** the neural retrieval index is gitignored, self-healing, rebuildable. Markdown stays canonical.
- **CI must not require a model download:** every unit test uses a deterministic stub encoder. Real-model runs are local opt-in (the bake-off + calibration), never CI-gated.
- **Pre-merge gate must hold:** `.venv/bin/python -m gateway.scripts.gate` — full suite + fast tiers + `eval-retrieval` recall@10 ≥ 0.90 (easy goldens) + merge-map 0 regressions + embedding namespaces OK + scoped lints at baseline.
- **Branch:** `feat/hole2-hybrid-retrieval` (off main post-Hole-1). Verify `git branch --show-current` before any commit. Never commit to main; merge via push + PR.
- **Hole-1 invariants preserved:** every assembled block keeps the placeholder-section gate (zero `_(needs population…)_`) and `draft="true"` annotation; finalized pages not displaced.

---

## Phase A — Neural encoder + dedicated retrieval index

### Task A1: Stub + neural `Encoder` implementations behind the Protocol

**Files:**
- Create: `src/gateway/retrieval_encoder.py`
- Test: `tests/gateway/test_retrieval_encoder.py`

**Interfaces:**
- Consumes: `gateway.embedding_index.Encoder` (Protocol: `model_version: str`, `dim: int`, `embed(texts) -> list[list[float]]`).
- Produces:
  - `StubRetrievalEncoder(dim: int = 256, model_version: str = "stub-retrieval-v1")` — deterministic, L2-normalized, used by ALL unit tests.
  - `MlxQwen3Encoder(model_id: str, dim: int)` — lazy-loading MLX neural encoder (real model; never instantiated in CI).
  - `retrieval_encoder() -> Encoder` — factory reading env `WIKI_RETRIEVAL_ENCODER` (`"stub"` default in tests via monkeypatch; `"mlx:<model_id>:<dim>"` in production).

- [ ] **Step 1: Write the failing test for the stub encoder contract**

```python
# tests/gateway/test_retrieval_encoder.py
import numpy as np
from gateway.embedding_index import Encoder
from gateway.retrieval_encoder import StubRetrievalEncoder


def test_stub_encoder_satisfies_protocol_and_is_deterministic():
    enc = StubRetrievalEncoder(dim=256)
    assert isinstance(enc, Encoder)            # runtime_checkable Protocol
    assert enc.dim == 256 and enc.model_version
    v1 = enc.embed(["hello world"])[0]
    v2 = enc.embed(["hello world"])[0]
    assert v1 == v2                            # deterministic
    assert len(v1) == 256
    assert abs(float(np.linalg.norm(v1)) - 1.0) < 1e-5   # L2-normalized


def test_stub_encoder_paraphrase_closer_than_unrelated():
    enc = StubRetrievalEncoder(dim=256)
    import numpy as np
    a, b, c = (np.asarray(enc.embed([t])[0]) for t in
               ["central bank selling bonds", "central bank sells bonds", "banana bread recipe"])
    assert float(a @ b) > float(a @ c)         # paraphrase nearer than unrelated
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_retrieval_encoder.py -q`
Expected: FAIL — `ModuleNotFoundError: gateway.retrieval_encoder`.

- [ ] **Step 3: Implement the stub encoder (reuse the lexical hashing so paraphrases land near)**

```python
# src/gateway/retrieval_encoder.py
"""Encoders for the dense RETRIEVE path (Hole 2). Separate from the lexical
EmbeddingIndex encoder so dedup/demand/merge-map gates stay on lexical-fallback-v1.

CI uses StubRetrievalEncoder (deterministic, no model download). Production uses a
local neural encoder (MLX/GGUF) selected by WIKI_RETRIEVAL_ENCODER.
"""
from __future__ import annotations

import os
from typing import Sequence

from gateway.embedding_index import LexicalFallbackEncoder


class StubRetrievalEncoder(LexicalFallbackEncoder):
    """Deterministic stand-in for the neural encoder in tests. Reuses the lexical
    hashing (paraphrase-tolerant, L2-normalized) at a configurable dim."""

    def __init__(self, dim: int = 256, model_version: str = "stub-retrieval-v1"):
        self.dim = dim
        self.model_version = model_version


class MlxQwen3Encoder:
    """Local MLX Qwen3-Embedding encoder. Lazy-loads weights on first embed().
    Never instantiated in CI (no model download)."""

    def __init__(self, model_id: str, dim: int):
        self.model_id = model_id
        self.dim = dim
        self.model_version = f"mlx:{model_id}:{dim}"
        self._model = None

    def _ensure(self):
        if self._model is None:
            from mlx_embeddings import load  # local dep, installed only where the model runs
            self._model = load(self.model_id)

    def embed(self, texts: Sequence[str]) -> list[list[float]]:
        import numpy as np
        self._ensure()
        raw = self._model.encode(list(texts))           # (n, native_dim)
        arr = np.asarray(raw, dtype="float32")[:, : self.dim]   # Matryoshka truncate
        norms = np.linalg.norm(arr, axis=1, keepdims=True)
        arr = arr / np.clip(norms, 1e-12, None)
        return arr.tolist()


def retrieval_encoder():
    """Factory: env WIKI_RETRIEVAL_ENCODER selects the encoder.
    'stub' (default) | 'mlx:<model_id>:<dim>'. Mock in tests via monkeypatch."""
    spec = os.environ.get("WIKI_RETRIEVAL_ENCODER", "stub")
    if spec == "stub":
        return StubRetrievalEncoder()
    if spec.startswith("mlx:"):
        _, model_id, dim = spec.split(":", 2)
        return MlxQwen3Encoder(model_id, int(dim))
    raise ValueError(f"unknown WIKI_RETRIEVAL_ENCODER: {spec!r}")
```

- [ ] **Step 4: Run to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_retrieval_encoder.py -q`
Expected: PASS (2 tests).

- [ ] **Step 5: Commit**

```bash
git add src/gateway/retrieval_encoder.py tests/gateway/test_retrieval_encoder.py
git commit -m "feat(rag): retrieval encoder Protocol impls (stub + MLX Qwen3)"
```

### Task A2: Dedicated neural retrieval index (separate db path)

**Files:**
- Modify: `src/gateway/paths.py` (add `retrieval_embedding_db_path()`)
- Create: `src/gateway/retrieval_index.py`
- Test: `tests/gateway/test_retrieval_index.py`

**Interfaces:**
- Consumes: `EmbeddingIndex(encoder, db_path)`, `EmbeddingIndex.nn`, `EmbeddingIndex.rebuild_from_canonical`, `retrieval_encoder()` (A1).
- Produces:
  - `retrieval_index() -> EmbeddingIndex` — an `EmbeddingIndex` bound to the neural encoder + a SEPARATE `retrieval_embedding_db_path()`. The existing `EmbeddingIndex()` (lexical) is untouched.
  - `dense_section_hits(query: str, k: int) -> list[tuple[str, str, float]]` — returns `(rel_path, heading, distance)` for the top-k section neighbors (parses the `rel_path#heading` key).

- [ ] **Step 1: Write the failing test (separate db, section NN over a tiny corpus)**

```python
# tests/gateway/test_retrieval_index.py
from pathlib import Path
import pytest
from gateway import paths, search_index, frontmatter as fm
from gateway.retrieval_index import retrieval_index, dense_section_hits


def _page(slug, body, draft=False):
    d = paths.wiki_dir() / "concepts"; d.mkdir(parents=True, exist_ok=True)
    front = {"type": "concept", "slug": slug, "title": slug, "domains": ["d"],
             "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z"}
    if draft: front["draft"] = True
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


def test_retrieval_index_uses_separate_db(kb_root: Path):
    idx = retrieval_index()
    assert idx._db_path == paths.retrieval_embedding_db_path()
    assert idx._db_path != paths.embedding_db_path()    # NOT the lexical index db


def test_dense_section_hits_finds_paraphrase_match(kb_root: Path):
    _page("vagal", "## Mechanism\n\nThe drug slows stomach emptying via the vagus nerve.\n")
    _page("noise", "## Other\n\nUnrelated content about quarterly tax filing.\n")
    retrieval_index().rebuild_from_canonical()
    hits = dense_section_hits("delays gastric emptying through vagal signaling", k=5)
    assert hits, "expected dense neighbors"
    assert any(rel.endswith("vagal.md") for rel, _heading, _dist in hits)
    assert all(isinstance(d, float) for _r, _h, d in hits)
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_retrieval_index.py -q`
Expected: FAIL — `ModuleNotFoundError: gateway.retrieval_index` (and no `retrieval_embedding_db_path`).

- [ ] **Step 3: Add the path**

```python
# src/gateway/paths.py — add near embedding_db_path()
def retrieval_embedding_db_path() -> Path:
    """Dense neural retrieval index (Hole 2). Separate from the lexical embedding
    index so dedup/demand stay on lexical-fallback-v1. Derived/gitignored."""
    return index_dir() / "retrieval.db"
```

- [ ] **Step 4: Implement the retrieval index module**

```python
# src/gateway/retrieval_index.py
"""Dense neural section retriever for the RETRIEVE path (Hole 2).

A second EmbeddingIndex instance bound to the neural encoder and a SEPARATE db
(retrieval_embedding_db_path). The existing lexical EmbeddingIndex — and the
entity/question/section namespaces it serves for dedup/demand/lint — is untouched.
"""
from __future__ import annotations

from gateway import paths
from gateway.embedding_index import EmbeddingIndex
from gateway.retrieval_encoder import retrieval_encoder


def retrieval_index() -> EmbeddingIndex:
    return EmbeddingIndex(encoder=retrieval_encoder(),
                          db_path=paths.retrieval_embedding_db_path())


def dense_section_hits(query: str, k: int) -> list[tuple[str, str, float]]:
    """Top-k (rel_path, heading, distance) section neighbors of `query`."""
    out: list[tuple[str, str, float]] = []
    for hit in retrieval_index().nn("section", query, k=k):
        rel, _, heading = hit.key.partition("#")
        out.append((rel, heading, hit.distance))
    return out
```

- [ ] **Step 5: Add the db to .gitignore**

Run: `echo '.index/retrieval.db*' >> .gitignore` (verify it is not already covered by an existing `.index/` ignore; if `.index/` is already ignored, skip).

Run: `git check-ignore .index/retrieval.db && echo IGNORED`
Expected: `IGNORED`.

- [ ] **Step 6: Run to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_retrieval_index.py -q`
Expected: PASS (2 tests). The stub encoder (paraphrase-tolerant) makes `vagal` the nearest section.

- [ ] **Step 7: Commit**

```bash
git add src/gateway/paths.py src/gateway/retrieval_index.py tests/gateway/test_retrieval_index.py .gitignore
git commit -m "feat(rag): dedicated neural retrieval index (separate db, section NN)"
```

---

## Phase B — Hybrid fusion in `retrieve()`

### Task B1: Reciprocal Rank Fusion helper (pure function)

**Files:**
- Modify: `src/gateway/ops/retrieve.py` (add `_rrf_fuse`)
- Test: `tests/gateway/test_ws2_retrieve.py` (append)

**Interfaces:**
- Produces: `_rrf_fuse(ranked_lists: list[list[str]], k_rrf: int = 60) -> list[str]` — RRF over rank-keyed id lists; returns ids ordered by descending fused score. Stable, deterministic.

- [ ] **Step 1: Write the failing test**

```python
# append to tests/gateway/test_ws2_retrieve.py
from gateway.ops.retrieve import _rrf_fuse


def test_rrf_fuse_rewards_agreement_and_merges():
    lexical = ["a", "b", "c"]
    dense   = ["b", "d", "a"]
    fused = _rrf_fuse([lexical, dense], k_rrf=60)
    assert set(fused) == {"a", "b", "c", "d"}     # union, deduped
    assert fused[0] == "b"                          # appears high in BOTH lists → top
    assert fused.index("a") < fused.index("c")      # 'a' in both beats 'c' in one


def test_rrf_fuse_single_list_preserves_order():
    assert _rrf_fuse([["x", "y", "z"]]) == ["x", "y", "z"]
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py -k rrf_fuse -q`
Expected: FAIL — `cannot import name '_rrf_fuse'`.

- [ ] **Step 3: Implement RRF**

```python
# src/gateway/ops/retrieve.py — module-level helper
def _rrf_fuse(ranked_lists: list[list[str]], k_rrf: int = 60) -> list[str]:
    """Reciprocal Rank Fusion. score(id) = Σ 1/(k_rrf + rank) over each list the id
    appears in (rank is 0-based). Returns ids by descending fused score; ties broken
    by first-seen order for determinism."""
    scores: dict[str, float] = {}
    first_seen: dict[str, int] = {}
    seq = 0
    for lst in ranked_lists:
        for rank, ident in enumerate(lst):
            scores[ident] = scores.get(ident, 0.0) + 1.0 / (k_rrf + rank)
            if ident not in first_seen:
                first_seen[ident] = seq; seq += 1
    return sorted(scores, key=lambda i: (-scores[i], first_seen[i]))
```

- [ ] **Step 4: Run to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py -k rrf_fuse -q`
Expected: PASS (2 tests).

- [ ] **Step 5: Commit**

```bash
git add src/gateway/ops/retrieve.py tests/gateway/test_ws2_retrieve.py
git commit -m "feat(rag): RRF fusion helper for hybrid retrieve"
```

### Task B2: Section-metadata lookup for dense hits

**Files:**
- Modify: `src/gateway/search_index.py` (add `hits_for_sections`)
- Test: `tests/gateway/test_ws5_authority_related.py` (append) or `tests/gateway/test_retrieval_index.py`

**Interfaces:**
- Consumes: the FTS `pages`/`sections` tables (existing).
- Produces: `hits_for_sections(pairs: list[tuple[str, str]]) -> dict[tuple[str, str], IndexHit]` — for each `(rel_path, heading)`, an `IndexHit` populated from the page row (slug/title/page_type/domain/inbound/draft/trust), `score`/`rank` left 0 (fusion uses RRF rank, not these). Missing sections are omitted.

- [ ] **Step 1: Write the failing test**

```python
# append to tests/gateway/test_retrieval_index.py
from gateway import search_index


def test_hits_for_sections_populates_page_metadata(kb_root: Path):
    _page("alpha", "## Mechanism\n\nbody about alpha topic.\n")
    search_index.refresh(rebuild=True)
    rel = "wiki/concepts/alpha.md"
    hits = search_index.hits_for_sections([(rel, "Mechanism"), (rel, "Nonexistent")])
    assert (rel, "Mechanism") in hits
    h = hits[(rel, "Mechanism")]
    assert h.slug == "alpha" and h.title == "alpha" and h.page_type == "concept"
    assert (rel, "Nonexistent") not in hits          # missing section omitted
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_retrieval_index.py -k hits_for_sections -q`
Expected: FAIL — `module 'gateway.search_index' has no attribute 'hits_for_sections'`.

- [ ] **Step 3: Implement `hits_for_sections`** (mirror the row→IndexHit mapping in `search_fts`)

```python
# src/gateway/search_index.py — new function near search_fts
def hits_for_sections(pairs: list[tuple[str, str]]) -> dict[tuple[str, str], "IndexHit"]:
    """Build IndexHits for explicit (rel_path, heading) sections (dense candidates).
    score/rank are 0 — hybrid fusion ranks via RRF, not these fields."""
    if not pairs:
        return {}
    refresh()
    rels = list({rel for rel, _h in pairs})
    placeholders = ",".join("?" * len(rels))
    conn = _connect()
    try:
        rows = conn.execute(
            f"""SELECT p.rel_path, p.slug, p.title, p.page_type,
                   (SELECT domain FROM page_domains pd WHERE pd.rel_path = p.rel_path LIMIT 1),
                   (SELECT COUNT(*) FROM links l WHERE l.target_rel = p.rel_path),
                   p.draft, p.last_updated, p.trust
                FROM pages p WHERE p.rel_path IN ({placeholders})""", rels,
        ).fetchall()
    finally:
        conn.close()
    by_rel = {r[0]: r for r in rows}
    out: dict[tuple[str, str], IndexHit] = {}
    for rel, heading in pairs:
        r = by_rel.get(rel)
        if r is None or not section_text(rel, heading):
            continue
        _, slug, title, ptype, dom, inbound, draft, last_updated, trust = r
        out[(rel, heading)] = IndexHit(
            rel_path=rel, slug=slug, title=title or slug, page_type=ptype,
            domain=dom or "", heading=heading, snippet="", score=0,
            rank=0.0, inbound_count=int(inbound), draft=bool(draft),
            last_updated=str(last_updated or ""),
            trust=float(trust) if trust is not None else 0.5,
        )
    return out
```

- [ ] **Step 4: Run to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_retrieval_index.py -k hits_for_sections -q`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/gateway/search_index.py tests/gateway/test_retrieval_index.py
git commit -m "feat(rag): hits_for_sections — page metadata for dense candidates"
```

### Task B3: Wire the hybrid path into `retrieve()`

**Files:**
- Modify: `src/gateway/ops/retrieve.py` (`retrieve()` single-domain branch + new `_hybrid_hits`)
- Test: `tests/gateway/test_ws2_retrieve.py` (append)

**Interfaces:**
- Consumes: `search_index.search_fts`, `retrieval_index.dense_section_hits`, `search_index.hits_for_sections`, `_rrf_fuse`, the existing `search_index._authority_key` ordering of the lexical list.
- Produces: `_hybrid_hits(query, *, domain, k, scope) -> list[IndexHit]` — fused BM25+dense hits, deduped to best-per-page, length ≤ k. `retrieve()` uses it when `hybrid=True` (config), else the existing lexical path. Block assembly downstream is UNCHANGED (Hole-1 placeholder gate + draft annotation + budget all still apply).

- [ ] **Step 1: Write the failing test (dense surfaces a page BM25 misses; Hole-1 invariants hold)**

```python
# append to tests/gateway/test_ws2_retrieve.py
from gateway.ops import retrieve as retr


def test_hybrid_surfaces_paraphrase_miss(kb_root: Path, monkeypatch):
    # 'reward-deficit' page uses jargon; query is lay. BM25 alone misses it.
    _page("rewarddef", "## Body\n\nAnhedonia: blunted reward sensitivity and lost motivation.\n")
    _page("filler", "## Body\n\ngastric emptying vagal tax filing widget unrelated.\n")
    search_index.refresh(rebuild=True)
    from gateway.retrieval_index import retrieval_index
    retrieval_index().rebuild_from_canonical()
    # stub encoder is paraphrase-tolerant → dense pulls rewarddef for the lay query
    block, sections = retr.retrieve("losing pleasure and drive", domain="d", hybrid=True)
    assert any(s.slug == "rewarddef" for s in sections)


def test_hybrid_preserves_hole1_placeholder_gate(kb_root: Path):
    _page("stubby", "## Summary\n\n_(needs population from legacy import)_\n", draft=True)
    search_index.refresh(rebuild=True)
    from gateway.retrieval_index import retrieval_index
    retrieval_index().rebuild_from_canonical()
    block, _ = retr.retrieve("needs population legacy import", domain="d", hybrid=True)
    assert "needs population from legacy import" not in block
```

Note: `_page` helper is defined earlier in this test module.

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py -k "hybrid_surfaces or hybrid_preserves" -q`
Expected: FAIL — `retrieve() got an unexpected keyword argument 'hybrid'`.

- [ ] **Step 3: Implement `_hybrid_hits` and the `hybrid` switch**

```python
# src/gateway/ops/retrieve.py
# (top) add: from gateway.retrieval_index import dense_section_hits

def _hybrid_hits(query: str, *, domain: str | None, k: int, scope: str) -> list:
    """Fuse BM25 (authority order) with dense section NN via RRF; best-per-page, ≤k."""
    lexical = search_index.search_fts(
        query, scope=scope, domain=domain, limit=k * 2,
        order="authority", include_drafts=True,
    )
    lex_ids = [f"{h.rel_path}#{h.heading}" for h in lexical]
    dense = dense_section_hits(query, k=k * 2)  # (rel, heading, dist)
    dense_ids = [f"{rel}#{heading}" for rel, heading, _d in dense]
    dense_meta = search_index.hits_for_sections([(r, h) for r, h, _ in dense])

    by_id = {f"{h.rel_path}#{h.heading}": h for h in lexical}
    for (rel, heading), hit in dense_meta.items():
        by_id.setdefault(f"{rel}#{heading}", hit)

    fused_ids = _rrf_fuse([lex_ids, dense_ids])
    out, seen_pages = [], set()
    for ident in fused_ids:
        hit = by_id.get(ident)
        if hit is None or hit.rel_path in seen_pages:   # best-section-per-page
            continue
        seen_pages.add(hit.rel_path)
        out.append(hit)
        if len(out) >= k:
            break
    return out
```

Then in `retrieve()`, add `hybrid: bool = False` to the signature and select the path in the single-domain branch:

```python
    else:
        single = multi[0] if multi else domain
        if hybrid:
            hits = _hybrid_hits(query.strip(), domain=single, k=k, scope=scope)
        else:
            hits = search_index.search_fts(
                query.strip(), scope=scope, domain=single, limit=k,
                order="authority", include_drafts=include_drafts,
            )
```

- [ ] **Step 4: Run to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py -k "hybrid_surfaces or hybrid_preserves" -q`
Expected: PASS (2 tests).

- [ ] **Step 5: Run the full retrieve suite (no Hole-1 regression)**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py -q`
Expected: PASS (all prior Hole-1 tests + the new hybrid tests).

- [ ] **Step 6: Commit**

```bash
git add src/gateway/ops/retrieve.py tests/gateway/test_ws2_retrieve.py
git commit -m "feat(rag): hybrid BM25+dense retrieve path (RRF), Hole-1 gates preserved"
```

---

## Phase C — Bake-off harness (calibration)

### Task C1: Config-scored probe runner (recall + G-NEG)

**Files:**
- Create: `src/gateway/scripts/bakeoff.py`
- Test: `tests/test_bakeoff.py`

**Interfaces:**
- Consumes: `retrieve.retrieve` (with `hybrid=True`), `semantic_mismatch.yaml`, `retrieval_index().rebuild_from_canonical()`.
- Produces: `score_config(goldens_path: str, k: int) -> dict` returning `{"recall_at_k": float, "placeholder_leaks": int, "n": int}` over the probe through the live hybrid retrieve path.

- [ ] **Step 1: Write the failing test (deterministic, stub encoder, tiny golden file)**

```python
# tests/test_bakeoff.py
from pathlib import Path
import yaml
from gateway import paths, search_index, frontmatter as fm
from gateway.scripts.bakeoff import score_config


def _page(slug, body):
    d = paths.wiki_dir() / "concepts"; d.mkdir(parents=True, exist_ok=True)
    (d / f"{slug}.md").write_text(fm.serialize(
        {"type": "concept", "slug": slug, "title": slug, "domains": ["d"],
         "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z"}, body))


def test_score_config_reports_recall_and_zero_leaks(kb_root: Path, tmp_path: Path):
    _page("anhedonia", "## Body\n\nblunted reward sensitivity and lost motivation.\n")
    search_index.refresh(rebuild=True)
    from gateway.retrieval_index import retrieval_index
    retrieval_index().rebuild_from_canonical()
    g = tmp_path / "g.yaml"
    g.write_text(yaml.safe_dump({"queries": [
        {"q": "losing pleasure and drive", "domain": "d", "expect": ["anhedonia"]}]}))
    res = score_config(str(g), k=10)
    assert res["n"] == 1 and 0.0 <= res["recall_at_k"] <= 1.0
    assert res["placeholder_leaks"] == 0
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_bakeoff.py -q`
Expected: FAIL — `ModuleNotFoundError: gateway.scripts.bakeoff`.

- [ ] **Step 3: Implement `score_config`**

```python
# src/gateway/scripts/bakeoff.py
"""Bake-off scorer for Hole-2 retrieval configs. Scores a config on the probe
through the REAL hybrid retrieve path (recall + placeholder-leak control)."""
from __future__ import annotations

import yaml

from gateway.ops import retrieve as retr

_LEAK_NEEDLES = ("needs population from legacy import", "summary not yet generated",
                 "claims not yet extracted", "no cross-references yet", "no citations returned")


def score_config(goldens_path: str, k: int = 10) -> dict:
    G = yaml.safe_load(open(goldens_path))["queries"]
    hits = leaks = 0
    for e in G:
        block, sections = retr.retrieve(e["q"], domain=e.get("domain"), k=k, hybrid=True)
        slugs = [s.slug for s in sections]
        hits += any(x in slugs for x in e["expect"])
        leaks += sum(block.count(n) for n in _LEAK_NEEDLES)
    n = len(G)
    return {"recall_at_k": hits / n if n else 0.0, "placeholder_leaks": leaks, "n": n}
```

- [ ] **Step 4: Run to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_bakeoff.py -q`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/gateway/scripts/bakeoff.py tests/test_bakeoff.py
git commit -m "feat(rag): bake-off config scorer (recall + placeholder-leak control)"
```

### Task C2: Latency micro-benchmark + sweep CLI

**Files:**
- Modify: `src/gateway/scripts/bakeoff.py` (add `time_config`, `run_sweep`, `main`)
- Modify: `src/gateway/cli.py` (register `eval-embedding-bakeoff` subcommand)
- Test: `tests/test_bakeoff.py` (append)

**Interfaces:**
- Produces:
  - `time_config(sample_queries: list[tuple[str, str | None]]) -> dict` → `{"query_ms_p50": float, "query_ms_p90": float}` (wall-clock per `retrieve(hybrid=True)` call; uses `time.perf_counter`, not the forbidden `Date.now`-style wall clock — `perf_counter` is allowed).
  - `run_sweep(configs: list[dict], goldens_path: str, sample_queries) -> list[dict]` → per-config `{config, recall_at_k, placeholder_leaks, query_ms_p50, query_ms_p90}`. Each config is `{"encoder": "<WIKI_RETRIEVAL_ENCODER value>", "k_rrf": int}`; `run_sweep` sets the env, rebuilds the retrieval index, scores, times.
  - `main()` wired to `wiki eval-embedding-bakeoff --goldens <path> --k N`.

- [ ] **Step 1: Write the failing test (sweep over two stub configs is deterministic)**

```python
# append to tests/test_bakeoff.py
from gateway.scripts.bakeoff import run_sweep


def test_run_sweep_scores_each_config(kb_root: Path, tmp_path: Path):
    _page("anhedonia", "## Body\n\nblunted reward sensitivity and lost motivation.\n")
    search_index.refresh(rebuild=True)
    g = tmp_path / "g.yaml"
    import yaml as _y
    g.write_text(_y.safe_dump({"queries": [
        {"q": "losing pleasure and drive", "domain": "d", "expect": ["anhedonia"]}]}))
    configs = [{"encoder": "stub", "k_rrf": 60}, {"encoder": "stub", "k_rrf": 10}]
    rows = run_sweep(configs, str(g), [("losing pleasure and drive", "d")])
    assert len(rows) == 2
    for r in rows:
        assert "recall_at_k" in r and "query_ms_p50" in r and r["placeholder_leaks"] == 0
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_bakeoff.py -k run_sweep -q`
Expected: FAIL — `cannot import name 'run_sweep'`.

- [ ] **Step 3: Implement timing + sweep**

```python
# append to src/gateway/scripts/bakeoff.py
import os, time, json, argparse
from gateway.retrieval_index import retrieval_index


def time_config(sample_queries: list[tuple[str, str | None]]) -> dict:
    times = []
    for q, dom in sample_queries:
        t0 = time.perf_counter()
        retr.retrieve(q, domain=dom, hybrid=True)
        times.append((time.perf_counter() - t0) * 1000.0)
    times.sort()
    def pct(p): return times[min(len(times) - 1, int(p * len(times)))] if times else 0.0
    return {"query_ms_p50": pct(0.5), "query_ms_p90": pct(0.9)}


def run_sweep(configs, goldens_path, sample_queries, k: int = 10) -> list[dict]:
    """Primary sweep axis is encoder identity + truncation dim (the WIKI_RETRIEVAL_ENCODER
    spec). RRF k_rrf is secondary; if the frontier is close, thread k_rrf through
    retrieve()->_hybrid_hits->_rrf_fuse in a follow-up and add it to the matrix then."""
    rows = []
    for cfg in configs:
        os.environ["WIKI_RETRIEVAL_ENCODER"] = cfg["encoder"]
        retrieval_index().rebuild_from_canonical()    # re-embed under this encoder
        sc = score_config(goldens_path, k=k)
        tm = time_config(sample_queries)
        rows.append({"config": cfg, **sc, **tm})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--goldens", default=".knowledge/eval/retrieval/semantic_mismatch.yaml")
    ap.add_argument("--k", type=int, default=10)
    args = ap.parse_args()
    import yaml as _y
    qs = [(e["q"], e.get("domain")) for e in _y.safe_load(open(args.goldens))["queries"]]
    # Production sweep configs are edited here before a real run (see Task C3).
    configs = [{"encoder": os.environ.get("WIKI_RETRIEVAL_ENCODER", "stub"), "k_rrf": 60}]
    rows = run_sweep(configs, args.goldens, qs, k=args.k)
    print(json.dumps(rows, indent=2))
```

Register in `cli.py` (follow the existing subcommand-registration pattern in that file):

```python
    # in the subparser block
    sp_bake = sub.add_parser("eval-embedding-bakeoff",
                             help="sweep retrieval encoder configs on the probe + latency")
    sp_bake.add_argument("--goldens", default=".knowledge/eval/retrieval/semantic_mismatch.yaml")
    sp_bake.add_argument("--k", type=int, default=10)
    # in the dispatch block
    elif args.command == "eval-embedding-bakeoff":
        from gateway.scripts.bakeoff import run_sweep
        import yaml as _y, os, json
        qs = [(e["q"], e.get("domain")) for e in _y.safe_load(open(args.goldens))["queries"]]
        configs = [{"encoder": os.environ.get("WIKI_RETRIEVAL_ENCODER", "stub"), "k_rrf": 60}]
        print(json.dumps(run_sweep(configs, args.goldens, qs, k=args.k), indent=2))
```

- [ ] **Step 4: Run to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_bakeoff.py -q`
Expected: PASS (all bakeoff tests).

- [ ] **Step 5: Verify the CLI is wired**

Run: `.venv/bin/wiki eval-embedding-bakeoff --help`
Expected: shows `--goldens` and `--k`.

- [ ] **Step 6: Commit**

```bash
git add src/gateway/scripts/bakeoff.py src/gateway/cli.py tests/test_bakeoff.py
git commit -m "feat(rag): bake-off sweep + latency micro-benchmark CLI"
```

### Task C3: RUN the bake-off and pick the winner (calibration — not TDD)

This is a one-time local calibration on the real M3 Max. No new code; it produces the decision data the spec defers to.

- [ ] **Step 1: Install the local model runtime** (MLX path)

Run: `VIRTUAL_ENV="$(pwd)/.venv" uv pip install mlx mlx-embeddings`
(If MLX-embeddings lacks a needed Qwen3 build, use the GGUF/llama.cpp path instead and adapt `MlxQwen3Encoder` to a llama.cpp embedding call — same Protocol.)

- [ ] **Step 2: Edit the sweep configs** in `bakeoff.py main()` / the CLI dispatch to the real candidate matrix:

```python
# Resolve the exact MLX 4-bit build ids on HuggingFace first (e.g.
#   `.venv/bin/python -c "from huggingface_hub import HfApi; print([m.id for m in HfApi().list_models(search='Qwen3-Embedding-4B', author='mlx-community')])"`)
# and substitute below. 0.6B 4-bit DWQ id is mlx-community/Qwen3-Embedding-0.6B-4bit-DWQ.
QWEN_06B = "mlx-community/Qwen3-Embedding-0.6B-4bit-DWQ"
QWEN_4B  = "<resolved-mlx-community-Qwen3-Embedding-4B-build>"   # fill from the HF lookup above
configs = [
    {"encoder": "stub"},                          # control / lower bound
    {"encoder": f"mlx:{QWEN_06B}:256"},
    {"encoder": f"mlx:{QWEN_06B}:512"},
    {"encoder": f"mlx:{QWEN_4B}:512"},
    {"encoder": f"mlx:{QWEN_4B}:native"},         # native = the build's full dim (drop the trailing :dim slice in MlxQwen3Encoder when == native)
]
```

- [ ] **Step 3: Run the sweep**

Run: `.venv/bin/wiki eval-embedding-bakeoff --k 10 | tee docs/260624_hole2-bakeoff-results.json`
Record the frontier: per config `recall_at_k`, `placeholder_leaks` (MUST be 0), `query_ms_p50/p90`, and note ingest/rebuild wall-time per encoder (from `rebuild_from_canonical` `RebuildStats.wall_seconds`).

- [ ] **Step 4: Pick the winner** on the accuracy/latency frontier per the spec's constraint (accuracy-primary; query latency ≤ ~2× the stub/0.6B baseline, never 3–5×). Document the choice + evidence in `docs/260624_hole2-bakeoff-results.json` plus a one-paragraph decision note appended to the design spec. STOP and confirm the pick with the user before Phase D.

- [ ] **Step 5: Commit the results**

```bash
git add docs/260624_hole2-bakeoff-results.json docs/260624_hole2-hybrid-retrieval-design.md
git commit -m "docs(rag): Hole-2 bake-off results + locked retrieval config"
```

---

## Phase D — Lock the winner + acceptance gate

### Task D1: Make hybrid the default retrieve path under the locked encoder

**Files:**
- Modify: `src/gateway/ops/retrieve.py` (`retrieve_op` passes `hybrid=True`; `retrieve()` default), `src/gateway/embedding_index.py` `thresholds()` (recalibrated `section` operating point if the winner needs it)
- Modify: deployment config / env docs for `WIKI_RETRIEVAL_ENCODER`
- Test: `tests/gateway/test_ws2_retrieve.py` (append)

**Interfaces:**
- Consumes: the winning encoder spec (Task C3).
- Produces: `retrieve_op(...)` runs the hybrid path by default; the lexical-only path stays reachable via `hybrid=False` for the bake-off control and tests.

**Carry-forward finding (whole-branch review, 2026-06-24):** `_hybrid_hits` currently hardcodes `search_fts(..., include_drafts=True)` and ignores the caller's `include_drafts`. Inert while hybrid is opt-in, but it becomes a live inconsistency the moment this task makes hybrid the default (a `retrieve(include_drafts=False, hybrid=True)` caller would still get drafts). **Fix as part of D1:** thread `include_drafts` through `_hybrid_hits` into its lexical leg (`src/gateway/ops/retrieve.py`, the `_hybrid_hits` `search_fts` call), and add a test that `retrieve(include_drafts=False, hybrid=True)` excludes drafts.

- [ ] **Step 1: Write the failing test**

```python
# append to tests/gateway/test_ws2_retrieve.py
def test_retrieve_op_uses_hybrid_by_default(kb_root, monkeypatch):
    calls = {}
    import gateway.ops.retrieve as R
    orig = R.retrieve
    def spy(*a, **k): calls["hybrid"] = k.get("hybrid"); return orig(*a, **k)
    monkeypatch.setattr(R, "retrieve", spy)
    _page("z", "## B\n\ncontent z about widgets.\n")
    search_index.refresh(rebuild=True)
    from gateway.retrieval_index import retrieval_index
    retrieval_index().rebuild_from_canonical()
    R.retrieve_op("widgets", domain="d")
    assert calls["hybrid"] is True
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py -k uses_hybrid_by_default -q`
Expected: FAIL (`hybrid` is None — `retrieve_op` doesn't pass it).

- [ ] **Step 3: Pass `hybrid=True` from `retrieve_op`**

```python
# src/gateway/ops/retrieve.py — in retrieve_op(), the retrieve() call
    block, sections = retrieve(
        query, domain=domain, domains=domains, k=k, budget_chars=budget_chars,
        hybrid=True,
    )
```

- [ ] **Step 4: Run to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_ws2_retrieve.py -k uses_hybrid_by_default -q`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/gateway/ops/retrieve.py tests/gateway/test_ws2_retrieve.py
git commit -m "feat(rag): hybrid retrieve is the default agent path"
```

### Task D2: Wire the probe-recall acceptance into the eval/gate

**Files:**
- Create: `tests/test_retrieval_probe_gate.py` (a fast, synthetic-corpus invariant test — NOT the live ~5k corpus)
- Modify: `docs/260624_hole2-hybrid-retrieval-design.md` (record the locked target)
- Test: itself

**Interfaces:**
- Consumes: `score_config` (C1), a small committed synthetic corpus fixture mirroring the probe's shape (jargon page + lay query).
- Produces: a gated invariant — hybrid recall on the synthetic probe ≥ a floor that the lexical-only path provably fails (drives the feature, corpus-independent, runs in the suite so `gate.py` Step-1 catches regressions).

- [ ] **Step 1: Write the gate test (hybrid passes, lexical-only fails — proves the feature drives recall)**

```python
# tests/test_retrieval_probe_gate.py
from pathlib import Path
import yaml
from gateway import paths, search_index, frontmatter as fm
from gateway.ops import retrieve as retr


def _page(slug, body):
    d = paths.wiki_dir() / "concepts"; d.mkdir(parents=True, exist_ok=True)
    (d / f"{slug}.md").write_text(fm.serialize(
        {"type": "concept", "slug": slug, "title": slug, "domains": ["d"],
         "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z"}, body))


def test_hybrid_beats_lexical_on_paraphrase(kb_root: Path):
    # jargon page, lay query: lexical alone misses; hybrid (dense) hits.
    _page("anhedonia", "## Body\n\nblunted reward sensitivity; loss of motivation and drive.\n")
    for i in range(4):
        _page(f"noise{i}", f"## B\n\nunrelated filler about tax filing widget {i}.\n")
    search_index.refresh(rebuild=True)
    from gateway.retrieval_index import retrieval_index
    retrieval_index().rebuild_from_canonical()
    q = "why do people lose pleasure and drive"
    _, lex = retr.retrieve(q, domain="d", hybrid=False)
    _, hyb = retr.retrieve(q, domain="d", hybrid=True)
    assert all(s.slug != "anhedonia" for s in lex), "precondition: lexical-only misses"
    assert any(s.slug == "anhedonia" for s in hyb), "hybrid must surface the paraphrase match"
```

- [ ] **Step 2: Run to verify it fails or passes correctly**

Run: `.venv/bin/python -m pytest tests/test_retrieval_probe_gate.py -q`
Expected: PASS once Phase B is in (hybrid surfaces it; lexical precondition holds with the stub encoder). If the stub can't separate them, strengthen the jargon/lay gap in the fixture until the lexical precondition holds RED and hybrid holds GREEN — this is the teeth.

- [ ] **Step 3: Confirm it is gated by the suite**

Run: `.venv/bin/python -m pytest tests/test_retrieval_probe_gate.py -q`
(The pre-merge gate Step-1 runs the full suite, so this test gates the feature automatically — no `gate.py` change needed.)

- [ ] **Step 4: Commit**

```bash
git add tests/test_retrieval_probe_gate.py docs/260624_hole2-hybrid-retrieval-design.md
git commit -m "test(rag): gate hybrid-beats-lexical recall invariant (synthetic, teeth-verified)"
```

### Task D3: Full pre-merge gate + live probe re-baseline

- [ ] **Step 1: Run the live probe through the locked hybrid path** (real corpus, real encoder set via `WIKI_RETRIEVAL_ENCODER`)

Run: `.venv/bin/python scripts/probe_retrieve.py --k 10`
Expected: recall climbs from 0.381 toward the locked target (~0.85); placeholder-pollution count = 0; the 3 controls still HIT.

- [ ] **Step 2: Run the pre-merge gate**

Run: `.venv/bin/python -m gateway.scripts.gate`
Expected: PASS — full suite green, `eval-retrieval` recall@10 ≥ 0.90 (easy goldens unmoved — RRF keeps BM25 hits), merge-map 0 regressions (lexical encoder untouched), embedding namespaces OK, lints at baseline.

- [ ] **Step 3: Commit any gate-surfaced fixes, then open the PR**

```bash
git push -u origin feat/hole2-hybrid-retrieval
# open PR to main; user merges. Paste probe before/after + gate result in the PR body.
```

---

## Phase E — Reranker (deferred; build ONLY if Phase-D probe < target)

**Trigger:** the live probe (D3) lands below the locked target with the bi-encoder fusion alone. If it clears target, SKIP Phase E (YAGNI) and record the skip in the design doc.

### Task E1: Config-gated cross-encoder rerank stage

**Files:**
- Create: `src/gateway/reranker.py` (Protocol + `StubReranker` + `Qwen3Reranker` via `tomaarsen/Qwen3-Reranker-0.6B-seq-cls`)
- Modify: `src/gateway/ops/retrieve.py` (`_hybrid_hits` reranks fused top-K when enabled)
- Test: `tests/gateway/test_reranker.py`, `tests/gateway/test_ws2_retrieve.py`

**Interfaces:**
- Produces: `Reranker` Protocol (`score(query: str, passages: list[str]) -> list[float]`), `StubReranker` (deterministic, for CI), `rerank_topk(query, hits, k_rerank) -> list[IndexHit]`. Gated by env `WIKI_RERANK` (off default); bounded K (default 20).

- [ ] **Step 1: Write the failing test (reranker reorders fused top-K; bounded K; off by default)**

```python
# tests/gateway/test_reranker.py
from gateway.reranker import StubReranker, rerank_topk


def test_stub_reranker_reorders_by_lexical_overlap():
    class H:  # minimal stand-in carrying rel_path + heading + text accessor
        def __init__(self, rel, text): self.rel_path = rel; self.heading = "B"; self._t = text
    # rerank_topk pulls passage text via search_index.section_text in real use;
    # here we inject a passage map to keep the unit pure.
    rr = StubReranker()
    scored = rr.score("alpha beta", ["gamma delta", "alpha beta gamma", "zzz"])
    assert scored[1] == max(scored)     # best lexical overlap ranks highest
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/gateway/test_reranker.py -q`
Expected: FAIL — `ModuleNotFoundError: gateway.reranker`.

- [ ] **Step 3: Implement the reranker (stub + neural) and wire `rerank_topk` into `_hybrid_hits` behind `WIKI_RERANK`**

```python
# src/gateway/reranker.py
from __future__ import annotations
import os
from typing import Sequence


class StubReranker:
    model_version = "stub-reranker-v1"
    def score(self, query: str, passages: Sequence[str]) -> list[float]:
        q = set(query.lower().split())
        return [len(q & set(p.lower().split())) / (len(q) or 1) for p in passages]


class Qwen3Reranker:
    model_version = "tomaarsen/Qwen3-Reranker-0.6B-seq-cls"
    def __init__(self): self._m = None
    def score(self, query: str, passages: Sequence[str]) -> list[float]:
        from sentence_transformers import CrossEncoder
        if self._m is None: self._m = CrossEncoder(self.model_version)
        return [float(s) for s in self._m.predict([(query, p) for p in passages])]


def reranker():
    return Qwen3Reranker() if os.environ.get("WIKI_RERANK") == "qwen3" else StubReranker()


def rerank_topk(query, hits, k_rerank: int = 20):
    """Reorder the top k_rerank hits by cross-encoder score; tail kept as-is."""
    from gateway import search_index
    head, tail = hits[:k_rerank], hits[k_rerank:]
    if not head:
        return hits
    passages = [search_index.section_text(h.rel_path, h.heading) for h in head]
    scores = reranker().score(query, passages)
    order = sorted(range(len(head)), key=lambda i: -scores[i])
    return [head[i] for i in order] + tail
```

In `_hybrid_hits`, before the best-per-page dedup, when `os.environ.get("WIKI_RERANK")`: build the fused IndexHit list, `rerank_topk(query, fused_hits)`, then dedup.

- [ ] **Step 4: Run to verify it passes**

Run: `.venv/bin/python -m pytest tests/gateway/test_reranker.py tests/gateway/test_ws2_retrieve.py -q`
Expected: PASS.

- [ ] **Step 5: Re-run the live probe + gate (Phase D3) with `WIKI_RERANK=qwen3`; confirm the bounded-K latency stays inside budget. Commit.**

```bash
git add src/gateway/reranker.py src/gateway/ops/retrieve.py tests/gateway/test_reranker.py tests/gateway/test_ws2_retrieve.py
git commit -m "feat(rag): config-gated Qwen3 cross-encoder rerank stage (bounded K)"
```

---

## Self-Review (spec coverage)

- Local neural encoder + Matryoshka truncation → A1 (`MlxQwen3Encoder`, dim-truncate). ✓
- Second encoder, retrieve-only; dedup/merge-map untouched → A2 (separate db), Global Constraints. ✓
- BM25 ∪ dense fusion via RRF → B1/B3. ✓
- Dense NN over `section` namespace → A2 (`dense_section_hits`). ✓
- Bake-off (recall + M3-Max latency, frontier, pick) → C1/C2/C3. ✓
- 256-dim unpinned / dimension swept → A1 (configurable dim), C3 (sweep matrix). ✓
- Hole-1 invariants preserved → B3 test, C1 leak control, D2 gate. ✓
- Gate: eval-retrieval ≥0.90, merge-map 0 regressions, probe acceptance → D2/D3. ✓
- Reranker deferred, probe-gated, bounded K → Phase E (trigger-gated). ✓
- Operating-point recalibration → D1 (`thresholds()` section). ✓
- CI needs no model download → stub encoder everywhere; real model only in C3/D3/E (local). ✓

**Note for the executor:** Phases A–B–C(harness) and D2 are deterministic TDD (stub encoder) and can be built + gated with zero model downloads. C3 (run the sweep), D1/D3 (lock + live gate), and E (reranker) require the local model on the M3 Max and are the calibration/finish phases — do them on the real machine, not in CI.
