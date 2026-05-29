# Session state — 2026-05-29

Last updated: 2026-05-29 (iOS Shortcut partially built; gateway fixes merged; orphan discharge runs)

---

## Open contracts

None.

Carry-forward (gateway build, unchanged):
- **ANTHROPIC_API_KEY_RESEARCH**: must be set in shell for edge-ai-agentic and glp1-reward-modulation eval runs. See RUNBOOK.md § Evaluation failures.
- **finalize-batch escalated**: 379 escalated drafts (uncited claims). `--suggest` unblocked once API key is set.
- **schema-drift**: ~191 remaining (legacy editorial tail — entity_kind, slug, canonical_name — human judgment).
- **orphans**: reduced this session via automated discharge runs (glp1, condo-capital-infra). Run `wiki lint --scope orphans` for current count.
- `wiki migrate` stub remains.

Carry-forward (orita-cmo):
- **R3** (`2026-05-28-orita-gcp-r3`): query plan ready. YouTube quota exhausted today (403); Firecrawl was up on last attempt but no candidates survived materialization. Retry tomorrow when YouTube quota resets: `.venv/bin/wiki research --execute 2026-05-28-orita-gcp-r3`
- **R2** (ICP validation): blocked on user exporting HubSpot closed-won/closed-lost CSVs (12-month window).
- **nlm login bug**: Chrome must be quit (Cmd-Q) before `nlm login`. Verify with `nlm login --check`.

Carry-forward (iOS Shortcut — K3/M48):
- **Tailscale**: connected on Mac (`andrew-grants-m2-max.tail477197.ts.net`, IP `100.109.141.64`) and iPhone. MagicDNS hostname doesn't resolve on iPhone — use IP directly.
- **wiki serve**: running on `0.0.0.0:7474`. Must be restarted with `wiki serve --bind 0.0.0.0` after reboots (not yet launchd-managed).
- **Bearer token**: `ios-shortcut-andrew-iphone` minted. Token stored in `.knowledge/auth.yaml`. Plaintext was shown once this session — must be retrieved from wherever Andrew saved it.
- **Shortcut build**: mostly complete. Issue: Shortcut Input is nil when running from inside the Shortcuts app (no Share Sheet context), causing "invalid HTTP request". Fix: test exclusively via Safari Share → Wiki Capture, not from the Shortcuts app directly. Hardcoded URL test (`https://example.com`) as the url field value is the next diagnostic step if Share Sheet trigger still fails.
- **Next step**: open Safari → any page → Share → Wiki Capture. If notification fires with task_id, export shortcut to `scripts/wiki-capture.shortcut` and commit.

---

## Files mid-edit

None.

---

## Decisions made this session

- **PR #11 merged**: `fix(research)` — bounded synthesis slugs to 80-char limit + YouTube adapter 1.5s inter-query throttle. Both fixes on main.
- **Tailscale setup complete** on Mac and iPhone. wiki serve bound to 0.0.0.0.
- **iOS Shortcut**: Share Sheet trigger confirmed available; Shortcut Input variable confirmed insertable. Root cause of "invalid HTTP request" is nil Shortcut Input when triggered from inside Shortcuts app, not from Share Sheet.

---

## Commits this session

- `60df633` fix(research): bound synthesis page slugs to 80-char validator limit
- `180f70d` fix(youtube-adapter): throttle inter-query calls to avoid 429s
- `787444b` chore(session): checkpoint 2026-05-28 — orphan discharge + R3 attempts
- `37f186b` Merge remote-tracking branch 'origin/main'

---

## Next atomic step

1. **iOS Shortcut completion**: Safari → Share → Wiki Capture → confirm task_id notification → export to `scripts/wiki-capture.shortcut` → commit.
2. **R3 retry**: `.venv/bin/wiki research --execute 2026-05-28-orita-gcp-r3` (tomorrow, after YouTube quota resets).
3. **R2**: user exports HubSpot CSVs → `wiki ingest <csv-path> --domain orita-cmo --with-plan`.
4. **Gateway Phase 13**: set `ANTHROPIC_API_KEY_RESEARCH` → `wiki evaluate --all-domains` → `wiki finalize-batch --suggest --execute`.
