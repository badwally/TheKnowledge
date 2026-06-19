"""Fragmentation lint check — concept clusters with high mutual identity-similarity.

Detects sets of concept/entity pages whose identity text (title + aliases) is
mutually very close in the ``entity`` embedding namespace, indicating the same
concept has been fragmented into multiple near-duplicate pages.

Algorithm:
- For each concept (or entity) page in the embedding index's ``entity`` namespace,
  run ``EmbeddingIndex.nn("entity", identity_text, k)`` to find neighbors.
- Group pages with mutual cosine distance ≤ ``band`` (default: entity threshold 0.30
  from ``EmbeddingIndex.thresholds()`` — tunable).
- Emit one ``LintFinding`` per cluster of size ≥ 2, with ``metadata={"members": [...]}``.

The check reads the embedding index directly — it does NOT perform any LLM calls.
Only pages whose identity is indexed in the ``entity`` namespace are checked
(entity + concept page types per ``embedding_index._ENTITY_PAGE_TYPES``).
"""

from __future__ import annotations

from gateway import paths
from gateway.embedding_index import EmbeddingIndex, thresholds
from gateway.lint import LintFinding, SEVERITY_WARNING


# Number of nearest neighbors to fetch per page.
_FRAGMENTATION_K = 20

# Minimum cluster size to emit a finding.
_MIN_CLUSTER_SIZE = 2


def run(*, band: float | None = None) -> list[LintFinding]:
    """Find near-duplicate concept/entity clusters in the entity embedding namespace.

    ``band`` overrides the entity threshold (default: ``thresholds()["entity"]``).
    Returns one LintFinding per cluster of size >= 2.
    """
    threshold = band if band is not None else thresholds()["entity"]
    idx = EmbeddingIndex()

    # Read all keys in the entity namespace from the embedding DB.
    import sqlite3
    db_path = paths.embedding_db_path()
    if not db_path.exists():
        return []

    conn = sqlite3.connect(str(db_path))
    try:
        rows = conn.execute(
            "SELECT key, vec FROM vectors WHERE namespace = 'entity'"
        ).fetchall()
    finally:
        conn.close()

    if not rows:
        return []

    # Build key → neighbor-keys mapping (mutual distance <= band).
    import numpy as np
    keys = [r[0] for r in rows]
    vecs = np.stack([np.frombuffer(r[1], dtype=np.float32) for r in rows])

    # All-pairs cosine distance matrix (vectors are unit-norm → dist = 1 - dot).
    dot_matrix = vecs @ vecs.T
    dist_matrix = 1.0 - dot_matrix
    np.fill_diagonal(dist_matrix, 1.0)  # Exclude self-similarity

    # Build adjacency: edge between i and j if dist_matrix[i,j] <= threshold.
    n = len(keys)
    adjacency: list[set[int]] = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if dist_matrix[i, j] <= threshold:
                adjacency[i].add(j)
                adjacency[j].add(i)

    # Connected-component clustering (Union-Find / BFS).
    visited = [False] * n
    clusters: list[list[str]] = []

    for start in range(n):
        if visited[start]:
            continue
        if not adjacency[start]:
            visited[start] = True
            continue
        # BFS from start.
        component: list[int] = []
        queue: list[int] = [start]
        visited[start] = True
        while queue:
            node = queue.pop(0)
            component.append(node)
            for neighbor in adjacency[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        if len(component) >= _MIN_CLUSTER_SIZE:
            clusters.append([keys[i] for i in component])

    findings: list[LintFinding] = []
    for cluster in clusters:
        # Sort members for deterministic output.
        members = sorted(cluster)
        findings.append(LintFinding(
            check="fragmentation",
            severity=SEVERITY_WARNING,
            message=(
                f"fragmentation cluster of {len(members)} near-duplicate pages "
                f"(entity distance ≤ {threshold:.2f}): consider merging"
            ),
            path=members[0],
            metadata={"members": members, "band": threshold},
        ))

    return findings
