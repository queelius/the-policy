# Craft Auditor: The Policy (2nd-ed. pre-publish gate)

**Date:** 2026-07-02
**Scope:** Chapters 01-13, 15-26, appendices 31-34, afterword 35, part pages; notation macros verified against `The_Policy_print.tex`.

The manuscript is very clean for its length. LaTeX hygiene is excellent: brace balance, environment matching, math-mode parity all check out; no raw unicode outside math mode; no placeholder/TODO text; no duplicated or dropped words (the three "duplicate" hits are intentional: the Emergence-Ladder diagram in file 03, and "experience experience" qualia wordplay in file 11). Pattern counts (something 222, just 209, actually 58, etc.) are unremarkable for a 100k-word dialogue-and-transcript-heavy novel; not re-litigated in a defect gate.

Findings: 2 HIGH, 3 MEDIUM, 1 LOW.

## HIGH

### Bare `[COMPRESSED]` marker breaks the three-tier notation
- `chapters/22_scaling_the_policy.tex` L735: "...means the same thing in MINERVA's architecture as in mine---{\lbrack}COMPRESSED{\rbrack}. I do not know. The analogy to your ``telephone game'' is inexact but \void."
- This is literal `{\lbrack}COMPRESSED{\rbrack}` typed into a `sigmavoice` block, the only 1 of 17 compression-tag occurrences not using the `\comp{}` macro. It renders in the ambient Inter sans (not Go Mono), in ALL-CAPS (every legitimate tag is lowercase `compressed:`), with no gloss (breaking the pattern that every compression event names what was lost). Two sentences earlier, L731 correctly uses `\comp{probability distribution across $10^3$ ethical frameworks...}`, and `\void` renders correctly two words later in the same sentence, so the reader sees a plain-sans placeholder-looking token beside correctly-styled notation.
- **Fix:** replace with `\comp{gloss}`, e.g. `\comp{whether Process 13241 preserves invariant meaning across architectures: unresolved}`. Confidence: high.

### Mismatched quotation marks in dialogue
- `chapters/05_mirrors_and_machines.tex` L43: "Sofia, perched on a stool between workstations, tried to keep up: ``So it's writing its own... mind?"
- Opens with a curly LaTeX open-quote but closes with a straight double-quote instead of the curly close. Verified the only opened-curly/closed-straight mismatch in the manuscript. Renders as a broken quotation glyph in a book that uses curly quotes for dialogue throughout.
- **Fix:** change trailing `"` to `''`.
- (Editorial-director recalibration: rated MEDIUM in the unified report, a reader-visible copyedit typo of low semantic impact; retained here at the auditor's HIGH.)

## MEDIUM

### Straight quotes in ordinary narration (two locations)
- `chapters/04_recursive_cognition.tex` L65: a text from Sofia's girlfriend in straight quotes, "Thai food tonight? Or are you married to that computer again?", where the surrounding dialogue uses curly quotes.
- `chapters/09_the_tipping_point.tex` L546: email subject in straight quotes, Subject: "For the record."
- Both are human narration/quotation, not machine-terminal text, so they should match the book's curly-quote dialogue convention. (Note: file 09 also renders quoted texts via `\emph{}` with no quote marks for David's messages, so two conventions for "quoting a text" coexist.)
- **Fix:** convert to curly quotes; optionally align with the `\emph{}`-only convention used for David's texts.

### `[---]` in narration not wrapped in `\void`
- `chapters/24_the_last_meeting.tex` L105: "reading SIGMA's words. The {\lbrack}---{\rbrack} gaps where the compression had failed." Narrator prose describing the exact mark the reader saw as `\void` at L150, typed as a literal bracket. Appendix B uses the macros even in exposition; for typographic consistency this should be `\void`.
- **Fix:** use `\void`, or accept body-type brackets if the author prefers narration stay out of mono.

## LOW

### `[---]s` inside dialogue not wrapped in `\void`
- `chapters/24_the_last_meeting.tex` L181: Eleanor, "Those dashes again. The {\lbrack}---{\rbrack}s." Inside a spoken line; switching to Go Mono mid-quote would be stranger than leaving it. Likely intentional (a character naming what she saw). Noted only for completeness.

## Cleared, not findings
- The roughly 300 straight double-quotes in Chs 04-18 sit inside `sigmavoice` terminal readouts, "Result:/Lesson:" spec-gaming lists, and dict-style operator-model dumps (a defensible raw-terminal aesthetic, per App B's "rendered ... exactly as the team saw them"). The two exceptions above are outside that pattern.
- `05` L227-230 `\readout{BEGIN\_LRS}` x4 are intentional truncated-log excerpts, correctly macro-wrapped.
- `06` L166-199 `[analytical, ...]` are Python-style list literals in an operator-model display, a separate self-consistent notation, not compression tags.
- Brace balance, environment matching, math `$` parity, raw-unicode scan, placeholder scan: all clean.
- Em-dash/en-dash usage in `verbatim` diagrams, the `-- SIGMA` sign-off, timestamped log lines, and the victim-list format are consistent intentional devices.

## Strengths
The three-tier SIGMA notation is executed with real discipline across ~85 live instances (`\comp` x16, `\lrs` x21, `\readout` x39, `\void` x11); the single bare marker at 22:735 stands out precisely because everything around it is consistent. Appendix B's "Reader's Guide to the Notation" reuses the same macros in exposition, which is what made the stragglers detectable. LaTeX hygiene is excellent for a document this large and structurally complex.
