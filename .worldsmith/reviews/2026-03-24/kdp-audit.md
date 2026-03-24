# KDP Audit Report: *The Policy*

**Date:** 2026-03-24
**Auditor:** Claude Opus 4.6
**Manuscript:** The Policy (novel)
**Word count:** ~91,000
**Page count:** 365 (screen PDF) / 365 (print 6x9 PDF)
**Target formats:** Kindle eBook (EPUB/KPF) + 6x9 trade paperback
**Build pipeline:** `kdp/build.sh` (LaTeX -> print PDF + EPUB)

---

## Executive Summary

The manuscript is **substantially ready for KDP submission.** The build pipeline, interior formatting, metadata, and content are all publication-quality. The print-ready 6x9 PDF uses proper margins, professional typography (EB Garamond), and standard trade paperback specs. The EPUB uses a clean Lua filter for math fallbacks and a professional Kindle CSS.

**Three blocking items** prevent immediate submission:
1. No full-wrap paperback cover (front + spine + back)
2. Author name missing from screen-version title page
3. Copyright page needs publisher/imprint line

**Everything else passes.** The audit found 26 overfull hbox warnings in the print PDF (all from verbatim/listing environments, fixable), but no margin violations, no structural issues, and no metadata gaps that would cause KDP rejection.

---

## Detailed Findings

### A. MANUSCRIPT FORMAT

| Requirement | eBook | Paperback | Notes |
|-------------|-------|-----------|-------|
| File format | PASS (EPUB3) | PASS (PDF, 6x9) | EPUB generated via pandoc; PDF via pdflatex |
| File size | PASS (270 KB) | PASS (902 KB) | Well under KDP limits |
| Page count | N/A | PASS (365 pp) | Within KDP range (24-828 for 6x9) |
| Fonts embedded | PASS | PASS (EB Garamond) | Screen version uses Latin Modern; print uses EB Garamond |
| Images | N/A | N/A | No interior images (text-only novel) |
| MathML | PASS | N/A | EPUB uses MathML with Lua fallbacks for complex expressions |

### B. PAGE GEOMETRY (Paperback)

| Parameter | Current | KDP Minimum | Verdict |
|-----------|---------|-------------|---------|
| Trim size | 6" x 9" | Supported | PASS |
| Inside (gutter) margin | 0.85" | 0.75" (for 365pp) | PASS |
| Outside margin | 0.60" | 0.25" | PASS |
| Top margin | 0.70" | 0.25" | PASS |
| Bottom margin | 0.70" | 0.25" | PASS |
| Bleed | None | Not required (no full-bleed images) | PASS |
| Paper type | White (assumed) | White or cream | PASS |

**Spine width calculation:** 365 pages x 0.002252"/page (white paper) = **0.822" spine**

### C. TYPOGRAPHY (Paperback)

| Parameter | Setting | Assessment |
|-----------|---------|------------|
| Body font | EB Garamond 11pt | PASS -- professional serif, excellent readability |
| Line spacing | 1.15x | PASS -- appropriate for fiction |
| Paragraph indent | 1.5em | PASS |
| Paragraph spacing | 0pt | PASS -- no inter-paragraph gaps (correct for fiction) |
| Widow/orphan control | \widowpenalty=10000, \clubpenalty=10000 | PASS |
| Emergency stretch | 1.5em | PASS -- prevents most overfull boxes |
| Headers | Book title (verso) / Chapter title (recto) | PASS |
| Page numbers | Centered footer | PASS |

### D. FRONT MATTER

| Element | Screen PDF | Print PDF | eBook | Assessment |
|---------|-----------|-----------|-------|------------|
| Half-title page | MISSING | PASS | N/A | Print has half-title; screen does not (acceptable for eBook) |
| Full title page | PASS (no author) | PASS (with author) | PASS | **ISSUE: Screen version missing author name** |
| Copyright page | PARTIAL | PARTIAL | PASS | **ISSUE: No publisher/imprint line in either version** |
| Dedication | PASS | PASS | PASS | "Is it kind?" before "Is it optimal?" |
| Epigraph | PASS | PASS | PASS | Stuart Russell quote + in-universe quote |
| Table of Contents | PASS | PASS | PASS | Auto-generated, chapter-level |

### E. BACK MATTER

| Element | Present | Assessment |
|---------|---------|------------|
| About the Author | PASS | Personal, authentic, includes health context, website links |
| Acknowledgments | PASS | Present |
| About This Novel | PASS | Technical reading recommendations (Russell, Hubinger, Alignment Forum) |
| "Also By" page | MISSING | LOW -- add when short story collection is published |
| Index | N/A | Not applicable for fiction |

### F. METADATA

| Field | Value | Assessment |
|-------|-------|------------|
| Title | "The Policy" | PASS |
| Author | "Alex Towell" | PASS |
| Language | en-US | PASS |
| Description | 200+ word blurb | PASS -- strong hook, comp titles (Chiang, Egan, Watts) |
| Categories | Hard SF, AI SF | PASS -- two BISAC categories |
| Keywords | 7 keywords | PASS -- max 7, all relevant ("AI alignment fiction," "mesa-optimization," etc.) |
| eBook price | $4.99 | PASS -- qualifies for 70% royalty ($2.99-$9.99 range) |
| Paperback price | $16.99 | PASS -- reasonable for 365pp trade paperback |
| ISBN | NOT SET | **ISSUE: Decision needed (KDP free vs. purchased)** |
| ASIN | N/A | Assigned by Amazon at upload |
| Series info | NOT SET | LOW -- add when trilogy materializes |

### G. COVER

| Requirement | eBook | Paperback |
|-------------|-------|-----------|
| File exists | PASS (`kdp/cover-generated.png`) | **FAIL -- no full-wrap cover** |
| Dimensions | 1600x2560 px (valid for KDP) | N/A |
| Format | PNG (KDP accepts PNG, JPG, TIFF) | N/A |
| Resolution | Adequate (1600px shortest side, KDP min 1000px) | N/A |
| Content | Front cover only | Need front + spine (0.822") + back |

**metadata.yaml comment is misleading:** States "2560x1600px (1.6:1 ratio)" but the actual file is 1600x2560 (portrait). KDP's actual spec is: minimum 1000px on shortest side, ideal 2560px on longest side, ratio between 1:1 and 1:1.6. The cover file IS valid.

### H. BUILD QUALITY

| Check | Result | Details |
|-------|--------|---------|
| Print PDF compiles | PASS | Two-pass, no errors |
| Overfull hbox | 26 warnings | All from verbatim/listing environments (terminal output, code blocks). Worst: 542pt overflow. These extend into margins on 6x9 and will be visible. |
| Underfull hbox | 161 warnings | Standard for fiction with many short paragraphs. Not a problem. |
| EPUB generates | PASS | pandoc with Lua filter, clean output |
| EPUB structure | PASS | EPUB3, proper content.opf, NCX, nav.xhtml |
| EPUB metadata | PASS | Title, author, description, language all populated |
| Math rendering | PASS | MathML with Unicode fallbacks via Lua filter |

---

## Action Items

### BLOCKING (must fix before submission)

| # | Issue | Severity | Fix |
|---|-------|----------|-----|
| 1 | **No full-wrap paperback cover** | BLOCKING | Use KDP Cover Calculator for 6x9, 365pp white paper (spine ~0.822"). Generate front + spine + back PDF. The `kdp-cover` MCP tool can compute exact dimensions. |
| 2 | **Author name missing from screen-version title page** | BLOCKING | Add `{\Large Alex Towell\par}` to `The_Policy.tex` title page (line ~73). The print version already has this. |
| 3 | **Copyright page missing publisher line** | BLOCKING | Add `Published by [imprint name]\\` or `Independently Published\\` to both `The_Policy.tex` (line ~84) and `The_Policy_print.tex` (line ~146). KDP paperback requires publisher identification. |

### HIGH (should fix before submission)

| # | Issue | Severity | Fix |
|---|-------|----------|-----|
| 4 | **26 overfull hbox in print PDF** | HIGH | The verbatim environments (SIGMA terminal output, code blocks) overflow the 6x9 margins. Fix: wrap long lines in verbatim blocks, or replace `verbatim` with `quote` + `\emph{}` environments (which the novel already uses elsewhere for SIGMA output). Check chapters 5, 15, 16 specifically. |
| 5 | **ISBN decision** | HIGH | Choose: (a) Free KDP ISBN (ties to Amazon, publisher listed as "Independently Published"), (b) Purchase ISBN from Bowker ($125 single, $295 for 10) with your own imprint. If distributing beyond Amazon later, own ISBN is better. |
| 6 | **Copyright year** | HIGH | Currently "2025." If publishing in 2026, update to "2026" or "2025, 2026." |

### MEDIUM (recommended improvements)

| # | Issue | Severity | Fix |
|---|-------|----------|-----|
| 7 | **"Look Inside" optimization** | MEDIUM | Amazon shows ~10% of book in preview. Currently: title, copyright, dedication, epigraph, TOC before Chapter 1 begins. Consider moving TOC to back matter (common in KDP fiction) so the preview reaches the opening scene. |
| 8 | **EPUB validation** | MEDIUM | `epubcheck` not installed. Install and validate before submission: `sudo apt install epubcheck && epubcheck The_Policy.epub`. Amazon's ingestion pipeline will reject some EPUB errors that pandoc doesn't catch. |
| 9 | **metadata.yaml cover comment** | MEDIUM | Change `cover_ebook: "2560x1600px JPG/TIFF (1.6:1 ratio)"` to `cover_ebook: "1600x2560px (portrait, 1:1.6 ratio, min 1000px shortest side)"` to match actual file and KDP spec. |
| 10 | **Print Makefile target** | MEDIUM | `The_Policy_print.tex` is not in the Makefile build chain. Add `make print` target so `make all` includes it. |

### LOW (optional polish)

| # | Issue | Severity | Fix |
|---|-------|----------|-----|
| 11 | **Price optimization** | LOW | $4.99 is valid. $5.99 or $6.99 may better signal literary quality. Author's call. |
| 12 | **Series metadata** | LOW | Add when The Defection / The Ontological Crisis are published. |
| 13 | **"Also By" page** | LOW | Add when short story collection is ready. |
| 14 | **Kindle Previewer test** | LOW | Download Amazon's Kindle Previewer 3 and test the EPUB before submission. Catches rendering issues on actual Kindle devices. |

---

## Submission Readiness Score

| Category | Score | Notes |
|----------|-------|-------|
| Manuscript content | 10/10 | Complete, reviewed, 91K words |
| Interior formatting (eBook) | 9/10 | Clean EPUB, math fallbacks, good CSS |
| Interior formatting (paperback) | 8/10 | Professional, but overfull hbox in verbatim environments |
| Front matter | 8/10 | Missing author name on screen title page; no publisher line |
| Back matter | 9/10 | About Author, Acknowledgments, About Novel all present |
| Metadata | 9/10 | Complete except ISBN |
| Cover (eBook) | 8/10 | Exists and valid, but generated/placeholder quality TBD |
| Cover (paperback) | 0/10 | Does not exist |
| Build pipeline | 9/10 | Solid, just needs print target in Makefile |
| **Overall** | **78/100** | **Close. Fix 3 blocking items + overfull hbox = submittable.** |
