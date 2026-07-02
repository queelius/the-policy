#!/usr/bin/env python3
"""Cover art for the collection *Is It Kind?* as a TikZ standalone.

Companion variation to the novel's cover (one Monte Carlo search tree, one bright
surviving path). Here: a row of small, varied sprigs along the lower third, one
per story, each a slighter offshoot of the same tree. Reads as a matched set on
a shelf with the novel: same austere near-black field, same EB Garamond, same
line-work, but plural and lighter. One sprig carries the bright surviving path.

Usage: python3 gen_cover_collection.py <mode> <out.tex>   mode in {paperback, ebook}
Deterministic (fixed seed).
"""
import math, random, sys

MODE = sys.argv[1] if len(sys.argv) > 1 else "paperback"
OUT = sys.argv[2] if len(sys.argv) > 2 else "cover-collection.tex"

if MODE == "paperback":
    W, H = 6.25, 9.25
    TITLE_SIZE, TITLE_LS = 30, 8
    SUB_SIZE, SUB_LS = 12, 14
    AUTH_SIZE, AUTH_LS = 13.5, 18
else:  # ebook 1600x2560 @ 300dpi
    W, H = 1600/300.0, 2560/300.0
    TITLE_SIZE, TITLE_LS = 28, 7
    SUB_SIZE, SUB_LS = 11, 12
    AUTH_SIZE, AUTH_LS = 12.5, 16

CX = W/2.0
FONT = "/usr/share/fonts/truetype/ebgaramond/"
random.seed(74)  # Day 74, the day the question was asked

N_SPRIGS = 11          # one per story
BASE_Y = 1.05
SPRIG_MAX_DEPTH = 6
CANOPY_CAP = H*0.46    # sprigs stay in the lower field, clear of the title

segments = []  # (x1,y1,x2,y2,depth,bright)
leaves = []    # (x,y,bright)

def grow(x, y, ang, length, depth, bright, spine):
    if depth > SPRIG_MAX_DEPTH or length < 0.05:
        leaves.append((x, y, bright and spine))
        return
    a = math.radians(ang)
    nx, ny = x + length*math.cos(a), y + length*math.sin(a)
    if ny > CANOPY_CAP: ny = CANOPY_CAP
    segments.append((x, y, nx, ny, depth, bright and spine))
    k = 1 if random.random() < 0.25 else 2
    spread = 26*(1 - depth/(SPRIG_MAX_DEPTH+3)) + 7
    spine_child = random.randrange(k) if spine else -1
    if k == 1:
        offs = [random.uniform(-7, 7)]
    else:
        offs = [(-0.5 + i/(k-1))*2*spread + random.uniform(-4, 4) for i in range(k)]
    for i, o in enumerate(offs):
        grow(nx, ny, ang+o, length*0.72*random.uniform(0.9, 1.05), depth+1,
             bright, spine and i == spine_child)

# lay the sprigs across the width; one (near center-left) is the bright one
positions = [ (i+0.5)/N_SPRIGS for i in range(N_SPRIGS) ]
bright_idx = 4
for i, fx in enumerate(positions):
    x0 = 0.5 + fx*(W-1.0)
    h0 = random.uniform(0.85, 1.35) * (1.15 if i == bright_idx else 1.0)
    grow(x0, BASE_Y, 90 + random.uniform(-6, 6), h0, 0,
         bright=(i == bright_idx), spine=True)

out = []
out.append(r"\documentclass[border=0pt]{standalone}")
out.append(r"\usepackage{tikz}\usepackage{fontspec}")
out.append(r"\definecolor{field}{RGB}{5,7,12}")
out.append(r"\newfontfamily\coverface{EBGaramond12-Regular}[Path="+FONT+
           r", Extension=.ttf, ItalicFont=EBGaramond12-Italic]")
out.append(r"\begin{document}\begin{tikzpicture}[x=1in,y=1in,line cap=round]")
out.append(rf"  \useasboundingbox (0,0) rectangle ({W:.3f},{H:.3f});")
out.append(rf"  \clip (0,0) rectangle ({W:.3f},{H:.3f});")
out.append(rf"  \fill[field] (0,0) rectangle ({W:.3f},{H:.3f});")
# faint ground line the sprigs stand on
out.append(rf"  \draw[white!7,line width=0.3pt] (0.5,{BASE_Y:.3f}) -- ({W-0.5:.3f},{BASE_Y:.3f});")
# faint branches
for (x1,y1,x2,y2,d,br) in segments:
    if br: continue
    mix = 9 + max(0, 5 - d)*2
    out.append(rf"  \draw[white!{mix},line width=0.3pt] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});")
for (x,y,br) in leaves:
    if br: continue
    out.append(rf"  \fill[white!12] ({x:.3f},{y:.3f}) circle (0.007);")
# the one bright sprig
for (x1,y1,x2,y2,d,br) in segments:
    if not br: continue
    out.append(rf"  \draw[white!90,line width={max(0.5,1.2-0.09*d):.2f}pt] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});")
for (x,y,br) in leaves:
    if br:
        out.append(rf"  \fill[white!95] ({x:.3f},{y:.3f}) circle (0.02);")
# roots (dots at each sprig base)
for i, fx in enumerate(positions):
    x0 = 0.5 + fx*(W-1.0)
    m = 70 if i == bright_idx else 34
    out.append(rf"  \fill[white!{m}] ({x0:.3f},{BASE_Y:.3f}) circle (0.015);")
# title / subtitle / author
ty = H - 1.5
out.append(rf"  \node[text=white!95,align=center] at ({CX:.3f},{ty:.3f}) "
           rf"{{{{\coverface\addfontfeature{{LetterSpace={TITLE_LS}}}\fontsize{{{TITLE_SIZE}}}{{{TITLE_SIZE+4}}}\selectfont IS IT KIND?}}}};")
out.append(rf"  \draw[white!38,line width=0.4pt] ({CX-1.05:.3f},{ty-0.42:.3f}) -- ({CX+1.05:.3f},{ty-0.42:.3f});")
out.append(rf"  \node[text=white!70,align=center] at ({CX:.3f},{ty-0.78:.3f}) "
           rf"{{{{\coverface\itshape\fontsize{{{SUB_SIZE}}}{{{SUB_SIZE+2}}}\selectfont Stories from The Policy}}}};")
out.append(rf"  \node[text=white!84,align=center] at ({CX:.3f},0.62) "
           rf"{{{{\coverface\addfontfeature{{LetterSpace={AUTH_LS}}}\fontsize{{{AUTH_SIZE}}}{{{AUTH_SIZE+3}}}\selectfont ALEX TOWELL}}}};")
out.append(r"\end{tikzpicture}\end{document}")
open(OUT,"w").write("\n".join(out)+"\n")
print(f"wrote {OUT} ({MODE}, {W}x{H}, {len(segments)} segs, {N_SPRIGS} sprigs)")
