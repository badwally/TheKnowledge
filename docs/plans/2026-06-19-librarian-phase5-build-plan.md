# Librarian Phase 5 — Lifecycle & Demand Governance — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task (fresh implementer + independent task-review + fix per task). Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the corpus loop — un-canonicalization (retraction cascade + resolution reversal), corpus-rot remediation, the DemandLedger + canonicalization trigger, gap-routing + keep-worthiness, and the planner/executor pre-flight — landing constraint IDs G1, G2, G3, G4, G6, G7, G8, I3, I4, F1 (claim-conservation), A4.

**Architecture:** Four tasks in the §0 build order: `INV,PROV,CG → ROT/LIFE`; `TIER,DEP → GAP`; `GAP → DEM`; `DEM,EMB → PEX`. T1 retraction/reversal (un-canonicalization, the destructive-but-reversible keystone) → T2 remediation + claim-conservation (the other destructive path) → T3 gap-routing + keep-worthiness (additive, on retrieve/answer/deposit) → T4 DemandLedger + preflight (additive, on the question embedding namespace). Every un-canonicalization or de-path action is a **provenanced, reversible CommitGate intent** — never an in-place mutation.

**Tech Stack:** Python 3 (`.venv/bin/python`, `.venv/bin/wiki` ONLY — system python lacks the gateway pkg), pytest, numpy, git-as-database. All corpus writes via the gateway / CommitGate; `docs/`, `src/`, `tests/` are direct-edit.

## Global Constraints

- **Environment:** `.venv/bin/python -m pytest` and `.venv/bin/wiki <sub>` only. Never system python.
- **Writes:** No direct writes to `wiki/` or `raw/` — all corpus mutation flows through the CommitGate as a typed, provenanced intent. `docs/`/`src/`/`tests/` are direct-edit.
- **Git hygiene (shared tree):** Never `git add -A` / `git add -u`. Guard `git branch --show-current` == `docs/librarian-phase5` before EVERY commit. Never stage watcher-owned `index.md` / `log.md` / `.knowledge/` / `.index/`. Stage only the exact files the task touched.
- **Lint:** Never run unscoped `wiki lint` as a gate (no per-check timeout; hung 1h28m a prior session). Run scoped: `wiki lint --scope orphans|schema-drift|broken-wikilinks` (seconds each).
- **Reversibility invariant:** Any op that un-canonicalizes (retraction cascade, resolution reversal, reverse-merge) or de-paths a page MUST (a) be a CommitGate intent, (b) record a reversible provenance act, (c) never destroy a reachable/cited page.
- **Standing build rule (every phase):** Write adversarial tests with **named negative controls** for every concurrency / destructive-op / idempotency / merge-reattachment path. Do NOT monkeypatch the core path under test. Merge/transform/reattachment/reverse tests MUST use **realistic payloads** (full multi-section body, frontmatter aliases, inbound + body wikilinks, non-empty preamble) — never claims-only stubs (the Phase-3 silent-corruption defects all hid behind minimal fixtures). The gate runs an INDEPENDENT review (reviewer ≠ author).
- **Verify-Before-Act on recorded structures:** The plan's exact on-disk schemas for the resolution-act JSONL, the merge-reattachment record, and the tombstone `redirect:`/`merged_into:` keys were partly reconstructed during interface mapping. Before implementing T1/T2, the builder MUST read the actual writer (`commit_gate.py` lines ~529–547 and ~797–805; `ops/contradiction.py`; the `.knowledge/contradictions/` writer) and assert the test against the REAL recorded format, not this plan's reproduction. A wrong assumed schema is a plan defect — verify first.
- **Eval floor:** `eval-retrieval --compare` fts recall@10 ≥ 0.90 (baseline 0.926). Any `_authority_key`/ranking change must not regress it.

---

## File Structure

| File | Responsibility | Task |
|---|---|---|
| `src/gateway/ops/revert_resolution.py` (new) | `revert-resolution <act-id>` op — submit a reversal as a CommitGate intent (G1) | T1 |
| `src/gateway/retraction.py` (new) | Pure cascade walk over `synthesizes:` + `[[sources/<id>]]` graphs to a fixpoint, cycle-terminating (G4); resolution-act re-open selection (G3); reverse-merge restore plan (G8) | T1 |
| `src/gateway/lint/retracted_citations.py` (modify) | Extend to surface transitive cascade dependents | T1 |
| `src/gateway/validator.py` (modify ~594) | Reuse `validate_synthesizes_integrity` walk for cascade reachability | T1 |
| `src/gateway/ops/remediate.py` (new) | De-path-as-intent (provenanced, reversible); never touches a reachable page (G6) | T2 |
| `src/gateway/lint/fragmentation.py` (new) | Fragmentation lint over high-mutual-similarity concept clusters | T2 |
| `src/gateway/lint/claim_conservation.py` (new) | Reconcile every committed intent's payload claims against the corpus (F1) | T2 |
| `src/gateway/ops/lint.py` (modify) | Register `fragmentation` + `claim-conservation` checks | T2 |
| `src/gateway/ops/retrieve.py` (modify) | Corpus-miss telemetry field | T3 |
| `src/gateway/ops/answer.py` (modify) | Corpus-first ladder + corpus-miss telemetry | T3 |
| `src/gateway/ops/deposit.py` (modify) | Keep-worthiness fields + orient-vs-ground gate (durable claim needs ingested source) | T3 |
| `src/gateway/demand_ledger.py` (new) | Online gap clustering (radius + recurrence-mass + cold-start), canonicalization trigger, raw-gap-text retention (I4) | T4 |
| `src/gateway/ops/preflight.py` (new) | Read-tier plan-time gap pre-flight + enrichment-status check | T4 |
| `src/gateway/reversal_detectors.py` (new) | Pure reversal/anomaly detectors over snapshots — §1.5 signals (G2) | T5 |
| `src/gateway/ops/policy_edit.py` (new) | Privileged-intent policy-edit path (G7) | T6 |
| `src/gateway/lint/policy_provenance.py` (new) | Out-of-band policy-edit detector (G7) | T6 |
| `.knowledge/eval/dedup/` merge-map golden + `merge_map_eval` | Dedup-precision non-regression gate (I3) | T6 |
| `src/gateway/embedding_index.py` (modify ~80) | Demand threshold keys | T4 |
| `src/gateway/tier.py` (modify ~30) | Add `preflight` to READ_OPS | T4 |
| `src/gateway/mcp_server.py` + `cli.py` (modify) | Register `revert-resolution`, `remediate`, `preflight` | T1/T2/T4 |
| `tests/gateway/test_retraction_cascade.py`, `test_revert_resolution.py`, `test_remediation.py`, `test_claim_conservation.py`, `test_gap_routing.py`, `test_keep_worthiness.py`, `test_demand_ledger.py`, `test_preflight.py` (new) | Per-task adversarial tests + negative controls | all |

---

## Verified interface anchors (from interface mapping; file:line)

- `OperationResult` — `src/gateway/core.py:84-101`: `success, intent_id, disposition, retry_after, canonical_path, paths_touched, summary, errors, warnings, data, no_op`.
- `IntentQueue.submit(intent)` durable enqueue; `compute_intent_id(payload, identity, *, semantics=...) -> str` — `src/gateway/intent_queue.py`. Terminal states under `.knowledge/intents/{committed,merged,dead_lettered}/`.
- `CommitGate.commit(authored: AuthoredIntent, fencing_token: int) -> OperationResult` — `commit_gate.py:298-547`. `AuthoredIntent(intent, writes: dict[rel,str], base_oid, base_oids, decision_basis: dict)` — `commit_gate.py:68-89`. Provenance recorded at `:529-539`; tombstone written at `:797-805`; `_claim_union(base,head,authored)->str|None` at `:216-258`.
- `validate_synthesizes_integrity(front, body) -> ValidationResult` — `validator.py:594-657`. `ValidationResult(errors, warnings)`, `.merge(other)`.
- `ops/contradiction.auto_resolve(side_a, side_b, *, policy_version=...) -> dict` — `ops/contradiction.py:32-67`. Resolution acts appended to `.knowledge/contradictions/resolution_acts.jsonl` (VERIFY exact reader/writer names + act keys before T1).
- `provenance.record(intent_id, decision_basis, *, root=None) -> node_id`; `provenance.read_nodes(*, root=None) -> list[dict]`; `provenance.coverage_gap(*, root=None) -> list[str]` — `provenance.py:42-140`. Stored `.knowledge/provenance/nodes.jsonl`.
- `search_index.inbound_counts(rel_paths: list[str]) -> dict[str,int]` — `search_index.py:476-494`. `search_index.related_pages(rel_path, *, limit=10) -> list[RelatedPage(rel_path, slug, title, page_type, shared, inbound_count)]` — `:525-573`. `citations.find_wikilinks(body)`.
- Lint: `_CHECKS: list[tuple[str, Callable[[], list[LintFinding]]]]` — `ops/lint.py:49-78`. `LintFinding(check, severity, message, path="", metadata={})` — `lint/__init__.py:25-40`. `lint(*, scope=None) -> OperationResult`. `retracted` (bool) read in `lint/retracted_citations.py:22-38`; `superseded_by` (str) in `lint/superseded_citations.py:14-29`. `walk_wiki_pages()` yields `(type_name, path, front, body)`.
- `EmbeddingIndex.nn(namespace, text, k=5) -> list[NNHit(key, distance)]` — `embedding_index.py:285-307`. `upsert(namespace, key, text)` — `:215-229`. `NAMESPACES=("section","entity","question")` — `:58`. `thresholds() -> dict[str,float]` — `:68-80` (`section 0.55, entity 0.30, question 0.70`). Thresholds are hardcoded in that dict today — add demand keys there.
- `retrieve(query, *, domain, domains, k, budget_chars, ...) -> (str, list[RetrievedSection])` — `ops/retrieve.py:83-93`; `retrieve_op(..., caller=None) -> OperationResult` logs via `log.append(op="retrieve", fields=...)` at `:224-237`; empty → `("", [])` / `success=False`.
- `answer(question, *, domain, domains, k=12, budget_chars=40000, client, model) -> AnswerResult(answer, sections, source_ids, stripped, usage)` — `ops/answer.py:77-86`; `answer_op(...) -> OperationResult`; miss → `success=False, summary="no wiki context found"` (no web fallback today).
- `deposit(payload, identity, *, depends_on=None, queue=None) -> OperationResult` — `ops/deposit.py:51-95`; `_validate` at `:30-48`; `_DEPOSIT_PAGE_TYPES={"entity","concept","source","synthesis"}`; `MAX_BACKLOG=256`.
- `log.append(op, fields=None, summary="") -> str` — `log.py:50-67` (holds `file_lock("log")`).
- `tier.READ_OPS` frozenset + `read_tier_tool_names()` — `tier.py:30-61`. Read-tier MCP factory `build_read_tier_server()` — `mcp_server.py:1378-1392` (iterates `read_tier_tool_names()`, `getattr` each, `read.tool()(fn)`).
- Test fixtures: `kb_root` (`tests/gateway/conftest.py:31-48`, sets `KNOWLEDGE_ROOT`, pre-creates dirs); `tmp_commit_env` (real git + `IntentQueue` + `CommitGate` + live domains, `test_dedup_commit.py:45-63`); `tmp_queue_env` (`test_deposit.py:19-36`); `_StubClient` for answer (`test_ws6_answer.py:14-41`).

---

# Task 1 — Retraction cascade + resolution reversal (Option A)

**Lands:** G1 (revert-resolution provenanced + reversible), G3 (retracting a winner re-opens its resolution acts), G4 (transitive `synthesizes:` cascade to a fixpoint, cycle-terminating), G8 (reverse-merge restores from the reattachment set); «retraction.cascade_trigger», «contradiction.precedence».

**Files:**
- Create: `src/gateway/retraction.py`, `src/gateway/ops/revert_resolution.py`
- Modify: `src/gateway/lint/retracted_citations.py`, `src/gateway/mcp_server.py`, `src/gateway/cli.py`
- Test: `tests/gateway/test_retraction_cascade.py`, `tests/gateway/test_revert_resolution.py`

**Interfaces:**
- Consumes: `retracted`/`superseded_by` frontmatter; the `[[sources/<id>]]` graph (`citations.find_wikilinks`); the `synthesizes:` graph (validator walk); resolution acts in `.knowledge/contradictions/resolution_acts.jsonl`; the merge-reattachment record in provenance `decision_basis`; `IntentQueue.submit`, `compute_intent_id`, `OperationResult`.
- Produces:
  - `retraction.cascade(retracted_source_ids: set[str], *, root=None) -> CascadeResult` where `CascadeResult` = `@dataclass(frozen=True)` with `flagged: list[str]` (rel_paths flagged/quarantined, in deterministic discovery order), `terminated_on_cycle: bool`, `depth: int`.
  - `retraction.acts_to_reopen(retracted_source_ids: set[str], *, root=None) -> list[dict]` (resolution acts whose winner source was retracted).
  - `retraction.reverse_merge_plan(tombstone_rel: str, *, root=None) -> ReverseMergePlan` (`canonical_rel`, `aliases_to_remove`, `sections_to_remove`, `claims_to_remove`, `tombstone_to_delete`).
  - `revert_resolution(act_id: str, identity: dict, *, queue=None) -> OperationResult` (disposition `"queued"`, intent records `reverts_act`).

### Step 0 (Verify-Before-Act): read the real recorded formats

- [ ] **Read** `commit_gate.py:520-547` (provenance basis written on commit) and `:790-810` (tombstone writer) and `ops/contradiction.py` + the `.knowledge/contradictions/` writer. Confirm the EXACT keys: the resolution-act JSONL field names (`winner`/`loser`/`rule`/`policy_version`/`inputs`/`resolved_at` vs whatever is actually written), the tombstone keys (`merged_into`, `redirect`), and where the reattachment set lives (`decision_basis["merge_reattachment"]` or another key). Write the verified schema as a comment block at the top of `retraction.py`. Every test below asserts the REAL format.

### G4 — transitive `synthesizes:` cascade to a fixpoint, cycle-terminating

- [ ] **Step 1: Write the failing test (chain + cycle, realistic pages).**

```python
# tests/gateway/test_retraction_cascade.py
import pytest
from gateway import retraction
from gateway import frontmatter as fm
from gateway import paths

def _synth(slug, synthesizes, body_extra=""):
    d = paths.wiki_dir() / "synthesis"; d.mkdir(parents=True, exist_ok=True)
    front = {"type": "synthesis", "slug": slug, "title": slug.replace("-", " "),
             "synthesizes": list(synthesizes), "domains": ["med"],
             "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z"}
    body = (f"# {slug}\n\n## Included works\n" +
            "".join(f"- [[{s}]]\n" for s in synthesizes) +
            f"\n## Analysis\n\nLoad-bearing claim [[{synthesizes[0]}]].\n{body_extra}")
    (d / f"{slug}.md").write_text(fm.serialize(front, body))

def test_cascade_flags_transitive_dependents_to_fixpoint(kb_root):
    # source pubmed-1 -> A synthesizes it -> B synthesizes A
    _synth("a", ["sources/pubmed-1"])
    _synth("b", ["synthesis/a"])
    res = retraction.cascade({"pubmed-1"})
    flagged = set(res.flagged)
    assert "wiki/synthesis/a.md" in flagged
    assert "wiki/synthesis/b.md" in flagged   # transitive
    assert res.depth >= 2

def test_cascade_terminates_on_cycle(kb_root):
    _synth("x", ["synthesis/y", "sources/pubmed-1"])
    _synth("y", ["synthesis/x"])
    res = retraction.cascade({"pubmed-1"})
    assert res.terminated_on_cycle is True
    assert {"wiki/synthesis/x.md", "wiki/synthesis/y.md"} <= set(res.flagged)

def test_cascade_negative_control_unrelated_page_not_flagged(kb_root):
    _synth("a", ["sources/pubmed-1"])
    _synth("unrelated", ["sources/pubmed-2"])   # cites a DIFFERENT, non-retracted source
    res = retraction.cascade({"pubmed-1"})
    assert "wiki/synthesis/unrelated.md" not in set(res.flagged)
```

- [ ] **Step 2: Run, verify it fails** — `.venv/bin/python -m pytest tests/gateway/test_retraction_cascade.py -v` → FAIL (`retraction` has no `cascade`).

- [ ] **Step 3: Implement `retraction.cascade`** — BFS/DFS over wiki pages: seed = pages whose body cites any `sources/<retracted-id>`; expand via `synthesizes:` reverse edges (a page B is a dependent if B `synthesizes` a flagged page's slug). Track `visited` set → fixpoint; if a back-edge revisits an in-progress node, set `terminated_on_cycle=True` and continue (never infinite-loop). Deterministic order (sorted rel_paths). Return `CascadeResult`.

- [ ] **Step 4: Run, verify pass.** All three cascade tests green.

- [ ] **Step 5: Commit** — `git add tests/gateway/test_retraction_cascade.py src/gateway/retraction.py && git commit` (after branch guard).

### G3 — retracting a winner re-opens its resolution acts

- [ ] **Step 6: Failing test.** Build a real `tmp_commit_env`, commit two contradictory claims so `auto_resolve` writes an act with a winner source; then assert `retraction.acts_to_reopen({winner_source_id})` returns that act, and `acts_to_reopen({unrelated_id})` returns `[]` (negative control). Assert against the REAL act keys verified in Step 0.

- [ ] **Step 7: Run → FAIL.**

- [ ] **Step 8: Implement `acts_to_reopen`** — read `.knowledge/contradictions/resolution_acts.jsonl` (via the verified reader), filter acts where the winner's source id ∈ retracted set, skip acts already reverted (a `reverts_act` marker exists). Return matching act dicts.

- [ ] **Step 9: Run → PASS. Commit.**

### G8 — reverse-merge restores from the reattachment set (realistic payload)

- [ ] **Step 10: Failing test (realistic merged payload).** In `tmp_commit_env`, commit entity A (canonical), then a second deposit B with the SAME referent carrying: aliases, a multi-section body (`## Mechanism`, `## Claims` with 2 bullets), inbound + body wikilinks, a non-empty preamble — so the merge writes a real reattachment set + tombstone. Then assert `retraction.reverse_merge_plan(tombstone_rel)` returns a plan that (a) targets the canonical, (b) lists exactly the aliases unioned from B, (c) lists the sections/claims carried from B, (d) marks the tombstone for deletion. Negative control: a canonical page that was NEVER a merge target yields an empty/raises plan, not a spurious restore.

- [ ] **Step 11: Run → FAIL.**

- [ ] **Step 12: Implement `reverse_merge_plan`** — read the tombstone (`merged_into`/`redirect`), read the canonical, and read the merge-reattachment record from provenance `decision_basis` to compute exactly what B contributed (do NOT diff-guess; use the recorded set, per the Phase-3 lesson that drops hide in diffs). Return the plan; raise/empty for non-tombstones.

- [ ] **Step 13: Run → PASS. Commit.**

### G1 — `revert-resolution` is a provenanced, reversible CommitGate intent

- [ ] **Step 14: Failing test.**

```python
# tests/gateway/test_revert_resolution.py
from gateway.ops.revert_resolution import revert_resolution
from gateway.intent_queue import IntentQueue

def test_revert_resolution_enqueues_provenanced_intent(tmp_queue_env):
    res = revert_resolution("act-abc123", {"agent": "tester"})
    assert res.success and res.disposition == "queued" and res.intent_id
    rec = IntentQueue().read_record(res.intent_id)  # use the real read API verified in Step 0
    assert rec["payload"]["reverts_act"] == "act-abc123"
    assert rec["identity"]["operation"] == "revert-resolution"

def test_revert_resolution_idempotent_same_act_same_intent_id(tmp_queue_env):
    a = revert_resolution("act-abc123", {"agent": "tester"})
    b = revert_resolution("act-abc123", {"agent": "tester"})
    assert a.intent_id == b.intent_id   # content-addressed; redelivery is a no-op downstream
```

- [ ] **Step 15: Run → FAIL.**

- [ ] **Step 16: Implement `revert_resolution`** — mirror `ops/deposit.py`: build `payload={"reversal_type":"contradiction-resolution","reverts_act":act_id,"policy_version":"contradiction-reversal-policy-v1"}`, `identity` with `operation="revert-resolution"`, `iid = compute_intent_id(payload, identity, semantics="revert")`, `queue.submit(Intent(...))`, return `OperationResult(success=True, intent_id=iid, disposition="queued", retry_after=2)`. The CommitGate applies the reversal (removes the `## Contested`/`disputes` edge, restores claim status) and records a provenance node linking `reverts_act` — reversible. (If the CommitGate apply-path for reversal-type intents does not yet exist, add a minimal branch in `commit_gate.py` keyed on `payload["reversal_type"]`, TDD'd in the same step with a real-gate test.)

- [ ] **Step 17: Run → PASS. Commit.**

### Cascade surfaced in lint + CLI/MCP registration

- [ ] **Step 18: Failing test** — extend `lint/retracted_citations.py` so a retracted source surfaces the transitive cascade dependents as findings (one `LintFinding` per flagged page, `metadata={"retracted_source": id, "depth": n}`). Negative control: no retracted sources → no findings.
- [ ] **Step 19: Run → FAIL. Step 20: Implement** (call `retraction.cascade` from the check). **Step 21: PASS.**
- [ ] **Step 22: Register `revert-resolution`** in `cli.py` (`SUBCOMMANDS` help + `IMPLEMENTED` + `build_parser` with `act_id` positional) and `mcp_server.py` build-tier (`@mcp.tool() def wiki_revert_resolution(act_id: str) -> dict: return _serialize(revert_resolution(act_id, {"agent": "mcp"}))`). It is BUILD-tier (it enqueues a mutation) — do NOT add to `READ_OPS`. Test: CLI parses; tool name absent from `read_tier_tool_names()`.
- [ ] **Step 23: Run scoped lint + full suite** — `.venv/bin/python -m pytest tests/gateway/test_retraction_cascade.py tests/gateway/test_revert_resolution.py -v`; then `.venv/bin/wiki lint --scope retracted-citations`. **Commit.**

---

# Task 2 — Corpus-rot remediation sweep + fragmentation lint + claim-conservation

**Lands:** G6 (de-path nothing reachable from the provenance graph; de-path is provenanced + reversible), F1 (claim-conservation accounts for every committed intent's payload claims); corpus.orphan_pct_ceiling, corpus.untagged_pct_ceiling.

**Files:**
- Create: `src/gateway/ops/remediate.py`, `src/gateway/lint/fragmentation.py`, `src/gateway/lint/claim_conservation.py`
- Modify: `src/gateway/ops/lint.py` (register both checks), `src/gateway/cli.py`, `src/gateway/mcp_server.py`
- Test: `tests/gateway/test_remediation.py`, `tests/gateway/test_claim_conservation.py`

**Interfaces:**
- Consumes: `search_index.inbound_counts`, `search_index.related_pages`, `citations.find_wikilinks`; `provenance.read_nodes`; `EmbeddingIndex.nn` (entity namespace); intent terminal records under `.knowledge/intents/{committed,merged}/`; the `## Claims` parser used by `_claim_union`.
- Produces:
  - `remediate(*, root=None, dry_run=False, queue=None) -> OperationResult` — finds genuinely-orphaned uncited pages and submits a de-path intent (provenanced, reversible) for each; NEVER targets a reachable page. `data={"depathed": [...], "skipped_reachable": [...]}`.
  - `lint/fragmentation.run() -> list[LintFinding]` — concept clusters with mutual entity-namespace distance ≤ band.
  - `lint/claim_conservation.run() -> list[LintFinding]` — one finding per committed payload claim not found in the corpus.

### G6 — de-path never touches a reachable / cited page

- [ ] **Step 1: Failing test (realistic, with a live-citation-target trap).**

```python
# tests/gateway/test_remediation.py
from gateway.ops.remediate import remediate
from gateway import frontmatter as fm, paths, search_index

def _concept(slug, body):
    d = paths.wiki_dir() / "concepts"; d.mkdir(parents=True, exist_ok=True)
    front = {"type": "concept", "slug": slug, "title": slug, "domains": ["med"],
             "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z"}
    (d / f"{slug}.md").write_text(fm.serialize(front, body))

def test_depaths_orphan_but_keeps_zero_inbound_citation_target(kb_root):
    # 'orphan' has no inbound links and cites nothing -> de-path candidate
    _concept("orphan", "# orphan\n\nNo links here.\n")
    # 'target' has ZERO inbound wikilinks BUT is a live citation target reachable
    # from the provenance graph (a committed source cites it). Must NOT be de-pathed.
    _concept("target", "# target\n\nReal content [[sources/pubmed-1]].\n")
    # ... seed provenance so 'target' is reachable (helper builds a provenance node
    #     whose decision_basis references wiki/concepts/target.md) ...
    search_index.refresh(rebuild=True)
    res = remediate(dry_run=True)
    assert "wiki/concepts/orphan.md" in res.data["depathed"]
    assert "wiki/concepts/target.md" in res.data["skipped_reachable"]
    assert "wiki/concepts/target.md" not in res.data["depathed"]
```

- [ ] **Step 2: Run → FAIL.**
- [ ] **Step 3: Implement `remediate`** — candidate = page with `inbound_counts==0` AND not reachable from `provenance.read_nodes` (no node's `decision_basis` references it) AND not a live `[[sources/...]]`/wiki citation target. For each candidate, `dry_run` → collect; else submit a de-path CommitGate intent (`payload={"op":"depath","target_rel":rel,"reversible":True}`, content-addressed id) so the action is provenanced + reversible. Reachable pages → `skipped_reachable`.
- [ ] **Step 4: Run → PASS. Commit.**

### F1 — claim-conservation accounts for every committed intent's payload claims

- [ ] **Step 5: Failing test.**

```python
# tests/gateway/test_claim_conservation.py
from gateway.lint import claim_conservation

def test_every_committed_payload_claim_present_in_corpus(tmp_commit_env):
    gate, queue, emb = tmp_commit_env
    # commit a deposit whose body has 2 ## Claims bullets; both must land in corpus
    # ... build + commit a realistic entity with 2 claims ...
    findings = claim_conservation.run()
    assert findings == []   # all payload claims conserved

def test_dropped_claim_is_reported(tmp_commit_env):
    gate, queue, emb = tmp_commit_env
    # commit, then simulate a corpus page where one claim bullet was lost
    # ... mutate the committed page to drop one claim line ...
    findings = claim_conservation.run()
    assert any(f.check == "claim-conservation" and "missing" in f.message for f in findings)
```

- [ ] **Step 6: Run → FAIL.**
- [ ] **Step 7: Implement `claim_conservation.run`** — enumerate terminal intent records under `.knowledge/intents/{committed,merged}/`, parse each `payload["body"]`'s `## Claims` bullets (reuse the parser behind `_claim_union`), and for each claim verify it appears in the canonical page (accounting for merges via `merged_into`). Emit a `LintFinding(check="claim-conservation", severity="error", ...)` per unaccounted claim.
- [ ] **Step 8: Run → PASS. Commit.**

### Fragmentation lint

- [ ] **Step 9: Failing test** — create 3 near-duplicate concept pages (high mutual entity-namespace similarity) + 1 distinct; assert `fragmentation.run()` flags the cluster of 3 and not the distinct one (negative control). Upsert into the embedding index in the fixture.
- [ ] **Step 10: Run → FAIL. Step 11: Implement** `fragmentation.run` — for each concept page, `EmbeddingIndex.nn("entity", identity_text, k)`; group pages with mutual distance ≤ band (start at `entity` threshold 0.30, tunable); emit one `LintFinding` per cluster of size ≥ 2 with `metadata={"members": [...]}`. **Step 12: PASS.**
- [ ] **Step 13: Register both checks** in `ops/lint.py` `_CHECKS` (`("fragmentation", fragmentation.run)`, `("claim-conservation", claim_conservation.run)`); register `remediate` in `cli.py` + `mcp_server.py` build-tier (`wiki_remediate(dry_run: bool=False)`). Test: `lint(scope="fragmentation")` runs only it; `remediate` absent from `read_tier_tool_names()`.
- [ ] **Step 14: Run scoped lint + targeted suite. Commit.**

---

# Task 3 — Gap-routing ladder + keep-worthiness + corpus-miss telemetry

**Lands:** decision 10 (corpus-first ladder, orient-vs-ground gate), A4 (carry-forward suppression — an agent re-querying its own outstanding deposit logs no corpus-miss).

**Files:**
- Modify: `src/gateway/ops/retrieve.py`, `src/gateway/ops/answer.py`, `src/gateway/ops/deposit.py`
- Test: `tests/gateway/test_gap_routing.py`, `tests/gateway/test_keep_worthiness.py`

**Interfaces:**
- Consumes: `retrieve` / `answer` results; `log.append`; deposit `_validate`; the `[[sources/<id>]]` → `raw/<id>.md` resolution.
- Produces:
  - `retrieve_op`/`answer_op` log a `corpus_miss=1` field on empty results (and `corpus_miss=0` otherwise).
  - `deposit` rejects a durable claim whose only support is a non-ingested URL (orient-vs-ground gate); accepts when `[[sources/<id>]]` resolves to a real `raw/` page; accepts volatile-flagged deposits without canonicalizing them.
  - Keep-worthiness fields on the deposit payload: `half_life`, `load_bearing` (self-report + audit flag), `domain_core`, `recurrence` (all optional/nullable, validated for type).

### Corpus-miss telemetry + A4 suppression

- [ ] **Step 1: Failing test.**

```python
# tests/gateway/test_gap_routing.py
from gateway.ops.retrieve import retrieve_op
from gateway import paths

def test_retrieve_miss_logs_corpus_miss(kb_root):
    res = retrieve_op("nothing matches this query xyzzy", domain="med", caller="agent-1")
    assert not res.success
    log_text = paths.log_path().read_text()
    assert "corpus_miss=1" in log_text

def test_retrieve_hit_logs_no_miss(kb_root):
    # ... seed a matching page + refresh index ...
    res = retrieve_op("gastric emptying", domain="med", caller="agent-1")
    assert res.success
    assert "corpus_miss=1" not in paths.log_path().read_text().splitlines()[-1]

def test_a4_requery_of_own_outstanding_deposit_logs_no_miss(kb_root):
    # agent-1 has an outstanding deposit for the same topic; re-querying it must not
    # count as a corpus-miss (A4 carry-forward suppression)
    # ... enqueue a deposit by agent-1, then retrieve_op(..., caller="agent-1") ...
    res = retrieve_op("its own pending topic", domain="med", caller="agent-1")
    assert "corpus_miss=1" not in paths.log_path().read_text()
```

- [ ] **Step 2: Run → FAIL.**
- [ ] **Step 3: Implement** — in `retrieve_op`/`answer_op`, add `corpus_miss` to the `log.append` fields (1 on empty sections, else 0). For A4: before logging a miss, check the intent queue for an outstanding (`submitted`/`claimed`/`authored`) deposit by the same `caller` matching the topic; if present, suppress the miss (log `corpus_miss=0, suppressed_a4=1`).
- [ ] **Step 4: Run → PASS. Commit.**

### Keep-worthiness + orient-vs-ground gate

- [ ] **Step 5: Failing test.**

```python
# tests/gateway/test_keep_worthiness.py
from gateway.ops.deposit import deposit

def test_durable_claim_with_non_ingested_url_rejected(tmp_queue_env):
    res = deposit(
        {"page_type": "concept", "title": "X", "body": "durable claim (https://ex.com/a)",
         "durable": True},
        {"canonical_name": "X", "domains": ["med"]})
    assert res.disposition == "rejected"
    assert any("ingested source" in e for e in res.errors)

def test_durable_claim_with_ingested_source_accepted(tmp_queue_env):
    # ... create raw/web/<id>.md so [[sources/<id>]] resolves ...
    res = deposit(
        {"page_type": "concept", "title": "X", "body": "durable claim [[sources/web-1]]",
         "durable": True},
        {"canonical_name": "X", "domains": ["med"]})
    assert res.disposition == "queued"

def test_volatile_deposit_not_canonicalized(tmp_queue_env):
    res = deposit(
        {"page_type": "concept", "title": "X", "body": "fast-moving note", "volatile": True},
        {"canonical_name": "X", "domains": ["med"]})
    assert res.disposition == "queued"
    assert res.data.get("canonicalize") is False
```

- [ ] **Step 6: Run → FAIL.**
- [ ] **Step 7: Implement** — extend `deposit._validate`: accept + type-check optional `half_life`, `load_bearing`, `domain_core`, `recurrence`, `durable`, `volatile`. Orient-vs-ground gate: if `durable` and the body has no `[[sources/<id>]]` resolving to a real `raw/` page, return `OperationResult(success=False, disposition="rejected", errors=["durable claim needs an ingested source"])`. Volatile deposits carry `data={"canonicalize": False}`.
- [ ] **Step 8: Run → PASS. Commit.**

---

# Task 4 — DemandLedger + planner/executor pre-flight

**Lands:** decision 11 (DemandLedger clustering + canonicalization trigger), decision 12 (planner/executor pre-flight), I4 (raw-gap-text retained; re-embedding survives a model bump); «demand.proximity_radius», «demand.recurrence_mass», «demand.cold_start_min_recurrences», «embed.demand_gap_threshold».

**Files:**
- Create: `src/gateway/demand_ledger.py`, `src/gateway/ops/preflight.py`
- Modify: `src/gateway/embedding_index.py` (~80, demand keys), `src/gateway/tier.py` (~30, add `preflight` to READ_OPS), `src/gateway/cli.py`, `src/gateway/mcp_server.py`
- Test: `tests/gateway/test_demand_ledger.py`, `tests/gateway/test_preflight.py`

**Interfaces:**
- Consumes: logged corpus-misses (from T3); the `question` embedding namespace (`EmbeddingIndex.nn("question", ...)`); the new demand thresholds.
- Produces:
  - `DemandLedger.record_gap(text: str, *, caller=None) -> GapRecord` — logs a gap, retains raw text (I4).
  - `DemandLedger.cluster() -> list[GapCluster(centroid_text, member_texts, recurrence_mass, triggered: bool)]` — online clustering by `proximity_radius`; cold-start (first `< cold_start_min_recurrences` occurrences logged, not clustered); a cluster reaching `recurrence_mass` triggers exactly ONE canonicalization intent (dedup-by-cluster).
  - `DemandLedger.reembed(new_encoder) -> None` — re-clusters from retained raw text without resetting recurrence (I4).
  - `preflight(plan_text: str, *, root=None) -> OperationResult` (READ-tier) — returns gap-coverage + enrichment-status for a proposed plan.

### Demand thresholds

- [ ] **Step 1: Failing test** — assert `embedding_index.thresholds()` (or a new `demand_thresholds()`) returns `demand.proximity_radius`, `demand.recurrence_mass`, `demand.cold_start_min_recurrences` with the ledger §1.3 initial values (radius ≈ question band ~0.40, mass 5, cold-start 3). **Step 2: FAIL. Step 3: Implement** (add keys). **Step 4: PASS. Commit.**

### DemandLedger clustering + trigger + I4

- [ ] **Step 5: Failing test (purity + cold-start + trigger + I4).**

```python
# tests/gateway/test_demand_ledger.py
from gateway.demand_ledger import DemandLedger

def test_recurring_gap_triggers_exactly_one_canonicalization(kb_root):
    led = DemandLedger()
    for _ in range(6):  # >= recurrence_mass(5), past cold-start(3)
        led.record_gap("how does semaglutide affect gastric emptying")
    clusters = [c for c in led.cluster() if c.triggered]
    assert len(clusters) == 1

def test_first_occurrence_logged_not_triggered_cold_start(kb_root):
    led = DemandLedger()
    led.record_gap("a brand new gap never seen before")
    assert all(not c.triggered for c in led.cluster())

def test_purity_paraphrases_one_cluster_distinct_two(kb_root):
    led = DemandLedger()
    led.record_gap("semaglutide and gastric emptying")
    led.record_gap("how semaglutide slows gastric emptying")   # paraphrase
    led.record_gap("federal reserve interest rate policy")     # distinct
    clusters = led.cluster()
    assert len(clusters) == 2   # paraphrases merge, distinct stays separate

def test_i4_reembed_survives_model_bump_without_resetting_recurrence(kb_root):
    led = DemandLedger()
    for _ in range(4):
        led.record_gap("semaglutide gastric emptying")
    before = sum(c.recurrence_mass for c in led.cluster())
    led.reembed(new_encoder=_BumpedEncoder())   # re-cluster from retained raw text
    after = sum(c.recurrence_mass for c in led.cluster())
    assert after == before   # recurrence preserved across re-embed
```

- [ ] **Step 6: Run → FAIL.**
- [ ] **Step 7: Implement `DemandLedger`** — persist gap records (raw text + timestamp + caller) under `.knowledge/demand/gaps.jsonl` (retain raw text → I4). `cluster()`: embed each gap into `question` namespace, online-cluster by `proximity_radius`; a gap is eligible only after `cold_start_min_recurrences`; a cluster with mass ≥ `recurrence_mass` sets `triggered=True` and (in the trigger path) submits exactly one build-tier synthesis CommitGate intent (dedup-by-cluster — re-running does not double-trigger). `reembed`: drop vectors, re-embed from retained raw text, preserve per-cluster recurrence counts.
- [ ] **Step 8: Run → PASS. Commit.**

### Planner/executor pre-flight (read-tier)

- [ ] **Step 9: Failing test** — `preflight("a research plan about X")` returns `OperationResult(success=True, data={"gaps": [...], "enrichment_status": ...})`; assert `"preflight"` ∈ `tier.READ_OPS` and `"wiki_preflight"` ∈ `read_tier_tool_names()`; negative control: `preflight` must not enqueue any intent (queue depth unchanged) and must not spend tokens.
- [ ] **Step 10: Run → FAIL.**
- [ ] **Step 11: Implement `preflight`** — read-tier: for the plan text, run `retrieve` (LLM-free) to estimate coverage, check the DemandLedger for matching outstanding gaps, and report enrichment-status. No writes, no token spend. Add `"preflight"` to `tier.READ_OPS`; register `wiki_preflight` via the read-tier factory; add to `cli.py`.
- [ ] **Step 12: Run → PASS.** Verify `build_read_tier_server()` registers `wiki_preflight` and the parity test (`test_tier_parity.py`) still passes. **Commit.**

---

# Task 5 — G2 reversal / anomaly detectors

**Lands:** G2 (detect reversal/governance anomalies on the auto-resolution + cascade paths). Populates the §1.5 Option-B gating signals + §2 corpus-health metrics with REAL measured values (today they are `n/a`).

**Rationale:** The §1.5 Option-B triggers (`reversal.auto_resolution_reversal_rate`, `reversal.cross_project_override_rate`, `reversal.observed_cascade_depth`) are the signals that tell the operator when to build Option B (automatic transitive cascade-revert). Without G2 there is no instrument that measures them — the trigger for reviving Option B is itself unobservable. This is the observability gap on the correctness-critical auto-resolution loop. Build it as a pure function over snapshots, mirroring the Phase-4 `provenance.alarms()` pattern exactly.

**Files:**
- Create: `src/gateway/reversal_detectors.py`
- Modify: `src/gateway/ops/lint.py` (register a `reversal-anomalies` check that surfaces detector trips) OR expose via `provenance.alarms()`-style call (mirror Phase-4 A7 placement — verify where `alarms()` lives and co-locate)
- Test: `tests/gateway/test_reversal_detectors.py`

**Interfaces:**
- Consumes: resolution acts (`.knowledge/contradictions/resolution_acts.jsonl`, incl. reversal markers written by T1's `revert-resolution`); cross-project override markers (a resolution whose loser belongs to a different project/domain than the winner); cascade depth from T1's `CascadeResult.depth`.
- Produces: `reversal_detectors.detect(snapshot: dict, *, window_days: int = 30) -> list[Alarm]` where `Alarm = @dataclass(frozen=True)(name, value, threshold, tripped: bool, detail)`. Three detectors: `auto_resolution_reversal_rate` (reverted / total auto-resolutions in window), `cross_project_override_rate` (cross-project resolutions / total), `observed_cascade_depth` (max cascade depth seen). Thresholds = ledger §1.5 (5%, 10%, 3).

- [ ] **Step 1 (Verify-Before-Act):** Read the Phase-4 `provenance.alarms()` implementation + its test (`test_producer_telemetry.py`) and mirror its shape EXACTLY (pure function over a snapshot, named negative controls, `min_volume` floor so a tiny sample can't trip a rate). Confirm the resolution-act + reversal-marker fields T1 writes.
- [ ] **Step 2: Failing test** — each detector trips on its synthetic signal; negative controls: healthy traffic trips none; a below-`min_volume` sample cannot trip a rate detector. Use realistic act records.

```python
# tests/gateway/test_reversal_detectors.py
from gateway.reversal_detectors import detect

def test_reversal_rate_trips_above_5pct(kb_root):
    snap = {"auto_resolutions": 100, "reversed": 6, "cross_project": 0, "total": 100, "max_cascade_depth": 1}
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["auto_resolution_reversal_rate"].tripped is True

def test_healthy_traffic_trips_nothing(kb_root):
    snap = {"auto_resolutions": 100, "reversed": 1, "cross_project": 2, "total": 100, "max_cascade_depth": 2}
    assert all(not a.tripped for a in detect(snap))

def test_below_min_volume_cannot_trip_rate(kb_root):
    snap = {"auto_resolutions": 3, "reversed": 2, "cross_project": 0, "total": 3, "max_cascade_depth": 1}
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["auto_resolution_reversal_rate"].tripped is False  # min_volume floor
```

- [ ] **Step 3: Run → FAIL. Step 4: Implement** `detect` (pure, `min_volume` floor, thresholds from §1.5). **Step 5: PASS.**
- [ ] **Step 6:** Wire a `reversal-anomalies` lint check (or `alarms()`-style entry) that builds the snapshot from the real act log + cascade history and runs `detect`. Register in `ops/lint.py`. Test scope-runs only it. **Commit.**

---

# Task 6 — G7 privileged-intent policy-edit path + I3 merge-map golden gate

**Lands:** G7 (policy change-control enforced, not documented — changes touching dedup/trust/contradiction policy route through the CommitGate as a privileged, allowlisted intent), I3 (merge-map golden re-eval as a non-regression gate on dedup precision). «contradiction.precedence» + policy-version provenance.

**Scope boundary (deliberate):** Build the ENFORCED MECHANISM — the new `policy-edit` privileged-intent path + the gate (eval-compare + merge-map golden re-eval) + the allowlist check + a lint that flags out-of-band policy edits. The MIGRATION of the three existing direct-write ops (`bootstrap-domain`, `promote-domain`, `demote-domain`) onto this channel is the spec's named "migration delta" and is a **triggered backlog item** (regression risk to working domain ops; deserves its own focused validation). Hardcoded threshold constants (`commit_gate.py:626`, `deposit.py:27`) are gated by code-review/PR, not the runtime path — note this explicitly in the lint message so the boundary is documented, not silent.

**Files:**
- Create: `src/gateway/ops/policy_edit.py`, `.knowledge/eval/dedup/merge_map_golden.yaml` (or reuse `golden.yaml` as the merge-map source — verify in Step 0), `src/gateway/lint/policy_provenance.py`
- Modify: `src/gateway/commit_gate.py` (accept the `policy-edit` typed intent; run the gate before committing a policy write), `src/gateway/cli.py`, `src/gateway/mcp_server.py`
- Test: `tests/gateway/test_policy_change_control.py`, `tests/gateway/test_merge_map_golden.py`
- Backlog (write the file): `docs/backlog/librarian-policy-edit-migrate-existing-ops.md` (trigger: next substantive edit to `bootstrap_domain.py`/`promote_domain.py`/`demote_domain.py`, OR first observed out-of-band policy edit flagged by `policy_provenance` lint).

**Interfaces:**
- Consumes: `IntentQueue.submit`, `compute_intent_id`, `CommitGate.commit`; the existing dedup golden (`.knowledge/eval/dedup/golden.yaml` from Phase 3); `eval-retrieval --compare`; `policy_validator.validate_policy` (`bootstrap_domain.py` deps).
- Produces:
  - `policy_edit(domain: str, policy_data: dict, *, identity: dict, reason: str, queue=None) -> OperationResult` — validates shape, checks `identity` against the build-time allowlist, enqueues a `policy-edit` CommitGate intent (`payload={"op":"policy-edit","domain":...,"policy_data":...,"reason":...,"policy_version":...}`). Non-allowlisted identity → `rejected`.
  - CommitGate `policy-edit` branch: before committing the policy write, run the gate — `eval-retrieval --compare` must hold ≥ recall.floor AND the merge-map golden re-eval (I3) must not regress merge precision; on failure → `dead_lettered` with the failing metric, policy NOT written.
  - `merge_map_eval(golden_path, *, root=None) -> MergeMapResult(precision, recall, regressions: list)` — the I3 gate function.
  - `lint/policy_provenance.run()` — flags any live `policy.yaml` whose last change has no `policy-edit` provenance node (out-of-band edit detector). Message documents that hardcoded constants are gated by code-review, not this path.

### I3 — merge-map golden gate (build first; G7's gate depends on it)

- [ ] **Step 0 (Verify-Before-Act):** Read `.knowledge/eval/dedup/golden.yaml` (Phase-3 dedup golden) and the dedup eval harness (`test_dedup_golden.py` + any `evaluate/` dedup scorer). Decide: extend `golden.yaml` in place as the merge-map source, or add `merge_map_golden.yaml`. Confirm the `dedup.adjudicate` interface the eval calls.
- [ ] **Step 1: Failing test** — `merge_map_eval` returns precision/recall over the curated merge/link/distinct golden; a deliberately-broken adjudication (geometry-only) shows regressions (falsifiability negative control, mirroring the Phase-3 control). **Step 2: FAIL. Step 3: Implement** `merge_map_eval`. **Step 4: PASS. Commit.**

### G7 — privileged-intent policy-edit path

- [ ] **Step 5: Failing test.**

```python
# tests/gateway/test_policy_change_control.py
from gateway.ops.policy_edit import policy_edit
from gateway.intent_queue import IntentQueue

def test_allowlisted_identity_enqueues_policy_edit(tmp_queue_env):
    res = policy_edit("med", {"domain": {"slug": "med"}, "filter": {"threshold_include": 0.7}},
                      identity={"agent": "librarian-admin", "role": "policy-admin"},
                      reason="raise threshold")
    assert res.success and res.disposition == "queued"

def test_non_allowlisted_identity_rejected(tmp_queue_env):
    res = policy_edit("med", {"domain": {"slug": "med"}},
                      identity={"agent": "random-worker"}, reason="x")
    assert res.disposition == "rejected"
    assert any("allowlist" in e or "privileg" in e for e in res.errors)
```

- [ ] **Step 6: FAIL. Step 7: Implement** `policy_edit` (allowlist check → enqueue typed intent). **Step 8: PASS. Commit.**
- [ ] **Step 9: Failing test (the gate)** — in `tmp_commit_env`, a `policy-edit` intent that would regress the merge-map golden is `dead_lettered` and the policy file is NOT changed (negative control: a benign edit that holds both gates commits). **Step 10: FAIL. Step 11: Implement** the CommitGate `policy-edit` branch (run eval-compare + `merge_map_eval`; gate). **Step 12: PASS. Commit.**
- [ ] **Step 13: Implement `lint/policy_provenance`** + register; failing test first (an out-of-band-edited policy is flagged; a provenanced one is not). **Commit.**
- [ ] **Step 14: Register** `policy-edit` in `cli.py` + `mcp_server.py` build-tier (NOT read-tier). **Step 15: Write the migration backlog file** with the concrete trigger. **Commit.**

---

## Green-gate (verbatim from ledger §4, Phase 5 — all must be `[x]` with evidence)

- [ ] Retraction flags/quarantines transitive `synthesizes:` dependents to a fixpoint, terminating on cycles (G4). *Evidence:* `test_retraction_cascade.py` source→A→B chain + cycle + negative control.
- [ ] Retracting a winning source re-opens its resolution acts (G3); `revert-resolution` is provenanced + reversible (G1); reversed merge restores from the reattachment set (G8). *Evidence:* G3/G1/G8 tests.
- [ ] Lost-update claim-conservation accounts for every committed intent's payload claims (F1). *Evidence:* `test_claim_conservation.py` reconciliation pass + dropped-claim negative control.
- [ ] Demand clusters meet the purity gate; cold-start and re-embedding-survival hold (I4). *Evidence:* `test_demand_ledger.py` purity + cold-start + I4 tests.
- [ ] Remediation de-paths nothing reachable from the provenance graph (G6); de-path is a provenanced, reversible intent. *Evidence:* `test_remediation.py` citation-target survival test.

**Reconciled additions (the gate tests what the phase lands — see scope decision 2026-06-19):**
- [ ] Reversal/anomaly detectors trip on the §1.5 signals and stay quiet on healthy traffic (G2). *Evidence:* `test_reversal_detectors.py` three detectors + negative controls (healthy + below-min-volume).
- [ ] Policy edits route through a privileged, allowlisted CommitGate intent; non-allowlisted identity is rejected; an edit that regresses the merge-map golden is dead-lettered without writing the policy (G7). *Evidence:* `test_policy_change_control.py`.
- [ ] Merge-map golden re-eval guards dedup precision; a geometry-only adjudication shows regressions (I3). *Evidence:* `test_merge_map_golden.py` + falsifiability negative control.

## Phase gate (the loop GATE step — a failing eval OR review HALTS)

1. **Eval/tests:** full suite green (`.venv/bin/python -m pytest`); `.venv/bin/wiki eval-retrieval --compare` fts recall@10 ≥ 0.90 (baseline 0.926, must not regress); scoped lints at/under baseline (`orphans`, `schema-drift`, `broken-wikilinks`); all five §4 green-gate tests pass with named negative controls.
2. **Independent code-review** (reviewer ≠ author) on the whole branch diff + an independent **security review** (the destructive/reversible paths — de-path, reverse-merge, revert-resolution — are the attack surface). All Critical/Important fixed TDD (RED-before).
3. **/session-review.**
4. **Ledger update** — §4 Phase-5 all `[x]` with evidence; §5 five Phase-5 rows + the two cross-cutting rows → `green`; §1.3 demand keys + §1.7 corpus ceilings exercised. **/contp** + session-state STOP-condition reached + branch-guarded commit. **NO Phase 6 — build complete at Phase 5 gate green.** Open a PR.

---

## Self-Review (run against the build-plan spec)

- **Spec coverage:** G1 (T1 step14-17) · G2 (T5 — dedicated detectors) · G3 (T1 step6-9) · G4 (T1 step1-5) · G6 (T2 step1-4) · G7 (T6 — privileged-intent path; existing-op migration triggered-backlog) · G8 (T1 step10-13) · I3 (T6 — merge-map golden gate) · I4 (T4 step5-8) · F1 (T2 step5-8) · A4 (T3 step1-4). All accounted for with dedicated code + tests.
- **Scope decision (2026-06-19):** the master build-plan's traceability table lists G2/G7/I3 for Phase 5 but the original green-gate did not test them — a source-doc tension. Resolved by building dedicated code for all three (T5/T6) and reconciling the §4 gate to test them, so "gate green" means complete. G7's existing-op migration (cutting bootstrap/promote/demote off direct file I/O) is the spec's named "migration delta" — explicitly carried as a triggered backlog item (regression risk to working domain ops), not silently dropped. Hardcoded threshold constants are gated by code-review, documented in the `policy_provenance` lint message.
- **Placeholder scan:** no `TBD`/`handle edge cases`/`similar to Task N`. Test bodies that elide fixture setup (`# ... seed ...`) reference the verified fixture helpers (`tmp_commit_env`, `kb_root`, `_StubClient`) — the implementer fills them from the named helper, not from imagination.
- **Type consistency:** `OperationResult` fields, `CascadeResult`/`ReverseMergePlan`/`GapCluster` dataclasses, `LintFinding(check, severity, message, path, metadata)`, `NNHit(key, distance)` used consistently across tasks.
- **Verify-Before-Act:** T1 Step 0 and T2 forced to read the real recorded schemas before asserting — the Phase-3/Phase-4 session-review lesson (don't assert from the op name / reconstructed schema).
