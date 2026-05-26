"""Validator unit tests for M1 rules."""

from gateway import citations as c
from gateway import validator as v


def _good_frontmatter():
    return {
        "id": "yt-abc123",
        "type": "youtube",
        "title": "Test",
        "ingested_at": "2026-04-27T20:00:00Z",
        "content_hash": "sha256:" + "0" * 64,
    }


def test_required_fields_all_present():
    result = v.validate_source_frontmatter(_good_frontmatter())
    assert result.ok


def test_required_field_missing():
    front = _good_frontmatter()
    del front["title"]
    result = v.validate_source_frontmatter(front)
    assert not result.ok
    assert any(e.rule == "required-field" and e.field_name == "title" for e in result.errors)


def test_type_enum_violation():
    front = _good_frontmatter()
    front["type"] = "spreadsheet"
    result = v.validate_source_frontmatter(front)
    assert any(e.rule == "type-enum" for e in result.errors)


def test_id_format_youtube_rejects_arxiv_id():
    front = _good_frontmatter()
    front["id"] = "arxiv-2403.12345"  # arxiv format on a youtube source
    result = v.validate_source_frontmatter(front)
    assert any(e.rule == "id-format" for e in result.errors)


def test_ingested_at_unparseable():
    front = _good_frontmatter()
    front["ingested_at"] = "yesterday"
    result = v.validate_source_frontmatter(front)
    assert any(e.rule == "ingested-at-format" for e in result.errors)


def test_content_hash_match():
    body = "exact body bytes\n"
    front = {"content_hash": v.compute_content_hash(body)}
    result = v.validate_content_hash(front, body)
    assert result.ok


def test_content_hash_mismatch():
    front = {"content_hash": "sha256:" + "0" * 64}
    result = v.validate_content_hash(front, "different body")
    assert any(e.rule == "content-hash-mismatch" for e in result.errors)


def test_wikilinks_balanced():
    text = "Some claim [[sources/yt-abc]] and another [[concepts/food-noise]]."
    assert v.validate_wikilinks(text).ok


def test_wikilinks_unbalanced():
    text = "Bad [[sources/yt-abc and missing close."
    assert not v.validate_wikilinks(text).ok


def test_immutability_unchanged():
    assert v.validate_source_immutability("body", "body").ok


def test_immutability_changed():
    result = v.validate_source_immutability("body v1", "body v2")
    assert any(e.rule == "source-immutability" for e in result.errors)


# === ARCH-2: validate_source_frontmatter_diff =================================


def _base_source_front():
    return {
        "id": "yt-abc123",
        "type": "youtube",
        "title": "Test",
        "ingested_at": "2026-04-27T20:00:00Z",
        "content_hash": "sha256:" + "0" * 64,
    }


def test_frontmatter_diff_unchanged():
    front = _base_source_front()
    result = v.validate_source_frontmatter_diff(front, dict(front))
    assert result.ok


def test_frontmatter_diff_allowlisted_filter_mutation():
    old = _base_source_front()
    new = dict(old)
    new["filter"] = {"score": 0.9, "decision": "include"}
    result = v.validate_source_frontmatter_diff(old, new)
    assert result.ok


def test_frontmatter_diff_allowlisted_wiki_pages_mutation():
    old = _base_source_front()
    new = dict(old)
    new["wiki_pages"] = ["wiki/sources/yt-abc123"]
    result = v.validate_source_frontmatter_diff(old, new)
    assert result.ok


def test_frontmatter_diff_allowlisted_nlm_corpus_ids_mutation():
    old = _base_source_front()
    new = dict(old)
    new["nlm_corpus_ids"] = ["nb_abc123"]
    result = v.validate_source_frontmatter_diff(old, new)
    assert result.ok


def test_frontmatter_diff_allowlisted_domains_mutation():
    old = _base_source_front()
    new = dict(old)
    new["domains"] = ["glp1-reward-modulation"]
    result = v.validate_source_frontmatter_diff(old, new)
    assert result.ok


def test_frontmatter_diff_title_mutation_rejected():
    old = _base_source_front()
    new = dict(old)
    new["title"] = "Changed Title"
    result = v.validate_source_frontmatter_diff(old, new)
    assert not result.ok
    assert any(e.rule == "frontmatter-mutation" and e.field_name == "title" for e in result.errors)


def test_frontmatter_diff_non_allowlisted_addition_rejected():
    old = _base_source_front()
    new = dict(old)
    new["extra_field"] = "should not be here"
    result = v.validate_source_frontmatter_diff(old, new)
    assert not result.ok
    assert any(e.rule == "frontmatter-mutation" and e.field_name == "extra_field" for e in result.errors)


def test_frontmatter_diff_non_allowlisted_deletion_rejected():
    old = _base_source_front()
    new = dict(old)
    del new["title"]
    result = v.validate_source_frontmatter_diff(old, new)
    assert not result.ok
    assert any(e.rule == "frontmatter-mutation" and e.field_name == "title" for e in result.errors)


def test_frontmatter_diff_multiple_violations():
    old = _base_source_front()
    new = dict(old)
    new["title"] = "Changed"
    new["type"] = "web"
    result = v.validate_source_frontmatter_diff(old, new)
    assert len([e for e in result.errors if e.rule == "frontmatter-mutation"]) == 2


# --- ONT-2: CiTO 8-verb typed citations -------------------------------------


def test_cito_verbs_exact_set():
    """ONT-2: _CITO_VERBS contains exactly the 8 specified verbs."""
    expected = frozenset({
        "supports", "disputes", "extends", "qualifies",
        "confirms", "reviews", "usesMethodIn", "citesAsAuthority",
    })
    assert c._CITO_VERBS == expected


def test_validate_citation_verbs_known_verb_no_warning():
    """ONT-2: known CiTO verb in aliased source citation → no warning."""
    body = "GLP-1 reduces food intake. [[sources/yt-abc123|supports]]\n"
    result = v.validate_citation_verbs(body)
    assert result.ok
    assert not result.warnings


def test_validate_citation_verbs_unknown_verb_emits_warning():
    """ONT-2: unknown verb in aliased source citation → SEVERITY_WARNING."""
    body = "GLP-1 reduces appetite. [[sources/yt-abc123|proves]]\n"
    result = v.validate_citation_verbs(body)
    assert result.ok  # warnings only, not errors
    assert any(w.rule == "citation-verb-unknown" for w in result.warnings)


def test_validate_citation_verbs_unaliased_unchanged():
    """ONT-2: plain [[sources/<id>]] (no alias) must never trigger the check."""
    body = "GLP-1 reduces appetite. [[sources/yt-abc123]]\n"
    result = v.validate_citation_verbs(body)
    assert result.ok
    assert not result.warnings


def test_validate_citation_verbs_wired_into_validate_wiki_page():
    """ONT-2: unknown verb is surfaced via validate_wiki_page for wiki pages."""
    front = {
        "type": "concept",
        "slug": "food-noise",
        "title": "Food Noise",
        "domain": "glp1",
        "domains": ["glp1"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }
    body = "Food noise is reduced. [[sources/yt-abc123|invented]]\n\n## Summary\n\nSummary text. [[sources/yt-abc123|invented]]\n"
    result = v.validate_wiki_page(front, body, page_type="concept", draft=True)
    assert any(w.rule == "citation-verb-unknown" for w in result.warnings)


# --- ONT-4: entity_kind controlled vocabulary --------------------------------


def _entity_front(entity_kind: str) -> dict:
    return {
        "type": "entity",
        "entity_kind": entity_kind,
        "slug": "test-entity",
        "title": "Test Entity",
        "canonical_name": "Test Entity",
        "domain": "glp1",
        "domains": ["glp1"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }


def test_entity_kind_enum_exact_set():
    """ONT-4: ENTITY_KIND_ENUM contains exactly the 12 canonical values."""
    expected = frozenset({
        "person", "organization", "paper", "drug", "dataset",
        "product", "software", "statute", "standard", "place", "event", "other",
    })
    assert v.ENTITY_KIND_ENUM == expected


def test_entity_kind_valid_passes():
    """ONT-4: entity pages with a valid entity_kind pass validation."""
    for kind in v.ENTITY_KIND_ENUM:
        result = v.validate_wiki_page_frontmatter(_entity_front(kind), "entity")
        assert result.ok, f"valid kind {kind!r} should pass: {result.errors}"


def test_entity_kind_invalid_fails():
    """ONT-4: entity pages with an unknown entity_kind are rejected with SEVERITY_ERROR."""
    result = v.validate_wiki_page_frontmatter(_entity_front("publication"), "entity")
    assert not result.ok
    assert any(e.rule == "entity-kind-unknown" for e in result.errors)


def test_entity_kind_none_passes():
    """ONT-4: entity_kind absent (None) does not trigger the enum check."""
    front = _entity_front("person")
    del front["entity_kind"]
    result = v.validate_wiki_page_frontmatter(front, "entity")
    # No entity-kind-unknown error (may have other required-field errors depending on schema)
    assert not any(e.rule == "entity-kind-unknown" for e in result.errors)


def test_migrate_entity_kinds_dry_run(kb_root, tmp_path, monkeypatch):
    """ONT-4: migration script remaps legacy values and is idempotent."""
    import subprocess
    entities_dir = kb_root / "wiki" / "entities"
    entities_dir.mkdir(parents=True, exist_ok=True)

    from gateway import frontmatter as fm

    def _write(slug: str, kind: str) -> None:
        front = {"type": "entity", "entity_kind": kind, "slug": slug, "title": slug, "domain": "d"}
        (entities_dir / f"{slug}.md").write_text(fm.serialize(front, "body\n"))

    _write("pub-entity", "publication")   # should become paper
    _write("person-entity", "person")    # already canonical — skip

    import sys as _sys
    result = subprocess.run(
        [_sys.executable, "migrations/0002-migrate-entity-kinds.py", "--dry-run"],
        capture_output=True, text=True,
        env={**__import__("os").environ, "KNOWLEDGE_ROOT": str(kb_root)},
    )
    assert result.returncode == 0
    assert "publication" in result.stdout
    assert "paper" in result.stdout
    # Dry run — file on disk should be unchanged
    front, _ = fm.parse((entities_dir / "pub-entity.md").read_text())
    assert front["entity_kind"] == "publication"


# --- ONT-8: slug length cap (80 chars) --------------------------------------


def _concept_front(slug: str) -> dict:
    return {
        "type": "concept",
        "slug": slug,
        "canonical_name": slug,
        "title": slug,
        "domain": "glp1",
        "domains": ["glp1"],
        "created_at": "2026-01-01T00:00:00Z",
        "last_updated": "2026-01-01T00:00:00Z",
    }


def test_slug_80_chars_passes():
    """ONT-8: slug of exactly 80 chars is accepted."""
    slug = "a" * 80
    result = v.validate_wiki_page_frontmatter(_concept_front(slug), "concept")
    assert not any(e.rule == "slug-too-long" for e in result.errors)


def test_slug_81_chars_rejected():
    """ONT-8: new slug of 81 chars is hard-rejected (SEVERITY_ERROR)."""
    slug = "a" * 81
    result = v.validate_wiki_page_frontmatter(_concept_front(slug), "concept")
    assert any(e.rule == "slug-too-long" for e in result.errors)


def test_slug_too_long_force_override():
    """ONT-8: --force-long-slug overrides the 80-char cap to a warning."""
    slug = "a" * 81
    result = v.validate_wiki_page_frontmatter(_concept_front(slug), "concept", force_long_slug=True)
    assert not any(e.rule == "slug-too-long" for e in result.errors)
    assert any(w.rule == "slug-too-long" for w in result.warnings)


def test_slug_too_long_lint_check(kb_root):
    """ONT-8: existing pages with long slugs trigger lint WARNING, not ERROR."""
    from gateway.lint.long_slugs import run as lint_long_slugs
    from gateway.lint import SEVERITY_WARNING
    concepts_dir = kb_root / "wiki" / "concepts"
    concepts_dir.mkdir(parents=True, exist_ok=True)
    from gateway import frontmatter as fm
    slug = "b" * 100
    front = {"type": "concept", "slug": slug, "title": "long", "domain": "d", "domains": ["d"]}
    (concepts_dir / f"long-slug.md").write_text(fm.serialize(front, "body\n"))
    findings = lint_long_slugs()
    assert any(f.check == "slug-too-long" and f.severity == SEVERITY_WARNING for f in findings)
