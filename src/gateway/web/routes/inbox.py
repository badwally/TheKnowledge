"""TOOL-11: /api/inbox — inbox and failed-ingest triage view."""

from __future__ import annotations

import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, HTTPException

from gateway import frontmatter as fm, paths
from gateway.web.schemas import InboxDetailResponse, InboxFailedItem, InboxPendingItem, RetryResponse


router = APIRouter(prefix="/api/inbox", tags=["inbox"])

_FAILED_PREFIX_RE = re.compile(r"^(\d{8}T\d{6}Z)-(.+)$")


def _failed_dir() -> Path:
    return paths.raw_dir() / "inbox" / "_failed"


def _inbox_dir() -> Path:
    return paths.raw_dir() / "inbox"


def _sniff(path: Path) -> tuple[str | None, str | None, str | None]:
    """Return (source_type, title, url) from frontmatter if parseable."""
    try:
        text = path.read_text(errors="replace")
        front, _ = fm.parse(text)
        source_type = str(front["type"]) if front.get("type") else None
        title = str(front["title"]) if front.get("title") else None
        url = str(front["url"]) if front.get("url") else None
        return source_type, title, url
    except Exception:
        return None, None, None


def _iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


@router.get("", response_model=InboxDetailResponse)
def get_inbox() -> InboxDetailResponse:
    inbox = _inbox_dir()
    failed = _failed_dir()

    pending: list[InboxPendingItem] = []
    if inbox.exists():
        for p in sorted(inbox.iterdir()):
            if not p.is_file() or p.suffix != ".md":
                continue
            stat = p.stat()
            stype, stitle, surl = _sniff(p)
            pending.append(InboxPendingItem(
                filename=p.name,
                size_bytes=stat.st_size,
                modified_at=_iso(stat.st_mtime),
                sniffed_type=stype,
                sniffed_title=stitle,
                sniffed_url=surl,
            ))

    failed_items: list[InboxFailedItem] = []
    if failed.exists():
        for p in sorted(failed.iterdir(), reverse=True):
            if not p.is_file() or not p.suffix == ".md":
                continue
            m = _FAILED_PREFIX_RE.match(p.stem)
            if m:
                failed_at_raw, original_stem = m.group(1), m.group(2)
                try:
                    failed_at = datetime.strptime(failed_at_raw, "%Y%m%dT%H%M%SZ").replace(
                        tzinfo=timezone.utc
                    ).isoformat()
                except ValueError:
                    failed_at = failed_at_raw
                original_name = original_stem + p.suffix
            else:
                failed_at = _iso(p.stat().st_mtime)
                original_name = p.name

            reason_path = p.with_suffix(p.suffix + ".reason.txt")
            reason = reason_path.read_text().strip() if reason_path.exists() else ""

            failed_items.append(InboxFailedItem(
                filename=p.name,
                original_name=original_name,
                failed_at=failed_at,
                reason=reason,
                size_bytes=p.stat().st_size,
            ))

    return InboxDetailResponse(pending=pending, failed=failed_items)


@router.post("/retry/{filename}", response_model=RetryResponse)
def retry_failed(filename: str) -> RetryResponse:
    """Move a failed file back to inbox/ for re-processing."""
    failed = _failed_dir()
    inbox = _inbox_dir()

    src = failed / filename
    if not src.exists():
        raise HTTPException(status_code=404, detail=f"not found: {filename}")
    if not src.is_file() or src.suffix != ".md":
        raise HTTPException(status_code=400, detail="only .md files can be retried")

    # Derive original name by stripping timestamp prefix
    m = _FAILED_PREFIX_RE.match(src.stem)
    original_name = (m.group(2) if m else src.stem) + src.suffix

    inbox.mkdir(parents=True, exist_ok=True)
    dest = inbox / original_name
    if dest.exists():
        raise HTTPException(status_code=409, detail=f"already pending: {original_name}")

    try:
        shutil.move(str(src), str(dest))
        reason_file = src.with_suffix(src.suffix + ".reason.txt")
        if reason_file.exists():
            reason_file.unlink(missing_ok=True)
    except OSError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return RetryResponse(ok=True, message=f"moved to inbox: {original_name}")
