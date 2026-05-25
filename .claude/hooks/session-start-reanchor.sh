#!/usr/bin/env bash
# SessionStart hook: instructs the agent to re-anchor on resume if a recent
# session-state snapshot exists. Output goes to stdout and becomes context.
cat <<'INSTRUCTION'
If docs/session-state.md exists and its mtime is newer than this session's start, re-read it before any plan-or-write action. Verify each ## Open contract and ## File mid-edit against the working tree. Flag any disagreement to the user before proceeding.
INSTRUCTION
