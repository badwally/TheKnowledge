"""`wiki reject-proposal <slug>` — delete a draft domain-proposal (M36).

Refuses to delete proposals that have been blessed (status != "draft").
A blessed proposal must be demoted via `wiki demote-domain` first.
"""

from __future__ import annotations

from gateway import frontmatter as fm
from gateway import log, paths
from gateway.core import OperationResult
from gateway.locking import file_lock


_LOCK_NAME = "wiki-author"


def reject_proposal(proposal_slug: str) -> OperationResult:
    proposal_path = paths.wiki_dir() / "proposals" / f"{proposal_slug}.md"
    if not proposal_path.exists():
        return OperationResult(
            success=False, errors=[f"no proposal at {proposal_path}"]
        )

    try:
        front, _ = fm.parse(proposal_path.read_text())
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"frontmatter: {e}"])

    status = front.get("status")
    if status != "draft":
        return OperationResult(
            success=False,
            errors=[
                f"proposal status is {status!r}; only 'draft' proposals can be rejected. "
                "Use `wiki demote-domain <domain>` to reverse a blessed proposal first."
            ],
        )

    with file_lock(_LOCK_NAME):
        proposal_path.unlink()
        log.append(
            op="reject-proposal",
            fields={"proposal": proposal_slug},
            summary=f"rejected proposal {proposal_slug}",
        )

    return OperationResult(
        success=True,
        paths_touched=[proposal_path, paths.log_path()],
        summary=f"rejected proposal {proposal_slug}",
    )
