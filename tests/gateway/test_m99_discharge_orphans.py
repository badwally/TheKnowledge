"""M99: discharge_orphans — batch synthesize wiki pages for orphaned sources."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from gateway import frontmatter as fm, paths
from gateway.core import OperationResult


@pytest.fixture(autouse=True)
def patch_nlm_notebook(monkeypatch):
    """Stub out nlm_registry.get_persistent so all tests see a registered notebook.

    Without this, the pre-flight notebook check added to discharge_orphans()
    would fail in the clean kb_root environment (no real notebooks.yaml).
    Tests that explicitly test the 'no notebook' path override this fixture.
    """
    monkeypatch.setattr("gateway.nlm_registry.get_persistent", lambda domain: "fake-nb-id")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _write_raw_source(
    kb_root: Path,
    *,
    source_type: str = "web",
    slug: str = "test-src",
    domain: str = "glp1",
    wiki_pages: list[str] | None = None,
    title: str = "Test source",
) -> Path:
    d = paths.raw_dir() / source_type
    d.mkdir(parents=True, exist_ok=True)
    front: dict = {
        "id": slug,
        "type": source_type,
        "title": title,
        "domains": [domain],
        "ingested_at": "2026-01-01T00:00:00Z",
    }
    if wiki_pages is not None:
        front["wiki_pages"] = wiki_pages
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, "Source body.\n"))
    return p


def _ok_result(**kwargs) -> OperationResult:
    defaults = dict(success=True, summary="Wrote draft: wiki/synthesis/ans.md", data={})
    defaults.update(kwargs)
    return OperationResult(**defaults)


# ---------------------------------------------------------------------------
# Core logic tests
# ---------------------------------------------------------------------------


def test_discharges_orphan_source(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(kb_root, slug="orphan-1", domain="glp1", wiki_pages=None)

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", limit=5)

    assert result.success
    assert "1 synthesis drafts filed" in result.summary
    mock_q.assert_called_once()
    call_kwargs = mock_q.call_args
    assert call_kwargs.kwargs["domain"] == "glp1"
    assert call_kwargs.kwargs["draft"] is True


def test_skips_covered_sources(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(
        kb_root, slug="covered-src", domain="glp1",
        wiki_pages=["wiki/synthesis/existing.md"]
    )

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", limit=5)

    assert result.success
    assert "no orphan sources found" in result.summary
    mock_q.assert_not_called()


def test_filters_by_domain(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(kb_root, slug="glp1-src", domain="glp1")
    _write_raw_source(kb_root, slug="other-src", domain="other-domain")

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", limit=5)

    assert mock_q.call_count == 1


def test_respects_limit(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    for i in range(5):
        _write_raw_source(kb_root, slug=f"src-{i}", domain="glp1")

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", limit=3)

    assert mock_q.call_count == 3
    assert "3 synthesis drafts filed" in result.summary


def test_dry_run_does_not_call_query(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(kb_root, slug="dry-src", domain="glp1")

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", dry_run=True)

    mock_q.assert_not_called()
    assert "dry-run" in result.summary
    assert "1 synthesis drafts filed" in result.summary


def test_no_orphans_returns_success(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    result = discharge_orphans("glp1")

    assert result.success
    assert "no orphan sources found" in result.summary


def test_empty_domain_returns_error(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    result = discharge_orphans("")

    assert not result.success
    assert "domain is required" in result.errors[0]


def test_no_notebook_for_domain_fails_fast(kb_root: Path, monkeypatch) -> None:
    """Pre-flight: domain with no registered NLM notebook fails before querying sources."""
    from gateway.ops.discharge_orphans import discharge_orphans

    monkeypatch.setattr("gateway.nlm_registry.get_persistent", lambda domain: None)
    _write_raw_source(kb_root, slug="orphan-x", domain="glp1")

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", limit=5)

    assert not result.success
    assert "no notebook" in result.errors[0]
    mock_q.assert_not_called()


def test_dry_run_includes_auth_not_validated_note(kb_root: Path) -> None:
    """Dry-run summary notes that NLM auth is NOT validated."""
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(kb_root, slug="dry-src-2", domain="glp1")

    with patch("gateway.ops.query.query", return_value=_ok_result()):
        result = discharge_orphans("glp1", dry_run=True)

    assert "NLM auth not validated" in result.summary


def test_query_failure_recorded_in_errors(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(kb_root, slug="fail-src", domain="glp1")
    fail = OperationResult(success=False, summary="NLM error", data={}, errors=["timeout"])

    with patch("gateway.ops.query.query", return_value=fail):
        result = discharge_orphans("glp1")

    assert not result.success
    assert "0 synthesis drafts filed" in result.summary
    assert len(result.errors) == 1


# ---------------------------------------------------------------------------
# _synthesis_question quality (M100)
# ---------------------------------------------------------------------------


def test_synthesis_question_uses_preview_and_domain_topic() -> None:
    from gateway.ops.discharge_orphans import _synthesis_question

    source = {
        "title": "Efficacy of semaglutide in reward circuits",
        "preview": "A 24-week RCT measuring GLP-1 receptor agonist effects on dopamine response.",
    }
    q = _synthesis_question(source, domain_topic="GLP-1 pharmacology and reward modulation")
    assert "GLP-1 pharmacology" in q
    assert "24-week RCT" in q
    assert "Efficacy of semaglutide" in q


def test_synthesis_question_preview_without_domain_topic() -> None:
    from gateway.ops.discharge_orphans import _synthesis_question

    source = {
        "title": "Edge inference for agentic systems",
        "preview": "Survey of on-device LLM deployment patterns.",
    }
    q = _synthesis_question(source)
    assert "Survey of on-device" in q
    assert "Edge inference" in q
    assert "in the context of" not in q


def test_synthesis_question_domain_topic_without_preview() -> None:
    from gateway.ops.discharge_orphans import _synthesis_question

    source = {"title": "Model compression techniques", "preview": ""}
    q = _synthesis_question(source, domain_topic="Edge AI and model optimization")
    assert "Edge AI" in q
    assert "Model compression" in q
    assert "contribute" in q


def test_synthesis_question_falls_back_gracefully() -> None:
    from gateway.ops.discharge_orphans import _synthesis_question

    source = {"title": "Some paper", "preview": ""}
    q = _synthesis_question(source)
    assert "Some paper" in q
    assert "domain's understanding" in q


def test_source_preview_uses_meta_abstract() -> None:
    from gateway.ops.discharge_orphans import _source_preview

    front = {"meta": {"abstract": "A study of dopamine."}}
    assert _source_preview(front, "body content") == "A study of dopamine."


def test_source_preview_uses_meta_excerpt() -> None:
    from gateway.ops.discharge_orphans import _source_preview

    front = {"meta": {"excerpt": "Article about edge AI."}}
    assert _source_preview(front, "body content") == "Article about edge AI."


def test_source_preview_falls_back_to_body() -> None:
    from gateway.ops.discharge_orphans import _source_preview

    front = {"meta": {}}
    assert _source_preview(front, "Body paragraph here.") == "Body paragraph here."


def test_source_preview_prefers_abstract_over_excerpt() -> None:
    from gateway.ops.discharge_orphans import _source_preview

    front = {"meta": {"abstract": "The abstract.", "excerpt": "The excerpt."}}
    assert _source_preview(front, "") == "The abstract."


def test_discharge_orphans_uses_domain_policy(kb_root: Path) -> None:
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(kb_root, slug="policy-src", domain="glp1")

    captured: list[str] = []

    def fake_query(question: str, **kwargs):
        captured.append(question)
        return _ok_result()

    with patch("gateway.ops.query.query", side_effect=fake_query):
        with patch("gateway.ops.discharge_orphans.policy_exists", return_value=True):
            with patch("gateway.ops.discharge_orphans.load_policy") as mock_lp:
                from unittest.mock import MagicMock
                pol = MagicMock()
                pol.domain_topic = "GLP-1 receptor pharmacology"
                mock_lp.return_value = pol
                result = discharge_orphans("glp1", limit=1)

    assert result.success
    assert len(captured) == 1
    assert "GLP-1 receptor pharmacology" in captured[0]


# ---------------------------------------------------------------------------
# CLI wiring
# ---------------------------------------------------------------------------


def test_cli_parser_discharge_orphans() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["routine", "discharge-orphans", "--domain", "glp1"])
    assert ns.domain == "glp1"
    assert ns.limit == 10
    assert ns.dry_run is False


def test_cli_parser_discharge_orphans_limit() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["routine", "discharge-orphans", "--domain", "glp1", "--limit", "5"])
    assert ns.limit == 5


def test_cli_parser_discharge_orphans_dry_run() -> None:
    from gateway.cli import build_parser

    parser = build_parser()
    ns = parser.parse_args(["routine", "discharge-orphans", "--domain", "glp1", "--dry-run"])
    assert ns.dry_run is True


# ---------------------------------------------------------------------------
# M110: skip sources already cited in existing synthesis pages
# ---------------------------------------------------------------------------


def test_skips_source_already_cited_in_synthesis(kb_root: Path) -> None:
    """Source cited in existing synthesis page is excluded, not re-discharged."""
    from gateway.ops.discharge_orphans import discharge_orphans

    source_id = "web/already-cited-src"
    _write_raw_source(kb_root, slug="already-cited-src", domain="glp1", wiki_pages=None)

    # Create a synthesis page that cites this source.
    synthesis_dir = paths.knowledge_root() / "wiki" / "synthesis"
    synthesis_dir.mkdir(parents=True, exist_ok=True)
    (synthesis_dir / "existing-synth.md").write_text(
        f"Some synthesis content.\n- [[sources/{source_id}]]\n"
    )

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", limit=5)

    assert result.success
    assert "no orphan sources found" in result.summary
    mock_q.assert_not_called()


def test_skips_cited_excludes_only_cited_sources(kb_root: Path) -> None:
    """Cited source is excluded; uncited source is still discharged."""
    from gateway.ops.discharge_orphans import discharge_orphans

    _write_raw_source(kb_root, slug="cited-src", domain="glp1", wiki_pages=None)
    _write_raw_source(kb_root, slug="orphan-new", domain="glp1", wiki_pages=None)

    synthesis_dir = paths.knowledge_root() / "wiki" / "synthesis"
    synthesis_dir.mkdir(parents=True, exist_ok=True)
    (synthesis_dir / "existing.md").write_text(
        "Content.\n- [[sources/web/cited-src]]\n"
    )

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", limit=5)

    assert result.success
    assert "1 synthesis drafts filed" in result.summary
    mock_q.assert_called_once()


def test_dry_run_excludes_cited_sources(kb_root: Path) -> None:
    """Dry-run count reflects cited-filter: already-cited sources not counted."""
    from gateway.ops.discharge_orphans import discharge_orphans

    for i in range(3):
        _write_raw_source(kb_root, slug=f"src-{i}", domain="glp1", wiki_pages=None)

    synthesis_dir = paths.knowledge_root() / "wiki" / "synthesis"
    synthesis_dir.mkdir(parents=True, exist_ok=True)
    (synthesis_dir / "existing.md").write_text(
        "Content.\n- [[sources/web/src-0]]\n- [[sources/web/src-1]]\n"
    )

    with patch("gateway.ops.query.query", return_value=_ok_result()) as mock_q:
        result = discharge_orphans("glp1", limit=10, dry_run=True)

    mock_q.assert_not_called()
    assert "1 synthesis drafts filed" in result.summary  # only src-2 is uncited


def test_cli_discharge_orphans_calls_op(kb_root: Path) -> None:
    from gateway.cli import _run_routine_cmd
    import argparse

    ns = argparse.Namespace(
        subcommand="routine",
        routine_name="discharge-orphans",
        domain="glp1",
        limit=5,
        dry_run=True,
    )
    with patch("gateway.ops.discharge_orphans.discharge_orphans", return_value=_ok_result()) as mock_op:
        rc = _run_routine_cmd(ns)

    mock_op.assert_called_once_with("glp1", limit=5, dry_run=True)
    assert rc == 0
