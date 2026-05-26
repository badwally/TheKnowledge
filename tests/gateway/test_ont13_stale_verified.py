"""ONT-13: last_verified_at coverage and staleness check for time-sensitive entities."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths
from gateway.lint import SEVERITY_ERROR, SEVERITY_WARNING
from gateway.lint.stale_verified import STALE_DAYS, run


# --- helpers -------------------------------------------------------------------


def _write_entity(
    kb_root: Path,
    slug: str,
    entity_kind: str,
    *,
    last_verified_at: str | None = None,
    include_field: bool = True,
) -> Path:
    d = kb_root / "wiki" / "entities"
    d.mkdir(parents=True, exist_ok=True)
    front: dict = {
        "type": "entity",
        "slug": slug,
        "canonical_name": slug.replace("-", " ").title(),
        "entity_kind": entity_kind,
        "domains": ["test"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    if include_field and last_verified_at is not None:
        front["last_verified_at"] = last_verified_at
    body = "## Overview\n\nContent [[sources/web-2026-01-01-abc]].\n"
    p = d / f"{slug}.md"
    p.write_text(fm.serialize(front, body))
    return p


def _recent_iso() -> str:
    dt = datetime.now(tz=timezone.utc) - timedelta(days=30)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _stale_iso() -> str:
    dt = datetime.now(tz=timezone.utc) - timedelta(days=STALE_DAYS + 10)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


# --- missing last_verified_at --------------------------------------------------


def test_statute_missing_last_verified_is_error(kb_root: Path) -> None:
    _write_entity(kb_root, "hsa-section-213", "statute", include_field=False)
    findings = run()
    assert len(findings) == 1
    f = findings[0]
    assert f.check == "stale-verified"
    assert f.severity == SEVERITY_ERROR
    assert "statute" in f.message
    assert "hsa-section-213" in f.message or "hsa-section-213" in f.metadata.get("slug", "")


def test_standard_missing_last_verified_is_error(kb_root: Path) -> None:
    _write_entity(kb_root, "iso-9001", "standard", include_field=False)
    findings = run()
    assert len(findings) == 1
    assert findings[0].severity == SEVERITY_ERROR
    assert findings[0].metadata["entity_kind"] == "standard"


def test_other_entity_kinds_not_flagged(kb_root: Path) -> None:
    for kind in ("person", "organization", "drug", "paper", "dataset", "product",
                 "software", "place", "event", "other"):
        _write_entity(kb_root, f"entity-{kind}", kind, include_field=False)
    findings = run()
    assert findings == []


# --- stale last_verified_at ----------------------------------------------------


def test_stale_statute_is_warning(kb_root: Path) -> None:
    _write_entity(kb_root, "old-statute", "statute", last_verified_at=_stale_iso())
    findings = run()
    assert len(findings) == 1
    f = findings[0]
    assert f.check == "stale-verified"
    assert f.severity == SEVERITY_WARNING
    assert f.metadata["days_since_verified"] > STALE_DAYS


def test_stale_standard_is_warning(kb_root: Path) -> None:
    _write_entity(kb_root, "old-standard", "standard", last_verified_at=_stale_iso())
    findings = run()
    assert len(findings) == 1
    assert findings[0].severity == SEVERITY_WARNING


def test_recent_statute_not_flagged(kb_root: Path) -> None:
    _write_entity(kb_root, "fresh-statute", "statute", last_verified_at=_recent_iso())
    findings = run()
    assert findings == []


def test_recent_standard_not_flagged(kb_root: Path) -> None:
    _write_entity(kb_root, "fresh-standard", "standard", last_verified_at=_recent_iso())
    findings = run()
    assert findings == []


# --- boundary: exactly STALE_DAYS old -----------------------------------------


def test_exactly_stale_boundary_is_warning(kb_root: Path) -> None:
    dt = datetime.now(tz=timezone.utc) - timedelta(days=STALE_DAYS + 1)
    _write_entity(kb_root, "boundary-statute", "statute",
                  last_verified_at=dt.strftime("%Y-%m-%dT%H:%M:%SZ"))
    findings = run()
    assert len(findings) == 1
    assert findings[0].severity == SEVERITY_WARNING


def test_just_under_stale_boundary_not_flagged(kb_root: Path) -> None:
    dt = datetime.now(tz=timezone.utc) - timedelta(days=STALE_DAYS - 1)
    _write_entity(kb_root, "near-boundary", "statute",
                  last_verified_at=dt.strftime("%Y-%m-%dT%H:%M:%SZ"))
    findings = run()
    assert findings == []


# --- unparseable value ---------------------------------------------------------


def test_unparseable_last_verified_is_error(kb_root: Path) -> None:
    _write_entity(kb_root, "bad-date-statute", "statute", last_verified_at="not-a-date")
    findings = run()
    assert len(findings) == 1
    assert findings[0].severity == SEVERITY_ERROR
    assert "unparseable" in findings[0].message


# --- mixed pages ---------------------------------------------------------------


def test_mixed_pages_only_flags_statute_standard(kb_root: Path) -> None:
    _write_entity(kb_root, "missing-statute", "statute", include_field=False)
    _write_entity(kb_root, "fresh-drug", "drug", include_field=False)
    _write_entity(kb_root, "stale-standard", "standard", last_verified_at=_stale_iso())
    _write_entity(kb_root, "fresh-statute", "statute", last_verified_at=_recent_iso())
    findings = run()
    assert len(findings) == 2
    checks = {f.metadata["slug"] for f in findings}
    assert "missing-statute" in checks
    assert "stale-standard" in checks


# --- empty dir / no entities ---------------------------------------------------


def test_empty_entity_dir_ok(kb_root: Path) -> None:
    findings = run()
    assert findings == []


def test_no_entity_dir_ok(kb_root: Path) -> None:
    findings = run()
    assert findings == []


# --- metadata fields -----------------------------------------------------------


def test_finding_metadata_contains_expected_fields(kb_root: Path) -> None:
    _write_entity(kb_root, "meta-test", "statute", include_field=False)
    findings = run()
    assert len(findings) == 1
    meta = findings[0].metadata
    assert meta["slug"] == "meta-test"
    assert meta["entity_kind"] == "statute"


def test_stale_finding_metadata_has_days_since_verified(kb_root: Path) -> None:
    _write_entity(kb_root, "days-check", "standard", last_verified_at=_stale_iso())
    findings = run()
    assert len(findings) == 1
    assert "days_since_verified" in findings[0].metadata
    assert findings[0].metadata["days_since_verified"] > STALE_DAYS
