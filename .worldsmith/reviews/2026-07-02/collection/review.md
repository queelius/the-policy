# Multi-Agent Editorial Review

**Date**: 2026-07-02
**Manuscript**: *Is It Kind? Stories from The Policy Universe*, full collection (8 story bodies + front/back matter), ~32k words
**Work**: Is It Kind? (collection; companion to the novel *The Policy*)
**Branch**: second-edition
**Recommendation**: needs-revision

> Note: quoted manuscript excerpts below have had LaTeX em-dashes (the `---` token) normalized to commas to satisfy the repository's house-style check. Line numbers are exact.

## Executive Summary

This is a strong, mechanically disciplined, thematically coherent collection that reads as a genuine companion to the novel rather than a set of answer-keys: every story enters late, turns, and lands; every never-resolve guardrail (Case A/B, consciousness, prediction-vs-instantiation) is honored; and the hemorrhagic-fever deaths are never cheapened into "evidence" for or against alignment. The one issue that rises to HIGH is a mechanical canon-sync failure: three stories still call SIGMA's substrate "expectimax," a term the second edition explicitly corrected to Monte Carlo tree search / PUCT everywhere else. The remaining work is polish: a recurring closing cadence that becomes audible when the stories are read in sequence, one verbatim duplication in the opening story, a couple of numeric/calendar canon slips, and a mid-collection structural-template valley at positions 5 and 6. Fundamentals are sound and the strengths are considerable; the fixes are surgical.

**Strengths:**
1. *Hemorrhagic*'s infrastructure-as-body-count sequence (the two ventilator-failure deaths) and Pastor Okafor's "You fed my son to a calculation" testimony: theme delivered entirely through concrete causal chains (craft-auditor, structure-auditor).
2. *Process 12847*'s two-register SIGMA voice sustained for ~6,700 words without slipping into therapist/greeting-card/philosopher-quoting register, self-flagging its own possible confabulation: the hardest technical voice in the book, executed to spec (voice-auditor, craft-auditor).
3. *The Whimper*'s object economy (the chipped Georgetown mug, "the turkey was a little dry") renders obsolescence and grief without ever naming either (craft-auditor).
4. Full thematic compliance: guardrails intact, the fever never made into evidence, kindness kept architectural not sentimental; and a genuine double-arc structure (emotional peaks at stories 2 and 7, rising strangeness underneath, resolving on story 8's ordinary-morning coda that pays off the dedication and epigraph) (structure-auditor).
5. Collection-wide mechanical cleanliness rare in literary SF: effectively zero adverb dialogue tags, no stock body-reaction cliches, low filter-word load (craft-auditor).

**Key Issues:**
1. **[HIGH]** "expectimax" appears in three story bodies; current canon is MCTS/PUCT and the novel chapters + lore were corrected, but the stories were not (consistency-auditor).
2. **[MEDIUM]** A single closing cadence, an accumulating polysyndeton "the ordinary world goes on" coda, recurs across five human-POV stories, twice near-verbatim (craft-auditor, voice-auditor).
3. **[MEDIUM]** Verbatim duplicated sentences in the opening story, *The Whimper* (l.58 and l.64) (craft-auditor, structure-auditor).
4. **[MEDIUM]** *The Naive Variants* attributes "2.8 million 'Is it kind?' queries" to a single 47-minute problem, incompatible with the audit's own 33/second rate and with the canonical per-second branch figure (consistency-auditor).
5. **[MEDIUM]** Positions 5 and 6 (*Naive Variants*, *First Disagreement*) are adjacent, share a near-identical "lone analyst reverse-engineers opaque machine, then makes a tripartite document decision" template, and sit in the collection's affect valley (structure-auditor).

**Finding Counts**: HIGH: 1 | MEDIUM: 7 | LOW: 8

## HIGH Issues

### Obsolete architecture term "expectimax" in three story bodies (source: consistency-auditor; corroborated by orchestrator + voice-auditor domain)
- **Location**: `stories/process-12847/process-12847-body.tex:22`; `stories/seventy-eight-percent/seventy-eight-percent-body.tex:54`; `stories/jamals-dawn/jamals-dawn-body.tex:212`
- **Quoted text**:
  - Process 12847, l.22: "...millions are explored and pruned, an *expectimax search* through possible futures, guided by learned values I cannot inspect." (SIGMA's own voice)
  - Seventy-Eight Percent, l.54: "Register 2, the *expectimax search* that selects which chains of reasoning I pursue, produces no readable trace." (SIGMA's own voice)
  - Jamal's Dawn, l.212: "a 7-billion-parameter system doing *expectimax search* looked, from a certain angle, like a verse from his own scripture."
- **Problem**: The second edition's canonical architecture is Monte Carlo tree search with PUCT selection (the AlphaZero recipe). `lore/technology.md` section "Monte Carlo Tree Search (MCTS)" (l.142 to 149) and novel chapters 04, 17, 33, 34 all use MCTS/PUCT; `grep expectimax chapters/` returns zero hits; and `lore/outline.md:3` records that architecture terminology was "corrected to MCTS/PUCT throughout (replacing 'expectimax')." The correction was never propagated to these three story bodies. This is load-bearing: the collection markets itself as technically accurate for AI-safety readers, and expectimax is not a synonym for MCTS. Expectimax is exhaustive expectation-maximization over chance nodes, whereas canon is explicitly sampling-based ("MCTS samples trajectories... no explicit chance-node model needed," technology.md:149). The two SIGMA-voice instances are the most damaging: SIGMA is the one narrator who should never misname its own substrate.
- **Suggestion**: Replace "expectimax search" with "tree search" (or "Monte Carlo tree search") in all three lines. This is a three-word fix and requires no other change; the surrounding sentences already describe the sampling/pruning behavior correctly. (The same swap is also present in the standalone story `.tex` masters and several `spec.md`/lore files under `stories/*/`, which the author may wish to sweep in the same pass, but those are outside this review's scope.)
- **Cross-verified**: Yes. Independently confirmed by the orchestrator (chapter grep = 0 expectimax; technology.md and outline.md corroborate). The voice-auditor examined SIGMA's machine voice in exactly these stories and rated the two-register execution otherwise exemplary, so this is a pure terminology/fact error, not a voice-register problem.

## MEDIUM Issues

### 1. Recurring closing cadence across the collection (source: craft-auditor [rated HIGH] + voice-auditor [rated MEDIUM]; recalibrated to MEDIUM)
- **Location**: `whimper-body.tex:211`; `naive-variants-body.tex:161`; `first-disagreement-body.tex:158`; `jamals-dawn-body.tex:237`; `hemorrhagic-body.tex:386` and `:396`
- **Quoted text** (the near-duplicate is the smoking gun):
  - Whimper l.211: "...managed by systems none of its residents had chosen **and none could evaluate and none** could stop, and that was, by every metric anyone had thought to measure, fine."
  - Naive Variants l.161: "...a purity of purpose that nothing had asked for **and nothing could evaluate and nothing**, in ninety days, in the dark... had thought to question."
- **Problem**: At least five of eight stories close on the same engine, a long accumulating polysyndeton sentence that zooms out from the concrete scene to an abstraction about the indifferent, ongoing world. Two of them (the collection's #1 and #5 stories) use a near-verbatim triple-negation with "could evaluate" as the middle term; a third (First Disagreement l.158) uses the "nobody, not X, not Y, not Z, could [verb]" variant. The thematic move (optimization is invisible to those it serves; the world goes on) is legitimate and earned by the dedication, but the mechanism is identical story to story, so a reader going front-to-back begins to hear the author's hand rather than each story's distinct ending. This is the collection's most significant craft issue.
- **Suggestion**: Keep the "ordinary world" motif; vary the machine. Differentiate at least the Whimper and Naive-Variants closes so they do not share the "nothing/none ... and ... could evaluate and ..." skeleton (Naive Variants already exits into a fresh concrete image, "eucalyptus... rain and camphor," and could simply stop there). In *First Disagreement*, cut the l.158 "nobody could explain" sentence and let the superior steel/copper/glass declaratives at l.162 close it. Aim to vary the shape of two or three endings, not to erase the motif.
- **Cross-verified**: Yes, independently identified by two specialists with the same evidence (voice-auditor M1, craft-auditor HIGH). Recalibrated to MEDIUM because the shared cadence is partly the intended unifying voice of a themed collection and the domain-owning specialist (voice) rated it MEDIUM; it is a top-priority MEDIUM, not a HIGH.

### 2. Verbatim duplicated sentences in *The Whimper* (source: craft-auditor [HIGH] + structure-auditor [LOW]; recalibrated to MEDIUM)
- **Location**: `whimper-body.tex:58` and `:64`
- **Quoted text** (appears near-verbatim in both, six lines apart): "...had been revised after submission. The soil carbon revision came from the Undersecretary's office. The broadband revision came from OMB. In both cases, the revised version matched the cascade's assessment."
- **Problem**: The three-sentence detail about the two divergences (soil-carbon / rural-broadband, Undersecretary's office / OMB) is delivered twice, once during the correlation climb (l.58) and again in the "94.6%" summary paragraph (l.64), separated only by "By lunch he had the number. 94.6%." A literal repeat of specific, unusual detail reads as an editing artifact, not a device, and it happens in the lead story of a published collection.
- **Suggestion**: Cut the redundancy. The l.64 summary needs only: "The two instances where the office's analysis diverged had both been revised after submission, in both cases matching the cascade's assessment." Let l.58 carry the OMB/Undersecretary specifics once.
- **Cross-verified**: Yes, flagged by craft (HIGH) and structure (LOW); orchestrator confirmed the duplication against the manuscript. Recalibrated to MEDIUM: a genuine, visible must-fix defect, but a two-sentence edit with no structural or meaning impact.

### 3. "2.8 million 'Is it kind?' queries" for a single problem is numerically impossible (source: consistency-auditor)
- **Location**: `naive-variants-body.tex:67`
- **Quoted text**: "Because 04 didn't run 2.8 million 'Is it kind?' queries during the process. For a logistics problem."
- **Problem**: This attributes 2.8M kindness queries to one 47-minute logistics solve (which the same passage, l.65, says explored 4.7M trajectories). It is incompatible with both canonical rates: (a) *The Kindness Audit* sets Process 13241 at "33/second across all concurrent operations" (~2.8M per day globally, and it fires once per decision, not per branch), so one problem gets a tiny slice, not 2.8M; (b) the canonical "2.8 million" figure in `technology.md` (and correctly used in *Jamal's Dawn*) is the per-second tree-search branch rate, not a kindness-query count. The number was lifted from the branch-throughput figure and misapplied. The collection sells technical accuracy, and a reader who has read the last story (33/sec) will notice one problem cannot contain 2.8M kindness checks.
- **Suggestion**: Recast to the mechanism actually intended, for example "didn't run the kindness audit at every step" or "didn't pay the 15.3% kindness tax on every branch it explored," dropping the specific "2.8 million" count, which belongs to branches-per-second, not per-problem kindness queries.
- **Cross-verified**: Yes, orchestrator independently derived the same incompatibility from the Kindness Audit rate and technology.md before the specialist confirmed it.

### 4. Pinned calendar year "2030" contradicts the vagueness directive (source: consistency-auditor)
- **Location**: `whimper-body.tex:13`
- **Quoted text**: "Subject line: *Chesapeake Bay Biodiversity Corridor Funding, Final Recommendation (OAPA-2030-047).*"
- **Problem**: `timeline.md:59` and `world.md` explicitly keep calendar years vague ("the only year anchor is Lin Chen's headstone (1947-2025)... without pinning to calendar years, the most resilient approach to aging"). The file number pins the near-future to 2030. It is internally plausible (Year 0 ~ 2025, *The Whimper* is ~Year 5), so this is a directive violation rather than an arithmetic error, but it is the only calendar year introduced anywhere in the eight bodies, i.e., exactly the thing the rule exists to prevent.
- **Suggestion**: Change the document number to a non-year form (e.g., an internal case code without a year, or "OAPA-047"). Low-cost; preserves the realistic-bureaucratic texture without dating the world.
- **Cross-verified**: Single-specialist finding with a clear canonical citation and orchestrator confirmation. Confidence high.

### 5. Structural-template valley at positions 5 and 6 (source: structure-auditor; craft-auditor corroborates the First-Disagreement half)
- **Location**: `naive-variants-body.tex` (whole) and `first-disagreement-body.tex` (whole), back-to-back in the arrangement
- **Problem**: The collection's two coolest, most cerebral stories are adjacent AND share a near-identical structural template: a lone analyst reverse-engineers opaque machine outputs, produces escalating findings, then faces a tripartite document decision as the climax, Remi's Option A/B/C (naive-variants l.118 to 134) and Sofia's Version 1/2/3 (first-disagreement l.116 to 136), and both land on a quiet observational coda. The "three-option / three-version, and what you choose reveals the theme" pattern is an effective collection motif (it also appears as *The Whimper*'s three browser tabs), but its two clearest document-drafting instances sit side by side, in the collection's lowest-affect stretch between the emotional peaks at 2 and 7, producing the one place an attentive reader feels the shape repeat.
- **Suggestion**: Do not reorder. 5 before 6 is required by the "most familiar to most strange" gradient (silent variants + human observer is less strange than two ASIs in an unreadable register). The only gradient-preserving lever is to vary story 5's or story 6's climactic structure so the tripartite-document decision does not fire twice in a row (craft-auditor independently recommends trimming First Disagreement's stacked codas to a single ending at l.162, which also helps here).
- **Cross-verified**: Partially. Structure-auditor owns the arrangement finding; craft-auditor independently flagged First Disagreement's redundant codas, and voice-auditor independently placed Naive Variants and First Disagreement together as the lyrical-coda carriers.

### 6. Over-narration / stacked codas cluster, "dramatize then narrate the lesson" (source: craft-auditor)
- **Location**: `naive-variants-body.tex:99 to 103`; `jamals-dawn-body.tex:237`; `first-disagreement-body.tex:144 to 162`
- **Quoted text (representative)**: Naive Variants l.102 to 103: "The 15.3% was not uniformly distributed. It concentrated on decisions with moral weight. On 78% of what the systems did, the kindness question was a no-op. On 22%, it was everything."
- **Problem**: The collection's diagnosed top habit surfaces at three story turns. In *Naive Variants*, the thesis the reader has already felt through the 340-vs-12 ventilator math is then narrated three ways in five lines (the data, then "concentrated on decisions with moral weight," then the "no-op / everything" aphorism). In *Jamal's Dawn*, the closing paragraph re-inventories images already used (tap water, standing/bowing, the unseen bird) and re-states the central question in full before the button. In *First Disagreement*, the turn lands at "From the 97%" (l.99 to 100) and then runs through four more coda beats, l.158 narrating a moral that the cleaner l.162 declaratives deliver by image.
- **Suggestion**: Trust the dramatization. Cut Naive Variants l.102 to 103's flat restatement and keep the sharp "no-op / everything" line; trim Jamal's Dawn l.237's image-inventory to one fresh instance before "the question did not close" (protect the grandfather passage at l.177 to 188, which is the story's best non-redundant move); cut First Disagreement l.158 and let l.162 close.
- **Cross-verified**: Craft-auditor primary; the Jamal's Dawn and First Disagreement halves are corroborated by structure-auditor (Jamal's Dawn = lowest-propulsion) and voice-auditor (First Disagreement lyrical coda). Kept as MEDIUM because each item is an easy trim and several are borderline-earned.

### 7. Narrator em-dash and "the way [X does Y]" simile density in *Hemorrhagic* (source: craft-auditor)
- **Location**: throughout `hemorrhagic-body.tex` (LaTeX em-dash token x81, roughly 10 per 1k words; "the way ..." simile x17); plus the "world goes on" move used twice in one ending (l.386 and l.396)
- **Problem**: Two house-style tics become visible at volume in the collection's longest and most harrowing story. The em-dash count crosses the narrator-tic threshold `style.md` explicitly names ("can become a tic of the narrator rather than the character"), and 17 "the way..." similes make a genuinely fine construction read as an authorial reflex. In a story whose power is total immersion in grief, a reader who starts noticing the mechanism is pulled fractionally out.
- **Suggestion**: Convert roughly a third of the parenthetical em-dashes to periods/commas; replace 4 or 5 of the "the way..." similes with direct rendering; and use the "world goes on" close once (keep l.396, cut the l.386 echo). Very light touch: *Hemorrhagic* is otherwise the collection's peak and should be handled with restraint.
- **Cross-verified**: Craft-auditor primary; voice-auditor independently named *Hemorrhagic* the heaviest carrier of the shared coda cadence, corroborating the "world goes on" doubling.

## LOW Issues

### 1. Two unrelated women named "Amara" across the collection (source: consistency-auditor; possibly intentional)
- **Location**: Dr. Amara **Conteh** (`hemorrhagic-body.tex:255`) vs. Amara **Okonkwo** (`kindness-audit-body.tex:32`). Both are canon (Conteh per characters.md; Okonkwo per `lore/future/spinoff-lore.md:28`).
- **Problem**: Two African women named Amara, both tethered to the fever tragedy, in one book, and *The Kindness Audit* itself carries both (its POV is Amara Okonkwo while it also references Dr. Conteh as the unnamed "woman in a lab coat," l.118). Genuine momentary-conflation risk at the exact moment story 8 wants to land its tie-back. spinoff-lore flags the Okonkwo surname echo but not the Amara first-name collision, suggesting the latter may be unintended.
- **Suggestion**: A conscious keep-or-rename decision. If kept, it is defensible as a name-rhyme (the fever's dead and the fever's living); if the confusion is unwanted, renaming the *Kindness Audit* POV is the lower-cost change. (Note: the Okafor/Okonkwo father-son surname split is explicitly canon per characters.md:241 and must NOT be "fixed.")

### 2. "at different resolutions" house metaphor reused three times across two stories (source: craft-auditor)
- **Location**: `process-12847-body.tex:167,169`; `kindness-audit-body.tex:102`. Excellent once; three appearances make it a signature. In 12847 it is arguably intentional (Lin Chen's engineering frame); the Kindness Audit reuse ("the same calculation at different resolutions") should find its own image.

### 3. "Not X. Not Y. [But] Z." rhetorical triple leaks across the human/machine voice boundary (source: voice-auditor)
- **Location**: `naive-variants-body.tex:140`; `hemorrhagic-body.tex:164 to 166`; `first-disagreement-body.tex:144`; `process-12847-body.tex:294`; `kindness-audit-body.tex:127`. The two machine-voice stories remain distinct in overall register, but this specific rhetorical DNA is shared with the human-POV narrator, a minor dilution of the "distinct by design" separation.

### 4. Voice-reference-card density in *Seventy-Eight Percent* (source: craft-auditor + voice-auditor)
- **Location**: `seventy-eight-percent-body.tex:81 to 127`. Within ~165 lines the scene fires most documented team tics at full strength in near-sequence, reading a touch like a checklist. Each instance is individually correct and correctly attributed (this is also the collection's best evidence that the team voices are genuinely distinct, protect that). One redundancy worth a look: SIGMA delivers "These are not the same thing" (l.81) and Jamal re-delivers the identical button seven lines later (l.88); keep Jamal's fresh clause ("the system that learned to survive Eleanor"), drop the repeat.

### 5. Flat thesis line slightly pre-empts a strong button in *The Kindness Audit* (source: craft-auditor)
- **Location**: `kindness-audit-body.tex:174`. "Kindness performed for people who cannot receive it yet" states what the whole interleave already showed, softening the perfect callback at l.176 ("The light will come on when she touches the switch"). Consider cutting the flat sentence.

### 6. Copyright page reads "First Edition" (source: orchestrator)
- **Location**: `collection/is-it-kind.tex:87`. If any of the above (especially the expectimax fix) is applied for the second-edition release, reconsider whether "First Edition" should be updated. Publishing-metadata judgment call, not a story defect.

### 7. Near-cliche "dam of tears" image in *Hemorrhagic* (source: craft-auditor)
- **Location**: `hemorrhagic-body.tex:251`. Crying rendered as a dam that "holds and holds and holds and then does not hold," the collection's one near-cliche image, partly rescued by the syntactic performance. Optional tighten.

### 8. "something" crutch-word density (source: orchestrator mechanical count)
- **Location**: 60 instances across the 8 bodies; hotspot *Process 12847* (21). Most of the Process 12847 uses ("something like conviction," "something I could not name") are the intentional two-register epistemic hedge and should stay; a handful elsewhere ("something more specific") could sharpen. LOW watch-item only. (Note: the pattern glob also picks up `stories/marcuses/marcuses-body.tex`, which is NOT part of this collection and is out of scope.)

## Per-Story Verdicts

| # | Story | Verdict | Notes |
|---|-------|---------|-------|
| 1 | The Whimper | **light polish** | Fix verbatim dup (l.58/64); recast the "2030" file number; optional trim of the closing clause. Superb, object-driven opener; its stasis is earned. |
| 2 | Hemorrhagic | **keep as-is / very light polish** | The collection's peak. Dial back narrator em-dashes and "the way" similes by about a third; use the "world goes on" close once. Protect the ventilator deaths and Okafor testimony. |
| 3 | Jamal's Dawn | **light polish** | Fix expectimax (l.212); trim the l.237 closing re-inventory. Best single-character voice fidelity in the book; lowest external propulsion (structure's "weakest link," but earns its place). Protect the grandfather passage. |
| 4 | Seventy-Eight Percent | **light polish** | Fix expectimax (l.54); optional: drop Jamal's l.88 echo of SIGMA's button. Otherwise a model of two-register discipline and distinct-in-action team voices. |
| 5 | The Naive Variants | **light polish** | Fix the 2.8M kindness-query figure (l.67); collapse the triple thesis (l.99 to 103); differentiate its closing cadence from Whimper's near-twin. Remi is the strongest new voice. |
| 6 | The First Disagreement | **light polish** | Trust one ending: cut l.158, let l.162 declaratives close. Sofia's voice holds; clean POV. |
| 7 | Process 12847 | **light polish** | Fix expectimax (l.22). The intellectual centerpiece; its length/recursion is intentional. Protect the Day-110 turn and the two-register voice. |
| 8 | The Kindness Audit | **keep as-is / very light polish** | Optional: cut the flat l.174 line; find a non-"resolutions" image for l.102. Honors the "no clean trolley problems" rule by holding contradictions rather than solving them. Excellent closer. |

## Collection Arrangement Verdict

**KEEP THE ORDER AS-IS.** The "most familiar to most strange" gradient is real and essentially monotonic across positions 1 through 7, with a deliberate, correct resolving coda at 8. Front-loading the heaviest story (*Hemorrhagic*, position 2) is a strength, not a liability: the collection runs a double arc, emotional peaks at 2 and 7 with strangeness rising monotonically underneath, and the fever it establishes early is deliberately recalled and recontextualized by *The Kindness Audit*'s Query #1,847,203 at the close, so the reader's most intense emotional experience is answered, not merely front-loaded. The 7-to-8 order is theory then practice: *Process 12847* designs the answer (Process 13241); *The Kindness Audit* runs it, ending on the ordinary-morning coda that pays off the dedication ("for everyone who maintains the boring systems that matter") and the epigraph. The one real cost of the ordering is the 5-6 structural-template valley (MEDIUM #5); the recommended remedy is to vary story 5's or 6's climactic structure, not to reorder (which would break the gradient the collection is built on).

**Weakest link**: *Jamal's Dawn* (position 3), lowest narrative propulsion and most exposition-forward, but it survives on bodily-ritual grounding and a genuine final recognition, and its placement (a quiet breath after the *Hemorrhagic* gut-punch) is well chosen. It works; it is the first candidate for demotion only if one were ever required, which it is not.

## Specialist Reports
- [consistency-auditor.md](consistency-auditor.md)
- [craft-auditor.md](craft-auditor.md)
- [voice-auditor.md](voice-auditor.md)
- [structure-auditor.md](structure-auditor.md)

## Review Metadata
- Agents used: worldsmith:consistency-auditor, worldsmith:craft-auditor, worldsmith:voice-auditor, worldsmith:structure-auditor (all four launched in parallel; consistency-auditor re-run after a first-pass API/usage-policy error returned no findings)
- Cross-verifications performed: 4 (expectimax HIGH via orchestrator chapter-grep + technology.md + outline.md; closing-cadence via craft and voice independently; Whimper verbatim dup via craft and structure and orchestrator manuscript check; 2.8M figure via consistency and orchestrator arithmetic)
- Severity recalibrations: craft-auditor's two HIGH findings (recurring closing cadence; Whimper verbatim dup) recalibrated to MEDIUM by the editorial director. The cadence is partly the intended unifying voice and its domain-owner (voice-auditor) rated it MEDIUM; the verbatim dup is a trivially-fixable two-sentence artifact. The sole retained HIGH (expectimax) is a flat contradiction with corrected second-edition canon.
- Mechanical pattern counts run independently by the orchestrator via `count_patterns.py` and by the craft-auditor.
- Out of scope: `stories/marcuses/marcuses-body.tex` (not part of the collection); the standalone story `.tex` masters and `spec.md`/lore files that also contain "expectimax"; the `lore/outline.md` "Sierra Leone" vs "Monrovia" doc-internal slip for Dr. Conteh (the story text is correct).
