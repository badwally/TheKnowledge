"""Tests for the CSV converter (M29)."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway import converters
from gateway import frontmatter as fm
from gateway import paths
from gateway.converters import csv as csv_mod
from gateway.converters.base import ConversionError


@pytest.fixture(autouse=True)
def _reset_registry():
    converters.reset_registry_for_tests()
    yield
    converters.reset_registry_for_tests()


# --- detect ----------------------------------------------------------------


def test_csv_detect_accepts_csv_and_tsv_paths():
    c = csv_mod.CSVConverter()
    assert c.detect("/tmp/foo.csv")
    assert c.detect("/tmp/foo.CSV")
    assert c.detect("relative/path.tsv")


def test_csv_detect_rejects_urls_and_other_extensions():
    c = csv_mod.CSVConverter()
    assert not c.detect("https://example.com/data.csv")
    assert not c.detect("/tmp/foo.md")
    assert not c.detect("/tmp/foo.xlsx")


# --- convert ---------------------------------------------------------------


def _write_csv(path: Path, rows: list[list[str]], delimiter: str = ",") -> None:
    text = "\n".join(delimiter.join(r) for r in rows) + "\n"
    path.write_text(text, encoding="utf-8")


def test_csv_convert_renders_table_and_writes_sidecar(kb_root, tmp_path):
    src = tmp_path / "sales.csv"
    _write_csv(
        src,
        [
            ["region", "qty", "amount"],
            ["NA", "12", "150.00"],
            ["EU", "7", "98.50"],
        ],
    )

    text = csv_mod.CSVConverter().convert(str(src))
    front, body = fm.parse(text)

    assert front["type"] == "csv"
    assert front["id"].startswith("csv-")
    assert len(front["id"]) == len("csv-") + 12
    assert front["title"] == "sales"
    assert front["meta"]["row_count"] == 2
    assert front["meta"]["column_count"] == 3
    assert front["meta"]["columns"] == ["region", "qty", "amount"]
    assert front["meta"]["delimiter"] == ","

    # Body has table preview
    assert "| region | qty | amount |" in body
    assert "| NA | 12 | 150.00 |" in body

    sidecar = paths.raw_dir_for("csv") / f"{front['id']}.csv"
    assert sidecar.exists()
    assert sidecar.read_bytes() == src.read_bytes()


def test_csv_convert_truncates_large_rows_with_note(kb_root, tmp_path):
    src = tmp_path / "big.csv"
    rows = [["col1", "col2"]]
    rows.extend([[f"r{i}", f"v{i}"] for i in range(75)])
    _write_csv(src, rows)

    text = csv_mod.CSVConverter().convert(str(src))
    front, body = fm.parse(text)

    assert front["meta"]["row_count"] == 75
    assert "25 additional rows omitted from preview" in body
    assert "Full data in sidecar" in body


def test_csv_convert_truncates_wide_columns_with_note(kb_root, tmp_path):
    src = tmp_path / "wide.csv"
    headers = [f"c{i}" for i in range(25)]
    data = [f"v{i}" for i in range(25)]
    _write_csv(src, [headers, data])

    text = csv_mod.CSVConverter().convert(str(src))
    front, body = fm.parse(text)

    assert front["meta"]["column_count"] == 25
    assert len(front["meta"]["columns"]) == 20
    assert "5 additional columns omitted from preview" in body


def test_csv_convert_escapes_pipe_in_cells(kb_root, tmp_path):
    src = tmp_path / "pipes.csv"
    src.write_text('name,note\nfoo,"a|b|c"\nbar,plain\n', encoding="utf-8")

    text = csv_mod.CSVConverter().convert(str(src))
    _, body = fm.parse(text)

    assert "a\\|b\\|c" in body


def test_csv_convert_handles_tsv(kb_root, tmp_path):
    src = tmp_path / "data.tsv"
    src.write_text("a\tb\tc\n1\t2\t3\n", encoding="utf-8")

    text = csv_mod.CSVConverter().convert(str(src))
    front, body = fm.parse(text)

    assert front["meta"]["delimiter"] == "\t"
    assert "| a | b | c |" in body
    assert "| 1 | 2 | 3 |" in body


def test_csv_convert_idempotent_id_for_same_content(kb_root, tmp_path):
    src1 = tmp_path / "first.csv"
    src2 = tmp_path / "second.csv"
    payload = "a,b\n1,2\n"
    src1.write_text(payload, encoding="utf-8")
    src2.write_text(payload, encoding="utf-8")

    front1, _ = fm.parse(csv_mod.CSVConverter().convert(str(src1)))
    front2, _ = fm.parse(csv_mod.CSVConverter().convert(str(src2)))

    assert front1["id"] == front2["id"]


def test_csv_convert_missing_file_raises(kb_root):
    with pytest.raises(ConversionError):
        csv_mod.CSVConverter().convert("/does/not/exist.csv")


def test_csv_convert_empty_file_raises(kb_root, tmp_path):
    src = tmp_path / "empty.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ConversionError):
        csv_mod.CSVConverter().convert(str(src))


# --- registry --------------------------------------------------------------


def test_dispatch_csv_path_routes_to_csv_converter():
    c = converters.dispatch("/tmp/data.csv")
    assert isinstance(c, csv_mod.CSVConverter)


def test_dispatch_tsv_path_routes_to_csv_converter():
    c = converters.dispatch("/tmp/data.tsv")
    assert isinstance(c, csv_mod.CSVConverter)
