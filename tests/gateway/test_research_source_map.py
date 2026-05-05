"""Tests for `gateway.research.source_map`.

The unit under test is the URL/title matching strategy and the cache
round-trip. The `nlm` CLI is always mocked — these tests never shell
out.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

import pytest

from gateway import frontmatter as fm
from gateway.research import source_map as sm


# --- helpers ---------------------------------------------------------------


def _write_raw(
    kb: Path,
    *,
    source_type: str,
    slug: str,
    title: str,
    url: str | None,
) -> None:
    """Write a minimal canonical raw page. Only the fields the source-map
    cares about (`title`, `url`) are populated; the validator is not
    invoked here — we're testing the indexer, not ingest."""
    front: dict[str, Any] = {
        "id": slug,
        "type": source_type,
        "title": title,
    }
    if url is not None:
        front["url"] = url
    target = kb / "raw" / source_type / f"{slug}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(fm.serialize(front, "Body.\n"), encoding="utf-8")


class _FakeCompletedProcess:
    def __init__(self, *, stdout: str = "", stderr: str = "", returncode: int = 0):
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode


def _patch_nlm_run(
    monkeypatch: pytest.MonkeyPatch,
    *,
    sources: list[dict] | None = None,
    returncode: int = 0,
    stderr: str = "",
) -> list[list[str]]:
    """Replace `subprocess.run` inside source_map with a recording stub.

    Returns the list that captures every argv it was called with."""
    calls: list[list[str]] = []
    payload = json.dumps(sources if sources is not None else [])

    def fake_run(args, **kwargs):
        calls.append(list(args))
        return _FakeCompletedProcess(
            stdout=payload,
            stderr=stderr,
            returncode=returncode,
        )

    monkeypatch.setattr(sm.subprocess, "run", fake_run)
    return calls


# --- tests -----------------------------------------------------------------


def test_url_match_wins_over_title(kb_root: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # Two raw pages share a title but have different URLs. The NLM
    # source carries the URL of the *second* page; URL match must pick
    # that one even though the first page would also satisfy a title
    # match.
    _write_raw(
        kb_root,
        source_type="web",
        slug="article-one",
        title="Shared Title",
        url="https://example.com/one",
    )
    _write_raw(
        kb_root,
        source_type="web",
        slug="article-two",
        title="Shared Title",
        url="https://example.com/two",
    )

    _patch_nlm_run(
        monkeypatch,
        sources=[
            {"id": "nlm-AAA", "title": "Shared Title", "url": "https://example.com/two"},
        ],
    )

    smap = sm.build_source_map("nb-123")
    assert smap == {"nlm-AAA": "raw/web/article-two"}


def test_title_fallback_when_url_absent(
    kb_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _write_raw(
        kb_root,
        source_type="pdf",
        slug="paper-x",
        title="Unique Paper Title",
        url="https://example.com/paper-x.pdf",
    )

    _patch_nlm_run(
        monkeypatch,
        sources=[
            # NLM omits URL; we should still resolve via title.
            {"id": "nlm-BBB", "title": "Unique Paper Title"},
        ],
    )

    smap = sm.build_source_map("nb-123")
    assert smap == {"nlm-BBB": "raw/pdf/paper-x"}


def test_unresolved_source_omitted(
    kb_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _write_raw(
        kb_root,
        source_type="web",
        slug="known",
        title="Known",
        url="https://example.com/known",
    )

    _patch_nlm_run(
        monkeypatch,
        sources=[
            {"id": "nlm-known", "title": "Known", "url": "https://example.com/known"},
            {"id": "nlm-orphan", "title": "Not in raw/", "url": "https://nope.example/"},
        ],
    )

    smap = sm.build_source_map("nb-456")
    assert smap == {"nlm-known": "raw/web/known"}
    # An unresolved source must not show up at all; resolve_citations
    # is what synthesizes a `[[nlm:...]]` placeholder for downstream
    # rendering.
    assert "nlm-orphan" not in smap


def test_cache_written_and_loaded(
    kb_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _write_raw(
        kb_root,
        source_type="youtube",
        slug="vid",
        title="A Video",
        url="https://youtu.be/abc",
    )
    _patch_nlm_run(
        monkeypatch,
        sources=[{"id": "nlm-vid", "title": "A Video", "url": "https://youtu.be/abc"}],
    )

    expected = {"nlm-vid": "raw/youtube/vid"}
    built = sm.build_source_map("nb-cache")
    assert built == expected

    cache_file = kb_root / "nlm" / "source_maps" / "nb-cache.json"
    assert cache_file.is_file(), "build_source_map must write the cache file"
    on_disk = json.loads(cache_file.read_text(encoding="utf-8"))
    assert on_disk == expected

    loaded = sm.load_cached_source_map("nb-cache")
    assert loaded == expected


def test_load_cached_returns_none_when_missing(kb_root: Path) -> None:
    assert sm.load_cached_source_map("nb-never-built") is None


def test_load_cached_returns_none_when_corrupt(kb_root: Path) -> None:
    cache_dir = kb_root / "nlm" / "source_maps"
    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / "nb-bad.json").write_text("{not json", encoding="utf-8")
    assert sm.load_cached_source_map("nb-bad") is None


def test_invokes_nlm_with_expected_args(
    kb_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    calls = _patch_nlm_run(monkeypatch, sources=[])
    sm.build_source_map("nb-args-check")
    assert len(calls) == 1
    argv = calls[0]
    # Anchor the contract: subcommand + flag must match the `nlm` CLI
    # we ship against (matches `~/code/research-notebook/src/output/source_map.py`).
    assert argv[0] == "nlm"
    assert argv[1:] == ["source", "list", "nb-args-check", "--json"]


def test_fetch_raises_on_nonzero_exit(
    kb_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _patch_nlm_run(monkeypatch, sources=[], returncode=2, stderr="boom")
    with pytest.raises(sm.SourceMapError):
        sm.build_source_map("nb-fail")


def test_fetch_raises_on_missing_executable(
    kb_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def fake_run(args, **kwargs):
        raise FileNotFoundError(args[0])

    monkeypatch.setattr(sm.subprocess, "run", fake_run)
    with pytest.raises(sm.SourceMapError):
        sm.build_source_map("nb-no-cli")


def test_fetch_raises_on_timeout(
    kb_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def fake_run(args, **kwargs):
        raise subprocess.TimeoutExpired(cmd=args, timeout=1.0)

    monkeypatch.setattr(sm.subprocess, "run", fake_run)
    with pytest.raises(sm.SourceMapError):
        sm.build_source_map("nb-slow")


def test_resolve_citations_resolved_and_unresolved() -> None:
    smap = {"nlm-aaa": "raw/web/known-page"}
    citations = {1: "nlm-aaa", 2: "nlm-missing"}

    resolved = sm.resolve_citations(citations, smap)

    assert resolved == {
        1: "[[sources/known-page]]",
        2: "[[nlm:nlm-missing]]",
    }


def test_resolve_citations_empty_inputs() -> None:
    assert sm.resolve_citations({}, {}) == {}
    assert sm.resolve_citations({}, {"nlm-x": "raw/web/x"}) == {}


def test_index_skips_malformed_frontmatter(
    kb_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # One good page, one with no frontmatter at all.
    _write_raw(
        kb_root,
        source_type="web",
        slug="good",
        title="Good",
        url="https://example.com/good",
    )
    bad = kb_root / "raw" / "web" / "broken.md"
    bad.write_text("no frontmatter here\n", encoding="utf-8")

    _patch_nlm_run(
        monkeypatch,
        sources=[
            {"id": "nlm-good", "url": "https://example.com/good"},
            {"id": "nlm-bad-title", "title": "broken"},
        ],
    )

    smap = sm.build_source_map("nb-tolerant")
    # The good page resolves; the malformed file is silently skipped
    # so nothing else matches.
    assert smap == {"nlm-good": "raw/web/good"}


def test_client_argument_accepted_but_unused(
    kb_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Passing a sentinel client must not change behavior or raise.
    _write_raw(
        kb_root,
        source_type="web",
        slug="page",
        title="Page",
        url="https://example.com/page",
    )
    _patch_nlm_run(
        monkeypatch,
        sources=[{"id": "nlm-1", "url": "https://example.com/page"}],
    )

    sentinel = object()
    smap = sm.build_source_map("nb-with-client", client=sentinel)  # type: ignore[arg-type]
    assert smap == {"nlm-1": "raw/web/page"}
