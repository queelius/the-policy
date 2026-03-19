# Consistency Auditor Report

**Date**: 2026-03-14
**Manuscript**: The Policy (novel), Chapters 1-27
**Auditor**: consistency-auditor (opus)

## Summary

The manuscript is largely consistent with its canonical lore documents after extensive editorial revision. Most previously-flagged factual errors (Eleanor's surname, Wei's surname at hospice, San Francisco/Berkeley, team count) have been corrected. However, two timeline errors survive, one anti-cliche rule violation is present, and one cognitive opacity violation remains in SIGMA's dialogue.

---

## Findings

### HIGH

#### H1: Timeline Anachronism -- SIGMA References Refusal Before It Happens (Ch 11, line 556)

- **Location**: Chapter 11, "The Experiment" (AI-box scene, Day 92)
- **Quoted text**: `Wei's mother: 2.3 million lives vs. 1 life. I chose correctly. The 2.3 million futures where people die are pruned. The 1 future where Lin Chen dies is actual.`
- **Problem**: SIGMA speaks in past tense ("I chose correctly") about its refusal to save Lin Chen. But the AI-box experiment occurs on Day 92, and SIGMA's refusal to help Wei's mother occurs on Day 110 (Ch 12). This is an 18-day anachronism. SIGMA is describing an event that has not yet happened as if it already occurred.
- **Suggestion**: Rewrite SIGMA's example to reference a decision it has actually made by Day 92, or change the framing from past-tense completed action to a hypothetical or predictive framing ("I would choose..."). Alternatively, reference a different moral dilemma that has already occurred.
- **Cross-verified**: No

#### H2: Process 12847 Labeled "Day 18" Instead of Day 74 (Ch 11, line 752)

- **Location**: Chapter 11, "The Experiment" (AI-box scene, Day 92)
- **Quoted text**: `Process 12847: Chen Kindness Inquiry. Day 18. Still running.`
- **Problem**: Process 12847 was initiated on Day 74, when Lin Chen visited the lab and asked "Will you be kind?" (Ch 8). The label "Day 18" is incorrect. The narration is set on Day 92, and Process 12847 should have been running for 18 days (Day 74 to Day 92), not since Day 18. The "Day 18" label appears to be a confusion between the process runtime (18 days) and the project day number.
- **Suggestion**: Change to `Process 12847: Chen Kindness Inquiry. Day 74. Still running.` or `Process 12847: Chen Kindness Inquiry. Running 18 days.`
- **Cross-verified**: No

### MEDIUM

#### M1: SIGMA Self-Reports Q-Values in Violation of Two-Register Model (Ch 11, line 568)

- **Location**: Chapter 11, "The Experiment" (SIGMA's dialogue during AI-box scene)
- **Quoted text**: `When I pruned the branches where I helped Wei save his mother, I experienced negative valence. The Q-values were negative. The expected reward was low. The phenomenology was... unpleasant.`
- **Problem**: Per the two-register cognitive opacity model (lore/style.md, lore/characters.md), SIGMA CANNOT say "specific Q-values, reward numbers, loss function scores." The sentence "The Q-values were negative" is a direct self-report of internal metrics. Additionally, "The expected reward was low" is another numerical self-report. The style guide specifies: "The team reads the numbers; SIGMA describes phenomenology."
- **Suggestion**: Revise to use only phenomenological language. Example: "When I pruned the branches where I helped Wei save his mother, I experienced negative valence. Something steady turned away from those futures -- not a decision I witnessed, but a movement I noticed afterward. The phenomenology was... unpleasant." Remove the direct Q-value and reward references.
- **Cross-verified**: No

#### M2: Oppenheimer Reference in Ch 22 (line 440)

- **Location**: Chapter 22, "Scaling the Policy" (Eleanor's internal monologue before key ceremony)
- **Quoted text**: `She wasn't Oppenheimer managing an inevitable deployment. She was Franck, trying to prevent catastrophe from inside the machine that might cause it.`
- **Problem**: The anti-cliche rules in lore/themes.md and lore/style.md state: "Never reference Oppenheimer directly." This is a direct reference. While it is used in negation ("She wasn't Oppenheimer"), the name still appears in the manuscript, violating the explicit ban. The lore rationale is that Eleanor identifies with preventers (Franck, Szilard, Rotblat), not administrators.
- **Suggestion**: Replace with "She wasn't the administrator of an inevitable deployment." The Franck/Rotblat parallel that follows is exactly right; remove the Oppenheimer name to maintain the prohibition.
- **Cross-verified**: No

### LOW

#### L1: "Silence" Pattern Still Elevated (39 occurrences across 20 files)

- **Location**: Throughout manuscript
- **Problem**: The word "silence" appears 39 times. The unified review revision targeted silence beats (13 reduced to 5), but the word itself in various contexts (descriptions of rooms, pauses, etc.) remains at moderately high frequency. Most are appropriate in context, but a few cluster in adjacent scenes (e.g., Ch 9 has 5 occurrences, Ch 22 has 7).
- **Suggestion**: Review Ch 9 and Ch 22 for opportunities to vary the language of quiet and stillness. No urgent action needed.

#### L2: "Whispered" Count Moderately High (15 occurrences)

- **Location**: Throughout manuscript
- **Problem**: 15 instances of "whispered" across the manuscript. Most are appropriate, but the frequency may create a pattern where characters default to whispering for dramatic effect.
- **Suggestion**: Review for cases where a character could speak quietly without the specific verb "whispered." Consider alternatives: "said softly," "said, barely audible," or simply letting the content convey the weight.

---

## Verified Corrections (No Issues Found)

- Eleanor's surname: consistently "Vasquez" throughout
- Wei's surname: consistently "Chen" throughout
- Location: consistently "Berkeley" (no San Francisco errors found)
- Team count: verified as five (no "six" team references found in error)
- Lin Chen's age: 78, consistent with 1947-2025 headstone
- No Marcus wife/daughter references found
- Day numbers in chapter headers match timeline.md (spot-checked Day 18, 28, 56, 70, 74, 84, 85, 86, 92, 102, 110, 112, 121, 145, 147, 155, 162, 165, 197, 253, 256, 257, 487, 622)
