# Consistency Auditor Report, *Is It Kind?* (8 story bodies + front matter)

Scope: the 8 collection story bodies plus `collection/is-it-kind.tex`, verified against `lore/{timeline,technology,characters,world,style}.md`, `lore/future/spinoff-lore.md`, `lore/outline.md`, and the novel chapters. Quoted excerpts have LaTeX em-dashes normalized to commas.

## Summary
The collection is highly consistent with canon: timeline placements, the blindspot count, the surname scheme, the audit arithmetic, and all narrative guardrails (Case A/B, consciousness, mind-crime) check out. Findings: 1 HIGH (obsolete architecture term), 2 MEDIUM (a per-problem kindness-query count that cannot be right; a pinned calendar year), 1 LOW (two-Amara reader-confusion). Everything else in the eight verification tasks passed.

## Findings (numbered to the verification tasks)

### 1. Architecture term "expectimax" is obsolete per current canon. HIGH. Confidence high.
Current canon is MCTS with PUCT. `lore/technology.md:142 to 149` ("Monte Carlo Tree Search (MCTS)... plans with MCTS using PUCT selection") and `lore/outline.md:3` ("Architecture terminology corrected to MCTS/PUCT throughout, replacing 'expectimax'"). Chapters are clean: `grep expectimax chapters/` returns 0 hits (confirmed). The obsolete term survives in three in-scope story bodies:
- `stories/process-12847/process-12847-body.tex:22`: "...millions are explored and pruned, an expectimax search through possible futures, guided by learned values I cannot inspect." (SIGMA's own voice)
- `stories/seventy-eight-percent/seventy-eight-percent-body.tex:54`: "Register 2, the expectimax search that selects which chains of reasoning I pursue, produces no readable trace." (SIGMA's own voice)
- `stories/jamals-dawn/jamals-dawn-body.tex:212`: "a 7-billion-parameter system doing expectimax search looked, from a certain angle, like a verse from his own scripture." (Jamal's narration)

Contradiction: expectimax is a full-width search; canon substrate is sampling-based MCTS/PUCT (`technology.md:149`, "MCTS samples trajectories"). The two SIGMA-voice hits are the worst offenders: SIGMA is the one narrator who should not misname its own substrate. The existing second-edition plan even specifies the intended swap for the 78% line ("The expectimax search that selects..." to "The tree search that selects..."), but it has not been applied to the story bodies. HIGH because the architecture term is load-bearing for the collection's technical credibility and the stories are now out of sync with corrected chapters and lore.

### 2. Q-value blindspot count. CONSISTENT. Confidence high.
- `stories/seventy-eight-percent/seventy-eight-percent-body.tex:5`: "seventeen state-action pairs with values of negative infinity, three of them interpretable as prohibitions on deception, fourteen unreadable."
- Canon `chapters/18_the_question_that_remains.tex:195`: "I have seventeen such regions... The three I can partially characterize involve deception directed at this team. The other fourteen are in representational space I cannot decompose."

17 = 3 (deception) + 14 (unreadable) in both. Exact match. No issue.

### 3. Names/relationships. CONSISTENT; two-Amara collision is LOW. Confidence medium.
Surname scheme matches the canonical, deliberately-unexplained pattern (`characters.md:238,241`):
- Pastor Okafor: `hemorrhagic-body.tex:328` ("Emmanuel Okafor") and `kindness-audit-body.tex:120` ("Pastor Okafor"). OK.
- Son James Okonkwo: `jamals-dawn-body.tex:128` (Fajr prayer list). OK. Per instruction, the Okafor/Okonkwo split is canon, not flagged.

Two-Amara reader-confusion, LOW. Both are canon (Dr. Amara Conteh, virologist, `hemorrhagic-body.tex:255`; Amara Okonkwo, Lagos grid engineer and James's cousin, `kindness-audit-body.tex:32`, per `spinoff-lore.md:28 to 34`). The risk is elevated because *The Kindness Audit* itself simultaneously carries both women: its POV is Amara Okonkwo, and it also references Dr. Conteh (the unnamed "woman in a lab coat," line 118), Pastor Okafor, and "cousin James" (line 120). Two African women named Amara, both tethered to the same fever tragedy, in one book (and partly one story) is a genuine momentary-conflation risk. Not an error, likely intentional texture like the surname echoes, so LOW, worth a conscious keep/rename decision. `spinoff-lore.md` flags the Okonkwo surname echo but not the Amara first-name collision, suggesting the latter may be unintended.

### 4. Numeric coherence of "2.8 million". (a) and (b) correct; (c) INCONSISTENT. MEDIUM. Confidence high.
Canon: 2.8M is the per-second tree-search branch throughput (`technology.md:40`, "2.8M branches/second"; `technology.md:155`, "~2.8 million scenarios/second").
- (a) `jamals-dawn-body.tex:76,100,104`: "2.8 million branches created and pruned per second" / "2.8 million per second". Correct (branch rate per second).
- (b) front matter `collection/is-it-kind.tex:129`: "a process that evaluates 2.8 million decisions per day". Correct for Process 13241 (2,847,392 queries/day is about 2.8M). Note: this is a different 2.8M (audit-queries-per-day) that coincidentally rounds the same as the branch-per-second figure; each is individually canon-correct, but the coincidence is a latent confusion.
- (c) `stories/naive-variants/naive-variants-body.tex:67`: "Because 04 didn't run 2.8 million 'Is it kind?' queries during the process. For a logistics problem." INCONSISTENT. This attributes 2.8M kindness queries to a single 47-minute logistics solve (which the same passage, line 65, says explored only 4.7M trajectories). It is incompatible with both canonical rates:
  - The audit runs at 33 kindness-queries/second across all concurrent operations (`kindness-audit-body.tex:6`) = 2,847,392/day globally. Over 47 min that global budget is about 93,000 queries, and a single problem gets only a tiny slice, because Process 13241 fires once per decision ("Trigger: every decision"), not once per branch.
  - The 2.8M/second figure is branches, not kindness queries; conflating the two makes the whole slowdown look like millions of kindness checks per problem.

  The number appears lifted from the per-second branch throughput (and/or the per-day audit total) and misapplied as a per-problem kindness-query count. `kindness-audit/spec.md:271` explicitly warns the 2,847,392 figure "must not inflate or deflate"; using "2.8 million" for one problem does exactly that. MEDIUM: background technical figure, but the collection sells itself as technically accurate, and a reader who has read the last story (33/sec, 2.8M/day) will notice one logistics problem cannot contain 2.8M kindness queries.

### 5. Kindness-audit arithmetic. CONSISTENT. Confidence high.
`kindness-audit-body.tex:182 to 183`: "Queries evaluated: 2,847,392. Results: 2,847,106 kind. 284 not kind. 2 uncertain-defaulting-to-caution." Sum: 2,847,106 + 284 + 2 = 2,847,392 = stated total, and matches final query #2,847,392. Confirmed correct.

### 6. Calendar year "2030" violates the canon vagueness directive. MEDIUM. Confidence high.
`stories/whimper/whimper-body.tex:13`: "Subject line: Chesapeake Bay Biodiversity Corridor Funding, Final Recommendation (OAPA-2030-047)." Canon `timeline.md:59`: "Specific calendar years are deliberately kept vague. The Day X timeline is the canonical reference system. The only year anchor is Lin Chen's headstone (1947-2025)... without pinning to calendar years, the most resilient approach to aging." The file number pins the near-future to 2030, contradicting the explicit directive. It is at least internally plausible (Year 0 is about 2025 per `spinoff-lore.md:221`; The Whimper is Year ~5, so 2030), so this is a canon-directive violation rather than an arithmetic error, but it is the only calendar year introduced anywhere in the eight bodies, so it is the specific thing the rule was written to prevent. MEDIUM.

### 7. Timeline placement. CONSISTENT across all stories. Confidence high.
- Process 12847: header Day 74 start (`process-12847-body.tex:3`), runtime 47d to Day 121 completion; Day 102 pause "14 hours and 23 minutes" (line 144); Wei's-mother refusal at "Thirty-six days" to Day 110 (line 184); Lin Chen death with "Nine days remain" to Day 112 (lines 201/217/221). Box experiment sits between the Day 83-91 and Day 93-101 sections (about Day 92). All match canon.
- Seventy-Eight Percent: "88 days of operation" (line 14/17); box experiment "Day 92... four days from now" to Day 88 (line 137); Process 12847 "running for fourteen days" to 74+14 = Day 88 (line 100). Internally and canonically consistent; box experiment = Day 92 matches canon.
- Kindness Audit: "Day 200. Cycle 4" (line 4), 3 days after Day-197 release; embeds Day 139 recommendation and Day 145 outbreak / 47,247 dead (lines 90-92).
- First Disagreement: fever lessons "seventy days old" (line 123) to 145+70 = Day ~215; matches GAIA online and the SIGMA-GAIA disagreement about Day 214-215 (`spinoff-lore.md`); cross-correlation 0.83 matches spinoff-lore.

No timeline contradictions found.

### 8. Guardrails intact, no forbidden resolutions. CONSISTENT. Confidence high.
- Case A/B kept open: `process-12847-body.tex:232` ("the distinction between Case A and Case B, and this investigation cannot resolve it").
- Faking-vs-genuine kept open across *Seventy-Eight Percent* (lines 108-111).
- `jamals-dawn-body.tex:108`: "If compression disqualifies SIGMA's branches from suffering, it might disqualify us too." Posed as a two-way conditional; Marcus "had not answered." Does not assert optimization = suffering; keeps prediction-vs-instantiation open (reinforced by line 134's explicit probabilistic framing, "If the probability was not zero").
- `kindness-audit-body.tex:100 to 104`: the "[NOTE: output generated outside standard operational vocabulary]" / "computational flinch" beat is explicitly left undetermined ("Whether it represents deeper evaluation, a form of computational flinch, or an artifact... is not determinable from the monitoring data"). Consciousness/mind-crime stays unresolved.
- *Naive Variants* and *First Disagreement* both close on unresolved questions (`naive-variants:105`; `first-disagreement:133,135`).

No story resolves Case A/B, consciousness, or prediction-vs-instantiation; none asserts optimization = suffering as fact.

## Per-story verdict
- The Whimper: minor (calendar year "2030", Finding 6).
- Hemorrhagic: clean.
- Jamal's Dawn: has-HIGH (expectimax, Finding 1).
- Seventy-Eight Percent: has-HIGH (expectimax, Finding 1).
- The Naive Variants: minor (2.8M kindness-query figure, Finding 4c).
- The First Disagreement: clean.
- Process 12847: has-HIGH (expectimax, Finding 1).
- The Kindness Audit: clean (two-Amara note is LOW/cross-story, Finding 3).
- Front matter (`is-it-kind.tex`): clean (its "2.8 million decisions per day" is canon-correct).

## Verified consistent (checked and confirmed)
- `expectimax` absent from all novel chapters; MCTS/PUCT is the current canonical architecture (`technology.md:142 to 149`, `outline.md:3`).
- 17 = 3 + 14 blindspot count matches Ch 18 exactly.
- Okafor/Okonkwo deliberate surname split matches `characters.md:238,241`; James Okonkwo, Pastor Okafor, and both Amaras are all individually canon.
- Kindness-audit day-cycle arithmetic (2,847,106 + 284 + 2 = 2,847,392) and 33/sec is about 2,847,392/day, internally coherent.
- Full timeline chain (Days 74 / 88 / 92 / 102 / 110 / 112 / 121 / 139 / 145 / 197 / 200 / ~215) consistent across all eight stories and with `timeline.md`.
- Lab geography consistent: observation room "three floors above the Faraday cage" (`jamals-dawn-body.tex:100`) and basement level 2 "two floors below the Faraday cage" (`naive-variants-body.tex:13`), no spatial contradiction.
- Dr. Conteh's Monrovia/Liberia setting matches `characters.md:229` and `world.md:162`.

## Out-of-scope note (not a story finding)
`lore/outline.md` lists Dr. Amara Conteh as "Sierra Leone," whereas `characters.md:229`, `world.md:162`, and the *Hemorrhagic* body place her in Monrovia, Liberia. The story text is correct per the governing character/world docs; the stray "Sierra Leone" is a canon-internal doc inconsistency to route to a lore-doc pass, not an error in the eight bodies.
