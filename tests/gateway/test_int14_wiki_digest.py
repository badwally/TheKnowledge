"""INT-14: wiki digest — daily content brief tests."""

from __future__ import annotations

import yaml
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.ops.wiki_digest import build_wiki_digest


def _write_raw(kb_root: Path, source_type: str, source_id: str, *, ingested_at: str, title: str = "Test", domain: str = "test-domain") -> Path:
    d = kb_root / "raw" / source_type
    d.mkdir(parents=True, exist_ok=True)
    front = {"id": source_id, "type": source_type, "title": title, "domain": domain, "ingested_at": ingested_at}
    p = d / f"{source_id}.md"
    p.write_text(fm.serialize(front, "body"))
    return p


def _write_synthesis(kb_root: Path, slug: str, *, created_at: str, domain: str = "test-domain", draft: bool = False) -> Path:
    d = kb_root / "wiki" / "synthesis"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "synthesis",
        "slug": slug,
        "title": f"Synthesis {slug}",
        "domains": [domain],
        "question": "What?",
        "created_at": created_at,
        "last_updated": created_at,
        "sources_count": 0,
    }
    if draft:
        front["draft"] = True
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, "## Synthesis\n\nContent.\n\n## Sources cited\n\n-\n"))
    return p


def _iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def test_digest_shows_recent_source(kb_root: Path) -> None:
    now = datetime.now(timezone.utc)
    _write_raw(kb_root, "web", "web-abc123", ingested_at=_iso(now - timedelta(hours=1)), title="Recent Article")

    digest = build_wiki_digest(hours=24)

    assert "web-abc123" in digest
    assert "Recent Article" in digest
    assert "New sources" in digest


def test_digest_excludes_old_source(kb_root: Path) -> None:
    old = datetime.now(timezone.utc) - timedelta(hours=48)
    _write_raw(kb_root, "web", "web-old-source", ingested_at=_iso(old), title="Old Article")

    digest = build_wiki_digest(hours=24)

    assert "web-old-source" not in digest


def test_digest_shows_recent_synthesis(kb_root: Path) -> None:
    now = datetime.now(timezone.utc)
    _write_synthesis(kb_root, "my-synth", created_at=_iso(now - timedelta(hours=2)))

    digest = build_wiki_digest(hours=24)

    assert "my-synth" in digest
    assert "New synthesis" in digest


def test_digest_excludes_old_synthesis(kb_root: Path) -> None:
    old = datetime.now(timezone.utc) - timedelta(hours=48)
    _write_synthesis(kb_root, "old-synth", created_at=_iso(old))

    digest = build_wiki_digest(hours=24)

    assert "old-synth" not in digest


def test_digest_counts_stale_drafts(kb_root: Path) -> None:
    old = datetime.now(timezone.utc) - timedelta(days=10)
    p = _write_synthesis(kb_root, "stale-draft", created_at=_iso(old), draft=True)
    # backdate mtime so it's older than stale threshold
    import os
    old_ts = old.timestamp()
    os.utime(p, (old_ts, old_ts))

    digest = build_wiki_digest(hours=24, stale_days=7)

    assert "1 page" in digest or "stale draft" in digest.lower()
    assert "Stale drafts" in digest


def test_digest_shows_triage_queue(kb_root: Path) -> None:
    triage_dir = kb_root / ".knowledge" / "triage"
    triage_dir.mkdir(parents=True, exist_ok=True)
    (triage_dir / "web-pending.yaml").write_text(yaml.safe_dump({"source_id": "web-pending"}))

    digest = build_wiki_digest(hours=24)

    assert "1 source" in digest
    assert "Triage queue" in digest


def test_digest_empty_state(kb_root: Path) -> None:
    digest = build_wiki_digest(hours=24)

    assert "Wiki Digest" in digest
    assert "None" in digest or "_None._" in digest


def test_digest_none_label_when_empty(kb_root: Path) -> None:
    digest = build_wiki_digest(hours=24)
    assert "New sources" in digest
    assert "New synthesis" in digest
    assert "Stale drafts" in digest
    assert "Triage queue" in digest
