"""AGT-14: wiki agent-log aggregation op + daily digest.

aggregate(since_hours) returns per-agent counts + top-5 event payloads.
build_digest_page(date_str) returns a draft wiki synthesis page.

The daily digest job writes a draft page to wiki/synthesis/ — it NEVER
auto-sends anything. The Message Send Gate is absolute.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

from gateway import events, paths


# Constant schedule entry definition for the daily 7am digest.
DIGEST_SCHEDULE_ENTRY: dict[str, Any] = {
    "name": "agent-digest",
    "cron": "0 7 * * *",
    "command": "wiki agent-log --since 24h",
    "enabled": True,
    "cooldown_seconds": 600,
}


def _parse_since_hours(since_hours: float) -> datetime:
    return datetime.now(timezone.utc) - timedelta(hours=since_hours)


def aggregate(*, since_hours: float) -> dict[str, dict]:
    """Aggregate event counts per agent within the last since_hours hours.

    Returns a dict keyed by agent name:
        {agent: {"count": int, "top_payloads": [dict, ...]}}
    """
    if since_hours <= 0:
        return {}

    since = _parse_since_hours(since_hours)
    all_events = events.list_events(since=since)

    by_agent: dict[str, list[dict]] = {}
    for ev in all_events:
        agent = str(ev.get("agent", "unknown"))
        by_agent.setdefault(agent, []).append(ev)

    result: dict[str, dict] = {}
    for agent, ev_list in by_agent.items():
        result[agent] = {
            "count": len(ev_list),
            "top_payloads": [e.get("payload", {}) for e in ev_list[:5]],
        }
    return result


def build_digest_page(*, date_str: str) -> str:
    """Build a draft wiki synthesis page for the agent digest."""
    data = aggregate(since_hours=24)
    lines = [
        "---",
        "type: synthesis",
        f"slug: agent-digest-{date_str}",
        f"title: Agent Activity Digest — {date_str}",
        "domains: []",
        "question: What did the automated agents do in the last 24 hours?",
        "draft: true",
        "---",
        "",
        "## Synthesis",
        "",
        f"Agent activity digest for {date_str} (last 24 hours).",
        "",
    ]

    if not data:
        lines.append("No agent events recorded in this window.")
    else:
        for agent, stats in sorted(data.items()):
            lines.append(f"**{agent}**: {stats['count']} event(s)")
            for payload in stats["top_payloads"]:
                if payload:
                    lines.append(f"  - {payload}")
        lines.append("")

    lines.extend([
        "## Sources cited",
        "",
        "_No source citations — this page summarizes internal agent activity._",
    ])

    return "\n".join(lines) + "\n"
