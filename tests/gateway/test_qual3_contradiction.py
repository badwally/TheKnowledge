"""Tests for QUAL-3: contradiction surfacing and resolution workflow."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway.ops import contradiction as cont_ops


# ── helpers ───────────────────────────────────────────────────────────────────

def _write_contradiction(root: Path, slug: str, severity: str, status: str, parties: list[str] | None = None) -> None:
    pages_dir = root / "wiki" / "contradictions"
    pages_dir.mkdir(parents=True, exist_ok=True)
    if parties is None:
        parties = ["[[sources/web-2026-01-01-abc123]]", "[[sources/arxiv-2024.12345]]"]
    import yaml
    front = {
        "type": "contradiction",
        "slug": slug,
        "parties": parties,
        "severity": severity,
        "status": status,
        "resolution": "",
    }
    front_text = yaml.safe_dump(front, default_flow_style=False, allow_unicode=True)
    content = f"---\n{front_text}---\n\n## Summary\n\nContradiction between source A and source B.\n"
    (pages_dir / f"{slug}.md").write_text(content)


def _write_source_page(root: Path, source_id: str, *, contested: bool = False) -> None:
    sources_dir = root / "wiki" / "sources"
    sources_dir.mkdir(parents=True, exist_ok=True)
    import yaml
    front: dict = {
        "type": "source",
        "source_id": source_id,
        "source_type": "web",
        "title": "Test Source",
        "ingested_at": "2026-01-01T00:00:00Z",
    }
    if contested:
        front["contested"] = True
    front_text = yaml.safe_dump(front, default_flow_style=False, allow_unicode=True)
    content = (
        f"---\n{front_text}---\n\n"
        "## Summary\n\nA test source.\n\n"
        "## Key claims\n\nSome claims here.\n\n"
        "## Cross-references\n\nNone.\n"
    )
    (sources_dir / f"{source_id}.md").write_text(content)


# ── list_contradictions ───────────────────────────────────────────────────────

def test_list_returns_open_by_default(kb_root: Path) -> None:
    _write_contradiction(kb_root, "issue-a", "major", "open")
    _write_contradiction(kb_root, "issue-b", "minor", "resolved")
    result = cont_ops.list_contradictions(severity=None, status="open")
    assert result.success
    assert "issue-a" in result.summary
    assert "issue-b" not in result.summary


def test_list_severity_filter_major(kb_root: Path) -> None:
    _write_contradiction(kb_root, "big-issue", "major", "open")
    _write_contradiction(kb_root, "small-issue", "minor", "open")
    result = cont_ops.list_contradictions(severity="major", status="open")
    assert "big-issue" in result.summary
    assert "small-issue" not in result.summary


def test_list_empty_returns_clean_output(kb_root: Path) -> None:
    result = cont_ops.list_contradictions(severity=None, status="open")
    assert result.success


def test_list_no_contradictions_dir_returns_ok(kb_root: Path) -> None:
    result = cont_ops.list_contradictions(severity=None, status="open")
    assert result.success


# ── resolve_contradiction ─────────────────────────────────────────────────────

def test_resolve_updates_status_and_resolution(kb_root: Path) -> None:
    _write_contradiction(kb_root, "dose-ceiling", "major", "open")
    result = cont_ops.resolve_contradiction("dose-ceiling", status="resolved", note="Study A is methodologically superior.")
    assert result.success
    page_path = kb_root / "wiki" / "contradictions" / "dose-ceiling.md"
    text = page_path.read_text()
    assert "status: resolved" in text
    assert "Study A is methodologically superior." in text


def test_resolve_wontfix_status(kb_root: Path) -> None:
    _write_contradiction(kb_root, "minor-issue", "minor", "open")
    result = cont_ops.resolve_contradiction("minor-issue", status="wontfix", note="Not actionable.")
    assert result.success
    text = (kb_root / "wiki" / "contradictions" / "minor-issue.md").read_text()
    assert "status: wontfix" in text


def test_resolve_already_resolved_returns_error(kb_root: Path) -> None:
    _write_contradiction(kb_root, "done-issue", "major", "resolved")
    result = cont_ops.resolve_contradiction("done-issue", status="resolved", note="")
    assert not result.success


def test_resolve_missing_slug_returns_error(kb_root: Path) -> None:
    result = cont_ops.resolve_contradiction("nonexistent", status="resolved", note="")
    assert not result.success


# ── contested flag ────────────────────────────────────────────────────────────

def test_resolve_sets_contested_on_source_with_2_unresolved(kb_root: Path) -> None:
    src_id = "web-2026-01-01-abc123"
    parties = [f"[[sources/{src_id}]]", "[[sources/arxiv-2024.12345]]"]
    _write_source_page(kb_root, src_id)
    _write_contradiction(kb_root, "issue-1", "major", "open", parties=parties)
    _write_contradiction(kb_root, "issue-2", "major", "open", parties=parties)
    _write_contradiction(kb_root, "issue-3", "major", "open", parties=parties)
    # Resolve one — the source still has 2 unresolved → contested
    cont_ops.resolve_contradiction("issue-1", status="resolved", note="done")
    source_text = (kb_root / "wiki" / "sources" / f"{src_id}.md").read_text()
    assert "contested: true" in source_text


def test_resolve_does_not_set_contested_with_only_1_unresolved(kb_root: Path) -> None:
    src_id = "web-2026-01-01-xyz999"
    parties = [f"[[sources/{src_id}]]", "[[sources/arxiv-2024.12345]]"]
    _write_source_page(kb_root, src_id)
    _write_contradiction(kb_root, "solo-issue", "major", "open", parties=parties)
    cont_ops.resolve_contradiction("solo-issue", status="resolved", note="done")
    source_text = (kb_root / "wiki" / "sources" / f"{src_id}.md").read_text()
    assert "contested: true" not in source_text


# ── wiki status integration ───────────────────────────────────────────────────

def test_status_includes_contradiction_summary(kb_root: Path) -> None:
    _write_contradiction(kb_root, "open-major", "major", "open")
    _write_contradiction(kb_root, "open-minor", "minor", "open")
    from gateway.ops.status import status
    result = status()
    assert "contradiction" in result.summary.lower()


# ── CLI: wiki contradiction ───────────────────────────────────────────────────

def test_cli_contradiction_list_subcommand(kb_root: Path) -> None:
    from gateway.cli import build_parser
    ns = build_parser().parse_args(["contradiction", "list"])
    assert ns.subcommand == "contradiction"
    assert ns.contradiction_action == "list"
    assert ns.status == "open"


def test_cli_contradiction_resolve_subcommand(kb_root: Path) -> None:
    from gateway.cli import build_parser
    ns = build_parser().parse_args(["contradiction", "resolve", "my-slug", "--status", "resolved", "--note", "done"])
    assert ns.contradiction_action == "resolve"
    assert ns.slug == "my-slug"
    assert ns.status == "resolved"
    assert ns.note == "done"
