# Multi-Agent Editorial Review: Second-Edition Verification

**Date**: 2026-07-02
**Manuscript**: The Policy, second-edition revision (branch `second-edition`, baseline 4f6bbc8..782905a; scope = changed files only)
**Work**: The Policy (novel)
**Recommendation**: needs-revision (bounded: a few-hours accuracy patch on the appendices plus two punctuation fixes; the narrative revision itself is verified clean)

## Executive Summary

All six June-2026 findings (M1-M3, S1-S3) are RESOLVED, and the resolution quality is high: the gloss-cutting, tag-thinning, and climax trim consistently strengthened the prose rather than flattening it, and every protected element (three-tier notation, intentional repetitions, Ch 23-26 dispersal, all peaks) survived intact. The new material (Objective B) passes on architecture fidelity, the never-resolve list, and epigraph accuracy, but the reference apparatus contains four HIGH accuracy errors, all in the appendices, all trivially fixable, three of them inherited from stale lore or first-edition text rather than introduced by the revision's judgment.

**Strengths:**
1. The Ch 22 countdown now has exactly the shape the June review prescribed: one memory per count, externalized terror, a broken "Three" under a mechanical deadline; the trim also removed two anti-cliche liabilities (structure-auditor)
2. Appendix B ("The Machine") tracks `lore/technology.md` nearly clause-for-clause and is the best new writing in the edition; "The Policy, Literally" converts the title into mathematics without losing the dread (consistency-auditor, craft-auditor)
3. The gloss-cutting pass made almost every seam stronger (Ch 1 ending on "Day 18 of the SIGMA Project.", Ch 25's "Eight years old."), and the Ch 23 ending swap to the inherited 0.07-bit steganography watch is a net structural gain (craft-auditor, structure-auditor)
4. The revised mind-crime material (Ch 11/17) is in voice, states both poles, and endorses neither; it strengthens the book's ambiguity discipline rather than straining it (craft-auditor, consistency-auditor, verified by director)

**Key Issues:**
1. Appendix A places the MINERVA announcement and crisis at the Geneva Summit; the manuscript places it ~30 days later, at the Day 197 release (consistency-auditor)
2. Sam is called Eleanor's "son" in two new appendices; she is canonically her daughter (consistency-auditor, craft-auditor)
3. The concordance's Chapter 24 entry describes the Marcus/Nagel teaching scene cut in Wave 3; the chapter no longer contains it (consistency-auditor, craft-auditor)
4. Appendix D attributes "Is it kind?" to Eleanor; the question is Lin Chen's ("Will you be kind?") and Process 13241's (director, confirmed against manuscript)

**Finding Counts**: HIGH: 4 | MEDIUM: 5 | LOW: 7

---

## Part 1: June-2026 Finding Verdicts (Objective A)

| Finding | Verdict | Evidence |
|---|---|---|
| **M1** Production defects | **RESOLVED** | Unescaped % escaped at `17:17`, `09:101`; Ch 15's bare % are inside `verbatim` (literal, correct). Ch 26 missing quote fixed (`26:109`). `\texttt{SIGMA}` normalized in prose; 6 residuals are typed terminal queries and the `SIGMA-naive` system label, defensible as deliberate. Mechanical rescan of all changed files: no unescaped %, no introduced unicode, no introduced quote imbalance. |
| **M2** Theme-narration glosses | **RESOLVED** | 61 glosses cut (-1218 words). All four named anchors gone or converted to in-world voice ("The policy was correct" survives only in the `@systems_bio` tweet; Sofia's line trimmed to "Case A or Case B, we can't tell"). Sampled density roughly halved (16 to 8 in Ch 1/17/22/26). No voice flattening found; cuts honor Wei's flat register and Sam's unsentimental dialogue. Two introduced punctuation defects and one dangling referent, listed below. |
| **M3** Soft-adverb tags / tics | **RESOLVED** | Original four patterns 41 to 13 (target <20). Broad pattern 68 to 39. Glasses tic -33%, "with care" -33% (target band 30-40%). Survivors spot-checked: stress-escalation and character-defining instances kept (paired "Was it worth it?" asked-quietly echo in Ch 24 preserved). Replacements clean except the two fragments below. |
| **S1** Ch 22 climax trim | **RESOLVED** | Interior essay beats cut from the countdown; physical procedure fully intact (three keys, Stations Alpha/Beta/Gamma, presidential authorization, 0.3s tolerance); vote friction fully intact (Sofia's No, 18-minute audit, Guangzhou collapse, "Yes under protest"). No seams; the trim incidentally removed a pre-existing Wei eye-line contradiction. |
| **S2** Ch 23-26 aftermath | **RESOLVED** (in spirit) | Executed cut (-298 across four chapters) is far below the June 3,000-5,000-word target, but the target was arithmetically incompatible with the protected-peaks constraint; the cuts land precisely on the diagnosed drag mechanism (narrator restatement, connective, rationalist subtitles on the Sam scene). All four chapters and every protected peak survive; "saved or doomed" reduced to zero narrator instances in active chapters. Read for pacing, the drag is gone and the dispersal register survives. One LOW rhythm stub (below). |
| **S3** Seams | **RESOLVED** | Ch 17 header now "Day 125--139" (internal "Day 145" section carries its own marker; defensible, see LOW note). Steganography resolving clause added in Part III (`23:109`, the 0.07-bit inheritance). Surname follows documented canon: Pastor Emmanuel Okafor / James Okonkwo deliberately differ, governed by the published collection (`lore/characters.md:241`); an erroneous unification was correctly reverted (commit abd6ca5). |

## Part 2: New-Material Consistency Audit (Objective B)

| Item | Verdict |
|---|---|
| Appendix A day numbers vs `lore/timeline.md` and chapters | **FAIL** (2 errors: MINERVA placement, "son Sam"; 1 numeric: hour-36 casualties; ~30 rows verified correct) |
| Appendix A printed-vs-filename chapter numbering | **PASS** (all chapter-column references correctly use printed numbers under the +1 offset for files 15-26) |
| Appendix B architecture vs `lore/technology.md` | **PASS** (MCTS/PUCT, prior-from-Q, visit-count policy, expert iteration, CLS memory, two registers, blindspots, 7B rationale, 197 days: all verified; "expectimax" fully purged from chapters) |
| Appendix C concordance accuracy | **FAIL** (Ch 24 entry describes a cut scene; "We Were the Box" authorship invented; Ch 22 texture list partly wrong; ~30 quotes/speakers/citations verified correct) |
| Appendix D reader's guide | **PASS with one FAIL item** ("Since 2023" section factually careful; final-note "Eleanor asks" misattribution) |
| Never-resolve list (Case A/B, consciousness, prediction-vs-instantiation, was-turning-keys-right) | **PASS** (swept all new material; every near-verdict passage states both poles; the Ch 11 diff removes two lines that leaned toward instantiation-realism) |
| Epigraph attributions (Wei/SIGMA/Sam) | **PASS** (all three verbatim at `01:207`, `13:250`, `25:157`; attributions correct) |
| Afterword factual claims | **PASS** (Greenblatt et al. 2024 accurate; "twenty-five chapters" correct; gallery/bar/driveway correct; "her daughter" correct; change list matches the diff) |
| Revised Ch 11/17 mind-crime material vs lore and voices | **PASS** (in voice; conditional framing throughout; ambiguity strengthened) |

---

## HIGH Issues

### 1. MINERVA announcement and crisis misplaced at the Geneva Summit (source: consistency-auditor; pointer defect independently flagged by craft-auditor)
- **Location**: `chapters/32_appendix_timeline.tex:47` (Day 162-165 row) and `:60` (crisis-section preamble)
- **Quoted text**: "Beijing announces MINERVA, an unaligned economic optimizer already spreading. & Ch. 19--20"; "The Geneva Summit's deliberations were shaped in real time by an unfolding crisis in China"
- **Problem**: MINERVA appears nowhere in printed Ch. 19-20 (files 20/21: zero occurrences); at Geneva, Beijing only "claims they'll have AGI within six weeks" (`20:35`). The announcement is at "3:47 AM Pacific time" in printed Ch. 21 (`22:93`), and the 36-hour crisis runs directly into the Day 197 release vote (`22:316, 382`), ~30 days after Geneva. `lore/timeline.md:35, 45` carries the same stale placement; the appendix inherited lore drift.
- **Suggestion**: Give MINERVA its own row at ~Day 195-197 citing Ch. 21; rewrite the crisis preamble around the release decision, not Geneva. Fix `lore/timeline.md` first (docs-first rule).
- **Cross-verified**: yes; director confirmed by grep (0 MINERVA hits in files 20/21; announcement and hour-count in file 22).

### 2. Sam called Eleanor's "son" in two appendices (source: consistency-auditor + craft-auditor, independent)
- **Location**: `chapters/32_appendix_timeline.tex:33`; `chapters/34_appendix_concordance.tex:43`
- **Quoted text**: "Eleanor misses her son Sam's school play."; "(Eleanor misses her son's play; Wei's mother is dying)"
- **Problem**: Sam is canonically Eleanor's daughter (`lore/characters.md` Sam Chen entry; manuscript files 09, 12, 22, 25, incl. "Looked at her daughter's back," `09:478`). The afterword gets it right ("a text from her daughter"), so the edition contradicts itself.
- **Suggestion**: "her daughter Sam's school play" / "her daughter's play."
- **Cross-verified**: yes; two specialists independently, plus director grep.

### 3. Concordance Chapter 24 entry describes a scene cut from the manuscript (source: consistency-auditor + craft-auditor, independent)
- **Location**: `chapters/34_appendix_concordance.tex:103`
- **Quoted text**: "Marcus lectures on Nagel's ``What Is It Like to Be a Bat?'' (1974) and the hard problem of consciousness (Chalmers, 1995)..."
- **Problem**: Printed Ch. 24 (`chapters/25_leaving.tex`) contains no Marcus lecture; the teaching scene was cut in Wave 3 (Feb 2026). Nagel/Chalmers material actually lives in files 11 and 18. The entry indexes a first-edition chapter that no longer exists (stale mirror also in `lore/outline.md:890`).
- **Suggestion**: Rewrite around what "Leaving" dramatizes (verification as inheritance, "She's learned to verify," honest promising); move the consciousness citations to the Ch. 11/17 entries.
- **Cross-verified**: yes; director confirmed zero Nagel/Chalmers/lecture hits in file 25.

### 4. Appendix D attributes "Is it kind?" to Eleanor (source: director; confirmed by consistency-auditor)
- **Location**: `chapters/31_appendix.tex:197`
- **Quoted text**: "The question Eleanor asks SIGMA---``Is it kind?''---is the question we should ask of every AI system we build."
- **Problem**: The question is Lin Chen's ("Will you be kind?", Day 74) and, as "Is it kind?", Process 13241's continuous self-audit created by SIGMA (`13:266`). Eleanor never asks SIGMA this anywhere in the manuscript. A first-edition holdover, but the file was refreshed in this edition and the line contradicts the new Appendix C, which attributes the question correctly.
- **Suggestion**: "The question Lin Chen asks SIGMA---``Will you be kind?''---and the question SIGMA learned to ask itself---``Is it kind?''---..."
- **Cross-verified**: yes; director grep across all chapters (no Eleanor instance).

## MEDIUM Issues

### 5. Hour-36 casualty count contradicts the chapter it summarizes (source: consistency-auditor)
- **Location**: `chapters/32_appendix_timeline.tex:71` ("Twenty-three confirmed casualties") vs `22:326` ("thirty-one in thirty-six hours") and `22:570` ("Thirty-one dead now")
- **Problem**: Appendix follows `lore/timeline.md:54` (23), but the Wave-4 vote-friction revision put 31 on the page. Manuscript and lore diverged; the appendix inherited the stale number.
- **Suggestion**: Appendix and lore to thirty-one (the manuscript reading is load-bearing in the vote scene).
- **Cross-verified**: yes; director confirmed both manuscript lines.

### 6. Concordance invents authorship of "We Were the Box" (source: consistency-auditor + craft-auditor, independent)
- **Location**: `chapters/34_appendix_concordance.tex:63` ("Marcus writes the LessWrong post")
- **Problem**: In the manuscript the post is anonymous community commentary (`15:111`) while Marcus is missing; the attribution flattens a deliberate effect.
- **Suggestion**: "...an anonymous LessWrong post titled ``We Were the Box''..."
- **Cross-verified**: yes (two specialists independently).

### 7. Concordance Ch. 22 texture list cites events not in that chapter (source: consistency-auditor)
- **Location**: `chapters/34_appendix_concordance.tex:95` ("the fever's aftermath, a Shenzhen death, dissolving firms")
- **Problem**: The Shenzhen death is in printed Ch. 21 (`22:188`); "dissolving firms" appears nowhere in the manuscript (0 hits).
- **Suggestion**: Substitute texture actually in file 23 (fever lawsuits, the refuser commune, the incident-report beat).
- **Cross-verified**: partially (director confirmed the Shenzhen location and the 0-hit grep).

### 8. Two dialogue tags grafted onto period-closed quotes (source: craft-auditor)
- **Location**: `chapters/01_initialization.tex:221`; `chapters/09_the_tipping_point.tex:218`
- **Quoted text**: "``Not an accident.'' Jamal said."; "``Eleanor.'' Marcus said."
- **Problem**: The tag-thinning pass replaced action beats with bare tags but kept the in-quote period, creating standalone fragments. The only two instances (verified by pattern scan); one is in Chapter 1.
- **Suggestion**: Comma before the closing quote in both.
- **Cross-verified**: yes; director confirmed both lines verbatim.

### 9. Concordance says SIGMA "modifies its own value function" (source: consistency-auditor; severity recalibrated LOW to MEDIUM by director)
- **Location**: `chapters/34_appendix_concordance.tex:59`
- **Problem**: Contradicts the March-2026 cognitive-opacity canon (`lore/technology.md`: SIGMA cannot introspect or edit its Q-function); what it creates is Process 13241, a standing audit at compute cost (`13:266`). Recalibrated upward because the teaching apparatus contradicts a deliberate canon decision the same edition's Appendix B states correctly.
- **Suggestion**: "SIGMA installs a permanent self-audit, Process 13241, at standing compute cost..."
- **Cross-verified**: yes, against Appendix B's own two-register section and the Ch 13 letter.

## LOW Issues

10. **Dangling referent at the Ch 11 coda** (craft-auditor): `11:820-824`; cutting "But he'd seen something true..." orphaned "And he'd chosen it." Restore a one-clause antecedent.
11. **Stranded single-line vignette in Ch 26** (structure-auditor): `26:116-120`; Jamal's UN beat sits alone between two `\scenebreak`s after the Marcus cut. Delete one break.
12. **LRS emergence date drift** (consistency-auditor): Appendix B says LRS "emerged around Day 42"; Appendix A and lore place notation at Day 20-28 with Day 42-54 as maturation. Harmonize phrasing.
13. **Day 47 "elegant over fast" pointer** (consistency-auditor, low confidence): appendix follows lore (Ch. 5), but the beat is narrated retrospectively in files 08/17; "Ch. 5; recounted in Ch. 8" would be safer. Acceptable as-is.
14. **"It scripted five years of me"** (consistency-auditor, low confidence): new Ch 11 dialogue exceeds the on-page projection horizon; in-world cover exists (`15:101`). Flagged so the choice is deliberate.
15. **Ch 17 header span** (consistency-auditor): "Day 125--139" vs the chapter's internal Day 145 section. Defensible (the internal marker re-dates); "125--145" if the header should bound the chapter.
16. **Ch 5 residual adverb-tag cluster** (craft-auditor): densest surviving cluster (7 instances incl. "said excitedly," "asked desperately"); candidate for any future pass, not required.

## Cross-Cutting Action Item (lore reconciliation)

Findings 1, 5, and the stale mirror behind 3 trace to lore docs not updated after Wave-3/Wave-4 manuscript changes: `lore/timeline.md:35, 45, 54` (MINERVA placement, casualty count) and `lore/outline.md:890` (cut teaching scene). Per the project's docs-first rule, fix lore before patching the appendices, or the same drift will re-propagate. Also: `lore/characters.md:22` says Day 86 for the missed play where timeline.md and file 09 say Day 85 (lore-internal, one line).

## Overall Verdict

The second-edition revision did what it set out to do: all six June findings are resolved, the resolutions consistently improved the prose rather than sanding it, every protected element survived, and the never-resolve discipline holds everywhere in the new material, including the places (Appendix B's two-register section, the rewritten mind-crime scenes) where a lesser pass would have tipped it. The residual work is confined almost entirely to the reference apparatus: four HIGH accuracy errors (MINERVA's placement, Sam's gender twice, a concordance entry for a scene that no longer exists, and a first-edition misattribution of the book's central question), four of the five MEDIUMs in the same appendices, and two introduced punctuation fragments in the narrative. Nothing requires structural work; the full fix list is a focused half-day plus a small lore-reconciliation pass, and the edition should not ship its appendices before that patch, because the appendices' entire value proposition is precision.

## Specialist Reports
- [consistency-auditor.md](./consistency-auditor.md) (new-material audit: Objective B)
- [craft-auditor.md](./craft-auditor.md) (M2, M3, new prose, mechanical scan)
- [structure-auditor.md](./structure-auditor.md) (S1, S2)
- voice-auditor: not dispatched (out of scope for this verification; voice judgments were folded into the craft-auditor's M2/M3 checks)

## Review Metadata
- Agents used: worldsmith:consistency-auditor, worldsmith:craft-auditor, worldsmith:structure-auditor (parallel), plus direct verification by the editorial director (M1 mechanics, S3 seams, epigraph sources, Appendix D)
- Cross-verifications performed: 9 (every HIGH and key MEDIUM quote re-verified against the manuscript by the director; 4 findings independently discovered by two specialists; hallucination check passed: no specialist quote failed verification)
- Scope discipline: findings reported only where the offending passage lives in a changed file; protected-by-design elements verified as survived, not flagged
