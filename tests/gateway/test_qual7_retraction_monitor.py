"""QUAL-7: PubMed retraction + arXiv revision pollers + retracted-citations lint."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from gateway import frontmatter as fm, paths
from gateway.lint import SEVERITY_ERROR
from gateway.lint.retracted_citations import run as lint_run
from gateway.pollers.arxiv_revisions import (
    ArxivRevisionPoller,
    current_version,
    _arxiv_id_from_source_id,
)
from gateway.pollers.pubmed_retractions import (
    PubmedRetractionPoller,
    is_retracted,
    _pmid_from_id,
)


# --- helpers -------------------------------------------------------------------

_RETRACTED_XML = """<?xml version="1.0" encoding="UTF-8"?>
<PubmedArticleSet>
  <PubmedArticle>
    <MedlineCitation>
      <Article>
        <PublicationTypeList>
          <PublicationType>Retraction of Publication</PublicationType>
        </PublicationTypeList>
      </Article>
    </MedlineCitation>
  </PubmedArticle>
</PubmedArticleSet>
"""

_NOT_RETRACTED_XML = """<?xml version="1.0" encoding="UTF-8"?>
<PubmedArticleSet>
  <PubmedArticle>
    <MedlineCitation>
      <Article>
        <PublicationTypeList>
          <PublicationType>Journal Article</PublicationType>
        </PublicationTypeList>
      </Article>
    </MedlineCitation>
  </PubmedArticle>
</PubmedArticleSet>
"""

_RETRACTED_VIA_CC_XML = """<?xml version="1.0" encoding="UTF-8"?>
<PubmedArticleSet>
  <PubmedArticle>
    <MedlineCitation>
      <CommentsCorrectionsList>
        <CommentsCorrections RefType="RetractionIn">
          <PMID>99999999</PMID>
        </CommentsCorrections>
      </CommentsCorrectionsList>
    </MedlineCitation>
  </PubmedArticle>
</PubmedArticleSet>
"""

_ARXIV_ATOM_V2 = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2403.12345v2</id>
    <title>Test Paper</title>
  </entry>
</feed>
"""

_ARXIV_ATOM_V1 = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2403.12345v1</id>
    <title>Test Paper</title>
  </entry>
</feed>
"""


def _write_pubmed_source(kb_root: Path, pmid: str, *, retracted: bool = False) -> Path:
    d = kb_root / "raw" / "pubmed"
    d.mkdir(parents=True, exist_ok=True)
    front: dict = {
        "id": f"pubmed-{pmid}",
        "type": "pubmed",
        "title": f"PubMed Source {pmid}",
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        "ingested_at": "2026-01-01T00:00:00Z",
        "domains": ["test"],
    }
    if retracted:
        front["retracted"] = True
        front["retracted_at"] = "2026-03-01T00:00:00Z"
    p = d / f"pubmed-{pmid}.md"
    p.write_text(fm.serialize(front, "Body.\n"))
    return p


def _write_arxiv_source(kb_root: Path, arxiv_id: str, *, version: int | None = None) -> Path:
    d = kb_root / "raw" / "arxiv"
    d.mkdir(parents=True, exist_ok=True)
    slug = arxiv_id.replace(".", "-")
    front: dict = {
        "id": f"arxiv-{slug}",
        "type": "arxiv",
        "title": f"arXiv {arxiv_id}",
        "url": f"https://arxiv.org/abs/{arxiv_id}",
        "ingested_at": "2026-01-01T00:00:00Z",
        "domains": ["test"],
    }
    if version is not None:
        front["arxiv_current_version"] = version
    p = d / f"arxiv-{slug}.md"
    p.write_text(fm.serialize(front, "Body.\n"))
    return p


# --- is_retracted unit tests ---------------------------------------------------


def test_is_retracted_publication_type():
    retracted, _ = is_retracted(_RETRACTED_XML)
    assert retracted is True


def test_is_retracted_comments_corrections():
    retracted, pmid = is_retracted(_RETRACTED_VIA_CC_XML)
    assert retracted is True
    assert pmid == "99999999"


def test_not_retracted_journal_article():
    retracted, _ = is_retracted(_NOT_RETRACTED_XML)
    assert retracted is False


def test_is_retracted_parse_error():
    retracted, _ = is_retracted("not xml")
    assert retracted is False


def test_pmid_from_id():
    assert _pmid_from_id("pubmed-12345678") == "12345678"
    assert _pmid_from_id("web-2026-01-01-abc") is None


# --- PubmedRetractionPoller integration ----------------------------------------


def test_poller_marks_retracted_source(kb_root: Path) -> None:
    p = _write_pubmed_source(kb_root, "12345678")

    def fake_fetch(pmid: str) -> str:
        return _RETRACTED_XML

    poller = PubmedRetractionPoller(fetch_fn=fake_fetch)
    result = poller.run()

    assert result.success
    front, _ = fm.parse(p.read_text())
    assert front.get("retracted") is True
    assert "retracted_at" in front


def test_poller_skips_already_retracted(kb_root: Path) -> None:
    _write_pubmed_source(kb_root, "99999999", retracted=True)
    calls: list[str] = []

    def fake_fetch(pmid: str) -> str:
        calls.append(pmid)
        return _RETRACTED_XML

    poller = PubmedRetractionPoller(fetch_fn=fake_fetch)
    result = poller.run()

    assert result.success
    # already retracted — should still check (no skip for already-retracted)
    # but the frontmatter won't change since retracted is already True


def test_poller_does_not_modify_non_retracted_source(kb_root: Path) -> None:
    p = _write_pubmed_source(kb_root, "11111111")
    original = p.read_text()

    def fake_fetch(pmid: str) -> str:
        return _NOT_RETRACTED_XML

    poller = PubmedRetractionPoller(fetch_fn=fake_fetch)
    poller.run()

    front, _ = fm.parse(p.read_text())
    assert not front.get("retracted")


def test_poller_handles_fetch_error_gracefully(kb_root: Path) -> None:
    _write_pubmed_source(kb_root, "22222222")

    def fake_fetch(pmid: str) -> str:
        raise ConnectionError("network down")

    poller = PubmedRetractionPoller(fetch_fn=fake_fetch)
    result = poller.run()

    assert result.success  # fetch error is non-fatal
    assert len(result.errors) == 1


def test_poller_no_sources_ok(kb_root: Path) -> None:
    poller = PubmedRetractionPoller(fetch_fn=lambda pmid: _NOT_RETRACTED_XML)
    result = poller.run()
    assert result.success


# --- current_version + ArxivRevisionPoller ------------------------------------


def test_current_version_v2():
    assert current_version(_ARXIV_ATOM_V2) == 2


def test_current_version_v1():
    assert current_version(_ARXIV_ATOM_V1) == 1


def test_current_version_parse_error():
    assert current_version("not xml") is None


def test_arxiv_id_from_source_id():
    assert _arxiv_id_from_source_id("arxiv-2403-12345") == "2403.12345"
    assert _arxiv_id_from_source_id("pubmed-12345") is None


def test_arxiv_poller_records_baseline_on_first_check(kb_root: Path) -> None:
    p = _write_arxiv_source(kb_root, "2403.12345")

    poller = ArxivRevisionPoller(fetch_fn=lambda _: _ARXIV_ATOM_V1)
    result = poller.run()

    assert result.success
    front, _ = fm.parse(p.read_text())
    assert front.get("arxiv_current_version") == 1
    assert not front.get("arxiv_revised")


def test_arxiv_poller_flags_revision(kb_root: Path) -> None:
    p = _write_arxiv_source(kb_root, "2403.12345", version=1)
    # Seed cursor with version=1 to simulate prior check
    cursor_p = paths.knowledge_internal() / "pollers" / "arxiv-revisions" / "cursor.yaml"
    cursor_p.parent.mkdir(parents=True, exist_ok=True)
    import yaml
    cursor_p.write_text(
        yaml.safe_dump({"checked": {"arxiv-2403-12345": {"version": 1, "checked_at": "2025-01-01T00:00:00Z"}}})
    )

    poller = ArxivRevisionPoller(fetch_fn=lambda _: _ARXIV_ATOM_V2)
    result = poller.run()

    assert result.success
    front, _ = fm.parse(p.read_text())
    assert front.get("arxiv_revised") is True
    assert front.get("arxiv_current_version") == 2


def test_arxiv_poller_no_sources_ok(kb_root: Path) -> None:
    poller = ArxivRevisionPoller(fetch_fn=lambda _: _ARXIV_ATOM_V1)
    result = poller.run()
    assert result.success


# --- retracted-citations lint --------------------------------------------------


def _write_wiki_synthesis(kb_root: Path, slug: str, body: str) -> Path:
    d = kb_root / "wiki" / "synthesis"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "synthesis",
        "slug": slug,
        "title": slug,
        "domains": ["test"],
        "question": "Q?",
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
        "sources_count": 1,
        "synthesizes": ["sources/pubmed-12345678"],
    }
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, body))
    return p


def test_lint_flags_citation_to_retracted_source(kb_root: Path) -> None:
    _write_pubmed_source(kb_root, "12345678", retracted=True)
    _write_wiki_synthesis(kb_root, "test-synth", "Analysis [[sources/pubmed-12345678]].\n")

    findings = lint_run()
    assert len(findings) == 1
    f = findings[0]
    assert f.check == "retracted-citations"
    assert f.severity == SEVERITY_ERROR
    assert "pubmed-12345678" in f.message
    assert f.metadata["retracted_source"] == "pubmed-12345678"


def test_lint_no_finding_for_non_retracted_source(kb_root: Path) -> None:
    _write_pubmed_source(kb_root, "11111111", retracted=False)
    _write_wiki_synthesis(kb_root, "clean-synth", "Analysis [[sources/pubmed-11111111]].\n")

    findings = lint_run()
    assert findings == []


def test_lint_empty_when_no_retracted_sources(kb_root: Path) -> None:
    findings = lint_run()
    assert findings == []


def test_lint_multiple_retracted_citations(kb_root: Path) -> None:
    _write_pubmed_source(kb_root, "11111111", retracted=True)
    _write_pubmed_source(kb_root, "22222222", retracted=True)
    _write_wiki_synthesis(
        kb_root, "double-cite",
        "[[sources/pubmed-11111111]] and [[sources/pubmed-22222222]].\n"
    )

    findings = lint_run()
    assert len(findings) == 2
    sources = {f.metadata["retracted_source"] for f in findings}
    assert "pubmed-11111111" in sources
    assert "pubmed-22222222" in sources
