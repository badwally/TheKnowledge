"""Subprocess wrapper around the `nlm` CLI.

The `NlmClient` Protocol is the only sanctioned API for hitting NotebookLM.
Tests inject `MockNlmClient`; production uses `NlmCLIClient` which shells out.

Per WIKI § 9.3 and the user's "I don't want to be the weak link" constraint,
agents must NOT call `nlm` directly. The schema doc forbids it; lint (M9)
greps for raw `nlm` invocations in committed wiki content.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
import re
import subprocess
from pathlib import Path
from typing import Protocol


DEFAULT_TIMEOUT_S = 600.0  # artifact creation can take several minutes


class NlmError(RuntimeError):
    """Raised when an `nlm` invocation fails or returns unparseable output."""


@dataclass
class ArtifactInfo:
    """Result of an artifact-creation call.

    `artifact_id` is best-effort: extracted from `nlm` stdout via regex.
    Empty string means the download will grab "the latest" of that type
    for the notebook (acceptable for v1).
    """

    notebook_id: str
    artifact_type: str          # "slides" | "audio" | "report"
    artifact_id: str = ""       # may be empty if extraction fails
    raw_stdout: str = ""        # preserved for debugging


class NlmClient(Protocol):
    """Operations the gateway needs from NotebookLM."""

    def notebook_create(self, title: str) -> str: ...

    def source_add_url(self, notebook_id: str, url: str) -> None: ...

    def source_add_text(self, notebook_id: str, content: str, *, title: str | None = None) -> None: ...

    def source_add_file(self, notebook_id: str, file_path: Path, *, title: str | None = None) -> None: ...

    def slides_create(self, notebook_id: str, *, focus: str | None = None) -> ArtifactInfo: ...

    def slides_revise(self, artifact_id: str, slide_revisions: list[tuple[int, str]]) -> ArtifactInfo: ...

    def audio_create(self, notebook_id: str, *, focus: str | None = None) -> ArtifactInfo: ...

    def report_create(self, notebook_id: str, *, format: str = "Briefing Doc") -> ArtifactInfo: ...

    def download_slides(self, notebook_id: str, dest: Path, *, artifact_id: str | None = None) -> None: ...

    def download_audio(self, notebook_id: str, dest: Path, *, artifact_id: str | None = None) -> None: ...

    def download_report(self, notebook_id: str, dest: Path, *, artifact_id: str | None = None) -> None: ...

    def notebook_query(self, notebook_id: str, question: str) -> dict: ...

    def artifact_status(self, notebook_id: str, artifact_id: str) -> str: ...

    def notebook_sources(self, notebook_id: str) -> list[dict]: ...


# --- subprocess implementation ---------------------------------------------


_ARTIFACT_ID_PATTERNS = [
    re.compile(r"artifact[_\s]id[\s:=]+([A-Za-z0-9_\-]+)", re.IGNORECASE),
    re.compile(r"\b(artifact_[A-Za-z0-9_\-]{6,})\b"),
    re.compile(r"\bid[:\s]+([A-Za-z0-9_\-]{8,})\b"),
]


def _extract_artifact_id(stdout: str) -> str:
    """Best-effort regex extraction of an artifact ID from `nlm` output."""
    for pattern in _ARTIFACT_ID_PATTERNS:
        match = pattern.search(stdout)
        if match:
            return match.group(1)
    return ""


def _extract_notebook_id(stdout: str) -> str:
    """Pull a notebook ID out of `nlm notebook create` stdout."""
    # `nlm notebook create <title>` typically prints something like
    # "Created notebook: <id>" or includes the URL with the id.
    patterns = [
        re.compile(r"notebook[/?]([A-Za-z0-9_\-]{12,})"),
        re.compile(r"\b([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})\b"),
        re.compile(r"\bid[:\s]+([A-Za-z0-9_\-]{12,})\b"),
    ]
    for pattern in patterns:
        match = pattern.search(stdout)
        if match:
            return match.group(1)
    raise NlmError(f"could not extract notebook id from `nlm notebook create` stdout: {stdout!r}")


class NlmCLIClient:
    """Default backend: shells out to `nlm <cmd>`."""

    def __init__(self, executable: str = "nlm", timeout_s: float = DEFAULT_TIMEOUT_S):
        self._exe = executable
        self._timeout = timeout_s

    # --- helpers ----------------------------------------------------------

    def _run(self, args: list[str], *, timeout_s: float | None = None) -> subprocess.CompletedProcess:
        try:
            return subprocess.run(
                [self._exe, *args],
                capture_output=True,
                text=True,
                timeout=timeout_s if timeout_s is not None else self._timeout,
                check=False,
            )
        except FileNotFoundError as e:
            raise NlmError(
                f"`{self._exe}` not found on PATH; install notebooklm-mcp-cli or inject an NlmClient"
            ) from e
        except subprocess.TimeoutExpired as e:
            raise NlmError(f"`{self._exe} {' '.join(args)}` timed out after {self._timeout}s") from e

    def _check(self, result: subprocess.CompletedProcess, *, args: list[str]) -> None:
        if result.returncode != 0:
            raise NlmError(
                f"`{self._exe} {' '.join(args)}` exited {result.returncode}: "
                f"{result.stderr.strip()[:500] or result.stdout.strip()[:500]}"
            )

    # --- notebooks ---------------------------------------------------------

    def notebook_create(self, title: str) -> str:
        args = ["notebook", "create", title]
        result = self._run(args)
        self._check(result, args=args)
        return _extract_notebook_id(result.stdout + "\n" + result.stderr)

    def notebook_list_json(self) -> list[dict]:
        args = ["notebook", "list", "--json"]
        result = self._run(args, timeout_s=60.0)
        self._check(result, args=args)
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError as e:
            raise NlmError(f"could not parse `{self._exe} notebook list --json`: {e}") from e
        if not isinstance(data, list):
            raise NlmError(f"expected JSON array from notebook list, got {type(data).__name__}")
        return data

    # --- sources -----------------------------------------------------------

    def source_add_url(self, notebook_id: str, url: str) -> None:
        # Modern form: `nlm source add NOTEBOOK_ID --url URL --wait`. The
        # legacy `nlm add url NOTEBOOK URL` form was removed when the CLI
        # consolidated source-creation under `source add` with explicit
        # flags. `--wait` blocks until NotebookLM has indexed the source,
        # so query-time failures don't masquerade as add-time successes.
        args = ["source", "add", notebook_id, "--url", url, "--wait"]
        result = self._run(args, timeout_s=max(self._timeout, 660.0))
        self._check(result, args=args)

    def source_add_text(self, notebook_id: str, content: str, *, title: str | None = None) -> None:
        # Use the modern `nlm source add --text VALUE` form. The legacy
        # `nlm add text NOTEBOOK TEXT` accepts text only as a positional
        # argv element, which mangles long bodies; the flag form is safe.
        args = ["source", "add", notebook_id, "--text", content, "--wait"]
        if title:
            args.extend(["--title", title])
        result = self._run(args)
        self._check(result, args=args)

    def source_add_file(self, notebook_id: str, file_path: Path, *, title: str | None = None) -> None:
        args = ["source", "add", notebook_id, "--file", str(file_path), "--wait"]
        if title:
            args.extend(["--title", title])
        result = self._run(args)
        self._check(result, args=args)

    def notebook_sources(self, notebook_id: str) -> list[dict]:
        """Return the list of source dicts (id, title, url?) currently in
        the notebook. Used by `nlm_sync` to reconcile NotebookLM-side state
        against frontmatter so partially-loaded corpora don't get duplicated.
        """
        args = ["notebook", "get", notebook_id]
        result = self._run(args, timeout_s=60.0)
        self._check(result, args=args)
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError as e:
            raise NlmError(
                f"could not parse `{self._exe} notebook get` output: {e}"
            ) from e
        value = data.get("value", data) if isinstance(data, dict) else {}
        sources = value.get("sources") or []
        return [s for s in sources if isinstance(s, dict)]

    # --- artifact status (M37) ---------------------------------------------

    def artifact_status(self, notebook_id: str, artifact_id: str) -> str:
        """Return the status of one artifact in a notebook ('completed' / 'in_progress' / 'unknown' / 'failed' / '')."""
        args = ["studio", "status", notebook_id]
        result = self._run(args, timeout_s=60.0)
        self._check(result, args=args)
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError as e:
            raise NlmError(f"could not parse `{self._exe} {' '.join(args)}` stdout: {e}") from e
        if not isinstance(data, list):
            raise NlmError(f"expected JSON array from studio status, got {type(data).__name__}")
        for item in data:
            if isinstance(item, dict) and item.get("id") == artifact_id:
                return str(item.get("status") or "")
        return ""

    # --- artifacts ---------------------------------------------------------

    def slides_create(self, notebook_id: str, *, focus: str | None = None) -> ArtifactInfo:
        args = ["slides", "create", notebook_id, "--confirm"]
        if focus:
            args.extend(["--focus", focus])
        result = self._run(args)
        self._check(result, args=args)
        return ArtifactInfo(
            notebook_id=notebook_id,
            artifact_type="slides",
            artifact_id=_extract_artifact_id(result.stdout + "\n" + result.stderr),
            raw_stdout=result.stdout,
        )

    def slides_revise(self, artifact_id: str, slide_revisions: list[tuple[int, str]]) -> ArtifactInfo:
        args = ["slides", "revise", artifact_id, "--confirm"]
        for slide_num, instruction in slide_revisions:
            args.extend(["--slide", f"{slide_num} {instruction}"])
        result = self._run(args)
        self._check(result, args=args)
        return ArtifactInfo(
            notebook_id="",  # revise doesn't take a notebook_id directly
            artifact_type="slides",
            artifact_id=_extract_artifact_id(result.stdout + "\n" + result.stderr) or "",
            raw_stdout=result.stdout,
        )

    def audio_create(self, notebook_id: str, *, focus: str | None = None) -> ArtifactInfo:
        args = ["audio", "create", notebook_id, "--confirm"]
        if focus:
            args.extend(["--focus", focus])
        result = self._run(args)
        self._check(result, args=args)
        return ArtifactInfo(
            notebook_id=notebook_id,
            artifact_type="audio",
            artifact_id=_extract_artifact_id(result.stdout + "\n" + result.stderr),
            raw_stdout=result.stdout,
        )

    def report_create(self, notebook_id: str, *, format: str = "Briefing Doc") -> ArtifactInfo:
        args = ["report", "create", notebook_id, "--confirm", "--format", format]
        result = self._run(args)
        self._check(result, args=args)
        return ArtifactInfo(
            notebook_id=notebook_id,
            artifact_type="report",
            artifact_id=_extract_artifact_id(result.stdout + "\n" + result.stderr),
            raw_stdout=result.stdout,
        )

    # --- downloads ---------------------------------------------------------

    def _download(self, kind: str, notebook_id: str, dest: Path, artifact_id: str | None) -> None:
        args = ["download", kind, notebook_id, "--output", str(dest)]
        if artifact_id:
            args.extend(["--id", artifact_id])
        if kind == "slide-deck":
            args.append("--no-progress")
        result = self._run(args)
        self._check(result, args=args)
        if not dest.exists():
            raise NlmError(f"`nlm download {kind}` reported success but {dest} does not exist")

    def download_slides(self, notebook_id: str, dest: Path, *, artifact_id: str | None = None) -> None:
        self._download("slide-deck", notebook_id, dest, artifact_id)

    def download_audio(self, notebook_id: str, dest: Path, *, artifact_id: str | None = None) -> None:
        self._download("audio", notebook_id, dest, artifact_id)

    def download_report(self, notebook_id: str, dest: Path, *, artifact_id: str | None = None) -> None:
        self._download("report", notebook_id, dest, artifact_id)

    # --- query -------------------------------------------------------------

    def notebook_query(self, notebook_id: str, question: str) -> dict:
        """Ask the notebook a question; return parsed answer + citations.

        Ports `query_notebook` from research-notebook/src/research/query.py.
        The `nlm notebook query` command emits JSON on stdout by default; the
        response is either `{value: {...}}` or the inner shape directly.
        """
        args = ["notebook", "query", notebook_id, question]
        result = self._run(args)
        if result.returncode != 0:
            stderr = result.stderr or ""
            if "NOT_FOUND" in stderr or "error code 5" in stderr:
                raise NlmError(
                    f"notebook {notebook_id} returned NOT_FOUND. The notebook is "
                    "reachable but its corpus is empty or unindexed — "
                    "NotebookLM rejects queries against zero-source notebooks. "
                    "Verify with `nlm notebook get <id>`; if source_count is 0, "
                    "sync sources via `wiki nlm-add <domain> <source-id>` "
                    "before querying. The CLI's auth-related advice is misleading "
                    "in this case."
                )
        self._check(result, args=args)
        try:
            raw = json.loads(result.stdout)
        except json.JSONDecodeError as e:
            raise NlmError(
                f"could not parse `{self._exe} {' '.join(args)}` stdout as JSON: "
                f"{e}; stdout={result.stdout.strip()[:500]!r}"
            ) from e
        value = raw.get("value", raw) if isinstance(raw, dict) else {}
        return {
            "answer": value.get("answer", ""),
            "citations": value.get("citations", {}),
            "sources_used": value.get("sources_used", []),
        }


def notebook_url(notebook_id: str) -> str:
    """Best-effort live URL for the notebook; used in artifact frontmatter."""
    return f"https://notebooklm.google.com/notebook/{notebook_id}"


def notebook_artifact_url(notebook_id: str, artifact_id: str) -> str:
    """Live URL pointing at the specific artifact, falling back to notebook root."""
    if artifact_id:
        return f"https://notebooklm.google.com/notebook/{notebook_id}/artifact/{artifact_id}"
    return notebook_url(notebook_id)
