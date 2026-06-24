# Hole 2 — Hybrid retrieval (BM25 + local neural embeddings) design spec

**Date:** 2026-06-24 · **Status:** design approved, plan not yet written · **Branch:** `feat/hole2-hybrid-retrieval` (off `main` after the Hole 1 merge).
**Lineage:** continues `docs/260622_rag-retrieval-draft-visibility-brief.md` (the three-hole framing). Hole 1 (draft visibility) is merged (PR #57). This is Hole 2.

## Objective

Close the semantic / vocabulary-mismatch gap in `wiki retrieve`: lay/paraphrased queries that avoid a page's jargon currently miss the right page because retrieval is BM25/FTS-only. Post-Hole-1 re-baseline on the `semantic_mismatch` probe is **recall@10 = 0.381 (8/21)**; the target is **~0.85+**. Fix: a **hybrid retriever** — BM25 fused with a local neural embedding model — with an optional cross-encoder rerank stage. Stay **local-on-ingest** (no hosted API on the ingest or query path; user decision 2026-06-23).

## Why now / prerequisites met

- Hole 1 shipped: the ~1,100 legacy-draft curated pages are now in the candidate pool, so a semantic retriever has real targets to match. Re-baselined at 0.381 (was 0.095 pre-Hole-1).
- The Phase-2 embedding substrate already exists and was built for exactly this: a pluggable `Encoder` Protocol, a `section` namespace, a SQLite vector store with upsert-on-commit and shadow-swap rebuild (`src/gateway/embedding_index.py`). Today it serves only dedup/demand/lint — **not** retrieve. Hole 2 wires a neural encoder into the retrieve path.

## Model decision (research + adversarial analysis)

Deep-research (mid-2026, primary sources: Qwen3-Embedding & EmbeddingGemma arxiv papers, official cards) + a HuggingFace inventory pass + an adversarial analysis under the user's **accuracy-primary, latency-floored** constraint (≤~2× slower acceptable; 3–5× embedding-time increase is fatal).

**Findings:**
- **Qwen3-Embedding** is the strongest locally-runnable open family for English semantic retrieval (8B No.1 MTEB-Multilingual 70.58; MTEB-Eng 0.6B 70.70 / 4B 74.60 / 8B 75.22). All sizes support Matryoshka truncation. Matching **Qwen3-Reranker** family (0.6B/4B/8B) for a two-stage pipeline.
- **EmbeddingGemma-300M** is dominated here — wins only on footprint (578MB), which is not a binding constraint on a 96GB M3 Max.
- **"Optimized versions" on HF are quantizations** (W4A16, AWQ-INT4, GGUF, MLX-DWQ, QAT) — they buy speed/memory, not accuracy. No derivative raises Qwen3's accuracy; more accuracy comes from a larger size or a reranker.
- **LFM2.5-Embedding-350M** (Liquid AI, May 2026, #1 trending) is a real new model but a **speed + multilingual** play, not an English-accuracy leapfrog: 512-token context (vs Qwen3 32K), no confirmed MRL→256, multilingual-tuned, non-standard LFM license. A fast-tier alternative, not the accuracy pick.

**Adversarial conclusions that shape the build:**
1. The "3–5× fatal" latency risk attaches to the **reranker** (per-query, user-facing, K forward passes) and **ingest/full-rebuild** (offline, amortizable) — **not** to bi-encoder query embedding, which stays absolute-small (tens of ms) even at 4B. So bi-encoder size can go big for accuracy; the latency discipline belongs on the reranker + ingest batch.
2. **256-dim and 4-bit are accuracy haircuts inherited from a speed-first framing.** 256 was calibrated for the lexical-fallback encoder; truncating Qwen3-4B's 2560→256 is 90% truncation (MRL degrades >80%), which can erase the reason to pay for 4B. Under accuracy-primary, **do not pin 256-dim or 4-bit** — sweep the dimension (256/512/native), run higher precision (8-bit/bf16) since bi-encoder speed is cheap. Storage at this corpus scale is trivial (a few hundred MB).
3. **Establish the accuracy ceiling first, then trim to the latency budget** — not climb up from the smallest model (that was speed-primary logic).
4. The reranker is the highest accuracy-per-point lever but only lifts recall@10 when reranking a **wide** bi-encoder pool (top-100 → top-10); bound K and use the small 0.6B reranker.
5. **Scope:** swapping the encoder invalidates the per-namespace cosine operating points, which are load-bearing for the Phase-3 **dedup/merge-map gates**. So the neural encoder serves the **retrieve/`section` path only**; dedup (`entity`) and demand (`question`) stay on `lexical-fallback-v1`. A second encoder instance, not a global swap.

**Provisional pick (to be confirmed by the bake-off):** Qwen3-Embedding-4B, 8-bit, widened dimension (test 512/native), bi-encoder + BM25; `Qwen3-Reranker-0.6B-seq-cls` deferred to a probe-gated second stage. Not 8B (≈0.6 MTEB pt over 4B for ~2× cost). The precise pick is settled empirically — see the bake-off.

## Architecture — hybrid retrieve, model-agnostic

`retrieve()` (`src/gateway/ops/retrieve.py`) gains a hybrid path. The Hole-1 invariants stay: placeholder-section gate (`is_placeholder_section`), `draft="true"` annotation, budget assembly.

1. **Lexical candidates** — `search_fts` (existing BM25/authority order), top-N.
2. **Dense candidates** — embed the query with a neural `Encoder`; cosine-NN over the `section` namespace in `embedding_index`. Brute-force numpy matmul is adequate at ~15–20k sections (no HNSW/FAISS needed at this scale). Top-N.
3. **Fuse** — **Reciprocal Rank Fusion** (RRF): `score(d) = Σ 1/(k_rrf + rank_i(d))` across the lexical and dense lists. Rank-based, no score-normalization fragility, one robust constant. Weighted-score fusion is an alternative the bake-off can sweep.
4. **Optional rerank** — a cross-encoder re-scores the fused top-K (bounded K, e.g. 20–50). Config-gated; off by default until the probe shows the bi-encoder fusion alone misses target.
5. **Assemble** — existing block builder (placeholder skip + draft annotation + budget).

Encoder identity, output dimension, fusion method/constant, rerank on/off + K are read from config, so one code path serves every bake-off config and the production pick.

## The bake-off harness (calibration — user-chosen settle method)

A dev command (e.g. `wiki eval-embedding-bakeoff`) that, per `(model, dim, fusion, ±reranker)` config:
- builds the `section`-namespace embeddings for that encoder/dim (or a representative subset for the accuracy signal),
- runs the **`semantic_mismatch` probe** through the **real hybrid retrieve path**: recall@10 + the Hole-1 G-NEG controls (placeholder-pollution = 0; finalized-page non-displacement),
- **times ingest-batch throughput and per-query latency on the actual M3 Max** (the numbers benchmarks can't give us),
- emits a **frontier table** (recall vs latency per config).

The user picks the point on the accuracy/latency frontier. The winner locks into `«embed.retrieval_model_version»`, the `section`-namespace output dimension, the fusion constant, and recalibrated cosine operating points. This is what turns "accuracy-primary with a latency floor" from a guess into a measurement.

Candidate sweep (initial): Qwen3-Embedding-{0.6B, 4B} × dim {256, 512, native} × {fusion: RRF} × {reranker: off, Qwen3-Reranker-0.6B@K=20}. LFM2.5-Embedding-350M optionally included as the fast-tier reference. 8-bit precision for the bi-encoders.

## Scoping & safety

- **Second encoder, retrieve-path only.** `entity`/`question` namespaces stay on `lexical-fallback-v1`; the Phase-3 merge-map/dedup gates are calibrated to it and must not move.
- **Derived & rebuildable.** The dense `section` index is gitignored, self-healing, shadow-swap rebuildable (Phase-2 machinery). Markdown stays canonical.
- **Local & offline.** Neural encoder runs locally (MLX or GGUF/llama.cpp on Apple Silicon). No API on ingest or query. Model weights are a one-time local download; record the active model in `«embed.retrieval_model_version»`.
- **Gate-guarded (pre-merge gate must hold):**
  - `eval-retrieval` recall@10 ≥ 0.90 on the easy goldens — the hybrid must not regress lexical-easy retrieval (RRF keeps BM25 hits, so this should hold by construction; verify).
  - merge-map eval: 0 regressions (untouched — dedup encoder unchanged).
  - embedding namespaces OK (`entity`/`question` unchanged; `section` retrieval is a new, separately-gated metric).
  - **New acceptance metric:** probe recall@10 ≥ target (~0.85) on `semantic_mismatch`, wired as a retrieve-path eval (the Hole-1 `probe_retrieve.py` scorer promoted into the harness).
- **Dimension not pinned at 256** — bake-off sweeps it; operating points recalibrated for the winner.

**Plug-in points (real code):**
- `src/gateway/embedding_index.py` — add a neural `Encoder` implementation (MLX/GGUF backend) behind the existing Protocol; a `section`-namespace query/NN method; configurable output dimension.
- `src/gateway/ops/retrieve.py` — hybrid fusion (RRF) in `retrieve()`; optional rerank stage; config plumbing.
- bake-off harness — new dev command/script reusing `semantic_mismatch.yaml` + `probe_retrieve.py`.
- `NAMESPACES` / operating-point config — recalibrated `section` operating point for the chosen encoder.

## Acceptance

- Probe recall@10 on `semantic_mismatch` climbs from 0.381 toward ~0.85+ on the chosen config.
- G-NEG-1 (placeholder pollution = 0) and G-NEG-2 (no finalized displacement) still hold (Hole-1 invariants).
- Pre-merge gate green (easy-goldens recall@10 ≥ 0.90, merge-map 0 regressions, embedding namespaces OK).
- Measured M3-Max latency within the user's budget (≤~2× the small-model baseline; reranker K + size chosen to stay off the 3–5× fatal zone).

## Non-goals

- Not touching the dedup (`entity`) or demand (`question`) encoders — Phase-3 gates stay on lexical-fallback.
- Not Hole 3 (finalize/cull the perma-draft backlog) — separate curation track.
- Not a hosted/API retriever (Voyage etc.) — local-only decision stands.
- Not a multi-vector/ColBERT index (would change the index structure; single-vector dense namespace only for v1).

## Open items the plan must resolve

- The neural-encoder runtime: MLX (`mlx-community` builds) vs GGUF/llama.cpp — pick per the bake-off's latency results and packaging simplicity; both are local. Mock the model in unit tests (no 4B download in CI).
- Exact RRF constant `k_rrf` and candidate-pool size N — bake-off-tuned.
- How the dense index rebuild integrates with the existing shadow-swap rebuild and the watcher/commit upsert path.
- Operating-point recalibration procedure for the `section` namespace under the new encoder.
