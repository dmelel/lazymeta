import json
import base64
import io
from pathlib import Path
from PIL import Image

import pytest

from lazymeta.studio.server import (
    extract_prompts_from_md,
    load_campaign_data,
    get_studio_state,
    save_studio_state,
)


def test_extract_prompts_from_md(tmp_path: Path):
    md_content = """# Test Campaign

### Image 01: Morning Light
* **File**: `images/01.jpg`
* **Prompt**:
  > A fluffy kitten playing with yarn, warm lighting, 8k

---

### Image 02: Afternoon Nap
* **Prompt**:
  > A sleeping cat on a windowsill, cozy atmosphere
"""
    md_file = tmp_path / "prompts.md"
    md_file.write_text(md_content, encoding="utf-8")

    prompts = extract_prompts_from_md(md_file)
    assert len(prompts) == 2
    assert "A fluffy kitten playing with yarn" in prompts[1]
    assert "A sleeping cat on a windowsill" in prompts[2]


def test_load_campaign_data(tmp_path: Path):
    campaign_dir = tmp_path / "campaign_test"
    campaign_dir.mkdir()
    images_dir = campaign_dir / "images"
    images_dir.mkdir()

    # Create dummy image 01.jpg
    img = Image.new("RGB", (200, 200), color=(100, 150, 200))
    img.save(images_dir / "01.jpg")

    captions_data = [
        {
            "id": 1,
            "day": 1,
            "slot": "morning",
            "bucket": "The Epiphany",
            "caption": "Test Caption 1",
            "images": ["01.jpg"]
        },
        {
            "id": 2,
            "day": 1,
            "slot": "afternoon",
            "bucket": "The Contrarian",
            "caption": "Test Caption 2",
            "images": ["02.jpg"]
        }
    ]
    (campaign_dir / "captions.json").write_text(json.dumps(captions_data), encoding="utf-8")

    data = load_campaign_data(campaign_dir)
    assert data["folder_name"] == "campaign_test"
    assert data["total_posts"] == 2
    assert data["images_ready"] == 1
    assert data["images_missing"] == 1
    assert data["completion_percent"] == 50.0

    posts = data["posts"]
    assert len(posts) == 2
    assert posts[0]["is_ready"] is True
    assert posts[0]["images"][0]["exists"] is True
    assert posts[0]["images"][0]["dimensions"] == "200x200"
    assert posts[1]["is_ready"] is False
    assert posts[1]["images"][0]["exists"] is False


def test_sanitize_and_stamp_image(tmp_path: Path):
    from lazymeta.studio.sanitizer import sanitize_and_stamp_image
    from PIL.ExifTags import Base

    # Create dummy image
    test_img = Image.new("RGBA", (300, 300), color=(100, 200, 255, 255))
    src_file = tmp_path / "raw_ai_input.png"
    test_img.save(src_file, "PNG")

    out_file = tmp_path / "sanitized_output.jpg"
    stats = sanitize_and_stamp_image(
        input_source=src_file,
        target_path=out_file,
        author="r1fat.pages.dev"
    )

    assert stats["success"] is True
    assert out_file.exists()

    raw_bytes = out_file.read_bytes()
    assert b"c2pa" not in raw_bytes
    assert b"SynthID" not in raw_bytes
    assert b"r1fat.pages.dev" in raw_bytes
    assert b"LazyMeta" in raw_bytes

    with Image.open(out_file) as im:
        ex = im.getexif()
        assert ex.get(Base.Make) == "Apple"
        assert ex.get(Base.Model) == "iPhone 15 Pro"
        assert ex.get(Base.Artist) == "r1fat.pages.dev"
        assert "LazyMeta" in ex.get(Base.Software)


