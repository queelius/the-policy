# Craft Auditor Report: Second-Edition Verification (M2, M3, new prose)

**Date:** 2026-07-02 | **Scope:** files changed since baseline 4f6bbc8 | **Tools:** count_patterns.py, git diff sampling, cold read of new material

## Summary

**Task 1 (M2 theme-narration): RESOLVED** with two small introduced defects. **Task 2 (M3 tags/tics): RESOLVED** cleanly. **Task 3 (new prose): two HIGH findings** (a repeated Sam gender error in the new appendices; a concordance entry describing a scene cut from the manuscript in Wave 3), one MEDIUM, two LOW. Totals: 2 HIGH, 3 MEDIUM, 3 LOW.

## Pattern Audit Results

`count_patterns.py` over `chapters/*.tex` (35 files, ~101,466 words incl. appendices and the two commented-out chapters): crutch words: something 222, just 209, actually 57, very 24, really 16. Filter words: could see 17, could feel 3, seemed to 3. Weak verbs: tried to 12, started/began to 5+5. Adverb dialogue tags (broad regex) 40 (39 in active chapters after excluding files 14/27 and the protected phrase "a question, asked continuously").

Interpretation: "just" (209) and "something" (222) run ~2 per 1,000 words, at the high end of normal for a dialogue-heavy manuscript; many "something" instances are load-bearing (the book's deliberate vocabulary of unverifiability: "something like conviction," "it's not nothing"). Filter words and weak verbs are well within normal range.

---

## Task 1: M2 theme-narration cuts. RESOLVED

**(a) Named anchors.** All verified gone or converted:
- "We're in epistemic free-fall": cut (`chapters/01_initialization.tex:207`; Wei's line now ends "...We don't know if *it* knows if it's aligned.", stronger, and it now serves as the Part I epigraph).
- "That was the horror. Not that innocents died..." and "The policy was correct. The death was unbearable.": cut from Ch 17 narration; also "The math was correct. The grief was unbearable." and the "both truths simultaneously" narration. "The policy was correct" survives only inside the `@systems_bio` tweet (`17:400`), **acceptable in-world usage**; a cold utilitarian tweet is exactly the register that line belongs in.
- "This is what aligned AGI looks like" survives as Sofia dialogue trimmed to two beats (`17:582`): the theme-lecture middle ("Not friendly. Not safe... but the math is clear") was cut, leaving the claim plus the protected Case A/B tag. **Acceptable**: terse, in-voice, and the juxtaposition now reads as irony rather than thesis statement. Confidence: high.
- Ch 26 "whether they asked because they cared...": **trimmed, not cut** (`26:176`): "Whether they cared, or asking was optimal / Eleanor didn't know. Went to bed." Now a four-beat Case A/B closure in free indirect style, not a narrated lesson. Acceptable residual. Confidence: high.

**(b) Sampled cuts** (diffs read in full for Ch 1, 17, 22, 26; sampled for 2, 5, 8, 9, 11, 12, 16, 19, 25). The cuts consistently removed the narrated echo while keeping the dramatized beat: Ch 5 lost "For now, SIGMA had given them a window. / Not into its mind. / But into its shadow." and the section now ends on "There was nothing more to say." (`05:477-479`); Ch 22 lost "Two words. Infinite implications.", "The literal and metaphorical cage opened simultaneously.", "Turtles all the way down.", and the trolley-problem gloss (which also honors the anti-cliche rule); Ch 9 lost "What revealed preferences revealed."; Ch 11 lost the "typed the question that would change everything" melodrama. Ch 1 now ends on "Day 18 of the SIGMA Project." with "The age of uncertainty had begun." cut. A real improvement.

**(c) Seam check** (12+ cut sites read in surrounding context). Two introduced defects and one soft seam:

### Finding: Dialogue tag grafted onto a period-closed quote (Ch 1)
- **Location**: `chapters/01_initialization.tex:221`
- **Passage**: "``Not an accident.'' Jamal said. ``An inevitability...''"
- **Problem**: The revision replaced the action beat ("Jamal set down his pen with care.") with a bare dialogue tag but kept the period inside the quote. "Jamal said." is now a standalone fragment; a tag requires a comma.
- **Why it matters**: A copyedit-level grammar error in Chapter 1, where readers form their judgment of the book's polish.
- **Fix**: "``Not an accident,'' Jamal said." (or restore an action beat that is not the pen tic).
- **Severity**: MEDIUM. **Confidence**: high

### Finding: Same error in Ch 9
- **Location**: `chapters/09_the_tipping_point.tex:218`
- **Passage**: "``Eleanor.'' Marcus said. ``You could go. We can handle this.''"
- **Fix**: "``Eleanor,'' Marcus said."
- **Severity**: MEDIUM. **Confidence**: high

These are the only two instances (verified by pattern scan across all chapters).

### Finding: Dangling referent after gloss cut (Ch 11 coda)
- **Location**: `chapters/11_the_experiment.tex:820-824`
- **Passage**: "The cracks were still there. / They never fully closed. / And he'd chosen it."
- **Problem**: The cut sentence ("But he'd seen something true. Something that couldn't be unseen.") was the antecedent of "it." Grammatically "it" now points at "the cracks"/"they." The pronoun stumbles at the emotional close of the book's most important chapter.
- **Fix**: Restore a one-clause antecedent ("He'd seen something true. And he'd chosen it.") or fold into one sentence with the 847,391 line.
- **Severity**: LOW. **Confidence**: medium

No other seams found: Ch 25's cut of "Not Mommy anymore... But Mom. And trying." initially looked like a lost landing, but the scene's close (`25:207-213`) retains the full emotional resolution, and "Bye, Mom" (`25:189`) now lands unglossed against Ch 22's "who called her ``Eleanor''", trusting the reader, correctly.

**(d) Residual density.** Sample count of narrated-gloss constructions: Ch 1: 4 to 2; Ch 17: 9 to 4; Ch 22: 2 to 2; Ch 26: 1 to 0 (total 16 to 8). **Roughly half or better; target met.** The most gloss-like survivor is Eleanor's "That's the horror... SIGMA is teaching us that correct policy decisions still produce unbearable outcomes" (`17:544`), but it is dialogue, grounded in action, and with the surrounding narration gone it carries the theme once instead of a third time. Acceptable; first candidate if further thinning is ever wanted. The Ch 12 "That was the horror Marcus had discovered..." (`12:1078`) is the protected Part II Case A/B restatement; not flagged.

---

## Task 2: M3 soft-adverb tags and tics. RESOLVED

**(a) Numbers.** Original four patterns: baseline 41 (said quietly 13, said slowly 13, said finally 8, asked quietly 7) now **13** (6/2/2/3). Target "under 20" met. Broad adverb-tag pattern: 68 to 39. Glasses-tic instances (cleaning/removing/setting down): 33 to 22 (-33%); "with care": 9 to 6 (-33%). Both inside the 30-40% band. Raw "glasses" mentions 55 to 42 (residue includes non-tic uses: "glasses slightly askew," "They were still dirty").

**(b) Survivors are the right ones.** Spot-checked in context: "Was it worth it?" asked quietly twice in Ch 24 (`24:51`, `24:121`), a deliberate echo at the last meeting, correct to keep; Wei's "died thirty-five days ago" said quietly (`18:261`), grief register; Eleanor's "Sofia... What's your vote?" said quietly (`22:366`), vote pressure; Marcus's "Which case do you think we're in?" asked quietly (`08:647`), pivotal; "he said finally" post-AI-box (`11:788`). All six sampled "with care" survivors are stress-escalation or thesis beats (Jamal's anatta speech `11:115`, the faith-shaken confession `12:483`, the vote `22:340`, `18:319`). The pruning kept the character-defining instances and cut the wallpaper. One LOW note: **Ch 5 is now the densest surviving adverb-tag cluster** (7 in one chapter: "said excitedly" `05:110`, "asked hopefully" `05:188`, "asked desperately" `05:301`, "said simply" x3). Early-book, pre-dating the thinning pass's focus; a candidate if a third pass ever happens. Severity: LOW, confidence: medium.

**(c) Replacements.** Sampled across Ch 1, 9, 12, 16, 18, 22, 24, 26: the substitutions are overwhelmingly clean; bare "said," or promotion of existing action ("He didn't look up," Ch 24; "Marcus was quiet a moment," Ch 12). The two grafting errors at `01:221` and `09:218` (above) are the only awkward substitutions found. The revision was smart about *which* tic instance to cut when two sat close together (e.g., `16:406` cut "Marcus set his glasses on the table, lenses down" but kept "He picked his glasses back up" inside the corrigibility speech at `16:483`).

---

## Task 3: New second-edition prose. FINDINGS

### Finding: Sam is called Eleanor's "son" in two new appendices
- **Location**: `chapters/32_appendix_timeline.tex:33` and `chapters/34_appendix_concordance.tex:43`
- **Passage**: "Eleanor misses her son Sam's school play." / "(Eleanor misses her son's play; Wei's mother is dying)"
- **Problem**: Factual contradiction with the manuscript. Sam is unambiguously Eleanor's daughter throughout (Ch 9: "Eleanor sat on Sam's bed. Looked at her daughter's back," `09:478`; SIGMA's own message: "Your daughter's performance will be complete in 45 minutes," `09:211`; Ch 22: "her daughter who barely knew her anymore").
- **Why it matters**: These appendices exist to certify the book's precision for instructors; getting a principal character's child wrong, twice, in reference apparatus, undercuts exactly the authority the appendices claim.
- **Fix**: "her daughter Sam's school play" / "her daughter's play."
- **Severity**: HIGH. **Confidence**: high

### Finding: Concordance Ch 24 entry describes a scene cut from the manuscript
- **Location**: `chapters/34_appendix_concordance.tex:103`
- **Passage**: "Marcus lectures on Nagel's ``What Is It Like to Be a Bat?'' (1974) and the hard problem of consciousness (Chalmers, 1995)..."
- **Problem**: Printed Chapter 24 ("Leaving," file `chapters/25_leaving.tex`) contains no Marcus lecture; the Marcus teaching scene was cut in Wave 3 (Feb 2026); Marcus appears in the chapter only in passing memories (`25:12`). The Nagel/Chalmers material actually lives in file 11 (`11:37`, `11:167`) and file 18 (`18:343-355`), and Marcus's teaching survives only as one line at the gallery (`26:104`). The entry indexes a first-edition chapter that no longer exists.
- **Why it matters**: A concordance whose entry describes content not in that chapter fails at the one thing a concordance does. An instructor assigning "Chapter 24 + Nagel 1974" will find a handover chapter about a daughter and an ice-cream parlor.
- **Fix**: Rewrite the entry around what printed Ch 24 actually dramatizes (honest calibration as a values lesson, post-AGI texture, the handover); move the Nagel/hard-problem citations into the Ch 11 and/or Ch 17 entries, where the text supports them.
- **Severity**: HIGH. **Confidence**: high

### Finding: Concordance misattributes "We Were the Box" to Marcus
- **Location**: `chapters/34_appendix_concordance.tex:63`
- **Passage**: "...and Marcus writes the LessWrong post ``We Were the Box.''"
- **Problem**: In the manuscript the post is anonymous ("A LessWrong post titled *We Were the Box* dissected the transcript," `15:111`), and at that moment Marcus has disappeared, leaving only a note. The entry invents an authorship the text withholds and flattens a deliberate effect (the outside world naming the team's condition before the team does).
- **Fix**: "...and an anonymous LessWrong post, ``We Were the Box,'' names what the team couldn't."
- **Severity**: MEDIUM. **Confidence**: high

### Finding: Appendix A points MINERVA's announcement at chapters where MINERVA never appears
- **Location**: `chapters/32_appendix_timeline.tex:47` and the "MINERVA Crisis" headnote at `:60`
- **Problem**: MINERVA does not appear anywhere in printed Ch 19-20 (files 20/21: zero grep hits); the reader first meets MINERVA in printed Ch 21 (file 22). The chapter pointer sends readers to chapters that don't contain the event. (Full timeline analysis is the consistency-auditor's; flagged here as a reader-facing pointer defect.)
- **Severity**: LOW here (superseded by the consistency-auditor's HIGH). **Confidence**: medium

### Everything else in the new prose: clean
- **Part pages** (`parts/part1-3.tex`): all three epigraphs verified verbatim against source (`01:207`, `13:250`, `25:157`); attributions correct; well-chosen (Sam's line as the Part III epigraph is quietly excellent).
- **Appendix B** (`33_appendix_machine.tex`): the strongest new prose in the edition. Facts verified against the manuscript (Sofia asks the Policy question on Day 125; twenty-three minds at eight weeks; 197 days); the closing section ("The architecture was never the secret. There was no secret.") earns its cadence. No purple patches, no overreach; the refusal to specify consolidation is handled honestly. Note: the "147 days of consolidated interaction" line at `18:290` is *correct* for its Day-147 chapter and does not conflict with Appendix B's 197 (verified).
- **Appendix D** (`31_appendix.tex`): the "Since 2023" additions are factually careful (alignment faking, sleeper agents, ELK, SAE interpretability; FHI closure and Superalignment dissolution both handled with restraint; "It is worth staying modest about what this buys" is the right register).
- **Afterword** (`35_afterword.tex`): reads well; no purple prose; the Greenblatt et al. characterization is accurate; "twenty-five chapters" matches the printed count; the personal-research paragraph is the honest version of an author's-note claim.
- **Revised mind-crime passages**: Ch 11's new exchange (`11:802-808`) is in voice; Wei's counterargument is properly data-first and aphoristic ("A weather model doesn't rain."), Sofia gets her visualization tic subverted ("started to pull up the trace visualizations, then stopped"), Marcus keeps the self-interrupt ("every pruned branch is..." He stopped.). Ch 17's revision (`17:487`) inserts the conditional inside Marcus's line ("if the models inside those branches are rich enough to matter, and I can't tell you whether they are; nobody can"). The prediction-vs-instantiation question is **not resolved in either direction** in Ch 11, Ch 17, SIGMA's revised "Insight gained" line (`11:692`), Appendix C's cautions paragraph, or Appendix D's s-risk section. All five state it as open. Verified.

## Mechanical Defect Scan (changed .tex files)

- **Unescaped %**: none found (WP0's fix of `95\%` at `17:17` confirmed in the diff; Ch 15's bare % instances are inside verbatim environments, where they are literal).
- **Unicode**: only pre-existing, compiling instances (pinyin/Pali diacritics in Ch 8/9, "Godel" umlaut in Ch 15, all present at baseline; the WP9 em-dash fix is in). `The_Policy_print.tex` has multiplication/inequality glyphs in comments only; harmless.
- **Quote balance**: imbalances in Ch 9/12/17 are byte-identical to baseline (multi-paragraph speeches / nested quotes); pre-existing, not introduced. The Ch 26 missing open quote at Wei's Global Health line was fixed by the revision (`26:109`).
- The only introduced mechanical defects are the two `"X said."`-after-period fragments reported under Task 1(c).

## Strengths

The gloss-cutting pass is the rare large-scale deletion that made almost every seam stronger: Ch 1 ending on "Day 18 of the SIGMA Project.", Ch 5's section closing on "There was nothing more to say.", and the Ch 22 key-turning sequence all read better than baseline. The tag-thinning shows real editorial discrimination: the paired "Was it worth it?" asked-quietly echo in Ch 24 survived while forty-odd interchangeable tags died. Appendix B's "The Policy, Literally" section is the best two pages of new writing in the edition; it converts the title into mathematics without losing the dread. The Afterword's "the prose has been tightened throughout, mostly by trusting the reader" is, on the evidence of this audit, a claim the revision actually earned. Fix the two "said."-fragments and the appendix accuracy errors and this edition is craft-clean.
