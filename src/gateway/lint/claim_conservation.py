"""Claim-conservation lint check — F1.

Every committed intent's payload ``## Claims`` bullets must appear in the
canonical corpus page. This catches lost-update scenarios where a merge,
rebase, or manual edit silently drops a claim that was successfully queued
and committed.

Merge accounting: when intent B was merged into A (tombstone at B's path with
``merged_into: A-slug``), B's payload claims are expected on A's canonical
page. The check follows the tombstone redirect instead of checking B's path.

Enumerated records: ``.knowledge/intents/committed/`` — all terminal committed
records whose ``payload`` carries a ``body`` with a ``## Claims`` section.
(There is no separate ``merged/`` directory; merged intents are in ``committed/``
with ``result.dedup == "merged"`` and a result ``canonical_path``.)

The ``## Claims`` parser is the same bullet-extraction logic used by
``CommitGate._claim_union``: lines that start with ``- `` under the
``## Claims`` heading, stopping at the next heading or EOF.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from gateway import frontmatter as fm, paths
from gateway.lint import LintFinding, SEVERITY_ERROR


_CLAIMS_HEADING_RE = re.compile(r"^#{1,6}\s+claims\s*$", re.IGNORECASE | re.MULTILINE)
_HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)


def _parse_claim_bullets(body: str) -> list[str]:
    """Extract ``- `` bullet lines from the ``## Claims`` section of ``body``.

    Returns the raw bullet lines (stripped of trailing whitespace) in order.
    Matches exactly the logic CommitGate._claim_union uses: lines starting with
    ``- `` that appear under the first ``## Claims`` (case-insensitive) heading
    and before the next heading (or EOF).
    """
    m = _CLAIMS_HEADING_RE.search(body)
    if not m:
        return []
    section_start = m.end()
    # Find the next heading after Claims (to bound the section).
    next_heading = _HEADING_RE.search(body, section_start)
    section_end = next_heading.start() if next_heading else len(body)
    section = body[section_start:section_end]
    bullets: list[str] = []
    for line in section.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(stripped)
    return bullets


def _resolve_canonical_path(
    record: dict, kb_root: Path
) -> Path | None:
    """Return the canonical on-disk Path for the claims from ``record``.

    Priority:
    1. ``result["canonical_path"]`` — absolute path written by CommitGate on commit.
    2. Derive from identity (``page_type`` + ``canonical_name``/``title``) as a fallback.

    If the canonical page has a ``merged_into`` tombstone, follow the redirect.
    """
    # Try explicit canonical_path from CommitGate result first.
    result = record.get("result") or {}
    canon_str = result.get("canonical_path")
    if canon_str:
        p = Path(canon_str)
        if p.exists():
            return _follow_tombstone(p, kb_root)

    # Fallback: look at declared_writes to find the written path.
    declared = record.get("declared_writes") or []
    if declared:
        for rel in declared:
            p = kb_root / rel
            if p.exists() and str(rel).startswith("wiki/"):
                return _follow_tombstone(p, kb_root)

    return None


def _follow_tombstone(path: Path, kb_root: Path) -> Path:
    """If ``path`` is a tombstone (``merged_into`` frontmatter), return the canonical."""
    try:
        content = path.read_text(errors="replace")
        front, _ = fm.parse(content)
    except Exception:
        return path

    merged_into = front.get("merged_into")
    if not merged_into:
        return path

    # merged_into is a slug like "entities/ozempic"; resolve to wiki/<slug>.md
    slug = merged_into.lstrip("wiki/")
    # slug may be e.g. "entities/ozempic" or "ozempic" depending on record shape
    candidate = kb_root / "wiki" / f"{slug}.md"
    if candidate.exists():
        return candidate
    # Also try without the leading wiki/ directory structure assumption
    for wiki_sub in ("entities", "concepts", "synthesis", "sources", "mocs"):
        candidate2 = kb_root / "wiki" / wiki_sub / f"{slug}.md"
        if candidate2.exists():
            return candidate2
    # If slug already contains a slash, try as-is under wiki/
    if "/" in slug:
        candidate3 = kb_root / "wiki" / f"{slug}.md"
        if candidate3.exists():
            return candidate3
    return path  # Can't follow tombstone → check the tombstone body itself


def run() -> list[LintFinding]:
    """Enumerate committed intents and verify every payload claim is in the corpus.

    Returns one LintFinding per claim bullet not found in the canonical page.
    """
    kb_root = paths.knowledge_root()
    committed_dir = paths.intents_dir() / "committed"
    if not committed_dir.exists():
        return []

    findings: list[LintFinding] = []

    for intent_file in sorted(committed_dir.glob("*.json")):
        try:
            record = json.loads(intent_file.read_text())
        except Exception:
            continue

        payload = record.get("payload") or {}
        body = payload.get("body") or ""
        if not body:
            continue

        claim_bullets = _parse_claim_bullets(body)
        if not claim_bullets:
            continue

        # Find the canonical page for this intent's claims.
        canon_path = _resolve_canonical_path(record, kb_root)
        if canon_path is None:
            # Can't locate the page — skip (coverage_gap handles missing pages).
            continue

        try:
            canon_content = canon_path.read_text(errors="replace")
            _front, canon_body = fm.parse(canon_content)
        except Exception:
            # If we can't read the page, report all claims as missing.
            for bullet in claim_bullets:
                findings.append(LintFinding(
                    check="claim-conservation",
                    severity=SEVERITY_ERROR,
                    message=f"missing claim (canonical page unreadable): {bullet!r}",
                    path=str(canon_path.relative_to(kb_root)),
                    metadata={
                        "intent_id": record.get("intent_id"),
                        "claim": bullet,
                    },
                ))
            continue

        # For each payload claim, verify it appears in the canonical page body.
        # We check the full body (including Claims section) for the exact bullet text,
        # as _claim_union merges bullets by exact string match.
        canon_lines_set = {ln.strip() for ln in canon_body.splitlines()}
        canon_rel = str(canon_path.relative_to(kb_root))

        for bullet in claim_bullets:
            if bullet not in canon_lines_set:
                findings.append(LintFinding(
                    check="claim-conservation",
                    severity=SEVERITY_ERROR,
                    message=f"missing claim not found in canonical page: {bullet!r}",
                    path=canon_rel,
                    metadata={
                        "intent_id": record.get("intent_id"),
                        "claim": bullet,
                    },
                ))

    return findings
