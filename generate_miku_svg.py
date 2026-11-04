#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generate_miku_svg.py
Generates a custom animated SVG featuring Hatsune Miku dancing / waving
with a gradient theme, perfectly styled for a GitHub profile README.
"""

from pathlib import Path

MIKU_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="564" height="676" viewBox="0 0 564 676" font-family="'SFMono-Regular','Consolas','Liberation Mono',monospace">
  <defs>
    <linearGradient id="mikuGrad" x1="0%" y1="0%" x2="100%" y2="100%" gradientTransform="rotate(0 .5 .5)">
      <stop offset="0%"  stop-color="#39c5bb"/>
      <stop offset="50%" stop-color="#008b8b"/>
      <stop offset="100%" stop-color="#20b2aa"/>
      <animateTransform attributeName="gradientTransform" type="rotate"
        from="0 .5 .5" to="360 .5 .5" dur="16s" repeatCount="indefinite"/>
    </linearGradient>
    <clipPath id="typeMiku">
      <rect x="130" y="629.4" height="29" width="0">
        <animate attributeName="width" dur="4.5s" repeatCount="indefinite"
          keyTimes="0;0.45;0.9;1" values="0;310;310;0"/>
      </rect>
    </clipPath>
    <style>
      .mono { font-size:11px; font-weight:600; fill:url(#mikuGrad); white-space:pre; }
      #mikuFace { animation: mikuBob 3s ease-in-out infinite; transform-origin: center; }
      @keyframes mikuBob { 0%,100% { transform: translateY(0px); } 50% { transform: translateY(-4px); } }
      #cursor { animation: blink 1s steps(1) infinite; }
      @keyframes blink { 0%,50% {opacity:1} 50.1%,100% {opacity:0} }
      .name { font-size:20px; font-weight:700; fill:url(#mikuGrad); letter-spacing:1px; }
    </style>
  </defs>
  <rect width="100%" height="100%" fill="#0d1117" rx="14"/>

  <!-- Hatsune Miku ASCII Art with Teal/Cyan Gradient & Floating Bob Animation -->
  <g id="mikuFace">
    <text class="mono" xml:space="preserve">
<tspan x="45" y="40">                 .,,,;;;:::;,,,,,.</tspan>
<tspan x="45" y="55">             .':;+++++*++*++***+++++;:,.</tspan>
<tspan x="45" y="70">          .,;++**#%@@@@@@@@@@@@@@@@%#***++;,</tspan>
<tspan x="45" y="85">        .,++*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**+.</tspan>
<tspan x="45" y="100">      .,+*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*+.</tspan>
<tspan x="45" y="115">     ,+*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*+,  ♪</tspan>
<tspan x="45" y="130">    :+*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*+:</tspan>
<tspan x="45" y="145">   ;+*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*+;</tspan>
<tspan x="45" y="160">  :+*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*+:</tspan>
<tspan x="45" y="175">  +*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*+</tspan>
<tspan x="45" y="190"> ;*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*;</tspan>
<tspan x="45" y="205"> +#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+</tspan>
<tspan x="45" y="220">+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+</tspan>
<tspan x="45" y="235">#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#</tspan>
<tspan x="45" y="250">#@@@@@@@@@@@@@@@@@@@@@@*+=---=+*@@@@@@@@@@@@@@@@@@@@@@@@@#</tspan>
<tspan x="45" y="265">#@@@@@@@@@@@@@@@@@*=-          -=*@@@@@@@@@@@@@@@@@@@@@@@#</tspan>
<tspan x="45" y="280">#@@@@@@@@@@@@@@=--   (o)    (o)   --=@@@@@@@@@@@@@@@@@@@@#</tspan>
<tspan x="45" y="295">@@@@@@@@@@@@@@=--      ____      --=@@@@@@@@@@@@@@@@@@@@</tspan>
<tspan x="45" y="310">@@@@@@@@@@@@@@@+=--   \____/   ---=+@@@@@@@@@@@@@@@@@@@@</tspan>
<tspan x="45" y="325">@@@@@@@@@@@@@@@@@*+=---    ---=+*@@@@@@@@@@@@@@@@@@@@@@@</tspan>
<tspan x="45" y="340">@@@@@@@@@@@@@@@@@@@@@%#****#%@@@@@@@@@@@@@@@@@@@@@@@@@@@</tspan>
<tspan x="45" y="355">@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@</tspan>
<tspan x="45" y="370">@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@</tspan>
<tspan x="45" y="385">@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@</tspan>
<tspan x="45" y="400">@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@</tspan>
<tspan x="45" y="415"> %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%</tspan>
<tspan x="45" y="430">  %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%</tspan>
<tspan x="45" y="445">   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#</tspan>
<tspan x="45" y="460">    *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*  ♫</tspan>
<tspan x="45" y="475">     +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+</tspan>
<tspan x="45" y="490">      -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-</tspan>
<tspan x="45" y="505">        -%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-</tspan>
    </text>
  </g>

  <!-- Divider line & typed text terminal footer -->
  <line x1="100" y1="620" x2="464" y2="620" stroke="url(#mikuGrad)" stroke-width="1.5" opacity="0.4"/>
  <g clip-path="url(#typeMiku)">
    <text class="name" x="130" y="650.4" xml:space="preserve">&gt; ♪ Hatsune Miku // Vocaloid 01</text>
  </g>
  <rect id="cursor" x="445" y="632.4" width="10" height="20" fill="#39c5bb"/>
</svg>
"""

def main():
    out_path = Path("miku_animation.svg")
    out_path.write_text(MIKU_SVG, encoding="utf-8")
    print(f"Successfully generated {out_path.absolute()}")

if __name__ == "__main__":
    main()
