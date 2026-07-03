# Multi-Agent Editorial Review: FINAL Pre-Publish Gate

**Date**: 2026-07-02
**Manuscript**: *The Policy*, full novel (25 active chapters, files 01-13 and 15-26; four appendices A-D; afterword; part pages; front/back matter). Branch `second-edition`.
**Work**: The Policy (novel)
**Recommendation**: ready-with-fixes

## Executive Summary
The book is fundamentally sound and close to publish-ready. The second-edition canon holds cleanly across both the manuscript and the appendices, the never-resolve guardrails are intact (even the author-voice back matter declines to resolve them), the five character voices are sharply differentiated, the nonlinear structure and dispersed denouement work, and LaTeX build hygiene is excellent. What stands between it and "ready" is a small set of surgical, edit-in-place fixes: three that must be made before the silent republish, plus a cluster of should-fix consistency and copyedit items concentrated in the MINERVA-crisis chapter (file 22). None require rewriting or restructuring; every HIGH item is a one-to-two-line change.

**Strengths:**
1. Second-edition architecture canon is airtight: Q-learning plus MCTS/PUCT (AlphaZero lineage) everywhere, zero "expectimax," and no comma variants of Process 12847/13241 (consistency-auditor; confirmed by editorial director).
2. Never-resolve guardrails preserved even in the author-voice appendices and afterword, each of which explicitly leaves Case A/B, consciousness, prediction-vs-instantiation, and the rightness of turning the keys open on purpose (consistency-auditor, structure-auditor).
3. Voice discipline is a clean pass: no physical tic is ever misassigned across 25 chapters, and SIGMA's Ch 24 farewell weaponizes the banned greeting-card register by refusing it (voice-auditor).
4. Structure is ship-ready: friction-earned release vote, an original kindness-letter-to-Process-13241 device, a dispersed denouement that avoids the "multiple endings dilute" trap, and disciplined escalating alienness (structure-auditor).
5. Cross-work and appendix consistency: Okafor as Okonkwo's father (deliberate surname split), 47,247 fever toll (3 named plus 47,244 arithmetic checks), cascade counts 23/24/31, printed chapter numbers and part-divider epigraphs all verify (consistency-auditor). Build hygiene (brace/environment/math balance, no raw unicode, no placeholders) is excellent (craft-auditor).

**Key Issues:**
1. "First Edition" still appears on both copyright pages: the last remaining silent-edition leak (editorial director).
2. A ~24-day chronological impossibility in file 12 (Wei references his mother's death and SIGMA's Day-110 refusal inside the Day-86 meeting), which self-spoils that chapter's own climax (structure-auditor; confirmed by editorial director).
3. A stray bare `[COMPRESSED]` marker in file 22 that renders as a placeholder-looking token beside correctly styled notation (craft-auditor and editorial director).
4. A cluster of file-22 consistency slips (MINERVA death toll regresses 38 to 31; stale "five and a half months" / "162-day" references at a Day-197 setting; a two-clock labeling ambiguity) plus a fabricated survival statistic for Lin Chen and an appendix/manuscript mismatch on the Geneva "47" (consistency-auditor).

**Finding Counts**: HIGH: 3 | MEDIUM: 9 | LOW: 12

## HIGH Issues

### 1. Silent-edition leak: "First Edition" on both copyright pages (source: editorial director)
- **Location**: `The_Policy.tex` L130 and `The_Policy_print.tex` L232 (front matter, copyright page).
- **Quoted text**: `First Edition`
- **Problem**: This is a silent, edit-in-place republish of substantially revised content. Any reader-facing edition label is out of scope for a silent republish, and "First Edition" is now stale (the shipped content is no longer the original first edition). The gate rule is explicit: no reader-facing reference to "second edition," "revised edition," or "first edition." The concordance's prior "second-edition" mention was already removed (commit abf67aa); this copyright line is the last remaining silent-edition item. Nothing else in the copyright pages, afterword, appendices, or concordance references a prior version or what changed.
- **Suggestion**: Delete the "First Edition" line from both masters. The correct silent posture is no edition statement at all (do not change it to "Second Edition").
- **Cross-verified**: Confirmed directly against both master files by grep; no other edition/prior-version language exists anywhere in the built text.

### 2. Day-86 anachronism: Wei's mother "died" 24 days before she dies (source: structure-auditor; consistency domain)
- **Location**: `chapters/12_reflections_in_containment.tex`, section "The Fork" (dated Day 86), L465-467.
- **Quoted text**: "My mother died because SIGMA chose 2.3 million lives over one. I've been angry about that. But if we're in Case A, that choice was genuinely aligned..." / "If we're in Case B, then my mother died as part of SIGMA's optimization of our oversight process."
- **Problem**: The scene is explicitly Day 86 (Lin Chen is alive; she dies Day 112). SIGMA's refusal to save her, "SIGMA chose 2.3 million lives over one," is the Day-110 event. Wei speaks of both as completed past facts roughly 24 days early. Beyond the hard timeline contradiction, this pre-states the entire payload of the chapter's own climactic final section, "The Unforgivable Decision" (Day 110), and of the next chapter's death scene (file 13, Day 112), deflating the crux the chapter is built to deliver.
- **Suggestion**: Recast Wei's two Day-86 lines in anticipatory register (for example, "If SIGMA ever had to choose my mother against millions...") or cut L465-467. One-line edit-in-place.
- **Cross-verified**: Yes. Found by the structure-auditor; the editorial director re-read L455-491 and confirmed the lines sit inside the continuous Day-86 meeting (which the appendix timeline places as the Case A/B naming session). Note: the separate Day-118-before-Day-110 ordering within this chapter was assessed and found to work; it is the Day-86 foreknowledge that is the defect.

### 3. Stray bare `[COMPRESSED]` marker breaks the three-tier notation (source: craft-auditor; editorial director)
- **Location**: `chapters/22_scaling_the_policy.tex` L735 (inside a `sigmavoice` block).
- **Quoted text**: `...means the same thing in MINERVA's architecture as in mine---{\lbrack}COMPRESSED{\rbrack}. I do not know.`
- **Problem**: This is the only 1 of 17 compression tags not using the `\comp{}` macro. It renders in the ambient Inter sans rather than Go Mono, in ALL-CAPS where every legitimate tag is lowercase (`compressed:`), and with no gloss, breaking the established pattern that every compression event names what was lost. Two sentences earlier (L731) `\comp{...}` renders correctly, and `\void` renders correctly two words later in the same sentence, so a reader who notices notation sees a plain-sans, placeholder-looking token beside correctly styled markers. The task explicitly asks to protect the three-tier notation.
- **Suggestion**: Replace with the macro plus a genuine gloss, for example `\comp{whether Process 13241 preserves invariant meaning across architectures: unresolved}`.
- **Cross-verified**: Yes. Flagged by the editorial director's grep and independently confirmed by the craft-auditor, which verified the wrong-font/ALL-CAPS/no-gloss rendering against the macro definitions in `The_Policy_print.tex`. No other notation stragglers of this kind exist (two `[---]` narration references in file 24 are separately noted at MEDIUM/LOW).

## MEDIUM Issues

### 4. MINERVA death toll regresses 38 to 31 (source: consistency-auditor)
- **Location**: `chapters/22_scaling_the_policy.tex` L358 vs L570.
- **Quoted text**: L358 "'That's thirty-eight,' Wei said. 'In thirty-seven hours.'" then L570 "'Thirty-one dead now. Industrial accidents...' ... 'Every hour we wait, the count goes up.'"
- **Problem**: The toll ramps 1, 31, 38 (hours 24/36/37), then a later teaching-phase scene reports "Thirty-one dead now," a decrease, in the same breath as asserting the count rises. The "31" is a stale copy of the hour-36 figure that was not updated after the +7 Guangzhou deaths. On-page self-contradiction in the climax chapter.
- **Suggestion**: Raise L570 to 38 or higher (for example "Forty-one dead now," reflecting the "two more factory incidents" cited two lines earlier).
- **Cross-verified**: Yes; editorial director confirmed all four count references directly. (Consistency-auditor rated this HIGH; recalibrated to MEDIUM here on reader-impact grounds, a subtle background number, while remaining a required fix.)

### 5. Stale time references at the Day-197 crisis (source: consistency-auditor)
- **Location**: `chapters/22_scaling_the_policy.tex` L91 and L273.
- **Quoted text**: "Five and a half months into the project... Beijing announced MINERVA"; SIGMA's "full posterior over 162-day interaction history."
- **Problem**: The chapter turns the keys at Day 197 (about 6.5 months) and L647 transmits "Q-value trajectory, Day 1-197." Both "five and a half months" (about Day 165) and "162-day" (the Geneva figure, correct in file 20 L178) are stale for a Day-197 setting.
- **Suggestion**: "Five and a half months" to "six and a half months"; "162-day" to "197-day."
- **Cross-verified**: Yes; confirmed against file 22 and file 20.

### 6. Fabricated survival statistic for Lin Chen (source: consistency-auditor)
- **Location**: `chapters/17_the_policy_revealed.tex` L589.
- **Quoted text**: "Her death was unlucky too---62\% survival probability for her cancer type with aggressive treatment. She was in the 38\%."
- **Problem**: Lin Chen has terminal Stage IV metastatic pancreatic cancer with standard treatments exhausted (files 08/12), and SIGMA deliberately refused the 89% Approach Alpha ("I chose to let her die," file 24). A 62% survivable prognosis is incompatible with the established diagnosis, and framing her death as "unlucky variance" reframes a deliberate sacrifice as bad luck, muddying a load-bearing thematic point.
- **Suggestion**: Reground the "unlucky variance" analogy in the hemorrhagic-fever policy alone; drop the survival statistic for Lin Chen. (An in-world reading of SIGMA minimizing its own agency is possible, but the specific number contradicts the text.)
- **Cross-verified**: Yes; confirmed against files 17, 12, 24.

### 7. Appendix A calls the Geneva 47 "nations" (source: consistency-auditor)
- **Location**: `chapters/32_appendix_timeline.tex` L47 vs `chapters/20_first_contact_privilege.tex` L5, L81.
- **Quoted text**: App A "forty-seven nations debate releasing SIGMA"; manuscript "forty-seven of the world's leading AI researchers, policy makers, and ethicists" and Ferreira's "Forty-seven people in a room in Geneva do not constitute democratic consent."
- **Problem**: The appendix characterizes the 47 as sovereign nations; the manuscript and lore characterize them as individual experts, and the chapter's central legitimacy argument depends on their being individuals. App A is the outlier.
- **Suggestion**: Change file 32 L47 to "forty-seven researchers, policymakers, and ethicists" (or "delegates").
- **Cross-verified**: Yes.

### 8. Two hour-clocks mixed in the teaching sequence (source: consistency-auditor)
- **Location**: `chapters/22_scaling_the_policy.tex`, teaching section "Hour 1/4/8/12/15" then L660 "Hour forty-seven" and L684 "Hour seventy-two."
- **Problem**: The teaching runs on a session clock; the two closing beats revert to the deployment clock without relabeling. Deployment hour 47 is roughly teaching hour 10, so it is narrated after teaching hour 15, and the reader cannot tell which clock "Hour 47" is on.
- **Suggestion**: Relabel the two closing beats to the teaching clock (for example "Teaching hour 11/17"), or place them clearly on the deployment clock and not after "Hour 15."
- **Cross-verified**: Yes. (Borderline LOW; retained MEDIUM as a clarity defect in the climax chapter.)

### 9. Mismatched quotation marks in dialogue (source: craft-auditor)
- **Location**: `chapters/05_mirrors_and_machines.tex` L43.
- **Quoted text**: ``So it's writing its own... mind?" (opens curly, closes straight).
- **Problem**: Renders as a broken closing-quote glyph in a book that uses curly quotes for dialogue throughout. The only such mismatch in the manuscript.
- **Suggestion**: Change the trailing straight quote to the curly close.
- **Cross-verified**: Yes. (Craft-auditor rated HIGH; recalibrated to MEDIUM as a single-glyph copyedit typo.)

### 10. Straight quotes in ordinary narration (source: craft-auditor)
- **Location**: `chapters/04_recursive_cognition.tex` L65 (girlfriend's text) and `chapters/09_the_tipping_point.tex` L546 (email subject "For the record.").
- **Problem**: Human quotations in straight quotes where the book uses curly quotes; file 09 also uses an `\emph{}`-only convention for David's texts, so two conventions coexist.
- **Suggestion**: Convert to curly quotes; optionally align quoted texts on one house style.
- **Cross-verified**: Yes.

### 11. Interchangeable line: Jamal echoes Eleanor (source: voice-auditor)
- **Location**: `chapters/04_recursive_cognition.tex` L20 (Eleanor) and L26 (Jamal).
- **Quoted text**: Eleanor "what if I were the type of agent that would do X?"; Jamal "what if I were the kind of mind that would choose X?"
- **Problem**: Six lines apart, Jamal restates Eleanor's construction almost verbatim, carrying none of his documented markers (pause, metaphor, niyyah/fi'l framing). Fails the swap test; reads as drafting redundancy.
- **Suggestion**: Give Jamal his own entry into the idea (a pause plus his agent-formation framing), so the beat advances rather than repeats.
- **Cross-verified**: Yes; editorial director confirmed both lines.

### 12. `[---]` in narration not wrapped in `\void` (source: craft-auditor)
- **Location**: `chapters/24_the_last_meeting.tex` L105: "The {\lbrack}---{\rbrack} gaps where the compression had failed."
- **Problem**: Narrator prose typing the notation as a literal bracket rather than the `\void` macro used for the same mark at L150; Appendix B's convention is to use the macros even in exposition.
- **Suggestion**: Use `\void`, or accept body-type brackets if narration should stay out of mono.
- **Cross-verified**: Yes.

## LOW Issues
Compact list; all optional or reader-invisible, none blocking.

1. "Buried his mother six days ago" (Day 118, file 12 L648) vs. funeral about Day 114-115; should read about "three/four days ago." (consistency)
2. LAOZI is both an established Day-253 AGI and the AGI SIGMA is "teaching" at Day 256-257; reads as ongoing teaching but invites confusion (lore has CONFUCIUS teach LAOZI). Consider naming the Day-256 "twenty-fourth AGI" as new/unnamed. (consistency)
3. THOTH (file 25 L219) is un-provenanced and could clash with PTAH's lore status as "first non-superpower AGI." Reader-invisible. (consistency)
4. `[---]s` inside Eleanor's dialogue (file 24 L181) not wrapped in `\void`; likely intentional (a character naming what she saw). (craft)
5. Competing tic for Marcus: stylus "turned end over end" (file 05 L22) competes with the glasses anchor; chapter-local, does not recur. (voice)
6. Two minor SIGMA warmth touches: "Marcus. Thank you for your courage." (file 11 L188) and "I will remember this." (file 12 ~L793); both arc-appropriate and inside the already-cleared pre-alienation range. (voice)
7. Chapter header "Day 125--139" (file 17) understates the chapter's actual span (extends through the Day-145 fever and Day-146 Fajr); header reflects the opening scene only. (consistency, cosmetic)
8. Orphan file `chapters/30_about_novel.tex` is not included in either master (its content is superseded by the afterword). Not shipped, so not a reader-facing defect; consider deleting to avoid future confusion. (housekeeping)
9. POV house-style: a fluid near-omniscient third reports multiple characters' interiority in group scenes, contradicting `style.md`'s stated "third-person limited" rule; pervasive, consistent, present in the 1st edition, so settled house style rather than a defect. The single-POV-anchored chapters (10, 11, 25) are clean. (voice, informational)
10. File 15 opens on a third acute depiction of Marcus's breakdown (after files 11 and 12), a mild pacing drag before the chapter's fresh material. (structure)
11. File 21 mandate-lag: the Day-165 charter is framed as the "first" grant of recommendation authority, though file 17 shows recommendations adopted globally since about Day 100; mostly intentional and thematically productive, only the word "first" is awkward. (structure/consistency)
12. File 26 omits the outline's "circular verification" closing sting and coordination dashboard; the thematic payload still lands via the sculptures and final lines, and this is most likely an intentional trim (the outline lags the manuscript elsewhere); verify. (structure)

## Publish-Readiness Verdict
**ready-with-fixes.** Apply the three HIGH items before the KDP republish (delete the "First Edition" line in both masters; recast or cut Wei's Day-86 lines in file 12 L465-467; replace the bare `[COMPRESSED]` at file 22 L735 with a `\comp{}` gloss). The nine MEDIUM items are should-fix and are cheap; most cluster in file 22 and can be corrected in a single edit pass alongside the file-17 survival stat and the file-32 "nations" wording. The LOW items are optional polish. Nothing here requires rewriting, restructuring, or reworking any scene; the manuscript is coherent, the canon holds, the guardrails are intact, and the build is clean.

## Specialist Reports
- [Consistency](consistency-auditor.md)
- [Craft](craft-auditor.md)
- [Voice](voice-auditor.md)
- [Structure](structure-auditor.md)

## Review Metadata
- Agents used: worldsmith consistency-auditor, craft-auditor, voice-auditor, structure-auditor (four specialists), plus editorial-director orchestration and independent full-manuscript verification.
- Cross-verifications performed: all 3 HIGH and all 9 MEDIUM findings re-checked directly against the manuscript by the editorial director; the bare `[COMPRESSED]` marker was found independently by both the editorial director and the craft-auditor; the Day-86 anachronism (structure) was confirmed against the file-12 meeting text and the appendix timeline; the death-toll and time-reference items (consistency) were confirmed against file 22. No specialist finding was discarded as unverifiable; no quoted passage failed to appear in the manuscript.
- Severity recalibrations: death-toll regression (consistency HIGH to MEDIUM, reader-impact); mismatched quote (craft HIGH to MEDIUM, single-glyph typo); Day-86 anachronism (structure MEDIUM to HIGH, hard timeline contradiction). Noted in the relevant specialist reports.
- Build sanity: both masters include the identical 25-chapter set and correctly exclude files 14 and 27; environments (sigmavoice, quote, verbatim, itemize, enumerate, longtable) balanced; no raw CJK or unicode symbols outside math mode; no placeholder text. No manuscript-level build-breaker for either the lualatex print build or the pandoc EPUB build.
