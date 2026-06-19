"""Operational-provenance log + per-producer telemetry — Librarian Phase 1 (T1.5).

The intent queue is a write-ahead log that yields an **operational-provenance
graph** (corpus-change -> intent -> agent), distinct from content-provenance
(claim -> source, the existing ``[[sources/<id>]]`` graph). Each node records the
**decision basis** sufficient to audit and replay a canonicalization without
re-running the LLM (decision 3): the policy/threshold version, the dedup score +
candidate referents, the contradiction/trust determinations, and the merge/rebase
branch taken. This is what makes a resolution reversible (§9, G1) and a lost
update detectable (§6, F1).

Storage: append-only ``.knowledge/provenance/nodes.jsonl`` (one JSON object per
line). This **adds alongside** ``log.md`` (the append-only event stream) — it does
not replace it. The provenance log is gitignored derived/operational state.

C7: every committed corpus change — including watcher/poller ingest — must
resolve to a provenance node. ``coverage_gap()`` returns committed corpus-touching
commits with no node.

A7 (stub): ``ProducerTelemetry`` tracks per-producer accept/reject/merge counts.
Alarms are wired in Phase 4; here only the counters exist.
"""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import uuid

from gateway import paths


def _nodes_path(root: Path | None = None) -> Path:
    base = paths.provenance_dir() if root is None else (root / ".knowledge" / "provenance")
    return base / "nodes.jsonl"


def record(intent_id: str, decision_basis: dict, *, root: Path | None = None) -> str:
    """Append an operational-provenance node; return its node_id."""
    node_id = uuid.uuid4().hex[:16]
    node = {
        "node_id": node_id,
        "intent_id": intent_id,
        "decision_basis": dict(decision_basis),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    path = _nodes_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(node, sort_keys=True) + "\n")
    return node_id


def read_nodes(*, root: Path | None = None) -> list[dict]:
    """Return all provenance nodes (oldest first)."""
    path = _nodes_path(root)
    if not path.exists():
        return []
    nodes: list[dict] = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                nodes.append(json.loads(line))
    return nodes


def coverage_gap(*, root: Path | None = None) -> list[str]:
    """Return committed corpus-touching commit SHAs lacking a provenance node (C7).

    A corpus-touching commit is one that modifies a path under ``wiki/`` or
    ``raw/``. Each such commit must be referenced by exactly one node's
    ``decision_basis.commit``.
    """
    repo = root or paths.knowledge_root()

    def _git(*args):
        return subprocess.run(
            ["git", *args], cwd=repo, capture_output=True, text=True, check=False
        )

    # Prefix each commit's SHA line with \x01 so SHA lines are unambiguously
    # distinguishable from file-name lines and blank lines — `--name-only` emits
    # a blank line immediately after the SHA, which a separator-based parser
    # would mistake for a commit boundary and drop every touched path.
    log = _git("log", "--all", "--format=\x01%H", "--name-only")
    if log.returncode != 0:
        return []

    blocks: list[tuple[str, set[str]]] = []
    cur: str | None = None
    cur_paths: set[str] = set()

    def _flush() -> None:
        if cur is not None:
            blocks.append((cur, set(cur_paths)))

    for line in log.stdout.splitlines():
        if line.startswith("\x01"):
            _flush()
            cur = line[1:].strip()
            cur_paths = set()
        elif cur is not None and (line.startswith("wiki/") or line.startswith("raw/")):
            cur_paths.add(line.strip())
    _flush()

    corpus_commits = [(sha, touched) for sha, touched in blocks if touched]

    nodes = read_nodes(root=root)
    # Commits covered by an explicit commit-SHA node (gate-authored).
    recorded_sha = {
        n["decision_basis"].get("commit")
        for n in nodes
        if n.get("decision_basis", {}).get("commit")
    }
    # CORRECTNESS-9: a producer node (e.g. the watcher) records the paths it
    # produced but not the commit SHA (the watcher daemon commits separately,
    # after the node is written). A corpus commit whose touched paths are all
    # produced by such a marker node is covered — it must NOT be flagged as a gap.
    producer_paths: set[str] = set()
    for n in nodes:
        basis = n.get("decision_basis", {})
        if basis.get("producer"):
            for p in basis.get("paths_touched", []) or []:
                producer_paths.add(p)

    gaps: list[str] = []
    for sha, touched in corpus_commits:
        if sha in recorded_sha:
            continue
        # Covered if every corpus path the commit touched was produced by a
        # marker node.
        if touched and touched <= producer_paths:
            continue
        gaps.append(sha)
    return gaps


class ProducerTelemetry:
    """Per-producer accept/reject/merge counters (A7 stub).

    Alarms (rejection-spike, dedup-merge spike, deposit-silence) are wired in
    Phase 4; Phase 1 ships the counters the alarms read.
    """

    def __init__(self) -> None:
        self._counts: dict[str, dict[str, int]] = defaultdict(
            lambda: defaultdict(int)
        )

    def incr(self, identity: str, kind: str) -> None:
        self._counts[identity][kind] += 1

    def snapshot(self) -> dict[str, dict[str, int]]:
        return {ident: dict(kinds) for ident, kinds in self._counts.items()}
