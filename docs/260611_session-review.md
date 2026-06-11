# Session review — 2026-06-11 (data-collectives foundation + Stage 2 + contp skill)

Scope: 17 commits (`83501165..240cdf43`), 409 files, +26,817/−731. **No application
code (`.py`) was touched** — the work was research authoring, gateway-managed
`wiki/`+`raw/` content, docs, one skill (`contp`), and ~17 ephemeral shell scripts.
§1 therefore evaluates artifacts/scripts, not app code. Stage 2 (`e7e591a4`,
`240cdf43`) ran after the visible turns — treated as continuity evidence in §3.

---

## § 1 — Code & coding quality

**High — recovery shell script shipped with a real bug, caught only at runtime.**
The Stream-2 recovery script used `declare -A R=([arxiv-2206.07284]=…)`; bash parsed
the dotted key as arithmetic (`invalid arithmetic operator`), so the filter-correct
loop silently no-op'd and a useless re-ingest loop ran until killed (`pkill`). Root
cause: backgrounded a multi-step script with no dry-validation. Fix: for batch
gateway ops, test on one item (or `echo` the loop expansion) before backgrounding —
the project's own CLAUDE.md "Validate Incrementally" rule applies. Severity high
because it burned a full background cycle and required manual kill/redo.

**Medium — `git add -u wiki/` swept the pre-existing condo backlog into a commit.**
Caught and fixed via `git reset --soft` + selective unstage, then encoded as a memory
rule (content-matched staging). Good recovery; the lesson is now durable. Residual:
the guard relied on a post-hoc grep rather than a pre-stage scope check.

**Medium — `wiki edit --section` body used `##` subheaders → duplicated sections.**
The synthesis page needed abandon + re-file + re-edit with `###`. Root cause:
discovered the `##`-delimited section model by breaking it. Now documented in the
Stage-2 plan and `contp`. Convention knowledge that should live in a wiki authoring
note, not be re-learned.

**Low — 8× near-identical ad-hoc ingest/recover scripts in `/tmp`.** Throwaway is
fine, but the shape recurred 8 times verbatim — copy-paste drift. A small committed
`tools/` helper (parameterized by URL list + domain) would have prevented the
assoc-array bug and the per-stream rewrites.

**Checked, clean:** `contp/SKILL.md` — frontmatter present, `description` is
triggers-only, body <500 words, explicit `Never`/non-goals, rationalization table.
The docs synthesis + stream notes are well-structured and citation-bearing.

---

## § 2 — Token efficiency

**High — the filter-correct two-pass ran on every stream (7×).** Pattern each
stream: ingest with `--with-plan` → filter rejects/reviews most in-domain sources →
`filter-correct --include` + **re-ingest** the same sources. That roughly doubled
ingest LLM cost across the whole foundation (~40+ avoidable re-ingest calls). The
filter systematically under-scored hand-vetted, deep-research-verified sources. A
one-time lowering of the domain's `threshold_include` (or a `--force-include` ingest
flag) would have eliminated ~7 recovery batches. I flagged this mid-session and chose
not to act ("don't introduce a variable") — defensible for safety, but the cost
compounded linearly and in hindsight the threshold tune was worth it.

**Medium — `find -newermt` failed silently → wasted a commit cycle.** It returned
empty (macOS quirk / clock), so the first Task-2 commit staged only 8 files; required
re-investigation (`git status --short`, content-match grep) and re-staging. ~3 excess
calls. A precondition `echo "$recent" | wc -l` before committing would have caught it.

**Medium — buggy script → kill → rewrite → rerun = one fully wasted background cycle.**
See §1-High. Verify-before-background would have saved it.

**Low — the spend-cap "probe" was a no-op.** Re-ingesting an already-ingested URL
without `--with-plan` dedup-returned instantly and tested nothing; I then correctly
re-probed. One wasted diagnostic call.

**Low — early background-task output re-reads.** A few `cat`/`grep` of `.output`
files before completion (the known polling anti-pattern); mostly avoided after the
first stream.

---

## § 3 — Prompt & context engineering

**High — one continuous session where fresh-session iterations were the right shape.**
The entire 10-task loop + synthesis + skillify ran in ONE context window. The
self-paced `/loop` was designed to bound per-iteration context via `session-state.md`,
but because each wakeup re-entered the **same** session, context accumulated instead
of resetting — every post-5-min wakeup paid a cold-cache reload of an ever-growing
window. I recommended `/compact`→`/clear` and the user agreed the work was fully
resumable, yet it continued in-session. Highest-impact change: run multi-stream loops
as genuinely fresh sessions (or `/clear` between streams), since all state is on disk.

**Medium — the first `wiki answer` prompt was mis-scoped.** The north-star question
at k=16 retrieved mostly policy-stream sections → "not answerable," forcing
abandon+refile+hand-author. Seeding failure: I knew `wiki answer` grounds on a narrow
retrieval but still threw the broadest possible question at it. Should have
hand-authored from the start or raised k drastically.

**Medium — auth/cap discovered mid-flight, not probed up front.** The `wiki answer`
401 (research key) and the workflow spend cap both surfaced as failures rather than
preconditions. A cheap viability probe before LLM-dependent synthesis ops would have
avoided the dead-end calls.

**Positive — deep-research prompts were strong.** Adversarially framed, recency-gated,
scoped US/Canada-primary with EU-reference — they produced verified, well-bounded
output on the first attempt every stream. This is the session's best prompt work.

**Positive — no surface-anchor leakage.** The foundation stayed rigorously
domain-neutral; condo terms appeared only in Stage 2. The guardrail held (verifiable
in the clean foundation/Stage-2 separation).

**Positive — continuity worked.** Stage 2 executed across a session boundary
(`e7e591a4`, `240cdf43`) off the session-state + continuation prompt — the empirical
basis that justified the `contp` skill.

---

## Priority (impact ÷ effort)

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | §3 Context | One ever-growing window for a 10-iteration loop; cold-cache reloads | Run multi-stream loops as fresh sessions / `/clear` between streams; rely on session-state to resume |
| 2 | §2 Token | 7× filter-correct re-ingest doubled ingest cost | Lower the domain's `threshold_include` once per curated research domain (or add a `--force-include`); stop re-ingesting |
| 3 | §1 Code | 8× copy-pasted /tmp scripts + the assoc-array bug | Commit one parameterized `tools/` batch-ingest+recover helper; test on one item before backgrounding |
| 4 | §3 Prompt | Auth/cap found via failure, not precondition | Probe research-key + cap viability before any `wiki answer`/`query`/workflow synthesis |
| 5 | §2 Token | Silent `find -newermt` empty → wasted commit | Assert non-empty file set before committing batch-staged work |

**One-line POV:** the research *content* and prompt craft were the strong parts;
the waste was almost entirely *mechanical* — a strict filter fought every stream, and
a 10-iteration loop was run in one swelling context instead of fresh ones. Both are
cheap one-time fixes, and #1 and #2 alone would have cut this session's token cost
materially.
