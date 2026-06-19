"""DemandLedger — online gap clustering + canonicalization trigger (Phase 5, decision 11).

Implements I4 (raw gap text retention for re-embed survival), decision 11 (online
clustering by proximity_radius, cold-start gate, exactly-one trigger dedup).

Storage: .knowledge/demand/gaps.jsonl (raw gap text + timestamp + caller, gitignored
derived state — see .gitignore).

Thresholds consumed from embedding_index.thresholds():
  demand.proximity_radius (0.40)        — cosine-distance threshold for cluster merge
  demand.recurrence_mass (5)            — cluster mass at which trigger fires
  demand.cold_start_min_recurrences (3) — gap must recur this many times before clustering

Canonicalization trigger: when a cluster reaches recurrence_mass, the ledger submits
exactly ONE build-tier synthesis intent via the IntentQueue. A cluster may only trigger
once; re-running cluster() does NOT double-submit (dedup-by-cluster-id).

I4 — reembed(new_encoder): drops cached vectors, re-embeds from retained raw text in
gaps.jsonl, re-clusters from scratch. Recurrence counts are preserved (they derive from
the raw gap count, not the vector state).
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np

from gateway import locking, paths
from gateway.embedding_index import LexicalFallbackEncoder, thresholds

# Lock guarding the read-modify-write of triggered.json (TOCTOU fix).
_DEMAND_TRIGGER_LOCK = "librarian-demand-trigger"


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass
class GapRecord:
    """A single logged corpus gap (I4: raw text retained, never summarised)."""
    text: str
    caller: str | None
    recorded_at: float


@dataclass
class GapCluster:
    """A cluster of related gap texts produced by cluster()."""
    centroid_text: str
    member_texts: list[str]
    recurrence_mass: int
    triggered: bool


# ---------------------------------------------------------------------------
# Persistence helpers
# ---------------------------------------------------------------------------


def _demand_dir() -> Path:
    return paths.knowledge_internal() / "demand"


def _gaps_path() -> Path:
    return _demand_dir() / "gaps.jsonl"


def _triggered_path() -> Path:
    """Records cluster IDs that have already fired a canonicalization trigger."""
    return _demand_dir() / "triggered.json"


def _load_gaps(gaps_path: Path) -> list[GapRecord]:
    if not gaps_path.exists():
        return []
    records = []
    with open(gaps_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            records.append(GapRecord(
                text=obj["text"],
                caller=obj.get("caller"),
                recorded_at=obj.get("recorded_at", 0.0),
            ))
    return records


def _load_triggered(triggered_path: Path) -> set[str]:
    if not triggered_path.exists():
        return set()
    try:
        return set(json.loads(triggered_path.read_text()))
    except (json.JSONDecodeError, OSError):
        return set()


def _save_triggered(triggered_path: Path, triggered: set[str]) -> None:
    triggered_path.parent.mkdir(parents=True, exist_ok=True)
    triggered_path.write_text(json.dumps(sorted(triggered)))


def _cluster_id(centroid_text: str) -> str:
    """Stable cluster identifier derived from centroid text."""
    return hashlib.sha256(centroid_text.encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------
# DemandLedger
# ---------------------------------------------------------------------------


class DemandLedger:
    """Online gap clustering + canonicalization trigger (decision 11).

    Usage:
        led = DemandLedger()
        led.record_gap("how does semaglutide affect gastric emptying")
        clusters = led.cluster()

    The ledger is stateless in memory; all state lives in .knowledge/demand/.
    Multiple DemandLedger instances (e.g. per-request) are safe because:
    - record_gap appends atomically (line-level append to .jsonl)
    - cluster() reads the full .jsonl then re-derives; last writer to
      triggered.json wins (safe: trigger dedup is additive only)
    """

    def __init__(
        self,
        *,
        encoder=None,
        queue=None,
        root: Path | None = None,
    ) -> None:
        self._encoder = encoder or LexicalFallbackEncoder()
        self._queue = queue  # IntentQueue | None — injected for tests
        self._root = root

    def _gaps_path(self) -> Path:
        if self._root is not None:
            return self._root / ".knowledge" / "demand" / "gaps.jsonl"
        return _gaps_path()

    def _triggered_path(self) -> Path:
        if self._root is not None:
            return self._root / ".knowledge" / "demand" / "triggered.json"
        return _triggered_path()

    def record_gap(self, text: str, *, caller: str | None = None) -> GapRecord:
        """Log a corpus gap. Raw text is retained for I4 re-embed survival."""
        rec = GapRecord(text=text.strip(), caller=caller, recorded_at=time.time())
        p = self._gaps_path()
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "a") as f:
            f.write(json.dumps({
                "text": rec.text,
                "caller": rec.caller,
                "recorded_at": rec.recorded_at,
            }) + "\n")
        return rec

    def cluster(self) -> list[GapCluster]:
        """Online cluster all logged gaps.

        Algorithm:
        1. Load all raw gap texts from .knowledge/demand/gaps.jsonl.
        2. Embed every unique text into the `question` namespace and cluster greedily:
           each text joins the first cluster whose centroid is within proximity_radius;
           otherwise a new cluster is started. All texts appear in the output (purity).
        3. Trigger-mass cold-start gate: a cluster's TRIGGER mass counts only those
           member-texts whose OWN occurrence-count >= cold_start_min_recurrences. A
           one-off (count below cold-start) contributes 0 toward the trigger, so a
           non-recurring paraphrase cannot push a below-mass cluster over. This makes
           cold_start_min_recurrences a live behavioral parameter (not dead code).
        4. A cluster whose TRIGGER mass >= recurrence_mass fires exactly one
           canonicalization intent. Dedup is on a STABLE cluster identity (the
           cold-start-eligible member text that sorts first) so a member joining the
           cluster after it triggered cannot re-trigger it. The read-modify-write of
           triggered.json runs under a file lock (TOCTOU-safe).

        `recurrence_mass` on each returned GapCluster is the TOTAL occurrence mass
        (all members) for reporting; the trigger decision uses the gated trigger-mass.
        """
        t = thresholds()
        proximity_radius: float = float(t["demand.proximity_radius"])
        recurrence_mass: int = int(t["demand.recurrence_mass"])
        cold_start_min: int = int(t["demand.cold_start_min_recurrences"])

        records = _load_gaps(self._gaps_path())
        if not records:
            return []

        # Count occurrences per unique text (insertion-ordered)
        text_counts: dict[str, int] = {}
        for r in records:
            key = r.text
            text_counts[key] = text_counts.get(key, 0) + 1

        all_texts = list(text_counts.keys())
        if not all_texts:
            return []

        # Embed all unique texts (one batch)
        vecs = self._encoder.embed(all_texts)

        def _cosine_dist(a: list[float], b: list[float]) -> float:
            va = np.asarray(a, dtype=np.float32)
            vb = np.asarray(b, dtype=np.float32)
            sim = float(np.dot(va, vb))
            return 1.0 - sim  # vectors are L2-normalised

        # Greedy clustering: assign each text to the nearest centroid within radius,
        # or start a new cluster. Centroid is the first text in the cluster (the
        # display centroid; the dedup key is computed separately and is stable).
        clusters: list[dict[str, Any]] = []  # [{centroid_text, centroid_vec, members}]

        for text, vec in zip(all_texts, vecs):
            count = text_counts[text]
            best_idx = None
            best_dist = float("inf")
            for i, cl in enumerate(clusters):
                d = _cosine_dist(vec, cl["centroid_vec"])
                if d <= proximity_radius and d < best_dist:
                    best_dist = d
                    best_idx = i
            if best_idx is not None:
                clusters[best_idx]["members"].append((text, count))
            else:
                clusters.append({
                    "centroid_text": text,
                    "centroid_vec": vec,
                    "members": [(text, count)],
                })

        # Compute per-cluster derived quantities OUTSIDE the lock (no I/O).
        derived: list[dict[str, Any]] = []
        for cl in clusters:
            member_texts = [m[0] for m in cl["members"]]
            total_mass = sum(m[1] for m in cl["members"])
            # Trigger mass: only members whose OWN count >= cold_start_min contribute.
            eligible_members = [m for m in cl["members"] if m[1] >= cold_start_min]
            trigger_mass = sum(m[1] for m in eligible_members)
            # Stable dedup identity (drift-proof): the per-member cid of EVERY
            # cold-start-eligible member. A cluster is "already triggered" if ANY of
            # its current eligible members' cids is in the triggered set — so a NEW
            # member joining after the trigger cannot make the cluster re-fire,
            # regardless of which member would otherwise be chosen as an anchor.
            member_cids = {_cluster_id(m[0]) for m in eligible_members}
            derived.append({
                "centroid_text": cl["centroid_text"],
                "member_texts": member_texts,
                "total_mass": total_mass,
                "trigger_mass": trigger_mass,
                "member_cids": member_cids,
            })

        # TOCTOU-safe read-modify-write of triggered.json: re-read UNDER the lock,
        # decide, submit, then persist the union — all while holding the lock.
        result: list[GapCluster] = []
        with locking.file_lock(_DEMAND_TRIGGER_LOCK):
            triggered_set = _load_triggered(self._triggered_path())
            new_triggered: set[str] = set()
            for d in derived:
                # Already triggered if ANY eligible member's cid was recorded before,
                # OR was recorded by an earlier cluster in this same run.
                seen = triggered_set | new_triggered
                already_triggered = bool(d["member_cids"] & seen)
                should_trigger = (
                    d["trigger_mass"] >= recurrence_mass and not already_triggered
                )
                if should_trigger:
                    self._submit_canonicalization_trigger(
                        d["centroid_text"], d["member_texts"], d["trigger_mass"],
                        anchor_cid=min(d["member_cids"]),
                    )
                    # Record ALL eligible member cids so any one of them recognizes
                    # the cluster on a later run (drift-proof dedup).
                    new_triggered |= d["member_cids"]
                result.append(GapCluster(
                    centroid_text=d["centroid_text"],
                    member_texts=d["member_texts"],
                    recurrence_mass=d["total_mass"],
                    triggered=should_trigger or already_triggered,
                ))
            if new_triggered:
                _save_triggered(
                    self._triggered_path(), triggered_set | new_triggered
                )

        return result

    def _submit_canonicalization_trigger(
        self, centroid_text: str, member_texts: list[str], mass: int,
        *, anchor_cid: str | None = None,
    ) -> None:
        """Submit exactly one build-tier synthesis intent for a gap cluster.

        Mirrors the deposit() pattern from ops/deposit.py. The intent payload
        is a synthesis type with the cluster's centroid as the title, so the
        CommitGate can canonicalize it as a synthesis page.

        The intent_id is computed over a STABLE identity (the cluster anchor_cid,
        which does not change when a member joins) so the durable queue can
        backstop the in-process dedup: a drifted cluster that slipped past the
        triggered.json check would still content-address to the same intent_id and
        be coalesced, rather than producing a duplicate canonicalization intent.
        """
        from gateway.intent_queue import Intent, IntentQueue, compute_intent_id

        payload = {
            "page_type": "synthesis",
            "title": centroid_text,
            "body": "",
            "synthesizes": member_texts[:5],  # top members as synthesis sources
            "demand_trigger": True,
            "recurrence_mass": mass,
            "cluster_members": member_texts,
        }
        identity = {
            "caller": "demand_ledger",
            "source": "canonicalization_trigger",
            "page_type": "synthesis",
        }
        # Stable id basis: anchor_cid (drift-proof) — NOT the full drifting payload.
        # Falls back to the centroid text if no anchor is supplied.
        id_basis = {"cluster_anchor": anchor_cid or _cluster_id(centroid_text)}
        iid = compute_intent_id(id_basis, identity, semantics="demand-trigger")
        intent = Intent(intent_id=iid, payload=payload, identity=identity)
        q = self._queue or IntentQueue()
        q.submit(intent)

    def reembed(self, new_encoder) -> None:
        """Re-embed from raw gap text using new_encoder (I4 re-embed survival).

        Replaces the in-memory encoder and drops cached vectors. The next call
        to cluster() will re-embed from the raw .jsonl text — recurrence counts
        are preserved because they derive from text occurrence counts, not vectors.

        The triggered.json is NOT reset: clusters that already fired do not
        re-trigger after a model bump.
        """
        self._encoder = new_encoder
        # No vector cache to flush — clustering always re-embeds fresh from .jsonl.
        # (Future: if a vector cache is added, flush it here.)
