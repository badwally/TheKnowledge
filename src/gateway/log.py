"""log.md append-only writer per WIKI.md § 8.

Each entry begins with `## [<ISO-datetime>] <op> | k=v | ... | <summary>`,
making `grep '^## \\[' log.md | tail -N` a useful operator.
"""

from datetime import datetime, timezone

from gateway import paths

_HEADER = "# Knowledge Log\n\nAppend-only chronological record of ingests, queries, lints, NotebookLM operations, and migrations.\n"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _format_fields(fields: dict) -> str:
    if not fields:
        return ""
    return " | " + " | ".join(f"{k}={v}" for k, v in fields.items())


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

    path = paths.log_path()
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(_HEADER)

    with open(path, "a") as f:
        f.write("\n" + entry)

    return entry
