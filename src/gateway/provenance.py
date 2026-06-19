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

    log = _git("log", "--all", "--format=%H", "--name-only")
    if log.returncode != 0:
        return []

    corpus_commits: list[str] = []
    cur: str | None = None
    touched_corpus = False
    blocks: list[tuple[str, bool]] = []
    for line in log.stdout.splitlines():
        if not line.strip():
            if cur is not None:
                blocks.append((cur, touched_corpus))
            cur = None
            touched_corpus = False
            continue
        if cur is None and len(line.strip()) == 40 and all(
            c in "0123456789abcdef" for c in line.strip()
        ):
            cur = line.strip()
            touched_corpus = False
        else:
            if line.startswith("wiki/") or line.startswith("raw/"):
                touched_corpus = True
    if cur is not None:
        blocks.append((cur, touched_corpus))

    corpus_commits = [sha for sha, touched in blocks if touched]

    recorded = {
        n["decision_basis"].get("commit")
        for n in read_nodes(root=root)
        if n.get("decision_basis", {}).get("commit")
    }
    return [sha for sha in corpus_commits if sha not in recorded]


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
