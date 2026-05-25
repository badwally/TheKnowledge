"""`wiki status` — show watcher state, recent activity, pending queues.

M4: watcher state + last few log entries + inbox depth.
M5+: extends with NotebookLM sync state, lint summary, etc.
M47 (K5): adds a 7-day LLM usage block aggregated from `llm-call` log lines.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import re

import yaml

from gateway import log, paths
from gateway.core import OperationResult
from gateway.costs import estimate_cost
from gateway.evaluate.persistence import eval_dir_for, read_trend
from gateway.ops.finetune import trigger_states_all
from gateway.watcher import watcher_state


_RECENT_LOG_ENTRIES = 5
_LLM_USAGE_WINDOW_DAYS = 7

# Match the structured `llm-call` line shape:
#   ## [<ISO-Z>] llm-call | op=<o> | model=<m> | in_tokens=<n> | out_tokens=<n> | cache_read=<n> | cache_creation=<n> | duration_ms=<n> | cost_usd=<f> ...
_LLM_LINE_RE = re.compile(r"^## \[(?P<ts>[^\]]+)\] llm-call \| (?P<fields>.+)$")


@dataclass
class _UsageBucket:
    calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    cache_creation_tokens: int = 0
    duration_ms: int = 0
    reported_cost_usd: float = 0.0  # cost_usd field straight from the log line


def status(*, with_cost: bool = False) -> OperationResult:
    """Render the status summary.

    ``with_cost``: when True, include a USD-cost column in the LLM-usage
    block. Off by default — tokens are factual, USD is a recomputed
    estimate from ``gateway.costs.PRICING`` and may diverge from the
    actual Max-plan / API billing.
    """
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
    log_text = log_path.read_text() if log_path.exists() else ""

    if log_text:
        recent = _tail_log_entries(log_text, _RECENT_LOG_ENTRIES)
        if recent:
            lines.append("Recent activity:")
            lines.extend(f"  {line}" for line in recent)
        else:
            lines.append("Recent activity: (no entries yet)")
    else:
        lines.append("Recent activity: (log.md not yet created)")

    # QUAL-5: fine-tune readiness block
    ft_block = _finetune_readiness_block()
    if ft_block:
        lines.append(ft_block)

    # M50: evaluation scores block
    eval_block = _evaluation_status_block()
    lines.append(eval_block)

    # K5: LLM usage block
    usage_block = _render_llm_usage_block(
        log_text, window_days=_LLM_USAGE_WINDOW_DAYS, with_cost=with_cost
    )
    if usage_block:
        lines.append(usage_block)

    return OperationResult(success=True, summary="\n".join(lines))


_FINETUNE_MILESTONE_PATH_NAME = "finetune_milestones.yaml"
_FINETUNE_MILESTONE_PCT = 80


def _finetune_milestone_path() -> "Path":
    from pathlib import Path
    return paths.knowledge_internal() / _FINETUNE_MILESTONE_PATH_NAME


def _load_finetune_milestones() -> set[str]:
    """Load the set of domains already logged for the 80% milestone."""
    p = _finetune_milestone_path()
    if not p.exists():
        return set()
    try:
        data = yaml.safe_load(p.read_text()) or {}
        return set(data.get("logged_domains", []))
    except (yaml.YAMLError, OSError):
        return set()


def _save_finetune_milestones(logged: set[str]) -> None:
    p = _finetune_milestone_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(yaml.safe_dump({"logged_domains": sorted(logged)}))


def _finetune_readiness_block() -> str:
    """Render per-domain fine-tune readiness for `wiki status`.

    Shows each domain's example-bank count toward the 500-decision threshold.
    Logs a one-shot entry when a domain crosses 80%. Returns empty string when
    no domains have policies.
    """
    states = trigger_states_all()
    if not states:
        return ""

    logged_milestones = _load_finetune_milestones()
    newly_logged: set[str] = set()

    rows: list[str] = []
    for ts in states:
        pct = int(min(100, ts.count / ts.threshold * 100))
        rows.append(f"  - {ts.domain}: {ts.count}/{ts.threshold} ({pct}%)")
        if pct >= _FINETUNE_MILESTONE_PCT and ts.domain not in logged_milestones:
            log.append(
                "finetune-milestone",
                fields={
                    "domain": ts.domain,
                    "count": ts.count,
                    "threshold": ts.threshold,
                    "pct": pct,
                },
                summary=f"{ts.domain} reached {pct}% fine-tune readiness ({ts.count}/{ts.threshold})",
            )
            newly_logged.add(ts.domain)

    if newly_logged:
        _save_finetune_milestones(logged_milestones | newly_logged)

    header = "Fine-tune readiness (decisions toward 500-example threshold):"
    return "\n".join([header] + rows)


def _evaluation_status_block() -> str:
    """Render the M50 evaluation scores section for `wiki status`.

    Lists the most recent mean_score per domain that has been evaluated,
    plus the delta versus the prior run.
    """
    eval_base = paths.knowledge_internal() / "eval"
    if not eval_base.exists():
        return "Evaluation scores: none yet (run `wiki evaluate --scaffold <domain>` to start)"

    domains = sorted(d.name for d in eval_base.iterdir() if d.is_dir())
    if not domains:
        return "Evaluation scores: none yet (run `wiki evaluate --scaffold <domain>` to start)"

    rows: list[str] = []
    for domain in domains:
        trend = read_trend(domain)
        if not trend:
            continue
        latest_score = float(trend[-1]["mean_score"])
        if len(trend) >= 2:
            prior_score = float(trend[-2]["mean_score"])
            delta = latest_score - prior_score
            sign = "+" if delta >= 0 else ""
            delta_str = f"{sign}{delta:.2f}"
        else:
            delta_str = "initial"
        rows.append(f"  - {domain}: mean={latest_score:.3f}  (Δ {delta_str})")

    if not rows:
        return "Evaluation scores: none yet (run `wiki evaluate --scaffold <domain>` to start)"

    header = "Evaluation scores (last run per domain):"
    return "\n".join([header] + rows)


def _tail_log_entries(log_text: str, n: int) -> list[str]:
    """Return the last `n` heading lines from log.md (cheap proxy for entries)."""
    headings = [
        ln.strip()
        for ln in log_text.splitlines()
        if ln.startswith("## [")
    ]
    return headings[-n:]


def _aggregate_llm_usage(
    log_text: str, *, window_days: int, now: datetime | None = None
) -> dict[str, _UsageBucket]:
    """Parse `llm-call` lines from log.md and aggregate into per-op buckets.

    Returns ``{op: UsageBucket}`` for calls whose timestamp falls within
    the last ``window_days`` days. ``now`` is injectable for tests.
    """
    if now is None:
        now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=window_days)

    buckets: dict[str, _UsageBucket] = {}
    for line in log_text.splitlines():
        m = _LLM_LINE_RE.match(line)
        if not m:
            continue
        ts_str = m.group("ts")
        try:
            ts = datetime.strptime(ts_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        except ValueError:
            continue
        if ts < cutoff:
            continue

        fields_text = m.group("fields")
        fields: dict[str, str] = {}
        # Format guarantees " | " separators with no embedded `|` in any value.
        for chunk in fields_text.split(" | "):
            if "=" not in chunk:
                continue
            k, _, v = chunk.partition("=")
            fields[k.strip()] = v.strip()

        op = fields.get("op", "unknown")
        bucket = buckets.setdefault(op, _UsageBucket())
        bucket.calls += 1
        bucket.input_tokens += _safe_int(fields.get("in_tokens"))
        bucket.output_tokens += _safe_int(fields.get("out_tokens"))
        bucket.cache_read_tokens += _safe_int(fields.get("cache_read"))
        bucket.cache_creation_tokens += _safe_int(fields.get("cache_creation"))
        bucket.duration_ms += _safe_int(fields.get("duration_ms"))
        bucket.reported_cost_usd += _safe_float(fields.get("cost_usd"))

    return buckets


def _render_llm_usage_block(
    log_text: str, *, window_days: int, with_cost: bool
) -> str:
    """Format the K5 LLM-usage section for `wiki status`.

    Returns an empty string if no `llm-call` entries fall within the window.
    """
    buckets = _aggregate_llm_usage(log_text, window_days=window_days)
    if not buckets:
        return ""

    total_calls = sum(b.calls for b in buckets.values())
    total_in = sum(b.input_tokens for b in buckets.values())
    total_out = sum(b.output_tokens for b in buckets.values())
    total_cr = sum(b.cache_read_tokens for b in buckets.values())
    total_cc = sum(b.cache_creation_tokens for b in buckets.values())
    total_reported_cost = sum(b.reported_cost_usd for b in buckets.values())

    header = f"LLM usage (last {window_days} days): {total_calls} calls"
    summary = (
        f"  total: in={total_in:,} · out={total_out:,} · "
        f"cache_read={total_cr:,} · cache_creation={total_cc:,}"
    )
    rows = [header, summary]

    by_op = " · ".join(f"{op}={b.calls}" for op, b in sorted(buckets.items()))
    rows.append(f"  by op: {by_op}")

    if with_cost:
        rows.append(f"  reported cost (from claude envelope): ${total_reported_cost:.4f}")
        # Also offer the recomputed estimate from gateway/costs.py — useful
        # for quick sanity-checks and for old log lines that pre-date the
        # cost_usd field on the line shape. Per-model isn't tracked yet
        # because the log line carries `op` and `model` but the aggregator
        # buckets by op only; expanding the bucket key to (op, model) is a
        # follow-up if needed.
        rows.append(
            f"  (USD estimate is approximate; authoritative billing lives with Anthropic)"
        )

    return "\n".join(rows)


def _safe_int(s: str | None) -> int:
    if not s:
        return 0
    try:
        return int(s)
    except ValueError:
        return 0


def _safe_float(s: str | None) -> float:
    if not s:
        return 0.0
    try:
        return float(s)
    except ValueError:
        return 0.0
