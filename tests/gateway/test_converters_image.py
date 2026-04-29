"""Tests for the Image converter (M33). VLM client is stubbed throughout."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from gateway import converters
from gateway import frontmatter as fm
from gateway import paths
from gateway.converters import image as image_mod
from gateway.converters.base import ConversionError
from gateway.vlm import FailingVLMClient, StubVLMClient


@pytest.fixture(autouse=True)
def _reset_registry():
    converters.reset_registry_for_tests()
    yield
    converters.reset_registry_for_tests()


def _build_png(path: Path, *, size: tuple[int, int] = (32, 32), color=(255, 0, 0)) -> None:
    img = Image.new("RGB", size, color)
    img.save(path, format="PNG")


def _build_jpeg(path: Path, *, size: tuple[int, int] = (16, 16)) -> None:
    img = Image.new("RGB", size, (0, 128, 255))
    img.save(path, format="JPEG", quality=80)


# --- detect ----------------------------------------------------------------


@pytest.mark.parametrize("name", [
    "/tmp/foo.png", "/tmp/foo.PNG",
    "/tmp/foo.jpg", "/tmp/foo.jpeg",
    "/tmp/foo.gif", "/tmp/foo.webp",
    "/tmp/foo.tiff", "/tmp/foo.tif",
    "/tmp/foo.bmp", "/tmp/foo.heic", "/tmp/foo.heif",
])
def test_image_detect_accepts_image_extensions(name):
    c = image_mod.ImageConverter(vlm_client=StubVLMClient())
    assert c.detect(name)


def test_image_detect_rejects_other_extensions_and_urls():
    c = image_mod.ImageConverter(vlm_client=StubVLMClient())
    assert not c.detect("/tmp/foo.pdf")
    assert not c.detect("/tmp/foo.docx")
    assert not c.detect("/tmp/foo.svg")  # vector formats not handled in v1
    assert not c.detect("https://example.com/foo.png")


# --- convert ---------------------------------------------------------------


def test_image_convert_writes_canonical_with_vlm_description(kb_root, tmp_path):
    src = tmp_path / "photo.png"
    _build_png(src, size=(64, 48))

    description = (
        "## Overview\nA test image.\n\n## Visible text\nNone.\n\n"
        "## Key elements\nA solid red square.\n\n## Domain-specific content\nNone."
    )
    stub = StubVLMClient(response=description)
    text = image_mod.ImageConverter(vlm_client=stub).convert(str(src))
    front, body = fm.parse(text)

    assert front["type"] == "image"
    assert front["id"].startswith("image-")
    assert front["title"] == "photo"
    assert front["meta"]["width"] == 64
    assert front["meta"]["height"] == 48
    assert front["meta"]["format"] == "PNG"
    assert front["meta"]["mode"] == "RGB"
    assert front["meta"]["original_filename"] == "photo.png"

    # Body is the VLM description verbatim
    assert "## Overview" in body
    assert "A solid red square." in body

    # Stub was called with the resolved path
    assert len(stub.calls) == 1
    called_path, _called_prompt = stub.calls[0]
    assert called_path.endswith("photo.png")


def test_image_convert_writes_sidecar(kb_root, tmp_path):
    src = tmp_path / "photo.png"
    _build_png(src)

    text = image_mod.ImageConverter(vlm_client=StubVLMClient()).convert(str(src))
    front, _ = fm.parse(text)

    sidecar = paths.raw_dir_for("image") / f"{front['id']}.png"
    assert sidecar.exists()
    assert sidecar.read_bytes() == src.read_bytes()


def test_image_convert_id_format_matches_validator_regex(kb_root, tmp_path):
    src = tmp_path / "photo.png"
    _build_png(src)

    text = image_mod.ImageConverter(vlm_client=StubVLMClient()).convert(str(src))
    front, _ = fm.parse(text)

    # image-YYYY-MM-DD-<12-hex>
    suffix = front["id"][len("image-"):]
    date_part, _, hash_part = suffix.rpartition("-")
    assert len(date_part) == 10  # YYYY-MM-DD
    assert date_part.count("-") == 2
    assert len(hash_part) == 12
    assert all(c in "0123456789abcdef" for c in hash_part)


def test_image_convert_jpeg_works(kb_root, tmp_path):
    src = tmp_path / "photo.jpg"
    _build_jpeg(src, size=(20, 30))

    text = image_mod.ImageConverter(vlm_client=StubVLMClient()).convert(str(src))
    front, _ = fm.parse(text)

    assert front["meta"]["format"] == "JPEG"
    assert front["meta"]["width"] == 20
    assert front["meta"]["height"] == 30
    sidecar = paths.raw_dir_for("image") / f"{front['id']}.jpg"
    assert sidecar.exists()


def test_image_convert_idempotent_id_for_same_content(kb_root, tmp_path):
    """Same image bytes → same canonical ID (within the same UTC day)."""
    src1 = tmp_path / "first.png"
    src2 = tmp_path / "second.png"
    _build_png(src1)
    src2.write_bytes(src1.read_bytes())

    f1, _ = fm.parse(image_mod.ImageConverter(vlm_client=StubVLMClient()).convert(str(src1)))
    f2, _ = fm.parse(image_mod.ImageConverter(vlm_client=StubVLMClient()).convert(str(src2)))
    assert f1["id"] == f2["id"]


def test_image_convert_missing_file_raises(kb_root):
    with pytest.raises(ConversionError):
        image_mod.ImageConverter(vlm_client=StubVLMClient()).convert("/does/not/exist.png")


def test_image_convert_corrupt_file_raises(kb_root, tmp_path):
    src = tmp_path / "corrupt.png"
    src.write_bytes(b"not a real PNG")
    with pytest.raises(ConversionError):
        image_mod.ImageConverter(vlm_client=StubVLMClient()).convert(str(src))


def test_image_convert_vlm_failure_raises_conversion_error(kb_root, tmp_path):
    src = tmp_path / "photo.png"
    _build_png(src)
    with pytest.raises(ConversionError):
        image_mod.ImageConverter(vlm_client=FailingVLMClient()).convert(str(src))


# --- registry --------------------------------------------------------------


def test_dispatch_png_path_routes_to_image_converter():
    c = converters.dispatch("/tmp/photo.png")
    assert isinstance(c, image_mod.ImageConverter)


def test_dispatch_jpeg_path_routes_to_image_converter():
    c = converters.dispatch("/tmp/photo.jpeg")
    assert isinstance(c, image_mod.ImageConverter)


def test_dispatch_heic_path_routes_to_image_converter():
    c = converters.dispatch("/tmp/photo.heic")
    assert isinstance(c, image_mod.ImageConverter)


def test_dispatch_svg_has_no_converter():
    """SVG (vector) is not an image format we handle in v1."""
    from gateway.converters import NoConverterError
    with pytest.raises(NoConverterError):
        converters.dispatch("/tmp/foo.svg")
