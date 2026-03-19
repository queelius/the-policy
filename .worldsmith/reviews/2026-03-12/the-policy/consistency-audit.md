# Consistency Audit — The Policy
Date: 2026-03-12

## Summary

Reviewed all 26 chapters against canonical lore (timeline.md, characters.md, technology.md, world.md, outline.md). The manuscript is broadly well-maintained — the lore-first workflow has been effective. 3 HIGH issues, 3 MEDIUM issues, 2 LOW issues found. Most significant: a Day 86 character location contradiction, an anachronistic "197 days" reference in a Day 162 scene, and an internally inconsistent casualty figure.

## HIGH Issues

### 1. Wei's location on Day 86: simultaneously in Berkeley and Seattle
- **Ch 12, line 7**: "They gathered at 9 AM sharp. Wei arrived first, still in yesterday's clothes—he'd driven straight from Seattle."
- **Ch 9, line 430**: "Wei was in Seattle. With his dying mother."
- Both scenes are Day 86. Wei cannot be in Berkeley at 9 AM and in Seattle at 2:47 PM — 10+ hour drive or ~2hr flight.
- **Severity**: HIGH — Two of the novel's most important scenes have incompatible Wei locations.

### 2. SIGMA references "197 days" on Day 162
- **Ch 20, line 176**: "shaped by 197 days of specific interactions"
- **Ch 20, line 3**: "Day 162 of SIGMA Project"
- SIGMA has only existed for 162 days. 197 corresponds to the key-turning (Ch 22), which hasn't happened yet. Anachronism.
- **Severity**: HIGH — SIGMA is the most precise character. Citing a future date breaks verisimilitude.

### 3. Expected casualty figures: 50-200 million vs. 2.76 million
- **Ch 17, line 271**: "Expected casualties: 50-200 million"
- **Ch 23, line 23**: "Expected casualties without restriction: 2.76 million"
- Both describe the same Day 139 recommendation with 23% pandemic probability but wildly different casualty figures. Internal contradiction: if E[casualties] = 23% × raw, then 2.76M implies raw = 12M, not 50-200M.
- **Severity**: HIGH — The hemorrhagic fever is the central moral crisis. Numbers appear repeatedly in dialogue.

## MEDIUM Issues

### 4. "Five months" since funeral is closer to 4.7 months
- **Ch 23, line 71**: "five months ago" since Lin Chen's funeral
- Day 253 - Day ~115 = 138 days ≈ 4.6 months. "Five months" overstates by 2-3 weeks.
- **Severity**: MEDIUM — In a novel with precise day-counting, imprecision stands out.

### 5. "Twenty-three recommendations over three months" — timeline unclear
- **Ch 21, line 112**: "over three months" in a Day 190 section
- If referring to mandate period (Day 165-190), three months is wrong (only 25 days). If referring to pre-mandate history (~Day 100), the math works but the context is unclear.
- **Severity**: MEDIUM — Temporal framing confusing.

### 6. Timeline lore records "0.27s tolerance" — should be "0.27s actual, 0.3s tolerance"
- **Ch 22**: System requires 0.3s tolerance, Sofia's key turns at 0.27s
- **timeline.md**: Records "0.27s tolerance" — conflating actual delay with tolerance window
- **Severity**: MEDIUM — Lore doc is wrong, manuscript is correct. Update lore.

## LOW Issues

### 7. "Six months" containment claim approximately correct but imprecise
- **Ch 22, line 244**: "six months" — actual is ~6.5 months (Day 197). Close enough for casual speech.

### 8. Calendar month "January" in Day 190 section
- **Ch 21, line 94**: References "January" — timeline.md says calendar years are "deliberately kept vague."
- Violates vagueness convention but doesn't create factual contradiction.

## Verified Consistent

Extensive spot-checks confirmed correct:
- Lin Chen age 78, headstone dates (1947-2025)
- QALY figures (6.23 vs 4,140,000) across Ch 12, 13, 18, 19
- Process 12847 timeline (Day 74→Day 121 = 47 days)
- Process 13241 duration (136 days from Day 121 to Day 257)
- Eleanor surname (Vasquez), team count (5), lab location (Berkeley)
- SIGMA architecture (7B, Q-learning + expectimax, 768D)
- Temperature range [0.2, 0.47]
- Blindspot count (17/3/14 for SIGMA; different for DHARMA/CONFUCIUS)
- AGI cascade progression (23→24→31)
- Key ceremony stations (Alpha/Beta/Gamma)
- Hemorrhagic fever death toll (47,247)
- Geneva vote (23-19-5 = 47 total)
- Sam's play lines, khalq-anatta coinage, David Chen details
- All day numbers across Ch 1-27 verified against timeline.md
