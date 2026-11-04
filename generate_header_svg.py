#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generate_header_svg.py
Draws ANEESH as a pixel grid of SVG rectangles so letter shapes
cannot collapse the way Unicode block characters do in GitHub's renderer.
"""

from pathlib import Path

# 5 columns x 7 rows. '#' is a filled pixel.
LETTERS = {
    "A": [
        ".###.",
        "#...#",
        "#...#",
        "#####",
        "#...#",
        "#...#",
        "#...#",
    ],
    "N": [
        "#...#",
        "##..#",
        "#.#.#",
        "#..##",
        "#...#",
        "#...#",
        "#...#",
    ],
    "E": [
        "#####",
        "#....",
        "#....",
        "####.",
        "#....",
        "#....",
        "#####",
    ],
    "S": [
        ".####",
        "#....",
        "#....",
        ".###.",
        "....#",
        "....#",
        "####.",
    ],
    "H": [
        "#...#",
        "#...#",
        "#...#",
        "#####",
        "#...#",
        "#...#",
        "#...#",
    ],
}

NAME = "ANEESH"
CELL = 16
GAP = 4
LETTER_GAP = 28
PITCH = CELL + GAP
ROWS = 7
COLS = 5
CANVAS_W = 1200
CANVAS_H = 340


def build_pixels():
    letter_w = COLS * PITCH - GAP
    total_w = len(NAME) * letter_w + (len(NAME) - 1) * LETTER_GAP
    origin_x = (CANVAS_W - total_w) / 2
    origin_y = 78
    rects = []
    for i, ch in enumerate(NAME):
        lx = origin_x + i * (letter_w + LETTER_GAP)
        for r, row in enumerate(LETTERS[ch]):
            for c, bit in enumerate(row):
                if bit != "#":
                    continue
                x = lx + c * PITCH
                y = origin_y + r * PITCH
                rects.append(
                    f'<rect x="{x:.1f}" y="{y:.1f}" width="{CELL}" height="{CELL}" rx="2" fill="url(#bwGrad)"/>'
                )
    return "\n    ".join(rects)


def build_svg():
    pixels = build_pixels()
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}" font-family="'Segoe UI',Helvetica,Arial,sans-serif">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#000000"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
    <linearGradient id="bwGrad" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="1200" y2="0">
      <stop offset="0%" stop-color="#8b949e"/>
      <stop offset="50%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#8b949e"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="-600 0; 600 0; -600 0" dur="10s" repeatCount="indefinite"/>
    </linearGradient>
    <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#ffffff" fill-opacity="0.04"/>
    </pattern>
    <clipPath id="cardClip"><rect width="{CANVAS_W}" height="{CANVAS_H}" rx="22"/></clipPath>
  </defs>
  <g clip-path="url(#cardClip)">
    <rect width="{CANVAS_W}" height="{CANVAS_H}" fill="url(#bgGrad)"/>
    <rect width="{CANVAS_W}" height="{CANVAS_H}" fill="url(#grid)"/>
    <circle cx="120" cy="70" r="1" fill="#ffffff" opacity="0.6"><animate attributeName="opacity" values="0.1;0.8;0.1" dur="2s" repeatCount="indefinite"/></circle>
    <circle cx="320" cy="290" r="1.2" fill="#8b949e" opacity="0.4"><animate attributeName="opacity" values="0.2;0.7;0.2" dur="3s" repeatCount="indefinite"/></circle>
    <circle cx="1020" cy="80" r="1" fill="#ffffff" opacity="0.7"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="2.5s" repeatCount="indefinite"/></circle>
    <circle cx="1100" cy="270" r="1.2" fill="#8b949e" opacity="0.5"><animate attributeName="opacity" values="0.1;0.6;0.1" dur="3.5s" repeatCount="indefinite"/></circle>
    {pixels}
    <text x="600" y="292" text-anchor="middle" font-size="14" font-weight="700" fill="#6e7681" letter-spacing="4">FULL-STACK WEB DEVELOPER  •  OPEN SOURCE  •  BUILDER</text>
  </g>
  <rect x="0.75" y="0.75" width="1198.5" height="338.5" rx="22" fill="none" stroke="#30363d" stroke-width="1.5"/>
</svg>
"""


def main():
    out_path = Path("header_banner.svg")
    out_path.write_text(build_svg(), encoding="utf-8")
    print(f"Successfully generated {out_path.absolute()}")


if __name__ == "__main__":
    main()
