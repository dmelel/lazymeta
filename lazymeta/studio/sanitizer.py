"""
LazyMeta Image Forensics & Metadata Engine
===========================================
Engineered to sanitize AI-generated imagery (Google AI Flow / Imagen 3 / Midjourney / Flux)
and protect Facebook Page publishing from automated synthetic media flagging.

Core Pipeline:
1. Complete C2PA / IPTC Purge: Drops all JUMBF metadata, Google PKI signatures, and AI tags.
2. Geometric Perturbation: Micro-crop (1% margin) + Lanczos resampling to disrupt fixed SynthID coordinate grids.
3. Optical Sensor Grain: Ultra-fine (1.2 stddev) organic sensor noise simulating physical CMOS camera sensors.
4. Camera EXIF Persona: Injects realistic Apple iPhone 15 Pro hardware metadata (lens, aperture, shutter, ISO).
5. LazyMeta & Author Stamp: Signs with LazyMeta engine and author branding (r1fat.pages.dev).
6. Progressive High-Fidelity JPEG: Encodes at 95 quality for crystal-clear visual quality.
"""

import io
import random
from datetime import datetime
from pathlib import Path
from PIL import Image
from PIL.ExifTags import Base, IFD

AUTHOR_SIGNATURE = "r1fat.pages.dev"
APP_STAMP = "LazyMeta Studio v1.0 (r1fat.pages.dev)"


def apply_sensor_grain(img: Image.Image, intensity: float = 1.2) -> Image.Image:
    """
    Applies an ultra-fine, imperceptible photographic sensor noise layer.
    Breaks high-frequency diffusion checkerboards and masks latent pixel watermarks
    while keeping the image crystal clear.
    """
    try:
        import numpy as np
        arr = np.array(img, dtype=np.float32)
        noise = np.random.normal(0, intensity, arr.shape)
        arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
        return Image.fromarray(arr)
    except ImportError:
        # High-performance standard library fallback if numpy is unavailable
        w, h = img.size
        tile_size = 64
        noise_bytes = bytes(
            max(0, min(255, 128 + random.randint(-2, 2)))
            for _ in range(tile_size * tile_size)
        )
        tile = Image.frombytes("L", (tile_size, tile_size), noise_bytes).convert("RGB")
        tiled_noise = Image.new("RGB", (w, h))
        for x in range(0, w, tile_size):
            for y in range(0, h, tile_size):
                tiled_noise.paste(tile, (x, y))
        return Image.blend(img, tiled_noise, alpha=0.015)


def build_camera_exif(
    author: str = AUTHOR_SIGNATURE,
    app_stamp: str = APP_STAMP,
    timestamp: datetime | None = None
) -> Image.Exif:
    """
    Constructs a complete Apple iPhone 15 Pro camera EXIF persona
    embedded with LazyMeta and author authentication stamps.
    """
    if timestamp is None:
        timestamp = datetime.now()

    time_str = timestamp.strftime("%Y:%m:%d %H:%M:%S")

    exif = Image.Exif()
    # 0th IFD (Main Camera Identifiers)
    exif[Base.Make] = "Apple"
    exif[Base.Model] = "iPhone 15 Pro"
    exif[Base.Software] = app_stamp
    exif[Base.Artist] = author
    exif[Base.Copyright] = f"Copyright (c) LazyMeta · {author}"
    exif[Base.ImageDescription] = f"Shot on iPhone 15 Pro · Stamped by {app_stamp}"
    exif[Base.DateTime] = time_str
    exif[Base.Orientation] = 1

    # Exif SubIFD (Optical & Sensor Hardware Parameters)
    exif_ifd = exif.get_ifd(IFD.Exif)
    exif_ifd[36867] = time_str  # DateTimeOriginal
    exif_ifd[36868] = time_str  # DateTimeDigitized
    exif_ifd[33434] = (1, 120)   # ExposureTime (1/120 sec)
    exif_ifd[33437] = (178, 100) # FNumber (f/1.78)
    exif_ifd[34855] = 64         # ISOSpeedRatings (ISO 64)
    exif_ifd[37386] = (678, 100) # FocalLength (6.78mm)
    exif_ifd[41989] = 24         # FocalLengthIn35mmFilm (24mm equivalent)
    exif_ifd[42036] = "iPhone 15 Pro back camera 6.78mm f/1.78"  # LensModel
    exif_ifd[37510] = f"LazyMeta Core Engine · {author}".encode("utf-8")  # UserComment

    return exif


def sanitize_and_stamp_image(
    input_source: bytes | Path | Image.Image,
    target_path: Path,
    author: str = AUTHOR_SIGNATURE,
    app_stamp: str = APP_STAMP,
    quality: int = 95
) -> dict[str, any]:
    """
    Sanitizes raw AI output and saves as a clean, stamped, crystal-clear JPEG.
    
    Returns a dictionary of forensic processing stats.
    """
    target_path = Path(target_path).resolve()
    target_path.parent.mkdir(parents=True, exist_ok=True)

    # 1. Open and decode raw image
    if isinstance(input_source, (bytes, bytearray)):
        img = Image.open(io.BytesIO(input_source))
    elif isinstance(input_source, (str, Path)):
        img = Image.open(Path(input_source))
    else:
        img = input_source.copy()

    orig_width, orig_height = img.size

    # 2. Flatten transparency onto obsidian studio backdrop
    if img.mode in ("RGBA", "P"):
        bg = Image.new("RGB", img.size, (11, 15, 23))
        mask = img.split()[3] if img.mode == "RGBA" else None
        bg.paste(img, mask=mask)
        img = bg
    else:
        img = img.convert("RGB")

    # 3. Geometric coordinate perturbation (1% micro-crop + Lanczos resample)
    # Disrupts SynthID's spatial wavelet alignment without losing visible detail
    crop_x = max(1, int(orig_width * 0.01))
    crop_y = max(1, int(orig_height * 0.01))
    img = img.crop((crop_x, crop_y, orig_width - crop_x, orig_height - crop_y))
    img = img.resize((orig_width, orig_height), Image.Resampling.LANCZOS)

    # 4. Organic photographic sensor grain
    img = apply_sensor_grain(img, intensity=1.2)

    # 5. Build authentic Apple camera EXIF persona with LazyMeta stamp
    exif = build_camera_exif(author=author, app_stamp=app_stamp)

    # 6. Save clean JPEG (completely purges C2PA/JUMBF chunks from input)
    img.save(
        target_path,
        format="JPEG",
        quality=quality,
        optimize=True,
        progressive=True,
        exif=exif
    )

    file_size = target_path.stat().st_size
    return {
        "success": True,
        "path": str(target_path),
        "filename": target_path.name,
        "width": orig_width,
        "height": orig_height,
        "file_size": file_size,
        "author": author,
        "app_stamp": app_stamp,
    }

