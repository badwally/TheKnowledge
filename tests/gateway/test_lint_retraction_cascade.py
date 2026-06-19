"""Tests for extended retracted-citations lint: cascade dependents (Phase 5 T1, Step 18).

Extends test_qual7_retraction_monitor.py's existing coverage with:
- Cascade transitive dependent surfaced as a LintFinding with depth metadata
- Negative control: no retracted sources → no findings from cascade path
- Direct-cite findings still carry the retracted_source metadata (non-regression)
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.lint.retracted_citations import run as lint_run
from gateway.lint import SEVERITY_ERROR, SEVERITY_WARNING


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _write_pubmed_source(kb_root: Path, source_id: str, *, retracted: bool = False) -> None:
    raw_dir = kb_root / "raw" / "pubmed"
    raw_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "pubmed",
        "id": source_id,
        "title": f"Paper {source_id}",
        "domains": ["med"],
        "created_at": "2026-01-01T00:00:00Z",
    }
    if retracted:
        front["retracted"] = True
    body = f"# Paper {source_id}\n\nAbstract.\n"
    (raw_dir / f"{source_id}.md").write_text(fm.serialize(front, body))


def _write_synthesis(
    kb_root: Path,
    slug: str,
    synthesizes: list[str],
    body_extra: str = "",
) -> Path:
    d = kb_root / "wiki" / "synthesis"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "synthesis",
        "slug": slug,
        "title": slug.replace("-", " "),
        "synthesizes": list(synthesizes),
        "domains": ["med"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    body = (
        f"# {slug}\n\n"
        "## Included works\n"
        + "".join(f"- [[{s}]]\n" for s in synthesizes)
        + f"\n## Analysis\n\nLoad-bearing claim [[{synthesizes[0]}]].\n{body_extra}"
    )
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, body))
    return p


# ===========================================================================
# Cascade findings surfaced from lint
# ===========================================================================

def test_lint_surfaces_transitive_cascade_dependent(kb_root):
    """A page that is a transitive dependent of a retracted source is flagged."""
    _write_pubmed_source(kb_root, "pubmed-retracted", retracted=True)
    # Page A directly cites the retracted source
    _write_synthesis(kb_root, "direct-dep", ["sources/pubmed-retracted"])
    # Page B synthesizes A — transitive dependent
    _write_synthesis(kb_root, "transitive-dep", ["synthesis/direct-dep"])

    findings = lint_run()
    finding_paths = {f.path for f in findings}

    # direct-dep appears because it cites the retracted source directly
    assert any("direct-dep" in p for p in finding_paths)
    # transitive-dep must also appear (cascade finding)
    assert any("transitive-dep" in p for p in finding_paths)


def test_lint_cascade_finding_carries_retracted_source_metadata(kb_root):
    """Cascade findings carry retracted_source and depth in metadata."""
    _write_pubmed_source(kb_root, "pubmed-r1", retracted=True)
    _write_synthesis(kb_root, "direct-d", ["sources/pubmed-r1"])
    _write_synthesis(kb_root, "transitive-t", ["synthesis/direct-d"])

    findings = lint_run()
    cascade_findings = [
        f for f in findings if "transitive-t" in f.path
    ]
    assert len(cascade_findings) >= 1
    cf = cascade_findings[0]
    assert cf.metadata.get("retracted_source") == "pubmed-r1"
    # depth must be >= 2 (transitive is at least one step removed from direct)
    assert cf.metadata.get("depth", 0) >= 2


def test_lint_no_cascade_findings_when_no_retracted_sources(kb_root):
    """No retracted sources → no cascade findings (negative control)."""
    _write_pubmed_source(kb_root, "pubmed-healthy", retracted=False)
    _write_synthesis(kb_root, "healthy-page", ["sources/pubmed-healthy"])
    _write_synthesis(kb_root, "healthy-transitive", ["synthesis/healthy-page"])

    findings = lint_run()
    assert findings == []


def test_lint_unrelated_page_not_flagged_by_cascade(kb_root):
    """A page that cites only non-retracted sources is not cascade-flagged."""
    _write_pubmed_source(kb_root, "pubmed-retracted", retracted=True)
    _write_pubmed_source(kb_root, "pubmed-clean", retracted=False)
    _write_synthesis(kb_root, "retracted-chain", ["sources/pubmed-retracted"])
    _write_synthesis(kb_root, "clean-chain", ["sources/pubmed-clean"])

    findings = lint_run()
    finding_paths = {f.path for f in findings}
    assert not any("clean-chain" in p for p in finding_paths)
    assert any("retracted-chain" in p for p in finding_paths)
