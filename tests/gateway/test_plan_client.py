"""Tests for the M44 `ClaudeCLIPlanClient` and `ClaudeCLIVLMClient` argv shape."""

from __future__ import annotations

import subprocess

import pytest

from gateway.plan import (
    ClaudeCLIPlanClient,
    PlanError,
    build_plan_prompt,
    build_plan_system_prompt,
    build_plan_user_prompt,
)
from gateway.vlm import ClaudeCLIVLMClient, VLMError


def _fake_completed(returncode: int, stdout: str = "", stderr: str = ""):
    return subprocess.CompletedProcess(
        args=["claude"],
        returncode=returncode,
        stdout=stdout,
        stderr=stderr,
    )


# --- plan client argv -------------------------------------------------------


def test_plan_client_argv_uses_opus_and_bare(monkeypatch):
    captured: list[list[str]] = []
    monkeypatch.setattr(
        subprocess,
        "run",
        lambda argv, *_a, **_k: (captured.append(list(argv)) or _fake_completed(0, stdout='{"source_id":"x","updates":[]}')),
    )

    ClaudeCLIPlanClient().call_split(system="PLAN_SYS", user="SRC")
    argv = captured[0]
    assert "--bare" not in argv  # bypasses Max OAuth
    assert "--tools" in argv and argv[argv.index("--tools") + 1] == ""
    assert "--model" in argv
    assert argv[argv.index("--model") + 1] == "claude-opus-4-7"
    assert argv[argv.index("--system-prompt") + 1] == "PLAN_SYS"
    assert argv[-1] == "SRC"


def test_plan_client_call_legacy_path_no_system_prompt_flag(monkeypatch):
    captured: list[list[str]] = []
    monkeypatch.setattr(
        subprocess,
        "run",
        lambda argv, *_a, **_k: (captured.append(list(argv)) or _fake_completed(0, stdout='{"source_id":"x","updates":[]}')),
    )

    ClaudeCLIPlanClient().call("monolithic prompt")
    argv = captured[0]
    assert "--system-prompt" not in argv
    assert argv[-1] == "monolithic prompt"


def test_plan_client_wraps_errors_as_plan_error(monkeypatch):
    monkeypatch.setattr(subprocess, "run", lambda *_a, **_k: _fake_completed(1, stderr="boom"))
    with pytest.raises(PlanError):
        ClaudeCLIPlanClient().call("anything")


# --- plan prompt split ------------------------------------------------------


def test_build_plan_system_prompt_is_static():
    a = build_plan_system_prompt()
    b = build_plan_system_prompt()
    assert a == b
    assert "wiki authorship agent" in a
    # Schema JSON snippet is in the system prompt, not the user payload
    assert '"source_id"' in a


def test_build_plan_user_prompt_includes_source_and_pages():
    user = build_plan_user_prompt("source body here", {"wiki/concepts/foo.md": "foo body"})
    assert "Source under evaluation" in user
    assert "source body here" in user
    assert "wiki/concepts/foo.md" in user
    assert "foo body" in user


def test_build_plan_user_prompt_handles_empty_pages():
    user = build_plan_user_prompt("body", {})
    assert "no existing wiki pages" in user


def test_build_plan_prompt_backwards_compat_concatenates_both():
    """Legacy callers that still want one string get system + user concatenated."""
    full = build_plan_prompt("body", {"wiki/concepts/foo.md": "foo"})
    assert "wiki authorship agent" in full
    assert "Source under evaluation" in full
    assert "body" in full


# --- VLM client argv --------------------------------------------------------


def test_vlm_client_argv_uses_opus_read_tool_and_skip_perms(monkeypatch, tmp_path):
    img = tmp_path / "img.png"
    img.write_bytes(b"\x89PNG\r\n\x1a\n")
    captured: list[list[str]] = []
    monkeypatch.setattr(
        subprocess,
        "run",
        lambda argv, *_a, **_k: (captured.append(list(argv)) or _fake_completed(0, stdout="A description.")),
    )

    out = ClaudeCLIVLMClient().describe(str(img), "Describe the figure briefly.")
    assert out == "A description."
    argv = captured[0]
    assert "--bare" not in argv  # bypasses Max OAuth
    # VLM needs Read tool to attach the image
    assert argv[argv.index("--tools") + 1] == "Read"
    assert "--dangerously-skip-permissions" in argv
    assert argv[argv.index("--model") + 1] == "claude-opus-4-7"
    # System prompt carries both the fixed VLM directive and the caller prompt
    assert "Describe the figure briefly." in argv[argv.index("--system-prompt") + 1]
    # User positional carries the absolute image path
    assert str(img) in argv[-1]
    assert argv[-1].startswith("Image path:")


def test_vlm_client_raises_on_empty_output(monkeypatch, tmp_path):
    img = tmp_path / "img.png"
    img.write_bytes(b"\x89PNG\r\n\x1a\n")
    monkeypatch.setattr(subprocess, "run", lambda *_a, **_k: _fake_completed(0, stdout="   \n  "))
    with pytest.raises(VLMError, match="empty"):
        ClaudeCLIVLMClient().describe(str(img), "describe")


def test_vlm_client_wraps_errors_as_vlm_error(monkeypatch, tmp_path):
    img = tmp_path / "img.png"
    img.write_bytes(b"\x89PNG\r\n\x1a\n")
    monkeypatch.setattr(subprocess, "run", lambda *_a, **_k: _fake_completed(1, stderr="boom"))
    with pytest.raises(VLMError):
        ClaudeCLIVLMClient().describe(str(img), "describe")
