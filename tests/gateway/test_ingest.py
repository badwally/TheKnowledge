"""End-to-end tests for the M1 `wiki ingest` operation."""

from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway.ops.ingest import _gather_existing_pages, ingest_canonical
from gateway.plan import build_plan_user_prompt


def _write_source(tmp: Path, name: str, content: str) -> Path:
    p = tmp / name
    p.write_text(content)
    return p


def test_ingest_happy_path(kb_root, make_source, tmp_path):
    source_text = make_source()
    src = _write_source(tmp_path, "input.md", source_text)

    result = ingest_canonical(src)

    assert result.success, result.errors
    assert not result.no_op

    raw = paths.raw_source_path("youtube", "yt-testABC_123")
    wiki = paths.wiki_source_path("yt-testABC_123")
    assert raw.exists(), "raw source file not written"
    assert wiki.exists(), "wiki source page not written"

    # Wiki source page is well-formed canonical markdown
    front, body = fm.parse(wiki.read_text())
    assert front["type"] == "source"
    assert front["source_id"] == "yt-testABC_123"
    assert "## Summary" in body

    # Index updated
    index_text = paths.index_path().read_text()
    assert "sources/yt-testABC_123" in index_text

    # Log appended
    log_text = paths.log_path().read_text()
    assert "ingest" in log_text
    assert "yt-testABC_123" in log_text


def test_ingest_idempotent_noop(kb_root, make_source, tmp_path):
    source_text = make_source()
    src = _write_source(tmp_path, "input.md", source_text)

    first = ingest_canonical(src)
    assert first.success and not first.no_op

    second = ingest_canonical(src)
    assert second.success
    assert second.no_op
    assert "already ingested" in second.summary


def test_ingest_backfills_missing_wiki_page(kb_root, make_source, tmp_path):
    """Convergent idempotency: when raw exists but wiki/sources/ page is missing
    (e.g., research / batch-ingest materialized raw without writing wiki summary),
    a subsequent ingest backfills the page rather than returning a misleading no-op."""
    source_text = make_source()
    src = _write_source(tmp_path, "input.md", source_text)

    first = ingest_canonical(src)
    assert first.success

    wiki = paths.wiki_source_path("yt-testABC_123")
    assert wiki.exists()
    wiki.unlink()  # simulate the orphan-raw state

    second = ingest_canonical(src)
    assert second.success
    assert not second.no_op
    assert "backfilled wiki page" in second.summary
    assert wiki.exists()

    front, body = fm.parse(wiki.read_text())
    assert front["source_id"] == "yt-testABC_123"

    # Log records the backfill explicitly
    log_text = paths.log_path().read_text()
    assert "backfilled_wiki_page" in log_text


def test_ingest_does_not_backfill_user_excluded(kb_root, make_source, tmp_path):
    """A source explicitly excluded by user_correction should not get a wiki page
    backfilled by a later ingest, even if its raw file exists."""
    source_text = make_source(
        extra_front={
            "filter": {
                "user_correction": {
                    "decision": "exclude",
                    "score": 0.0,
                    "decided_at": "2026-05-09T22:00:00Z",
                    "rationale": "Off-topic",
                }
            }
        },
    )
    src = _write_source(tmp_path, "excluded.md", source_text)
    raw = paths.raw_source_path("youtube", "yt-testABC_123")
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(source_text)
    # No wiki page intentionally — the source is excluded.

    result = ingest_canonical(src)
    assert result.success
    assert result.no_op
    assert not paths.wiki_source_path("yt-testABC_123").exists()


def test_ingest_noop_when_wiki_page_already_present(kb_root, make_source, tmp_path):
    """Re-ingesting a fully-canonical source stays a true no-op (no spurious backfill or log entry)."""
    source_text = make_source()
    src = _write_source(tmp_path, "input.md", source_text)

    first = ingest_canonical(src)
    assert first.success

    log_size_before = paths.log_path().stat().st_size

    second = ingest_canonical(src)
    assert second.success
    assert second.no_op
    assert paths.log_path().stat().st_size == log_size_before


def test_ingest_malformed_frontmatter(kb_root, tmp_path):
    src = _write_source(tmp_path, "bad.md", "no frontmatter here at all\n")
    result = ingest_canonical(src)
    assert not result.success
    assert any("frontmatter" in e for e in result.errors)


def test_ingest_missing_required_field(kb_root, make_source, tmp_path):
    # Build a source then strip out 'title'
    source_text = make_source()
    front, body = fm.parse(source_text)
    del front["title"]
    bad_text = fm.serialize(front, body)
    src = _write_source(tmp_path, "missing.md", bad_text)

    result = ingest_canonical(src)
    assert not result.success
    assert any("required-field" in e and "title" in e for e in result.errors)

    # No partial writes
    assert not paths.raw_source_path("youtube", "yt-testABC_123").exists()
    assert not paths.wiki_source_path("yt-testABC_123").exists()


def test_ingest_content_hash_mismatch(kb_root, make_source, tmp_path):
    # Build a source then mutate the body so the declared hash no longer matches
    source_text = make_source(body="declared body\n")
    front, _ = fm.parse(source_text)
    bad_text = fm.serialize(front, "tampered body\n")
    src = _write_source(tmp_path, "tampered.md", bad_text)

    result = ingest_canonical(src)
    assert not result.success
    assert any("content-hash-mismatch" in e for e in result.errors)


def test_ingest_wrong_id_format(kb_root, make_source, tmp_path):
    source_text = make_source(id_="not-a-valid-yt-id")
    src = _write_source(tmp_path, "bad-id.md", source_text)
    result = ingest_canonical(src)
    assert not result.success
    assert any("id-format" in e for e in result.errors)


def test_ingest_immutability_violated(kb_root, make_source, tmp_path):
    # First ingest with body A
    source_text_a = make_source(id_="yt-immutA", body="original body\n")
    src_a = _write_source(tmp_path, "a.md", source_text_a)
    first = ingest_canonical(src_a)
    assert first.success and not first.no_op

    # Now manually create a re-ingest with same id but different body and matching declared hash
    source_text_b = make_source(id_="yt-immutA", body="MUTATED body\n")
    src_b = _write_source(tmp_path, "b.md", source_text_b)
    second = ingest_canonical(src_b)
    assert not second.success
    assert any("source-immutability" in e for e in second.errors)


def test_ingest_input_not_found(kb_root, tmp_path):
    missing = tmp_path / "nope.md"
    result = ingest_canonical(missing)
    assert not result.success
    assert any("not found" in e for e in result.errors)


def test_ingest_unbalanced_wikilink_rejected(kb_root, make_source, tmp_path):
    bad_body = "Claim [[sources/yt-abc and dangling.\n"
    source_text = make_source(body=bad_body)
    src = _write_source(tmp_path, "bad-link.md", source_text)
    result = ingest_canonical(src)
    assert not result.success
    assert any("wikilink-malformed" in e for e in result.errors)


# --- TOK-4: _gather_existing_pages two-stage select -------------------------


def _write_wiki_entity(kb_root: Path, slug: str, domain: str, body: str) -> None:
    d = kb_root / "wiki" / "entities"
    d.mkdir(parents=True, exist_ok=True)
    front = {
        "type": "entity",
        "entity_kind": "drug",
        "slug": slug,
        "title": slug.replace("-", " ").title(),
        "domain": domain,
    }
    (d / f"{slug}.md").write_text(fm.serialize(front, body))


def test_gather_existing_pages_30_page_stage1_under_15kb(kb_root):
    """TOK-4: stage-1 output for a 30-page fixture must fit within 15 KB."""
    long_body = "x" * 5000 + "\n"  # 5 KB body per page
    for i in range(30):
        _write_wiki_entity(kb_root, f"entity-{i:02d}", "test-domain", long_body)

    pages = _gather_existing_pages("test-domain")

    assert len(pages) == 30
    prompt_block = build_plan_user_prompt("source text", pages)
    # The existing-pages section alone must be ≤15 KB
    existing_section_bytes = len("\n".join(pages.values()).encode())
    assert existing_section_bytes <= 15_000, (
        f"Stage-1 existing-pages block is {existing_section_bytes} bytes (limit 15 000)"
    )


def test_gather_existing_pages_small_wiki_sends_full_body(kb_root):
    """TOK-4: ≤5 pages → full body is preserved."""
    body = "Full body content " * 20  # ~360 chars
    for i in range(5):
        _write_wiki_entity(kb_root, f"small-{i}", "small-domain", body)

    pages = _gather_existing_pages("small-domain")

    assert len(pages) == 5
    for content in pages.values():
        assert body in content, "full body should be present for small wiki"


def test_gather_existing_pages_no_domain_returns_empty(kb_root):
    """TOK-4: without a domain, always returns {}."""
    _write_wiki_entity(kb_root, "orphan-entity", "some-domain", "body\n")
    assert _gather_existing_pages(None) == {}


def test_gather_existing_pages_wrong_domain_excluded(kb_root):
    """TOK-4: pages from a different domain are not returned."""
    _write_wiki_entity(kb_root, "other-entity", "other-domain", "body\n")
    assert _gather_existing_pages("my-domain") == {}


def test_ingest_force_include_bypasses_filter(kb_root, make_source, tmp_path):
    """--force-include writes the wiki page WITHOUT invoking the semantic filter.

    Eliminates the filter-correct + re-ingest two-pass for caller-vetted sources.
    """

    class _RaisingFilter:
        def call(self, prompt: str) -> str:  # pragma: no cover - must never run
            raise AssertionError("filter must not be called when force_include=True")

    src = _write_source(tmp_path, "input.md", make_source(domains=["data-collectives"]))

    result = ingest_canonical(
        src,
        domain="data-collectives",
        force_include=True,
        filter_client=_RaisingFilter(),
    )

    assert result.success, result.errors
    assert paths.wiki_source_path("yt-testABC_123").exists(), (
        "force-include must write the wiki source page even with no passing filter"
    )
    raw_front, _ = fm.parse(
        paths.raw_source_path("youtube", "yt-testABC_123").read_text()
    )
    assert raw_front["filter"]["policy_version"] == "force-include"
    assert raw_front["filter"]["score"] == 1.0
