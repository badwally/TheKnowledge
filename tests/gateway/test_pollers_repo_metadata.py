"""Tests for the repo-metadata poller (INT-8).

~/code/ filesystem is simulated via tmp_path — no real project dirs touched.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import frontmatter as fm
from gateway import paths
from gateway.pollers import repo_metadata as rm_mod
from gateway.pollers import get_poller, list_pollers, UnknownPollerError
from gateway.pollers.repo_metadata import RepoMetadataPoller


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def _make_code_root(tmp_path: Path) -> Path:
    """Create a fake ~/code/ directory under tmp_path."""
    code_root = tmp_path / "code"
    code_root.mkdir()
    return code_root


def _add_project(code_root: Path, name: str, files: dict[str, str]) -> Path:
    """Create a fake project directory with the given files."""
    project = code_root / name
    project.mkdir()
    for rel, content in files.items():
        target = project / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
    return project


# ---------------------------------------------------------------------------
# new file detection
# ---------------------------------------------------------------------------


def test_new_file_written_to_raw_note(kb_root, monkeypatch):
    code_root = _make_code_root(kb_root)
    _add_project(code_root, "my-project", {"README.md": "# My Project\n\nGreat project.\n"})
    monkeypatch.setattr(rm_mod, "_CODE_ROOT", code_root)

    poller = RepoMetadataPoller()
    result = poller.run()

    assert result.success is True
    assert result.fetched == 1

    note_dir = paths.raw_dir_for("note")
    files = list(note_dir.glob("note-repo-my-project-*.md"))
    assert len(files) == 1
    front, body = fm.parse(files[0].read_text())

    assert front["type"] == "note"
    assert front["meta"]["source_app"] == "repo-metadata"
    assert "My Project" in body or "Great project" in body


def test_source_app_is_repo_metadata_on_every_output(kb_root, monkeypatch):
    code_root = _make_code_root(kb_root)
    _add_project(code_root, "alpha", {"README.md": "Alpha readme.\n", "CLAUDE.md": "Alpha claude.\n"})
    _add_project(code_root, "beta", {"README.md": "Beta readme.\n"})
    monkeypatch.setattr(rm_mod, "_CODE_ROOT", code_root)

    poller = RepoMetadataPoller()
    result = poller.run()

    assert result.success is True
    note_dir = paths.raw_dir_for("note")
    files = list(note_dir.glob("note-repo-*.md"))
    assert len(files) == 3
    for f in files:
        front, _ = fm.parse(f.read_text())
        assert front["meta"]["source_app"] == "repo-metadata"


# ---------------------------------------------------------------------------
# cursor / skip behaviour
# ---------------------------------------------------------------------------


def test_unchanged_file_skipped_on_second_run(kb_root, monkeypatch):
    code_root = _make_code_root(kb_root)
    _add_project(code_root, "proj", {"README.md": "Stable content.\n"})
    monkeypatch.setattr(rm_mod, "_CODE_ROOT", code_root)

    poller = RepoMetadataPoller()
    first = poller.run()
    assert first.fetched == 1

    second = poller.run()
    assert second.success is True
    assert second.fetched == 0
    assert second.skipped == 1


def test_changed_file_reingested_on_second_run(kb_root, monkeypatch):
    code_root = _make_code_root(kb_root)
    proj = _add_project(code_root, "proj", {"README.md": "Original content.\n"})
    monkeypatch.setattr(rm_mod, "_CODE_ROOT", code_root)

    poller = RepoMetadataPoller()
    first = poller.run()
    assert first.fetched == 1

    (proj / "README.md").write_text("Updated content.\n")
    second = poller.run()
    assert second.success is True
    assert second.fetched == 1
    assert second.skipped == 0

    note_dir = paths.raw_dir_for("note")
    files = list(note_dir.glob("note-repo-proj-*.md"))
    assert len(files) == 1
    _, body = fm.parse(files[0].read_text())
    assert "Updated content" in body


# ---------------------------------------------------------------------------
# excluded paths
# ---------------------------------------------------------------------------


def test_excluded_dirs_never_ingested(kb_root, monkeypatch):
    code_root = _make_code_root(kb_root)
    proj = code_root / "proj"
    proj.mkdir()
    (proj / "README.md").write_text("Good file.\n")

    for excluded in ("node_modules", ".venv", "__pycache__", ".git", "vendor", "dist", "build"):
        d = proj / excluded
        d.mkdir()
        (d / "README.md").write_text(f"Should be ignored in {excluded}.\n")

    monkeypatch.setattr(rm_mod, "_CODE_ROOT", code_root)

    poller = RepoMetadataPoller()
    result = poller.run()

    assert result.success is True
    assert result.fetched == 1  # only the top-level README.md


# ---------------------------------------------------------------------------
# missing code root
# ---------------------------------------------------------------------------


def test_missing_code_root_returns_empty_result(kb_root, monkeypatch):
    missing = kb_root / "no_code_dir_here"
    monkeypatch.setattr(rm_mod, "_CODE_ROOT", missing)

    poller = RepoMetadataPoller()
    result = poller.run()

    assert result.success is True
    assert result.fetched == 0
    assert result.errors == []


# ---------------------------------------------------------------------------
# auto-domain tagging
# ---------------------------------------------------------------------------


def test_domain_tagged_when_policy_exists(kb_root, monkeypatch):
    code_root = _make_code_root(kb_root)
    _add_project(code_root, "my-proj", {"README.md": "Stuff.\n"})
    monkeypatch.setattr(rm_mod, "_CODE_ROOT", code_root)

    # Create the policy file so the slug is recognised
    policy_dir = paths.policies_dir()
    policy_dir.mkdir(parents=True, exist_ok=True)
    (policy_dir / "my-proj.yaml").write_text("slug: my-proj\n")

    poller = RepoMetadataPoller()
    poller.run()

    note_dir = paths.raw_dir_for("note")
    files = list(note_dir.glob("note-repo-my-proj-*.md"))
    assert len(files) == 1
    front, _ = fm.parse(files[0].read_text())
    assert "my-proj" in front["domains"]


def test_domain_empty_when_no_policy(kb_root, monkeypatch):
    code_root = _make_code_root(kb_root)
    _add_project(code_root, "untagged-proj", {"README.md": "Something.\n"})
    monkeypatch.setattr(rm_mod, "_CODE_ROOT", code_root)

    poller = RepoMetadataPoller()
    poller.run()

    note_dir = paths.raw_dir_for("note")
    files = list(note_dir.glob("note-repo-untagged-proj-*.md"))
    assert len(files) == 1
    front, _ = fm.parse(files[0].read_text())
    assert front["domains"] == []


# ---------------------------------------------------------------------------
# docs subdirectory
# ---------------------------------------------------------------------------


def test_docs_md_files_ingested(kb_root, monkeypatch):
    code_root = _make_code_root(kb_root)
    _add_project(code_root, "proj", {
        "README.md": "Top-level readme.\n",
        "docs/architecture.md": "Architecture notes.\n",
        "docs/api.md": "API notes.\n",
    })
    monkeypatch.setattr(rm_mod, "_CODE_ROOT", code_root)

    poller = RepoMetadataPoller()
    result = poller.run()

    assert result.success is True
    assert result.fetched == 3


# ---------------------------------------------------------------------------
# registry
# ---------------------------------------------------------------------------


def test_registered_under_repo_metadata():
    assert "repo-metadata" in list_pollers()


def test_get_poller_returns_repo_metadata_instance():
    p = get_poller("repo-metadata")
    assert isinstance(p, RepoMetadataPoller)
    assert p.name == "repo-metadata"
    assert p.source_type == "note"
