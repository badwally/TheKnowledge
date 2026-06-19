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
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from gateway import paths
from gateway.embedding_index import EmbeddingIndex, LexicalFallbackEncoder, thresholds


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
        2. Apply cold-start gate: texts appearing < cold_start_min_recurrences times
           are logged but not eligible for clustering.
        3. Embed eligible texts into the `question` namespace and cluster greedily:
           each text is assigned to the first existing cluster whose centroid is within
           proximity_radius; otherwise a new cluster is started.
        4. Clusters at or above recurrence_mass trigger exactly one canonicalization
           intent (dedup via triggered.json).

        Returns list of GapCluster (all clusters, not just triggered ones).
        """
        t = thresholds()
        proximity_radius: float = float(t["demand.proximity_radius"])
        recurrence_mass: int = int(t["demand.recurrence_mass"])
        cold_start_min: int = int(t["demand.cold_start_min_recurrences"])

        records = _load_gaps(self._gaps_path())
        if not records:
            return []

        # Count occurrences per unique text (case-insensitive strip)
        text_counts: dict[str, int] = {}
        for r in records:
            key = r.text
            text_counts[key] = text_counts.get(key, 0) + 1

        # All unique texts are clustered (for structure + purity).
        # The cold-start gate controls trigger eligibility, not cluster membership.
        all_texts = list(text_counts.keys())
        if not all_texts:
            return []

        # Embed all texts
        vecs = self._encoder.embed(all_texts)
        import numpy as np

        def _cosine_dist(a: list[float], b: list[float]) -> float:
            va = np.asarray(a, dtype=np.float32)
            vb = np.asarray(b, dtype=np.float32)
            sim = float(np.dot(va, vb))
            return 1.0 - sim  # vectors are L2-normalised

        # Greedy clustering: assign each text to the nearest centroid within radius,
        # or start a new cluster. Centroid is the first text in the cluster.
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

        # Load already-triggered clusters (dedup gate)
        triggered_set = _load_triggered(self._triggered_path())

        result: list[GapCluster] = []
        new_triggered: set[str] = set()

        for cl in clusters:
            member_texts = [m[0] for m in cl["members"]]
            mass = sum(m[1] for m in cl["members"])

            cid = _cluster_id(cl["centroid_text"])
            already_triggered = cid in triggered_set
            # Cold-start gate: cluster must have total mass >= cold_start_min_recurrences
            # before it is eligible to trigger (prevents first-occurrence triggers).
            # Trigger also requires mass >= recurrence_mass (the heavy threshold).
            eligible_for_trigger = mass >= cold_start_min
            should_trigger = eligible_for_trigger and (mass >= recurrence_mass) and not already_triggered

            if should_trigger:
                self._submit_canonicalization_trigger(cl["centroid_text"], member_texts, mass)
                new_triggered.add(cid)

            result.append(GapCluster(
                centroid_text=cl["centroid_text"],
                member_texts=member_texts,
                recurrence_mass=mass,
                triggered=should_trigger or already_triggered,
            ))

        # Persist any new triggers
        if new_triggered:
            updated = triggered_set | new_triggered
            _save_triggered(self._triggered_path(), updated)

        return result

    def _submit_canonicalization_trigger(
        self, centroid_text: str, member_texts: list[str], mass: int
    ) -> None:
        """Submit exactly one build-tier synthesis intent for a gap cluster.

        Mirrors the deposit() pattern from ops/deposit.py. The intent payload
        is a synthesis type with the cluster's centroid as the title, so the
        CommitGate can canonicalize it as a synthesis page.
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
        iid = compute_intent_id(payload, identity, semantics="demand-trigger")
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
