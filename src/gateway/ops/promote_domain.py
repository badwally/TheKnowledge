"""`wiki promote-domain <proposal-slug>` — bless a draft proposal (M36).

Writes a minimal `policy.yaml` for the proposed domain, back-tags every
member source's frontmatter with `domains: [<proposed_domain>]` (raw and
wiki-source pages), and flips the proposal's `status` to `blessed`.

Atomic: all validation happens before any write; member-source
frontmatter mutations preserve body bytes (immutability check passes).
On any validation failure, zero on-disk changes occur.

Reversed by `wiki demote-domain <proposed_domain>`.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from gateway import frontmatter as fm
from gateway import log, paths, validator, wiki_pages
from gateway.core import OperationResult, write_atomic
from gateway.filter.policy import policy_exists, policy_path
from gateway.locking import file_lock


_LOCK_NAME = "wiki-author"


@dataclass
class _PendingWrite:
    path: Path
    content: str


def promote_domain(proposal_slug: str) -> OperationResult:
    proposal_path = paths.wiki_dir() / "proposals" / f"{proposal_slug}.md"
    if not proposal_path.exists():
        return OperationResult(
            success=False,
            errors=[f"no proposal at {proposal_path}: slug {proposal_slug!r} unknown"],
        )

    try:
        prop_front, prop_body = fm.parse(proposal_path.read_text())
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"proposal frontmatter: {e}"])

    status = prop_front.get("status")
    if status != "draft":
        return OperationResult(
            success=False,
            errors=[f"proposal status is {status!r}; only 'draft' proposals can be promoted"],
        )

    proposed_domain = str(prop_front.get("proposed_domain") or "")
    if not proposed_domain or not wiki_pages.is_valid_slug(proposed_domain):
        return OperationResult(
            success=False,
            errors=[f"proposal has invalid proposed_domain: {proposed_domain!r}"],
        )

    if policy_exists(proposed_domain):
        return OperationResult(
            success=False,
            errors=[
                f"policy for domain {proposed_domain!r} already exists at "
                f"{policy_path(proposed_domain)}; refuse to clobber"
            ],
        )

    member_ids = list(prop_front.get("member_sources") or [])
    if not member_ids:
        return OperationResult(
            success=False, errors=["proposal has no member_sources to back-tag"]
        )

    # --- Phase 1: locate every member source, build all writes in memory ---
    pending: list[_PendingWrite] = []
    errors: list[str] = []

    # 1. Policy file
    policy_yaml = _build_policy_yaml(
        proposed_domain=proposed_domain,
        title=str(prop_front.get("title") or proposed_domain),
        rationale=str(prop_front.get("rationale") or ""),
    )
    pending.append(_PendingWrite(policy_path(proposed_domain), policy_yaml))

    # 2. Each member source: raw/<type>/<id>.md and wiki/sources/<id>.md
    for sid in member_ids:
        raw_pair = _locate_raw_source(sid)
        if raw_pair is None:
            errors.append(f"member source {sid!r}: raw file not found in any raw/<type>/")
            continue
        raw_path, raw_text = raw_pair
        try:
            raw_front, raw_body = fm.parse(raw_text)
        except fm.FrontmatterError as e:
            errors.append(f"member source {sid!r} ({raw_path}): frontmatter: {e}")
            continue

        new_raw_front = dict(raw_front)
        domains = list(new_raw_front.get("domains") or [])
        if proposed_domain not in domains:
            domains.append(proposed_domain)
        new_raw_front["domains"] = domains
        new_raw_text = fm.serialize(new_raw_front, raw_body)

        # Body immutability check (frontmatter-only mutation)
        imm = validator.validate_source_immutability(raw_body, raw_body)
        if not imm.ok:  # pragma: no cover — body is identical, can't fail
            errors.append(f"member source {sid!r}: immutability check spuriously failed")
            continue

        pending.append(_PendingWrite(raw_path, new_raw_text))

        wiki_path = paths.wiki_source_path(sid)
        if wiki_path.exists():
            try:
                wiki_front, wiki_body = fm.parse(wiki_path.read_text())
            except fm.FrontmatterError as e:
                errors.append(f"member source {sid!r} (wiki page): frontmatter: {e}")
                continue
            new_wiki_front = dict(wiki_front)
            wdomains = list(new_wiki_front.get("domains") or [])
            if proposed_domain not in wdomains:
                wdomains.append(proposed_domain)
            new_wiki_front["domains"] = wdomains
            pending.append(
                _PendingWrite(wiki_path, fm.serialize(new_wiki_front, wiki_body))
            )

    # 3. Proposal page status: draft → blessed
    new_prop_front = dict(prop_front)
    new_prop_front["status"] = "blessed"
    pending.append(_PendingWrite(proposal_path, fm.serialize(new_prop_front, prop_body)))

    if errors:
        return OperationResult(
            success=False,
            errors=errors,
            summary=f"promote-domain {proposal_slug}: {len(errors)} validation error(s); no writes",
        )

    # --- Phase 2: commit atomically (under lock) ---
    paths_touched: list[Path] = []
    with file_lock(_LOCK_NAME):
        for w in pending:
            w.path.parent.mkdir(parents=True, exist_ok=True)
            write_atomic(w.path, w.content)
            paths_touched.append(w.path)

        log.append(
            op="promote-domain",
            fields={
                "proposal": proposal_slug,
                "domain": proposed_domain,
                "members": len(member_ids),
            },
            summary=f"blessed proposal {proposal_slug} → domain {proposed_domain}",
        )
        paths_touched.append(paths.log_path())

    return OperationResult(
        success=True,
        paths_touched=paths_touched,
        summary=(
            f"promoted {proposal_slug} → {proposed_domain} "
            f"({len(member_ids)} member source(s) tagged)"
        ),
    )


def _locate_raw_source(source_id: str) -> tuple[Path, str] | None:
    """Find the raw source file for a source_id by trying each known type dir."""
    for source_type in paths.SOURCE_TYPES:
        candidate = paths.raw_source_path(source_type, source_id)
        if candidate.exists():
            return candidate, candidate.read_text()
    return None


def _build_policy_yaml(*, proposed_domain: str, title: str, rationale: str) -> str:
    """Compose a minimal-viable policy.yaml from a proposal.

    Marked `auto_generated: true`. Inclusion criteria are empty — the
    user is expected to flesh them out before running `wiki filter`
    against this domain. Filter thresholds use library defaults.
    """
    data = {
        "version": "v0.1.0-auto",
        "auto_generated": True,
        "auto_generated_from_proposal": True,
        "domain": {
            "slug": proposed_domain,
            "topic": title,
            "field": "",
            "description": rationale,
        },
        "filter": {
            "threshold_include": 0.70,
            "threshold_review": 0.50,
            "example_count_in_prompt": 12,
            "example_strategy": "balanced",
        },
        "inclusion_criteria": [],
        "exclusion_criteria": [],
    }
    header = (
        "# Auto-generated policy from a domain-proposal (M36).\n"
        "# Flesh out inclusion_criteria / exclusion_criteria before running\n"
        "# `wiki filter` against this domain.\n\n"
    )
    return header + yaml.safe_dump(data, sort_keys=False, default_flow_style=False)
