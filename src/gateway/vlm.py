"""VLM (vision-language model) client for image description.

The default `VLMClient` shells out to `claude -p` so the user's Max-plan
auth is reused without an `ANTHROPIC_API_KEY`. Callers (the image converter)
inject a `StubVLMClient` in tests.

Mirrors the `gateway/filter/semantic.py` Protocol + ClaudeCLI + Stub pattern.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Protocol


class VLMError(RuntimeError):
    """Raised when the VLM call fails or returns an unparseable response."""


class VLMClient(Protocol):
    """Anything that takes (image_path, prompt) and returns a description string."""

    def describe(self, image_path: str, prompt: str) -> str: ...


class ClaudeCLIVLMClient:
    """Default backend: `claude -p <prompt>` subprocess call.

    Includes the absolute image path in the prompt body. Claude Code attaches
    file paths referenced this way as multimodal content. Slow per call
    (~10-30s) but correct for the use case (one image per ingest).
    """

    def __init__(self, executable: str = "claude", timeout_s: float = 180.0):
        self._exe = executable
        self._timeout = timeout_s

    def describe(self, image_path: str, prompt: str) -> str:
        # Resolve to absolute path so claude -p can find it regardless of cwd.
        abs_path = str(Path(image_path).expanduser().resolve())
        full_prompt = f"{prompt}\n\nImage path: {abs_path}"
        # `--dangerously-skip-permissions` is necessary so the subprocess can
        # use the Read tool to attach the image without an interactive prompt.
        # Safe in this context: the prompt only asks Claude to describe one
        # specific image, the path was explicitly passed by the user via
        # `wiki ingest`, and the subprocess output is captured then discarded.
        cmd = [self._exe, "-p", full_prompt, "--dangerously-skip-permissions"]
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self._timeout,
                check=False,
            )
        except FileNotFoundError as e:
            raise VLMError(
                f"`{self._exe}` not found on PATH; install Claude Code or inject a VLMClient"
            ) from e
        except subprocess.TimeoutExpired as e:
            raise VLMError(f"`{self._exe} -p` timed out after {self._timeout}s") from e

        if result.returncode != 0:
            raise VLMError(
                f"`{self._exe} -p` exited {result.returncode}: {result.stderr.strip()[:300]}"
            )
        text = result.stdout.strip()
        if not text:
            raise VLMError(f"`{self._exe} -p` returned an empty description")
        return text


class StubVLMClient:
    """Test-only stub. Returns a canned description regardless of input."""

    def __init__(self, response: str = "A test image. Visible text: None. Key elements: synthetic test fixture."):
        self._response = response
        self.calls: list[tuple[str, str]] = []  # records (image_path, prompt) for assertions

    def describe(self, image_path: str, prompt: str) -> str:
        self.calls.append((image_path, prompt))
        return self._response


class FailingVLMClient:
    """Test-only stub that raises VLMError on every call."""

    def __init__(self, message: str = "stubbed VLM failure"):
        self._message = message

    def describe(self, image_path: str, prompt: str) -> str:
        raise VLMError(self._message)
