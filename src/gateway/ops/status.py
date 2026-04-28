"""`wiki status` — show watcher state, recent activity, pending queues.

M4: watcher state + last few log entries + inbox depth.
M5+: extends with NotebookLM sync state, lint summary, etc.
"""

from __future__ import annotations

from gateway import paths
from gateway.core import OperationResult
from gateway.watcher import watcher_state


_RECENT_LOG_ENTRIES = 5


def status() -> OperationResult:
    state = watcher_state()
    lines: list[str] = []

    # Watcher
    if state["running"]:
        lines.append(
            f"Watcher: running (pid={state['pid']}, last heartbeat {state['last_heartbeat'] or 'never'})"
        )
    else:
        lines.append("Watcher: not running")

    # Inbox
    lines.append(
        f"Inbox: {state['inbox_pending']} pending · {state['inbox_failed']} failed"
    )

    # Recent activity from log.md
    log_path = paths.log_path()
    if log_path.exists():
        recent = _tail_log_entries(log_path.read_text(), _RECENT_LOG_ENTRIES)
        if recent:
            lines.append("Recent activity:")
            lines.extend(f"  {line}" for line in recent)
        else:
            lines.append("Recent activity: (no entries yet)")
    else:
        lines.append("Recent activity: (log.md not yet created)")

    return OperationResult(success=True, summary="\n".join(lines))


def _tail_log_entries(log_text: str, n: int) -> list[str]:
    """Return the last `n` heading lines from log.md (cheap proxy for entries)."""
    headings = [
        ln.strip()
        for ln in log_text.splitlines()
        if ln.startswith("## [")
    ]
    return headings[-n:]
