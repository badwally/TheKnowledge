# Hole 2 bake-off — results & locked decision (2026-06-24)

> **Update 2026-06-25 — the "locked decision" below is being PROPERLY completed.**
> The 0.6B-only run never tested the 4B (the obvious middle model in the matrix) or the
> 8B, so the model choice was not actually settled — it is being finished now (4B-4bit-DWQ
> and 8B-4bit-DWQ through the same instruction+cache+memo pipeline; frontier table → user pick).
>
> **bf16 bug found + fixed (commit `68d3af8a`).** The encoder was validated ONLY on
> 0.6B-8bit, which emits float32. The quantized 4B/8B `*-DWQ` builds emit **bfloat16**,
> whose PEP-3118 buffer numpy cannot read directly (`Item size 2 ... format B item size 1`)
> — the encoder crashed on first embed for both bigger models. Fix: route non-ndarray mlx
> output through `.tolist()` before `np.asarray` (float32 fast-path preserved, no `mlx.core`
> import so the stub/fake test path stays CI-safe). Verified on the real 4B (2560-dim,
> L2-normalized). Without this fix the 4B/8B half of the bake-off could not run at all — so
> the prior "8B not needed" conclusion was reached on a pipeline that could not have measured
> the 8B. Productionization unit tests (encoder/cache/instruction/memo) also landed in `68d3af8a`.


Calibration of the hybrid-retrieval config (C3 of `docs/plans/2026-06-24-hole2-hybrid-retrieval-build-plan.md`), run on the **real corpus** (5,866 pages / 28,435 sections / 4,034 canonical pages → 19,317 section vectors) against the `semantic_mismatch` probe (21 paraphrase queries). Local MLX on the M3 Max via `mlx-embeddings`.

## Results (0.6B-8bit bi-encoder)

| Config | recall@10 | recall@20 | recall@50 | query latency p50 |
|---|---|---|---|---|
| lexical-only (pre-Hole-2 baseline) | 0.381 | — | — | ~30ms |
| hybrid, **no** query-instruction | 0.429 | — | — | — |
| hybrid **+ query-instruction** | 0.619 | 0.810 | **0.857** | 219ms |
| dense-only + query-instruction | **0.667** | 0.810 | — | ~200ms |
| + Qwen3-Reranker-0.6B-seq-cls | **0.333** ⛔ | — | — | 5.2s |

Rebuild (full corpus, 0.6B): **65 min** (~200ms/section; document sections are long). 8B projected at **5–10 h**.

## Findings

1. **The 0.6B is sufficient for retrieval — the 8B is not needed.** recall@50 = 0.857: the correct page is in the top-50 for 18/21 queries. The gap is *ranking into top-10*, not retrieval power. Only 3 queries have no answer in the top-50 (the only place a bigger model could help by *retrieving* what the 0.6B can't).
2. **Query-instruction prefix is the dominant lever** (+0.19 recall). Qwen3-Embedding is asymmetric: queries get `Instruct: …\nQuery: {q}`, documents stay raw. The naive symmetric pipeline left most of the model's value unused.
3. **The Qwen3-Reranker-0.6B actively harms** (0.619 → 0.333): it demotes precise concept answers (e.g. `active-vs-passive-qt`, bi-encoder rank 3 → reranker rank 15–31) below topically-related entity pages (jp-morgan, central-banking commentary), even with the instruction format. The reranker upside the design assumed does not materialize on this curated corpus. **Reranker is out.**
4. **BM25 fusion slightly hurts on pure-paraphrase queries** (dense-only 0.667 > hybrid 0.619 @10) — RRF rewards lexically-similar-but-wrong pages BM25 surfaces. But BM25 is still needed for lexically-easy queries, so the fix is dense-*weighted* fusion, not dropping BM25.
5. **Latency was an implementation bug, not the model:** 830ms → **219ms** via (a) memoizing the encoder (it was reloading the model every query) + (b) an in-memory section-vector cache (NN was re-reading all 19k vectors from sqlite per query). Query *embedding* itself is only ~20ms.

## Locked decision

- **Model:** `mlx-community/Qwen3-Embedding-0.6B-8bit`, native 1024-dim (no Matryoshka truncation needed at this scale). **Not** the 8B (uncertain ~+0.1 for a 5–10 h rebuild + permanently slower ingest) and **not** EmbeddingGemma.
- **Query asymmetry:** instruction-prefixed queries (`embed_query`), raw documents.
- **Fusion:** dense-weighted RRF — **to be tuned and validated against BOTH the probe and the easy goldens** (must keep `eval-retrieval` recall@10 ≥ 0.90 on lexical) before the final lock.
- **No reranker.**
- **Realistic recall:** ~0.62–0.67 @10 / ~0.81 @20 — a **~2× lift** off 0.381. Hitting 0.85 @10 is a later goal needing better *content* (the 8B's ceiling, or Hole-3 curation), not more ranking effort.

## Validated code (the encoder path the stub-tested #60 machinery needs to actually work)

These were validated by measurement; they need unit tests before merge (productionization, follow-up branch):
- `MlxQwen3Encoder`: real `mlx-embeddings` API (`load()→(model,tok)`, `generate(...).text_embeds`), `embed_query()` instruction prefix, `max_length`.
- `retrieval_encoder()`: memoized per spec (model loads once).
- `retrieval_index.dense_section_hits`: in-memory vector cache + `embed_query` for the query side.

## Remaining (productionization → activation, follow-up build)

1. Unit-test the encoder/cache/instruction/memo changes (stub encoder; the neural path stays uncovered in CI by design).
2. Tune dense-weighted fusion; validate recall on the probe AND no regression on the easy goldens.
3. D1: make hybrid the default retrieve path (thread `include_drafts` through `_hybrid_hits` — carry-forward finding) under `WIKI_RETRIEVAL_ENCODER=mlx:mlx-community/Qwen3-Embedding-0.6B-8bit:1024`.
4. Rebuild the production retrieval index once; pre-merge gate; PR.
