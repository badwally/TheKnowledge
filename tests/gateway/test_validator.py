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
    }
    body = "Food noise is reduced. [[sources/yt-abc123|invented]]\n\n## Summary\n\nSummary text. [[sources/yt-abc123|invented]]\n"
    result = v.validate_wiki_page(front, body, page_type="concept", draft=True)
    assert any(w.rule == "citation-verb-unknown" for w in result.warnings)
