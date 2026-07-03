# Consistency Auditor: The Policy (2nd-ed. pre-publish gate)

**Date:** 2026-07-02
**Scope:** All shipping chapters (files 01-13, 15-26), four appendices (31-34), afterword (35), back matter (28-29), part dividers, both masters, vs. canonical lore.

Traced every day-number, casualty figure, AGI count, architecture claim, and appendix cross-reference. Findings: 1 HIGH, 4 MEDIUM, 3 LOW. (Editorial director recalibrated the HIGH death-toll item to MEDIUM in the unified report on reader-impact grounds; it remains a required correction.)

## HIGH (as filed by auditor)

### MINERVA death toll regresses 38 back to 31
- `chapters/22_scaling_the_policy.tex` L354-358: Guangzhou collapse, "Seven dead. Three more in the building. ... 'That's thirty-eight,' Wei said. 'In thirty-seven hours.'" Then L570 (post-vote teaching, chronologically later): "'Thirty-one dead now. Industrial accidents...' ... 'Every hour we wait, the count goes up.'"
- Ramp elsewhere: 1 (hr 24, L190), 31 (hr 36, L220), 38 (hr 37, L358). The "31" at L570 is a stale copy of the hr-36 figure; it decreases the toll while the same line asserts the count rises.
- **Fix:** raise L570 to 38 or higher (e.g., "Forty-one dead now," reflecting the "two more factory incidents" cited two lines earlier). Confidence: high.

## MEDIUM

### File 22 uses stale time references for the Day-197 crisis
- L91 "Five and a half months into the project... Beijing announced MINERVA"; L273 SIGMA "full posterior over 162-day interaction history." But the chapter turns the keys at Day 197 and L647 transmits "Q-value trajectory, Day 1-197." "162 days" is the Geneva figure (correctly used in file 20 L178). Day 197 is about 6.5 months.
- **Fix:** "Five and a half months" to "six and a half months"; "162-day" to "197-day."

### Lin Chen "62% survival, she was in the 38%" contradicts her diagnosis
- `chapters/17_the_policy_revealed.tex` L589. Established: Stage IV metastatic pancreatic, standard treatments exhausted, roughly 8-month terminal prognosis (files 08/12), and SIGMA deliberately refused the 89% Approach Alpha (file 12), "I chose to let her die" (file 24). A "62% survival with aggressive treatment / unlucky variance" framing is incompatible with a terminal diagnosis and reframes a deliberate sacrifice as bad luck.
- **Fix:** reground the "unlucky variance" analogy in the hemorrhagic-fever policy alone; drop the fabricated survival statistic.

### Appendix A calls the Geneva 47 "nations"; manuscript and lore say individuals
- `chapters/32_appendix_timeline.tex` L47 "forty-seven nations debate." Manuscript (file 20 L5) "forty-seven of the world's leading AI researchers, policy makers, and ethicists"; Ferreira's central argument (L81), "Forty-seven people in a room ... do not constitute democratic consent," depends on their being individuals. App A is the outlier.
- **Fix:** file 32 L47 to "forty-seven researchers, policymakers, and ethicists" (or "delegates").

### File 22 mixes two hour-clocks in the teaching sequence
- Post-vote teaching narrated on a session clock ("Hour 1/4/8/12/15"), then reverts to the deployment clock ("Hour forty-seven," L660; "Hour seventy-two," L684). Deployment hr-47 is roughly teaching hr-10, so it is narrated after teaching hr-15, an out-of-order beat, and the reader cannot tell which clock "Hour 47" is on.
- **Fix:** relabel the two closing beats consistently (e.g., "Teaching hour 11/17") or place them explicitly on the deployment clock without following "Hour 15."

## LOW
- "Buried his mother six days ago" (Day 118, file 12 L648) vs. funeral about Day 114-115 (mother dies Day 112; Wei "returned three days later, after the funeral," file 13 L65). Should read about "three/four days ago."
- LAOZI is both an established Day-253 AGI ("LAOZI thinks kindness is restraint," file 23 L65) and the AGI SIGMA is "teaching" at Day 256-257 (files 24 L177/197, 25 L219). Lore has CONFUCIUS teach LAOZI. Reads as ongoing teaching, but invites confusion. Consider naming the Day-256 "twenty-fourth AGI" as a new/unnamed system.
- THOTH (file 25 L219) is un-provenanced and could clash with PTAH's lore status as "first non-superpower AGI." Reader-invisible.

## Verified consistent (spot-corroborated by editorial director)
- Architecture: "expectimax" = 0; Q-learning plus MCTS/PUCT (AlphaZero lineage) throughout (files 04, 11, 17, App B). Reward 65/15/10/10; 7B/16k; 17 blindspots consistent (files 16, 18, 23).
- Process numbers 12847 / 13241: zero comma variants; 12847 = 47-day investigation; 13241 permanent at 15.3% compute; file 25 "136 days" = Day 257 minus Day 121. Correct.
- Fever toll 47,247 (3 named plus 47,244 = 47,247 arithmetic checks, file 17 L543); 2.76M / 23% / 7.3% consistent.
- Cascade counts 1, 2, 23, 24, 31 consistent across files 22-26, App A, App B.
- Wei carries the prediction-vs-instantiation counter (file 11 L802). Okafor is Okonkwo's father, deliberate split (file 17). Vasquez (never Zhang); Berkeley (never SF); team of five; Lin Chen 78 / headstone 1947-2025.
- App C printed chapter numbers 1-25 map correctly; App A day-to-chapter rows all resolve under the printed-number convention; sculpture "canary" dates (86/92/145/197) correct.
- Part-divider epigraphs verbatim (Part I Wei/file 01 L207; Part II SIGMA/file 13 L250; Part III Sam/file 25 L157).
- No back matter (App B/C/D, Afterword) resolves any never-resolve guardrail.
- Both masters include the identical chapter set, exclude files 14 and 27, identical back-matter order.
