#!/usr/bin/env bash
# PreCompact hook: instructs the agent to write a session-state snapshot before
# context is compacted. Output goes to stdout and becomes additional context.
cat <<'INSTRUCTION'
BEFORE COMPACTION PROCEEDS: Write docs/session-state.md with the following sections filled in from your current working memory. Do not leave any section empty — write "none" if nothing applies.

---
## Open contracts
(invariants currently held in working memory but not yet committed — e.g., "validator must reject X before any write op can proceed")

## Files mid-edit
(paths + what is in flight — e.g., "src/gateway/foo.py: adding _bar() helper, not yet wired to callers")

## Decisions made this session
(one line each — architectural choices, approach selections, confirmed behaviors)

## Rejected approaches this session
(one line each with reason — helps the next session avoid relitigating)

## Next atomic step
(the single action to take on resume — specific enough that a cold session can execute it without context)
---

After writing the file, commit with message: 'session-state: precompact snapshot'
INSTRUCTION
