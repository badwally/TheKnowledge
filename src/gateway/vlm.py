"""VLM (vision-language model) client for image description.

The default `VLMClient` shells out to `claude -p` so the user's Max-plan
auth is reused without an `ANTHROPIC_API_KEY`. Callers (the image converter)
inject a `StubVLMClient` in tests.

M44: delegates to `gateway.llm.ClaudeCLIClient` for ``--bare``,
``--system-prompt``, and explicit ``--model claude-opus-4-7``. Keeps the
Read tool enabled (via ``tools="Read"``) so Claude Code can still attach
the image referenced by absolute path; ``--dangerously-skip-permissions``
suppresses the interactive prompt for reading outside cwd.
"""

from __future__ import annotations

from pathlib import Path
from typing import Protocol

from gateway.llm import ClaudeCLIClient, LLMError, model_for


_VLM_SYSTEM_PROMPT = (
    "You are an image-description assistant. When given the absolute path to an "
    "image in the user message, read the image, then return ONLY the description "
    "requested — no preamble, no apology, no markdown fences."
)


class VLMError(RuntimeError):
    """Raised when the VLM call fails or returns an unparseable response."""


class VLMClient(Protocol):
    """Anything that takes (image_path, prompt) and returns a description string."""

    def describe(self, image_path: str, prompt: str) -> str: ...


class ClaudeCLIVLMClient:
    """Default backend: `claude -p` via the shared `ClaudeCLIClient`.

    The caller-supplied `prompt` is folded into the system prompt (since it's
    a describe directive that doesn't vary per image within a converter run).
    The image absolute path is the user positional; Claude Code's Read tool
    picks it up as multimodal content.

    Slow per call (~10–30s) but correct for the use case (one image per ingest).
    """

    def __init__(
        self,
        executable: str = "claude",
        timeout_s: float = 180.0,
        *,
        model: str | None = None,
        cli: ClaudeCLIClient | None = None,
    ):
        self._model = model or model_for("vlm")
        self._cli = cli or ClaudeCLIClient(
            executable=executable,
            timeout_s=timeout_s,
            max_retries=0,
        )

    def describe(self, image_path: str, prompt: str) -> str:
        abs_path = str(Path(image_path).expanduser().resolve())
        # `--dangerously-skip-permissions` lets the Read tool open a file
        # outside cwd without an interactive prompt. Safe here: the path
        # was explicitly passed by the user via `wiki ingest`, the prompt
        # is constrained to image description, and stdout is captured.
        try:
            text = self._cli.call(
                user_prompt=f"Image path: {abs_path}",
                system_prompt=f"{_VLM_SYSTEM_PROMPT}\n\n{prompt}",
                model=self._model,
                tools="Read",
                extra_args=["--dangerously-skip-permissions"],
            )
        except LLMError as e:
            raise VLMError(str(e)) from e

        text = text.strip()
        if not text:
            raise VLMError("claude -p returned an empty description")
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
