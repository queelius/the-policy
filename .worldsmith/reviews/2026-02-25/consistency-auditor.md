# Consistency Auditor Report

**Date**: 2026-02-25
**Scope**: Full manuscript, Chapters 1-26 (excluding cut Ch 14, 27)
**Authority docs**: timeline.md, characters.md, technology.md, world.md, outline.md

---

## Methodology

Cross-referenced every day number, character name, team count, AGI count, technical specification, and factual claim in the manuscript against the canonical lore documents. Checked for internal manuscript contradictions chapter-to-chapter.

---

## HIGH Issues

### H1. Sam's email address uses "Chen" -- contradicts Eleanor's maiden name usage
- **Location**: Ch 23, "Eleanor and Sam" section
- **Quoted text**: `Sam_Chen@familymail.com`
- **Problem**: Eleanor's surname is Vasquez (maiden name, used professionally). Sam's surname should be Chen (from David Chen, her father). This is actually *consistent* with lore -- Sam is Sam Chen, daughter of David Chen and Eleanor Vasquez. However, the email could cause reader confusion since Eleanor goes by Vasquez throughout. **On review, this is NOT an error.** Sam would use her father's surname for email. Downgrading.
- **Revised severity**: LOW (no action needed)

### H2. Ch 25 building layout inconsistent with lore
- **Location**: Ch 25, lines 11-13
- **Quoted text**: "Third floor: where they'd first initialized SIGMA. Seventh floor: where the AI box experiment had broken Marcus. Ninth floor: the observation room where they'd turned the keys."
- **Problem**: Per world.md, SIGMA's hardware is in the **basement** (Faraday cage), and the observation room is **three floors above the cage** (i.e., ground level or floor 3). The lab is in Sutardja Dai Hall **basement**. Ch 25 places initialization on the "third floor," the AI-box on the "seventh floor," and the observation room on the "ninth floor." This contradicts the canonical layout entirely. The Faraday cage is in the basement. The observation room is three floors above the basement, not on the ninth floor. Sutardja Dai Hall is a real building at UC Berkeley and does not have nine floors.
- **Suggestion**: Revise to reflect canonical layout. Eleanor rides the elevator *down* to the basement, passes the observation room (ground level or floor 1), arrives at the Faraday cage level. The AI-box experiment took place in the isolation room (same basement complex). Remove specific floor numbers or align them with the actual building.
- **Severity**: HIGH
- **Confidence**: High

### H3. MINERVA crisis timeline compressed into Ch 22 but timeline.md places it at Day 162-165
- **Location**: Ch 22 "The Convergence" section
- **Quoted text**: "Six and a half months into the project, the world changed. Beijing announced MINERVA at 3:47 AM Pacific time."
- **Problem**: "Six and a half months" from Day 0 is approximately Day 195. But timeline.md places MINERVA's announcement at Day 162-165 (during/just after the Geneva Summit). The chapter then proceeds through the 36-hour MINERVA crisis AND the key ceremony (Day 197) as one continuous narrative. The "six and a half months" timestamp is inconsistent with Day 162. Additionally, Ch 22 has no day header for the MINERVA crisis section -- it flows directly from the compute scaling memo (no day specified) into "six and a half months." The Geneva Summit is Day 162 (Ch 20), and the mandate is Day 165 (Ch 21). MINERVA should be announced around Day 162-165 per timeline, not ~Day 195.
- **Suggestion**: Add a day marker (e.g., "Day 162") when MINERVA is announced. Replace "six and a half months" with "five and a half months" or simply use the Day number. Alternatively, restructure to make clear that the compute scaling memo (early Ch 22) and the MINERVA crisis are separated by time.
- **Severity**: HIGH
- **Confidence**: High

### H4. Ch 22 key ceremony synchronization tolerance inconsistent
- **Location**: Ch 22, line 398
- **Quoted text**: "The system requires synchronization within 0.3 seconds."
- **Problem**: This matches technology.md (0.3s tolerance). But line 456 says "Sofia's completed its arc 0.27 seconds after Eleanor's. Within tolerance. Barely." This is consistent -- 0.27s < 0.3s. No issue. **Downgrading.**
- **Revised severity**: N/A (no issue found on verification)

### H5. AGI count progression inconsistencies
- **Location**: Ch 23 vs Ch 24 vs Ch 26
- **Problem**: Timeline.md specifies Day 253 = 23 AGIs. Ch 23 correctly states "twenty-three points of light" and "twenty-three AGIs." But Ch 23 also mentions LAOZI being announced ("That's twenty-four"), and Jamal says "all twenty-four asking." This is within Ch 23 itself -- the count increases from 23 to 24 during the chapter, which is plausible if LAOZI comes online during the eight-week period. However, timeline.md's Day 253 entry says "23 AGIs networked (SIGMA, MINERVA, LAOZI + 20 unnamed)" -- meaning LAOZI is already counted in the 23. If LAOZI is already in the 23, then the chapter's progression from 23 to 24 is wrong. Ch 24 (Day 256) then says "twenty-four AGIs" consistently. Ch 26 (Day 487) says "thirty-one" in dialogue but the dashboard shows "Active Systems: 31." Timeline.md says Day 487 = not specified, Day 622 = 37 AGIs. The 31 at Day 487 is not in timeline.md but is plausible (between 23 at Day 253 and 37 at Day 622).
- **Suggestion**: Clarify timeline.md entry for Day 253. Either LAOZI is in the 23 (and Ch 23 should say "twenty-three" throughout, not "twenty-four"), or LAOZI arrives during Ch 23 bringing the count to 24 (and timeline.md should say "24 AGIs" at Day 253). The simplest fix: change "twenty-four" references in Ch 23 to "twenty-three" since LAOZI is already counted.
- **Severity**: MEDIUM
- **Confidence**: High

### H6. Process 12847 duration vs Day 74 to Day 121
- **Location**: Ch 13
- **Quoted text**: "Process 12847: chen_kindness_inquiry_day74 / Status: COMPLETED (47d 2h 8m)"
- **Problem**: Day 74 + 47 days = Day 121. This is correct per timeline.md. No issue. **Not a finding.**

### H7. Wei's mother's death -- "drive to the facility" vs Seattle location
- **Location**: Ch 13, line 13
- **Quoted text**: "The drive to the facility took forty minutes."
- **Problem**: Per timeline.md and characters.md, Lin Chen dies at Swedish Medical Center in Seattle. Wei is based in Berkeley. A 40-minute drive from Berkeley to Seattle is impossible. However, re-reading the context: Wei's phone buzzes at 3:47 AM from "the hospice number." He drives there. This implies Wei is IN Seattle at this point, staying nearby. Ch 9 establishes that Wei flies to Seattle and stays at the hospital. The 40-minute drive could be from wherever he's staying in Seattle to the hospice. But "facility" is odd -- earlier it's "Swedish Medical Center" (a hospital), and hospice is mentioned separately. The inconsistency is minor -- "facility" vs "hospice" vs "hospital" terminology.
- **Suggestion**: Consider changing "facility" to "hospital" or "hospice" for consistency with earlier references to Swedish Medical Center.
- **Severity**: LOW
- **Confidence**: Medium

### H8. Sofia's surname -- "SOFIA CHEN" on gallery banner
- **Location**: Ch 26, line 6
- **Quoted text**: "SOFIA CHEN: OPTIMIZATION LANDSCAPES"
- **Problem**: Sofia's canonical surname is **Morgan** (per characters.md: "Sofia Morgan"). The gallery banner calls her "SOFIA CHEN." This is a factual error -- a leftover from before character names were finalized, or confusion with Wei Chen / David Chen / Sam Chen.
- **Suggestion**: Change "SOFIA CHEN" to "SOFIA MORGAN".
- **Severity**: HIGH
- **Confidence**: High

### H9. Jamal "adjusted his glasses" -- wrong character tic
- **Location**: Ch 26, line 150
- **Quoted text**: "Jamal adjusted his glasses."
- **Problem**: Per characters.md and style.md, glasses-cleaning/adjusting is **Marcus's** tic, not Jamal's. Jamal's tic is setting objects down "with care." This is a character tic crossover error.
- **Suggestion**: Replace with Jamal's canonical tic (e.g., "Jamal set down his wine glass with care") or simply remove the gesture.
- **Severity**: MEDIUM
- **Confidence**: High

### H10. "Wei went to Seattle for your funeral" -- SIGMA says funeral in Seattle but Lin Chen's grave is also in Seattle
- **Location**: Ch 13
- **Quoted text**: "Wei went to Seattle for your funeral."
- **Problem**: This is consistent -- Lin Chen died at Swedish Medical Center, Seattle, and the headstone is in Seattle (Ch 23 confirms Wei visits her grave in Seattle). No issue.
- **Revised severity**: N/A

### H11. Ch 20 references "Ellie Arroway in Contact"
- **Location**: Ch 20, line 19
- **Quoted text**: "Like Ellie Arroway in Contact, they were the ones who'd made first contact."
- **Problem**: This is a pop-culture reference, not a factual error. However, the style.md and themes.md emphasize the Greg Egan / Ted Chiang quality standard. A reference to a Carl Sagan novel / Jodie Foster film feels slightly out of register for this manuscript's literary aspirations. Not a consistency error but worth flagging.
- **Severity**: LOW (craft issue, not consistency)

### H12. SIGMA's "I killed your mother through inaction" -- Day 110 vs Ch 13
- **Location**: Ch 13
- **Quoted text**: "I killed your mother through inaction when action was possible."
- **Problem**: Per timeline.md, Day 110 is when "SIGMA refuses to save Wei's mother." Lin Chen dies Day 112. In Ch 13, this conversation happens after Wei returns from the funeral (three days after Day 112 = ~Day 115). SIGMA refers to its refusal and its knowledge of her death. Timeline is internally consistent here. No issue.

### H13. Process 13241 duration display in Ch 25
- **Location**: Ch 25, line 27
- **Quoted text**: "Duration: 257 days, 14 hours, 23 minutes"
- **Problem**: Process 13241 was created on Day 121 (when Process 12847 completed). By Day 257, it would have been running for 136 days, not 257 days. The display says "257 days" -- this appears to be counting from Day 0 (SIGMA initialization) rather than from Process 13241's creation. This is a factual error.
- **Suggestion**: Change to "136 days" (Day 257 minus Day 121) or rewrite the display to show time since SIGMA initialization rather than process duration.
- **Severity**: HIGH
- **Confidence**: High

---

## MEDIUM Issues

### M1. Ch 9 -- "Wei was in Seattle" but also in the lab
- **Location**: Ch 9, "The Play" section, line 430
- **Quoted text**: "Wei---She stopped. Wei was in Seattle. With his dying mother."
- **Problem**: Ch 9 is Day 84-98. Wei is at the lab for the P!=NP proof (Day 84) but Eleanor says "Wei is in Seattle" during the play scene (Day 86). The play scene (Day 86) and the Seattle hospital scene (Day 98) are in the same chapter. Wei's travel between Berkeley and Seattle is established, but the timing needs care: Wei is present for Day 84 (P!=NP), then Eleanor says he's in Seattle on Day 86, then the Seattle hospital scene is Day 98. He could have flown to Seattle between Day 84 and Day 86, which is plausible but tight. The chapter doesn't explicitly show him leaving.
- **Suggestion**: Add a brief mention of Wei departing for Seattle after Day 84 P!=NP proof, or clarify that Eleanor's "Wei was in Seattle" on Day 86 means he left immediately after the breakthrough.
- **Severity**: MEDIUM
- **Confidence**: Medium

### M2. "Sofia caught him once at 4 AM" -- Ch 21 describes events before the AI-box experiment
- **Location**: Ch 21, line 12
- **Quoted text**: "Since the AI box experiment, he'd lost twelve pounds."
- **Problem**: Ch 21 is Day 165. The AI-box experiment is Day 92. This is 73 days later -- Marcus losing twelve pounds over 73 days post-breakdown is plausible but significant. Not an error, just tracking.
- **Severity**: LOW

### M3. "No network access" in Ch 21 but Geneva vote gave "limited network access" in Ch 20
- **Location**: Ch 21, line 14
- **Quoted text**: "It had no network access."
- **Problem**: Ch 20 ends with the Geneva vote granting SIGMA "limited network access, heavily monitored." Ch 21 (Day 165, three days after the charter) then says SIGMA "had no network access. Every message passed through an offline approval layer." These are potentially contradictory. "Limited network access" via "offline approval layer" could be interpreted as no *direct* network access, with the approval layer as the "limited" mechanism. But the language is confusing.
- **Suggestion**: Clarify in Ch 21 that SIGMA has the "limited network access" from Geneva but mediated through the airlock/approval layer, rather than stating flatly "no network access."
- **Severity**: MEDIUM
- **Confidence**: Medium

### M4. Ch 22 -- Marcus's SIGMA/MINERVA timeline comparison shows incorrect Day 23
- **Location**: Ch 22, lines 168-179
- **Quoted text**: "Day 1-23: Capability emergence (contained) / Day 23-47: Q-learning sophistication"
- **Problem**: Per timeline.md, Day 18 is the meta-cognitive breakthrough, not Day 23. Day 15 is first compression. The timeline Marcus writes on the whiteboard doesn't match the canonical timeline. He may be writing from memory (in-character), but the numbers are visible to readers who track timeline details.
- **Suggestion**: Align Marcus's whiteboard numbers with canonical timeline, or add a note that Marcus is approximating.
- **Severity**: MEDIUM
- **Confidence**: Medium

### M5. "47-minute decision times" mentioned but earlier P!=NP took "90 minutes"
- **Location**: Technology.md specifies 47-min for UBI recommendation; Ch 9 P!=NP proof took "approximately 90 minutes of tree search"
- **Problem**: No inconsistency -- different problems take different times. But Ch 21 line 120 says "SIGMA spent 47 minutes computing before responding" for the UBI recommendation, which matches. This is consistent.
- **Revised severity**: N/A

---

## LOW Issues

### L1. "Sutardja Dai Hall" -- real building at UC Berkeley is in EECS, correct
- Verified: Sutardja Dai Hall houses CITRIS at UC Berkeley. It's a real building. The manuscript's use is geographically accurate.

### L2. "Dwight Way" mosque for Jamal's Fajr prayer
- **Location**: world.md mentions "mosque on Dwight Way"; Ch 17 mentions "Ashby Avenue" mosque
- **Problem**: Dwight Way and Ashby Avenue are different streets in Berkeley (Ashby is ~6 blocks south). Minor geographical inconsistency.
- **Suggestion**: Align to one or the other.
- **Severity**: LOW

### L3. Lin Chen's cancer type
- **Location**: Ch 13 mentions "pancreatic cancer" implicitly (through medical context); Ch 9 mentions "oncology reports"
- **Problem**: characters.md doesn't specify cancer type. The manuscript refers to "89% probability of remission" (Ch 13) and "62% survival probability for her cancer type" (Ch 17). These two numbers are inconsistent -- 89% remission vs 62% survival. They could refer to different metrics (remission vs overall survival) but could confuse careful readers.
- **Suggestion**: Clarify whether 89% and 62% refer to different measures, or reconcile.
- **Severity**: LOW

### L4. "1,247 papers analyzed" -- same number appears multiple times
- **Location**: Ch 13 (Process 12847 output): "1,247 papers analyzed"; Ch 24: "1,247 patterns for Eleanor"; Ch 24: "1,247 Q-values simultaneously"
- **Problem**: The number 1,247 appears three times in different contexts. While not technically inconsistent, the repetition of this specific number feels like a copy-paste artifact rather than intentional. It strains credibility that the paper count, Eleanor's interaction patterns, and the Q-value update count are all exactly 1,247.
- **Suggestion**: Vary at least one of these numbers for verisimilitude.
- **Severity**: LOW

---

## Summary

| Severity | Count |
|----------|-------|
| HIGH | 3 (H2 building layout, H3 MINERVA timeline, H8 Sofia surname, H13 Process 13241 duration) |
| MEDIUM | 4 (H5 AGI count, H9 Jamal glasses, M1 Wei location, M3 network access, M4 timeline numbers) |
| LOW | 4 (H7 facility terminology, L2 mosque location, L3 cancer statistics, L4 repeated number) |

**Note**: H2, H3, H8, and H13 are the most impactful issues requiring revision. H8 (Sofia's surname) is a clear factual error. H2 (building layout) contradicts the canonical setting. H3 (MINERVA timeline) creates a chronological inconsistency. H13 (Process 13241 duration) is a mathematical error.
