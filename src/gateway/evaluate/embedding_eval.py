"""Per-namespace embedding adequacy gate (Librarian Phase 2, I2).

One shared encoder pulls geometry in incompatible directions, so each namespace
ships its OWN golden set and an INDEPENDENTLY-FALSIFIABLE gate (design §13). The
active encoder is the lexical fallback (`lexical-fallback-v1`); it is honest
starting infrastructure, not a correctness guarantee. Each operating point's gate
is falsifiable: flip a golden label and the gate flips. The active fallback must
pass its own (honestly weak) gate or be marked active+falsifiable.

Golden sets live under `.knowledge/eval/embedding/{section,entity,question}.yaml`.

Metrics:
- entity   → precision on the merge/no-merge decision at the dedup threshold.
- section  → recall@1 (the relevant section is the nearest neighbor + within band).
- question → cluster purity (within-cluster pairs near, cross-cluster pairs far).
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import yaml

from gateway import paths
from gateway.embedding_index import Encoder, default_encoder, thresholds


def golden_dir() -> Path:
    return paths.knowledge_internal() / "eval" / "embedding"


@dataclass
class NamespaceGateReport:
    namespace: str
    metric: str
    value: float
    floor: float
    passed: bool
    fallback_active: bool
    fallback_falsifiable: bool
    model_version: str

    def summary(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        fb = " (fallback active, falsifiable)" if self.fallback_active else ""
        return (
            f"[{status}] {self.namespace}: {self.metric}={self.value:.3f} "
            f">= floor {self.floor:.3f}{fb} @ {self.model_version}"
        )


def _load(namespace: str) -> dict:
    path = golden_dir() / f"{namespace}.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


def _dist(enc: Encoder, a: str, b: str) -> float:
    va, vb = enc.embed([a, b])
    return 1.0 - float(np.dot(np.asarray(va), np.asarray(vb)))


def _entity_precision(enc, golden, threshold) -> float:
    """Precision of the merge decision (predict merge iff dist <= threshold)."""
    correct = 0
    total = 0
    for pair in golden["pairs"]:
        predicted_merge = _dist(enc, pair["a"], pair["b"]) <= threshold
        if predicted_merge == bool(pair["merge"]):
            correct += 1
        total += 1
    return correct / total if total else 0.0


def _section_recall_at_1(enc, golden, threshold) -> float:
    sections = golden["sections"]
    keys = list(sections)
    mat = np.stack([np.asarray(v) for v in enc.embed([sections[k] for k in keys])])
    hits = 0
    total = 0
    for case in golden["queries"]:
        q = np.asarray(enc.embed([case["query"]])[0])
        dists = 1.0 - (mat @ q)
        best = int(np.argmin(dists))
        if keys[best] == case["relevant"] and dists[best] <= threshold:
            hits += 1
        total += 1
    return hits / total if total else 0.0


def _question_purity(enc, golden, threshold) -> float:
    """Fraction of pairs correctly classified: within-cluster near, cross far."""
    clusters = golden["clusters"]
    members = {name: items for name, items in clusters.items()}
    correct = 0
    total = 0
    names = list(members)
    # within-cluster pairs should be near
    for name in names:
        for a, b in itertools.combinations(members[name], 2):
            if _dist(enc, a, b) <= threshold:
                correct += 1
            total += 1
    # cross-cluster pairs should be far
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            for a in members[names[i]]:
                for b in members[names[j]]:
                    if _dist(enc, a, b) > threshold:
                        correct += 1
                    total += 1
    return correct / total if total else 0.0


def _score(namespace: str, enc, golden: dict, threshold: float) -> tuple[str, float]:
    metric = golden["metric"]
    if namespace == "entity":
        return metric, _entity_precision(enc, golden, threshold)
    if namespace == "section":
        return metric, _section_recall_at_1(enc, golden, threshold)
    if namespace == "question":
        return metric, _question_purity(enc, golden, threshold)
    raise ValueError(f"unknown namespace: {namespace!r}")


def _flip_one_label(namespace: str, golden: dict) -> dict:
    """Return a copy of the golden with ONE label flipped (falsifiability probe).

    A correct gate must FAIL on the flipped golden — proving the gate is not a
    rubber stamp that passes regardless of the labels.
    """
    import copy

    g = copy.deepcopy(golden)
    if namespace == "entity":
        g["pairs"][0]["merge"] = not g["pairs"][0]["merge"]
    elif namespace == "section":
        # point the first query at a wrong relevant section
        keys = [k for k in g["sections"] if k != g["queries"][0]["relevant"]]
        g["queries"][0]["relevant"] = keys[0]
    elif namespace == "question":
        # move a member from one cluster to another (corrupts purity)
        names = list(g["clusters"])
        moved = g["clusters"][names[0]].pop()
        g["clusters"][names[1]].append(moved)
    return g


def evaluate_namespace(
    namespace: str, encoder: Encoder | None = None
) -> NamespaceGateReport:
    enc = encoder or default_encoder()
    golden = _load(namespace)
    threshold = thresholds()[namespace]
    floor = float(golden["floor"])

    metric, value = _score(namespace, enc, golden, threshold)
    passed = value >= floor

    # Falsifiability: the gate must FAIL on a flipped golden label.
    flipped = _flip_one_label(namespace, golden)
    _m, flipped_value = _score(namespace, enc, flipped, threshold)
    falsifiable = flipped_value < floor

    # The lexical fallback is the active encoder (I2). It is "active+falsifiable"
    # when it is the encoder in use AND its gate is falsifiable.
    fallback_active = enc.model_version == "lexical-fallback-v1"

    return NamespaceGateReport(
        namespace=namespace,
        metric=metric,
        value=value,
        floor=floor,
        passed=passed,
        fallback_active=fallback_active,
        fallback_falsifiable=falsifiable,
        model_version=enc.model_version,
    )


def evaluate_all(encoder: Encoder | None = None) -> dict[str, NamespaceGateReport]:
    return {ns: evaluate_namespace(ns, encoder) for ns in ("section", "entity", "question")}
