"""Subprocess-level unit tests for NlmCLIClient.notebook_query.

The gateway-layer tests in tests/gateway/test_nlm.py inject a MockNlmClient.
These tests exercise the actual subprocess wrapper by mocking subprocess.run,
validating stdout-JSON parsing and error surfaces.
"""

from __future__ import annotations

import json
import subprocess
from unittest.mock import patch

import pytest

from gateway.nlm_client import NlmCLIClient, NlmError


def _completed(stdout: str = "", stderr: str = "", returncode: int = 0) -> subprocess.CompletedProcess:
    return subprocess.CompletedProcess(
        args=["nlm", "notebook", "query", "nb-1", "q"],
        returncode=returncode,
        stdout=stdout,
        stderr=stderr,
    )


def test_notebook_query_parses_canned_stdout():
    payload = {
        "answer": "Semaglutide reduces appetite via GLP-1 receptor agonism.",
        "citations": {"1": "Wilding 2021", "2": "Davies 2021"},
        "sources_used": ["src-a", "src-b"],
    }
    client = NlmCLIClient()
    with patch(
        "gateway.nlm_client.subprocess.run",
        return_value=_completed(stdout=json.dumps(payload)),
    ) as run:
        result = client.notebook_query("nb-1", "How does semaglutide work?")

    run.assert_called_once()
    assert run.call_args.args[0] == ["nlm", "notebook", "query", "nb-1", "How does semaglutide work?"]
    assert result == payload


def test_notebook_query_unwraps_value_envelope():
    payload = {
        "value": {
            "answer": "yes",
            "citations": {"1": "src-a"},
            "sources_used": ["src-a"],
        },
    }
    client = NlmCLIClient()
    with patch(
        "gateway.nlm_client.subprocess.run",
        return_value=_completed(stdout=json.dumps(payload)),
    ):
        result = client.notebook_query("nb-1", "anything")

    assert result["answer"] == "yes"
    assert result["citations"] == {"1": "src-a"}
    assert result["sources_used"] == ["src-a"]


def test_notebook_query_defaults_missing_keys():
    client = NlmCLIClient()
    with patch(
        "gateway.nlm_client.subprocess.run",
        return_value=_completed(stdout=json.dumps({})),
    ):
        result = client.notebook_query("nb-1", "q")

    assert result == {"answer": "", "citations": {}, "sources_used": []}


def test_notebook_query_nonzero_exit_raises_nlm_error():
    client = NlmCLIClient()
    with patch(
        "gateway.nlm_client.subprocess.run",
        return_value=_completed(stdout="", stderr="boom: auth failed", returncode=1),
    ):
        with pytest.raises(NlmError) as exc:
            client.notebook_query("nb-1", "q")

    assert "exited 1" in str(exc.value)
    assert "boom: auth failed" in str(exc.value)


def test_notebook_query_unparseable_json_raises_nlm_error():
    client = NlmCLIClient()
    with patch(
        "gateway.nlm_client.subprocess.run",
        return_value=_completed(stdout="not json at all"),
    ):
        with pytest.raises(NlmError) as exc:
            client.notebook_query("nb-1", "q")

    assert "could not parse" in str(exc.value)
    assert "not json at all" in str(exc.value)


def test_notebook_query_empty_stdout_raises_nlm_error():
    client = NlmCLIClient()
    with patch(
        "gateway.nlm_client.subprocess.run",
        return_value=_completed(stdout=""),
    ):
        with pytest.raises(NlmError):
            client.notebook_query("nb-1", "q")


def test_notebook_query_executable_not_found_raises_nlm_error():
    client = NlmCLIClient(executable="nlm-does-not-exist")
    with patch(
        "gateway.nlm_client.subprocess.run",
        side_effect=FileNotFoundError(),
    ):
        with pytest.raises(NlmError) as exc:
            client.notebook_query("nb-1", "q")

    assert "not found on PATH" in str(exc.value)


def test_notebook_query_timeout_raises_nlm_error():
    client = NlmCLIClient()
    with patch(
        "gateway.nlm_client.subprocess.run",
        side_effect=subprocess.TimeoutExpired(cmd="nlm", timeout=600.0),
    ):
        with pytest.raises(NlmError) as exc:
            client.notebook_query("nb-1", "q")

    assert "timed out" in str(exc.value)
