#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generate_miku_svg.py
Keeps the upper body formatting intact, but gently shifts the lower leg/feet lines
to the center so the entire figure is balanced.
"""

from pathlib import Path

MIKU_ART = [
    "                     ⢠⠦⣄⣠⠴⠒⠒⠉⠒⠶⣄⡏⣶",
    "                     ⢸⣠⡞⣡⠀⢠⡀⠀⢦⡀⢹⣷⣼⣄",
    "                     ⣸⡿⠁⣿⠟⣷⣿⢦⡈⣇⠀⢻⣿⣈⢷⡄",
    "                    ⢠⣿⡇⣶⣻⣀⠘⣿⣀⣹⣿⣰⣼⡟⣯⠟⣿⡄",
    "                    ⢸⣿⡇⣿⡿⠿⠋⠉⠋⠛⢿⣿⣿⡇⠈⢦⡸⣾⣆",
    "                    ⢸⣿⡇⠛⣷⣄⠀⠀⠀⠀⣸⠟⠃⠉⠀⠈⢷⣩⡻⣄",
    "                    ⢸⣿⠹⡄⠈⠙⠒⢤⣴⣾⠉⠁⣀⡀⠀⠀⠀⠹⣟⢮⡳⣄",
    "                    ⣼⣿⠀⣿⠀⣀⣴⣿⡏⣀⡬⠟⠁⠈⣆⠀⠀⠀⠘⢧⡉⢿⣧⡀",
    "                  ⢠⡿⣿⠀⢻⣫⠉⣽⡟⠉⡅⢀⣆⠀⢠⣿⠀⠀⠀⠀⠀⠹⣦⡉⠻⢦⡀⡄",
    "                  ⣸⢗⣿⢀⡷⠁⣸⡿⠁⠀⠀⢸⣿⠃⣄⣈⡆⠀⠀⠀⠀⠀⠈⠫⣱⠦⣌⡓⢤⣀",
    "                ⢰⣇⣾⣿⢟⡇⢀⣿⡇⠀⢀⣰⢸⡌⢿⣿⢻⡟⣃⠀⠀⠀⠰⡂⠠⠌⠲⢤⣙⣻⠛⠓⠶⢦⡤⣄⣀⡀",
    "              ⣠⣿⣻⣿⠏⣾⠃⢸⢽⡇⠀⡏⠁⡶⠁⠈⣿⣎⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠒⠶⢤⣀⠈⠻⣄",
    "            ⢠⣴⣿⠟⠁⡼⠀⣿⠀⡟⢸⡇⢰⠃⢸⠇⠀⠀⢹⣷⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⣄⠘⣧",
    "          ⢀⣀⣤⣾⠟⠋⠀⣠⡼⢁⣼⣿⢠⣧⢾⡇⠘⡀⠸⡇⠀⠀⠘⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡉⠚⢧⠹⣷",
    "  ⢀⣠⡴⠖⢋⣽⡿⠥⠖⠚⠉⢁⣴⣾⣿⠃⢈⠀⢸⠇⠀⠁⠀⢳⡀⠀⠀⣿⣿⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡇",
    "⣀⣤⣾⠛⠁⣠⡼⠋⠁⠀⢀⣀⢀⣴⣿⣿⠟⠁⠀⠀⣷⠋⠂⠀⠀⠀⠀⠳⡀⠀⢹⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⢸⠧",
    "⢀⡠⠖⠋⣩⠶⢋⡴⠋⠁⠀⠀⠿⣭⡿⣿⠿⠟⢉⣷⣄⠀⢀⣼⣿⡄⠀⠀⠀⠀⠀⢀⣹⠄⠀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠐⡧",
    "⣸⣄⣴⣛⣡⠞⠋⠀⠀⠀⠀⠀⠀⠀⣭⣤⣴⣾⣿⣿⣿⣷⣿⣿⣿⣷⣤⣴⣶⣾⣿⣿⣿⣆⠀⢈⣿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢑",
    "⠰⣏⡿⢫⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣹⠿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⢀",
    "⢀⣿⡵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⢀⡜⠀⠀⠀⠀⠀⠀⢀⠎",
    "⢠⢸⡟⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡧⠤⢙⠛⠋⠛⠛⠿⠿⢿⡟⠛⠉⠁⠀⠀⠀⠀⠀⠠⠐⠀⠀⠀⠀⠀⠀⠀⢀⡼⢀⠀⠄⠀⠀⡀⡀⠀⠀",
    "⢸⣎⡇⠀⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⡀⢰⡅⠀⠀⠀⠀⠀⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⢋⠞⠀⣮⠎⠀⠀⠀",
    "⢿⣷⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣶⣿⣇⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⣠⠋⣴⠟⠁⠀⠀⠀⠀",
    "⠘⣏⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⢹⣻⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢡⠞⣁⣴⠟⠁⠀⠀⠀⠀⠀⠀",
    "⠸⡄⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⢄⡀⠀⠀⠘⣿⣿⣿⯯⢶⢧⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⢁⣴⠿⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠹⡄⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⣄⠈⢿⣿⣿⯯⣝⣾⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡯⢖⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠹⡄⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣽⣿⡇⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⢴⣶⠿⠋⠁⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠘⢦⡀⠀⠙⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣻⢿⣿⡍⠑⠒⠒⣒⣾⣷⠿⠛⣋⡵⠚⠁⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠙⠢⣄⡀⠀⠙⠓⠒⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣷⡚⠛⠉⠁⠀⠀⠐⠋⢀⡀⢀⡤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠉⠉⠙⠋⠛⠛⣹⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    # Legs / bottom lines shifted slightly right for center alignment
    "                       ⣿⣿⣿⣻⣿⣿⣿⣿⣇",
    "                       ⣿⣿⣿⣿⢿⣿⣿⣿",
    "                     ⢀⣿⣿⣿⡏⠸⣿⣿⣿",
    "                     ⢸⣿⣿⣿⠁⠀⢹⣿⣿⡄",
    "                     ⢸⣿⣿⡏⠀⠀⠈⣿⣿⡆",
    "                     ⢸⣿⣿⠀⠀⠀⠀⢼⣿⣷⡀",
    "                     ⣼⣿⣿⠀⠀⠀⠀⣼⣿⣿⡇",
    "                   ⠰⣿⣿⣿⠀⠀⠀⢀⣿⣿⣿⡇",
    "                     ⣿⣿⣿⡆⠀⠀⣾⣿⣿⣿⣧",
    "                   ⢰⣿⣿⣿⣷⠀⠀⠸⣿⣿⣿⠟",
    "                   ⣾⣿⣿⣿⣻⡇⠀⠀⠈⠋⠉",
    "                   ⢹⣿⣿⣟⠟",
    "                   ⠘⣿⣿⣿⣯",
    "                   ⠀⠙⢿⣿⣿⡀"
]

def generate_svg():
    lines_svg = []
    y_start = 22
    for i, line in enumerate(MIKU_ART):
        # Upper body lines (0 to 29) left-aligned at x="35", lower legs (30+) shifted right for centering
        x_pos = 50 if i >= 30 else 35
        safe_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        lines_svg.append(f'    <text x="{x_pos}" y="{y_start}" class="mono" xml:space="preserve">{safe_line}</text>')
        y_start += 14.0

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="530" height="676" viewBox="0 0 530 676" font-family="'SFMono-Regular','Consolas','Liberation Mono',monospace">
  <defs>
    <linearGradient id="mikuGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"  stop-color="#39c5bb"/>
      <stop offset="50%" stop-color="#008b8b"/>
      <stop offset="100%" stop-color="#20b2aa"/>
      <animateTransform attributeName="gradientTransform" type="rotate"
        from="0 .5 .5" to="360 .5 .5" dur="16s" repeatCount="indefinite"/>
    </linearGradient>
    <style>
      .mono {{ font-size:9.0px; font-weight:600; fill:url(#mikuGrad); white-space:pre; }}
      #mikuContainer {{ animation: mikuBob 3s ease-in-out infinite; transform-origin: center; }}
      @keyframes mikuBob {{ 0%,100% {{ transform: translateY(0px); }} 50% {{ transform: translateY(-4px); }} }}
    </style>
  </defs>
  <rect width="100%" height="100%" fill="#0d1117" rx="14"/>

  <g id="mikuContainer">
{'\n'.join(lines_svg)}
  </g>

  <rect x="0.75" y="0.75" width="528.5" height="674.5" rx="13" fill="none" stroke="#39c5bb" stroke-opacity="0.3" stroke-width="1.5"/>
</svg>
"""
    return svg_content

def main():
    out_path = Path("miku_animation.svg")
    out_path.write_text(generate_svg(), encoding="utf-8")
    print(f"Successfully generated clean Miku SVG at {out_path.absolute()}")

if __name__ == "__main__":
    main()
