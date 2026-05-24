"""Tests for `wiki cite` — gateway-mediated citation insertion."""

from __future__ import annotations

from pathlib import Path

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.cite import cite


def _write_wiki_source(kb_root: Path, source_id: str, *, source_type: str = "web") -> Path:
    """Create both a raw/ source and the wiki/sources/ summary page so a citation can target them."""
    raw_path = kb_root / "raw" / source_type / f"{source_id}.md"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_front = {
        "id": source_id,
        "type": source_type,
        "title": f"Raw source {source_id}",
        "url": f"https://example.com/{source_id}",
        "domains": ["test-domain"],
        "wiki_pages": [],
    }
    raw_path.write_text(fm.serialize(raw_front, "Body.\n"))

    wiki_src = kb_root / "wiki" / "sources" / f"{source_id}.md"
    wiki_src.parent.mkdir(parents=True, exist_ok=True)
    wiki_src.write_text(
        fm.serialize(
            {
                "type": "source",
                "source_id": source_id,
                "source_type": source_type,
                "title": f"Wiki source {source_id}",
                "domains": ["test-domain"],
            },
            f"# {source_id}\n\nSummary.\n",
        )
    )
    return wiki_src


def _write_synthesis_page(kb_root: Path, slug: str, body: str) -> Path:
    page = kb_root / "wiki" / "synthesis" / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "synthesis",
        "slug": slug,
        "title": "Test synthesis",
        "domains": ["test-domain"],
        "draft": True,
    }
    page.write_text(fm.serialize(front, body))
    return page


def test_cite_adds_token_and_updates_backlink(kb_root):
    src_id = "web-2026-01-01-aaa"
    _write_wiki_source(kb_root, src_id)
    page = _write_synthesis_page(
        kb_root,
        "test-cite-1",
        "# Test\n\n## Synthesis\n\nA factual claim that needs grounding here.\n",
    )

    text_before = page.read_text()
    target_line = next(
        i + 1
        for i, ln in enumerate(text_before.splitlines(keepends=True))
        if "factual claim" in ln
    )

    result = cite(page, [(target_line, src_id)])

    assert result.success, result.errors
    body_after = page.read_text()
    assert f"[[sources/{src_id}]]" in body_after
    # backlink propagated to raw frontmatter
    raw_path = paths.raw_source_path("web", src_id)
    raw_front, _ = fm.parse(raw_path.read_text())
    rel = page.relative_to(kb_root)
    assert str(rel) in (raw_front.get("wiki_pages") or [])


def test_cite_rejects_missing_source_page(kb_root):
    page = _write_synthesis_page(
        kb_root,
        "test-cite-2",
        "# Test\n\n## Synthesis\n\nA claim sentence with five words here.\n",
    )
    result = cite(page, [(5, "web-does-not-exist")])
    assert not result.success
    assert any("does not exist" in e for e in result.errors)


def test_cite_rejects_already_cited_line(kb_root):
    src_id = "web-2026-01-01-bbb"
    _write_wiki_source(kb_root, src_id)
    body = "# Test\n\n## Synthesis\n\nA claim already cited [[sources/" + src_id + "]].\n"
    page = _write_synthesis_page(kb_root, "test-cite-3", body)

    text = page.read_text()
    target_line = next(
        i + 1
        for i, ln in enumerate(text.splitlines(keepends=True))
        if "already cited" in ln
    )
    result = cite(page, [(target_line, src_id)])
    assert not result.success
    assert any("already cites" in e for e in result.errors)


def test_cite_rejects_out_of_range_line(kb_root):
    src_id = "web-2026-01-01-ccc"
    _write_wiki_source(kb_root, src_id)
    page = _write_synthesis_page(kb_root, "test-cite-4", "# Test\n\nShort body.\n")
    result = cite(page, [(9999, src_id)])
    assert not result.success
    assert any("out of range" in e for e in result.errors)


def test_cite_rejects_page_outside_wiki(kb_root):
    src_id = "web-2026-01-01-ddd"
    _write_wiki_source(kb_root, src_id)
    not_a_wiki_page = kb_root / "raw" / "web" / "scratch.md"
    not_a_wiki_page.write_text(
        fm.serialize({"id": "scratch", "type": "web", "title": "x"}, "body\n")
    )
    result = cite(not_a_wiki_page, [(5, src_id)])
    assert not result.success
    assert any("not under wiki/" in e for e in result.errors)


def test_cite_handles_multiple_additions_atomically(kb_root):
    sid_a = "web-2026-01-01-eee"
    sid_b = "web-2026-01-01-fff"
    _write_wiki_source(kb_root, sid_a)
    _write_wiki_source(kb_root, sid_b)
    body = (
        "# Test\n\n## Synthesis\n\nFirst claim sentence here please.\n"
        "Second claim sentence here please.\n"
    )
    page = _write_synthesis_page(kb_root, "test-cite-5", body)

    text = page.read_text()
    lines = text.splitlines(keepends=True)
    line_a = next(i + 1 for i, ln in enumerate(lines) if "First claim" in ln)
    line_b = next(i + 1 for i, ln in enumerate(lines) if "Second claim" in ln)

    result = cite(page, [(line_a, sid_a), (line_b, sid_b)])
    assert result.success, result.errors
    body_after = page.read_text()
    assert f"[[sources/{sid_a}]]" in body_after
    assert f"[[sources/{sid_b}]]" in body_after


def test_cite_rejects_when_one_source_missing_no_partial_writes(kb_root):
    sid_a = "web-2026-01-01-ggg"
    _write_wiki_source(kb_root, sid_a)
    body = "# Test\n\n## Synthesis\n\nA claim sentence with five words.\n"
    page = _write_synthesis_page(kb_root, "test-cite-6", body)

    text_before = page.read_text()
    target_line = next(
        i + 1
        for i, ln in enumerate(text_before.splitlines(keepends=True))
        if "claim sentence" in ln
    )
    # second addition references a missing source — should reject everything
    result = cite(page, [(target_line, sid_a), (target_line, "web-missing-zzz")])
    assert not result.success
    assert page.read_text() == text_before  # no partial mutation
