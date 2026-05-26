"""QUAL-3: contradiction surfacing and resolution ops.

list_contradictions() — list open contradiction pages.
resolve_contradiction() — update status/resolution, set contested on sources.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from gateway import frontmatter as fm, paths
from gateway.core import OperationResult, write_atomic


def _contradictions_dir() -> Path:
    return paths.wiki_dir() / "contradictions"


def _load_contradiction(slug: str) -> tuple[Path, dict, str] | None:
    page_path = _contradictions_dir() / f"{slug}.md"
    if not page_path.exists():
        return None
    text = page_path.read_text()
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    try:
        front = yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return None
    body = text[end + 3:]
    return page_path, front, body


def list_contradictions(
    *,
    severity: str | None,
    status: str,
) -> OperationResult:
    """Return a summary of contradiction pages matching the filters."""
    cdir = _contradictions_dir()
    if not cdir.exists():
        return OperationResult(success=True, summary="No contradiction pages found.")

    found: list[str] = []
    for md_file in sorted(cdir.glob("*.md")):
        text = md_file.read_text()
        if not text.startswith("---"):
            continue
        end = text.find("---", 3)
        if end == -1:
            continue
        try:
            front = yaml.safe_load(text[3:end]) or {}
        except yaml.YAMLError:
            continue

        page_status = str(front.get("status", ""))
        page_severity = str(front.get("severity", ""))
        slug = str(front.get("slug", md_file.stem))

        if page_status != status:
            continue
        if severity is not None and page_severity != severity:
            continue
        found.append(f"  {slug} (severity={page_severity})")

    if not found:
        return OperationResult(success=True, summary=f"No {status} contradiction pages found.")
    summary = f"{len(found)} {status} contradiction(s):\n" + "\n".join(found)
    return OperationResult(success=True, summary=summary)


_WIKILINK_RE = re.compile(r"\[\[sources/([^\]|]+)")


def _source_ids_from_parties(parties: list) -> list[str]:
    ids: list[str] = []
    for p in parties:
        m = _WIKILINK_RE.search(str(p))
        if m:
            ids.append(m.group(1).strip())
    return ids


def _count_unresolved_for_source(source_id: str) -> int:
    cdir = _contradictions_dir()
    if not cdir.exists():
        return 0
    pattern = f"sources/{source_id}"
    count = 0
    for md_file in cdir.glob("*.md"):
        text = md_file.read_text()
        if not text.startswith("---"):
            continue
        end = text.find("---", 3)
        if end == -1:
            continue
        try:
            front = yaml.safe_load(text[3:end]) or {}
        except yaml.YAMLError:
            continue
        status = str(front.get("status", ""))
        if status in ("resolved", "wontfix"):
            continue
        parties = front.get("parties", []) or []
        if any(pattern in str(p) for p in parties):
            count += 1
    return count


def _set_contested(source_id: str) -> None:
    source_path = paths.wiki_dir() / "sources" / f"{source_id}.md"
    if not source_path.exists():
        return
    text = source_path.read_text()
    if not text.startswith("---"):
        return
    end = text.find("---", 3)
    if end == -1:
        return
    front_text = text[3:end]
    rest = text[end + 3:]
    if "contested:" in front_text:
        front_text = re.sub(r"contested:\s*\S+", "contested: true", front_text)
    else:
        front_text = front_text.rstrip() + "\ncontested: true\n"
    write_atomic(source_path, "---" + front_text + "---" + rest)


def resolve_contradiction(
    slug: str,
    *,
    status: str,
    note: str,
) -> OperationResult:
    """Resolve a contradiction page: update status and resolution note.

    Returns an error result if the slug does not exist or is already resolved.
    """
    loaded = _load_contradiction(slug)
    if loaded is None:
        return OperationResult(
            success=False,
            summary=f"contradiction {slug!r} not found",
            errors=[f"not found: wiki/contradictions/{slug}.md"],
        )

    page_path, front, body = loaded
    current_status = str(front.get("status", ""))
    if current_status in ("resolved", "wontfix"):
        return OperationResult(
            success=False,
            summary=f"contradiction {slug!r} is already {current_status}",
            errors=[f"already {current_status}"],
        )

    parties = front.get("parties", []) or []

    # Update frontmatter
    front["status"] = status
    front["resolution"] = note

    new_front = yaml.safe_dump(front, default_flow_style=False, allow_unicode=True)
    write_atomic(page_path, "---\n" + new_front + "---" + body)

    # Set contested on source pages with ≥2 remaining unresolved contradictions
    for source_id in _source_ids_from_parties(parties):
        unresolved = _count_unresolved_for_source(source_id)
        if unresolved >= 2:
            _set_contested(source_id)

    return OperationResult(success=True, summary=f"resolved {slug!r} as {status!r}")
