"""Tests for the M5 NotebookLM gateway.

Every test injects a `MockNlmClient`. We never invoke the real `nlm` CLI
during unit tests — the gateway is the thing under test, NotebookLM is
mocked out. The subprocess wrapper itself has tiny coverage (parse helpers).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import shutil

import pytest
import yaml

from gateway import frontmatter as fm
from gateway import nlm_registry, paths
from gateway.nlm_client import (
    ArtifactInfo,
    NlmError,
    _extract_artifact_id,
    _extract_notebook_id,
    notebook_artifact_url,
    notebook_url,
)
from gateway.ops.nlm import (
    nlm_add,
    nlm_audio,
    nlm_briefing,
    nlm_revise,
    nlm_slides,
    nlm_sync,
)


# --- mock client -----------------------------------------------------------


@dataclass
class MockNlmClient:
    """Records calls; returns canned values."""

    next_notebook_id: str = "nb-test-12345"
    next_artifact_id: str = "art-abc-99999"

    notebooks_created: list[str] = field(default_factory=list)
    sources_added: list[tuple[str, str]] = field(default_factory=list)
    text_sources_added: list[tuple[str, str, str | None]] = field(default_factory=list)
    file_sources_added: list[tuple[str, Path, str | None]] = field(default_factory=list)
    artifact_creates: list[tuple[str, str, str | None]] = field(default_factory=list)
    revisions: list[tuple[str, list[tuple[int, str]]]] = field(default_factory=list)
    downloads: list[tuple[str, str, Path, str | None]] = field(default_factory=list)

    def notebook_create(self, title: str) -> str:
        self.notebooks_created.append(title)
        return self.next_notebook_id

    def source_add_url(self, notebook_id: str, url: str) -> None:
        self.sources_added.append((notebook_id, url))

    def source_add_text(self, notebook_id, content, *, title=None):
        self.text_sources_added.append((notebook_id, content, title))

    def source_add_file(self, notebook_id, file_path, *, title=None):
        self.file_sources_added.append((notebook_id, file_path, title))

    def artifact_status(self, notebook_id, artifact_id):
        # Tests don't exercise NotebookLM's async generation; return
        # 'completed' so the artifact-create flow proceeds to download.
        return "completed"

    def slides_create(self, notebook_id, *, focus=None) -> ArtifactInfo:
        self.artifact_creates.append(("slides", notebook_id, focus))
        return ArtifactInfo(notebook_id=notebook_id, artifact_type="slides", artifact_id=self.next_artifact_id)

    def slides_revise(self, artifact_id, slide_revisions):
        self.revisions.append((artifact_id, slide_revisions))
        return ArtifactInfo(notebook_id="", artifact_type="slides", artifact_id="art-revised-77777")

    def audio_create(self, notebook_id, *, focus=None) -> ArtifactInfo:
        self.artifact_creates.append(("audio", notebook_id, focus))
        return ArtifactInfo(notebook_id=notebook_id, artifact_type="audio", artifact_id=self.next_artifact_id)

    def report_create(self, notebook_id, *, format="Briefing Doc") -> ArtifactInfo:
        self.artifact_creates.append(("report", notebook_id, format))
        return ArtifactInfo(notebook_id=notebook_id, artifact_type="report", artifact_id=self.next_artifact_id)

    def _do_download(self, kind, notebook_id, dest, artifact_id):
        self.downloads.append((kind, notebook_id, dest, artifact_id))
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(b"fake artifact content")

    def download_slides(self, notebook_id, dest, *, artifact_id=None):
        self._do_download("slides", notebook_id, dest, artifact_id)

    def download_audio(self, notebook_id, dest, *, artifact_id=None):
        self._do_download("audio", notebook_id, dest, artifact_id)

    def download_report(self, notebook_id, dest, *, artifact_id=None):
        self._do_download("report", notebook_id, dest, artifact_id)

    def notebook_query(self, notebook_id, question):
        # Stub — concrete tests inject their own MockClient with canned
        # answers. Default returns an empty payload so any op that
        # exercises the query path doesn't crash on protocol checks.
        return {"answer": "", "citations": {}, "sources_used": []}

    # `notebook_sources` is consulted by `nlm_sync` to reconcile NotebookLM
    # state. Tests override `pre_loaded_sources` to simulate sources that
    # are already on the NotebookLM side (e.g., from a prior partial run).
    pre_loaded_sources: dict[str, list[dict]] = field(default_factory=dict)

    def notebook_sources(self, notebook_id):
        return list(self.pre_loaded_sources.get(notebook_id, []))


# --- fixtures ---------------------------------------------------------------


@pytest.fixture
def mock_client() -> MockNlmClient:
    return MockNlmClient()


def _make_youtube_source(kb_root, make_source, *, source_id="yt-mockSrcABC", domain="test-domain"):
    """Pre-populate raw/youtube/<id>.md as if it had been ingested."""
    text = make_source(id_=source_id, domains=[domain], url=f"https://www.youtube.com/watch?v={source_id}")
    raw_path = paths.raw_source_path("youtube", source_id)
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_text(text)
    return raw_path


# --- regex helpers in nlm_client -------------------------------------------


def test_extract_artifact_id_finds_id():
    assert _extract_artifact_id("Created artifact_id: artifact_abc123") == "artifact_abc123"
    assert _extract_artifact_id("Some other id: art-xyz98765") == "art-xyz98765"


def test_extract_artifact_id_returns_empty_when_absent():
    assert _extract_artifact_id("nothing matched") == ""


def test_extract_notebook_id_from_url_form():
    text = "https://notebooklm.google.com/notebook/abc123def4567890"
    assert _extract_notebook_id(text) == "abc123def4567890"


def test_extract_notebook_id_uuid_form():
    text = "Created: 12345678-1234-1234-1234-123456789012"
    assert _extract_notebook_id(text) == "12345678-1234-1234-1234-123456789012"


def test_extract_notebook_id_raises_when_absent():
    with pytest.raises(NlmError):
        _extract_notebook_id("nothing here")


def test_notebook_artifact_url_falls_back_when_no_artifact_id():
    assert notebook_artifact_url("nb-x", "") == notebook_url("nb-x")
    assert "artifact" in notebook_artifact_url("nb-x", "art-y")


# --- registry --------------------------------------------------------------


def test_registry_register_and_lookup(kb_root):
    assert nlm_registry.get_notebook_id("d1") is None
    nlm_registry.register("d1", "nb-1")
    assert nlm_registry.get_notebook_id("d1") == "nb-1"

    nlm_registry.increment_sources("d1", by=3)
    entry = nlm_registry.load()["d1"]
    assert entry.sources_count == 3


def test_registry_persists_yaml_shape(kb_root):
    nlm_registry.register("alpha", "nb-a")
    nlm_registry.register("beta", "nb-b")
    raw = yaml.safe_load(nlm_registry.notebooks_yaml_path().read_text())
    assert "notebooks" in raw
    assert raw["notebooks"]["alpha"]["persistent"]["notebook_id"] == "nb-a"


# --- nlm-add ---------------------------------------------------------------


def test_nlm_add_creates_notebook_and_updates_source(kb_root, make_source, mock_client):
    raw_path = _make_youtube_source(kb_root, make_source, source_id="yt-addTest1AB", domain="d1")

    result = nlm_add("d1", "yt-addTest1AB", client=mock_client)
    assert result.success, result.errors
    assert mock_client.notebooks_created == ["d1 (knowledge base)"]
    assert mock_client.sources_added == [(mock_client.next_notebook_id, "https://www.youtube.com/watch?v=yt-addTest1AB")]

    front, _ = fm.parse(raw_path.read_text())
    assert mock_client.next_notebook_id in front["nlm_corpus_ids"]
    assert "d1" in front["domains"]


def test_nlm_add_idempotent_on_repeat(kb_root, make_source, mock_client):
    raw_path = _make_youtube_source(kb_root, make_source, source_id="yt-addIdemAB", domain="d1")

    first = nlm_add("d1", "yt-addIdemAB", client=mock_client)
    assert first.success and not first.no_op

    second = nlm_add("d1", "yt-addIdemAB", client=mock_client)
    assert second.success and second.no_op
    assert "already in" in second.summary
    # Notebook was not created twice
    assert len(mock_client.notebooks_created) == 1
    # Source was not added twice
    assert len(mock_client.sources_added) == 1


def test_nlm_add_unknown_source(kb_root, mock_client):
    result = nlm_add("d1", "yt-doesNotExist", client=mock_client)
    assert not result.success
    assert any("no raw source" in e for e in result.errors)


def test_nlm_add_source_without_url_falls_back_to_text(kb_root, make_source, mock_client):
    """M37: PDF/note sources have no URL; fall back to source_add_text using
    the canonical body and frontmatter title."""
    raw_path = _make_youtube_source(kb_root, make_source, source_id="yt-noUrlABC1", domain="d1")
    front, body = fm.parse(raw_path.read_text())
    del front["url"]
    front["title"] = "Test Source Title"
    raw_path.write_text(fm.serialize(front, body))

    result = nlm_add("d1", "yt-noUrlABC1", client=mock_client)
    assert result.success, result.errors
    assert mock_client.sources_added == []
    assert len(mock_client.text_sources_added) == 1
    nb_id, content, title = mock_client.text_sources_added[0]
    assert nb_id == mock_client.next_notebook_id
    assert content == body
    assert title == "Test Source Title"


def test_nlm_add_source_without_url_or_body_errors(kb_root, make_source, mock_client):
    """If the source has no url, no sidecar, and no body — nothing to send."""
    raw_path = _make_youtube_source(kb_root, make_source, source_id="yt-emptySrc", domain="d1")
    front, body = fm.parse(raw_path.read_text())
    del front["url"]
    raw_path.write_text(fm.serialize(front, ""))

    result = nlm_add("d1", "yt-emptySrc", client=mock_client)
    assert not result.success
    assert any("nothing to add to NotebookLM" in e for e in result.errors)


def test_nlm_add_uploads_sidecar_file_when_present(kb_root, make_source, mock_client):
    """M37: PDF / docx / image sources have a sidecar binary at source_path —
    prefer file upload over text upload (preserves layout / figures / native
    NotebookLM processing)."""
    raw_path = _make_youtube_source(
        kb_root, make_source, source_id="yt-withSidecar", domain="d1"
    )
    front, body = fm.parse(raw_path.read_text())
    del front["url"]
    sidecar_rel = "raw/youtube/yt-withSidecar.pdf"
    sidecar_abs = paths.knowledge_root() / sidecar_rel
    sidecar_abs.write_bytes(b"%PDF-1.4 stub binary")
    front["source_path"] = sidecar_rel
    front["title"] = "Sidecar Test"
    raw_path.write_text(fm.serialize(front, body))

    result = nlm_add("d1", "yt-withSidecar", client=mock_client)
    assert result.success, result.errors
    assert mock_client.text_sources_added == []
    assert mock_client.sources_added == []
    assert len(mock_client.file_sources_added) == 1
    nb_id, path, title = mock_client.file_sources_added[0]
    assert path == sidecar_abs
    assert title == "Sidecar Test"


# --- nlm-sync --------------------------------------------------------------


def test_nlm_sync_no_op_when_domain_has_no_sources(kb_root, mock_client):
    result = nlm_sync("empty-domain", client=mock_client)
    assert result.success
    assert result.no_op
    assert mock_client.notebooks_created == []
    assert mock_client.sources_added == []


def test_nlm_sync_dry_run_lists_candidates_without_calling_client(kb_root, make_source, mock_client):
    _make_youtube_source(kb_root, make_source, source_id="yt-syncDryA1", domain="ds")
    _make_youtube_source(kb_root, make_source, source_id="yt-syncDryB2", domain="ds")
    _make_youtube_source(kb_root, make_source, source_id="yt-otherDom1", domain="other")

    result = nlm_sync("ds", dry_run=True, client=mock_client)

    assert result.success
    assert "would sync 2 source(s)" in result.summary
    assert "yt-syncDryA1" in result.summary
    assert "yt-syncDryB2" in result.summary
    assert "yt-otherDom1" not in result.summary  # filtered by domain
    assert mock_client.notebooks_created == []
    assert mock_client.sources_added == []


def test_nlm_sync_adds_every_tagged_source_and_skips_already_synced(kb_root, make_source, mock_client):
    # Two fresh sources tagged with the domain.
    _make_youtube_source(kb_root, make_source, source_id="yt-syncFresh1", domain="ds")
    _make_youtube_source(kb_root, make_source, source_id="yt-syncFresh2", domain="ds")
    # A third source already synced — should be counted as skipped.
    raw_third = _make_youtube_source(kb_root, make_source, source_id="yt-syncAlready", domain="ds")
    nlm_add("ds", "yt-syncAlready", client=mock_client)
    sources_before = list(mock_client.sources_added)

    progress_calls: list[tuple] = []
    result = nlm_sync(
        "ds",
        client=mock_client,
        progress=lambda i, n, sid, status, detail: progress_calls.append((i, n, sid, status)),
    )

    assert result.success, result.errors
    assert "2 added" in result.summary
    assert "1 already in corpus" in result.summary
    assert "0 failed" in result.summary

    # Only the two fresh sources caused new client calls.
    new_calls = mock_client.sources_added[len(sources_before):]
    assert {url for _, url in new_calls} == {
        "https://www.youtube.com/watch?v=yt-syncFresh1",
        "https://www.youtube.com/watch?v=yt-syncFresh2",
    }

    # Each fresh source's frontmatter now carries the persistent notebook id.
    for sid in ("yt-syncFresh1", "yt-syncFresh2"):
        front, _ = fm.parse(paths.raw_source_path("youtube", sid).read_text())
        assert mock_client.next_notebook_id in front["nlm_corpus_ids"]

    # progress callback fires once per source, in stable order.
    assert [c[2] for c in progress_calls] == ["yt-syncAlready", "yt-syncFresh1", "yt-syncFresh2"]
    statuses = {c[2]: c[3] for c in progress_calls}
    assert statuses == {
        "yt-syncAlready": "skipped",
        "yt-syncFresh1": "added",
        "yt-syncFresh2": "added",
    }
    # raw_third still parses cleanly post-run.
    fm.parse(raw_third.read_text())


def test_nlm_sync_continues_after_individual_source_failure(kb_root, make_source, mock_client):
    _make_youtube_source(kb_root, make_source, source_id="yt-syncOk1", domain="ds")
    # Source with empty body, no url, no sidecar — `nlm_add` rejects this.
    bad_text = make_source(
        id_="yt-syncBad1", domains=["ds"], body="", url=""
    )
    bad_path = paths.raw_source_path("youtube", "yt-syncBad1")
    bad_path.write_text(bad_text)
    _make_youtube_source(kb_root, make_source, source_id="yt-syncOk2", domain="ds")

    result = nlm_sync("ds", client=mock_client)

    assert not result.success  # one failure → success=False
    assert "2 added" in result.summary
    assert "1 failed" in result.summary
    assert any("yt-syncBad1" in e for e in result.errors)
    # The good sources before AND after the failing one both got synced.
    urls_added = {url for _, url in mock_client.sources_added}
    assert "https://www.youtube.com/watch?v=yt-syncOk1" in urls_added
    assert "https://www.youtube.com/watch?v=yt-syncOk2" in urls_added


def test_nlm_sync_reconciles_sources_already_in_notebook(kb_root, make_source, mock_client):
    """If a source is already on the NotebookLM side (e.g., from a prior
    partial run before we updated frontmatter) `nlm_sync` should detect
    that via title signature, fix the frontmatter, and skip the add — no
    duplicate."""
    # First, attach the persistent notebook to the domain so reconciliation
    # has somewhere to look.
    from gateway import nlm_registry as registry_module
    registry_module.register("ds", "nb-existing")

    # An arxiv source whose URL contains the canonical arxiv id.
    arxiv_text = make_source(
        id_="arxiv-2401.12345",
        type_="arxiv",
        domains=["ds"],
        url="http://arxiv.org/abs/2401.12345v2",
        title="Some long enough title for fallback matching",
    )
    arxiv_path = paths.raw_source_path("arxiv", "arxiv-2401.12345")
    arxiv_path.write_text(arxiv_text)

    # Mark the notebook as already containing the arxiv source — simulated by
    # NotebookLM-side title that embeds the arxiv id (this is exactly the
    # title shape NotebookLM uses for arxiv ingests).
    mock_client.pre_loaded_sources["nb-existing"] = [
        {"id": "src-abc", "title": "[2401.12345v1] Some Edge Inference Paper"}
    ]

    result = nlm_sync("ds", client=mock_client)

    assert result.success, result.errors
    assert "1 reconciled" in result.summary
    # No actual adds happened — reconciliation took the place of the add.
    assert mock_client.sources_added == []
    # Frontmatter now records the persistent notebook id, so a re-run is a no-op.
    front, _ = fm.parse(arxiv_path.read_text())
    assert "nb-existing" in front["nlm_corpus_ids"]


def test_nlm_sync_respects_limit(kb_root, make_source, mock_client):
    for i in range(5):
        _make_youtube_source(kb_root, make_source, source_id=f"yt-syncLim{i}A", domain="ds")

    result = nlm_sync("ds", limit=2, client=mock_client)

    assert result.success
    assert "2 added" in result.summary
    assert len(mock_client.sources_added) == 2


# --- nlm-slides / nlm-audio / nlm-briefing ---------------------------------


def test_nlm_slides_creates_artifact_page_with_bidirectional_link(kb_root, make_source, mock_client):
    _make_youtube_source(kb_root, make_source, source_id="yt-slidesPrep", domain="d1")
    nlm_add("d1", "yt-slidesPrep", client=mock_client)

    result = nlm_slides("d1", "reward dose response", client=mock_client)
    assert result.success, result.errors

    artifacts = list((paths.wiki_dir() / "artifacts" / "slides").glob("*.md"))
    assert len(artifacts) == 1
    page = artifacts[0]
    front, body = fm.parse(page.read_text())
    assert front["type"] == "artifact"
    assert front["artifact_type"] == "slides"
    assert front["domain"] == "d1"
    assert front["nlm_notebook_id"] == mock_client.next_notebook_id
    assert front["nlm_artifact_id"] == mock_client.next_artifact_id
    assert "notebooklm.google.com" in front["nlm_artifact_url"]
    assert "reward dose response" in front["question"]
    assert "## Local file" in body
    assert "## NotebookLM (live, editable)" in body

    # PDF was downloaded
    assert any(p.suffix == ".pdf" for p in (paths.wiki_dir() / "artifacts" / "slides").iterdir())


def test_nlm_slides_without_notebook_errors(kb_root, mock_client):
    result = nlm_slides("nonexistent-domain", "anything", client=mock_client)
    assert not result.success
    assert any("no notebook" in e for e in result.errors)


def test_nlm_audio_creates_m4a_and_page(kb_root, make_source, mock_client):
    _make_youtube_source(kb_root, make_source, source_id="yt-audioPrep", domain="d2")
    nlm_add("d2", "yt-audioPrep", client=mock_client)

    result = nlm_audio("d2", "deep dive on mechanisms", client=mock_client)
    assert result.success, result.errors

    audio_dir = paths.wiki_dir() / "artifacts" / "audio"
    assert any(p.suffix == ".m4a" for p in audio_dir.iterdir())
    pages = list(audio_dir.glob("*.md"))
    assert len(pages) == 1
    front, _ = fm.parse(pages[0].read_text())
    assert front["artifact_type"] == "audio"


def test_nlm_briefing_creates_report_md(kb_root, make_source, mock_client):
    _make_youtube_source(kb_root, make_source, source_id="yt-briefPrep", domain="d3")
    nlm_add("d3", "yt-briefPrep", client=mock_client)

    result = nlm_briefing("d3", client=mock_client)
    assert result.success, result.errors

    briefing_dir = paths.wiki_dir() / "artifacts" / "briefing"
    pages = list(briefing_dir.glob("*.md"))
    # One artifact page (.md) and the downloaded report (also .md by extension)
    assert any(p.name.endswith("-briefing.md") for p in pages)


# --- nlm-revise -------------------------------------------------------------


def test_nlm_revise_creates_new_artifact_page(kb_root, make_source, mock_client):
    _make_youtube_source(kb_root, make_source, source_id="yt-revPrep", domain="d4")
    nlm_add("d4", "yt-revPrep", client=mock_client)

    first = nlm_slides("d4", "topic A", client=mock_client)
    assert first.success
    original_pages = list((paths.wiki_dir() / "artifacts" / "slides").glob("*.md"))
    original_slug = original_pages[0].stem

    result = nlm_revise(original_slug, ["1 Make title larger", "3 Remove the image"], client=mock_client)
    assert result.success, result.errors

    # A new page exists distinct from the original
    pages = list((paths.wiki_dir() / "artifacts" / "slides").glob("*.md"))
    assert len(pages) == 2
    new_pages = [p for p in pages if p.stem != original_slug]
    assert len(new_pages) == 1
    assert "rev" in new_pages[0].stem.lower()

    # The mock saw both revisions
    assert len(mock_client.revisions) == 1
    art_id, revs = mock_client.revisions[0]
    assert art_id == mock_client.next_artifact_id
    assert revs == [(1, "Make title larger"), (3, "Remove the image")]


def test_nlm_revise_unknown_artifact(kb_root, mock_client):
    result = nlm_revise("does-not-exist", ["1 anything"], client=mock_client)
    assert not result.success
    assert any("no slide artifact" in e for e in result.errors)


def test_nlm_revise_invalid_revision_format(kb_root, make_source, mock_client):
    _make_youtube_source(kb_root, make_source, source_id="yt-revFmtPrep", domain="d5")
    nlm_add("d5", "yt-revFmtPrep", client=mock_client)
    first = nlm_slides("d5", "topic", client=mock_client)
    slug = list((paths.wiki_dir() / "artifacts" / "slides").glob("*.md"))[0].stem

    result = nlm_revise(slug, ["no number prefix"], client=mock_client)
    assert not result.success
    assert any("could not parse" in e for e in result.errors)


# --- log integration --------------------------------------------------------


def test_nlm_add_writes_log_entry(kb_root, make_source, mock_client):
    _make_youtube_source(kb_root, make_source, source_id="yt-logTestAB", domain="d6")
    nlm_add("d6", "yt-logTestAB", client=mock_client)
    text = paths.log_path().read_text()
    assert "nlm-add" in text
    assert "yt-logTestAB" in text
    assert "d6" in text
