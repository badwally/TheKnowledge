"""M45 citation-chains lint scope.

Walks the `synthesizes:` graph across synthesis pages and reports breaks:

- **dangling-synthesizes-ref**: `synthesizes:` entry points to a page that
  doesn't exist on disk (e.g., a renamed or deleted constituent).
- **synthesizes-shape**: malformed entries (not matching
  `(sources|synthesis)/<slug>`) or mixed-tier lists.
- **synthesizes-included-works-drift**: `## Included works` section absent
  or its wikilinks don't mirror `synthesizes:` 1:1.
- **aggregate-framing-without-synthesizes**: a synthesis page contains an
  aggregate-framing opener (`Based on the provided sources...`) but no
  `synthesizes:` frontmatter to back it — the page is making aggregate
  claims without an enumerated constituent set.

The validator already covers the in-page shape checks at write time
(`validate_synthesizes_integrity`). This lint adds the cross-page
dangling-reference check and surfaces existing pages that predate M45
and emit aggregate framing without `synthesizes:`.
"""

from __future__ import annotations

from pathlib import Path

from gateway import citations
from gateway import paths
from gateway.lint import LintFinding, SEVERITY_ERROR, SEVERITY_WARNING
from gateway.lint._walk import walk_wiki_pages


def run() -> list[LintFinding]:
    findings: list[LintFinding] = []

    # First pass: build the set of page identities that exist on disk so we
    # can resolve `synthesizes:` references.
    existing_identities: set[str] = set()
    pages: list[tuple[str, Path, dict, str]] = []
    for type_name, path, front, body in walk_wiki_pages():
        pages.append((type_name, path, front, body))
        rel = path.relative_to(paths.knowledge_root())
        parts = rel.with_suffix("").parts
        if parts and parts[0] == "wiki":
            existing_identities.add("/".join(parts[1:]))
    # Raw sources are addressable as `sources/<id>` too.
    raw_root = paths.raw_dir()
    if raw_root.exists():
        for source_type in paths.SOURCE_TYPES:
            d = raw_root / source_type
            if not d.exists():
                continue
            for p in d.glob("*.md"):
                existing_identities.add(f"sources/{p.stem}")

    for type_name, path, front, body in pages:
        if type_name != "synthesis":
            continue
        rel_path = str(path.relative_to(paths.knowledge_root()))
        synth = front.get("synthesizes") if isinstance(front, dict) else None

        if synth is None:
            # No synthesizes: but the page emits aggregate framing? Warn.
            if _has_aggregate_framing(body):
                findings.append(
                    LintFinding(
                        check="aggregate-framing-without-synthesizes",
                        severity=SEVERITY_WARNING,
                        message=(
                            "synthesis page contains aggregate-framing opener "
                            "(e.g., 'Based on the provided sources...') but has "
                            "no `synthesizes:` frontmatter; framing claims are "
                            "uncited — add `synthesizes:` and `## Included works` "
                            "to ground them, or rewrite the openers with citations"
                        ),
                        path=rel_path,
                    )
                )
            continue

        if not isinstance(synth, list) or not synth:
            continue  # validator handles shape/empty cases

        # Cross-page integrity: every entry must resolve to a page on disk.
        for entry in synth:
            if not isinstance(entry, str):
                continue
            if entry not in existing_identities:
                findings.append(
                    LintFinding(
                        check="dangling-synthesizes-ref",
                        severity=SEVERITY_ERROR,
                        message=(
                            f"`synthesizes:` entry {entry!r} does not exist on "
                            f"disk — rename, delete the entry, or restore the "
                            f"missing page"
                        ),
                        path=rel_path,
                        metadata={"target": entry},
                    )
                )

    return findings


def _has_aggregate_framing(body: str) -> bool:
    """Return True if any line in `body` looks like an aggregate-framing opener."""
    for raw_line in body.split("\n"):
        line = raw_line.strip()
        if not line:
            continue
        first_sentence = line.split(". ", 1)[0]
        if citations.is_aggregate_framing_opener(first_sentence):
            return True
    return False
