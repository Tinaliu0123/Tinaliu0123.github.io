#!/usr/bin/env python3
"""
Shrink JPEG/PNG images so each output file is at most N MiB (default 10).

Usage:
  python3 bin/compress_images_max_mb.py assets/img/misc
  python3 bin/compress_images_max_mb.py assets/img/misc --max-mb 5
  python3 bin/compress_images_max_mb.py photo.jpg --in-place

Requires: pip install Pillow
"""

from __future__ import annotations

import argparse
import sys
from io import BytesIO
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    print("Install Pillow: pip install Pillow", file=sys.stderr)
    sys.exit(1)

SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}


def jpeg_bytes(img: Image.Image, quality: int, progressive: bool = True) -> bytes:
    buf = BytesIO()
    rgb = img.convert("RGB")
    rgb.save(
        buf,
        format="JPEG",
        quality=quality,
        optimize=True,
        progressive=progressive,
    )
    return buf.getvalue()


def compress_one(path: Path, max_bytes: int) -> tuple[bool, str]:
    try:
        img = Image.open(path)
        img = ImageOps.exif_transpose(img)
    except OSError as e:
        return False, f"skip (open error): {e}"

    fmt = (img.format or "").upper()
    stem = path.stem
    suffix = path.suffix.lower()

    # PNG / WEBP with transparency -> flatten to white for JPEG target
    if fmt in ("PNG", "WEBP") and (img.mode in ("RGBA", "P") or "A" in img.getbands()):
        bg = Image.new("RGB", img.size, (255, 255, 255))
        rgba = img.convert("RGBA")
        bg.paste(rgba, mask=rgba.split()[3])
        work = bg
        out_suffix = ".jpg"
    elif fmt == "PNG" or suffix == ".png":
        work = img.convert("RGB")
        out_suffix = ".jpg"
    else:
        work = img.convert("RGB")
        out_suffix = ".jpg" if suffix in (".jpg", ".jpeg", ".jpe") else ".jpg"

    scale = 1.0
    best_data: bytes | None = None

    while scale >= 0.08:
        if scale < 1.0:
            w, h = work.size
            nw = max(1, int(w * scale))
            nh = max(1, int(h * scale))
            cur = work.resize((nw, nh), Image.Resampling.LANCZOS)
        else:
            cur = work

        for q in range(95, 19, -4):
            data = jpeg_bytes(cur, q)
            if len(data) <= max_bytes:
                best_data = data
                break
        if best_data is not None:
            break
        scale *= 0.82

    if best_data is None:
        return False, "could not reach target (try lower --max-mb or larger limit)"

    if path.suffix.lower() in (".jpg", ".jpeg", ".jpe"):
        out_path = path
    else:
        out_path = path.with_suffix(".jpg")

    out_path.write_bytes(best_data)
    if out_path.resolve() != path.resolve() and path.exists():
        path.unlink()

    extra = f" ({len(best_data) // 1024} KiB)"
    if out_path != path:
        return True, f"-> {out_path.name}{extra}"
    return True, "ok" + extra


def main() -> None:
    ap = argparse.ArgumentParser(description="Compress images to max file size (default 10 MiB).")
    ap.add_argument("paths", nargs="+", help="Files or directories")
    ap.add_argument("--max-mb", type=float, default=10.0, help="Max size per file in MiB (default: 10)")
    ap.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite originals (default when processing a directory)",
    )
    args = ap.parse_args()

    max_bytes = int(args.max_mb * 1024 * 1024)
    files: list[Path] = []

    for p in args.paths:
        path = Path(p)
        if path.is_dir():
            for f in sorted(path.iterdir()):
                if f.is_file() and f.suffix.lower() in SUFFIXES and not f.name.startswith("."):
                    files.append(f)
        elif path.is_file():
            files.append(path)

    if not files:
        print("No image files found.", file=sys.stderr)
        sys.exit(1)

    ok = 0
    for f in files:
        good, msg = compress_one(f, max_bytes)
        status = "OK" if good else "FAIL"
        print(f"{status}  {f}  {msg}")
        if good:
            ok += 1

    print(f"\nDone: {ok}/{len(files)}")
    sys.exit(0 if ok == len(files) else 1)


if __name__ == "__main__":
    main()
