# Session state — 2026-06-10

Last updated: 2026-06-15 (daily-review skill built + deployed via skillify — all pushed)

---

## ✅ DAILY-REVIEW SKILL (2026-06-15) — built via skillify, deployed, pushed

Cross-session arc: turned the ad-hoc "daily review" request into a reusable skill.
Lives in `~/code/claude-config` (not knowledge), but tracked here as session work.

**Sequence:** re-authored the user's loose prompt to Anthropic best practices →
ran the full skillify cycle (qualify → RED → write → GREEN → deploy).
- **Skill:** `~/code/claude-config/skills/daily-review/SKILL.md` (commit `3a0226c`,
  `origin/master`). Six-section cross-project work journal (where/why/accomplished/
  lessons/priorities/next); defers code/token/prompt analysis to `session-review`.
- **RED→GREEN proof:** GREEN out-performed a hand-written review — the cross-project
  rule caught 2 repos (Condo, local-inference) a single-repo glance missed. Live
  invocation later caught a 4th (claude-config itself) + the doc's own commit.
- **Deploy:** symlinked into `~/.claude/skills/daily-review` (user-global → invocable
  from any repo). README skills table updated.
- **Bootstrap:** `install.sh` (commit `cff22bb`) — idempotent one-step relink of ALL
  skills into `~/.claude/skills/` (links new, repoints stale, never clobbers a real
  dir; `--dry-run`). Closes the machine-local-symlink gap; README points at it.
- **Today's doc:** `docs/260615_daily-review.md` (commits `f468f17f`, `920bfae7`) —
  the live deliverable, cross-project across knowledge/Condo/local-inference/claude-config.

**Lesson logged in the doc:** run the daily review LAST — it goes stale by its own tail
(the skill commit + doc commit landed after the first draft).

**Open / deferred:** none. Multi-machine relink is solved (`install.sh`); no per-machine
script beyond it is needed (YAGNI until a new machine).

---

## ✅ FIRECRAWL SECRETS REACH BACKGROUND DAEMONS (2026-06-15) — shipped, tested

**Problem:** launchd agents (`com.knowledge.watcher`, running; `com.knowledge.scheduler`,
script only — not installed) start from a minimal environment (plist gave only
`KNOWLEDGE_ROOT` + `PATH`). So `FIRECRAWL_API_KEY` / `WIKI_WEB_SCRAPER` — exported in
the interactive shell — were invisible to background ingest. Every watcher-ingested
URL silently degraded to trafilatura-only and 403'd on biorXiv/PNAS with no error
(the converter swallows Firecrawl misses by design). Same latent gap in the scheduler.

**Fix (Option B — env-file loader, chosen over baking into the plist):**
- `src/gateway/secrets_env.py` — `load_secrets_env(path=None)`: reads
  `.knowledge/secrets.env`, applies each `KEY=value` with `os.environ.setdefault`
  (real env wins), strips `export `/quotes, skips comments/blank/malformed, no-op on
  missing file. Returns the applied mapping.
- `src/gateway/cli.py` — `main()` calls `secrets_env.load_secrets_env()` first thing,
  so BOTH daemons (both dispatch through `main`) and interactive ingest see the secrets.
- `.knowledge/secrets.env` (gitignored) — `FIRECRAWL_API_KEY` + `WIKI_WEB_SCRAPER=fallback`.
- `.gitignore` — `.knowledge/secrets.env`.
- `tests/gateway/conftest.py` — suite-wide autouse `os.environ` snapshot/restore
  (root-cause fix: `main()` loading a real on-disk file is a global side effect; the
  suite had no env isolation, so any `main()`-calling test leaked the vars).
- Watcher reloaded (PID 1744 → 57803), now on the loader code.

**Eval (TDD, all GREEN):** 9 loader unit tests + `main()` integration test; baseline
repro (trafilatura 403); post-fix live eval — daemon-minimal env → loader → `fallback`
escalates 403 → Firecrawl, 22,966 words; `env -i` launchd-minimal entrypoint proof;
full gateway suite **1942 passed, 0 failed**.

**Benefit of Option B:** plists stay clean → key rotation is a one-line file edit, no
reinstall; the not-yet-installed scheduler inherits the fix for free on install.

**Shipped + follow-ups (all on `origin/main`):**
- PR #16 merged → `a71d59bb`. NOTE: the PR branch was cut from a local `main` that
  was 6 commits ahead of origin, so the squash also swept the unpushed orita-cmo arc
  (55 files) under the firecrawl commit message. No content lost (origin is a superset);
  local main soft-reset to origin to reconcile. LESSON: in this repo cut branches from
  `origin/main`, not local `main` (local routinely runs ahead).
- Follow-up fix `4cf76a13` (session-review #4): empty-value guard in the loader — a
  `KEY=` / `KEY=""` line no longer writes `""` (an empty FIRECRAWL_API_KEY would win
  over no-key via set-if-absent and suppress the trafilatura fallback). +2 tests.
- DECISION (#3): loader stays in `main()` = **global** (all CLI invocations, not just
  daemons). Parity (URL works in watcher AND by hand) > blast radius; firecrawl only
  fires after trafilatura already 403'd, so no happy-path spend. REVISIT TRIGGER: when
  a non-firecrawl secret is added to `secrets.env`, scope that key rather than narrow
  the loader.

**Open / deferred:** none. The scheduler is still script-only (not loaded in launchctl);
when installed it works without an installer change. Phase-1 firecrawl-scrape plan
(`docs/plans/2026-06-15-firecrawl-scrape-phase1.md`) is the broader arc this unblocks.

---

## ✅ ORITA-CMO DOMAIN MOC + ORITA.MD FINALIZE (2026-06-15) — pushed

Rode alongside the firecrawl work in the same session.
- **MOC** `wiki/mocs/orita-cmo.md` (commit `8f94e49a`): canonical single-read domain hub
  authored via `wiki moc-add` (gateway path; `citation_grounded=False`). Overview frames
  Orita's **upstream-only** audience-intelligence position and the **own-execution-vs-
  Klaviyo-partnership fork**; grouped+glossed entity/concept/synthesis links (0 broken),
  source clusters, open threads. Built from committed wiki content via an Explore subagent
  (operating-model arc + 20-concept toolkit) + direct spine reads. Interim narrative doc
  `docs/research/orita-cmo/domain-synthesis.md` was written then **deleted** (MOC supersedes).
- **Finalize** `wiki/entities/orita.md` (commit `feb19e46`): draft → finalized; passed the
  citation-grounding gate; `finalized_at` set. Closes the one stale-draft item the MOC flagged.
- Session review filed: `docs/260615_session-review-firecrawl-moc.md`.

---

## ✅ ORITA-CMO COMPETITIVE INTELLIGENCE (2026-06-15) — built, finalized, synthesized

Arc began from "draft a synthesis for orita-cmo" → the competitive-positioning
synthesis was impossible (empty competitor corpus; the grounded model correctly
refused). Built the corpus end-to-end, then synthesized.

**What was delivered (all committed to `main`):**
- **Discovery** (`docs/research/orita-cmo/competitive-set.md`): harvested 237
  youtube+web results via direct adapters (outside the analyst-grade ingest gate,
  which rejected 159/160 survey-tier candidates); enumerated ~50 competitors
  across Orita's 5 channels (email/ESP, deliverability/bot, SMS, programmatic
  direct mail, ad-audience, CDP/agentic). Commit 3ef47911.
- **Phase 1 direct tier**: ingested 5 direct competitors + adjacents — entities
  `black-crow-ai, monocle (+ OuterSignal M&A), clustie (+ full-venue), enalito,
  aampe (+ offerfit, movable-ink, hightouch)` + concepts
  `agentic-personalization-platform, martech-consolidation`. Commit 72e38682.
- **Blocked-aggregator access solved**: firecrawl→Capterra→`wiki ingest
  --force-include` pipeline (CB Insights account-gated; F6S hCaptcha — both
  unreachable). Built canonical sources via gateway id/hash helpers. Commits
  f7a5b517 (Black Crow) + b5e01bac (9 incumbents: klaviyo, attentive, postscript,
  drip, bloomreach, omnisend, yotpo, simon-ai, listrak — real ratings/features/
  pricing/integration catalogs).
- **Finalize**: all 25 competitor/adjacent pages citation-cleaned + finalized
  (Related-section annotations → bare links; Clustie pricing cited). Commit
  (chore finalize).
- **Synthesis** (`wiki/synthesis/2026-06-16-map-the-competitive-landscape-orita-operates.md`):
  complete 14-competitor landscape map + "Where Orita Sits" conclusion. Reframed
  prescriptive→descriptive (corpus grounds facts, not strategy). Regenerated at
  4000-token budget after the first version truncated at the 1500 cap. Commit
  71283c43.

**Domain state now:** orita-cmo has 2 synthesis pages (operating-model 2026-06-15
+ competitive-landscape 2026-06-16), ~25 finalized competitor entities (much
benchmark-grounded), `competitive-set.md` discovery inventory.

**Open / deferred (explicit-trigger only):**
- **Prescriptive positioning** doc (how Orita *should* position) needs Orita's own
  strategy material in the corpus — not a retrieval task; deferred until requested.
- **Blocked sources**: CB Insights "Orita alternatives" (needs paid account) +
  F6S (hCaptcha) — the richest curated competitor lists, still unreachable.
- **`answer.py` 1500-token cap** is a latent limit for wide syntheses — worked
  around via in-process override; a `--max-tokens` CLI flag would productize it.

---

## ✅ STAGE 2 COMPLETE (2026-06-11) — data-collectives project DONE

Foundation loop COMPLETE (Tasks 1–10, committed c3eaee04..3989c841). **Stage 2 —
condo application leg — now COMPLETE.** Deliverable filed:
`docs/research/data-collectives/stage2-condo-collective.md` — feasibility + design
position for a reserve-study data collective among engineering firms / PMs / HOAs.
Pure synthesis over the two grounded domains (data-collectives foundation +
condo-capital-infra); no re-research; spend cap respected.

**Verdict: Qualified GO** as governance-and-network infrastructure pooling the
non-rivalrous component-condition signal, Canada-first, reserve-study value (not
agentic demand) carrying the P&L. Key insight: condo is the STRONGEST application
of the foundation because the engine is *data-bound* — pooled cross-firm failure
observations are the binding input to its accuracy ceiling, making contribution
rational on narrow self-interest. 3 load-bearing assumptions, full risk set
(cold-start/SME, downstream-model liability resolved via "engine informs, PEng
firm certifies/owns stamp", substitutes trap, agentic bet), and exit cross-ref to
condo's ADR-0004 acquirer thesis (CINC/Associa; the co-op caps what an acquirer can
capture → sell the administrator/workflow layer, not the data).

Stage 2 wiki-grounding (Task 3) DONE 2026-06-11 (user requested). Grounded synthesis
page FILED + finalized: wiki/synthesis/2026-06-11-is-a-data-collective-among-condo.md
(via wiki answer --file scaffold → wiki edit grounded body → wiki finalize, mirroring
the foundation page recipe). 19 sources cited across BOTH domains (condo engine
docx-818ed0a0ce55/bf4965d0d33a + NS studies + acquirer/PropTech sources; foundation
fraud-utility/substitutes/legal/Catena-X/data-moat sources). finalize passed the
citation-grounding gate. ANTHROPIC_API_KEY_RESEARCH valid; one small answer call.

---

## Open contracts

**data-collectives research foundation — IN PROGRESS (self-paced loop).**
Spec: `docs/superpowers/specs/2026-06-10-data-collectives-research-foundation-design.md`.
Plan: `docs/superpowers/plans/2026-06-10-data-collectives-research-foundation.md`.

New citation-grounded wiki domain `data-collectives`, forked from `condo-capital-infra`.
Policy/market-structure spine; Approach C (agentic dimensional fan-out). Executed as a
self-paced loop, one plan Task per iteration: deep-research → `wiki ingest --with-plan`
the verified sources → author concept/synthesis pages → verify grounding → commit →
checkpoint here → schedule next.

**Task ledger (loop tracks progress here):**
- [x] Task 1 — bootstrap `data-collectives` domain (policy.yaml created, verified)
- [x] Task 2 — Stream 0 precedent census (seed) — 7 source pages + 8 concept pages + entities grounded; analytical note at docs/research/data-collectives/stream-0-precedent-census.md
- [x] Task 3 — Stream 1 economic/incentive — grounded: nonrivalry-of-data, data-shapley, competitor-data-sharing-tradeoff, product-differentiation-collaboration (+ Jones&Tonetti, Tsoy&Konstantinov, Data Shapley sources). Vives 1984 + Farboodi-Veldkamp verified but full-text won't convert (noted in stream-1 note). KEY: substitutes in same market have weak/negative pooling incentive (Vives Cournot PD).
- [x] Task 4 — Stream 2 technical/architecture — GROUNDED. 6 source pages live (FL gradient-inversion, subject MIA, DP-FL, DP survey, Azure Confidential Clean Rooms, NIST US-UK PETs Prize) via filter-correct + re-ingest. ACM-Queue + OPAL chapter still need alt URLs (cited by reference in note). KEY: agentic-layer gap (zero verified precedent — see note).
- [x] Task 5 — Stream 3 legal — GROUNDED. 6 sources: US DOJ safety-zone withdrawal (Arnold&Porter), Canada Competitor Collaboration Guidelines + draft ACCA, PIPEDA/C-27 de-id, property-in-data (Hastings), data-trust entity forms (Ada Lovelace). KEY: Feb-2023 DOJ withdrawal removed US bright-line safe harbors → case-by-case only; Canada two-track clearer (legal-certainty edge for Canada-first). No property in data → rights are contractual.
- [x] Task 6 — Stream 4 regulatory — GROUNDED. 7 sources (Canada Consumer-Driven Banking + PIPEDA data-mobility right, US info-blocking/TEFCA, ISED Voluntary GenAI Code, AIDA-death, Ag Data Transparent, EU Data Act ref). KEY: NO regulation compels/funds cross-competitor pooling — only consumer/holder-directed PORTABILITY exists. AIDA dead; Canada has no binding AI statute; US deregulatory. 'Why Canada' must rest on the economy-wide data-mobility right + strategy/funding, NOT regulatory compulsion.
- [x] Task 7 — Stream 5 governmental/policy (SPINE) — GROUNDED. 7 sources (Sovereign Compute Strategy, Pan-Canadian Phase 2, C.D. Howe missing-pillar, FNIGC/OCAP, Scale AI, NAIRR US-contrast, IAPP data-mobility). VERDICT: Canada funds talent/commercialization/COMPUTE, NOT data infrastructure — no funded mechanism for a data collective. 'Why Canada' rests on (a) CAN/DGSI 100-7 governance standard, (b) economy-wide data-mobility right, (c) data-sovereignty framing — NOT funding/mandate. Compute strategy is a distraction for a data play. Validates user's rhetoric-vs-mechanism skepticism.
- [x] Task 8 — Stream 6 academic — GROUNDED. 6 sources (GKC/Constructing-Commons, Ostrom 8 principles, data-as-labor AEA, Vincent 2025 collective bargaining, Jonker + Duncan critiques). VERDICT: strong theory, near-absent empirics, every org form has a distinct fragility; collectives solving collective-action was REFUTED in verification. Enabling regulation may be a precondition (Jonker). Convergent with S0 failures + S1 substitutes.
- [x] Task 9 — Stream 7 industrial — GROUNDED. 6 sources (Early Warning Services + Cifas = genuine fraud-utility pooling; LexisNexis = aggregation contrast; a16z data-moat debate; Datavault aspirational; Catena-X SME stall ref). KEY: real cross-competitor pooling concentrates in FRAUD/AML utilities (pool the non-rivalrous signal). Agentic zero-precedent now CONFIRMED across 3 streams (0,2,7). Stream 7 verification partly truncated by Anthropic spend cap.
- [x] Task 10 — synthesis COMPLETE (analysis). docs/research/synthesis-policy-market.md answers the north-star + full confidence/uncertainty ledger. DEFERRED (external cap, not blocking): the citation-grounded wiki synthesis PAGE via wiki query — file on Anthropic spend-cap reset. wiki answer stays 401-blocked. Agentic targeted pass cancelled (zero-precedent confirmed 3x).
- [x] Task 11 / Stage 2 (condo application leg) — COMPLETE 2026-06-11. Deliverable: docs/research/data-collectives/stage2-condo-collective.md. Qualified GO. See top block.

**Guardrails (every Task):** foundation pages domain-neutral (no reserve-study /
condo / Longspan terms — that is Stage 2); citations mandatory (`[[sources/<id>]]`,
`--draft` then `wiki finalize`); adversarial verification before filing load-bearing
claims; date precedents, flag pre-2023 for AI-model claims; `wiki retrieve`/`context`
only, never dump index.md/log.md.

**Per-stream recipe (learned in Task 2 — REUSE):**
1. deep-research workflow → verified findings + source URLs.
2. `wiki ingest "<url>" --with-plan --draft --domain data-collectives` per source
   (authorship path = Max-OAuth `claude -p`, WORKS).
3. For obviously-in-domain sources the strict filter put in review/rejected:
   `wiki filter-correct <id> --include --rationale "…" --domain data-collectives`
   then RE-INGEST `--with-plan` (correction alone does not author the source page).
4. Grounded concept/entity/source pages = the canonical stream deliverable.
5. Preserve the analytical findings + adversarial caveats + open questions in
   `docs/research/data-collectives/stream-N-*.md` (project doc, NOT wiki — avoids
   direct-write violation; feeds Task 10 + condo Stage 2).
6. Verify with `wiki retrieve`; commit. STAGING DISCIPLINE: never `git add -u wiki/`
   or `git add wiki/` — the working tree has a pre-existing condo backlog of
   modified/untracked pages (leave alone). Stage ONLY this stream's files by content
   match: `git ls-files --others --exclude-standard wiki/ raw/ | grep -lE data-collectives`
   plus the specific source IDs; add docs/research note + session-state + index.md +
   log.md + .knowledge/policies/data-collectives explicitly.

**AUTH CONSTRAINT (blocks `wiki answer` / SDK path):** `ANTHROPIC_API_KEY_RESEARCH`
returns 401 (invalid). So `wiki answer` and any SDK-cached call FAIL. Do NOT use
`wiki answer` per stream. The Max-OAuth `claude -p` path (filter / plan / --with-plan
authorship) WORKS. Final synthesis (Task 10) goes through `wiki query` (NotebookLM,
separate browser auth) once the corpus is rich — corpus-quality gate first.
Known authorship friction: the LLM sometimes picks entity_kind values outside the
controlled enum (consortium/proposal/project) → that entity page fails but the
source + other pages still commit. Not blocking.

---

## RESOLVED

**RAG retrieval build — DONE and MERGED to main (2026-06-09).** All 6 workstreams
landed; 2002 tests pass; recall@5 0.889 / recall@10 0.926 / MRR 0.722. Deferred WS7
hybrid vector retrieval (trigger: golden recall@10 < ~0.8 or ~10k pages — unmet).
`main` was 9 ahead of `origin/main` at that checkpoint; push remains the user's call.

Carry-forward (pre-existing, untouched): schema-drift ~208; finalize-batch ~460;
orphans (condo-capital-infra, glp1-reward-modulation, ai-native-business); edge-ai
notebook quota; `wiki migrate` stub; orita-cmo R3/R2; iOS Shortcut; web-API hardening.

---

## Files mid-edit

None. Working tree carries pre-existing untracked gateway-managed `nlm/`/`raw/`/`wiki/`
content (gateway-owned — leave alone).

---

## Next atomic step

**data-collectives project COMPLETE (foundation + Stage 2).** No open work.

**Cross-domain synthesis gap — RESOLVED 2026-06-11 (PR #15, merged to main at
089dac39).** `wiki retrieve`/`wiki answer` now take `--domains a,b`: per-domain
quota merge (ceil(k/N) each, round-robin-interleaved, dedup by path) so balance
survives budget truncation; `answer` files list-valued `domains:` frontmatter
(fixes the old single-valued `answer.py:222`). Mirrored on the `wiki_retrieve`/
`wiki_answer` MCP tools. Golden set unchanged (recall@5 0.889 / recall@10 0.926 /
MRR 0.722 — single/global paths untouched); 1924 gateway tests pass; live smoke
test cited both domains. Spec/plan: `docs/superpowers/{specs,plans}/2026-06-11-
multi-domain-balanced-retrieval*.md`.

Remaining items are explicit-user-trigger only:
1. **Wiki-grounding backfill (both stages), cap-gated.** On Anthropic spend-cap
   reset or explicit request: file/finalize citation-grounded wiki synthesis pages
   for the foundation (from synthesis-policy-market.md) and Stage 2 (from
   stage2-condo-collective.md) via `wiki answer --file` (key now valid) or
   `wiki query` (corpus-quality gate first).
2. Optional source backfill: ACM-Queue + OPAL alt URLs (Stream 2); Truveta/Datavant
   health-pooling cases (Stream 7, truncated by cap).

**Carry-forward finding (still load-bearing):** privacy-preserving pooling substrate
is mature; the agentic layer on top is greenfield — no verified 2023–2026 precedent.
In Stage 2 this is the explicit unproven bet; the condo P&L closes on reserve-study
value without it.
