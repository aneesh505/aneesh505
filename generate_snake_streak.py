#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generate_snake_streak.py
Create a looping “snake” animation that follows a GitHub contribution streak.

Features:
* Pixel‑art snake that crawls over the contribution heat‑map.
* Uses real contribution data (only cells with >0 commits are part of the path).
* Outputs an animated GIF (default 10 fps, infinite loop).
* No GitHub token required – reads the public SVG at
  https://github.com/users/<USERNAME>/contributions

Usage:
    python generate_snake_streak.py <github‑username> [output‑file]

Example:
    python generate_snake_streak.py aneesh505 snake.gif
"""

import sys
import datetime as dt
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw

# ---------------------------------------------------------------------------
# 1️⃣  Helpers
# ---------------------------------------------------------------------------
SVG_URL = "https://github.com/users/{user}/contributions"

# Colours that GitHub uses for the heat‑map (light to dark)
PALETTE = {
    "#ebedf0": (235, 237, 240),  # no contributions (background)
    "#9be9a8": (155, 233, 168),
    "#40c463": (64, 196, 99),
    "#30a14e": (48, 161, 78),
    "#216e39": (33, 110, 57),
}

# Snake colours
SNAKE_BODY = (255, 255, 255, 180)   # semi‑transparent white
SNAKE_HEAD = (255, 255, 0, 255)     # bright yellow

# Size of a single cell (GitHub uses 10 px square with 2 px padding)
CELL_SIZE = 10
CELL_PADDING = 2
IMG_BORDER = 4   # a little margin around the whole grid


def fetch_svg(username: str) -> str:
    """Download the public contributions SVG for *username*."""
    url = SVG_URL.format(user=username)
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.text


def parse_svg(svg_text: str):
    """Parse the GitHub contributions SVG.
    Returns a list of dicts sorted chronologically:
        {"date": datetime.date, "count": int, "color": "#rrggbb", "x": int, "y": int}
    """
    soup = BeautifulSoup(svg_text, "html.parser")
    rects = soup.select("rect[data-date]")
    contributions = []
    for r in rects:
        date_str = r["data-date"]
        count = int(r["data-count"])
        color = r["fill"]
        # GitHub positions the days in a grid: x = week number, y = day of week
        x = int(r["x"]) // (CELL_SIZE + CELL_PADDING)
        y = int(r["y"]) // (CELL_SIZE + CELL_PADDING)
        contributions.append({
            "date": dt.datetime.strptime(date_str, "%Y-%m-%d").date(),
            "count": count,
            "color": color,
            "x": x,
            "y": y,
        })
    contributions.sort(key=lambda d: d["date"])  # ensure order
    return contributions


def build_grid(contributions):
    """Create a 2‑D colour matrix that mirrors the GitHub heat‑map."""
    max_week = max(c["x"] for c in contributions)
    weeks = max_week + 1
    rows = 7
    grid = [[PALETTE["#ebedf0"] for _ in range(weeks)] for _ in range(rows)]
    for c in contributions:
        rgb = PALETTE.get(c["color"], PALETTE["#ebedf0"])
        grid[c["y"]][c["x"]] = rgb
    return grid


def get_snake_path(contributions):
    """Ordered list of (x, y) cells where count > 0 (the snake's route)."""
    return [(c["x"], c["y"]) for c in contributions if c["count"] > 0]


def draw_frame(grid, snake_coords, head_idx):
    rows = len(grid)
    cols = len(grid[0])
    width = cols * (CELL_SIZE + CELL_PADDING) - CELL_PADDING + IMG_BORDER * 2
    height = rows * (CELL_SIZE + CELL_PADDING) - CELL_PADDING + IMG_BORDER * 2
    im = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)

    # Draw heat‑map background
    for y in range(rows):
        for x in range(cols):
            cx = IMG_BORDER + x * (CELL_SIZE + CELL_PADDING)
            cy = IMG_BORDER + y * (CELL_SIZE + CELL_PADDING)
            draw.rectangle([cx, cy, cx + CELL_SIZE, cy + CELL_SIZE], fill=grid[y][x])

    # Draw snake body
    for i in range(head_idx):
        x, y = snake_coords[i]
        cx = IMG_BORDER + x * (CELL_SIZE + CELL_PADDING)
        cy = IMG_BORDER + y * (CELL_SIZE + CELL_PADDING)
        draw.rectangle([cx, cy, cx + CELL_SIZE, cy + CELL_SIZE], fill=SNAKE_BODY)

    # Draw snake head (if any)
    if head_idx < len(snake_coords):
        x, y = snake_coords[head_idx]
        cx = IMG_BORDER + x * (CELL_SIZE + CELL_PADDING)
        cy = IMG_BORDER + y * (CELL_SIZE + CELL_PADDING)
        draw.rectangle([cx, cy, cx + CELL_SIZE, cy + CELL_SIZE], fill=SNAKE_HEAD)
    return im


def make_gif(frames, out_path, fps=12, loop=0):
    duration = int(1000 / fps)
    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=loop,
        disposal=2,
        transparency=0,
    )
    print(f"✅ GIF saved to {out_path}")


def main():
    if len(sys.argv) < 2 or "--help" in sys.argv:
        print(__doc__)
        sys.exit(1)
    username = sys.argv[1]
    out_file = Path(sys.argv[2] if len(sys.argv) > 2 else "snake.gif")
    print(f"🔎 Downloading contribution SVG for user '{username}' …")
    svg = fetch_svg(username)
    contributions = parse_svg(svg)
    if not contributions:
        print("❌ No contribution data found – aborting.")
        sys.exit(1)
    grid = build_grid(contributions)
    snake_path = get_snake_path(contributions)
    if not snake_path:
        print("⚠️ User has no contribution days – nothing to animate.")
        sys.exit(0)
    frames = []
    total = len(snake_path)
    print(f"🎞️ Generating {total + 1} frames …")
    for head_idx in range(total):
        frames.append(draw_frame(grid, snake_path, head_idx))
    frames.append(draw_frame(grid, snake_path, total - 1))
    make_gif(frames, out_file, fps=12, loop=0)

if __name__ == "__main__":
    main()
