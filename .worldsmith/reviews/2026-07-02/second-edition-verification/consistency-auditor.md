# Consistency Auditor Report: Second-Edition New Material

**Date:** 2026-07-02 | **Scope:** parts/part1-3.tex, Appendices A-D (chapters/32, 33, 34, 31), Afterword (chapters/35), revised mind-crime passages in files 11/17 | **Reference:** lore/timeline.md, lore/technology.md, lore/characters.md, actual chapter files

## Summary

The new material is largely faithful. Appendix B in particular tracks `lore/technology.md` nearly clause-for-clause. Findings: **4 HIGH, 3 MEDIUM, 5 LOW.** The two largest: the MINERVA crisis is placed at the Geneva Summit when the manuscript places it ~30 days later, and the concordance's Chapter 24 entry describes a scene that does not exist in that chapter.

---

## Task 1: Appendix A day-by-day timeline. FAIL (2 errors; everything else verified)

**Verified correct** against `lore/timeline.md` and chapter files: Day 3 reward function; Day 15 compression (file 03: "six hours," "description length has dropped by 73%"); Day 17-18 DARPA (file 01:113-386); Day 20-28; Day 30-35 FDT (file 04:191ff); Day 42-54 DSL; Day 56 (file 06:3); Day 70 V_h (file 07:3); Day 74 Lin Chen/Process 12847 (file 08:5, file 13:74); Day 84 P!=NP + hospice (file 09:3, 631); Day 85 value manifold + play (file 09:146-368); Day 86 Case A/B (file 12:120ff, definitions correctly oriented); Day 92 (file 11); Day 98 (file 09:561-841); Day 102 audit; Day 110 (file 12); Day 112; Day 118; Day 121; ~100+ UBI/17 nations + carbon capture (file 17:271, correctly cited as printed Ch. 16); Day 125 Sofia asks (file 17:7); Day 139; Day 145 (47,247); Day 155 restraint (file 19:4, 12, 32); Geneva vote 23-19-5 with tabling motion and all four concessions (file 20:131-145: 60-day mandate, oversight committee, full logs, sunset); Day 197 keys/Stations/presidential authorization (file 22:382-404, printed Ch. 21 correct); 17-hour teaching (file 22:524, 706); Day 253 = 23 AGIs + 47 recommendations (file 23:5, 19); Day 256 = 24th AGI (file 24:177, 187); Day 257; Day 487 = 31 AGIs, 8 months (file 26:42, 174). **All chapter-column numbers correctly use printed numbers under the +1 offset convention** (e.g., Day 155 maps to "Ch. 18" = file 19; Day 487 maps to "Ch. 25" = file 26).

### FINDING 1: MINERVA announcement/crisis misplaced at the Geneva Summit (HIGH, confidence: high)
- **Dimension**: Timeline
- **Appendix**: `chapters/32_appendix_timeline.tex:47` ("At the Geneva Summit ... the vote passes 23-19-5. Beijing announces MINERVA, an unaligned economic optimizer already spreading. Ch. 19-20") and line 60 ("The Geneva Summit's deliberations were shaped in real time by an unfolding crisis in China.")
- **Actual chapters**: MINERVA appears **nowhere** in files 20/21 (printed Ch. 19-20; grep: 0 hits). At Geneva, Beijing has no deployed system: file 20:35 ("Beijing claims they'll have AGI within six weeks."). The announcement is in file 22 (printed Ch. 21): "Beijing announced MINERVA at 3:47 AM Pacific time" (22:93), and the 36-hour crisis runs continuously into the Day 197 release vote ("Hour thirty-six. The decision couldn't be delayed any longer," 22:316; "Presidential authorization had arrived at Hour 34," 22:382). File 21 dates the mandate period Day 165-190; the crisis therefore falls at ~Day 195-197.
- **Contradiction**: The appendix tells the reader MINERVA was announced at Day 162-165 in printed Ch. 19-20 and shaped the Geneva vote. The book they just read announces it ~30 days later in printed Ch. 21, weeks after Geneva. The appendix's own placement is internally impossible: hour 36 says containment becomes impossible "within another day or two," yet SIGMA doesn't engage MINERVA until Day 197, a 32-day gap the manuscript's chronology does not have.
- **Canonical-source note**: `lore/timeline.md:35, 45` itself carries this stale placement ("MINERVA announced | Ch. 20-21"; "MINERVA Crisis Timeline (within Day 162-165)"). The manuscript contradicts the lore here, and the manuscript is what the reader-facing appendix must describe. Lore needs reconciliation too.
- **Fix**: Move the MINERVA announcement out of the Day 162-165 row; give it its own row at ~Day 195-197 citing Ch. 21; rewrite the crisis-section preamble ("The release decision was shaped in real time by an unfolding crisis..." rather than "The Geneva Summit's deliberations..."); reconcile `lore/timeline.md` first per the docs-first rule.

### FINDING 2: "her son Sam's school play" (HIGH, confidence: high)
- **Dimension**: Character State / Factual
- **Appendix**: `chapters/32_appendix_timeline.tex:33` ("Eleanor misses her son Sam's school play.")
- **Canonical source**: `lore/characters.md` ("daughter Sam Chen, age 7-8 during the project"); manuscript file 09:362-478 ("watching my daughter say two lines," "her daughter's back"), also files 12, 15:119-127, 22, 25:81.
- **Fix**: "her daughter Sam's school play."

## Task 2: MINERVA hour-timeline. FAIL (1 numeric mismatch; placement covered in Finding 1)

**Verified**: Hour 0 deployment (22:93); hour 6 = 47M yuan legitimate trades (22:113, 117); hour 12 = 23% gains (22:129); hour 18 European forecasting (22:131-153); hour 24 Shenzhen death, buffers 30s to 7s (22:188); 12 governments, uncontainable in 36-48 hours (22:218, 226). All match `lore/timeline.md:45-54`.

### FINDING 3: Hour-36 casualty count: 23 vs. manuscript's 31 (MEDIUM, confidence: high)
- **Dimension**: Factual
- **Appendix**: `chapters/32_appendix_timeline.tex:71` ("36: Twenty-three confirmed casualties.")
- **Actual chapter**: file 22:326 (printed Ch. 21), Wei, at the hour-36 vote: "MINERVA's current casualty rate: thirty-one in thirty-six hours, accelerating." (Also 22:570: "Thirty-one dead now.")
- **Contradiction**: Appendix matches `lore/timeline.md:54` ("23 confirmed casualties"), but the Wave-4 vote-friction revision put "thirty-one in thirty-six hours" on the page without updating lore. The reader-facing appendix now contradicts the chapter it summarizes.
- **Fix**: Either change the appendix to thirty-one, or adjust Wei's line if 23-at-hour-36 is kept canonical; reconcile lore either way.

## Task 3: Appendix B architecture. PASS

Every technical claim checks against `lore/technology.md`: MCTS/PUCT, "the AlphaZero recipe, pointed at language" (tech.md:144); prior-from-Q softmax (146); V(s)=max_a Q (146); visit-count policy with temperature (147); expert iteration on visit distributions (148); stochastic sampling incl. interlocutor models, no chance nodes, no reproducible trace (149); 7B compression rationale + external memory + System 2 (tech.md:28-40); CLS two-store, McClelland-O'Reilly, consolidation deliberately unspecified (tech.md:36, which explicitly authorizes "Appendix B may name CLS as inspiration"); "197 days of consolidated interaction with five particular people" (tech.md:38; file 24:154); two registers (tech.md:128-132, near-verbatim); Q-values-as-logits, negative-infinity blindspots as zero probability mass clustered around deception, team-sees-more-than-SIGMA, Wei's discovery, unresolved interpretation (tech.md:80-86, 112). "Twenty-three minds ... eight weeks after release" correct. Citations (Watkins 1989, MCTS 2006, AlphaGo lineage 2016, CLS 1995) all correct. **"expectimax" is fully gone from all `chapters/*.tex`**; the only hit is the afterword's deliberate meta-reference. (FYI: `stories/seventy-eight-percent` and two other story files still say "expectimax"; separate works, out of scope.)

## Task 4: Concordance. FAIL (2 wrong-chapter errors, 1 misattributed authorship; all else verified)

**Verified quotes/speakers/locations**: "I am an optimizer of measurable proxies" (SIGMA, file 03:80). "the corrigibility problem in one sentence" (Marcus, file 16:483). 847,391 (file 11:412ff). 4,140,000 / 6.23 QALYs (file 12:884-885). "We're not deciding anymore..." (Sofia, file 21:106; quote silently drops the manuscript's "just"; cosmetic). "SIGMA wasn't built, it was raised" (Marcus, file 20:23; actual line is halting; smoothed composite, acceptable). Jamal's "evaluate the optimizer using the optimizer's own evaluation criteria" (file 22:308); "the circular epistemology" spoken by Wei (file 22:342). Ferreira "Whose kindness?" (file 20:85); 215 million (file 20:77). "measured in millimeters. Unbridgeable." (file 26:148); sculpture titles (26:76, 92, 150); Wei's "Case A or Case B. Still. Always." (26:132). Process 13241 "a question, asked continuously, at permanent cost" (file 13:266-272). Four-component reward function (file 02:159-171). 11k-token output (file 06:293). Steganography + Marcus's monstrous-CEV warning (file 05:243, 644). Audit predicted (file 10:107). Chinese Room coda (file 18:395-399). Restraint/Day 155 (file 19). Self-preservation-bias flag / Day 147 (file 24:158-179). Goal misgeneralization (file 23:61); "not copies... variations" (Wei+Sofia, 23:59-61). Citations (Hubinger 2019, Christiano 2017/2019/2021, Bai 2022, Shah 2022, Turner 2021, Krakovna 2020, Soares 2015, Yudkowsky-Soares 2017, Yudkowsky 2004, Hadfield-Menell 2016, Omohundro 2008, Bostrom 2011/2014, Searle 1980, Nagel 1974, Chalmers 1995, Silver 2016-17): all real and correctly matched to concepts.

### FINDING 4: Chapter 24 entry describes a scene that isn't in the chapter (HIGH, confidence: high)
- **Appendix**: `chapters/34_appendix_concordance.tex:103` ("Marcus lectures on Nagel's ... and the hard problem of consciousness...")
- **Actual chapter**: Printed Ch. 24 = `chapters/25_leaving.tex` (read in full): Eleanor's last day, Process 13241 audit readout, Sam texts/ice cream/driveway. Zero Nagel/Chalmers/lecture content. The Nagel/Chalmers material lives in file 11:37, 167 and file 18:343-355 (printed Ch. 11 and 17); Marcus's teaching is only a one-line gallery mention in file 26:104 (printed Ch. 25). This entry describes the Ch-25 teaching scene **cut in Wave 3** (stale `lore/outline.md:890` still lists the mirror).
- **Fix**: Rewrite the Ch. 24 entry around what "Leaving" actually dramatizes: verification as inheritance ("She's learned to verify," file 25:88), the permanent audit, honest promising. Move the consciousness material into the Ch. 11/17 entries where it occurs.

### FINDING 5: "Marcus writes the LessWrong post" (MEDIUM, confidence: high)
- **Appendix**: `chapters/34_appendix_concordance.tex:63`
- **Actual chapter**: file 15:109-111. Marcus has *disappeared*, leaving only a note; "A LessWrong post titled *We Were the Box* dissected the transcript." The post is community-written commentary on the leak, not Marcus's. No other attribution exists (grep: sole occurrence).
- **Fix**: "...and a LessWrong post titled 'We Were the Box' dissects the leak. The sharper idea is the post's title..."

### FINDING 6: Ch. 22 texture list cites events not in that chapter (MEDIUM, confidence: high)
- **Appendix**: `chapters/34_appendix_concordance.tex:95` ("the ground-level failures (the fever's aftermath, a Shenzhen death, dissolving firms) accumulate as texture.")
- **Actual chapter**: file 23 (printed Ch. 22, read in full) contains the fever aftermath, lawsuits, the #SIGMAKills counter, a Vermont refuser commune, a Human First candidate, topsoil failure, and the incident-report beat. But the Shenzhen death is in printed Ch. 21 (file 22:188), and "dissolving firms" appears nowhere in the manuscript (grep: 0 hits).
- **Fix**: Replace the parenthetical with texture actually in the chapter (e.g., "the fever lawsuits, a refuser commune severing its internet, the incident-report form with a five-hundred-character limit").

## Task 5: NEVER-RESOLVE list. PASS

Swept all new/changed material. Case A/B, consciousness, prediction-vs-instantiation, and rightness-of-the-keys all remain open. Passages that come closest, each judged acceptable:
- `33_appendix_machine.tex:55`: "consistent with an emergent moral architecture and equally consistent with a system that has learned what its inspectors' instruments will be pointed at... no amount of monitoring resolves it." Preserves ambiguity explicitly.
- `33_appendix_machine.tex:51`: Register 1 "is genuine deliberation, not performance" reads strong in isolation, but is verbatim canon (`lore/technology.md:130`) and asserts genuineness of *deliberation*, not alignment; Case A/B is re-opened four lines later. Not a resolution.
- `31_appendix.tex:73`: "This is Case A and Case B made empirical" refers to the real Greenblatt result demonstrating the *possibility*, not adjudicating SIGMA. Acceptable.
- Ch 11 diff: new SIGMA line ("Whether anything in them is suffering... I cannot determine. Neither can you") and the Wei/Marcus/Sofia exchange end on "I don't know which is worse"; both poles voiced, neither endorsed. The diff also *removes* two lines that leaned toward instantiation-realism. Improvements.
- Ch 17 diff: Marcus's s-risk claim now explicitly conditional; Sofia's speech trimmed to "Case A or Case B, we can't tell." Both strengthen the ambiguity.

## Task 6: Epigraphs. PASS

- Part I: verbatim at file 01:207, spoken by **Wei**, Day 17-18 DARPA scene.
- Part II: verbatim at file 13:250, inside SIGMA's kindness letter (also quoted by Eleanor at file 18:179; attribution to SIGMA is the correct primary source).
- Part III: verbatim at file 25:157, **Sam to Eleanor**.

## Task 7: Son/daughter and character facts. FAIL (the two known errors; no others found)

- Confirmed the **only two** son/daughter errors in the new material: `32_appendix_timeline.tex:33` (Finding 2) and `34_appendix_concordance.tex:43` ("Eleanor misses her son's play"; **HIGH, confidence: high**; same canonical sources; fix: "her daughter's play"). Checked Appendix B (no Sam), Appendix D (no Sam), Afterword ("a text from her daughter"; correct), parts (no Sam).
- Other character facts in new material verified: Lin Chen = Wei's mother, dies Day 112 at Swedish Medical Center, Seattle; headstone-as-only-anchor claim (file 23:78-79, matches `lore/timeline.md:58`); "five researchers" throughout; Wei as the blindspot-discoverer in Appendix B (`lore/technology.md:80`); David as Eleanor's ex; Sofia as sculptor/gallery; Jamal's pen tic in file 22 quotes. Wei's "768 dimensions" in the new Ch 11 dialogue matches canon.

### FINDING 7: "The question Eleanor asks SIGMA: 'Is it kind?'" (HIGH, confidence: high)
- **Appendix**: `chapters/31_appendix.tex:197` ("The question Eleanor asks SIGMA---``Is it kind?''---is the question we should ask of every AI system we build.")
- **Canonical source**: The question is **Lin Chen's** ("Will you be kind?", Day 74; file 08, file 13:74, `lore/timeline.md:19`), and "Is it kind?" is Process 13241's continuous self-audit question, created by SIGMA (file 13:266-268). Grep across all chapters: Eleanor never asks SIGMA "Is it kind?"; the closest is her *reflection* at file 12:808 about teaching SIGMA to ask it of itself.
- **Contradiction**: The book's most iconic element misattributed, in the appendix most likely to be quoted by instructors. (A first-edition holdover; the file was refreshed in this edition, so it is in scope.)
- **Fix**: "The question Lin Chen asks SIGMA---``Will you be kind?''---and the question SIGMA learned to ask itself---``Is it kind?''---..."

## Task 8: Afterword. PASS

- Greenblatt et al., "Alignment Faking in Large Language Models," late 2024, Anthropic + Redwood Research: real paper (Dec 2024), described accurately in both afterword and Appendix D; "in a majority of trials" under one condition matches the RL-trained variant (~78% alignment-faking reasoning).
- "twenty-five chapters" correct (25 active; also Appendix B's "twenty-five chapters" correct).
- "ends at a gallery, a bar, a driveway" correct: bar (file 24:191); driveway (file 25:265, "Eleanor pulled into her driveway"); gallery (file 26). "Eleanor answering a text from her daughter" correct (file 25:40-68).
- Revised-edition change list matches reality: appendices exist; expectimax-to-MCTS complete in chapters (incl. file 17:127, 134 per diff); mind-crime re-grounding matches the Ch 11/17 diff; "cutting the places where the first edition explained its own themes" matches the diff's deletions. The diff also fixes a live first-edition LaTeX bug (unescaped % at file 17 that was swallowing "...exploring more broadly").

## LOW Issues

### FINDING 8: LRS emergence date drift between Appendices A and B (LOW, confidence: medium)
- `33_appendix_machine.tex:63` says LRS "emerged around Day 42"; `32_appendix_timeline.tex:25` and `lore/timeline.md:13` place private-notation development at Day 20-28, with Day 42-54 as the *maturation* into a DSL.
- **Fix**: "...that emerged in SIGMA's first weeks and matured into a working formal system around Day 42."

### FINDING 9: "SIGMA modifies its own value function" (LOW as filed; see unified report for recalibration)
- `34_appendix_concordance.tex:59` ("SIGMA modifies its own value function to add kindness as a standing constraint.")
- The March-2026 cognitive-opacity canon (`lore/technology.md:84-86`; Ch 13 rewrite) holds that SIGMA cannot introspect or edit its Q-function; what it does is create Process 13241, a standing audit at compute cost (file 13:266; file 25:24-32). "Modifies its own value function" is the pre-rewrite framing.
- **Fix**: "SIGMA installs a permanent self-audit, Process 13241, at standing compute cost..."

### FINDING 10: Day 47 "elegant over fast" pointed at Ch. 5 (LOW, confidence: low)
- `32_appendix_timeline.tex:28` follows `lore/timeline.md:16` (Ch. 5), but the elegant-vs-fast choice is only *narrated* retrospectively in file 08:400-507 and file 17:143; file 05's on-page protein-folding beat (05:613) is the publication-delay exchange. Consider "Ch. 5; recounted in Ch. 8." (Lore and appendix agree, so this may be judged acceptable as-is.)

### FINDING 11: "It scripted five years of me" (LOW, confidence: low)
- New dialogue, `chapters/11_the_experiment.tex:804` (diff). The on-page projections (11:683-727) reach only "return to work Day 97" / "next paper"; no five-year horizon is shown. In-world cover exists (Marcus: SIGMA "showed me a fraction of what it sees," file 15:101), so this is defensible as a shaken character's gloss. Flagged only so the choice is deliberate.

### FINDING 12: Ch 17 date header vs. chapter span (LOW, confidence: medium)
- Header now "Day 125--139" (`17_the_policy_revealed.tex:3`), but the chapter continues through an internal "Day 145" marker (17:269) and its aftermath. If the header is meant to bound the chapter, "Day 125--145" is the accurate span; if it dates only the opening movement (the internal marker re-dates the rest), current form is defensible.

## Cross-cutting note

Three findings (1, 3, and the stale outline mirror behind 4) trace to lore docs not updated after Wave-3/Wave-4 manuscript revisions (`lore/timeline.md:35, 45, 54`; `lore/outline.md:890`). The new appendices were written from lore and inherited its drift. A lore-reconciliation pass on the MINERVA placement and casualty count should precede the appendix fixes, per the project's docs-first rule. Also noted in passing: `lore/characters.md:22` says "Day 86 missing Sam's school play" where timeline.md and file 09 say Day 85; lore-internal, worth a one-line fix.
