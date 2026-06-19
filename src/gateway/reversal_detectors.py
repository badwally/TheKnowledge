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

Cross-project detection: a resolution act counts as cross-project iff the winner
source's real wiki domain (from raw/ frontmatter ``domains:``) is disjoint from the
loser source's. Acts whose source domain cannot be resolved are EXCLUDED, not
guessed — we under-detect honestly rather than fire on source-type heterogeneity.

Cascade depth: computed LIVE — collect currently-retracted source ids from raw
frontmatter and run ``retraction.cascade`` over the real ``synthesizes:`` graph,
taking the max ``CascadeResult.depth``. No inert sidecar.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
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
# Snapshot builder — LIVE signals over the real corpus + act log
# ---------------------------------------------------------------------------

def build_snapshot(*, window_days: int = 30) -> dict:
    """Build a snapshot dict from real corpus state — every signal is live.

    Called by the ``reversal-anomalies`` lint check. All three signals are
    computed from current on-disk state; none depend on an inert sidecar:

    auto_resolutions / reversed
        Counted from ``.knowledge/contradictions/resolution_acts.jsonl`` (read via
        ``contradictions_log.read_resolution_acts``). An act counts as **reversed**
        iff it carries a ``reverts_act`` marker — the only reversal field T1 writes
        (``contradictions_log.mark_act_reverted``). ``reversal_type`` is an
        intent-queue payload field, NOT an act field, so it is never consulted here.

    cross_project
        Resolves each act's winner/loser source to its **real wiki domain** from the
        raw source frontmatter (``domains:``). An act is cross-project iff the
        winner's and loser's resolved domains are disjoint. If either source's domain
        cannot be resolved (missing raw file / empty ``domains:``), the act is
        **excluded** from the cross-project computation — we under-detect honestly
        rather than guess from an id prefix.

    max_cascade_depth
        Computed LIVE: collect every currently-retracted source id from raw
        frontmatter (``retracted: true``, same discovery as
        ``lint/retracted_citations``) and run ``retraction.cascade`` over the real
        ``synthesizes:`` graph; take the max observed ``CascadeResult.depth``. Zero
        retractions → depth 0.

    All reads resolve through ``paths``/``contradictions_log``, which honor the
    ``KNOWLEDGE_ROOT`` env var, so tests under the ``kb_root`` fixture stay isolated
    to the temp root.
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

        # Reversal marker: ONLY reverts_act (T1's mark_act_reverted writes it onto
        # the act entry). reversal_type is not an act field — never counted.
        if act.get("reverts_act"):
            reversed_count += 1

        # Cross-project: compare the REAL wiki domains of winner vs loser sources.
        winner = act.get("winner") or {}
        loser = act.get("loser") or {}
        winner_domains = _domains_for_source(winner.get("source", ""))
        loser_domains = _domains_for_source(loser.get("source", ""))
        if winner_domains is None or loser_domains is None:
            # Unresolvable domain on either side → exclude (under-detect honestly).
            continue
        if winner_domains.isdisjoint(loser_domains):
            cross_project += 1

    max_cascade_depth = _live_max_cascade_depth()

    return {
        "auto_resolutions": auto_resolutions,
        "reversed": reversed_count,
        "cross_project": cross_project,
        "total": auto_resolutions,
        "max_cascade_depth": max_cascade_depth,
    }


def _domains_for_source(source_id: str) -> set[str] | None:
    """Resolve a source id to its real wiki domains from raw/ frontmatter.

    Returns the set of domains, or ``None`` if the source cannot be resolved
    (no raw file found, unreadable, or empty ``domains:``). Callers treat
    ``None`` as "exclude this act" rather than guessing.
    """
    if not source_id:
        return None
    from gateway import frontmatter as fm, paths

    raw = paths.raw_dir()
    for source_type in paths.SOURCE_TYPES:
        candidate = raw / source_type / f"{source_id}.md"
        if not candidate.exists():
            continue
        try:
            front, _ = fm.parse(candidate.read_text())
        except Exception:
            return None
        domains = front.get("domains") or []
        if not domains:
            return None
        return {str(d) for d in domains}
    return None


def _live_max_cascade_depth() -> int:
    """Max observed cascade depth over the current retraction graph (live).

    Collects all currently-retracted source ids from raw frontmatter (same
    discovery as ``lint/retracted_citations``) and drives ``retraction.cascade``
    over the real ``synthesizes:`` graph. No retractions → 0.
    """
    from gateway import frontmatter as fm, paths, retraction

    raw = paths.raw_dir()
    if not raw.exists():
        return 0
    retracted: set[str] = set()
    for source_type in paths.SOURCE_TYPES:
        d = raw / source_type
        if not d.exists():
            continue
        for p in d.glob("*.md"):
            try:
                front, _ = fm.parse(p.read_text())
            except Exception:
                continue
            if front.get("retracted"):
                retracted.add(str(front.get("id", p.stem)))

    if not retracted:
        return 0
    result = retraction.cascade(retracted)
    return int(result.depth)
