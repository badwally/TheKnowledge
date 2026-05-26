"""ONT-11: synthesizes_coverage lint check tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.lint.synthesizes_coverage import run


def _write_synthesis(
    kb_root: Path,
    slug: str,
    *,
    with_synthesizes: bool = False,
) -> Path:
    d = kb_root / "wiki" / "synthesis"
    d.mkdir(parents=True, exist_ok=True)
    front: dict = {
        "type": "synthesis",
        "slug": slug,
        "title": f"Synthesis {slug}",
        "domains": ["test"],
        "question": "What?",
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        "sources_count": 1,
    }
    if with_synthesizes:
        front["synthesizes"] = ["sources/web-abc123"]
    body = "## Synthesis\n\nContent.\n\n## Sources cited\n\n- [[sources/web-abc123]]\n"
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, body))
    return p


def test_missing_synthesizes_flagged(kb_root: Path) -> None:
    _write_synthesis(kb_root, "no-synth", with_synthesizes=False)
    findings = run()
    assert len(findings) == 1
    assert findings[0].check == "synthesizes-coverage"
    assert findings[0].severity == "warning"
    assert "no-synth" in findings[0].metadata.get("slug", "") or "no-synth" in findings[0].path


def test_present_synthesizes_not_flagged(kb_root: Path) -> None:
    _write_synthesis(kb_root, "has-synth", with_synthesizes=True)
    findings = run()
    assert findings == []


def test_empty_synthesis_dir_ok(kb_root: Path) -> None:
    findings = run()
    assert findings == []


def test_mixed_synthesis_pages(kb_root: Path) -> None:
    _write_synthesis(kb_root, "missing-a", with_synthesizes=False)
    _write_synthesis(kb_root, "missing-b", with_synthesizes=False)
    _write_synthesis(kb_root, "has-c", with_synthesizes=True)
    findings = run()
    assert len(findings) == 2
    slugs = {f.metadata.get("slug") for f in findings}
    assert "missing-a" in slugs
    assert "missing-b" in slugs
