# Session state — 2026-05-28

Last updated: 2026-05-28 (gateway stream complete; 371 discharge-orphans drafts; discharge parallelised)

---

## Open contracts

None.

Carry-forward (gateway build):
- **schema-drift**: ~208 remaining (legacy editorial tail — entity_kind, slug, canonical_name — human judgment).
- **finalize-batch escalated**: ~460 researcher entity pages with no auto-appliable citations. Source ingestion required before cite-suggest can fill these. Engineering is unblocked.
- **orphans**: substantially reduced this session (371 drafts filed). All three active notebooks quota-exhausted (~24h cooldown). Resume tomorrow: condo-capital-infra, glp1-reward-modulation, ai-native-business.
- **edge-ai notebook quota**: ~15 specific YouTube sources (`yt-rugGoieVQ2Y`, `yt-tVvKlx-oVqc`, `yt-0Wwn5IEqFcg`, etc.) return persistent `RESOURCE_EXHAUSTED` (error code 8) on every round — not transient quota, likely a per-source NLM restriction. These block further progress on edge-ai until diagnosed. Workaround: filter them from `_orphan_sources_for_domain` or ingest via a different path.
- `wiki migrate` stub remains.

Carry-forward (orita-cmo — unchanged from prior session):
- **R3** (`2026-05-28-orita-gcp-r3`): query plan ready. Retry when YouTube quota resets: `.venv/bin/wiki research --execute 2026-05-28-orita-gcp-r3`
- **R2** (ICP validation): blocked on user exporting HubSpot closed-won/closed-lost CSVs (12-month window).
- **nlm login bug**: Chrome must be quit (Cmd-Q) before `nlm login`. Verify with `nlm login --check`.

Carry-forward (iOS Shortcut — K3/M48 — unchanged from prior session):
- **Tailscale**: connected on Mac (`andrew-grants-m2-max.tail477197.ts.net`, IP `100.109.141.64`) and iPhone.
- **wiki serve**: running on `0.0.0.0:7474`. Must be restarted with `wiki serve --bind 0.0.0.0` after reboots.
- **Bearer token**: `ios-shortcut-andrew-iphone` minted. Stored in `.knowledge/auth.yaml`.
- **Next step**: Safari → Share → Wiki Capture → confirm task_id notification → export to `scripts/wiki-capture.shortcut` → commit.

---

## Files mid-edit

None.

---

## Decisions made this session

- **ANTHROPIC_API_KEY_RESEARCH rotated**: old key invalid. New key set in `~/.zshrc` (lines 23-24, clean). Bash tool inherits old key from process env — must pass explicitly: `ANTHROPIC_API_KEY_RESEARCH='...' .venv/bin/wiki evaluate --all-domains`.
- **`wiki evaluate --all-domains` restored**: 4/4 domains scored cleanly (ai-native=0.942, edge-ai=0.697, condo=0.632, glp1=0.538).
- **`finalize-batch --suggest --execute` ran**: 0 finalized. Three failure categories: (1) ~460 researcher entities with no ingested backing source — human-editorial tail; (2) `entity_kind` vocab gaps (regulation/artifact) — fixed this session; (3) WikiLoom-derived pages — fixed this session by regenerating missing wiki/sources/web-2026-04-11-879.md.
- **`entity_kind` vocab expanded**: added `regulation` and `artifact` to `ENTITY_KIND_ENUM`. `regulation` subject to `last_verified_at` staleness rule (alongside `statute`). `regulation` alias removed from backfill map. 1871 tests pass.
- **WikiLoom source page regenerated**: `wiki/sources/web-2026-04-11-879.md` was missing; re-ran `wiki ingest raw/web/web-2026-04-11-879.md --with-plan`. 12 WikiLoom-derived pages now citation-clean.
- **discharge-orphans parallelised**: `ThreadPoolExecutor(max_workers=4)` in `discharge_orphans.py`. Each `query()` call creates its own `NlmCLIClient` (independent subprocess) so threads share no state. Dry-run returns early with "would be filed" message. 1871 tests pass.
- **Parallel dispatch side-effect**: running condo + glp1 + edge-ai simultaneously caused all three notebooks to hit `RESOURCE_EXHAUSTED` at round 3. Future runs should stagger domains or cap to 1-2 parallel notebooks.
- **nlm/notebooks.yaml merge conflict resolved**: `<<<<<<< HEAD` conflict at line 248 (orita-cmo sessions block) was present during the failed batch runs; resolved by the auto-merge commit `37f186b`.
- **Half-mutated risksystems synthesis pages restored**: `git checkout wiki/synthesis/2026-05-20-risksystems-02-physics-informed-sciml-hybrid-modeling...md wiki/synthesis/2026-05-20-risksystems-05-bounded-gamma-deterioration-kernel...md`.

---

## Commits this session

- `68c8649` feat(ont4): add regulation and artifact to entity_kind vocabulary
- `7e3ac9a` feat(wikiloom): generate missing source page + cite WikiLoom-derived pages
- `c1badb3` perf(discharge-orphans): parallelise NLM queries with ThreadPoolExecutor
- ~30+ `chore(discharge-orphans)` auto-commits: 371 synthesis drafts across 4 domains

---

## Next atomic step

1. **Resume discharge-orphans** (tomorrow, after notebook quota resets ~24h):
   - `wiki routine discharge-orphans --domain condo-capital-infra --limit 20`
   - `wiki routine discharge-orphans --domain glp1-reward-modulation --limit 20`
   - `wiki routine discharge-orphans --domain ai-native-business --limit 20`
   - **Do NOT run edge-ai** until the persistent RESOURCE_EXHAUSTED sources are diagnosed/filtered.
2. **R3 retry**: `.venv/bin/wiki research --execute 2026-05-28-orita-gcp-r3`
3. **iOS Shortcut completion**: Safari → Share → Wiki Capture.
