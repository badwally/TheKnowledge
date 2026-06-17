# YouTube corpus-gap remediation — staged plan

**Date:** 2026-06-17
**Status:** Staged (planning complete; execution gated — see Sequencing)
**Trigger:** promote-to-persistent URL-drop fix (PR #17, `d005d17d`) + YouTube-aware filter fix (`a4b11ac2`). With both adapters now working, re-examine prior research projects for YouTube material that never reached a corpus / synthesis.

---

## 1. Detection result (authoritative)

Probe: for each `raw/youtube/*.md`, check `nlm_corpus_ids` frontmatter (the gateway's own idempotency key) for corpus membership, and attribute orphans via `nlm/source_maps/<session>.json`. Reproduce with:

```
.venv/bin/python - <<'PY'
import sys; sys.path.insert(0,"src")
from pathlib import Path; from gateway import frontmatter as fm
never=incorpus=0
for p in sorted(Path("raw/youtube").glob("*.md")):
    front,_=fm.parse(p.read_text())
    (incorpus:=incorpus+1) if (front.get("nlm_corpus_ids") or []) else (never:=never+1)
print(incorpus, never)
PY
```

**340 YouTube sources: 103 in ≥1 corpus, 237 never in any corpus.**

The starting hypothesis ("the promote bug dropped YouTube in all prior queries") is **not** supported. Three distinct causes are tangled together; only one is the promote bug.

| Bucket (YouTube not in any corpus) | # YT | Cause | Class |
|---|---|---|---|
| `ai-temporal-video` | 86 | Domain **never bootstrapped** — no policy, no notebook. Nowhere to promote to. | C (no corpus) |
| `glp1-reward-modulation` | 48 | Persistent notebook is an **empty stub** (`sources_count: 0`). Whole-corpus gap. | C (dead corpus) |
| Orphan/abandoned sessions (bare notebook ids absent from `notebooks.yaml`: `311f9069`, `a0b35624`, `db1e4b75`, `0a9d3d94`, `3de60ed7`, `92cefb57`) | ~37 (overlaps below) | Research sessions never promoted to a domain. | C (abandoned) |
| `convergent-ai-brain` | ~14 | Promoted sessions; YouTube dropped on persist. | **A (promote bug)** |
| `ai-native-business` | ~4 | Same — partial drop (2 others *did* land). | **A (promote bug)** |
| `risksystems` | 2 | Same. | **A (promote bug)** |
| No `source_map` at all (ungated direct-adapter harvests, e.g. orita competitive-set) | 16 | Harvested outside the research gate by design. | Discard |
| ~~`agentic-data-layer`~~ | 30 | Pre-fix promote-failures, **being re-run on the fixed tool**. | Excluded |
| ~~`semantic-models`~~ | 4 | In-progress (user driving the loop). | Excluded |

Counts for A-class domains and orphan sessions overlap (a YouTube id can appear in multiple session source_maps); execution re-derives the exact per-domain manifest with the probe above filtered by domain.

**Cross-check that confirms the diagnosis:** every pre-fix domain with promoted research sessions but **zero** YouTube tagged (risksystems' main corpus, `condo`, `condo-capital-infra`, convergent's main corpus) shows the **filter regression** (0-accept) suppressed YouTube *upstream* of promote in most runs — so the promote bug literally had nothing to drop there. Domains that *did* get YouTube in: `edge-ai-agentic` 97/98, `orita-cmo` 4/4.

---

## 2. Sequencing rule (the binding constraint)

A concurrent research session (semantic-models loop, separate window) is exercising the YouTube **adapter**. The correction work and that session contend on **different** resources:

| Operation | Hits our YouTube API/key? |
|---|---|
| `wiki nlm-sync` / `nlm-add` (WS-1, WS-3, WS-2 backfill) | **No** — `nlm.py:218` `source_add_url`; NotebookLM (Google) fetches the transcript on its side. Transcript already in `raw/`. |
| `wiki query` re-synthesis | **No** — queries the notebook. |
| Fresh `wiki research --execute` discovery | **Yes** — the YouTube adapter does search + transcript fetch on our key. |

**Rule:** the now-track (backfill + re-synthesis over already-materialized `raw/` sources) shares **no** rate-limit bucket with the concurrent session and can run anytime. **Only fresh-discovery runs** (expanding a corpus with new YouTube beyond what is already in `raw/`) must be **serialized after** the semantic-models loop completes — same shared-key lesson as the S2 concurrency note. When bursting `source_add_url` calls (e.g. ai-temporal-video's 86), throttle with `nlm-sync --limit N` so NotebookLM's own ingestion isn't rate-limited.

> Hold gate: do not start autonomous execution while the user is driving the semantic-models loop. This document stages the work; the user triggers each workstream.

---

## 3. Workstreams

### WS-1 — Promote-bug backfill (now-track; mechanical, high-confidence)

Domains: `convergent-ai-brain`, `ai-native-business`, `risksystems`.

Per domain:
1. `wiki nlm-sync <domain>` — the live run uses the PR-#17 URL-recovery path to add the dropped YouTube via `source_add_url`. `--limit` to throttle if needed.
2. Re-run the affected synthesis: `wiki query "<original session question>" --domain <domain> --draft` (look up the question in `nlm/notebooks.yaml` → `sessions[].query`).
3. `wiki cite` + `wiki finalize` per regenerated page.
4. **Verify:** re-run the §1 probe filtered to the domain — YouTube gap should drop to ~0.

### WS-2 — Dead/missing corpora (mixed track)

**`glp1-reward-modulation`** (48 YT; now-track sync, low synthesis value — biomedical, YouTube is conference-talk tier):
1. `wiki nlm-sync glp1-reward-modulation` (syncs the 48 YT + any other tagged raw not yet in the stub corpus).
2. Corpus-quality gate, then `wiki query` if synthesis is wanted. Decide whether this domain is worth reviving before spending synthesis quota.

**`ai-temporal-video`** (86 YT; highest YouTube value — it is a video domain). **D1 resolved: stands up as its own domain.**

> **Subject-matter finding (from sampling the 86 sources):** the slug is misleading — this is temporal video *understanding*, NOT video generation. "temporal" appears 215× across titles; text-to-video/diffusion is essentially absent (1 hit). The bootstrap description must scope to understanding or the policy will inherit a wrong generation assumption.

**Canonical bootstrap description** (pass verbatim to `wiki bootstrap-domain`):

> AI methods for temporal understanding of video — recognizing, localizing, grounding, tracking, and reasoning about actions, events, and objects as they unfold over time. Covers temporal action detection/localization/segmentation in untrimmed videos; spatio-temporal action recognition; temporal and spatio-temporal video grounding (localizing language queries in space-time); video LLMs and multimodal models for temporal reasoning over long/hour-long videos; multi-object tracking and trajectory prediction; and dense video captioning / video QA with temporal structure. Backbone methods include 3D CNNs, spatio-temporal graph networks, temporal transformers, and recurrent/LSTM temporal models. Excludes video generation/synthesis (text-to-video, diffusion), static single-image understanding, and text-only temporal reasoning. Sources are predominantly conference paper walkthroughs (CVPR/ECCV/WACV/ICCV) and workshop/lecture talks.

**Filter guidance for the policy** (video-heavy → `channel_authority` + `speaker_expertise` signals):
- Prioritize: named-researcher and conference-channel talks; recent (2022–2026) video-LLM temporal-reasoning work alongside foundational TAD/action-recognition methods.
- Down-weight/exclude: SEO/tutorial-mill uploads, student "final project" walkthroughs, service-ad videos (the sample includes a Matlab gig ad with a phone number).
- Caveat: `channel`/`author` frontmatter is empty on these sources → authority scoring leans on title/transcript signals, not channel allowlists.

1. `wiki bootstrap-domain "<canonical description above>" ai-temporal-video` — creates policy + notebook, with channel-authority auto-emit (video-heavy domain) from `feat/bootstrap-channel-authority`.
2. Tag the 86 raw sources to `ai-temporal-video` (`domains:` frontmatter) and `wiki nlm-sync ai-temporal-video --limit N` to load them into the new notebook, then `wiki query` to synthesize.
3. **Fresh-discovery gate:** any `wiki research --execute` to expand the corpus beyond the existing 86 is serialized after the semantic-models loop (shared YouTube-adapter key).

### WS-3 — Orphan sessions + ungated harvests (triage; lowest priority)

- ~37 YouTube in abandoned sessions (bare notebook ids) + 16 with no source_map (orita-style direct harvests).
- Triage: for each orphan session, decide promote-to-a-domain (then sync + synthesize) vs discard. The 16 ungated harvests are likely discard (survey-tier, rejected by the gate by design).
- No YouTube API contention (all `raw/`-resident).

---

## 4. Execution order (recommended)

1. **WS-1** (now) — clean, mechanical, validates the end-to-end backfill→synthesis recipe on small domains.
2. **WS-2 glp1 sync** (now) — sync; defer synthesis pending value call.
3. **WS-2 ai-temporal-video** — resolve the bootstrap-or-fold decision, then sync (now). Fresh expansion gated behind the loop.
4. **WS-3** — triage after the above; low priority.

All of 1–3 (sync + synthesis) run without touching the YouTube adapter key. Only ai-temporal-video *expansion* (if chosen) waits on the concurrent session.

---

## 5. Open decisions

- **D1 — ai-temporal-video:** RESOLVED 2026-06-17 — stands up as its own bootstrapped domain (not folded). See WS-2.
- **D2 — glp1 revival:** is synthesizing the glp1 corpus in scope, or sync-only (park it)? YouTube there is low-value.
- **D3 — WS-3 orphan sessions:** which (if any) abandoned sessions are worth promoting vs discarding.
