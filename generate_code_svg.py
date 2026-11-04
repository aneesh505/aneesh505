#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generate_code_svg.py
Generates an animated typing code-snippet SVG for a GitHub profile README.
"""

from pathlib import Path

SVG_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="680" height="420" viewBox="0 0 680 420" font-family="'SFMono-Regular','Consolas','Liberation Mono',monospace" font-size="14">
  <defs>
    <clipPath id="cl0"><rect x="26" y="52.0" height="21" width="0"><animate attributeName="width" dur="20s" repeatCount="indefinite" keyTimes="0;0.02;0.05;0.95;1" values="0;0;150;150;0"/></rect></clipPath>
    <clipPath id="cl1"><rect x="26" y="76.0" height="21" width="0"><animate attributeName="width" dur="20s" repeatCount="indefinite" keyTimes="0;0.06;0.10;0.95;1" values="0;0;220;220;0"/></rect></clipPath>
    <clipPath id="cl2"><rect x="26" y="100.0" height="21" width="0"><animate attributeName="width" dur="20s" repeatCount="indefinite" keyTimes="0;0.12;0.22;0.95;1" values="0;0;420;420;0"/></rect></clipPath>
    <clipPath id="cl3"><rect x="26" y="124.0" height="21" width="0"><animate attributeName="width" dur="20s" repeatCount="indefinite" keyTimes="0;0.24;0.34;0.95;1" values="0;0;450;450;0"/></rect></clipPath>
    <clipPath id="cl4"><rect x="26" y="148.0" height="21" width="0"><animate attributeName="width" dur="20s" repeatCount="indefinite" keyTimes="0;0.36;0.46;0.95;1" values="0;0;410;410;0"/></rect></clipPath>
    <clipPath id="cl5"><rect x="26" y="184.0" height="21" width="0"><animate attributeName="width" dur="20s" repeatCount="indefinite" keyTimes="0;0.48;0.52;0.95;1" values="0;0;200;200;0"/></rect></clipPath>
    <clipPath id="cl6"><rect x="26" y="208.0" height="21" width="0"><animate attributeName="width" dur="20s" repeatCount="indefinite" keyTimes="0;0.54;0.64;0.95;1" values="0;0;380;380;0"/></rect></clipPath>
    <clipPath id="cl7"><rect x="26" y="232.0" height="21" width="0"><animate attributeName="width" dur="20s" repeatCount="indefinite" keyTimes="0;0.66;0.76;0.95;1" values="0;0;440;440;0"/></rect></clipPath>
    <clipPath id="cl8"><rect x="26" y="256.0" height="21" width="0"><animate attributeName="width" dur="20s" repeatCount="indefinite" keyTimes="0;0.78;0.82;0.95;1" values="0;0;80;80;0"/></rect></clipPath>
    <clipPath id="cl9"><rect x="26" y="292.0" height="21" width="0"><animate attributeName="width" dur="20s" repeatCount="indefinite" keyTimes="0;0.84;0.88;0.95;1" values="0;0;240;240;0"/></rect></clipPath>
    <clipPath id="cl10"><rect x="26" y="316.0" height="21" width="0"><animate attributeName="width" dur="20s" repeatCount="indefinite" keyTimes="0;0.90;0.94;0.95;1" values="0;0;360;360;0"/></rect></clipPath>
  </defs>

  <!-- Window background -->
  <rect x="0.5" y="0.5" width="679" height="419" rx="12" fill="#0d1117" stroke="#21262d"/>
  <rect x="1" y="1" width="677" height="40" rx="11" fill="#161b22"/>
  <rect x="1" y="28" width="677" height="13" fill="#161b22"/>

  <!-- Window buttons -->
  <circle cx="24" cy="21" r="6" fill="#ff5f56"/>
  <circle cx="44" cy="21" r="6" fill="#ffbd2e"/>
  <circle cx="64" cy="21" r="6" fill="#27c93f"/>

  <!-- Title -->
  <text x="340" y="25" text-anchor="middle" font-size="12" fill="#8b949e" font-family="monospace">aneesh.py</text>
  <line x1="0" y1="41" x2="680" y2="41" stroke="#21262d"/>

  <!-- Code Lines -->
  <text x="26" y="68.0" clip-path="url(#cl0)" xml:space="preserve"><tspan fill="#ff7b72">class</tspan><tspan fill="#e6edf3"> </tspan><tspan fill="#79c0ff">AneeshSuvarna</tspan><tspan fill="#d2a8ff">:</tspan></text>
  <text x="26" y="92.0" clip-path="url(#cl1)" xml:space="preserve"><tspan fill="#e6edf3">    </tspan><tspan fill="#ff7b72">def</tspan><tspan fill="#e6edf3"> </tspan><tspan fill="#d2a8ff">__init__</tspan><tspan fill="#e6edf3">(</tspan><tspan fill="#ffa657">self</tspan><tspan fill="#e6edf3">):</tspan></text>
  <text x="26" y="116.0" clip-path="url(#cl2)" xml:space="preserve"><tspan fill="#e6edf3">        </tspan><tspan fill="#ffa657">self</tspan><tspan fill="#e6edf3">.</tspan><tspan fill="#79c0ff">role</tspan><tspan fill="#e6edf3"> = </tspan><tspan fill="#a5d6ff">"Full-Stack Web Developer"</tspan></text>
  <text x="26" y="140.0" clip-path="url(#cl3)" xml:space="preserve"><tspan fill="#e6edf3">        </tspan><tspan fill="#ffa657">self</tspan><tspan fill="#e6edf3">.</tspan><tspan fill="#79c0ff">location</tspan><tspan fill="#e6edf3"> = </tspan><tspan fill="#a5d6ff">"India"</tspan></text>
  <text x="26" y="164.0" clip-path="url(#cl4)" xml:space="preserve"><tspan fill="#e6edf3">        </tspan><tspan fill="#ffa657">self</tspan><tspan fill="#e6edf3">.</tspan><tspan fill="#79c0ff">focus</tspan><tspan fill="#e6edf3"> = </tspan><tspan fill="#a5d6ff">"React, Node.js, Open Source"</tspan></text>

  <text x="26" y="200.0" clip-path="url(#cl5)" xml:space="preserve"><tspan fill="#e6edf3">    </tspan><tspan fill="#ff7b72">def</tspan><tspan fill="#e6edf3"> </tspan><tspan fill="#d2a8ff">get_skills</tspan><tspan fill="#e6edf3">(</tspan><tspan fill="#ffa657">self</tspan><tspan fill="#e6edf3">):</tspan></text>
  <text x="26" y="224.0" clip-path="url(#cl6)" xml:space="preserve"><tspan fill="#e6edf3">        </tspan><tspan fill="#ff7b72">return</tspan><tspan fill="#e6edf3"> [</tspan><tspan fill="#a5d6ff">"JavaScript"</tspan><tspan fill="#e6edf3">, </tspan><tspan fill="#a5d6ff">"Python"</tspan><tspan fill="#e6edf3">, </tspan><tspan fill="#a5d6ff">"HTML/CSS"</tspan><tspan fill="#e6edf3">, </tspan><tspan fill="#a5d6ff">"Git"</tspan><tspan fill="#e6edf3">]</tspan></text>
  <text x="26" y="248.0" clip-path="url(#cl7)" xml:space="preserve"><tspan fill="#e6edf3">        </tspan><tspan fill="#ff7b72">return</tspan><tspan fill="#e6edf3"> [</tspan><tspan fill="#a5d6ff">"React"</tspan><tspan fill="#e6edf3">, </tspan><tspan fill="#a5d6ff">"Node.js"</tspan><tspan fill="#e6edf3">, </tspan><tspan fill="#a5d6ff">"Namamit"</tspan><tspan fill="#e6edf3">]</tspan></text>
  <text x="26" y="272.0" clip-path="url(#cl8)" xml:space="preserve"><tspan fill="#e6edf3">        </tspan><tspan fill="#8b949e"># ...</tspan></text>

  <text x="26" y="308.0" clip-path="url(#cl9)" xml:space="preserve"><tspan fill="#e6edf3">    </tspan><tspan fill="#ff7b72">def</tspan><tspan fill="#e6edf3"> </tspan><tspan fill="#d2a8ff">status</tspan><tspan fill="#e6edf3">(</tspan><tspan fill="#ffa657">self</tspan><tspan fill="#e6edf3">):</tspan></text>
  <text x="26" y="332.0" clip-path="url(#cl10)" xml:space="preserve"><tspan fill="#e6edf3">        </tspan><tspan fill="#ff7b72">return</tspan><tspan fill="#e6edf3"> </tspan><tspan fill="#a5d6ff">"Always building &amp; shipping 🚀"</tspan></text>

  <!-- Blinking Cursor -->
  <rect x="26" y="53.0" width="8" height="16" fill="#79c0ff">
    <animate attributeName="x" dur="20s" repeatCount="indefinite" calcMode="discrete"
             keyTimes="0;0.02;0.05;0.06;0.10;0.12;0.22;0.24;0.34;0.36;0.46;0.48;0.52;0.54;0.64;0.66;0.76;0.78;0.82;0.84;0.88;0.90;0.94;0.95;1"
             values="26;26;170;26;246;26;446;26;476;26;436;26;226;26;406;26;466;26;106;26;266;26;386;26;26"/>
    <animate attributeName="y" dur="20s" repeatCount="indefinite" calcMode="discrete"
             keyTimes="0;0.02;0.05;0.06;0.10;0.12;0.22;0.24;0.34;0.36;0.46;0.48;0.52;0.54;0.64;0.66;0.76;0.78;0.82;0.84;0.88;0.90;0.94;0.95;1"
             values="53;53;53;77;77;101;101;125;125;149;149;185;185;209;209;233;233;257;257;293;293;317;317;53;53"/>
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1s" repeatCount="indefinite"/>
  </rect>
</svg>
"""

def main():
    out_path = Path("aneesh_intro.svg")
    out_path.write_text(SVG_TEMPLATE, encoding="utf-8")
    print(f"Successfully generated {out_path.absolute()}")

if __name__ == "__main__":
    main()
