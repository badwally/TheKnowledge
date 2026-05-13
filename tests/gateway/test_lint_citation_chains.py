"""Tests for M45 `wiki lint --scope citation-chains`."""

from __future__ import annotations

from pathlib import Path

from gateway import paths
from gateway.lint import citation_chains


def _write_synthesis(
    kb_root: Path,
    slug: str,
    body: str,
    *,
    synthesizes: list[str] | None = None,
) -> Path:
    front_lines = [
        "---",
        "type: synthesis",
        f"slug: {slug}",
        f"title: {slug}",
        "domains:",
        "- test",
        "question: test question",
        "created_at: '2026-05-13T00:00:00Z'",
    ]
    if synthesizes is not None:
        front_lines.append("synthesizes:")
        for s in synthesizes:
            front_lines.append(f"- {s}")
    front_lines.append("---")
    front_lines.append("")
    path = kb_root / "wiki" / "synthesis" / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(front_lines) + body)
    return path


def _write_source(kb_root: Path, slug: str) -> Path:
    path = kb_root / "raw" / "web" / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\nid: " + slug + "\ntype: web\ntitle: t\n---\nbody\n")
    return path


def test_dangling_synthesizes_ref_flagged(kb_root):
    _write_synthesis(
        kb_root,
        "page-a",
        body="## Synthesis\n\nA claim with citation [[sources/web-known]].\n\n"
             "## Included works\n\n- [[sources/web-known]]\n- [[sources/web-MISSING]]\n",
        synthesizes=["sources/web-known", "sources/web-MISSING"],
    )
    _write_source(kb_root, "web-known")
    findings = citation_chains.run()
    dangling = [f for f in findings if f.check == "dangling-synthesizes-ref"]
    assert len(dangling) == 1
    assert "sources/web-MISSING" in dangling[0].metadata["target"]


def test_clean_synthesizes_no_findings(kb_root):
    _write_source(kb_root, "web-a")
    _write_source(kb_root, "web-b")
    _write_synthesis(
        kb_root,
        "page-clean",
        body="## Synthesis\n\nBased on the provided sources, patterns emerge.\n\n"
             "## Included works\n\n- [[sources/web-a]]\n- [[sources/web-b]]\n",
        synthesizes=["sources/web-a", "sources/web-b"],
    )
    findings = citation_chains.run()
    assert not any(f.check == "dangling-synthesizes-ref" for f in findings)
    assert not any(f.check == "aggregate-framing-without-synthesizes" for f in findings)


def test_aggregate_framing_without_synthesizes_warns(kb_root):
    _write_synthesis(
        kb_root,
        "page-legacy",
        body="## Synthesis\n\nBased on the provided sources, several themes emerge.\n",
        synthesizes=None,  # no synthesizes: field — legacy page
    )
    findings = citation_chains.run()
    framing = [f for f in findings if f.check == "aggregate-framing-without-synthesizes"]
    assert len(framing) == 1
    assert framing[0].severity == "warning"
    assert "page-legacy" in framing[0].path


def test_no_framing_no_warning(kb_root):
    """A page without aggregate framing and without `synthesizes:` is fine."""
    _write_synthesis(
        kb_root,
        "page-normal",
        body="## Synthesis\n\nA direct claim with a citation [[sources/web-x]].\n",
        synthesizes=None,
    )
    _write_source(kb_root, "web-x")
    findings = citation_chains.run()
    assert not any(f.check == "aggregate-framing-without-synthesizes" for f in findings)


def test_synthesis_tier_ref_resolves(kb_root):
    """`synthesizes:` pointing to another synthesis page (second-derivative)
    resolves as long as that synthesis page exists on disk."""
    _write_synthesis(kb_root, "page-leaf-1", body="## Synthesis\nx [[sources/web-1]]\n")
    _write_synthesis(kb_root, "page-leaf-2", body="## Synthesis\ny [[sources/web-2]]\n")
    _write_source(kb_root, "web-1")
    _write_source(kb_root, "web-2")
    _write_synthesis(
        kb_root,
        "page-cross",
        body="## Synthesis\n\nBased on the corpus, a cross-cutting pattern.\n\n"
             "## Included works\n\n- [[synthesis/page-leaf-1]]\n- [[synthesis/page-leaf-2]]\n",
        synthesizes=["synthesis/page-leaf-1", "synthesis/page-leaf-2"],
    )
    findings = citation_chains.run()
    assert not any(f.check == "dangling-synthesizes-ref" for f in findings)
