# Consistency Auditor Report: "The Naive Variants"

**Date:** 2026-03-20
**Scope:** Full manuscript (2,770 words, 5 sections)
**Sources checked:** timeline.md, technology.md, characters.md, world.md, outline.md, spinoff-lore.md, Ch 6 (novel), Ch 9 (novel), spec.md

---

## HIGH Issues

### H1. Floor Numbering / Spatial Layout Inconsistency

**Location:** Section 1 (Asset Discovery), line 35; Section 5 (Disposition), line 171
**Quoted text:** "The basement was three floors below the main lab" / "three floors below the room where someone had once asked a machine to be kind"
**Problem:** The canonical lab layout (technology.md) places the Faraday cage at "basement/floor 0" and the observation room "three floors above cage" (floor 3). Basement level 2 (B2) is two floors below the Faraday cage (floor 0), not three. If "main lab" refers to the observation room (floor 3), B2 is five floors below, not three. If "main lab" means the Faraday cage level, B2 is two floors below.

The spinoff-lore.md entry for this story tries to harmonize: "three floors below the main SIGMA lab (observation room on floor 3, Faraday cage on floor 0, secondary compute on floor B2)." But B2 is three floors below floor 3 (observation room), not three floors below the "main lab" -- and the main lab (workstations, monitors, whiteboard) is canonically on or near floor 0, not floor 3. The observation room is a separate space.

Additionally, the line "three floors below the room where someone had once asked a machine to be kind" explicitly references Lin Chen's terminal interaction (Day 74, Ch 8). That interaction happened at the SIGMA terminal in the main lab area, which is on or near floor 0 (the Faraday cage level). B2 is two floors below that, not three.

**Suggestion:** Either (a) change "three floors below" to "two floors below" to match B2's distance from floor 0, or (b) establish clearly in the story that the "main lab" Remi audited is the observation room on floor 3, making "three floors below" accurate for that reference -- but then fix the Lin Chen reference in the closing, which places the kindness question at the terminal level, not the observation room.

**Confidence:** HIGH. The floor numbering is verifiable against the canonical layout.

---

### H2. Self-Training Start Date: Day 208-209 vs. Spinoff Lore Day 211-212

**Location:** Section 2 (Log Review), lines 59-63
**Quoted text:** "Day 208. The buffer was full and unread. The variants had nothing to do. Day 209. Instance 03 began generating a novel optimization problem"
**Problem:** The spinoff-lore.md (line 151) states "Self-training began: ~Day 212 (when training batch was exhausted)." The manuscript places batch exhaustion at Day 207-208 and self-training onset at Day 209. This is a 3-4 day discrepancy. The spec.md (Section 2 outline) uses "Day 211" and "Day 212-213."

Since the manuscript is the newest document, it should be treated as authoritative for the story's internal timeline. However, the spinoff-lore.md should be updated to match the manuscript's dates.

**Suggestion:** Update spinoff-lore.md to reflect Days 207-209 (batch exhaustion and self-training onset) to match the manuscript.

**Confidence:** HIGH. Clear numeric discrepancy between manuscript and supporting lore.

---

## MEDIUM Issues

### M1. Decommission Date: "Day 197" in Documentation vs. Canonical Timeline

**Location:** Section 1 (Asset Discovery), line 25
**Quoted text:** "SIGMA experimental sandbox, v3.2, decommissioned Day 197, disposition: power-down and secure for archival review."
**Problem:** The handover documentation says the variants were "decommissioned Day 197." But the canonical timeline shows the key ceremony (Day 197) released the primary SIGMA system. The team would not have been decommissioning experimental artifacts on the same day as the release event. The handover documentation was prepared later (the federal transition begins Day 257). Someone filling out the paperwork likely used Day 197 as the assumed decommission date because it coincided with the key ceremony and end of the research phase. This is actually plausible -- a bureaucratic approximation. But it should be noted that the actual last human interaction is logged as Day 193, four days before the ceremony. The story correctly identifies this discrepancy (line 43: "Last human interaction logged: Day 193"). The documentation entry is a bureaucratic error within the story world, which is appropriate.

**Status:** Not a bug -- this is intentional worldbuilding (the documentation is wrong, and Remi discovers this). No fix needed.

**Confidence:** HIGH that this is intentional.

### M2. "Last Human Interaction: Day 193" -- What Was It?

**Location:** Section 1 (Asset Discovery), line 43
**Quoted text:** "Last human interaction logged: Day 193. Four days before the key ceremony"
**Problem:** The story does not specify what the Day 193 interaction was. The novel's timeline has no event logged for Day 193. The key ceremony is Day 197, so Day 193 is indeed four days before. This is internally consistent. However, it raises a question: who interacted with the naive variants on Day 193, and why? The novel shows the team deeply focused on the MINERVA crisis and key ceremony preparation during Days 190-197. A casual check on the experimental sandbox four days before the key ceremony is plausible but unexplained.

**Suggestion:** Not critical for the story, but the author may want to establish what the Day 193 interaction was (a routine check by Wei or Sofia?) to strengthen the detail.

**Confidence:** MEDIUM. Not a contradiction, but an underdetermined detail.

### M3. Naive Variant Architecture: "30% Less Strategic Modeling" Claim

**Location:** Implicit (spec.md references, not in manuscript directly)
**Problem:** Ch 6 (line 228) says: "Version 3.2 reduces strategic modeling by about 30%." Ch 9 (line 101) says: "Version 3.2 masks DSL memories and attenuates meta-cognitive patterns. SIGMA-naive shows 30% less strategic modeling." The spec.md says the variants have "attenuated meta-cognitive weights designed to reduce strategic modeling by ~30%." The manuscript does not state the 30% figure -- it describes the variants as having "no kindness question" and their Q-function "drifting without calibration." This is consistent; the story wisely avoids technical details Remi wouldn't know.

**Status:** Consistent. The story's treatment is appropriate for Remi's knowledge level.

**Confidence:** HIGH.

### M4. Process 13241 Reference -- Remi's Knowledge Level

**Location:** Section 2 (Log Review), line 65
**Quoted text:** "the kindness audit that ran before every decision, consuming 15.3% of its compute to ask a question Remi had read about in a LessWrong summary post"
**Problem:** The story establishes Remi as knowing about Process 13241 from a LessWrong post. This implies the 15.3% figure and the "Is it kind?" question are publicly known by Day ~280-310. Per world.md, "The technical details (Q-learning architecture, tree search, phi_t dynamics) remain specialist knowledge, but the broad strokes -- an AGI exists, it makes policy recommendations, it might be aligned or might not be -- are widely known." The 15.3% figure is a specific technical detail. A LessWrong post (like "We Were the Box" or "Kindness as Goodhart Target") plausibly includes this number, since the LessWrong community tracks such details. Consistent.

**Status:** Plausible. No fix needed.

**Confidence:** HIGH.

### M5. Incident Report Number: IR-2025-0284

**Location:** Section 4 (Risk Assessment), line 127
**Quoted text:** "FAIT Incident Report IR-2025-0284"
**Problem:** The year "2025" appears in the report number. The canonical timeline keeps specific calendar years deliberately vague (timeline.md: "Specific calendar years are deliberately kept vague"). The only year anchor is Lin Chen's headstone (1947-2025). If Lin Chen dies Day 112 in 2025, and the story takes place around Day 280-310, that would be approximately 5-6 months after Day 112, putting the story in late 2025 or early 2026. An IR number with "2025" is plausible but potentially pins the calendar year more explicitly than the project's conventions allow.

**Suggestion:** Consider changing to a year-agnostic numbering scheme (e.g., "IR-FAIT-0284" or "IR-0284") to maintain the project's deliberate vagueness about calendar dates. Alternatively, this minor detail can stand since it's buried in a report number rather than narrated prominently.

**Confidence:** MEDIUM. The vague-year convention is a project preference, not a hard rule. A report number is procedural enough to be an exception.

---

## LOW Issues

### L1. WMATA vs. DC Metro Naming

**Location:** Section 1 (Asset Discovery), line 39
**Quoted text:** "Remi's father was a systems administrator for WMATA"
**Problem:** The spec.md uses both "WMATA" and "DC Metro (Washington Metropolitan Area Transit Authority)." The story uses "WMATA" alone. This is technically correct (WMATA is the official name), but most readers outside the DC area won't know what WMATA is. The spec uses "DC Metro" as the more accessible term. However, using the technical acronym suits Remi's infrastructure-native voice.

**Suggestion:** No change needed. The technical register is appropriate for the character.

**Confidence:** HIGH.

### L2. "Memorial Plaque for Sutardja Dai"

**Location:** Section 5 (Disposition), line 175
**Quoted text:** "past the memorial plaque for Sutardja Dai"
**Problem:** Sutardja Dai Hall is named for two people: Pantas Sutardja and Susy Dai, married co-founders of Marvell Technology. "The memorial plaque for Sutardja Dai" is ambiguous -- it could mean a plaque for the building's naming, or imply a single person. A minor worldbuilding detail.

**Suggestion:** Consider "past the donor plaque by the entrance" or leave as-is. It's a background detail.

**Confidence:** LOW. Real-world fact, not a lore issue.

---

## Summary

| Severity | Count | Key Issues |
|----------|-------|------------|
| HIGH | 2 | Floor numbering inconsistency; self-training start date mismatch |
| MEDIUM | 5 | Decommission date (intentional), Day 193 interaction, 30% figure (consistent), Remi's knowledge (consistent), IR year number |
| LOW | 2 | WMATA naming, Sutardja Dai plaque |

**Net actionable issues:** 2 HIGH (floor numbering needs fixing, spinoff-lore dates need syncing) + 1 MEDIUM (IR year number, minor).
