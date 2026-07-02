#!/usr/bin/env python3
"""Generate The Policy cover art as a TikZ standalone document.

Motif: a Monte Carlo search tree branching upward from one root. Most branches
are faint (pruned); a single high-visit path survives bright. The canopy of
surviving leaves forms an implied visit distribution: "The Policy" is that
distribution. Austere white line-work on a near-black field, EB Garamond,
matching the-unbegotten's procedural cover method.

Usage: python3 gen_cover.py <mode>  where mode in {paperback, ebook}
Deterministic (fixed seed) so the art is reproducible.
"""
import math
import random
import sys

MODE = sys.argv[1] if len(sys.argv) > 1 else "paperback"

# Canvas in inches. Paperback = 6x9 trim + 0.125 bleed all around.
# Ebook = 1600x2560 px at 300 dpi = 5.3333 x 8.5333 in (1.6:1).
if MODE == "paperback":
    W, H = 6.25, 9.25
    TITLE_SIZE, TITLE_LS = 33, 10
    AUTH_SIZE, AUTH_LS = 14, 18
elif MODE == "ebook":
    W, H = 1600 / 300.0, 2560 / 300.0
    TITLE_SIZE, TITLE_LS = 31, 9
    AUTH_SIZE, AUTH_LS = 13, 16
else:
    raise SystemExit("mode must be paperback or ebook")

CX = W / 2.0
FONT = "/usr/share/fonts/truetype/ebgaramond/"

random.seed(31)  # 31 = the MINERVA hour-36 toll; a private joke, harmless

# --- Tree geometry --------------------------------------------------------
# Root sits low; the tree grows up into the dark. Title sits above the canopy.
ROOT_Y = 1.25
ROOT_LEN = H * 0.15          # first branch length, scales with canvas height
DECAY = 0.76                 # length shrink per generation
MAX_DEPTH = 9
CANOPY_CAP = H - 2.35        # keep branches clear of the title band

segments = []  # (x1,y1,x2,y2,depth,visit) visit in [0,1]
leaves = []    # (x,y,visit)

def grow(x, y, angle_deg, length, depth, on_spine, spine_choices):
    """Recursively emit branch segments. on_spine marks the surviving path."""
    if depth > MAX_DEPTH:
        leaves.append((x, y, 1.0 if on_spine else random.uniform(0.0, 0.25)))
        return
    a = math.radians(angle_deg)
    nx = x + length * math.cos(a)
    ny = y + length * math.sin(a)
    if ny > CANOPY_CAP:
        ny = CANOPY_CAP
    # visit weight: the spine is heavily visited; everything else is faint,
    # decaying with depth (deeper = more speculative = less visited).
    if on_spine:
        visit = 1.0
    else:
        visit = max(0.0, random.uniform(0.05, 0.42) * (1.0 - depth / (MAX_DEPTH + 3)))
    segments.append((x, y, nx, ny, depth, visit))

    # number of children: mostly 2, sometimes 3, occasionally 1 (a pruned line
    # that runs on alone). Spread narrows with depth.
    r = random.random()
    k = 1 if r < 0.12 else (3 if r > 0.72 else 2)
    spread = 30 * (1.0 - depth / (MAX_DEPTH + 4)) + 8
    # pick which child continues the bright spine
    spine_child = random.randrange(k) if on_spine else -1
    # symmetric-ish angle offsets around the current heading
    if k == 1:
        offsets = [random.uniform(-6, 6)]
    else:
        base = [(-0.5 + i / (k - 1)) for i in range(k)]  # -0.5..0.5
        offsets = [b * 2 * spread + random.uniform(-5, 5) for b in base]
    for i, off in enumerate(offsets):
        child_angle = angle_deg + off
        child_len = length * DECAY * random.uniform(0.9, 1.06)
        grow(nx, ny, child_angle, child_len, depth + 1,
             on_spine and i == spine_child, spine_choices)

grow(CX, ROOT_Y, 90 + random.uniform(-3, 3), ROOT_LEN, 0, True, None)

# --- Emit TikZ ------------------------------------------------------------
def whiten(visit, lo, hi):
    """Map visit weight to a white!X mix percentage in [lo,hi]."""
    return lo + (hi - lo) * max(0.0, min(1.0, visit))

out = []
out.append(r"\documentclass[border=0pt]{standalone}")
out.append(r"\usepackage{tikz}")
out.append(r"\usepackage{fontspec}")
out.append(r"\definecolor{field}{RGB}{5,7,12}")   # near-black, faint cool cast
out.append(r"\newfontfamily\coverface{EBGaramond12-Regular}"
           r"[Path=" + FONT + r", Extension=.ttf, "
           r"ItalicFont=EBGaramond12-Italic]")
out.append(r"\begin{document}")
out.append(r"\begin{tikzpicture}[x=1in,y=1in,line cap=round]")
# pin the bounding box to the canvas and clip, so overscanned contours/text
# do not enlarge the standalone crop box.
out.append(rf"  \useasboundingbox (0,0) rectangle ({W:.3f},{H:.3f});")
out.append(rf"  \clip (0,0) rectangle ({W:.3f},{H:.3f});")
out.append(rf"  \fill[field] (0,0) rectangle ({W:.3f},{H:.3f});")

# faint substrate: a dim halo behind the canopy (the space of futures the
# search spreads into), echoing the unbegotten contour motif. Centered in the
# canopy region rather than the root, so it reads as an aura, not a target.
halo_cy = CANOPY_CAP - 1.15
for s in [1.5, 2.4, 3.4]:
    out.append(
        rf"  \draw[white!5,line width=0.3pt] ({CX:.3f},{halo_cy:.3f}) "
        rf"ellipse [x radius={s:.2f}, y radius={s*0.92:.2f}];")

# branches, faint first (drawn under), spine last (drawn over)
faint = [s for s in segments if s[5] < 0.9]
spine = [s for s in segments if s[5] >= 0.9]
for (x1, y1, x2, y2, depth, visit) in faint:
    mix = whiten(visit, 6, 34)
    lw = 0.25 + 0.5 * visit
    out.append(
        rf"  \draw[white!{mix:.0f},line width={lw:.2f}pt] "
        rf"({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});")
# terminal points of faint leaves: a scattered canopy (the distribution)
for (x, y, visit) in leaves:
    if visit < 0.9:
        mix = whiten(visit, 8, 30)
        rr = 0.006 + 0.012 * visit
        out.append(rf"  \fill[white!{mix:.0f}] ({x:.3f},{y:.3f}) circle ({rr:.3f});")
# the surviving policy: bright spine over everything. A faint wide underlay
# gives it a subtle glow so the chosen path reads through the canopy.
for (x1, y1, x2, y2, depth, visit) in spine:
    out.append(
        rf"  \draw[white!12,line width=2.6pt] "
        rf"({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});")
for (x1, y1, x2, y2, depth, visit) in spine:
    lw = 1.5 - 0.08 * depth
    out.append(
        rf"  \draw[white!92,line width={max(0.6,lw):.2f}pt] "
        rf"({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});")
# a bright node where the spine terminates (the chosen action)
if spine:
    tx, ty = spine[-1][2], spine[-1][3]
    out.append(rf"  \fill[white!96] ({tx:.3f},{ty:.3f}) circle (0.03);")
    out.append(rf"  \draw[white!40,line width=0.4pt] ({tx:.3f},{ty:.3f}) circle (0.07);")
# the root: a single point at the base (the present state)
out.append(rf"  \fill[white!70] ({CX:.3f},{ROOT_Y:.3f}) circle (0.022);")

# title
ty_title = H - 1.15
ty_rule = ty_title - 0.42
out.append(
    rf"  \node[text=white!95,align=center] at ({CX:.3f},{ty_title:.3f}) "
    rf"{{{{\coverface\addfontfeature{{LetterSpace={TITLE_LS}}}"
    rf"\fontsize{{{TITLE_SIZE}}}{{{TITLE_SIZE+4}}}\selectfont THE POLICY}}}};")
out.append(
    rf"  \draw[white!40,line width=0.4pt] "
    rf"({CX-1.05:.3f},{ty_rule:.3f}) -- ({CX+1.05:.3f},{ty_rule:.3f});")
out.append(
    rf"  \node[text=white!62,align=center] at ({CX:.3f},{ty_rule-0.30:.3f}) "
    rf"{{{{\coverface\addfontfeature{{LetterSpace=22}}"
    rf"\fontsize{{11}}{{13}}\selectfont A NOVEL}}}};")
# author
out.append(
    rf"  \node[text=white!84,align=center] at ({CX:.3f},0.85) "
    rf"{{{{\coverface\addfontfeature{{LetterSpace={AUTH_LS}}}"
    rf"\fontsize{{{AUTH_SIZE}}}{{{AUTH_SIZE+3}}}\selectfont ALEX TOWELL}}}};")

out.append(r"\end{tikzpicture}")
out.append(r"\end{document}")

with open(sys.argv[2], "w") as f:
    f.write("\n".join(out) + "\n")
print(f"wrote {sys.argv[2]} ({MODE}, {W}x{H}in, {len(segments)} segments)")
