# Continuation prompt — Multi-agent test harness + production committer

Paste the block below into a FRESH session (this work is a large multi-task build; the prior session hit its 50% context ceiling and handed off at a clean seam — nothing is committed on the branch yet).

---

```
Fresh session. Branch: test/multi-agent-test-harness (already cut off main @ 0a688378; verify with `git branch --show-current`; nothing committed on it yet). If not on it: `git checkout test/multi-agent-test-harness`.

OBJECTIVE: build the production intent-queue COMMITTER + a 6-tier automated test harness that drives the REAL system (no simulators). This closes the keystone gap found in planning: the async deposit→commit path has NO production drainer — deposits enqueue durably but nothing claims+authors+commits them. User ratified building the real committer (Option 2), NOT a test reference simulator (testing a simulator while production lacks the component = the inert-in-production trap this whole exercise exists to kill).

FIRST: read docs/MULTI-AGENT-BUILD-PLAYBOOK.md — it is the binding discipline (reviewer-dispatch template, the inert-in-production hunt list, the standing build rule, plan-time Verify-Before-Act). Then read this file's "VERIFIED INTERFACES" appendix below (plan-time Verify-Before-Act already done — do NOT re-verify; reuse it). Then run PLAN (writing-plans, scoped) → EXECUTE (subagent-driven-development) → GATE → CodeRabbit.

HARD RULES: .venv/bin/python + .venv/bin/wiki ONLY. Coordinator window ≤50% — keep build/review/fix in subagents; checkpoint + /contp + /clear at the ceiling. Never `git add -A`/`-u`; guard `git branch --show-current`==test/multi-agent-test-harness before every commit; never stage watcher-owned index.md/log.md/.knowledge/.index. Scoped lints only (orphans/schema-drift/broken-wikilinks — NOT unscoped). Apply the playbook: adversarial tests + named negative controls, no monkeypatching the core path, realistic payloads, opus reviewer≠author on every concurrency/destructive/governance task, drive-on-real-data.

TASKS (right-size in the PLAN step; ~8):
- D0 — Production committer. (a) `author_deposit(intent) -> AuthoredIntent` (NEW; deposit payload {page_type,title,body,aliases,domains,synthesizes} → {canonical_rel: rendered frontmatter+body}; reuse fm.serialize + slug logic; mirror the test fixture _authored_entity in test_dedup_commit.py). (b) drain loop: claim() → author_deposit → gate.commit(authored, fencing_token) → handle disposition (committed/merged/dead_lettered/retry-later); lease/fencing/recovery/backpressure already exist (don't rebuild). (c) entry: `wiki commit-worker` CLI + a launchd-style daemon mirroring `wiki watch` (watcher.py is the template). TDD: a deposited intent is autonomously committed end-to-end through the REAL loop; crash mid-author → lease expiry reclaims; poison/invalid intent → dead-letters, loop continues; write-skew (2 same-entity deposits) both survive.
- D1 — demand-cluster driver: `wiki demand-cluster` CLI op calling DemandLedger.cluster() (closes backlog I1). Mirror the `remediate` CLI registration (verbatim pattern in appendix). Optional: a `wiki schedule add` entry.
- M1 — pytest markers (unit/integration/e2e/slow) in pyproject [tool.pytest.ini_options] + a fast-inner-loop vs full `-m` split. Foundation for the heavier tiers.
- T2 — integration flow tests (driving the REAL committer D0): lifecycle chain deposit→commit→dedup-merge→retract source→cascade flags dependents→reverse-merge restores; demand loop corpus-miss→record_gap→cluster(D1)→canonicalization intent→committed; governance policy-edit via CLI→gate eval+merge-map→dead-letter on regression / commit on benign.
- T3 — N-agent concurrency soak: N concurrent depositors + the real committer draining; assert all intents reach terminal state, commits serialized, fencing rejects stale, backpressure sheds at MAX_BACKLOG=256, write-skew survivors both present, no torn writes. Mirror the threading.Event rendezvous pattern (appendix).
- T4 — surface E2E: (a) MCP protocol — boot mcp_server.mcp (build) + build_read_tier_server() (read) via mcp.shared.memory.create_connected_server_and_client_session (pass FastMCP directly); client list_tools + call_tool; assert read server == read allowlist and build-only tools absent + a deposit round-trips. (b) CLI E2E — drive `wiki remediate / revert-resolution / policy-edit / demand-cluster / commit-worker` against a real repo, assert on-disk + git state.
- T6 — inert-in-production property tests (the playbook hunt list as executable invariants): parametrized — every registered lint check + detector fires on a synthesized real signal; every gate dead-letters a real bad input; EVERY consumer's data source has a producer (the check that would've caught the cascade-depth sidecar); no apply-branch-less intent type.
- G1 — pre-merge gate script: full suite + the new tiers + eval floors (retrieval_eval.evaluate("fts").recall_at(10) ≥ 0.90; merge_map_eval no regressions; embedding_eval.evaluate_all() all pass). Wire into a local script + document in the playbook + CLAUDE.md.

GATE (a failing eval OR review HALTS): full suite green; eval-retrieval --compare fts recall@10 ≥ 0.90 (==0.926 baseline); scoped lints at baseline; all new tiers green; whole-branch opus review (READY) + security review (SHIP IT, the committer is a new privileged/destructive surface) + /session-review → ledger/BUILD.md updated → push branch + PR to main. Fold session-review findings back into the playbook (its Part C maintenance loop).

BACKLOG to file (triggered): if author_deposit needs richer page-type-specific rendering beyond the thin version, stage it. Confirm whether the committer daemon should be installed in launchd (like com.knowledge.watcher) or stay on-demand.
```

---

## VERIFIED INTERFACES (plan-time Verify-Before-Act — reuse, do not re-verify)

**No production queue drainer** (the gap D0 closes). `deposit()` (`ops/deposit.py:133`) → `IntentQueue.submit()` (`intent_queue.py:215`) → `submitted/`. `IntentQueue.claim(*, lease_ttl=120.0, now=None) -> Claim|None` (`intent_queue.py:222`, atomic os.replace → claimed/, advances fencing). `CommitGate.commit(authored: AuthoredIntent, fencing_token: int) -> OperationResult` (`commit_gate.py:298`, takes `file_lock("librarian-commit", timeout=30.0)`). Nothing connects claim→commit in prod. Watcher (`watcher.py`) only drains raw/inbox/; scheduler runs shell commands.

**Authoring gap (D0a, bounded).** `AuthoredIntent.writes: dict[rel,str]` is already-rendered content; `commit()` does NOT render. No prod fn builds AuthoredIntent from a deposit payload — only `commit_gate.py` internals + test fixtures. The test fixture `_authored_entity` in `tests/gateway/test_dedup_commit.py` encodes the deposit→page logic to mirror. Deposit payload fields: `page_type` (entity/concept/source/synthesis), `title`, `body` (markdown, agent-supplied), `aliases`, `domains`, `synthesizes`, `durable`, `volatile` (`ops/deposit.py:80-123`).

**DemandLedger (D1).** `cluster(self) -> list[GapCluster]` (`demand_ledger.py:175`; GapCluster: centroid_text/member_texts/recurrence_mass/triggered). `record_gap(self, text, *, caller=None) -> GapRecord` (`:162`). Trigger submits a `page_type=synthesis` + `demand_trigger=True` intent via submit() (`:323`, semantics="demand-trigger", drift-proof anchor_cid).

**CLI op registration (D1/D0 entries)** — mirror `remediate`: SUBCOMMANDS dict (`cli.py:117`), IMPLEMENTED set (`:195`), CLI_ONLY set (for non-MCP ops), build_parser add_parser (`:463`), main() dispatch (`:1661`), `_run_remediate` handler (`:2945`: `from gateway.ops.X import X; result = X(...); return _emit_result(result)`). `cli.main(argv: list[str]|None) -> int`. Scheduler: `wiki schedule add <name> "<cron>" "<command>"` → `.knowledge/schedule.yaml` (shell-command jobs only).

**MCP E2E (T4a).** `mcp` (build server, `mcp_server.py:37`), `build_read_tier_server()` (`:1444`). Use `from mcp.shared.memory import create_connected_server_and_client_session` — pass the FastMCP directly (it unwraps `._mcp_server`). `async with create_connected_server_and_client_session(mcp_server.mcp) as session: await session.list_tools(); await session.call_tool(name, args)`. Read allowlist = `tier.read_tier_tool_names()` (READ_OPS at `tier.py:30` + READ_AUX_TOOLS). `mcp.list_tools()` is async (`asyncio.run`).

**CLI E2E (T4b).** `cli.main(["subcmd", ...]) -> int`; pattern in `test_smoke.py:35`, `test_agents_cli.py:113`. On-disk/git assert pattern in `test_commit_gate.py:57-69` (the `repo` fixture: real git tmp repo, KNOWLEDGE_ROOT set, seeded commit).

**pytest tiering (M1).** `pyproject.toml:55-57` = `[tool.pytest.ini_options]` / `testpaths=["tests"]` / `addopts="-ra"`. Zero custom markers today. Add `markers=` + `-m` split.

**Concurrency pattern (T3).** threading.Event rendezvous — `test_bounded_acquire.py:13` (real fcntl, only paths.locks_dir redirected); commit-barrier-under-load `test_commit_gate.py:134`; concurrent-deposit `test_deposit.py:51` (overlapping spans → not serialized).

**Lifecycle entry points (T2).** deposit (`ops/deposit.py:133`); dedup/merge INSIDE commit (`_dedup_recheck` `:615`, `_retarget_to_canonical` `:664`; pure `dedup.adjudicate(identity, candidates, *, blocking_band, identity_threshold) -> Verdict` `dedup.py:61`); `retraction.cascade(retracted_source_ids: set, *, root=None) -> CascadeResult(flagged,terminated_on_cycle,depth)` (`retraction.py:221`); `retraction.acts_to_reopen(...)` (`:261`); `retraction.reverse_merge_plan(tombstone_rel, *, root) -> ReverseMergePlan` (`:332`); `revert_resolution(act_id, identity, *, queue=None)` (`ops/revert_resolution.py:26`); `remediate(*, root=None, dry_run=False, queue=None)` (`ops/remediate.py:99`). CommitGate dispatch routes on `payload["reversal_type"]` (`:339`) then `payload["op"]=="policy-edit"` (`:349`) else CAS pipeline.

**Eval gate (G1).** `retrieval_eval.evaluate(retriever="fts", *, goldens=None, k=10) -> EvalReport`; `EvalReport.recall_at(k) -> float`; `load_goldens(path=None)` (default `.knowledge/eval/retrieval/goldens.yaml`). `merge_map_eval(golden_path, *, root=None, adjudicator=None, blocking_band=0.15, identity_threshold=0.30) -> MergeMapResult(precision,recall,regressions)` (golden `.knowledge/eval/dedup/golden.yaml`). `embedding_eval.evaluate_all(encoder=None) -> dict[ns, NamespaceGateReport(passed)]` (goldens `.knowledge/eval/embedding/{section,entity,question}.yaml`). RECALL_FLOOR=0.90 (commit_gate.py:1129).

## State at handoff
- Branch `test/multi-agent-test-harness` cut off `main` @ `0a688378`; **nothing committed** on it. Working tree: only watcher-owned index.md/log.md modified + pre-existing untracked docs/260618 brief.
- main is fully merged + clean (PRs #31 Phase-5 build, #32 playbook, #33 BUILD.md §24 — all on origin/main).
- Decision ratified: Option 2 (build the REAL committer). Author scope = bounded (one author_deposit fn). Test scope = full 6 tiers.
- This contp + the playbook are the binding inputs. No tasks done yet.
