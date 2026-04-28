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
    assert parsed_front == front
    assert parsed_body == body
