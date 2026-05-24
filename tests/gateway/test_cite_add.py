"""K1 (M48): `wiki cite-add` op — claim-text-driven citation insertion.

Internal escalation pipeline per D5:
1. Exact substring match
2. Normalized substring (NFKC + casefold + whitespace + trailing-punct)
3. Optional fuzzy LLM (--fuzzy flag, off by default)
4. Error with 3 nearest-by-edit-distance suggestions

At any step: 1 hit → cite; 2+ hits → ambiguity error.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.cite_add import cite_add


_FRONTMATTER_LINES = 7  # how many lines the test page's frontmatter occupies


def _make_source(kb_root: Path, source_id: str = "web-2026-05-24-test") -> None:
    """Place a stub raw source + wiki source page so cite_add can resolve it."""
    raw_path = paths.raw_source_path("web", source_id)
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_front = {
        "id": source_id,
        "type": "web",
        "title": "Test Source",
        "url": "https://example.com/test",
        "ingested_at": "2026-05-24T00:00:00Z",
        "content_hash": "sha256:" + "0" * 64,
        "domains": ["testdom"],
        "wiki_pages": [],
        "nlm_corpus_ids": [],
    }
    raw_path.write_text(fm.serialize(raw_front, "Body content for the test source.\n"))

    wiki_path = paths.wiki_source_path(source_id)
    wiki_path.parent.mkdir(parents=True, exist_ok=True)
    wiki_path.write_text(
        fm.serialize(
            {
                "type": "source",
                "slug": source_id,
                "canonical_name": "Test Source",
                "source_type": "web",
                "domains": ["testdom"],
            },
            "# Test Source\n\n_(stub source page for test fixtures)_\n",
        )
    )


def _make_synthesis(kb_root: Path, body: str, slug: str = "test-synth") -> Path:
    page_path = paths.wiki_dir() / "synthesis" / f"{slug}.md"
    page_path.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "synthesis",
        "slug": slug,
        "canonical_name": "Test Synthesis",
        "domains": ["testdom"],
        "draft": True,
    }
    page_path.write_text(fm.serialize(front, body))
    return page_path


# --- exact match path -------------------------------------------------------


def test_cite_add_exact_match_single_hit_cites_line(kb_root: Path):
    _make_source(kb_root)
    body = (
        "# Test Synthesis\n\n## Summary\n\n"
        "This is a substantive claim sentence we want to cite directly.\n"
    )
    page = _make_synthesis(kb_root, body)

    result = cite_add(
        page,
        claim_text="This is a substantive claim sentence we want to cite directly.",
        source_id="web-2026-05-24-test",
    )
    assert result.success, result.errors
    text = page.read_text()
    assert "[[sources/web-2026-05-24-test]]" in text


def test_cite_add_idempotent_on_repeat_same_claim(kb_root: Path):
    _make_source(kb_root)
    body = (
        "# Test\n\n## Summary\n\nThis is a substantive claim we want to cite for the test.\n"
    )
    page = _make_synthesis(kb_root, body)

    r1 = cite_add(
        page,
        claim_text="This is a substantive claim we want to cite for the test.",
        source_id="web-2026-05-24-test",
    )
    assert r1.success
    r2 = cite_add(
        page,
        claim_text="This is a substantive claim we want to cite for the test.",
        source_id="web-2026-05-24-test",
    )
    # Re-citing the same claim with the same source is a no_op (or success
    # with no actual change). Either is acceptable; what matters is the file
    # didn't double-cite.
    text = page.read_text()
    assert text.count("[[sources/web-2026-05-24-test]]") == 1
    assert r2.no_op or r2.success


# --- ambiguity --------------------------------------------------------------


def test_cite_add_returns_ambiguity_when_claim_appears_twice(kb_root: Path):
    _make_source(kb_root)
    body = (
        "# Test\n\n## Section A\n\nDuplicate substantive claim sentence appears here.\n"
        "\n## Section B\n\nDuplicate substantive claim sentence appears here.\n"
    )
    page = _make_synthesis(kb_root, body)
    result = cite_add(
        page,
        claim_text="Duplicate substantive claim sentence appears here.",
        source_id="web-2026-05-24-test",
    )
    assert not result.success
    assert any("ambigu" in str(e).lower() or "multiple" in str(e).lower()
               for e in result.errors), f"expected ambiguity error: {result.errors}"


# --- normalized substring path ----------------------------------------------


def test_cite_add_normalized_match_handles_whitespace_drift(kb_root: Path):
    _make_source(kb_root)
    body = (
        "# Test\n\n## Summary\n\n"
        "This is a substantive claim with some interior text and final words.\n"
    )
    page = _make_synthesis(kb_root, body)
    # User provides version with extra spaces and different case
    result = cite_add(
        page,
        claim_text="THIS  is  a   substantive    claim   with some interior text and final words",
        source_id="web-2026-05-24-test",
    )
    assert result.success, f"normalized match should resolve: {result.errors}"


def test_cite_add_normalized_match_handles_trailing_punct(kb_root: Path):
    _make_source(kb_root)
    body = "# Test\n\n## Summary\n\nThis is a meaningful sentence with a final period.\n"
    page = _make_synthesis(kb_root, body)
    # Without the period
    result = cite_add(
        page,
        claim_text="This is a meaningful sentence with a final period",
        source_id="web-2026-05-24-test",
    )
    assert result.success, f"trailing-punct tolerant match should resolve: {result.errors}"


# --- no-match path ----------------------------------------------------------


def test_cite_add_no_match_returns_helpful_error_with_suggestions(kb_root: Path):
    _make_source(kb_root)
    body = (
        "# Test\n\n## Summary\n\nThe quick brown fox jumps over the lazy dog.\n"
    )
    page = _make_synthesis(kb_root, body)
    result = cite_add(
        page,
        claim_text="A completely unrelated sentence with no overlap whatsoever.",
        source_id="web-2026-05-24-test",
    )
    assert not result.success
    # Some form of "not found" / "no match" message
    err_text = " ".join(str(e) for e in result.errors).lower()
    assert "not found" in err_text or "no match" in err_text


# --- fuzzy path (LLM stub) --------------------------------------------------


class _StubFuzzyClient:
    """Test stub for cite_add's fuzzy LLM client. Returns a canned line."""

    def __init__(self, *, line_to_return: int | None = 5):
        self.calls: list[tuple[str, str]] = []
        self._line = line_to_return

    def resolve(self, claim_text: str, body: str) -> int | None:
        self.calls.append((claim_text, body))
        return self._line


def test_cite_add_fuzzy_default_off_does_not_invoke_llm(kb_root: Path):
    """`fuzzy=False` (default): if normalized substring misses, no LLM call."""
    _make_source(kb_root)
    body = "# Test\n\n## Summary\n\nThe original wording is here verbatim.\n"
    page = _make_synthesis(kb_root, body)
    stub = _StubFuzzyClient()

    result = cite_add(
        page,
        claim_text="Paraphrased version with no substring overlap whatsoever.",
        source_id="web-2026-05-24-test",
        fuzzy=False,
        fuzzy_client=stub,
    )
    assert not result.success
    assert stub.calls == [], "fuzzy client must not be invoked when fuzzy=False"


def test_cite_add_fuzzy_true_invokes_llm_on_miss(kb_root: Path):
    """`fuzzy=True`: when normalized substring misses, ask LLM."""
    _make_source(kb_root)
    body = (
        "# Test\n\n## Summary\n\n"
        "The original wording uses different vocabulary than the user provided.\n"
    )
    page = _make_synthesis(kb_root, body)
    # Compute the file-line that the LLM should "find" — body-line 5 + offset
    # for our 7-line frontmatter ≈ 12. Use whatever the test's actual offset is.
    page_text = page.read_text()
    body_offset = fm.body_line_offset(page_text)
    stub = _StubFuzzyClient(line_to_return=body_offset + 5)

    result = cite_add(
        page,
        claim_text="Paraphrased version completely different from the source text.",
        source_id="web-2026-05-24-test",
        fuzzy=True,
        fuzzy_client=stub,
    )
    assert result.success, f"fuzzy LLM resolution should succeed: {result.errors}"
    assert len(stub.calls) == 1, "fuzzy client should be invoked exactly once"


def test_cite_add_fuzzy_true_llm_returns_none_yields_error(kb_root: Path):
    _make_source(kb_root)
    body = "# Test\n\n## Summary\n\nSome content.\n"
    page = _make_synthesis(kb_root, body)
    stub = _StubFuzzyClient(line_to_return=None)

    result = cite_add(
        page,
        claim_text="Completely different paraphrase nobody recognizes.",
        source_id="web-2026-05-24-test",
        fuzzy=True,
        fuzzy_client=stub,
    )
    assert not result.success


# --- argument validation ----------------------------------------------------


def test_cite_add_rejects_empty_claim_text(kb_root: Path):
    _make_source(kb_root)
    body = "# Test\n\n## Summary\n\nContent.\n"
    page = _make_synthesis(kb_root, body)
    result = cite_add(page, claim_text="", source_id="web-2026-05-24-test")
    assert not result.success


def test_cite_add_rejects_missing_source(kb_root: Path):
    body = "# Test\n\n## Summary\n\nA substantive claim that needs a citation.\n"
    page = _make_synthesis(kb_root, body)
    # Don't make the source — should fail at source-existence check (delegated to cite())
    result = cite_add(
        page,
        claim_text="A substantive claim that needs a citation.",
        source_id="web-does-not-exist",
    )
    assert not result.success
