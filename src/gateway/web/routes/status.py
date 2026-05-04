"""Read-only status / log / lint endpoints."""

from __future__ import annotations

import re

from fastapi import APIRouter, Query

from gateway import paths
from gateway.ops.lint import lint as lint_op
from gateway.watcher import watcher_state
from gateway.web.schemas import (
    InboxState,
    LintResponse,
    LogEntry,
    StatusResponse,
    WatcherState,
)


router = APIRouter(prefix="/api", tags=["status"])


_LOG_HEADER_RE = re.compile(
    r"^## \[(?P<ts>[^\]]+)\] (?P<op>[a-z0-9-]+)(?: \| (?P<fields>.*))?$"
)


@router.get("/status", response_model=StatusResponse)
def get_status() -> StatusResponse:
    state = watcher_state()
    return StatusResponse(
        watcher=WatcherState(
            running=state["running"],
            pid=state["pid"],
            last_heartbeat=state["last_heartbeat"],
        ),
        inbox=InboxState(
            pending=state["inbox_pending"],
            failed=state["inbox_failed"],
        ),
        drafts=_count_drafts(),
        sources=_count_sources(),
        domains=_count_domains(),
    )


@router.get("/log", response_model=list[LogEntry])
def get_log(lines: int = Query(50, ge=1, le=500)) -> list[LogEntry]:
    log_path = paths.log_path()
    if not log_path.exists():
        return []
    text = log_path.read_text()
    entries = _parse_log_entries(text)
    return list(reversed(entries[-lines:]))


@router.get("/lint", response_model=LintResponse)
def get_lint(scope: str | None = Query(None)) -> LintResponse:
    result = lint_op(scope=scope)
    return LintResponse(
        summary=result.summary,
        report_path=str(result.paths_touched[0]) if result.paths_touched else None,
        issues=[],
    )


def _count_drafts() -> int:
    wiki = paths.wiki_dir()
    if not wiki.exists():
        return 0
    count = 0
    for sub in ("entities", "concepts", "synthesis", "mocs"):
        d = wiki / sub
        if not d.exists():
            continue
        for path in d.glob("*.md"):
            try:
                if "draft: true" in path.read_text():
                    count += 1
            except OSError:
                continue
    return count


def _count_sources() -> int:
    raw = paths.raw_dir()
    if not raw.exists():
        return 0
    count = 0
    for source_type in paths.SOURCE_TYPES:
        d = raw / source_type
        if d.exists():
            count += sum(1 for _ in d.glob("*.md"))
    return count


def _count_domains() -> int:
    policies_dir = paths.policies_dir()
    if not policies_dir.exists():
        return 0
    return sum(
        1 for d in policies_dir.iterdir()
        if d.is_dir() and (d / "policy.yaml").exists()
    )


def _parse_log_entries(text: str) -> list[LogEntry]:
    entries: list[LogEntry] = []
    current: LogEntry | None = None
    summary_lines: list[str] = []
    for line in text.splitlines():
        m = _LOG_HEADER_RE.match(line)
        if m:
            if current is not None:
                current.summary = "\n".join(summary_lines).strip()
                entries.append(current)
            fields_dict: dict[str, str] = {}
            raw_fields = m.group("fields") or ""
            for pair in raw_fields.split(" | "):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    fields_dict[k.strip()] = v.strip()
            current = LogEntry(
                timestamp=m.group("ts"),
                op=m.group("op"),
                fields=fields_dict,
                summary="",
            )
            summary_lines = []
        elif current is not None:
            summary_lines.append(line)
    if current is not None:
        current.summary = "\n".join(summary_lines).strip()
        entries.append(current)
    return entries
