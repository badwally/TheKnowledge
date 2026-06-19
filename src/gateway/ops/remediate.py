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

De-path intent payload (a typed CommitGate reversal intent — the gate's
``_apply_depath`` branch dispatches on ``reversal_type``, mirroring Task 1's
reversal precedent, and actually executes the tracked delete + provenance):
  {"reversal_type": "depath", "target_rel": "<wiki-rel-path>", "reversible": True,
   "policy_version": "corpus-rot-depath-policy-v1"}

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


def _normalize_to_wiki_rel(value: str, kb_root: Path) -> str | None:
    """Return a kb-relative ``wiki/*.md`` path for ``value``, or None.

    Handles BOTH forms a provenance node may carry:
    - an ABSOLUTE path (e.g. ``decision_basis["canonical_path"]``), and
    - an ALREADY-RELATIVE path (e.g. the nested ``merge_reattachment.target`` /
      ``.tombstone`` keys, which CommitGate writes as ``wiki/...`` rel-paths).
    """
    if not isinstance(value, str) or not value.endswith(".md"):
        return None
    # Already a wiki-relative path.
    if value.startswith("wiki/"):
        return value
    # An absolute path → make it kb-relative.
    try:
        rel = str(Path(value).relative_to(kb_root))
    except ValueError:
        return None
    return rel if rel.startswith("wiki/") else None


def _collect_wiki_rels(obj: object, kb_root: Path, out: set[str]) -> None:
    """Recursively collect every ``wiki/*.md`` rel-path reachable in ``obj``.

    Walks strings, lists, and nested dicts so a path buried in
    ``merge_reattachment.target`` / ``.tombstone`` (G8 reverse-merge state) or
    in a list-valued ``paths_touched`` is found — not just top-level string values.
    """
    if isinstance(obj, str):
        rel = _normalize_to_wiki_rel(obj, kb_root)
        if rel is not None:
            out.add(rel)
    elif isinstance(obj, dict):
        for v in obj.values():
            _collect_wiki_rels(v, kb_root, out)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            _collect_wiki_rels(v, kb_root, out)


def _provenance_reachable_rels(*, root: Path | None = None) -> set[str]:
    """Return the set of wiki/ rel-paths referenced ANYWHERE in any node's basis.

    Critical (G6): this includes NESTED dicts (e.g. ``merge_reattachment.target``
    and ``.tombstone`` — a live merge tombstone is reachable ONLY via that nested
    key and would otherwise be silently de-pathed) and list-valued path
    collections. Both absolute and already-relative path forms are normalized.
    """
    kb_root = root or paths.knowledge_root()
    nodes = provenance.read_nodes(root=root)
    reachable: set[str] = set()
    for node in nodes:
        basis = node.get("decision_basis") or {}
        _collect_wiki_rels(basis, kb_root, reachable)
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
            # The de-path is a typed CommitGate reversal intent: the gate's
            # _apply_depath branch (keyed on reversal_type, mirroring Task 1)
            # removes the page via the commit machinery, records a provenanced
            # node carrying the page content, and is reverse-applicable
            # (restore-depath). reversal_type — NOT a bare op key — is what the
            # gate dispatches on, so this actually executes.
            payload = {
                "reversal_type": "depath",
                "target_rel": rel,
                "reversible": True,
                "policy_version": "corpus-rot-depath-policy-v1",
            }
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
