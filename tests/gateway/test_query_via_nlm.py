"""Tests for the rebuilt `wiki query` op (`gateway.ops.query`).

The op now queries the persistent NotebookLM corpus and files the answer
as a synthesis page. The bag-of-words fallback is gone; missing-domain
notebooks now error out with a hint to run `wiki research`.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import nlm_registry, paths
from gateway.ops.query import query
from gateway.research import source_map as sm


# --- mock client -----------------------------------------------------------


@dataclass
class _CannedNlm:
    answer: str = ""
    citations: dict = field(default_factory=dict)
    sources_used: list = field(default_factory=list)
    queries_made: list[tuple[str, str]] = field(default_factory=list)

    def notebook_query(self, notebook_id: str, question: str) -> dict:
        self.queries_made.append((notebook_id, question))
        return {
            "answer": self.answer,
            "citations": self.citations,
            "sources_used": self.sources_used,
        }


# --- helpers ---------------------------------------------------------------


def _seed_persistent(domain: str, notebook_id: str = "nb-domain-1") -> str:
    nlm_registry.register(domain, notebook_id)
    return notebook_id


def _seed_source_map_cache(notebook_id: str, mapping: dict[str, str]) -> None:
    """Pre-populate the source-map cache so build_source_map isn't called."""
    cache_dir = paths.knowledge_root() / "nlm" / "source_maps"
    cache_dir.mkdir(parents=True, exist_ok=True)
    import json

    (cache_dir / f"{notebook_id}.json").write_text(
        json.dumps(mapping, indent=2, sort_keys=True), encoding="utf-8"
    )


def _write_raw_source(kb_root: Path, *, slug: str, source_type: str = "web"):
    """Write a minimal raw source so [[sources/<slug>]] resolves."""
    body = f"Body for {slug}.\n"
    from gateway import validator

    front = {
        "id": slug,
        "type": source_type,
        "title": f"Title: {slug}",
        "url": f"https://example.com/{slug}",
        "authors": ["Test"],
        "published_at": "2026-01-01",
        "ingested_at": "2026-01-01T00:00:00Z",
        "content_hash": validator.compute_content_hash(body),
        "domains": ["alpha"],
        "nlm_corpus_ids": [],
        "wiki_pages": [],
        "meta": {},
    }
    target = kb_root / "raw" / source_type / f"{slug}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(fm.serialize(front, body))


# --- happy path -----------------------------------------------------------


def test_query_files_synthesis_with_resolved_citations(kb_root: Path):
    notebook_id = _seed_persistent("alpha")
    _write_raw_source(kb_root, slug="known-page")
    _seed_source_map_cache(notebook_id, {"nlm-x": "raw/web/known-page"})

    client = _CannedNlm(
        answer="GLP-1 reduces food noise [1].",
        citations={1: "nlm-x"},
        sources_used=["nlm-x"],
    )

    result = query(
        "Does GLP-1 reduce food noise?",
        domain="alpha",
        nlm_client=client,
    )
    assert result.success, result.errors
    assert client.queries_made == [(notebook_id, "Does GLP-1 reduce food noise?")]

    # Find the freshly-written synthesis page.
    synth_dir = kb_root / "wiki" / "synthesis"
    pages = list(synth_dir.glob("*.md"))
    assert pages, "expected one synthesis page"
    text = pages[0].read_text()
    assert "[[sources/known-page]]" in text
    assert "GLP-1 reduces food noise" in text
    front, _ = fm.parse(text)
    assert front["type"] == "synthesis"
    assert front["domains"] == ["alpha"]
    assert front["nlm_notebook_id"] == notebook_id


# --- no notebook ----------------------------------------------------------


def test_query_without_persistent_notebook_errors(kb_root: Path):
    client = _CannedNlm()
    result = query("any question", domain="undefined", nlm_client=client)
    assert not result.success
    joined = " ".join(result.errors)
    assert "no notebook" in joined
    assert "wiki research" in joined
    # No notebook_query call should have been made.
    assert client.queries_made == []


# --- unresolved citations ------------------------------------------------


def test_unresolved_citations_emit_nlm_placeholder(kb_root: Path):
    notebook_id = _seed_persistent("alpha", "nb-orphan-1")
    # Empty source-map cache so every NLM id is unresolved.
    _seed_source_map_cache(notebook_id, {})

    client = _CannedNlm(
        answer="Some answer about [1] and [2].",
        citations={1: "nlm-orphan-a", 2: "nlm-orphan-b"},
    )

    result = query("question?", domain="alpha", nlm_client=client)
    assert result.success, result.errors

    # Synthesis page should contain `[[nlm:...]]` for both orphan ids.
    synth_dir = kb_root / "wiki" / "synthesis"
    pages = list(synth_dir.glob("*.md"))
    assert pages
    text = pages[0].read_text()
    assert "[[nlm:nlm-orphan-a]]" in text
    assert "[[nlm:nlm-orphan-b]]" in text

    # Lint-warning event should have been logged.
    log_text = paths.log_path().read_text()
    assert "lint-warning" in log_text or "unresolved_citations" in log_text


# --- honest provenance: no backstop citation on uncited lines ------------


def test_query_does_not_backstop_uncited_lines(kb_root: Path):
    """Regression: `_backstop_uncited_lines` previously slathered the first
    resolved citation onto every uncited line, falsely attributing claims
    to sources that did not actually support them. Synthesis pages must
    now reflect only the inline citations NotebookLM produced."""
    notebook_id = _seed_persistent("alpha", "nb-honest")
    _write_raw_source(kb_root, slug="cited-page")
    _write_raw_source(kb_root, slug="other-page")
    _seed_source_map_cache(
        notebook_id,
        {"nlm-cited": "raw/web/cited-page", "nlm-other": "raw/web/other-page"},
    )

    client = _CannedNlm(
        answer=(
            "First sentence with an explicit citation [1].\n"
            "Second sentence with no citation marker at all in NotebookLM output.\n"
        ),
        citations={1: "nlm-cited"},
    )
    result = query("test?", domain="alpha", nlm_client=client, draft=True)
    assert result.success, result.errors

    pages = list((kb_root / "wiki" / "synthesis").glob("*.md"))
    assert pages
    text = pages[0].read_text()
    body = text.split("---", 2)[2]
    cited_line = next(ln for ln in body.splitlines() if "First sentence" in ln)
    uncited_line = next(ln for ln in body.splitlines() if "Second sentence" in ln)
    assert "[[sources/cited-page]]" in cited_line
    # Critical: the uncited line must NOT have been auto-stamped with the
    # cited-page citation as a backstop.
    assert "[[sources/cited-page]]" not in uncited_line
    assert "[[sources/other-page]]" not in uncited_line


# --- empty inputs ---------------------------------------------------------


def test_query_empty_question_errors(kb_root: Path):
    _seed_persistent("alpha")
    result = query("   ", domain="alpha")
    assert not result.success
    assert "non-empty" in " ".join(result.errors)


def test_query_missing_domain_errors(kb_root: Path):
    result = query("anything", domain="")
    assert not result.success
    joined = " ".join(result.errors)
    assert "domain" in joined.lower()


# --- builds source-map when cache absent ---------------------------------


def test_query_builds_source_map_when_cache_missing(
    kb_root: Path, monkeypatch: pytest.MonkeyPatch
):
    notebook_id = _seed_persistent("alpha", "nb-fresh")
    _write_raw_source(kb_root, slug="fresh-page")

    # Stub the subprocess inside source_map so it returns one mapping.
    class _Fake:
        def __init__(self, *, stdout: str = "", returncode: int = 0):
            self.stdout = stdout
            self.stderr = ""
            self.returncode = returncode

    import json

    def _fake_run(args, **kwargs):
        return _Fake(
            stdout=json.dumps(
                [{"id": "nlm-fresh", "url": "https://example.com/fresh-page"}]
            )
        )

    monkeypatch.setattr(sm.subprocess, "run", _fake_run)

    client = _CannedNlm(
        answer="Answer cites [1].",
        citations={1: "nlm-fresh"},
    )
    result = query("question?", domain="alpha", nlm_client=client)
    assert result.success, result.errors

    synth_dir = kb_root / "wiki" / "synthesis"
    pages = list(synth_dir.glob("*.md"))
    assert pages
    assert "[[sources/fresh-page]]" in pages[0].read_text()
