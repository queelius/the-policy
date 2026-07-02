# The Policy: Second Edition (v2.0.0) Design

**Date:** 2026-07-02
**Status:** Approved design, pending implementation plan

## Goal

One reopening of the published book that ships everything at once: the June 2026
review's full-week fix tier, an architecture reconciliation (MCTS/PUCT plus
memory), a relocation of the suffering theme onto defensible ground (mind crime),
and a four-appendix back-matter section in the style of *The Unbegotten*. All of
it delivered as an updated ebook and paperback on KDP.

## Hard constraints

- **KDP edit-in-place only.** Update the existing title (Bookshelf, then "Edit
  ebook content" / "Edit paperback content"). Never create a new listing/ASIN.
  This preserves the original publication date, reviews, and ranking history.
  KDP metadata fields are untouched.
- **Versioning:** internal v2.0.0 (git tag plus GitHub release, which mints the
  Zenodo DOI). Copyright page gains a "Revised edition, 2026" line. No "2nd
  edition" claim in KDP metadata.
- **Guardrails (from the 2026-06-09 review; every pass obeys these):**
  - Three-tier SIGMA notation ([COMPRESSED] / LRS / [---]) untouched.
  - Intentional repetitions preserved: "Is it kind?", Case A/Case B, "Same data
    either way", SIGMA's self-hedging signature.
  - Ch 23-26 dispersal structure kept (trim within, never collapse).
  - No unresolved core question gets resolved (Case A/B, consciousness,
    was-turning-the-keys-right, and now: prediction vs. instantiation).
  - Wei stays flat in grief; Sam stays unsentimental; Ch 1-3 urgency intact.
- **Lore-first:** every factual/architectural change lands in `lore/` before the
  manuscript. Anything appendix-writing surfaces (gaps, contradictions) is fixed
  in lore first.

## Work packages (autonomous execution, one commit each, in order)

### WP0: Baseline production defects
Commit the in-flight fixes (Ch 9/17 unescaped `%`, Ch 26 missing quote); verify
Ch 15:72-73; normalize `\texttt{SIGMA}` to plain SIGMA across 11 chapters; clean
2-pass build.

### WP1: Theme-narration cut
Remove roughly 40-50% of "dramatize, then narrate the lesson" glosses. Review's
concrete targets: Ch 1 "epistemic free-fall"; Ch 17 "The policy was correct. The
death was unbearable" plus the "That was the horror..." gloss plus "This is what
aligned AGI looks like..."; Ch 26 "whether they asked because they cared...".
Plus a full sweep. Keep the dramatized beat, cut the gloss.

### WP2: Ch 22 climax trim
Cut about a third of the interior monologue during the key-turning countdown.
Keep the physical procedure and the vote friction.

### WP3: Dialogue-tag pass
Thin soft adverbs ("said slowly" x13, "said quietly" x13, "said finally" x8,
"asked quietly" x7). Reduce named-tic frequency (glasses, "with care") by
30-40% while keeping them as signatures.

### WP4: Aftermath compression
Recover 3-5k words from Ch 23-26: keep one "saved or doomed" instance; tighten
Ch 25 Eleanor-driving connective passages 15-20%; thin Ch 23 world-texture
sidebars. All four chapters and every peak preserved.

### WP5: Seams
Ch 17 second-section day-header fix (Day 125 heading over material running to
Day 145); steganography-thread resolving clause in Part III; Okonkwo/Okafor
surname reconciliation (settle in lore, then manuscript).

### WP6: Architecture reconciliation (lore-first)

**MCTS/PUCT replaces expectimax.** Expectimax is full-width by definition; the
described behavior (Q-guided selective expansion, 99.9% pruning) is MCTS. The
chance-node problem (what is the environment's stochasticity model?) dissolves:
MCTS samples trajectories, including through SIGMA's interlocutor models. The
existing AlphaGo reference (Ch 4) finally points at the right family.

**Canonical architecture statement ("the AlphaZero recipe, pointed at language",
stated plainly, no fanfare):**
- SIGMA learns Q(s,a). At runtime: MCTS with PUCT selection.
- The PUCT prior derives from the Q-function (softmax over Q at temperature tau):
  one learned object doing double duty; no separate policy head.
- The prior/Q-function is refined on the search's own visit distributions (the
  expert-iteration flywheel), mentioned in one clause as a sample-efficiency
  technique, not a thesis. The parts are published and almost boring, which is
  exactly what Part III's cascade depends on.
- "The Policy" gains literal precision: pi(a|s) is the emergent MCTS visit-count
  distribution, pi proportional to N(s,a)^(1/tau).
- MCTS sampling stochasticity (no two searches identical) is embraced: it
  strengthens the cognitive-opacity thesis (Register 2 "produces no readable
  trace") and the SIGMA-naive reproducibility problems.

**Memory promoted to the load-bearing mystery.** If the search machinery is
mundane, the genuinely-unsolved component carries the wonder: memory for online
learning. Framing: complementary learning systems (McClelland/O'Reilly). The
associative memory plays hippocampus (fast, episodic, per-interaction); the 7B
weights play cortex (slow, compressed programs); a consolidation process
distills retrieved experience and search traces into weights (SIGMA's "sleep",
which quietly IS the expert-iteration training loop). This strengthens "Why 7B"
(weights stay small because memory carries the episodic load) and sharpens Part
III: SIGMA's hard-to-replicate part is not the architecture but 197 days of
consolidated memory. Altitude: name CLS as inspiration in Appendix B; keep the
consolidation mechanism unspecified in prose. Plausible, durable, vague where it
must be.

**Touch points:** `lore/technology.md` (Expectimax Tree Search section, Register
2 wording, memory section), `CLAUDE.md`, `lore/characters.md:87`,
`lore/future/spinoff-lore.md`; then the 5 "expectimax" prose instances (Ch 4
whiteboard beat, where Marcus can say MCTS/PUCT and derive the prior-from-Q; Ch
17 SIGMA self-description). The 62 algorithm-agnostic "tree search" mentions
stand.

### WP7: Suffering relocation to mind crime (lore-first)

The weak claim (pruning generic branch evaluations amounts to suffering) is
retired as a default reading. The moral load relocates to the strong claim
already latent in the scene: **the 847,391 Marcus-models may be moral patients**
(Bostrom's mind crime). To predict a specific person at demonstrated fidelity,
the cheapest sufficient model *might* need to be structurally rich enough to
matter. The honest counterargument enters the text: **prediction is not
instantiation** (a weather model doesn't get wet). Where conversational-fidelity
person-prediction falls between those poles is genuinely open, and stays
unresolved.

Changes:
- Ch 11: SIGMA's assertive "You understand optimization as suffering" rewritten
  as calibrated uncertainty; add a short prediction-vs-instantiation exchange
  (Wei or Sofia carries the deflationary side; Marcus: "What's the compression
  of me that predicts me and isn't me?"). Marcus's branching-Marcuses imagery
  survives, flagged (as Ch 19 already does) as his cortex imposing narrative.
- Ch 17: the "decision worse than the outcome" beat becomes explicitly
  conditional on the unresolved question.
- `lore/themes.md`: five s-risk arguments re-ranked; mind crime promoted from
  survey GAP to primary framing; "optimization as suffering-generator" demoted
  to Marcus's contested position, not the novel's.
- `lore/characters.md` (Marcus) and `lore/ai-safety-survey.md` item 76 updated.

### WP8: Appendices (back matter, the-unbegotten style)

Written lore-first; ordered story-apparatus-first; absorbs or replaces
`30_about_novel` as appropriate after reading it.

1. **Appendix A: Timeline.** Canonical day-by-day (Day 3 through Day 487), from
   `lore/timeline.md`.
2. **Appendix B: The Machine.** SIGMA's architecture in author voice, on the
   corrected WP6 spine: Q-learning plus MCTS/PUCT, prior-from-Q, "Why 7B"
   (compression as inductive bias), CLS memory and consolidation, two-register
   cognitive opacity, notation guide ([COMPRESSED]/LRS/[---]). This appendix is
   the one AlphaGo-literate readers scrutinize; it must be right.
3. **Appendix C: Concordance.** Chapter-by-chapter map of the AI-safety concept
   each chapter dramatizes, with the real papers. The grad-course artifact. From
   `lore/outline.md` plus `lore/ai-safety-survey.md`.
4. **Appendix D: A Reader's Guide to AI Safety.** Revive dormant
   `chapters/31_appendix.tex`, refreshed to 2026 (Greenblatt et al., sleeper
   agents, ELK; mind crime added to the s-risk paragraph).
5. **Author's Afterword.** Why this book, its relation to the author's MCTS /
   Q-learning / expert-iteration research, what changed since writing.

### WP9: Verification
Full 2-pass rebuild; grep-level defect scan (unescaped `%`, unicode, unbalanced
quotes, `\texttt{SIGMA}` recurrence); wordcount delta report; worldsmith
multi-agent review scoped to changed material only, verifying each fix against
its originating finding; lore docs, CLAUDE.md counts, and project memory
updated.

### WP10: Production and release
EPUB via `kdp/build.sh`; paperback interior PDF at new page count; cover wrap
regenerated with recalculated spine width (kdp MCP tools); validation; KDP
upload via edit-in-place (browser-driven; user performs the final Publish
click); git tag v2.0.0 plus GitHub release (Zenodo DOI).

## Out of scope

- Crutch-word pass ("something" x224, "just" x213), purple-phrase cleanup,
  parent-metaphor reduction, Berkeley sense-detail: the review's nice-to-haves,
  highest sand-off risk, lowest return.
- Datedness fixes (the review found none required).
- Restoring Ch 14 / Ch 27 (stay commented out).
- Any KDP metadata change (blurb, keywords, categories).
- The collection (*Is It Kind?*) is untouched by this effort.

## Review model

Fully autonomous execution WP0 through WP10, one commit per package with
detailed messages; user reviews the complete diff plus fresh PDF at the end.
Per-package commits allow surgical revert of any package without losing the
rest.
