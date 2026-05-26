"""Frontmatter parser/serializer tests."""

import pytest

from gateway import frontmatter as fm


def test_parse_minimal():
    text = "---\nid: yt-abc\ntype: youtube\n---\nbody here\n"
    front, body = fm.parse(text)
    assert front == {"id": "yt-abc", "type": "youtube"}
    assert body == "body here\n"


def test_parse_missing_opening():
    with pytest.raises(fm.FrontmatterError):
        fm.parse("no frontmatter here")


def test_parse_missing_closing():
    with pytest.raises(fm.FrontmatterError):
        fm.parse("---\nid: x\nstill yaml\nstill yaml")


def test_parse_invalid_yaml():
    text = "---\nthis: : is: bad\n---\nbody\n"
    with pytest.raises(fm.FrontmatterError):
        fm.parse(text)


def test_parse_non_mapping_rejected():
    text = "---\n- list\n- not\n- mapping\n---\nbody\n"
    with pytest.raises(fm.FrontmatterError):
        fm.parse(text)


def test_serialize_roundtrip():
    front = {"id": "yt-abc", "type": "youtube", "title": "Hello"}
    body = "Body content.\n\nMore body.\n"
    text = fm.serialize(front, body)
    parsed_front, parsed_body = fm.parse(text)
    # schema_version is injected automatically; exclude it from the equality check
    assert {k: v for k, v in parsed_front.items() if k != "schema_version"} == front
    assert parsed_front["schema_version"] == fm.CURRENT_SCHEMA_VERSION
    assert parsed_body == body


def test_serialize_injects_schema_version():
    front = {"id": "yt-xyz", "type": "youtube"}
    text = fm.serialize(front, "body\n")
    parsed, _ = fm.parse(text)
    assert parsed["schema_version"] == fm.CURRENT_SCHEMA_VERSION
    # schema_version is the first key
    assert list(parsed.keys())[0] == "schema_version"


def test_serialize_preserves_existing_schema_version():
    front = {"schema_version": 99, "id": "yt-abc"}
    text = fm.serialize(front, "body\n")
    parsed, _ = fm.parse(text)
    assert parsed["schema_version"] == 99
