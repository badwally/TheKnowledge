"""G2 — reversal / anomaly detectors for the auto-resolution + cascade paths.

Mirrors the Phase-4 A7 ``provenance.alarms()`` pattern exactly:
  - Pure function over a snapshot dict — no I/O, fully replayable.
  - Named negative controls in the test suite (healthy traffic + below-min-volume).
  - ``min_volume`` floor so a tiny sample cannot trip a rate alarm.

The detectors populate the §1.5 Option-B gating signals that tell the operator
when automatic transitive cascade-revert (Option B) needs to be built:

  ``reversal.auto_resolution_reversal_rate``  — >5 % reverted in window
  ``reversal.cross_project_override_rate``    — >10 % cross-project overrides
  ``reversal.observed_cascade_depth``         — max cascade depth >3

Snapshot schema (built from the real act log + cascade history by the lint
wiring in ``ops/lint.py``):

  {
    "auto_resolutions": int,   # total auto-resolutions in the window
    "reversed":         int,   # how many were subsequently reverted
    "cross_project":    int,   # resolutions where loser.domain != winner.domain
    "total":            int,   # same as auto_resolutions (kept symmetric)
    "max_cascade_depth": int,  # max CascadeResult.depth observed in window
  }

Real act-log fields (verified from contradictions_log.py + ops/contradiction.py):
  act_id, rule, policy_version, inputs, winner, loser, resolved_at
  + ``reverts_act`` (str) added by mark_act_reverted() when reversed — this is
    the reversal marker T1 writes.

Cross-project detection: a resolution act where
  winner["source_domain"] != loser["source_domain"]  (if populated by T1)
  OR where the source-ID prefixes differ across project/domain boundaries.

Cascade depth: CascadeResult.depth from retraction.cascade() (T1).
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from gateway import contradictions_log


# ---------------------------------------------------------------------------
# Thresholds — §1.5 Option-B gating signals
# ---------------------------------------------------------------------------

ALARM_THRESHOLDS: dict[str, Any] = {
    "auto_resolution_reversal_rate": 0.05,   # >5 %
    "cross_project_override_rate": 0.10,     # >10 %
    "observed_cascade_depth": 3,             # >3
    "min_volume": 10,                        # below this, rate alarms are suppressed
}


# ---------------------------------------------------------------------------
# Alarm dataclass — mirrors the A7 pattern; frozen so it's replayable
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Alarm:
    """A single detector result.

    Attributes
    ----------
    name       : detector slug (matches §1.5 signal names)
    value      : measured value (rate 0-1 or integer for depth)
    threshold  : the configured threshold this is compared against
    tripped    : True when ``value > threshold`` AND volume requirements met
    detail     : dict with supporting counts/metadata for the operator
    """
    name: str
    value: float
    threshold: float
    tripped: bool
    detail: dict


# ---------------------------------------------------------------------------
# Detector implementation
# ---------------------------------------------------------------------------

def detect(
    snapshot: dict,
    *,
    window_days: int = 30,
    thresholds: dict[str, Any] | None = None,
) -> list[Alarm]:
    """Run all three reversal/anomaly detectors over a snapshot.

    Always returns exactly three ``Alarm`` objects (one per detector),
    regardless of how many trip. Pure over the snapshot — no I/O.

    Parameters
    ----------
    snapshot    : dict with keys ``auto_resolutions``, ``reversed``,
                  ``cross_project``, ``total``, ``max_cascade_depth``.
    window_days : informational — callers build the snapshot over this window.
    thresholds  : optional override dict (same keys as ``ALARM_THRESHOLDS``).
    """
    th = {**ALARM_THRESHOLDS, **(thresholds or {})}
    min_vol = th["min_volume"]

    auto_resolutions = int(snapshot.get("auto_resolutions", 0))
    reversed_count = int(snapshot.get("reversed", 0))
    cross_project = int(snapshot.get("cross_project", 0))
    total = int(snapshot.get("total", 0))
    max_cascade_depth = int(snapshot.get("max_cascade_depth", 0))

    # --- Detector 1: auto_resolution_reversal_rate ---
    reversal_threshold = float(th["auto_resolution_reversal_rate"])
    if auto_resolutions >= min_vol:
        reversal_rate = reversed_count / auto_resolutions
        reversal_tripped = reversal_rate > reversal_threshold
    else:
        reversal_rate = reversed_count / auto_resolutions if auto_resolutions else 0.0
        reversal_tripped = False  # min_volume floor

    alarm_reversal = Alarm(
        name="auto_resolution_reversal_rate",
        value=reversal_rate,
        threshold=reversal_threshold,
        tripped=reversal_tripped,
        detail={
            "reversed": reversed_count,
            "auto_resolutions": auto_resolutions,
            "min_volume": min_vol,
            "window_days": window_days,
        },
    )

    # --- Detector 2: cross_project_override_rate ---
    cross_threshold = float(th["cross_project_override_rate"])
    if total >= min_vol:
        cross_rate = cross_project / total
        cross_tripped = cross_rate > cross_threshold
    else:
        cross_rate = cross_project / total if total else 0.0
        cross_tripped = False  # min_volume floor

    alarm_cross = Alarm(
        name="cross_project_override_rate",
        value=cross_rate,
        threshold=cross_threshold,
        tripped=cross_tripped,
        detail={
            "cross_project": cross_project,
            "total": total,
            "min_volume": min_vol,
            "window_days": window_days,
        },
    )

    # --- Detector 3: observed_cascade_depth ---
    depth_threshold = float(th["observed_cascade_depth"])
    depth_tripped = max_cascade_depth > depth_threshold

    alarm_depth = Alarm(
        name="observed_cascade_depth",
        value=float(max_cascade_depth),
        threshold=depth_threshold,
        tripped=depth_tripped,
        detail={
            "max_cascade_depth": max_cascade_depth,
            "window_days": window_days,
        },
    )

    return [alarm_reversal, alarm_cross, alarm_depth]


# ---------------------------------------------------------------------------
# Snapshot builder — reads the real act log + cascade history
# ---------------------------------------------------------------------------

def build_snapshot(*, root: Path | None = None, window_days: int = 30) -> dict:
    """Build a snapshot dict from the real resolution-act log and cascade history.

    Called by the ``reversal-anomalies`` lint check. Reads:
    - ``.knowledge/contradictions/resolution_acts.jsonl`` (via ``contradictions_log``)
    - Cascade-depth history from ``.knowledge/contradictions/cascade_depths.jsonl``
      (written by T1's retraction.cascade() when depth > 0; optional — absent → 0).

    Cross-project detection heuristic: a resolution act is "cross-project" when
    the winner's source domain prefix differs from the loser's. T1 may annotate
    acts with ``winner.domain`` / ``loser.domain``; if not present, the source ID
    slug prefix is used as a proxy (best-effort — false positives possible until T1
    annotates).
    """
    cutoff = datetime.now(timezone.utc) - timedelta(days=window_days)
    cutoff_str = cutoff.strftime("%Y-%m-%dT%H:%M:%SZ")

    acts = contradictions_log.read_resolution_acts()

    auto_resolutions = 0
    reversed_count = 0
    cross_project = 0

    for act in acts:
        resolved_at = act.get("resolved_at", "")
        # Filter to window
        if resolved_at and resolved_at < cutoff_str:
            continue
        auto_resolutions += 1

        # Reversal marker: T1's mark_act_reverted() adds ``reverts_act`` to the
        # act entry (see contradictions_log.mark_act_reverted). For the reversal
        # rate we count acts that have been reverted (have a reversal_type intent
        # in the queue OR have a ``reverts_act`` marker stamped on them). In the
        # current schema the reverted act itself gets ``reverts_act`` appended;
        # a separate revert-intent record is enqueued. We look for both:
        if act.get("reverts_act") or act.get("reversal_type") == "contradiction-resolution":
            reversed_count += 1

        # Cross-project heuristic
        winner = act.get("winner") or {}
        loser = act.get("loser") or {}
        winner_domain = winner.get("domain") or _domain_from_source(winner.get("source", ""))
        loser_domain = loser.get("domain") or _domain_from_source(loser.get("source", ""))
        if winner_domain and loser_domain and winner_domain != loser_domain:
            cross_project += 1

    # Cascade depth: read from optional sidecar log
    max_cascade_depth = _read_max_cascade_depth(root=root, cutoff_str=cutoff_str)

    return {
        "auto_resolutions": auto_resolutions,
        "reversed": reversed_count,
        "cross_project": cross_project,
        "total": auto_resolutions,
        "max_cascade_depth": max_cascade_depth,
    }


def _domain_from_source(source: str) -> str:
    """Heuristic: extract a domain token from a source identifier.

    For sources like ``"pubmed-123"`` → ``"pubmed"``;
    ``"web-abc"`` → ``"web"`` etc. Returns ``""`` if unparseable.
    """
    if not source:
        return ""
    # If the source has an explicit domain separator (e.g. "med/pubmed-1") take the first segment
    parts = str(source).split("/")
    if len(parts) >= 2:
        return parts[0]
    # Otherwise take the type prefix before the first hyphen
    return parts[0].split("-")[0] if "-" in parts[0] else ""


def _cascade_depths_path(root: Path | None) -> Path:
    from gateway import paths as _paths
    base = _paths.knowledge_root() if root is None else root
    return base / ".knowledge" / "contradictions" / "cascade_depths.jsonl"


def _read_max_cascade_depth(*, root: Path | None, cutoff_str: str) -> int:
    """Read the max cascade depth from the optional sidecar log.

    If the file doesn't exist (T1 not yet shipped or no cascades), returns 0.
    Each line: ``{"depth": int, "recorded_at": "..."}``
    """
    import json
    path = _cascade_depths_path(root)
    if not path.exists():
        return 0
    max_depth = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        recorded_at = obj.get("recorded_at", "")
        if recorded_at and recorded_at < cutoff_str:
            continue
        depth = int(obj.get("depth", 0))
        if depth > max_depth:
            max_depth = depth
    return max_depth
