"""Tests for cite_suggest (M49 Phase C).

Mocks AnthropicAPIClient so tests are hermetic. Real-network verification
is done in the M49 hand-test (see docs/milestones/M49.md).
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

from gateway import frontmatter as fm
from gateway.llm.telemetry import CallResult
from gateway.ops.cite_suggest import (
    CiteSuggestion,
    suggest_cites,
)


def _write_concept_draft_with_one_claim(kb_root: Path, slug: str,
                                        source_ids: list[str]) -> Path:
    page = kb_root / "wiki" / "concepts" / f"{slug}.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "concept",
        "slug": slug,
        "title": slug.replace("-", " ").title(),
        "domains": ["test-domain"],
        "draft": True,
        "draft_started_at": "2026-05-12T00:00:00Z",
        "sources": source_ids,
    }
    body = "# title\n\n## Summary\n\nThe unique claim X requires citation.\n"
    page.write_text(fm.serialize(front, body))
    return page


def _write_raw_source(kb_root: Path, source_id: str, body_text: str,
                      source_type: str = "web") -> Path:
    raw = kb_root / "raw" / source_type / f"{source_id}.md"
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw_front = {
        "id": source_id,
        "type": source_type,
        "title": f"Source {source_id}",
        "url": f"https://example.com/{source_id}",
        "domains": ["test-domain"],
    }
    raw.write_text(fm.serialize(raw_front, body_text))

    wiki_src = kb_root / "wiki" / "sources" / f"{source_id}.md"
    wiki_src.parent.mkdir(parents=True, exist_ok=True)
    wiki_src.write_text(fm.serialize(
        {
            "type": "source",
            "source_id": source_id,
            "source_type": source_type,
            "title": f"Source {source_id}",
            "domains": ["test-domain"],
        },
        f"# {source_id}\n",
    ))
    return raw


def test_suggest_returns_unambiguous_when_single_source_quotes_claim(kb_root):
    source_id = "web-2026-01-01-aaa"
    _write_raw_source(kb_root, source_id, "Claim X is documented here.\n")
    page = _write_concept_draft_with_one_claim(kb_root, "concept-a", [source_id])

    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = CallResult(
        text=(
            '{"suggestions": [{"line": 6, "source_id": "web-2026-01-01-aaa", '
            '"evidence_quote": "Claim X is documented here."}]}'
        ),
        input_tokens=100, output_tokens=20, model="claude-sonnet-4-6",
    )

    results = suggest_cites(page, client=fake_client)

    assert len(results) == 1
    s: CiteSuggestion = results[0]
    assert s.line == 6
    assert s.source_id == source_id
    assert s.unambiguous is True
    assert s.evidence_verified is True


def test_two_suggestions_on_same_line_are_marked_ambiguous(kb_root):
    sid1 = "web-2026-01-01-aaa"
    sid2 = "web-2026-01-02-bbb"
    _write_raw_source(kb_root, sid1, "Claim X is documented in source one.\n")
    _write_raw_source(kb_root, sid2, "Claim X is documented in source two.\n")
    page = _write_concept_draft_with_one_claim(kb_root, "concept-b", [sid1, sid2])

    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = CallResult(
        text=(
            '{"suggestions": ['
            f'{{"line": 6, "source_id": "{sid1}", "evidence_quote": "Claim X is documented in source one."}},'
            f'{{"line": 6, "source_id": "{sid2}", "evidence_quote": "Claim X is documented in source two."}}'
            ']}'
        ),
        input_tokens=100, output_tokens=40, model="claude-sonnet-4-6",
    )

    results = suggest_cites(page, client=fake_client)

    assert len(results) == 2
    assert all(not s.auto_appliable for s in results)
    assert all(s.skip_reason == "multi-candidate line" for s in results)


def test_unverified_evidence_quote_marks_suggestion_not_appliable(kb_root):
    sid = "web-2026-01-01-ccc"
    _write_raw_source(kb_root, sid, "Real text only.\n")
    page = _write_concept_draft_with_one_claim(kb_root, "concept-c", [sid])

    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = CallResult(
        text=(
            '{"suggestions": [{"line": 6, "source_id": "%s", '
            '"evidence_quote": "HALLUCINATED QUOTE NOT IN SOURCE"}]}' % sid
        ),
        input_tokens=80, output_tokens=15, model="claude-sonnet-4-6",
    )

    results = suggest_cites(page, client=fake_client)

    assert len(results) == 1
    s = results[0]
    assert s.unambiguous is True
    assert s.evidence_verified is False
    assert s.auto_appliable is False
    assert "not found" in s.skip_reason


def test_synthesizes_with_sources_prefix_loads_raw_body(kb_root):
    """`synthesizes:` frontmatter entries are stored as `sources/<id>`
    (matching the inline `[[sources/<id>]]` citation token). The raw
    file lives at `raw/<type>/<id>.md` without the prefix. cite_suggest
    must strip the prefix before reading raw bodies; otherwise it sends
    an empty source corpus to the LLM and verification always fails.
    Regression for hand-test discovery on real synthesis pages."""
    source_id_bare = "web-2024-02-07-prefix"
    _write_raw_source(kb_root, source_id_bare, "Verifiable evidence text.\n")

    # Build a draft whose `synthesizes:` uses the prefixed form (the wire
    # format in real synthesis pages).
    page = kb_root / "wiki" / "synthesis" / "test-prefix.md"
    page.parent.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "synthesis",
        "slug": "test-prefix",
        "title": "Test Prefix",
        "domains": ["test-domain"],
        "draft": True,
        "draft_started_at": "2026-05-23T00:00:00Z",
        "synthesizes": [f"sources/{source_id_bare}"],
    }
    body = "# Test\n\n## Synthesis\n\nClaim needing citation here.\n"
    page.write_text(fm.serialize(front, body))

    # LLM emits the bare id form (per the system prompt instructions).
    fake_client = MagicMock()
    fake_client.call_with_usage.return_value = CallResult(
        text=(
            '{"suggestions": [{"line": 6, "source_id": "%s", '
            '"evidence_quote": "Verifiable evidence text."}]}' % source_id_bare
        ),
        input_tokens=80, output_tokens=15, model="claude-sonnet-4-6",
    )

    results = suggest_cites(page, client=fake_client)

    assert len(results) == 1
    s = results[0]
    # source_id stored as bare id (no `sources/` prefix)
    assert s.source_id == source_id_bare
    assert s.unambiguous is True
    # Verification succeeds — the bare id resolved to the raw file on disk
    assert s.evidence_verified is True
    assert s.auto_appliable is True
