"""--fetch-pdf flag on `wiki ingest`: parses and forwards to the ingest op.

The arxiv converter supports full-text PDF extraction via convert_with_pdf,
exposed on the ingest op as fetch_pdf. This wires the CLI surface to it so the
operation is reproducible (default ingest is abstract-only for arxiv).
"""

import argparse

import gateway.cli as cli
from gateway.cli import build_parser
from gateway.core import OperationResult


def test_fetch_pdf_flag_parses_true():
    ns = build_parser().parse_args(["ingest", "https://arxiv.org/abs/2301.07041", "--fetch-pdf"])
    assert ns.fetch_pdf is True


def test_fetch_pdf_defaults_false():
    ns = build_parser().parse_args(["ingest", "https://arxiv.org/abs/2301.07041"])
    assert ns.fetch_pdf is False


def test_run_ingest_forwards_fetch_pdf(monkeypatch):
    captured = {}

    def fake_ingest(source, **kwargs):
        captured.update(kwargs)
        captured["source"] = source
        return OperationResult(success=True, summary="ok")

    monkeypatch.setattr("gateway.ops.ingest.ingest", fake_ingest)
    ns = argparse.Namespace(
        input="https://arxiv.org/abs/2301.07041",
        domain="ai-and-agents",
        with_plan=False,
        draft=False,
        force_include=False,
        fetch_pdf=True,
        plan_timeout=None,
    )
    cli._run_ingest(ns)
    assert captured.get("fetch_pdf") is True
