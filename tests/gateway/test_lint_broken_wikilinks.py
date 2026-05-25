"""Tests for QUAL-4: broken-wikilinks lint scope."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm, paths, validator
from gateway.lint import broken_wikilinks
from gateway.ops.lint import KNOWN_CHECKS


# --- helpers ------------------------------------------------------------------


def _write_wiki_page(kind: str, slug: str, body: str) -> Path:
    schemas = {
        "concept": {
            "type": "concept",
            "slug": slug,
            "canonical_name": slug.replace("-", " "),
            "domains": ["d-test"],
        },
        "entity": {
            "type": "entity",
            "slug": slug,
            "canonical_name": slug.replace("-", " "),
            "domains": ["d-test"],
        },
        "source": {
            "type": "source",
            "slug": slug,
            "source_type": "web",
            "source_id": f"web-2026-04-01-{slug[:12]}",
            "title": slug,
            "domains": ["d-test"],
        },
    }
    _KIND_TO_DIR = {"entity": "entities", "concept": "concepts", "source": "sources"}
    dir_name = _KIND_TO_DIR.get(kind, f"{kind}s")
    front = schemas.get(kind, {"type": kind, "slug": slug})
    target = paths.wiki_dir() / dir_name / f"{slug}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(fm.serialize(front, body))
    return target


# --- tests -------------------------------------------------------------------


def test_broken_wikilinks_clean_when_no_pages(kb_root):
    findings = broken_wikilinks.run()
    assert findings == []


def test_broken_wikilinks_passes_for_valid_sources_link(kb_root):
    # Create the source page first.
    _write_wiki_page("source", "yt-abc123", "# Source\n\nBody.\n")
    # Create a concept that cites it.
    _write_wiki_page(
        "concept", "food-noise",
        "# Food Noise\n\n## Summary\n\nA claim. [[sources/yt-abc123]]\n\n## Key claims\n\n- [[sources/yt-abc123]]\n\n## Sources\n\n- [[sources/yt-abc123]]\n\n## Related\n\n-\n"
    )
    findings = broken_wikilinks.run()
    broken = [f for f in findings if f.metadata.get("target", "").startswith("sources/")]
    assert broken == []


def test_broken_wikilinks_errors_on_missing_source(kb_root):
    _write_wiki_page(
        "concept", "concept-a",
        "# Concept A\n\n## Summary\n\nA claim. [[sources/yt-missing]]\n\n## Key claims\n\n- [[sources/yt-missing]]\n\n## Sources\n\n- [[sources/yt-missing]]\n\n## Related\n\n-\n"
    )
    findings = broken_wikilinks.run()
    broken = [f for f in findings if f.metadata.get("target") == "sources/yt-missing"]
    assert len(broken) == 1
    assert broken[0].severity == "error"


def test_broken_wikilinks_passes_for_valid_entity_link(kb_root):
    _write_wiki_page("entity", "semaglutide", "# Semaglutide\n\nBody.\n")
    _write_wiki_page(
        "concept", "food-noise2",
        "# Food Noise\n\n## Summary\n\nA claim [[entities/semaglutide]].\n\n## Key claims\n\n- [[entities/semaglutide]]\n\n## Sources\n\n-\n\n## Related\n\n-\n"
    )
    findings = broken_wikilinks.run()
    broken = [f for f in findings if f.metadata.get("target") == "entities/semaglutide"]
    assert broken == []


def test_broken_wikilinks_errors_on_missing_entity(kb_root):
    _write_wiki_page(
        "concept", "concept-b",
        "# Concept B\n\n## Summary\n\nSee [[entities/unknown-entity]].\n\n## Key claims\n\n-\n\n## Sources\n\n-\n\n## Related\n\n-\n"
    )
    findings = broken_wikilinks.run()
    broken = [f for f in findings if f.metadata.get("target") == "entities/unknown-entity"]
    assert len(broken) >= 1
    assert broken[0].severity == "error"


def test_broken_wikilinks_aliased_link_is_warning(kb_root):
    """[[target|alias]] where target doesn't exist → warning (forward-reference)."""
    _write_wiki_page(
        "concept", "concept-c",
        "# Concept C\n\n## Summary\n\nSee [[entities/future-entity|Future Entity]].\n\n## Key claims\n\n-\n\n## Sources\n\n-\n\n## Related\n\n-\n"
    )
    findings = broken_wikilinks.run()
    fwd = [f for f in findings if f.metadata.get("target") == "entities/future-entity"]
    assert len(fwd) >= 1
    assert fwd[0].severity == "warning"


def test_broken_wikilinks_nlm_exempt(kb_root):
    """[[nlm:<uuid>]] must not be flagged."""
    _write_wiki_page(
        "concept", "concept-d",
        "# Concept D\n\n## Summary\n\nSynthesis [[nlm:a1b2c3d4-e5f6-7890-abcd-ef1234567890]].\n\n## Key claims\n\n-\n\n## Sources\n\n-\n\n## Related\n\n-\n"
    )
    findings = broken_wikilinks.run()
    nlm = [f for f in findings if "nlm:" in f.metadata.get("target", "")]
    assert nlm == []


def test_broken_wikilinks_registered_in_known_checks():
    assert "broken-wikilinks" in KNOWN_CHECKS
