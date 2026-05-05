"""Tests for `gateway.research.adapters.local.LocalAdapter`.

The adapter enumerates user-supplied paths/globs and emits one
`CandidateItem` per file with a registered converter. Files with no
converter (e.g. `.xyz`) are silently skipped.

Note on file types: the brief lists "two PDFs, one DOCX, one unsupported".
The current converter registry has no DOCX handler, so the third
supported file is a `.csv` (handled by `gateway.converters.csv`). The
test intent — one PDF kind + one non-PDF supported kind + one
unsupported kind — is preserved.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from gateway.research.adapters.base import CandidateItem
from gateway.research.adapters.local import LocalAdapter


# --- helpers ---------------------------------------------------------------


def _touch(path: Path, content: bytes = b"") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


def _expected_id(path: Path) -> str:
    return hashlib.sha1(str(path.resolve()).encode("utf-8")).hexdigest()[:12]


@pytest.fixture
def populated_dir(tmp_path: Path) -> Path:
    """Two PDFs, one CSV (supported non-PDF), one unsupported `.xyz`."""
    _touch(tmp_path / "alpha.pdf", b"%PDF-1.4 fake")
    _touch(tmp_path / "beta.pdf", b"%PDF-1.4 fake")
    _touch(tmp_path / "data.csv", b"col1,col2\n1,2\n")
    _touch(tmp_path / "notes.xyz", b"unsupported")
    return tmp_path


# --- tests -----------------------------------------------------------------


def test_directory_walk_emits_supported_files_only(populated_dir: Path):
    adapter = LocalAdapter(paths=[str(populated_dir)])
    items = adapter.search("ignored-query")

    # Three supported files: 2 PDFs + 1 CSV. The .xyz is skipped.
    assert len(items) == 3
    by_type: dict[str, list[CandidateItem]] = {}
    for item in items:
        by_type.setdefault(item.source_type, []).append(item)

    assert sorted(by_type.keys()) == ["csv", "pdf"]
    assert len(by_type["pdf"]) == 2
    assert len(by_type["csv"]) == 1


def test_emitted_items_have_correct_shape(populated_dir: Path):
    adapter = LocalAdapter(paths=[str(populated_dir)])
    items = adapter.search("ignored-query")

    pdf_item = next(i for i in items if i.title == "alpha")
    abs_path = str((populated_dir / "alpha.pdf").resolve())

    assert pdf_item.item_id == _expected_id(populated_dir / "alpha.pdf")
    assert pdf_item.source_type == "pdf"
    assert pdf_item.url == f"file://{abs_path}"
    assert pdf_item.title == "alpha"
    assert pdf_item.description == ""
    assert pdf_item.authors == []
    assert pdf_item.publish_date is None
    assert pdf_item.source_metadata["absolute_path"] == abs_path
    assert pdf_item.source_metadata["size_bytes"] > 0


def test_glob_expansion_filters_to_pattern(populated_dir: Path):
    pattern = str(populated_dir / "*.pdf")
    adapter = LocalAdapter(paths=[pattern])
    items = adapter.search("ignored")

    assert len(items) == 2
    assert {item.title for item in items} == {"alpha", "beta"}
    assert all(item.source_type == "pdf" for item in items)


def test_recursive_glob_walks_subdirs(tmp_path: Path):
    _touch(tmp_path / "a.pdf")
    _touch(tmp_path / "nested" / "b.pdf")
    _touch(tmp_path / "nested" / "deep" / "c.pdf")

    adapter = LocalAdapter(paths=[str(tmp_path / "**" / "*.pdf")])
    items = adapter.search("ignored")

    assert {item.title for item in items} == {"a", "b", "c"}


def test_url_uses_absolute_paths(populated_dir: Path, monkeypatch: pytest.MonkeyPatch):
    # Pass a relative path; resolved url must still be absolute.
    monkeypatch.chdir(populated_dir.parent)
    rel = populated_dir.name
    adapter = LocalAdapter(paths=[rel])
    items = adapter.search("ignored")

    for item in items:
        assert item.url.startswith("file://")
        path_part = item.url[len("file://"):]
        assert Path(path_part).is_absolute()


def test_item_id_is_stable_hash_of_absolute_path(populated_dir: Path):
    adapter = LocalAdapter(paths=[str(populated_dir)])
    first = adapter.search("a")
    second = adapter.search("b")  # different query, same set

    by_path = {i.source_metadata["absolute_path"]: i.item_id for i in first}
    for item in second:
        assert item.item_id == by_path[item.source_metadata["absolute_path"]]
        # And the hash matches what we'd compute by hand.
        expected = hashlib.sha1(
            item.source_metadata["absolute_path"].encode("utf-8")
        ).hexdigest()[:12]
        assert item.item_id == expected


def test_dedupes_when_same_file_reached_via_multiple_entries(populated_dir: Path):
    # Same file reached via directory walk AND glob — appears only once.
    adapter = LocalAdapter(
        paths=[
            str(populated_dir),
            str(populated_dir / "*.pdf"),
        ]
    )
    items = adapter.search("ignored")

    # 2 PDFs + 1 CSV, no duplicates from the overlap.
    assert len(items) == 3
    paths = [i.source_metadata["absolute_path"] for i in items]
    assert len(paths) == len(set(paths))


def test_max_results_caps_output(populated_dir: Path):
    adapter = LocalAdapter(paths=[str(populated_dir)])
    items = adapter.search("ignored", max_results=2)
    assert len(items) == 2


def test_max_results_none_means_unlimited(populated_dir: Path):
    adapter = LocalAdapter(paths=[str(populated_dir)])
    items = adapter.search("ignored", max_results=None)
    # All three supported files emitted.
    assert len(items) == 3


def test_nonexistent_path_yields_no_items(tmp_path: Path):
    adapter = LocalAdapter(paths=[str(tmp_path / "does-not-exist")])
    items = adapter.search("ignored")
    assert items == []


def test_single_file_path(populated_dir: Path):
    adapter = LocalAdapter(paths=[str(populated_dir / "alpha.pdf")])
    items = adapter.search("ignored")
    assert len(items) == 1
    assert items[0].title == "alpha"
    assert items[0].source_type == "pdf"
