# Backlog: install the intent-queue committer as an autonomous daemon

**Status:** deferred (decided 2026-06-19, committer-test-harness build).
**Decision:** the production committer (`wiki commit-worker`, built in the committer-test-harness phase) ships **on-demand only** — `--once` (drain-to-empty) and `--loop` (foreground polling). No autonomous background install.

## Why deferred (not built now)

The committer authors and **commits arbitrary deposit bodies into git, unattended** — a different risk class than `com.knowledge.watcher`, which only appends `log.md` and writes untracked `raw/` files. Two blockers:

1. **Shared working tree.** This repo's tree is shared with concurrent sessions that branch-switch (see memory `feedback_verify_branch_before_commit_shared_tree`). An always-on committer would commit to whatever branch is checked out → wiki commits could land on the wrong branch with no human in the loop. The watcher is immune (untracked writes); the committer is not.
2. **Brand-new privileged surface.** Running unattended commit automation before the code has been exercised amplifies the blast radius of any bug (poison-loop, runaway commits, slug path-traversal). Let it bake under on-demand invocation first.
3. **The committer autonomously applies privileged ops on drain** (added 2026-06-19, D0-reopen): it now routes `policy-edit` + `reversal_type` (`depath`, `contradiction-resolution`) intents to the gate's apply dispatch. Security re-check MEDIUM-2: privilege is enforced only at ENQUEUE (server-sourced principal + allowlist, fail-closed), NOT re-checked at apply — consistent with the documented Phase-5 model (FS write to `.knowledge/intents/` already implies shell access; the change-control gate still fail-closes every policy apply). For an ON-DEMAND operator-run worker this is fine. But an UNATTENDED daemon draining policy-edits/reversals autonomously raises the stakes of the enqueue-only boundary — so "security clears the committer surface" in the revival trigger below MUST specifically cover autonomous privileged-op apply, not just the deposit path.

## The two background options when revived

- **Option A — launchd daemon** (mirrors `com.knowledge.watcher`): always-on polling drain. Closes the async deposit→commit contract fully (autonomous receipt polled via `intent_status`). Highest autonomy, highest standing risk.
- **Option B (preferred eventual answer) — scheduler cron entry**: `wiki schedule add committer "<cron>" "wiki commit-worker --once"`. Bounded periodic drain, **no standing process**, no permanent branch hazard from a long-lived loop. Still drains the queue without a human, but only in bounded bursts.

Option B is likely the right shape — it gets autonomous drainage without a persistent unattended git-committer. Prefer it over Option A when this is revived.

## Revival trigger (both must hold)

1. The committer surface has **cleared a security review** (path-traversal in slug/rel-path, frontmatter body injection, unbounded-loop resource use — the items flagged in the D0 security review).
2. A **dedicated-checkout or branch-pin story** exists so an unattended `commit-worker` cannot land commits on whatever branch a concurrent session left checked out (e.g. the daemon operates on its own worktree pinned to `main`, or refuses to commit unless on an expected branch).

Until both hold, on-demand `wiki commit-worker` is the only sanctioned invocation.
