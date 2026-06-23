# RAG Retrieval Diagnostic — the curated layer is invisible to `wiki retrieve`

**Date:** 2026-06-22 · **Status:** diagnosis complete, fix not yet implemented · **Diagnosed against:** main @ `305b4136` (the `fix/authorship-loop-comprehensive` branch this was drafted on is now merged + deleted; implement the fix on a new branch `fix/rag-draft-visibility` in an isolated worktree)
**Lineage:** continues `docs/260609-rag-retrieval-review` line and `docs/260620_librarian-rag-as-built-review.md`.

## One-line finding

`wiki retrieve` — the default, every-query grounding path for agents — hard-excludes `draft: true` pages, and ~30% of concepts, ~30% of entities, and **92% of synthesis** pages are perma-draft from legacy migration. So roughly **1,100 curated pages are invisible to the default retrieval path**. This is a larger, cheaper-to-fix problem than the "we need embeddings" hypothesis that started the investigation, and it must be fixed before any embedding work is worth doing.

## How we got here

The investigation began as "what's the embedding strategy, and is the lack of a real embedding model a big hole?" The answer reframed the question:

- The system uses **no neural embeddings**. Encoder is a lexical fallback (`lexical-fallback-v1`, 256-dim hashed n-grams, `src/gateway/embedding_index.py:107`). It's used only for commit-time dedup (`entity` namespace), demand-ledger clustering (`question` namespace), and fragmentation lint. **Retrieval is BM25/FTS5 only** — embeddings are not consulted in the retrieve path.
- The three-way framing the user proposed (current BM25 vs embedding model vs NotebookLM) is a category error: BM25 and embeddings are both *retrieval*; NotebookLM is *synthesis* downstream of retrieval. NotebookLM is not a retrieval fix and inherits whatever retrieval feeds it.

So the real question was: how good is the current retrieval layer, and where does it fail. We built a probe to measure it.

## The probe and what it measured

We reused the validated eval harness (`wiki eval-retrieval --goldens <path>`, same recall@k/MRR scoring) with a hand-built **semantic-mismatch golden set** of 21 queries: deliberately lay/paraphrased queries that avoid each target page's jargon vocabulary, plus 3 lexically-easy controls. Ground truth set independently from the page list, then every miss triaged by hand (reading the page + the actual retrieved results).

| Query set | Layer measured | recall@10 |
|---|---|---|
| Existing golden set (27 q, lexically easy) | FTS index | **0.93** |
| Hard probe (21 q, paraphrased) | FTS layer (`wiki search`, best case) | **~0.33** |
| Hard probe (21 q, paraphrased) | **actual `wiki retrieve`** (agent path) | **~0.10** (2/21) |

Two distinct gaps fell out of the triage:

1. The FTS layer drops from 0.93 (easy) to ~0.33 (paraphrased) — a genuine **vocabulary-mismatch gap** (Hole 2, embeddings territory).
2. The actual `wiki retrieve` command scores **~0.10**, roughly a third of the FTS ceiling on the *same* queries — a second, larger, embedding-independent gap in the assembly layer (Hole 1).

The decisive tell: the 3 near-exact-title **controls** ("mesolimbic dopamine system", "federated learning across silos", "Apple Neural Engine on-device inference") **pass in `wiki search` (concept ranked #1–#2) but fail in `wiki retrieve` (absent even at k=20)**. That comparison needs none of our paraphrase judgment to hold, so the core finding is robust.

## Hole 1 — root cause, pinned

`wiki retrieve` hard-excludes draft pages from the candidate pool *before ranking*:

1. `retrieve()` defaults `include_drafts=False` (`src/gateway/ops/retrieve.py:160`); `retrieve_op` never overrides it (`retrieve.py:282`).
2. `search_fts` translates that into SQL `WHERE p.draft = 0` (`src/gateway/search_index.py:385-386`) — drafts removed from the candidate pool *before* BM25/authority ranking, not merely demoted.
3. `wiki search` defaults `include_drafts=True` (`search_index.py:356`), so it sees the same pages and ranks them #1. That is the entire search-vs-retrieve divergence.

**Proof (perfect correlation):** the 3 missed control concepts are all `draft: true`; the 3 that survived `wiki retrieve` (`active-vs-passive-qt` @ rank 5, `automated-lockbox` HIT, `30-year-cash-flow-projection` HIT) are all non-draft.

**Blast radius (why a quiet default is catastrophic):**

| Layer | Draft (invisible to `retrieve`) |
|---|---|
| concepts | 382 / 1314 (29%) |
| entities | 335 / 1100 (30%) |
| **synthesis** | **400 / 433 (92%)** |
| mocs | 4 / 28 (14%) |

Because MOCs are only 14% draft, the surviving non-draft hubs plus source pages fill every block — exactly the type-mix the probe saw (MOCs + sources, zero concepts). The result composition was a fingerprint of the draft filter.

**Secondary effect (present, not the cause):** `_authority_key` (`search_index.py:461`) up-weights inbound-link count (`_W_AUTHORITY * log1p(inbound)`), so MOC hubs outrank leaf concepts even among non-draft pages. Its `_DRAFT_PENALTY = -2.0` and `+1.0` concept/entity `_TYPE_BOOST` — the machinery meant to lift canonical pages over mentions — never fire on drafts, because the SQL filter removed them first.

**The design tension (why this isn't a blind flag flip):** draft exclusion was principled. The draft model deliberately downgrades citation-grounding (hard rule #3) to a lint warning until `wiki finalize`. Excluding unfinalized pages from grounding context protects citation fidelity. The choice was sound in isolation. It collides with one fact: legacy migration committed the entire imported concept/entity/synthesis layer as `draft: true` and it was never finalized. So "don't ground on unfinalized pages" silently became "don't ground on ~90% of the curated knowledge layer." It is the inert-in-production pattern from `docs/MULTI-AGENT-BUILD-PLAYBOOK.md` — a guard that passed its tests and then ate the feature on real data.

## The three holes and the sequence

1. **Hole 1 — draft exclusion in `wiki retrieve`** (mechanism pinned above). Cheapest, embedding-independent, and the **prerequisite for everything else**: if `retrieve` keeps filtering drafts, a future semantic retriever's draft-concept hits get filtered out too, so Hole 2 work is wasted until this lands.
2. **Hole 2 — semantic / vocabulary-mismatch gap.** Even the best lexical layer (raw BM25) gets ~0.33 on paraphrased queries vs 0.93 on lexically-easy. Fix is a hybrid retriever (BM25 + a real embedding model, fused). Local SOTA options: EmbeddingGemma-300M or Qwen3-Embedding-0.6B (Matryoshka→256, MLX/GGUF), with `model2vec`/potion as a speed-floor spike; hosted SOTA option: Voyage (`voyage-3-large` + `voyage-context-3` + `rerank-2.5`), but Voyage is API-gated and breaks the local-on-ingest constraint. Comes **after** Hole 1.
3. **Hole 3 — content debt.** The perma-draft backlog itself: legacy-import stubs reading `_(needs population from legacy import)_`, 758 orphans. No retrieval mechanism fixes an empty page. Runs as a parallel curation loop (`wiki finalize`), partly automatable.

NotebookLM (`wiki query`) is orthogonal — downstream synthesis, unaffected, not a retrieval fix.

## Prospective actions

### Immediate — Hole 1 fix (next session)

Options, in recommended order:

- **A — Demote, don't exclude (recommended).** Stop hard-filtering drafts in `retrieve`; let them into the candidate pool and rely on the `_DRAFT_PENALTY` already in `_authority_key` (currently dead code for the retrieve path, since the SQL removes drafts first) to rank them below finalized pages. A draft concept that is the best match surfaces; a finalized page outranks it when one competes. The empty-section skip (`retrieve.py:195`) already drops truly-empty stub sections. Tune `_DRAFT_PENALTY` so stubs stay down but real drafts surface; the probe is the before/after gate.
- **D — Content gate (compose with A).** Admit drafts whose matched section is *populated*; exclude placeholder stubs (detect `_(needs population...)_` markers, not just empty strings). More surgical on the thin-stub worry.
- **B — Flip `include_drafts=True`.** Simplest, bluntest; drafts compete minus the 2.0 penalty.
- **C — Finalize the backlog.** The "correct" content fix (this is Hole 3), but ~1,100 pages of work and it doesn't fix the mechanism for future drafts.

**Recommendation: A, optionally tightened with D, with the probe as the regression test.** This is a citation-grounding behavior change, so it warrants a deliberate design pass (the brainstorming flow was started for this and paused for this handoff).

Open design questions to resolve before implementing:
- Should draft sections in the assembled block be **annotated** (e.g. `draft="true"` on the `<page>` tag) so a consuming agent knows the provenance is unfinalized? Leaning yes — cheap, preserves the citation-fidelity intent while restoring visibility.
- Does the fix touch `wiki answer` (which calls `retrieve`)? Yes by inheritance — confirm acceptable.
- Should the hard-probe goldens become a **permanent eval fixture** (e.g. `.knowledge/eval/retrieval/semantic_mismatch.yaml`) wired into the gate, so this can't regress silently? Leaning yes.

### Later — Hole 2 (separate spec)
Hybrid retrieval. Decision axis: relax "local" for Voyage quality + reranker, or hold "local" with EmbeddingGemma/Qwen3. Re-run the probe after Hole 1 to re-baseline the true semantic ceiling before committing model/infra.

### Parallel — Hole 3 (curation loop)
`wiki finalize` the legacy-import drafts; cull dead stubs. Partly an LLM-assisted batch.

## Reproduction

Probe artifacts were built in the (ephemeral) session scratchpad; the load-bearing one (the goldens) is reproduced in Appendix A so it survives. Method:

```bash
# baseline on the existing easy golden set
.venv/bin/wiki eval-retrieval --compare --k 10

# hard probe through the FTS layer (matches wiki search)
.venv/bin/wiki eval-retrieval --goldens <semantic_mismatch.yaml> --k 10

# hard probe through the ACTUAL retrieve path (the one that scores ~0.10):
#   run each query via `wiki retrieve "<q>" --domain <d> --k 10 --json`
#   and check whether the expected slug is in sources[].slug  (see Appendix B)
```

Key divergence to re-demonstrate in 30 seconds:
```bash
.venv/bin/wiki search  "mesolimbic dopamine system" --domain glp1-reward-modulation   # concept ranks #1
.venv/bin/wiki retrieve "mesolimbic dopamine system" --domain glp1-reward-modulation --k 20 --json  # concept ABSENT (draft:true)
```

---

## Appendix A — semantic-mismatch probe goldens (durable copy)

Save to `.knowledge/eval/retrieval/semantic_mismatch.yaml` (or pass via `--goldens`). Schema matches the existing goldens: `q` / `domain` / `expect` (recall@k passes if ANY expected slug is in top-k).

```yaml
queries:
  # ---- glp1-reward-modulation (jargon-dense) ----
  - q: "why do people on weight-loss shots feel less pleasure and lose their drive"
    domain: glp1-reward-modulation
    expect: [reward-deficit-and-anhedonia]
  - q: "how these appetite drugs change the brain's feel-good chemical circuitry"
    domain: glp1-reward-modulation
    expect: [mesolimbic-dopamine-system-modulation]
  - q: "a medication to bring back motivation lost while using appetite suppressants"
    domain: glp1-reward-modulation
    expect: [the-clinical-application-of-bupropion-a-dopamine-and-norepinephrine-reuptake-inhibitor-to-counteract-glp-1-induced-anhedonia-and-restore-patient-motivation]
  - q: "could these injections protect the aging brain against memory-loss conditions"
    domain: glp1-reward-modulation
    expect: [neurodegenerative-disease-prevention]
  - q: "the gut-to-brain nerve route that signals the reward area to stop eating"
    domain: glp1-reward-modulation
    expect: [glp-1-neurons-in-the-nucleus-of-the-solitary-tract-project-directly-to-the-ventral-tegmental-area-and-nucleus-accumbens-to-control-for-food-intake-alhadeff-et-al-2012]
  # ---- edge-ai-agentic ----
  - q: "running machine-learning models directly on iphone processors"
    domain: edge-ai-agentic
    expect: [apple-silicon-and-neural-engines]
  - q: "keeping data encrypted even while it is being processed on a device"
    domain: edge-ai-agentic
    expect: [confidential-computing-and-secure-enclaves]
  - q: "brain-inspired low-power chips that mimic how neurons fire"
    domain: edge-ai-agentic
    expect: [custom-and-neuromorphic-silicon]
  - q: "a standard that lets autonomous AI assistants talk to one another"
    domain: edge-ai-agentic
    expect: [agent-to-agent-a2a-protocol]
  # ---- trading-and-markets ----
  - q: "the year stocks and bonds fell together and wrecked balanced retirement funds"
    domain: trading-and-markets
    expect: [60-40-portfolio-2022-collapse, 2022-bond-bear-market]
  - q: "central bank shrinking its balance sheet by selling bonds versus letting them mature"
    domain: trading-and-markets
    expect: [active-vs-passive-qt]
  - q: "how much share prices move when investors collectively buy more stock"
    domain: trading-and-markets
    expect: [aggregate-equity-demand-elasticity]
  # ---- data-collectives ----
  - q: "why a new data-sharing network has little value until enough members join"
    domain: data-collectives
    expect: [cold-start-problem]
  - q: "shared resources many can use but are hard to fence off, like fisheries or grazing land"
    domain: data-collectives
    expect: [common-pool-resources]
  - q: "training one shared model across companies without pooling their raw records"
    domain: data-collectives
    expect: [cross-silo-federated-learning]
  - q: "rules letting customers share their bank-account data with outside apps"
    domain: data-collectives
    expect: [consumer-driven-banking]
  # ---- condo-software ----
  - q: "a long-range forecast of a building's major repair funding needs"
    domain: condo-software
    expect: [30-year-cash-flow-projection]
  - q: "a service that receives and processes homeowner dues checks automatically"
    domain: condo-software
    expect: [automated-lockbox]
  # ---- CONTROLS (lexically easy — should pass; fail ONLY because draft-excluded) ----
  - q: "Apple Neural Engine on-device inference"
    domain: edge-ai-agentic
    expect: [apple-silicon-and-neural-engines]
  - q: "federated learning across silos"
    domain: data-collectives
    expect: [cross-silo-federated-learning]
  - q: "mesolimbic dopamine system"
    domain: glp1-reward-modulation
    expect: [mesolimbic-dopamine-system-modulation]
```

## Appendix B — triage script (scores the actual `wiki retrieve` path)

The eval harness scores the FTS layer, not the full `retrieve` assembly. This script scores the real agent path (the one that returns ~0.10):

```python
import subprocess, json, yaml
G = yaml.safe_load(open("<path to semantic_mismatch.yaml>"))
for e in G["queries"]:
    q, dom, exp = e["q"], e.get("domain"), e["expect"]
    cmd = [".venv/bin/wiki", "retrieve", q, "--k", "10", "--json"]
    if dom: cmd += ["--domain", dom]
    man = json.loads(subprocess.run(cmd, capture_output=True, text=True).stdout)
    slugs = [s["slug"] for s in man.get("sources", [])]
    hit = any(x in slugs for x in exp)
    print(f"[{'HIT ' if hit else 'MISS'}] {q[:60]}")
    if not hit:
        print(f"        expect {exp}  got {slugs}")
```

Expected current result: ~2/21 HIT (the two non-draft condo concepts). After the Hole 1 fix, this should climb toward the FTS ceiling (~0.33) and the 3 controls should all flip to HIT.

---

## Appendix C — Negative controls + the stub-pollution HARD GATE (real slugs, verified 2026-06-23)

Appendix A measures only the *upside* (recall — did a draft surface). A fix that surfaces good drafts **and** floats placeholder stubs into the grounding block passes Appendix A and the `eval-retrieval` regression. This appendix closes that gap with verified, falsifiable controls. **This is the inert-in-production trap from `docs/MULTI-AGENT-BUILD-PLAYBOOK.md`: a guard (or in this case a fix) that passes its happy-path test and then misbehaves on real data. Do not declare the fix done on recall alone.**

### What the legacy drafts actually look like (verified, not assumed)
The dominant legacy-import draft is **hybrid**, not an empty stub. Verified on disk 2026-06-23:
- `wiki/concepts/mesolimbic-dopamine-system-modulation.md` (`draft: true`, 171w): real lede paragraph + populated `## Methods` (3 wikilinks), then `## Summary` / `## Key claims` / `## Sources` / `## Related` each a literal `_(needs population from legacy import)_`.
- `wiki/concepts/apple-silicon-and-neural-engines.md` (`draft: true`, 105w): same shape.
- **177 pages** carry the `_(needs population from legacy import)_` marker.

Two consequences that change the fix:
1. The empty-section skip (`retrieve.py:195`, `if not text: continue`) does **NOT** drop these sections — the placeholder is non-empty text. Under **option A-alone**, a query matching a `## Summary` section returns the literal string `_(needs population from legacy import)_` to the agent as grounding context. That is the pollution, concretely.
2. The probe's positive targets (`mesolimbic-dopamine-system-modulation`, `apple-silicon-and-neural-engines`) **are** these hybrid pages — their value is the lede + Methods. So **option D must gate at SECTION level** (drop the placeholder sections, keep the lede + Methods), **not page level**. Page-level exclusion would kill the very content Appendix A's positive controls depend on. This is the sharp form of open question Q1.

### The three gates — all must hold (recall up, pollution zero, no displacement)

**G-POS (recall, from Appendix A):** the 3 lexically-easy draft controls flip to HIT; overall climbs off ~2/21.

**G-NEG-1 (stub-pollution — the HARD, un-gameable gate):** across the FULL probe run, the assembled `wiki retrieve` blocks contain **ZERO** occurrences of `_(needs population from legacy import)_`. One grep over the `--json`/text output. If the count is > 0, the fix is floating placeholder stubs into grounding context — **STOP and fix before claiming done.** This single invariant is the corner that must not be cut:
```bash
# after the fix — run every probe query through wiki retrieve and grep the blocks
for q in "why do people on weight-loss shots feel less pleasure" \
         "running machine-learning models directly on iphone processors" \
         "mesolimbic dopamine system" "Apple Neural Engine on-device inference"; do
  .venv/bin/wiki retrieve "$q" --k 10 2>/dev/null
done | grep -c "needs population from legacy import"
# REQUIRED OUTPUT: 0   (any positive count = stub pollution = not done)
```

**G-NEG-2 (no displacement):** the finalized (non-draft) pages that are correct answers must NOT be displaced by newly-admitted drafts. Verified-finalized control pages (no `draft:` key on disk 2026-06-23): `active-vs-passive-qt`, `automated-lockbox`, `30-year-cash-flow-projection`. Every query that HITs a finalized page today must STILL HIT after the fix. The `eval-retrieval --compare ≥0.90` on the easy goldens covers most of this; assert these three explicitly as well.

### Evidence-before-done (verification-before-completion)
Do not report the fix complete without pasting: (a) the G-POS before/after triage counts, (b) the **G-NEG-1 grep count = 0**, (c) the G-NEG-2 finalized-control results. A green that shows only (a) is the recall-only false green this appendix exists to prevent.
