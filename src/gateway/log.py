"""log.md append-only writer per WIKI.md § 8.

Each entry begins with `## [<ISO-datetime>] <op> | k=v | ... | <summary>`,
making `grep '^## \\[' log.md | tail -N` a useful operator.

M47:
- `append()` now acquires `file_lock("log")` around the write so concurrent
  writers (CLI + watcher + research orchestrator + pollers + LLM telemetry)
  don't interleave inside multi-line entries. Closes ARCH-1 from the K1–K5
  review.
- New `log_llm_call(op, result, session_id=None)` helper writes one
  pipe-delimited line per LLM invocation for K5 cost/latency telemetry.
"""

from datetime import datetime, timezone

from gateway import paths
from gateway.llm.telemetry import CallResult
from gateway.locking import file_lock

_HEADER = "# Knowledge Log\n\nAppend-only chronological record of ingests, queries, lints, NotebookLM operations, and migrations.\n"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _format_fields(fields: dict) -> str:
    if not fields:
        return ""
    return " | " + " | ".join(f"{k}={v}" for k, v in fields.items())


def _write_entry(entry: str) -> None:
    """Append `entry` to log.md under the `log` lock.

    Creates log.md with the header if it does not yet exist. The single
    lock ensures concurrent callers (multi-process or multi-thread) see
    serial appends with no interleaved bytes.
    """
    path = paths.log_path()
    with file_lock("log"):
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(_HEADER)
        with open(path, "a") as f:
            f.write("\n" + entry)


def append(op: str, fields: dict | None = None, summary: str = "") -> str:
    """Write a log entry. Returns the entry text that was appended.

    Creates log.md with a header if it does not yet exist.
    """
    fields = fields or {}
    timestamp = _now_iso()
    header = f"## [{timestamp}] {op}{_format_fields(fields)}"

    parts = [header]
    if summary:
        parts.append("")
        parts.append(summary)
    parts.append("")  # ensures trailing newline
    entry = "\n".join(parts)

    _write_entry(entry)
    return entry


def log_llm_call(
    op: str,
    result: CallResult,
    *,
    session_id: str | None = None,
    extra: dict | None = None,
) -> str:
    """Write one structured log line for an LLM call (K5 telemetry).

    Single-line entry (no body, no trailing newline beyond `_write_entry`'s
    separator) so 7-day aggregation in `wiki status` can parse all
    `llm-call` lines with a single regex.

    `op` names the gateway operation that triggered the call (e.g.,
    ``filter``, ``plan_authorship``, ``vlm``, ``research_query_planner``).
    `session_id` is an optional correlation id (e.g., a research session)
    so multi-call runs can be reconstructed. `extra` injects additional
    key/value pairs (used for error cases: `error=timeout` etc.).
    """
    fields = {
        "op": op,
        "model": result.model,
        "in_tokens": result.input_tokens,
        "out_tokens": result.output_tokens,
        "cache_read": result.cache_read_tokens,
        "cache_creation": result.cache_creation_tokens,
        "duration_ms": result.duration_ms,
        "cost_usd": f"{result.total_cost_usd:.6f}",
    }
    if session_id:
        fields["session"] = session_id
    if extra:
        fields.update(extra)

    timestamp = _now_iso()
    entry = f"## [{timestamp}] llm-call{_format_fields(fields)}\n"
    _write_entry(entry)
    return entry
