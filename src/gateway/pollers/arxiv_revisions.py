"""QUAL-7: arXiv revision monitor.

Checks each ingested arXiv source against the arXiv API. If the paper has
been revised (current version > stored version), stamps `arxiv_revised: true`,
`arxiv_current_version: N`, and `arxiv_versions_checked_at` in the raw source
frontmatter.

On first check: records the current version as the baseline. On subsequent
checks: flags if the version has increased since baseline.

Hard rule §6 allows frontmatter mutation by pipeline stages.

Cursor: .knowledge/pollers/arxiv-revisions/cursor.yaml
  checked:
    arxiv-2403.12345: {version: 2, checked_at: "2026-05-26T00:00:00Z"}
    ...
"""

from __future__ import annotations

import re
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Callable

import yaml

from gateway import frontmatter as fm, paths
from gateway.core import write_atomic
from gateway.pollers.base import Poller, PollerResult


_ARXIV_API_URL = "https://export.arxiv.org/api/query?id_list={arxiv_id}"
_REQUEST_TIMEOUT = 15
RECHECK_DAYS = 30

_ATOM_NS = "http://www.w3.org/2005/Atom"
_ARXIV_NS = "http://arxiv.org/schemas/atom"
_VERSION_RE = re.compile(r"v(\d+)$")


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _days_since(iso_str: str) -> float | None:
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return (datetime.now(timezone.utc) - dt).total_seconds() / 86400
    except Exception:
        return None


def _arxiv_id_from_source_id(source_id: str) -> str | None:
    if source_id.startswith("arxiv-"):
        return source_id[len("arxiv-"):].replace("-", ".")
    return None


def fetch_arxiv_atom(arxiv_id: str) -> str:
    """Fetch Atom feed for an arXiv ID. Raises urllib.error.URLError on failure."""
    url = _ARXIV_API_URL.format(arxiv_id=arxiv_id)
    with urllib.request.urlopen(url, timeout=_REQUEST_TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


def current_version(atom_text: str) -> int | None:
    """Parse the arXiv Atom feed to extract the current version number.

    Returns None on parse failure or missing version info.
    """
    try:
        root = ET.fromstring(atom_text)
    except ET.ParseError:
        return None

    # The arXiv API returns an <id> like https://arxiv.org/abs/2403.12345v3
    entry = root.find(f"{{{_ATOM_NS}}}entry")
    if entry is None:
        return None

    id_el = entry.find(f"{{{_ATOM_NS}}}id")
    if id_el is None or not id_el.text:
        return None

    m = _VERSION_RE.search(id_el.text)
    if m:
        return int(m.group(1))
    return None


class ArxivRevisionPoller(Poller):
    name = "arxiv-revisions"
    source_type = "arxiv"

    def __init__(
        self,
        *,
        fetch_fn: Callable[[str], str] = fetch_arxiv_atom,
    ) -> None:
        self._fetch = fetch_fn

    def run(self) -> PollerResult:
        raw_arxiv = paths.raw_dir() / "arxiv"
        if not raw_arxiv.exists():
            return PollerResult(success=True, summary="arxiv-revisions: no raw/arxiv/ sources")

        cursor = self._load_cursor()
        checked = 0
        skipped = 0
        revised_count = 0
        errors: list[str] = []

        for src in sorted(raw_arxiv.glob("*.md")):
            try:
                front, body = fm.parse(src.read_text())
            except Exception as e:
                errors.append(f"{src.name}: parse error: {e}")
                continue

            source_id = front.get("id", src.stem)
            arxiv_id = _arxiv_id_from_source_id(source_id)
            if not arxiv_id:
                skipped += 1
                continue

            # Skip recently checked
            entry = cursor.get(source_id) or {}
            last_checked = entry.get("checked_at") if isinstance(entry, dict) else None
            if last_checked:
                age = _days_since(last_checked)
                if age is not None and age < RECHECK_DAYS:
                    skipped += 1
                    continue

            try:
                atom_text = self._fetch(arxiv_id)
            except Exception as e:
                errors.append(f"{source_id}: fetch error: {e}")
                continue

            ver = current_version(atom_text)
            now = _now_iso()
            checked += 1

            if ver is None:
                cursor[source_id] = {"checked_at": now}
                continue

            baseline = entry.get("version") if isinstance(entry, dict) else None
            cursor[source_id] = {"version": ver, "checked_at": now}

            if baseline is None:
                # First check — record baseline; no revision flag yet
                if not front.get("arxiv_current_version"):
                    front["arxiv_current_version"] = ver
                    front["arxiv_versions_checked_at"] = now
                    write_atomic(src, fm.serialize(front, body))
            elif ver > baseline:
                # Version has increased since we last checked
                front["arxiv_revised"] = True
                front["arxiv_current_version"] = ver
                front["arxiv_versions_checked_at"] = now
                write_atomic(src, fm.serialize(front, body))
                revised_count += 1

        self._save_cursor(cursor)

        return PollerResult(
            success=True,
            fetched=checked,
            skipped=skipped,
            errors=errors,
            summary=(
                f"arxiv-revisions: {checked} checked, {skipped} skipped, "
                f"{revised_count} newly revised, {len(errors)} errors"
            ),
        )

    def _load_cursor(self) -> dict:
        p = self.cursor_path()
        if not p.is_file():
            return {}
        try:
            raw = yaml.safe_load(p.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                return raw.get("checked", {}) or {}
        except Exception:
            pass
        return {}

    def _save_cursor(self, checked: dict) -> None:
        p = self.cursor_path()
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(
            yaml.safe_dump({"checked": checked}, sort_keys=True, allow_unicode=True),
            encoding="utf-8",
        )
