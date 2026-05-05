"""Smoke test for `wiki serve` CLI argument parsing."""

from __future__ import annotations

import pytest

from gateway.cli import build_parser


def test_serve_parser_accepts_default_args():
    parser = build_parser()
    ns = parser.parse_args(["serve"])
    assert ns.subcommand == "serve"
    assert ns.port == 7474
    assert ns.bind == "127.0.0.1"


def test_serve_parser_accepts_custom_port_and_bind():
    parser = build_parser()
    ns = parser.parse_args(["serve", "--port", "9000", "--bind", "0.0.0.0"])
    assert ns.port == 9000
    assert ns.bind == "0.0.0.0"
