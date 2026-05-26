"""AGT-4: contradiction sweeper — weekly per-domain sweep tests."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest

from gateway import frontmatter as fm, paths
from gateway.lint import LintFinding, SEVERITY_WARNING
from gateway.ops.contradiction_sweeper import (
    _blessed_domains,
    _build_page,
    _page_path,
    _week_str,
    run_contradiction_sweep,
    sweep_domain,
)


# --- helpers ----------------------------------------------------------------


def _make_policy(kb_root: Path, domain: str) -> None:
    p = paths.policies_dir() / domain / "policy.yaml"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"domain:\n  slug: {domain}\n")


def _fake_finding(domain: str, a_slug: str = "concept/foo", b_slug: str = "concept/bar") -> LintFinding:
    return LintFinding(
        check="contradictions",
        severity=SEVERITY_WARNING,
        message=f"contradiction in '{domain}': {a_slug} vs {b_slug}",
        metadata={
            "domain": domain,
            "a_page": a_slug,
            "b_page": b_slug,
            "a_text": "Claim A states X.",
            "b_text": "Claim B states not-X.",
            "rationale": "Directly conflicting empirical claims.",
        },
    )


def _make_stub_client(findings: list[LintFinding]):
    """Return a (mock_gather, mock_client) that produces given findings."""

    class _StubClient:
        def call(self, prompt: str) -> str:
            # return JSON for 1 contradiction pair (indices 1 and 2)
            return '{"contradictions": [{"a": 1, "b": 2, "rationale": "conflict"}]}'

    return _StubClient()


# --- unit tests -------------------------------------------------------------


def test_week_str_format(kb_root: Path) -> None:
    w = _week_str()
    import re
    assert re.match(r"\d{4}-W\d{2}$", w)


def test_page_path_format(kb_root: Path) -> None:
    p = _page_path("glp1", "2026-W22")
    assert p.name == "contradictions-glp1-2026-W22.md"
    assert "synthesis" in str(p)


def test_blessed_domains_empty(kb_root: Path) -> None:
    assert _blessed_domains() == []


def test_blessed_domains_lists_policies(kb_root: Path) -> None:
    _make_policy(kb_root, "alpha")
    _make_policy(kb_root, "beta")
    assert _blessed_domains() == ["alpha", "beta"]


def test_build_page_structure(kb_root: Path) -> None:
    findings = [_fake_finding("alpha")]
    page = _build_page("alpha", "2026-W22", findings)
    front, body = fm.parse(page)
    assert front["type"] == "synthesis"
    assert front["draft"] is True
    assert "2026-W22" in front["title"]
    assert front["domains"] == ["alpha"]
    assert "synthesizes" in front
    assert "## Synthesis" in body
    assert "## Sources cited" in body


# --- sweep_domain tests -----------------------------------------------------


def test_sweep_domain_skips_if_page_exists(kb_root: Path) -> None:
    page = _page_path("alpha", "2026-W01")
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text("---\ntype: synthesis\n---\n# stub\n")

    result = sweep_domain("alpha", week="2026-W01")
    assert result.success
    assert "already exists" in result.summary


def test_sweep_domain_skips_too_few_claims(kb_root: Path) -> None:
    # No wiki pages in this KB → zero claims
    result = sweep_domain("alpha", week="2026-W22")
    assert result.success
    assert "fewer than" in result.summary


def test_sweep_domain_writes_page_on_findings(kb_root: Path) -> None:
    from gateway.lint.contradictions import _Claim
    from unittest.mock import patch

    claims = [
        _Claim(page_type="concept", page_slug="foo", text="X is true."),
        _Claim(page_type="concept", page_slug="bar", text="X is false."),
        _Claim(page_type="concept", page_slug="baz", text="Y holds."),
        _Claim(page_type="concept", page_slug="qux", text="Z holds."),
    ]

    client_mock = MagicMock()
    client_mock.call.return_value = '{"contradictions": [{"a": 1, "b": 2, "rationale": "direct conflict"}]}'

    with patch("gateway.ops.contradiction_sweeper._gather_claims_by_domain", return_value={"alpha": claims}):
        result = sweep_domain("alpha", client=client_mock, week="2026-W22")

    assert result.success
    out = _page_path("alpha", "2026-W22")
    assert out.exists()
    front, body = fm.parse(out.read_text())
    assert front["draft"] is True
    assert front["domains"] == ["alpha"]
    assert "## Synthesis" in body
    assert "## Sources cited" in body


def test_sweep_domain_skips_no_contradictions(kb_root: Path) -> None:
    from gateway.lint.contradictions import _Claim
    from unittest.mock import patch

    claims = [_Claim("concept", f"slug{i}", f"Claim {i}.") for i in range(5)]
    client_mock = MagicMock()
    client_mock.call.return_value = '{"contradictions": []}'

    with patch("gateway.ops.contradiction_sweeper._gather_claims_by_domain", return_value={"alpha": claims}):
        result = sweep_domain("alpha", client=client_mock, week="2026-W22")

    assert result.success
    assert "no contradictions" in result.summary
    assert not _page_path("alpha", "2026-W22").exists()


def test_sweep_domain_returns_error_on_llm_failure(kb_root: Path) -> None:
    from gateway.lint.contradictions import _Claim
    from unittest.mock import patch

    claims = [_Claim("concept", f"slug{i}", f"Claim {i}.") for i in range(5)]
    client_mock = MagicMock()
    client_mock.call.side_effect = RuntimeError("API timeout")

    with patch("gateway.ops.contradiction_sweeper._gather_claims_by_domain", return_value={"alpha": claims}):
        result = sweep_domain("alpha", client=client_mock, week="2026-W22")

    assert not result.success
    assert any("API timeout" in e for e in result.errors)


# --- run_contradiction_sweep tests ------------------------------------------


def test_run_sweep_no_domains(kb_root: Path) -> None:
    result = run_contradiction_sweep()
    assert result.success
    assert "no blessed domains" in result.summary


def test_run_sweep_specific_domain(kb_root: Path) -> None:
    from unittest.mock import patch

    with patch("gateway.ops.contradiction_sweeper.sweep_domain") as mock_sweep:
        mock_sweep.return_value = MagicMock(success=True, summary="swept", errors=[])
        run_contradiction_sweep(domain="alpha", week="2026-W22")
    mock_sweep.assert_called_once_with("alpha", client=None, week="2026-W22")


def test_run_sweep_all_domains_aggregates(kb_root: Path) -> None:
    from unittest.mock import patch

    _make_policy(kb_root, "alpha")
    _make_policy(kb_root, "beta")

    with patch("gateway.ops.contradiction_sweeper.sweep_domain") as mock_sweep:
        mock_sweep.return_value = MagicMock(
            success=True,
            summary="contradiction-sweeper: alpha/2026-W22 — 2 pair(s) → contradictions-alpha-2026-W22.md",
            errors=[],
        )
        result = run_contradiction_sweep(week="2026-W22")

    assert result.success
    assert mock_sweep.call_count == 2
