# Session review — 2026-06-17 (YouTube corpus-gap remediation: detection + staging)

**Scope:** detection → planning → decision-resolution → an aborted execution attempt blocked by shared-tree contention. The remediation's *execution* (WS-1/WS-2) has not run — it is parked behind the clean-window poller (`bmkrcwuck`). This review is therefore of the analysis/staging arc and the two process incidents, not of executed gateway work.

**Deliverables this session:** `docs/plans/2026-06-17-youtube-corpus-gap-remediation.md` (on `main`, `c2278e3f` + `1b431086`); memory `feedback_verify_branch_before_commit_shared_tree.md`. No source/test/feature changes.

---

## § 1 — Code and coding quality

No production code was written. Findings are on the analysis artifacts (probe scripts, pollers) and the plan doc.

- **[High] First detection method used the wrong primitive.** `wiki nlm-sync <domain> --dry-run` was treated as a corpus-gap detector. It is not: reading `src/gateway/ops/nlm.py:420` showed dry-run lists *every* raw source tagged to the domain (no `nlm_corpus_ids` check; reconciliation happens only in the live run), and the printer caps at 50 (`nlm.py:422-425`) with `youtube/` sorting last — so every >50-source domain reported a false `youtube=0`. Root cause: relied on a CLI's output semantics without reading the op first. Fix applied mid-session: replaced with a direct `nlm_corpus_ids`-vs-`source_maps` probe using the gateway's own `frontmatter` parser. **Lesson:** verify the semantics of a detector before drawing conclusions from it — same class as the "read the signature before calling" discipline.
- **[Medium] First poller's quiescence condition was unsafe.** `/tmp/wait_loop_idle.sh` defined "safe to proceed" as research-loop idle only. That is necessary but not sufficient: the concurrent session went research-idle, then switched the shared tree to a refactor branch — a state the idle poller would have greenlit. Caught before damage by a manual `git status` check, then fixed by the second poller (`wait_clean_window.sh`) which ANDs three conditions (branch==main, `notebooks.yaml` clean, loop idle). **Lesson:** a safety gate must check every resource the action touches (git branch + the specific file mutated), not just the most obvious one.
- **[Low] Frontmatter parsed with a hand-rolled regex before switching to the gateway parser.** The first attribution probe used `re.findall` on frontmatter and undercounted (missed list-valued `domains:` and the recent semantic/agentic sources). Switched to `from gateway import frontmatter as fm`. **Lesson:** use the project's own parser for project formats from the first probe — convention drift even in throwaway scripts costs re-runs.
- **[Low/positive] Plan doc quality is high and self-aware.** It flags its own approximate/overlapping counts ("~14", "~37") and defers exact enumeration to execution-time re-derivation, and records each decision with a one-line why. Matches the `docs/plans/` convention.

---

## § 2 — Token efficiency

- **[Marquee] The `nlm-sync --dry-run` detour cost ~4 avoidable calls + a 46.7KB truncated dump.** Sequence: 8-domain dry-run (huge truncated output) → 15-domain dry-run → read the op code → discover it's the wrong tool → rebuild with a Python probe. Reading `nlm.py`'s gap logic *first* (1 targeted read) would have skipped all three dry-run rounds. Estimated waste: 3–4 tool calls and one oversized context load.
- **[Medium] First `notebooks.yaml` read dumped 46.7KB into context** (`cat nlm/notebooks.yaml`) where the very next step parsed it with `yaml.safe_load` for a 1-line-per-domain summary. The targeted parse should have been first. Estimated waste: ~45KB context for a table I rebuilt programmatically anyway.
- **[Medium] Four Python probe iterations to converge on YouTube attribution.** Probe 1 (regex, undercounted) → import error → probe 2 (gateway parser) → probe 3 (corpus membership) → probe 4 (source_map attribution). Probes 1 and the import failure were avoidable: checking the `frontmatter` import path (`grep` in `nlm.py`, which I did only *after* the ImportError) and using `nlm_corpus_ids` from the start would have collapsed this to ~2 probes.
- **[Low] One retry from an unverified import** (`from gateway import fm` → ImportError → grep → re-run). A 1-line grep of the import path before running would have avoided a full failed script execution.
- **[Positive] The pollers were the right token move.** Backgrounding the wait (instead of spin-reading `wiki status` each turn) kept context off the cold-cache treadmill the project's own `feedback_multistream_loop_fresh_sessions` warns about.

---

## § 3 — Prompt and context engineering

- **[Medium] Inconsistent context-seeding — verified one external contract, assumed another.** Before claiming "no YouTube-key contention," I read `nlm.py:218` and confirmed `source_add_url` (correctly seeded). But the `nlm-sync --dry-run` semantics were *assumed*, not seeded, and three runs happened before the constraint surfaced. Same discipline, applied to one call and skipped on the other. The tell: when a conclusion rests on a tool's behavior, load that behavior first — uniformly.
- **[Medium] Shared-tree precondition not seeded before the first commit.** The session committed to `main` while a concurrent session had HEAD on `test/isolate-promote-fixtures`; the commits orphaned and were recovered via `git show <sha>:<path>`. A 1-line `git branch --show-current` guard before staging would have prevented it. Now encoded in memory and applied to every subsequent commit. This is the canonical "constraint discovered after the action" failure.
- **[Positive] Surface-anchor drift caught before it propagated.** The `ai-temporal-video` slug implied video *generation*; sampling the 86 sources showed temporal video *understanding* ("temporal" 215×, text-to-video ~1). Drafting the bootstrap description from the slug would have seeded a wrong-domain policy. This is exactly the anti-pattern guard #6 working as intended.
- **[Positive] `AskUserQuestion` reserved for genuine forks.** Scope (which buckets) and coordination (how to handle the live loop) were real user-owned decisions with no safe default; the questions surfaced the NotebookLM/git collision risk rather than papering over it. No questions were asked where a convention or the data already dictated the answer.
- **[Process] The review itself hit the shared-tree constraint.** This brief is written as a new untracked file (safe across checkouts); `session-state.md` refresh was deferred rather than written onto the refactor branch — the skill's "refresh if exists" instruction yields to the higher-priority safety rule the session just learned.

---

## § 4 — Session-state checkpoint (port into `docs/session-state.md` once back on `main`)

**In-flight / open contract:**
- **YouTube corpus-gap remediation — STAGED, execution NOT started.** Plan: `docs/plans/2026-06-17-youtube-corpus-gap-remediation.md` (on `main`, `c2278e3f`/`1b431086`). All decisions resolved; awaiting a clean execution window.
- **Background process running:** poller `bmkrcwuck` (`/tmp/wait_clean_window.sh`) — fires when branch==`main` AND `nlm/notebooks.yaml` clean AND research loop idle ~12 min, or times out at ~3h. On fire → execute.
- **This review brief** `docs/260617_session-review-4.md` is UNTRACKED — commit it on `main` (do not commit on the current refactor branch).

**Decisions made:**
- D1 — `ai-temporal-video` stands up as its own bootstrapped domain (not folded); it is temporal video *understanding*, not generation.
- D2 — glp1 YouTube (48) discarded: consumer/influencer content vs a 77-PubMed biomedical corpus; would degrade synthesis. glp1 PubMed-corpus revival is a separate, out-of-scope backlog item.
- D3 — "orphan sessions" are abandoned runs of existing domains: convergent-ai-brain research talks (17) fold into WS-1; condo HOA explainers + 16 ungated harvests are skip/discard.
- Unifying screen: sync researcher/conference talks; never sync consumer/influencer explainers.

**Rejected approaches:**
- Executing concurrently with the live loop — shared NotebookLM browser session + shared git tree (auto-committing) = collision/corruption risk.
- `wiki nlm-sync --dry-run` as a corpus-gap detector — lists all tagged sources, 50-cap, youtube sorts last → false zeros.
- Committing on the shared tree without a branch guard — orphaned two commits onto another session's branch.
- A git worktree to isolate execution — `notebooks.yaml` registry + NotebookLM account are shared singletons; a second checkout diverges them.

**Current system state (verified):**
- Detection complete and authoritative: 340 raw YouTube → 103 in ≥1 corpus, 237 not. Gap buckets: ai-temporal-video 86 (no domain), glp1 48 (empty stub), convergent-ai-brain ~17 talks (untagged), ai-native-business ~4, risksystems 2, orphan/ungated remainder.
- Plan committed to `main`. NotebookLM untouched this session. No `wiki` mutation run.
- Working tree currently on `refactor/promote-public-title-resolver` (concurrent session), 478 dirty files (434 untracked, 44 modified) — NOT this work; do not `git add -A`/`-u`, do not switch branches.

**Next atomic step:**
- When `bmkrcwuck` reports `CLEAN_WINDOW`: execute **WS-1 convergent-ai-brain** first — `wiki nlm-add convergent-ai-brain <id>` for the 17 vetted talk IDs: `yt--Hau9_8r2Ew yt-0W-cRw-EBAc yt-1_xH2mUFpZw yt-46vht4LAqGk yt-4KpXlmoQtxs yt-4SaY4uQEewU yt-4j78w__YudU yt-CI26o8nkh-M yt-NvbkfNxLVAA yt-_CxOYR8hLVM yt-em8lPQVtfFM yt-fYoW8TxUAco yt-ilAwtIwCLRg yt-psCQ65zjqPc yt-rTQ5B0wF6H0 yt-tyYIuvbV2po yt-ysv2g9M3ong` → re-synthesize "What sets the ceiling on representational alignment between biological brains and artificial neural networks?" via `wiki query --domain convergent-ai-brain --draft` → `wiki cite` + `wiki finalize`. Then ai-native-business + risksystems backfill, then WS-2 ai-temporal-video (`wiki bootstrap-domain` with the canonical description in the plan → sync 86 → synthesize). Branch-guard (`==main`) + explicit-path staging on every commit.

---

## Priority table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | §3 / §1 | Committed on a shared tree without checking the branch → orphaned commits | Branch guard before every commit (done); memory written. Keep applying. |
| 2 | §1 / §2 | `nlm-sync --dry-run` mistaken for a gap detector; 3 runs + a 46.7KB dump wasted | Read an op's logic before relying on its output; the `nlm_corpus_ids` probe is the correct detector — reuse it for post-execution verification. |
| 3 | §1 | First poller greenlit an unsafe window (idle ≠ exclusive) | Safety gates must AND every touched resource (branch + mutated file + idle), as `wait_clean_window.sh` now does. |
| 4 | §2 | Over-wide first reads (`cat notebooks.yaml`, 8→15 dry-runs) before the targeted parse | Lead with the targeted parse/grep; reserve full dumps for when structure is unknown. |
| 5 | §3 | Inconsistent context-seeding (verified `source_add_url`, assumed dry-run) | When a claim rests on tool behavior, read that behavior first — every time, not selectively. |
