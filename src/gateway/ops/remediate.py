"""Corpus-rot remediation sweep — G6: de-path never touches a reachable/cited page.

``remediate`` scans wiki pages for genuinely-orphaned, uncited, provenance-unreachable
pages and submits a de-path CommitGate intent (provenanced, reversible) for each.

A page is a de-path CANDIDATE iff ALL of the following hold:
  1. It has zero inbound wiki-links (inbound_counts == 0).
  2. It is NOT reachable from the provenance graph — no provenance node's
     decision_basis references it (checked via canonical_path values).
  3. It is NOT a live citation target — no ``[[sources/...]]`` or ``[[wiki/...]]``
     wikilink from ANY provenance node or any other page points to it.
     (Condition 1 covers wiki→wiki; provenance covers commit-origin; together
     they ensure nothing that was intentionally placed is silently dropped.)

NEVER targets moc or artifact pages (intentional entry-points per orphan check).

De-path intent payload:
  {"op": "depath", "target_rel": "<wiki-rel-path>", "reversible": True}

The intent is content-addressed (compute_intent_id) so re-running is idempotent.
dry_run=True → collect candidates, return them in data["depathed"], submit nothing.
"""

from __future__ import annotations

from pathlib import Path

from gateway import paths, provenance
from gateway import search_index
from gateway.core import OperationResult
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id
from gateway.lint._walk import walk_wiki_pages


# Page types that are intentional entry-points — never de-path them.
_DEPATH_EXEMPT_TYPES = frozenset({"moc", "artifact"})


def _provenance_reachable_rels(*, root: Path | None = None) -> set[str]:
    """Return the set of wiki/ rel-paths referenced in any provenance node's decision_basis.

    The decision_basis["canonical_path"] is an absolute path string. We translate
    it to a root-relative rel_path for comparison with the page walker.
    """
    kb_root = root or paths.knowledge_root()
    nodes = provenance.read_nodes(root=root)
    reachable: set[str] = set()
    for node in nodes:
        basis = node.get("decision_basis") or {}
        for _key, val in basis.items():
            if not isinstance(val, str):
                continue
            # canonical_path is an absolute path; convert to a relative one.
            try:
                rel = Path(val).relative_to(kb_root)
                rel_str = str(rel)
                if rel_str.startswith("wiki/") and rel_str.endswith(".md"):
                    reachable.add(rel_str)
            except ValueError:
                pass
    return reachable


def remediate(
    *,
    root: Path | None = None,
    dry_run: bool = False,
    queue: IntentQueue | None = None,
) -> OperationResult:
    """Find genuinely-orphaned uncited pages and submit a de-path intent for each.

    Returns OperationResult with data={"depathed": [...], "skipped_reachable": [...]}.
    "depathed" lists rel-paths that are (or would be, in dry_run) de-pathed.
    "skipped_reachable" lists pages that have zero inbound links but are reachable
    from the provenance graph and thus must NOT be removed.
    """
    kb_root = root or paths.knowledge_root()

    # Collect all wiki page rel-paths for the inbound-count bulk query.
    pages: list[tuple[str, str]] = []  # (page_type, rel_path)
    for page_type, path, _front, _body in walk_wiki_pages():
        rel = str(path.relative_to(kb_root))
        pages.append((page_type, rel))

    if not pages:
        return OperationResult(
            success=True,
            summary="remediate: no wiki pages found",
            data={"depathed": [], "skipped_reachable": []},
        )

    # Bulk inbound-count query (one DB call).
    rel_paths = [rel for _ptype, rel in pages]
    counts = search_index.inbound_counts(rel_paths)

    # Build provenance reachability set.
    prov_reachable = _provenance_reachable_rels(root=root)

    depathed: list[str] = []
    skipped_reachable: list[str] = []
    _queue = queue or IntentQueue()

    for page_type, rel in pages:
        if page_type in _DEPATH_EXEMPT_TYPES:
            continue
        if counts.get(rel, 0) > 0:
            # Has inbound links — safe, skip.
            continue
        # Zero inbound links. Check provenance reachability.
        if rel in prov_reachable:
            skipped_reachable.append(rel)
            continue
        # Genuine orphan: no inbound links AND not provenance-reachable.
        depathed.append(rel)
        if not dry_run:
            payload = {"op": "depath", "target_rel": rel, "reversible": True}
            identity = {"agent": "remediate", "operation": "depath"}
            iid = compute_intent_id(payload, identity, semantics="depath")
            intent = Intent(intent_id=iid, payload=payload, identity=identity)
            _queue.submit(intent)

    depathed.sort()
    skipped_reachable.sort()

    mode = "dry-run" if dry_run else "live"
    summary = (
        f"remediate ({mode}): {len(depathed)} candidate(s) for de-path, "
        f"{len(skipped_reachable)} provenance-reachable page(s) skipped"
    )
    return OperationResult(
        success=True,
        summary=summary,
        data={"depathed": depathed, "skipped_reachable": skipped_reachable},
    )
