"""`wiki demote-domain <slug>` — reverse a `promote-domain` (M36).

Removes `<slug>` from every source's `domains:` frontmatter, deletes the
auto-generated policy file, flips any blessed proposal back to draft.
Idempotent: removing a tag that's not present is a no-op; deleting a
missing policy is a no-op.

Refuses to delete a policy that is not marked `auto_generated_from_proposal: true`
— that protects hand-authored policies from accidental demotion.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from gateway import frontmatter as fm
from gateway import log, paths
from gateway.core import OperationResult, write_atomic
from gateway.filter.policy import policy_exists, policy_path
from gateway.locking import file_lock


_LOCK_NAME = "wiki-author"


@dataclass
class _PendingDelete:
    path: Path


@dataclass
class _PendingWrite:
    path: Path
    content: str


def demote_domain(domain_slug: str) -> OperationResult:
    pending_writes: list[_PendingWrite] = []
    pending_deletes: list[_PendingDelete] = []
    errors: list[str] = []

    # 1. Find the proposal that promoted this domain (any proposal whose
    #    `proposed_domain` matches and whose status is `blessed`).
    proposals_dir = paths.wiki_dir() / "proposals"
    proposal_path: Path | None = None
    member_ids: list[str] = []
    if proposals_dir.exists():
        for path in sorted(proposals_dir.glob("*.md")):
            try:
                front, body = fm.parse(path.read_text())
            except fm.FrontmatterError:
                continue
            if (
                front.get("proposed_domain") == domain_slug
                and front.get("status") == "blessed"
            ):
                proposal_path = path
                member_ids = list(front.get("member_sources") or [])
                new_front = dict(front)
                new_front["status"] = "draft"
                pending_writes.append(_PendingWrite(path, fm.serialize(new_front, body)))
                break

    # 2. Sanity: at least one of (proposal, policy file) must exist
    pol_path = policy_path(domain_slug)
    if proposal_path is None and not pol_path.exists():
        return OperationResult(
            success=False,
            errors=[
                f"no blessed proposal for domain {domain_slug!r} and no policy at "
                f"{pol_path}; nothing to demote"
            ],
        )

    # 3. Plan the policy deletion (only if auto-generated-from-proposal)
    if pol_path.exists():
        try:
            policy_data = yaml.safe_load(pol_path.read_text()) or {}
        except yaml.YAMLError as e:
            errors.append(f"policy YAML at {pol_path}: {e}")
            policy_data = {}
        if errors:
            return OperationResult(success=False, errors=errors)
        if not policy_data.get("auto_generated_from_proposal"):
            return OperationResult(
                success=False,
                errors=[
                    f"policy at {pol_path} is not marked "
                    "`auto_generated_from_proposal: true`; refusing to delete"
                ],
            )
        pending_deletes.append(_PendingDelete(pol_path))

    # 4. Plan untagging on every source that carries this domain.
    #    Use member_ids from the proposal if available; otherwise scan.
    sources_to_check = list(member_ids) if member_ids else _scan_source_ids_with_domain(domain_slug)
    for sid in sources_to_check:
        for source_type in paths.SOURCE_TYPES:
            raw = paths.raw_source_path(source_type, sid)
            if raw.exists():
                try:
                    front, body = fm.parse(raw.read_text())
                except fm.FrontmatterError as e:
                    errors.append(f"raw source {sid!r}: {e}")
                    break
                domains = list(front.get("domains") or [])
                if domain_slug in domains:
                    domains = [d for d in domains if d != domain_slug]
                    new_front = dict(front)
                    new_front["domains"] = domains
                    pending_writes.append(_PendingWrite(raw, fm.serialize(new_front, body)))
                break
        wiki = paths.wiki_source_path(sid)
        if wiki.exists():
            try:
                front, body = fm.parse(wiki.read_text())
            except fm.FrontmatterError as e:
                errors.append(f"wiki source page {sid!r}: {e}")
                continue
            domains = list(front.get("domains") or [])
            if domain_slug in domains:
                domains = [d for d in domains if d != domain_slug]
                new_front = dict(front)
                new_front["domains"] = domains
                pending_writes.append(_PendingWrite(wiki, fm.serialize(new_front, body)))

    if errors:
        return OperationResult(success=False, errors=errors)

    paths_touched: list[Path] = []
    with file_lock(_LOCK_NAME):
        for w in pending_writes:
            write_atomic(w.path, w.content)
            paths_touched.append(w.path)
        for d in pending_deletes:
            try:
                d.path.unlink()
                paths_touched.append(d.path)
            except FileNotFoundError:  # pragma: no cover — race
                pass
            # Clean up the parent directory if empty
            parent = d.path.parent
            try:
                parent.rmdir()
            except OSError:
                pass

        log.append(
            op="demote-domain",
            fields={
                "domain": domain_slug,
                "untagged_sources": sum(
                    1 for w in pending_writes if w.path.parent.name in ("sources",)
                    or w.path.parent.parent.name == "raw"
                ),
            },
            summary=f"demoted domain {domain_slug}",
        )
        paths_touched.append(paths.log_path())

    return OperationResult(
        success=True,
        paths_touched=paths_touched,
        summary=f"demoted {domain_slug} ({len(pending_writes)} files updated)",
    )


def _scan_source_ids_with_domain(domain_slug: str) -> list[str]:
    """Fallback: scan all wiki source pages for `domains:` containing the slug."""
    out: list[str] = []
    sources_dir = paths.wiki_dir() / "sources"
    if not sources_dir.exists():
        return out
    for path in sources_dir.glob("*.md"):
        try:
            front, _ = fm.parse(path.read_text())
        except fm.FrontmatterError:
            continue
        if domain_slug in (front.get("domains") or []):
            sid = str(front.get("source_id") or path.stem)
            out.append(sid)
    return out
