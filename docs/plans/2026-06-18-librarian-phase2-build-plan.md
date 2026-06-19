# Librarian Phase 2 — Identity substrate (build plan)

Status: in-progress · Branch: `docs/librarian-rag-design` · Author: build agent · 2026-06-18

Stands up the embedding index (three namespaces) with incremental upsert-on-commit
and shadow-swap rebuild, so commit-time dedup, demand clustering, and gap pre-flight
have the identity geometry they depend on. Adds **alongside** `search_index.py` (FTS),
inheriting the same derived / gitignored / rebuildable discipline (design §2, §13).

## Global Constraints

- `.venv/bin/python` / `.venv/bin/wiki` ONLY. Branch MUST be `docs/librarian-rag-design`.
- Never commit to `main`. Never `git add -A`/`-u`/`.`. Explicit file lists only.
  `log.md` / `index.md` are watcher-owned — never staged. The untracked
  `docs/260618_librarian-rag-design-session-brief.md` is left alone.
- TDD per task: failing test first → run (confirm fail) → minimal impl → run
  (confirm pass) → broader suite → commit. Adversarial tests with negative controls
  for every concurrency / rebuild-race / freshness path. No monkeypatching of the
  core path under test.
- **Encoder fork (pre-decided, do NOT deviate):** pluggable encoder protocol; the
  ACTIVE default is the I2 **lexical fallback** (`lexical-fallback-v1`) — pure
  numpy / python, no heavy ML deps. `numpy 2.4.4` is available under `.venv`.
- The embedding store is derived state: gitignored under `.index/`, rebuildable from
  canonical markdown, never canonical. Markdown stays the source of truth.
- Phase 2 adds an index alongside FTS; it does **not** change FTS retrieval. Baseline
  `eval-retrieval --compare` recall@10 = 0.926 must not regress (floor 0.90).

## Architecture summary

```
src/gateway/embedding_index.py        # the store + encoder + namespaces + shadow-swap
src/gateway/evaluate/embedding_eval.py # per-namespace adequacy gate + fallback flag
.index/embeddings.db                   # derived SQLite store (gitignored)
.index/embeddings.shadow.db            # shadow location during rebuild (gitignored)
.knowledge/eval/embedding/*.yaml       # per-namespace golden sets
```

Three namespaces, three granularities, three operating points (design §13):

| Namespace | Granularity | Similarity notion | Threshold key |
|---|---|---|---|
| `section` | markdown section | query→passage relevance | «embed.retrieval_relevance_threshold» |
| `entity` | entity/concept page identity text | co-reference identity (strict) | «embed.dedup_identity_threshold» |
| `question` | gap-signature / question | topical-gap (coarse) | «embed.demand_gap_threshold» |

Encoder protocol (pluggable):

```python
class Encoder(Protocol):
    model_version: str
    dim: int
    def embed(self, texts: Sequence[str]) -> list[list[float]]: ...
```

Active default = `LexicalFallbackEncoder` (`lexical-fallback-v1`): normalized
token-set + char-3-gram hashing into a fixed-dim L2-normalized numpy vector.
Cosine **distance** = `1 - dot` (vectors are unit-norm). Deterministic: same text →
same vector, byte-stable across rebuilds.

## Distance / threshold semantics

Distance is cosine distance in `[0, 2]`; for unit vectors `d = 1 - cos`. A namespace
NN-search returns `(key, distance)` ascending. An identity/relevance/gap match is
`distance <= threshold`. The lexical encoder is honestly weak: its gates are set to
operating points it actually clears on the golden sets (recorded in the gate report),
and each gate is independently falsifiable — flip a golden label and the gate fails.

---

## Task 1 — Embedding store scaffold + pluggable encoder + lexical fallback

**Files:** create `src/gateway/embedding_index.py`,
`tests/gateway/test_embedding_index.py`. Modify `src/gateway/paths.py` (add
`embedding_db_path()` / `embedding_shadow_db_path()`).

**Interfaces:**

```python
# paths.py
def embedding_db_path() -> Path:        # index_dir() / "embeddings.db"
def embedding_shadow_db_path() -> Path: # index_dir() / "embeddings.shadow.db"
```

```python
# embedding_index.py
NAMESPACES = ("section", "entity", "question")

class Encoder(Protocol):
    model_version: str
    dim: int
    def embed(self, texts) -> list[list[float]]: ...

class LexicalFallbackEncoder:
    model_version = "lexical-fallback-v1"
    dim = 256
    def embed(self, texts) -> list[list[float]]: ...   # hashed, L2-normalized

@dataclass
class NNHit:
    key: str
    distance: float

class EmbeddingIndex:
    def __init__(self, encoder=None, db_path=None): ...
    def upsert(self, namespace, key, text) -> None
    def nn(self, namespace, text, k=5) -> list[NNHit]      # ascending distance
    def model_version(self) -> str
    def rebuild_from_canonical(self) -> RebuildStats        # Task 4 extends
    def upsert_page(self, rel_path, text, front) -> None     # routes to namespaces
```

**Store schema (SQLite):**
```
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);   -- model_version, schema_version
CREATE TABLE vectors (
  namespace TEXT NOT NULL,
  key TEXT NOT NULL,        -- rel_path for section/entity, signature for question
  dim INTEGER NOT NULL,
  vec BLOB NOT NULL,        -- float32 numpy tobytes()
  model_version TEXT NOT NULL,
  PRIMARY KEY (namespace, key)
);
```

`nn` loads the namespace's vectors, computes cosine distance vs the query vector in
numpy, returns the k smallest. The encoder writes `model_version` into `meta` on
first connect; a stored `model_version` mismatch is surfaced (drives re-embed).

**RED → GREEN → commit steps:**

1. RED: `test_paths_embedding_db_path` — `embedding_db_path()` lives under `index_dir()`,
   gitignored prefix. Run → fail.
2. GREEN: add the two path helpers. Run → pass.
3. RED: `test_lexical_encoder_deterministic` — same text twice → identical vector;
   different text → different vector; vector is unit-norm; dim == 256. Negative
   control: two unrelated strings have distance > two paraphrases.
4. GREEN: implement `LexicalFallbackEncoder`. Run → pass.
5. RED: `test_upsert_and_nn_per_namespace` — upsert 3 keys into `entity`, nn for a
   near-duplicate returns it at rank 0 with small distance; an unrelated string ranks
   it far. Repeat for `section` and `question`. Negative control: nn into an empty
   namespace returns `[]`.
6. RED: `test_self_heal_after_delete` — build store, delete the db file, `rebuild_from_canonical`
   (stub: re-embed from a passed page list), nn returns correct results.
   `test_model_version_recorded` — `model_version()` == `lexical-fallback-v1`.
7. GREEN: implement `EmbeddingIndex` (connect, schema, upsert, nn, model_version).
   Run new tests → pass.
8. Broader: `pytest tests/gateway/test_embedding_index.py -q`. Commit
   (`embedding_index.py`, `paths.py`, `test_embedding_index.py`).

---

## Task 2 — Three namespaces wired to page content + per-namespace thresholds

**Files:** modify `src/gateway/embedding_index.py` (add `upsert_page` routing +
threshold accessors), `tests/gateway/test_embedding_index.py`.

`upsert_page(rel_path, text, front)` routes by page type / location:
- `section`: each markdown section (reuse `search_index._split_sections`) → key
  `"{rel_path}#{heading}"`, text = heading + section body.
- `entity`: pages of type `entity` / `concept` → key `rel_path`, identity text =
  `title + aliases + canonical_name` (the identity surface, not the full body).
- `question`: not page-derived — fed by the DemandLedger (Phase 5). `upsert_page`
  skips it; `question` is exercised directly via `upsert(namespace="question", ...)`.

Threshold accessors read the three §1.2 keys (with the placeholder starts), bound to
`model_version`:

```python
def thresholds() -> dict[str, float]:
    return {
        "section": 0.30,   # «embed.retrieval_relevance_threshold»  (cosine dist)
        "entity":  0.08,   # «embed.dedup_identity_threshold» (strict)
        "question": 0.40,  # «embed.demand_gap_threshold» (coarse)
    }
```

(Calibrated in Task 5 against the golden sets; values recorded to the ledger §1.2.)

**RED → GREEN → commit:**

1. RED: `test_upsert_page_routes_entity_and_section` — an entity page upserts one
   `entity` row keyed by rel_path AND `section` rows keyed by `rel_path#heading`;
   a `question` row is NOT created. Negative control: a `source`-type page upserts
   `section` rows only, no `entity` row.
2. RED: `test_thresholds_per_namespace_distinct` — three distinct values; entity
   strictest. Negative control: assert they are not all equal.
3. GREEN: implement `upsert_page` + `thresholds`. Run → pass.
4. Broader suite for the file. Commit (`embedding_index.py`, `test_embedding_index.py`).

---

## Task 3 — Incremental upsert-on-commit (freshness)

**Files:** modify `src/gateway/commit_gate.py` (upsert committed pages into the
entity + section namespaces inside the commit, after the git commit, before return),
`tests/gateway/test_commit_freshness.py`.

The committer, after a successful `git commit`, upserts each written page's embedding
rows current-as-of-HEAD. This is **not lazy** — it happens in the commit flow so the
next intent in the same serialization window can NN-search the entity namespace and
see the just-committed page (the dedup freshness dependency, §13). The CommitGate
takes an optional `embedding_index` (None → no-op, so existing tests are unaffected).

```python
def __init__(self, ..., embedding_index=None): ...
# after self._git("commit", ...):
if self._embedding_index is not None:
    for rel, content in writes.items():
        front, body = fm.parse(content)
        self._embedding_index.upsert_page(rel, content, front)
```

Crash-safety note (design §2): embeddings are derived; a crash after `git commit` but
before upsert self-heals on the next incremental upsert / rebuild. The git commit is
the atomic boundary — embedding upsert is strictly downstream.

**RED → GREEN → commit (adversarial freshness):**

1. RED: `test_commit_upserts_entity_namespace_freshness` — real `CommitGate` over a
   real temp git repo (mirror `test_commit_gate.py` fixture; NOT monkeypatched):
   commit page A (an entity), then NN-search the entity namespace for A's identity
   text → A present at rank 0, current-as-of-HEAD. Commit page B (near-duplicate
   identity) in the same window; before B's commit, NN-search sees A (proving the
   earlier-in-window page is visible — the freshness contract). Negative control:
   a page committed with `embedding_index=None` produces NO entity rows (proves the
   upsert is the cause, not a lazy rebuild elsewhere).
2. RED: `test_commit_no_embedding_index_is_noop` — `CommitGate(embedding_index=None)`
   commits cleanly, no embedding store created (back-compat for Phase-1 tests).
3. GREEN: thread `embedding_index` through `__init__` + the post-commit upsert. Run →
   pass.
4. Broader: `pytest tests/gateway/test_commit_gate.py tests/gateway/test_commit_freshness.py -q`.
   Commit (`commit_gate.py`, `test_commit_freshness.py`).

---

## Task 4 — Shadow-swap rebuild + quiesce + rebuild-and-diff (A6, F2)

**Files:** modify `src/gateway/embedding_index.py` (shadow rebuild + atomic swap +
rebuild lock / quiesce + diff), `tests/gateway/test_embedding_rebuild.py`.

`rebuild_from_canonical()`:
1. Acquire a rebuild lock (`locking.file_lock("librarian-embedding-rebuild")`).
2. Write a complete fresh index to `embedding_shadow_db_path()` (re-embed every
   canonical page via `upsert_page`, walking `wiki/` like `search_index._scan_files`).
3. Atomically swap: `os.replace(shadow, live)` — readers see old-complete or
   new-complete, never half (a concurrent `nn` opening the live db either reads the
   pre-swap file or the post-swap file; `os.replace` is atomic on the same fs).
4. Record wall-time → return `RebuildStats(pages, wall_seconds, model_version)`.

**Quiesce (A6):** commits acquire the same rebuild lock (or read a pinned pre-rebuild
snapshot) during a rebuild so commit-time dedup never reads a half index. Concretely:
`EmbeddingIndex.upsert_page` and the CommitGate post-commit upsert take the rebuild
lock briefly; a rebuild holds it for the swap. Since markdown is canonical and the
swap is atomic, the simplest correct discipline is: rebuild builds the shadow WITHOUT
the lock (slow), then takes the lock only for the `os.replace` swap; commits take the
lock only for their upsert. The window is the swap, which is atomic.

**Rebuild-and-diff equivalence (F2):** `diff_against_live()` rebuilds into the shadow
and compares (namespace, key, model_version) row sets + per-row vector equality
against the live store; any divergence is the §16 `index-rebuild-divergence` bad
state. Returns a `DivergenceReport(missing, extra, vector_mismatch)`.

**RED → GREEN → commit (adversarial concurrency):**

1. RED: `test_rebuild_shadow_swap_complete` — build a live store from N pages, mutate
   one page on disk, `rebuild_from_canonical`, the live store now reflects the
   mutation and has exactly N rows (complete, no orphan). `RebuildStats.wall_seconds`
   is recorded (> 0).
2. RED: `test_concurrent_read_during_rebuild_no_half_state` — REAL concurrency:
   start a rebuild in a background thread that holds the build long enough (a real
   slow `upsert_page` over many pages, or a synchronization barrier the test
   controls WITHOUT monkeypatching `os.replace`), and from the main thread issue
   repeated `nn` reads; assert EVERY read returns a complete result set (either the
   full pre-rebuild set or the full post-rebuild set), never a partial count.
   Negative control: a deliberately broken non-atomic rebuild (build directly into
   the live db) would expose a partial count — assert the atomic path never does.
3. RED: `test_commit_quiesced_during_rebuild` — a commit's upsert and a rebuild swap
   serialize on the rebuild lock; the post-commit state is consistent (the committed
   page is present after both complete, regardless of interleaving). Run with a real
   thread, real lock.
4. RED: `test_rebuild_and_diff_detects_divergence` — live store equals a fresh
   rebuild → `DivergenceReport` empty. Then corrupt one live vector → diff reports
   exactly that key as `vector_mismatch`. Delete one live row → reported as `missing`.
   Negative control: an unrelated key is NOT reported.
5. GREEN: implement shadow rebuild, atomic swap, rebuild lock, `diff_against_live`.
   Run → pass.
6. Broader: `pytest tests/gateway/test_embedding_rebuild.py -q`. Commit
   (`embedding_index.py`, `test_embedding_rebuild.py`).

---

## Task 5 — Per-namespace adequacy gate + golden sets + fallback (I2)

**Files:** create `src/gateway/evaluate/embedding_eval.py`,
`.knowledge/eval/embedding/{section,entity,question}.yaml`,
`tests/gateway/test_embedding_adequacy.py`.

Each namespace ships its own golden set and an independently-falsifiable gate:

- `entity.yaml` — merge / no-merge pairs (co-reference identity). Gate: precision on
  merge pairs at `dedup_identity_threshold` ≥ a recorded floor (the lexical encoder's
  honest operating point). Fallback: alias/lexical-canonical blocking is the active
  authority; embeddings are recall-only. The active fallback is FALSIFIABLE — flip a
  label and the gate fails.
- `section.yaml` — query → relevant-section pairs. Gate: recall@k ≥ floor at
  `retrieval_relevance_threshold`.
- `question.yaml` — gap-signature paraphrase clusters. Gate: cluster purity ≥ floor at
  `demand_gap_threshold`.

```python
@dataclass
class NamespaceGateReport:
    namespace: str
    metric: str            # "precision" | "recall@k" | "purity"
    value: float
    floor: float
    passed: bool
    fallback_active: bool       # True for the lexical fallback
    fallback_falsifiable: bool  # the gate fails on a flipped golden label
    model_version: str

def evaluate_namespace(namespace, index, golden_path) -> NamespaceGateReport: ...
def evaluate_all(index) -> dict[str, NamespaceGateReport]: ...
```

**RED → GREEN → commit:**

1. Author the three golden YAMLs (small, hand-checked, 5–10 items each; validate each
   item before adding the next per the incremental-validation rule).
2. RED: `test_entity_gate_passes_or_fallback_active` — `evaluate_namespace("entity")`
   either passes its floor OR `fallback_active and fallback_falsifiable`. Adversarial:
   a SECOND assertion flips one golden merge→no-merge label and re-runs → the report's
   `passed` (or fallback falsifiability) flips, proving the gate is not a rubber stamp.
3. RED: same shape for `section` (recall@k) and `question` (purity), each with a
   flipped-label negative control.
4. GREEN: implement `embedding_eval.py`. Run → pass.
5. Broader: `pytest tests/gateway/test_embedding_adequacy.py -q`.
6. **Calibration:** with the gates green, set the three §1.2 threshold values to the
   operating points the lexical encoder actually clears; record them + the gate
   report into the ledger §1.2. Commit (`embedding_eval.py`, three golden YAMLs,
   `test_embedding_adequacy.py`).

---

## Eval gate (Phase 2 done)

- `pytest tests/gateway -q` → no NEW failures vs baseline (1998 passed + 4 flaky
  pre-existing `test_doc5_rotate_log` order-dependent); all Phase-2 tests pass,
  adversarial, no monkeypatched core path.
- Green-gate items each with a genuine proving test:
  (a) per-namespace adequacy gate passes OR named fallback active+falsifiable (I2);
  (b) shadow-swap rebuild complete, no half-state to a concurrent reader, wall-time
      recorded (A6, F2) — real concurrent read during rebuild;
  (c) commit-time freshness — commit a page, NN-search the entity namespace, find it
      current-as-of-HEAD (proves incremental upsert, not lazy).
- `wiki eval-retrieval --compare` → recall@10 unmoved (≥ 0.90; baseline 0.926).
- `wiki lint` → no new errors in touched scopes.

## Cursor update on completion

- Ledger §5: flip the Embedding-index row to `green` (or in-progress if partial).
- Ledger §1.2: set «embed.model_version» = `lexical-fallback-v1`; record the three
  calibrated thresholds. Ledger §3: populate the three embedding rebuild-time rows.
- `docs/session-state.md`: one line — Phase 2 status + next = Phase 3.
- Commit with explicit `git add --`.
