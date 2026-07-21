"""Tests for G2 reversal/anomaly detectors.

RED-before-GREEN: these tests are written before the implementation.
Mirrors the provenance.alarms() pattern (Phase-4 A7):
  - pure function over a snapshot dict
  - named negative controls
  - min_volume floor so a tiny sample can't trip a rate
  - frozen Alarm dataclass with name/value/threshold/tripped/detail
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone

import pytest

from gateway import contradictions_log
from gateway import frontmatter as fm
from gateway import paths
from gateway.reversal_detectors import Alarm, build_snapshot, detect
from gateway.ops.lint import lint


# ---------------------------------------------------------------------------
# Realistic-fixture helpers (mirror test_retraction_cascade.py)
# ---------------------------------------------------------------------------

def _synth(slug: str, synthesizes: list[str]) -> None:
    d = paths.wiki_dir() / "synthesis"
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
        f"# {slug}\n\n## Included works\n"
        + "".join(f"- [[{s}]]\n" for s in synthesizes)
        + f"\n## Analysis\n\nLoad-bearing claim [[{synthesizes[0]}]].\n"
    )
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


def _raw_source(
    source_id: str,
    *,
    source_type: str = "pubmed",
    domains: list[str] | None = None,
    retracted: bool = False,
) -> None:
    """Write a minimal raw/<type>/<id>.md with a real domains: list."""
    raw_dir = paths.raw_dir() / source_type
    raw_dir.mkdir(parents=True, exist_ok=True)
    front = {
        "type": source_type,
        "id": source_id,
        "title": f"Paper {source_id}",
        "domains": list(domains) if domains is not None else ["med"],
        "created_at": "2026-01-01T00:00:00Z",
    }
    if retracted:
        front["retracted"] = True
    body = f"# Paper {source_id}\n\nAbstract content.\n"
    (raw_dir / f"{source_id}.md").write_text(fm.serialize(front, body))


def _recent_iso(days_ago: int = 1) -> str:
    """A resolution timestamp inside build_snapshot's 30-day window, relative to now.

    build_snapshot() only counts acts with resolved_at >= now - window_days (30).
    A FIXED fixture date silently ages out once wall-clock passes it — the acts then
    read as zero and every count-based assertion fails on a date that has nothing to
    do with the behavior under test. Anchoring the fixture to `now` matches the
    wall-clock-relative production window, so the tests stay valid regardless of when
    the suite runs.
    """
    return (datetime.now(timezone.utc) - timedelta(days=days_ago)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def _write_act(
    *,
    act_id: str,
    winner_source: str,
    loser_source: str,
    reverted: bool = False,
    resolved_at: str | None = None,
) -> None:
    """Append a realistic resolution act to the temp-root act log."""
    resolved_at = resolved_at or _recent_iso()
    acts_path = contradictions_log.resolution_acts_path()
    acts_path.parent.mkdir(parents=True, exist_ok=True)
    act = {
        "act_id": act_id,
        "rule": "trust-tier-then-recency",
        "policy_version": "contradiction-policy-v1",
        "inputs": {
            "a": {"source": winner_source, "claim": "x"},
            "b": {"source": loser_source, "claim": "y"},
        },
        "winner": {"source": winner_source, "claim": "x", "trust": 0.9},
        "loser": {"source": loser_source, "claim": "y", "trust": 0.5},
        "resolved_at": resolved_at,
    }
    if reverted:
        act["reverts_act"] = f"reverting-intent-{act_id}"
    with acts_path.open("a") as f:
        f.write(json.dumps(act) + "\n")


# ---------------------------------------------------------------------------
# Detector 1 — auto_resolution_reversal_rate (>5%, min_volume floor)
# ---------------------------------------------------------------------------

def test_reversal_rate_trips_above_5pct(kb_root):
    """6 reversals out of 100 auto-resolutions → 6% > 5% threshold → tripped."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 6,
        "cross_project": 0,
        "total": 100,
        "max_cascade_depth": 1,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["auto_resolution_reversal_rate"].tripped is True


def test_reversal_rate_at_threshold_does_not_trip(kb_root):
    """Exactly 5% (5/100) is at the threshold, not above it — must not trip."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 5,
        "cross_project": 0,
        "total": 100,
        "max_cascade_depth": 1,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["auto_resolution_reversal_rate"].tripped is False


def test_below_min_volume_cannot_trip_rate(kb_root):
    """2 reversals out of 3 auto-resolutions = 67%, but below min_volume → no alarm.

    Named negative control: min_volume floor prevents noise from tiny samples.
    """
    snap = {
        "auto_resolutions": 3,
        "reversed": 2,
        "cross_project": 0,
        "total": 3,
        "max_cascade_depth": 1,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["auto_resolution_reversal_rate"].tripped is False  # min_volume floor


# ---------------------------------------------------------------------------
# Detector 2 — cross_project_override_rate (>10%, min_volume floor)
# ---------------------------------------------------------------------------

def test_cross_project_rate_trips_above_10pct(kb_root):
    """11 cross-project overrides out of 100 total → 11% > 10% → tripped."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 0,
        "cross_project": 11,
        "total": 100,
        "max_cascade_depth": 1,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["cross_project_override_rate"].tripped is True


def test_cross_project_rate_at_threshold_does_not_trip(kb_root):
    """Exactly 10% is at the threshold, not above — must not trip."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 0,
        "cross_project": 10,
        "total": 100,
        "max_cascade_depth": 1,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["cross_project_override_rate"].tripped is False


def test_cross_project_below_min_volume_cannot_trip(kb_root):
    """Named negative control: cross_project rate with total < min_volume → no alarm."""
    snap = {
        "auto_resolutions": 3,
        "reversed": 0,
        "cross_project": 2,
        "total": 3,
        "max_cascade_depth": 1,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["cross_project_override_rate"].tripped is False


# ---------------------------------------------------------------------------
# Detector 3 — observed_cascade_depth (>3)
# ---------------------------------------------------------------------------

def test_cascade_depth_trips_above_3(kb_root):
    """Max cascade depth of 4 > threshold of 3 → tripped."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 0,
        "cross_project": 0,
        "total": 100,
        "max_cascade_depth": 4,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["observed_cascade_depth"].tripped is True


def test_cascade_depth_at_threshold_does_not_trip(kb_root):
    """Depth exactly 3 is at the threshold, not above — must not trip."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 0,
        "cross_project": 0,
        "total": 100,
        "max_cascade_depth": 3,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["observed_cascade_depth"].tripped is False


# ---------------------------------------------------------------------------
# Healthy traffic → no alarms (named negative control)
# ---------------------------------------------------------------------------

def test_healthy_traffic_trips_nothing(kb_root):
    """Named negative control: healthy traffic trips none of the three detectors.

    1 reversal / 100 = 1% < 5%; 2 cross-project / 100 = 2% < 10%; depth 2 < 3.
    """
    snap = {
        "auto_resolutions": 100,
        "reversed": 1,
        "cross_project": 2,
        "total": 100,
        "max_cascade_depth": 2,
    }
    assert all(not a.tripped for a in detect(snap))


# ---------------------------------------------------------------------------
# Alarm dataclass shape
# ---------------------------------------------------------------------------

def test_alarm_is_frozen_dataclass_with_required_fields(kb_root):
    """Alarm must expose name, value, threshold, tripped, detail."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 6,
        "cross_project": 0,
        "total": 100,
        "max_cascade_depth": 1,
    }
    alarms = detect(snap)
    assert len(alarms) == 3  # exactly three detectors
    for a in alarms:
        assert hasattr(a, "name")
        assert hasattr(a, "value")
        assert hasattr(a, "threshold")
        assert hasattr(a, "tripped")
        assert hasattr(a, "detail")
        # Frozen: attempting mutation must raise
        with pytest.raises((AttributeError, TypeError)):
            a.name = "mutated"  # type: ignore[misc]


def test_detect_always_returns_all_three_alarms(kb_root):
    """detect() always returns 3 Alarm objects regardless of trips."""
    snap = {
        "auto_resolutions": 0,
        "reversed": 0,
        "cross_project": 0,
        "total": 0,
        "max_cascade_depth": 0,
    }
    alarms = detect(snap)
    names = {a.name for a in alarms}
    assert names == {
        "auto_resolution_reversal_rate",
        "cross_project_override_rate",
        "observed_cascade_depth",
    }


# ---------------------------------------------------------------------------
# Step 6 — lint wiring: reversal-anomalies scope check
# ---------------------------------------------------------------------------

def test_lint_reversal_anomalies_scope_runs_without_error(kb_root):
    """reversal-anomalies is a registered lint check that runs cleanly (no exceptions)."""
    res = lint(scope="reversal-anomalies")
    assert res.success is True


def test_lint_reversal_anomalies_no_findings_on_empty_act_log(kb_root):
    """Empty act log → no tripped alarms → no lint findings."""
    # Act log doesn't exist in the fresh kb_root → snapshot is all-zero → no trips
    res = lint(scope="reversal-anomalies")
    assert res.success is True
    # Summary should show 0 findings for this check
    assert "reversal-anomalies: 0" in res.summary or "0 finding" in res.summary


def test_lint_reversal_anomalies_emits_finding_when_reversal_rate_tripped(kb_root):
    """When reversal rate is above 5% (via realistic acts + revert markers), a finding is emitted."""
    # Write 10 resolution acts — above min_volume=10 — then mark 2 as reverted → 20% > 5%
    acts_path = contradictions_log.resolution_acts_path()
    acts_path.parent.mkdir(parents=True, exist_ok=True)
    for i in range(10):
        act = {
            "act_id": f"act-{i:04d}",
            "rule": "trust-tier-then-recency",
            "policy_version": "contradiction-policy-v1",
            "inputs": {"a": {"source": f"pubmed-{i}", "claim": "x"},
                       "b": {"source": f"arxiv-{i}", "claim": "y"}},
            "winner": {"source": f"pubmed-{i}", "claim": "x", "trust": 0.9},
            "loser": {"source": f"arxiv-{i}", "claim": "y", "trust": 0.5},
            "resolved_at": _recent_iso(),
        }
        # Mark 2 of the acts as reverted (20% reversal rate)
        if i < 2:
            act["reverts_act"] = f"reverting-intent-{i}"
        acts_path.open("a").write(json.dumps(act) + "\n")

    res = lint(scope="reversal-anomalies")
    assert res.success is True
    # Exactly one finding: the tripped auto_resolution_reversal_rate detector.
    # The lint summary lists per-check counts as "<check>: <n>" only when n > 0.
    assert "reversal-anomalies: 1" in res.summary
    # And the detector name is carried in the written report finding message.
    report_path = res.paths_touched[0]
    assert "auto_resolution_reversal_rate" in report_path.read_text()


def test_lint_reversal_anomalies_scope_runs_only_that_check(kb_root):
    """Scoped lint run executes ONLY reversal-anomalies, not any other check."""
    res = lint(scope="reversal-anomalies")
    assert res.success is True
    # The summary/counts must not mention other checks like orphans or schema-drift
    assert "orphans" not in res.summary
    assert "schema-drift" not in res.summary


# ===========================================================================
# build_snapshot — LIVE signals over real data (review fixes)
# ===========================================================================

# --- CRITICAL: cascade-depth computed LIVE from the real retraction graph ---

def test_build_snapshot_cascade_depth_live_from_retraction_chain(kb_root):
    """A real source→A→B retraction chain yields observed cascade depth ≥ 2.

    Drives retraction.cascade over the actual graph — no fabricated sidecar.
    Detector must TRIP (depth 2 ... but we want > threshold(3), so build a
    deeper chain): source -> a -> b -> c -> d gives depth 4 > 3.
    """
    _raw_source("pubmed-1", retracted=True)
    _synth("a", ["sources/pubmed-1"])
    _synth("b", ["synthesis/a"])
    _synth("c", ["synthesis/b"])
    _synth("d", ["synthesis/c"])
    snap = build_snapshot()
    assert snap["max_cascade_depth"] >= 4
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["observed_cascade_depth"].tripped is True


def test_build_snapshot_cascade_depth_shallow_does_not_trip(kb_root):
    """A shallow retraction graph (depth 1) does not trip the cascade detector."""
    _raw_source("pubmed-9", retracted=True)
    _synth("only", ["sources/pubmed-9"])  # depth 1
    snap = build_snapshot()
    assert snap["max_cascade_depth"] <= 3
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["observed_cascade_depth"].tripped is False


def test_build_snapshot_no_retractions_cascade_depth_zero(kb_root):
    """Named negative control: no retracted sources → cascade depth 0 → no trip."""
    snap = build_snapshot()
    assert snap["max_cascade_depth"] == 0
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["observed_cascade_depth"].tripped is False


# --- IMPORTANT 2: cross-project resolves REAL wiki domains, not id prefixes ---

def test_cross_project_trips_on_real_different_domains(kb_root):
    """Two sources in genuinely different wiki domains → cross-project counts."""
    # 11 acts, each winner in domain 'med', loser in domain 'finance' → 100% cross-project
    for i in range(11):
        _raw_source(f"pubmed-w{i}", source_type="pubmed", domains=["med"])
        _raw_source(f"pubmed-l{i}", source_type="pubmed", domains=["finance"])
        _write_act(act_id=f"act-x{i}", winner_source=f"pubmed-w{i}",
                   loser_source=f"pubmed-l{i}")
    snap = build_snapshot()
    assert snap["cross_project"] == 11
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["cross_project_override_rate"].tripped is True


def test_cross_project_same_domain_different_source_type_does_not_count(kb_root):
    """Named negative control: same domain across different SOURCE TYPES is NOT cross-project.

    The old prefix heuristic falsely treated pubmed-vs-arxiv as cross-project even
    in the same project. With real-domain resolution, both in 'med' → 0 cross-project.
    """
    for i in range(11):
        _raw_source(f"pubmed-{i}", source_type="pubmed", domains=["med"])
        _raw_source(f"arxiv-{i}", source_type="arxiv", domains=["med"])
        _write_act(act_id=f"act-s{i}", winner_source=f"pubmed-{i}",
                   loser_source=f"arxiv-{i}")
    snap = build_snapshot()
    assert snap["cross_project"] == 0
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["cross_project_override_rate"].tripped is False


def test_cross_project_unresolvable_domain_excluded(kb_root):
    """A source whose domain can't be resolved is EXCLUDED (under-detect honestly)."""
    # winner has a real domain; loser source file does not exist → exclude the act
    _raw_source("pubmed-real", source_type="pubmed", domains=["med"])
    _write_act(act_id="act-u1", winner_source="pubmed-real",
               loser_source="pubmed-missing")
    snap = build_snapshot()
    assert snap["cross_project"] == 0  # excluded, not guessed


# --- IMPORTANT 1: reversal counted SOLELY via reverts_act ---

def test_reversal_counted_only_via_reverts_act(kb_root):
    """reversal_type on an act is NOT counted (dead schema arm removed)."""
    # 10 acts; one carries a bogus reversal_type (intent-queue field, not an act field)
    for i in range(10):
        _raw_source(f"pubmed-r{i}", source_type="pubmed", domains=["med"])
        _write_act(act_id=f"act-r{i}", winner_source=f"pubmed-r{i}",
                   loser_source=f"pubmed-r{i}")
    # Inject a non-reverts_act act carrying reversal_type — must NOT count
    acts_path = contradictions_log.resolution_acts_path()
    bogus = {
        "act_id": "act-bogus",
        "rule": "trust-tier-then-recency",
        "policy_version": "contradiction-policy-v1",
        "inputs": {"a": {"source": "pubmed-r0", "claim": "x"},
                   "b": {"source": "pubmed-r0", "claim": "y"}},
        "winner": {"source": "pubmed-r0", "claim": "x", "trust": 0.9},
        "loser": {"source": "pubmed-r0", "claim": "y", "trust": 0.5},
        "resolved_at": _recent_iso(),
        "reversal_type": "contradiction-resolution",  # NOT a real act field
    }
    with acts_path.open("a") as f:
        f.write(json.dumps(bogus) + "\n")
    snap = build_snapshot()
    assert snap["reversed"] == 0  # reversal_type ignored; only reverts_act counts


def test_reverts_act_marker_counts_as_reversal(kb_root):
    """A real reverts_act marker (T1's mark_act_reverted) IS counted."""
    for i in range(10):
        _raw_source(f"pubmed-c{i}", source_type="pubmed", domains=["med"])
        _write_act(act_id=f"act-c{i}", winner_source=f"pubmed-c{i}",
                   loser_source=f"pubmed-c{i}", reverted=(i < 2))
    snap = build_snapshot()
    assert snap["reversed"] == 2


# --- isolation: act-log writes + reads stay under kb_root temp ---

def test_build_snapshot_reads_only_temp_root(kb_root):
    """The act log under the kb_root fixture must resolve to the temp dir, not prod."""
    acts_path = contradictions_log.resolution_acts_path()
    assert str(kb_root) in str(acts_path)
    # And build_snapshot, reading via the same helper, sees only what we wrote here
    _raw_source("pubmed-iso", source_type="pubmed", domains=["med"])
    _write_act(act_id="act-iso", winner_source="pubmed-iso", loser_source="pubmed-iso")
    snap = build_snapshot()
    assert snap["auto_resolutions"] == 1
