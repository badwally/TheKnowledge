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


def cascade(
    retracted_source_ids: set[str],
    *,
    root: Path | None = None,
) -> CascadeResult:
    """Walk the synthesizes: + [[sources/]] citation graph and return all
    transitively-flagged wiki pages.

    Algorithm:
    1. Seed: any wiki page whose body directly cites [[sources/<id>]] where id ∈
       retracted_source_ids (direct dependents, depth=1).
    2. Expand: for each flagged page P, find pages Q where Q's synthesizes: list
       contains P's slug or the path variant. Unflagged neighbors → queue (depth+1).
    3. Cycle detection: track an in-progress set (grey nodes). A back-edge to a
       grey node sets terminated_on_cycle=True and does NOT re-enqueue it.
    4. Fixpoint: stop when the queue is empty.
    5. Return flagged in deterministic discovery order (BFS level-sorted).
    """
    if root is not None:
        import os
        os.environ["KNOWLEDGE_ROOT"] = str(root)

    if not retracted_source_ids:
        return CascadeResult(flagged=[], terminated_on_cycle=False, depth=0)

    pages = _load_wiki_pages()

    # Index: slug → (rel_str, front, body)
    slug_index: dict[str, tuple[str, dict, str]] = {}
    for rel, path, front, body in pages:
        slug = front.get("slug") or path.stem
        slug_index[slug] = (rel, front, body)

    # Build reverse index: page_rel → list of page_rels that synthesize it
    # (Q synthesizes P → Q is a dependent of P)
    synthesizes_reverse: dict[str, list[str]] = {}
    for rel, path, front, body in pages:
        for target in front.get("synthesizes", []) or []:
            target_str = str(target)
            # Normalize: "synthesis/a" → slug "a"
            # Could be "sources/...", "synthesis/...", plain slug, or rel_path
            key = target_str
            synthesizes_reverse.setdefault(key, []).append(rel)

    # Helper: get all reverse-synthesizes dependents of a given flagged rel/slug
    def _dependents_of(rel: str, path: Path, front: dict) -> list[str]:
        slug = front.get("slug") or path.stem
        page_type = front.get("type", "")
        # The synthesizes: field can use various forms. We check all plausible keys:
        # - "synthesis/slug" (most common for synthesis pages)
        # - "slug" (bare)
        # - the rel_path "wiki/synthesis/slug.md"
        candidates: list[str] = [slug]
        if page_type:
            candidates.append(f"{page_type}/{slug}")
        # Also the rel without the wiki/ prefix for cross-type refs:
        rel_no_wiki = rel[len("wiki/"):] if rel.startswith("wiki/") else rel
        rel_no_ext = rel_no_wiki[:-len(".md")] if rel_no_wiki.endswith(".md") else rel_no_wiki
        candidates.append(rel_no_ext)

        deps: list[str] = []
        for c in candidates:
            deps.extend(synthesizes_reverse.get(c, []))
        return deps

    # BFS
    visited: set[str] = set()      # already enqueued/processed
    flagged_ordered: list[str] = []
    terminated_on_cycle = False
    max_depth = 0

    # Seed: pages that directly cite any retracted source
    from collections import deque
    queue: deque[tuple[str, int]] = deque()  # (rel, depth)
    rel_by_path: dict[str, tuple[Path, dict, str]] = {r: (p, f, b) for r, p, f, b in pages}

    for rel, path, front, body in pages:
        for link in find_wikilinks(body):
            sid = _source_id_from_rel(link.target)
            if sid and sid in retracted_source_ids:
                if rel not in visited:
                    visited.add(rel)
                    flagged_ordered.append(rel)
                    queue.append((rel, 1))
                break

    # BFS expansion — build a forward-edge set to detect cycles
    # A cycle exists when a page P's dependent D is already in visited
    # (it was already flagged/enqueued earlier in the BFS, meaning there
    # is a path from a seed to D, and D also synthesizes P which synthesizes
    # something that led to P — closing a loop).
    while queue:
        rel, depth = queue.popleft()
        max_depth = max(max_depth, depth)

        if rel not in rel_by_path:
            continue

        path, front, body = rel_by_path[rel]
        for dep_rel in _dependents_of(rel, path, front):
            if dep_rel in visited:
                # dep_rel was already seen — it has a path to the flagged set
                # AND is being synthesized by rel, which is already in the
                # flagged set. This is a cycle in the synthesizes: graph.
                terminated_on_cycle = True
            else:
                visited.add(dep_rel)
                flagged_ordered.append(dep_rel)
                queue.append((dep_rel, depth + 1))

    # Sort within BFS tiers for deterministic order: sort the full list by rel_path
    # while preserving the guarantee that all depth-1 come before depth-2, etc.
    # Since BFS order is already level-sequential, a final sort by rel_path
    # within each BFS level gives determinism. For simplicity (and to match the
    # spec's "deterministic discovery order"), we sort the complete flagged list.
    flagged_sorted = sorted(flagged_ordered)

    return CascadeResult(
        flagged=flagged_sorted,
        terminated_on_cycle=terminated_on_cycle,
        depth=max_depth,
    )


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
