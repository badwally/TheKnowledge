"""Retraction cascade, acts_to_reopen, and reverse_merge_plan — Phase 5 Task 1.

## Step 0 verified schemas (from commit_gate.py and contradictions_log.py)

### Resolution act JSONL (contradictions_log.append_resolution_act / read_resolution_acts)
Written by ops/contradiction.auto_resolve → contradictions_log.append_resolution_act.
Path: .knowledge/contradictions/resolution_acts.jsonl
EXACT keys per commit_gate.py:57-66 and contradictions_log.py:58-72:
  {
    "rule":           str,        # "trust-tier-then-recency"
    "policy_version": str,        # "contradiction-policy-v1"
    "inputs":         {"a": {...}, "b": {...}},
    "winner":         {"source": str, "claim": str, "trust": float},
    "loser":          {"source": str, "claim": str, "trust": float},
    "resolved_at":    str,        # ISO-8601 UTC, set by append_resolution_act
    # optional, added by revert-resolution:
    "reverts_act":    str | absent,
  }

### Tombstone frontmatter (commit_gate.py:783-794)
Keys written at _write_merge_tombstone (commit_gate.py ~783-794):
  merged_into:  str    # target slug (e.g. "semaglutide"), NOT the rel_path
  redirect:     str    # "[[entities/semaglutide]]" (wikilink without wiki/ prefix)
  type:         str    # carried from dep_front
  title:        str    # carried from dep_front

### Provenance merge-reattachment record (commit_gate.py:797-804)
Stored in decision_basis["merge_reattachment"] of the provenance node:
  {
    "target":           str,        # canonical rel_path e.g. "wiki/entities/semaglutide.md"
    "tombstone":        str,        # deposited rel_path e.g. "wiki/entities/ozempic-brand.md"
    "aliases_unioned":  list[str],  # aliases B contributed
    "sections_carried": list[str],  # section headers B contributed (e.g. "## Side Effects")
    "claims_unioned":   list[str],  # claim bullet strings B contributed
  }
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from gateway import contradictions_log, frontmatter as fm, paths
from gateway.citations import find_wikilinks


# ---------------------------------------------------------------------------
# Public types
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CascadeResult:
    """Result of a transitive retraction cascade walk."""
    flagged: list[str]          # rel_paths (wiki/…) flagged, deterministic order
    terminated_on_cycle: bool
    depth: int                  # maximum BFS depth reached


@dataclass(frozen=True)
class CascadeDetail:
    """Per-page detail from a cascade walk (used by the lint check)."""
    rel: str                # rel_path of the flagged page
    depth: int              # BFS depth (1 = direct source citation)
    retracted_source: str   # the retracted source id that triggered this path


@dataclass(frozen=True)
class ReverseMergePlan:
    """Plan to undo a dedup merge: what to strip from canonical + what to delete."""
    canonical_rel: str          # the merge target page (to remove contributions from)
    aliases_to_remove: list[str]
    sections_to_remove: list[str]
    claims_to_remove: list[str]
    tombstone_to_delete: str    # rel_path of the tombstone to remove


# ---------------------------------------------------------------------------
# G4 — transitive synthesizes: cascade to a fixpoint, cycle-terminating
# ---------------------------------------------------------------------------

def _rel(path: Path) -> str:
    """Return a path relative to KNOWLEDGE_ROOT as a string."""
    return str(path.relative_to(paths.knowledge_root()))


def _source_id_from_rel(rel: str) -> str | None:
    """Extract the source id from a 'sources/<id>' wikilink target."""
    if rel.startswith("sources/"):
        return rel[len("sources/"):]
    return None


def _load_wiki_pages() -> list[tuple[str, Path, dict, str]]:
    """Load all wiki pages as (rel_str, path, front, body). Skips malformed."""
    wiki = paths.wiki_dir()
    if not wiki.exists():
        return []
    result: list[tuple[str, Path, dict, str]] = []
    for p in sorted(wiki.rglob("*.md")):
        try:
            front, body = fm.parse(p.read_text())
        except Exception:
            continue
        result.append((_rel(p), p, front, body))
    return result


def _run_cascade_bfs(
    retracted_source_ids: set[str],
    pages: list[tuple[str, Path, dict, str]],
) -> tuple[CascadeResult, list[CascadeDetail]]:
    """Core BFS over the synthesizes: + [[sources/]] citation graph.

    Returns (CascadeResult, list[CascadeDetail]) — the latter carries per-page
    depth and the triggering retracted_source_id. Used by both cascade() and
    cascade_detail().

    Algorithm:
    1. Seed: any wiki page whose body directly cites [[sources/<id>]] where id ∈
       retracted_source_ids (direct dependents, depth=1).
    2. Expand: for each flagged page P, find pages Q where Q's synthesizes: list
       references P (slug, "type/slug", or "type/slug" without wiki/ prefix).
    3. Cycle detection: when a BFS neighbor is already visited, set
       terminated_on_cycle=True and skip re-enqueueing.
    4. Fixpoint: stop when the queue is empty.
    5. Return sorted by rel_path for determinism.
    """
    if not pages:
        return CascadeResult(flagged=[], terminated_on_cycle=False, depth=0), []

    # Build reverse index: synthesizes-target-string → list of dependents' rels
    # (Q synthesizes P → Q is a dependent of P; "P" appears as synthesizes_reverse key)
    synthesizes_reverse: dict[str, list[str]] = {}
    for rel, path, front, body in pages:
        for target in front.get("synthesizes", []) or []:
            target_str = str(target)
            synthesizes_reverse.setdefault(target_str, []).append(rel)

    rel_by_path: dict[str, tuple[Path, dict, str]] = {r: (p, f, b) for r, p, f, b in pages}

    def _dependents_of(rel: str, path: Path, front: dict) -> list[str]:
        """Return rels of all pages whose synthesizes: references this page."""
        slug = front.get("slug") or path.stem
        page_type = front.get("type", "")
        # A synthesizes: entry can be:
        #   - "synthesis/slug" (most common)
        #   - "slug" (bare)
        #   - "type/slug" (e.g. "entities/ozempic")
        #   - rel without wiki/ prefix: "synthesis/slug.md" stripped of .md
        candidates: list[str] = [slug]
        if page_type:
            candidates.append(f"{page_type}/{slug}")
        rel_no_wiki = rel[len("wiki/"):] if rel.startswith("wiki/") else rel
        rel_no_ext = rel_no_wiki[:-len(".md")] if rel_no_wiki.endswith(".md") else rel_no_wiki
        candidates.append(rel_no_ext)

        deps: list[str] = []
        seen_deps: set[str] = set()
        for c in candidates:
            for dep_rel in synthesizes_reverse.get(c, []):
                if dep_rel not in seen_deps:
                    seen_deps.add(dep_rel)
                    deps.append(dep_rel)
        return deps

    from collections import deque
    visited: set[str] = set()
    queue: deque[tuple[str, int, str]] = deque()  # (rel, depth, triggering_source_id)
    details: list[CascadeDetail] = []
    terminated_on_cycle = False
    max_depth = 0

    # Seed: pages that directly cite any retracted source (sorted for determinism)
    for rel, path, front, body in sorted(pages, key=lambda t: t[0]):
        triggering: str | None = None
        for link in find_wikilinks(body):
            sid = _source_id_from_rel(link.target)
            if sid and sid in retracted_source_ids:
                triggering = sid
                break
        if triggering and rel not in visited:
            visited.add(rel)
            details.append(CascadeDetail(rel=rel, depth=1, retracted_source=triggering))
            queue.append((rel, 1, triggering))

    # BFS expansion
    while queue:
        rel, depth, src_id = queue.popleft()
        max_depth = max(max_depth, depth)

        if rel not in rel_by_path:
            continue

        path, front, body = rel_by_path[rel]
        for dep_rel in _dependents_of(rel, path, front):
            if dep_rel in visited:
                terminated_on_cycle = True
            else:
                visited.add(dep_rel)
                details.append(CascadeDetail(rel=dep_rel, depth=depth + 1, retracted_source=src_id))
                queue.append((dep_rel, depth + 1, src_id))

    details_sorted = sorted(details, key=lambda d: d.rel)
    flagged_sorted = [d.rel for d in details_sorted]

    result = CascadeResult(
        flagged=flagged_sorted,
        terminated_on_cycle=terminated_on_cycle,
        depth=max_depth,
    )
    return result, details_sorted


def cascade(
    retracted_source_ids: set[str],
    *,
    root: Path | None = None,
) -> CascadeResult:
    """Walk the synthesizes: + [[sources/]] citation graph and return all
    transitively-flagged wiki pages, cycle-terminating.

    Returns CascadeResult with flagged rel_paths in deterministic (sorted) order.
    """
    if root is not None:
        import os
        os.environ["KNOWLEDGE_ROOT"] = str(root)

    if not retracted_source_ids:
        return CascadeResult(flagged=[], terminated_on_cycle=False, depth=0)

    pages = _load_wiki_pages()
    result, _ = _run_cascade_bfs(retracted_source_ids, pages)
    return result


def cascade_detail(
    retracted_source_ids: set[str],
    *,
    root: Path | None = None,
) -> list[CascadeDetail]:
    """Like cascade() but returns per-page CascadeDetail (rel, depth, retracted_source).

    Used by the retracted-citations lint check to produce per-page findings
    with depth metadata.
    """
    if root is not None:
        import os
        os.environ["KNOWLEDGE_ROOT"] = str(root)

    if not retracted_source_ids:
        return []

    pages = _load_wiki_pages()
    _, details = _run_cascade_bfs(retracted_source_ids, pages)
    return details


# ---------------------------------------------------------------------------
# G3 — resolution acts to re-open when a winner source is retracted
# ---------------------------------------------------------------------------

def acts_to_reopen(
    retracted_source_ids: set[str],
    *,
    root: Path | None = None,
) -> list[dict]:
    """Return resolution acts whose winner source is in retracted_source_ids.

    Skips acts that have already been reverted (carry a 'reverts_act' key).
    """
    if root is not None:
        import os
        os.environ["KNOWLEDGE_ROOT"] = str(root)

    acts = contradictions_log.read_resolution_acts()
    result: list[dict] = []
    for act in acts:
        # Skip already-reverted acts
        if "reverts_act" in act:
            continue
        winner = act.get("winner", {})
        winner_source = winner.get("source", "")
        if winner_source in retracted_source_ids:
            result.append(act)
    return result


# ---------------------------------------------------------------------------
# G8 — reverse-merge plan (restore from reattachment set)
# ---------------------------------------------------------------------------

def _read_provenance_nodes(root: Path | None = None) -> list[dict]:
    """Read .knowledge/provenance/nodes.jsonl."""
    if root is not None:
        base = root / ".knowledge" / "provenance" / "nodes.jsonl"
    else:
        from gateway import paths as _paths
        base = _paths.provenance_dir() / "nodes.jsonl"
    if not base.is_file():
        return []
    out: list[dict] = []
    for line in base.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            out.append(obj)
    return out


def reverse_merge_plan(
    tombstone_rel: str,
    *,
    root: Path | None = None,
) -> ReverseMergePlan:
    """Build a reverse-merge plan from the tombstone rel_path.

    Reads the tombstone to confirm it carries merged_into, then finds the
    provenance node whose merge_reattachment.tombstone matches tombstone_rel
    to extract exactly what the merged deposit contributed.

    Raises ValueError if tombstone_rel is not a tombstone or the page is absent.
    Raises KeyError if no provenance node records the merge-reattachment.
    """
    kb = root or paths.knowledge_root()
    tombstone_path = kb / tombstone_rel

    if not tombstone_path.exists():
        raise FileNotFoundError(f"tombstone page not found: {tombstone_rel}")

    try:
        front, body = fm.parse(tombstone_path.read_text())
    except Exception as e:
        raise ValueError(f"cannot parse {tombstone_rel}: {e}") from e

    merged_into = front.get("merged_into")
    if not merged_into:
        raise ValueError(
            f"{tombstone_rel} is not a tombstone (no merged_into frontmatter key)"
        )

    # Find the canonical rel from the tombstone's redirect
    # redirect is "[[entities/semaglutide]]" — we need "wiki/entities/semaglutide.md"
    redirect = front.get("redirect", "")
    # Strip [[ and ]]
    link_target = redirect.strip("[] ") if redirect else f"entities/{merged_into}"
    canonical_rel = f"wiki/{link_target}.md"

    # Find provenance node recording the merge-reattachment for this tombstone
    nodes = _read_provenance_nodes(root)
    reattachment: dict[str, Any] | None = None
    for node in reversed(nodes):  # most recent first
        basis = node.get("decision_basis", {})
        mr = basis.get("merge_reattachment")
        if mr and mr.get("tombstone") == tombstone_rel:
            reattachment = mr
            break

    if reattachment is None:
        raise KeyError(
            f"no provenance node records merge_reattachment for tombstone {tombstone_rel!r}"
        )

    return ReverseMergePlan(
        canonical_rel=reattachment.get("target", canonical_rel),
        aliases_to_remove=list(reattachment.get("aliases_unioned", [])),
        sections_to_remove=list(reattachment.get("sections_carried", [])),
        claims_to_remove=list(reattachment.get("claims_unioned", [])),
        tombstone_to_delete=tombstone_rel,
    )
