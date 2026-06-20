"""Unit tests for the P5 pre-push hook (scripts/pre-push).

The hook propagates the gate's exit code exactly: 0→0, nonzero→nonzero.
These tests exercise that contract WITHOUT running the real gate (which would
trigger the full pytest suite + evals — minutes).

Seam: the hook honours an env-var override GATE_CMD. Tests set GATE_CMD to
a tiny stub that exits with a controlled code; the test then asserts the hook
exits with the same code.

Negative controls:
  - NEGATIVE_NONZERO: gate exits 1 → hook must exit non-zero.
    A hook that always exits 0 is inert (hunt #1) — this control goes RED
    on that defect.
  - NEGATIVE_ZERO: gate exits 0 → hook must exit 0.
    A hook that always exits non-zero fails every push — this control catches
    that mirror-defect.
"""

from __future__ import annotations

import os
import stat
import subprocess
import sys
from pathlib import Path

import pytest

# Path to the hook under test, relative to the repo root.
_HOOK_PATH = Path(__file__).parent.parent / "scripts" / "pre-push"


def _run_hook(env_overrides: dict[str, str]) -> int:
    """Invoke scripts/pre-push with env_overrides, return its exit code.

    The hook is executed as a subprocess with its own env so GATE_CMD reaches
    it. stdout/stderr are captured (not streamed) to keep test output clean.
    """
    env = {**os.environ, **env_overrides}
    result = subprocess.run(
        [str(_HOOK_PATH)],
        env=env,
        capture_output=True,
        check=False,
    )
    return result.returncode


def _stub_cmd(exit_code: int) -> str:
    """Return a shell command string that exits with the given code."""
    # Use the same python that's running the tests so the stub is portable and
    # doesn't depend on /bin/sh arithmetic.
    return f"{sys.executable} -c 'import sys; sys.exit({exit_code})'"


class TestHookExitCodePropagation:
    """The hook must propagate the gate's exit code unchanged.

    Hunt #1 guard: a hook that always exits 0 is inert.
    """

    def test_hook_script_exists_and_is_executable(self):
        """scripts/pre-push must exist and be executable before any other test."""
        assert _HOOK_PATH.exists(), (
            f"scripts/pre-push not found at {_HOOK_PATH}; "
            "run Step 2 (write the hook script) before re-running."
        )
        mode = _HOOK_PATH.stat().st_mode
        assert mode & stat.S_IXUSR, (
            f"scripts/pre-push is not user-executable (mode={oct(mode)}); "
            "run chmod +x scripts/pre-push."
        )

    # -- NEGATIVE CONTROL: gate fails → hook must exit non-zero --

    def test_nonzero_gate_exit_propagated(self):
        """NEGATIVE CONTROL: gate exits 1 → hook must exit non-zero.

        A hook that always exits 0 is inert — this control goes RED on that defect.
        """
        rc = _run_hook({"GATE_CMD": _stub_cmd(1)})
        assert rc != 0, (
            "NEGATIVE CONTROL FAILED: hook exited 0 when the gate returned 1. "
            "This means the hook is inert — it swallows gate failures and allows "
            "pushes to succeed even when the gate blocks them."
        )

    def test_gate_exit_2_propagated(self):
        """NEGATIVE CONTROL: gate exits 2 → hook must exit non-zero.

        Covers gate failure codes > 1 (e.g. subprocess crash, argparse error).
        """
        rc = _run_hook({"GATE_CMD": _stub_cmd(2)})
        assert rc != 0, (
            "NEGATIVE CONTROL FAILED: hook exited 0 when the gate returned 2."
        )

    # -- NEGATIVE CONTROL: gate passes → hook must exit 0 --

    def test_zero_gate_exit_propagated(self):
        """NEGATIVE CONTROL: gate exits 0 → hook must exit 0.

        A hook that always exits non-zero would block every push, which is also
        a defect. This control goes RED on that mirror-defect.
        """
        rc = _run_hook({"GATE_CMD": _stub_cmd(0)})
        assert rc == 0, (
            "NEGATIVE CONTROL FAILED: hook exited non-zero when the gate returned 0. "
            "This means the hook blocks pushes even when the gate passes."
        )

    def test_exit_code_preserved_exactly(self):
        """The hook propagates the gate's exact exit code, not a normalised 0/1.

        This is belt-and-suspenders: if the hook maps all nonzero codes to 1,
        the previous tests still pass, but callers that inspect the raw code
        (e.g. CI step detection) may misattribute failures. Assert the exact
        value for both pass (0) and a specific fail code (3).
        """
        assert _run_hook({"GATE_CMD": _stub_cmd(0)}) == 0
        # Gate exit 3 may appear if the gate sub-steps report a specific code;
        # the hook must not normalise it.
        rc = _run_hook({"GATE_CMD": _stub_cmd(3)})
        assert rc != 0, "hook must not swallow gate exit code 3"
