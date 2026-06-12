#!/usr/bin/env bash
#
# compress-image.sh — downscale + compress an image for the web using Pillow.
#
# Usage:
#   scripts/compress-image.sh INPUT [OUTPUT] [-w MAX_WIDTH] [-q QUALITY]
#
# Examples:
#   scripts/compress-image.sh figure.png                 # -> figure.webp (1600px, q80)
#   scripts/compress-image.sh figure.png out.jpg         # JPEG instead of WebP
#   scripts/compress-image.sh figure.png -w 1200 -q 75   # custom width/quality
#
# Defaults: max width 1600px (only downscales, never upscales), quality 80.
# Output format is inferred from the OUTPUT extension (.webp/.jpg/.png);
# when OUTPUT is omitted it writes a .webp next to the input.
#
# Notes:
#   - CMYK images are converted to RGB (fixes wrong colors in browsers).
#   - Requires Python 3 with Pillow:  python3 -c "import PIL"
#
set -euo pipefail

MAX_WIDTH=1600
QUALITY=80
INPUT=""
OUTPUT=""

usage() { sed -n '3,20p' "$0" | sed 's/^# \{0,1\}//'; exit "${1:-0}"; }

# Parse args: positional INPUT/OUTPUT plus -w/-q flags in any order.
while [[ $# -gt 0 ]]; do
  case "$1" in
    -w|--width)   MAX_WIDTH="$2"; shift 2 ;;
    -q|--quality) QUALITY="$2";   shift 2 ;;
    -h|--help)    usage 0 ;;
    -*)           echo "Unknown option: $1" >&2; usage 1 ;;
    *)
      if [[ -z "$INPUT" ]]; then INPUT="$1"
      elif [[ -z "$OUTPUT" ]]; then OUTPUT="$1"
      else echo "Unexpected argument: $1" >&2; usage 1
      fi
      shift ;;
  esac
done

[[ -n "$INPUT" ]] || { echo "Error: no input file given." >&2; usage 1; }
[[ -f "$INPUT" ]] || { echo "Error: input not found: $INPUT" >&2; exit 1; }
[[ -n "$OUTPUT" ]] || OUTPUT="${INPUT%.*}.webp"

python3 - "$INPUT" "$OUTPUT" "$MAX_WIDTH" "$QUALITY" <<'PY'
import os, sys
from PIL import Image

src, out, max_w, quality = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
im = Image.open(src)

# CMYK JPEGs render with wrong colors in many browsers — normalize to RGB.
if im.mode == "CMYK":
    im = im.convert("RGB")

# Downscale only if wider than the target; preserve aspect ratio.
if im.width > max_w:
    im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)

ext = os.path.splitext(out)[1].lower()
if ext in (".jpg", ".jpeg"):
    im.convert("RGB").save(out, "JPEG", quality=quality, optimize=True, progressive=True)
elif ext == ".webp":
    im.save(out, "WEBP", quality=quality, method=6)
elif ext == ".png":
    im.save(out, "PNG", optimize=True)
else:
    sys.exit(f"Unsupported output extension: {ext or '(none)'} — use .webp/.jpg/.png")

before, after = os.path.getsize(src), os.path.getsize(out)
pct = (1 - after / before) * 100 if before else 0
print(f"{src} ({before//1024} KB) -> {out} ({after//1024} KB, -{pct:.0f}%)")
PY
