# Session state — 2026-05-28

Last updated: 2026-05-28 (Orita-CMO domain bootstrapped; R1 HubSpot capability research complete; nlm login bug root-caused)

---

## Open contracts

None.

Carry-forward (gateway build, unchanged from prior session):
- **ANTHROPIC_API_KEY_RESEARCH**: must be set in shell for edge-ai-agentic and glp1-reward-modulation eval runs. See RUNBOOK.md § Evaluation failures. Once set, `wiki evaluate --all-domains` will run cleanly for all four domains.
- **finalize-batch escalated**: 379 escalated drafts (uncited claims). `--suggest` unblocked once API key is set.
- **schema-drift**: 208 remaining (legacy editorial tail — entity_kind, slug, canonical_name — human judgment).
- **orphans**: 531 wiki-page orphans. discharge-orphans now auto-commits; next run on any domain will be clean.
- **INT-18/INT-19 hand-tests**: deferred (live tokens required).
- `wiki migrate` stub remains.

Carry-forward (new from this session):
- **`nlm login` silent-failure bug (CORRECTED DIAGNOSIS, supersedes prior "cookies expire within seconds")**: when Google Chrome is running, `nlm login` (v0.6.12) attaches via Chrome DevTools Protocol and may report "✓ Successfully authenticated!" while NOT actually validating against Google. Verified mechanism: `~/.notebooklm-mcp-cli/profiles/default/metadata.json` `last_validated` timestamp does NOT advance; subsequent operations fail with "Authentication expired." Operations CAN run for 10+ min against valid auth (R1 run #1 reached materialize step 12min in), so the prior diagnosis ("cookies expire in seconds in CLI subprocess context") was wrong on mechanism. Fix protocol: (a) quit Chrome fully (Cmd-Q, not just close windows); (b) `nlm login`; (c) verify with `nlm login --check` — must show "Authentication valid!" AND `metadata.json` `last_validated` MUST advance to current time. The `--clear` flag is an alternative; quit-and-retry was the validated path this session.
- **Gateway gaps filed in docs/260527_knowledge_phase12_backlog-rubric.md § 5** (all S-effort, marked Active on recurrence):
  - `wiki nlm-register <domain> <notebook_id>` CLI — no surface to bind an existing notebook; only auto-create path via `_resolve_or_create_notebook` (src/gateway/ops/nlm.py:63). Two domains registered by direct YAML edit (glp1-reward-modulation `1a5d99b`, orita-cmo `c372346`).
  - `NoteConverter` for local `.md` and `.txt` — `note` is in `paths.SOURCE_TYPES` but no converter is registered; only pollers (apple_notes, notion, repo_metadata) write to `raw/note/`. Workaround: pandoc → `.docx` → ingest via DocxConverter.
  - `wiki ingest` idempotent-reingest skips domain-tag step — when content_hash matches, frontmatter `domains: []` is NOT updated. `wiki nlm-add <domain> <source_id>` is the correct semantic completion (writes both domain tag and corpus binding), but the gap in `wiki ingest` is worth surfacing.
- **YouTube adapter HTTP 429 on retry-exhaustion** reproduced this session during R1 multi-adapter fan-out. Adapter returned partial data (95 candidates → 0 in the third R1 run). Known issue per session-state predecessor; no fix this session.
- **VOC corpus (Avoma transcripts + Klaviyo community + Reddit + podcasts) is a separate workstream**, NOT part of `orita-cmo`. The domain policy at `.knowledge/policies/orita-cmo/policy.yaml` explicitly excludes raw VOC sources (exclusion criterion #3); synthesized VOC outputs may cite into the domain.

---

## Files mid-edit

None. R1 committed in `9bd8350`. lint --scope contradiction-pages: 0 findings.

---

## Decisions made this session

- **Orita-CMO is a domain in the knowledge wiki** (not a free-standing project). Phase 0.1 (notebook registry) + 0.2 (policy bootstrap) + 1.x (5-source seed) + R1 (HubSpot capability research, 5 sources, ~22 wiki pages) complete. Domain at 10 sources total, ~50 wiki pages, lint clean.
- **C2 validation harness design = (a) dry-run queue with approval gate** (Postgres queue on the chosen GCP stack + Slack approval surface). Committed before R1 ran; R1's safe-write-pattern arxiv + semantic_scholar candidates all filter-rejected. Design now proceeds from the commitment without further pre-research.
- **R1 partial-completion accepted**: HubSpot MCP capability surface (two-server architecture, OAuth 2.0 → 2.1 + PKCE), association labels (incl. Pro/Enterprise license gate — Starter blocked), and Breeze buy-vs-build inputs ("priced to the teeth"; weak writes) are well-covered. Community MCP variants (peakmojo et al.) and canonical REST + Private Apps docs are gaps deferred unless R2/R3 surfaces specific need.
- **Authoritative positioning of Orita**: charter framing ("AI-powered audience intelligence layer; platform-agnostic ML scoring engine") leads. Transcript's "AI customer segmentation for the Klaviyo ecosystem" treated as colloquial CMO description tied to the Klaviyo beachhead, not full product architecture. Resolved 4 logged contradictions on wiki/entities/orita.md + 1 on wiki/entities/klaviyo.md in commit `faf7c3b`.
- **Authorship path**: incremental `wiki ingest --with-plan` (not `batch-ingest`). Validated end-to-end. Idempotent on content_hash; `wiki nlm-add` is the required completion step for domain tagging + corpus push.

---

## Commits this session

- `c372346` fix(nlm-registry): register orita-cmo notebook adc34eb9
- `b7c1288` feat(domain): bootstrap orita-cmo domain policy
- `905f0ef` feat(orita-cmo): seed corpus ingest — 5 sources, ~30 wiki pages
- `e586a4b` docs(phase12-backlog): file nlm-register + NoteConverter gateway gaps
- `faf7c3b` fix(orita-cmo): reconcile orita+klaviyo positioning contradictions
- `9bd8350` feat(orita-cmo): R1 HubSpot capability research — 5 sources, ~22 wiki pages

---

## Next atomic step

**Auth protocol before any nlm-touching operation in next session:**
1. Quit Chrome fully (Cmd-Q, not just window-close).
2. `nlm login` (or `nlm login --clear`).
3. `nlm login --check` — must report "Authentication valid!" AND `~/.notebooklm-mcp-cli/profiles/default/metadata.json` `last_validated` must advance to current time.
4. Proceed with `wiki nlm-*` / `wiki research` operations.

**Orita-CMO research stream (§6 of the research plan committed in faf7c3b context):**
1. **R3 — multi-user/GCP deployment patterns**. Self-contained; no human input needed. `wiki research --review` → user-edits-if-needed → `--execute`. Standard pattern; auth blocker is now well-understood.
2. **R2 — ICP validation against HubSpot closed-won data**. Requires user to export HubSpot closed-won + closed-lost CSVs (12-month window) so they can be ingested via `wiki ingest <csv-path> --domain orita-cmo --with-plan`. Blocked on user-side action.

Recommended order: R3 first (parallelizable with the user pulling HubSpot data), then R2 when CSVs land.

**Gateway build (unchanged from prior session, Phase 13 gate):**
1. User sets `export ANTHROPIC_API_KEY_RESEARCH=sk-ant-...` in shell.
2. `wiki evaluate --all-domains` → confirm all 4 domains score cleanly.
3. `wiki finalize-batch --suggest --execute` → citation auto-fill on 379 escalated drafts.
4. `wiki routine discharge-orphans --domain <domain> --limit 20` on any domain.

Backlog rubric (`docs/260527_knowledge_phase12_backlog-rubric.md`) now has three additional Active items eligible for next build phase (nlm-register CLI, NoteConverter, idempotent-reingest domain-tag fix).
