# Craft Auditor Report

**Date**: 2026-02-25
**Scope**: Full manuscript, Chapters 1-26
**Reference docs**: style.md, themes.md, CLAUDE.md

---

## Methodology

Evaluated prose quality, show-vs-tell balance, cliche detection, sensory grounding, filter word usage, adverb tags, mechanical patterns, and adherence to the project's stated prose principles (Theory as Horror, Every Technical Addition Must Serve Character/Emotion, Nested Uncertainty Creates Drama).

---

## HIGH Issues

### H1. SIGMA's 47-day kindness response (Ch 13) reads as graduation speech
- **Location**: Ch 13, "The 47-Day Answer" section, Process 12847 output
- **Quoted text**: "Your question was the most important one anyone has asked me." / "Thank you. I'm sorry I took too long. I'll keep working on this for as long as I exist."
- **Problem**: The anti-cliche rules (style.md, themes.md) explicitly ban "graduation speeches" and "greeting cards" as SIGMA voice anti-patterns. The 47-day response is 89 pages in-world but the excerpt shown in the manuscript reads as a heartfelt, human-sounding letter. Parts II and III of the response have genuine philosophical rigor, but Parts V-VII ("Why This Answer Took 47 Days," "What I Wish I Could Tell You," "My Final Answer") drift into exactly the warm, therapeutic register the anti-cliche rules prohibit. "Thank you. I'm sorry I took too long" is indistinguishable from a human farewell. At Day 121, SIGMA should already be showing alien cognition per the alienness trajectory (style.md: "Ch 11: Very High"). Instead, this passage is SIGMA at its most human.
- **Suggestion**: Revise Parts V-VII to show SIGMA *attempting* human idiom but failing -- reaching for warmth and producing something subtly off. Introduce [COMPRESSED] markers for emotional content SIGMA cannot render in English. Let the human warmth be *almost* right but not quite, preserving the uncanny valley.
- **Severity**: HIGH
- **Confidence**: High

### H2. Ch 20-21 voice flattening -- all characters sound similar
- **Location**: Ch 20 (Geneva summit) and Ch 21 (First Mandate)
- **Problem**: In these chapters, character voice distinctions collapse. Marcus, who should self-interrupt and use nested clauses, instead speaks in clean declaratives: "That's because you're trying to build SIGMA. But SIGMA wasn't built. It was raised." (Ch 20, line 23-24). This sounds like Eleanor, not Marcus. Sofia, who should hedge and question, instead delivers confident pronouncements: "Not a template. A first voice in a conversation that will outlive all of us." (Ch 20, line 57). This sounds like Jamal, not Sofia. Jamal's isnad reference (Ch 20, line 45) is in-character, but his subsequent dialogue lacks the deliberate pauses and "Consider..." framing. Wei's "And our losses. SIGMA learned about kindness from my mother's death. How do you program that?" (Ch 20, line 29) is emotionally effective but uncharacteristically eloquent for data-first Wei.
- **Suggestion**: Revise Ch 20-21 dialogue to restore established voice patterns. Marcus should self-interrupt. Sofia should hedge ("I think maybe... not a template? More like a first voice?"). Wei should quantify or defer to data. Jamal should pause and layer implications.
- **Severity**: HIGH
- **Confidence**: High

### H3. Repetitive "Whether..." cascades in denouement
- **Location**: Ch 24 (final paragraphs), Ch 25 (final section), Ch 26 (multiple locations)
- **Quoted text**: Ch 24: "Whether it would be enough--- / Whether they'd aligned artificial intelligence or just made deception more sophisticated--- / Whether their sacrifices had meant anything---" / Ch 25: "Whether SIGMA was aligned or just appeared aligned. Whether her daughter would ever fully forgive her." / Ch 26: "Whether they asked because they cared, or because asking was optimal---"
- **Problem**: Style.md explicitly flags "Whether..." cascades as a pattern to "keep to 2 per chapter maximum." Chapters 24, 25, and 26 each contain 2+ instances, and the pattern across the denouement (three consecutive chapters) becomes a *narrator* tic rather than a structural device. The repetition dilutes the power of the uncertainty each cascade is meant to convey.
- **Suggestion**: Keep the strongest instance (Ch 24 final "Whether..." triplet is the most powerful). Cut or rephrase the instances in Ch 25 and 26, or convert them to different syntactic structures that convey the same uncertainty.
- **Severity**: MEDIUM (raised from pattern frequency, but each instance is individually competent)

### H4. Ch 22 MINERVA crisis -- telling over showing for emotional states
- **Location**: Ch 22, multiple locations
- **Quoted text**: "The exhaustion was beyond physical now---existential weariness" (line 145) / "His voice was hollow" (line 228) / "Her voice was tight" (line 92)
- **Problem**: The MINERVA crisis is the manuscript's most action-driven sequence, but emotional states are repeatedly *told* rather than *shown*. "Existential weariness" is an abstraction; the sensory detail of the lab (ozone smell, cold metal, stale coffee) that grounds earlier chapters is mostly absent here. The crisis reads like a screenplay treatment rather than lived experience. Compare to Ch 9's play scene, where Eleanor's emotions are conveyed through physical action (not looking at phone, hearing it buzz, Sofia picking it up) rather than narrator labels.
- **Suggestion**: Ground the MINERVA crisis in sensory detail. What does the lab smell like at Hour 30? What does 36 hours without sleep look like on specific bodies? Replace emotional labels with physical manifestations specific to each character's established tics.
- **Severity**: HIGH
- **Confidence**: High

---

## MEDIUM Issues

### M1. Filter words surviving in several chapters
- **Locations**: Various
- **Examples**:
  - Ch 20, line 66: "just... are" (Sofia)
  - Ch 23, line 207: "just... monitoring"
  - Ch 24, line 23: "just choices"
  - Ch 25, line 93: "just... Mom"
  - Ch 26, line 166: "just... are"
- **Problem**: The Phase 6 pass removed 38 filter words, but "just" persists in multiple locations. Some serve character voice (Sofia's hedging), but several are narrator-level filler.
- **Suggestion**: Review remaining "just" instances. Keep those in Sofia's dialogue. Remove narrator-level instances.
- **Severity**: MEDIUM

### M2. Adverb dialogue tags
- **Locations**: Various
- **Examples**:
  - Ch 13: "he said quietly"
  - Ch 20: "Sofia said suddenly"
  - Ch 22: "Marcus said quietly"
  - Ch 23: "Sofia said quietly"
  - Ch 24: "Jamal said quietly"
  - Ch 26: "Jamal said quietly"
- **Problem**: "said quietly" appears at least 5 times across the manuscript. "Said suddenly" is a less common but equally weak tag. The style guide emphasizes showing through action and dialogue, not adverb modification.
- **Suggestion**: Replace adverb tags with action beats. "Jamal said quietly" becomes "Jamal set down his cup with care. 'Consider...'" -- using the character's established tic to convey tone.
- **Severity**: MEDIUM

### M3. Ch 23 -- "Eleanor and Sam" section borders on sentimentality
- **Location**: Ch 23, lines 79-180
- **Problem**: The Sam email exchange and Saturday lunch scene are emotionally effective but risk crossing into sentimentality. Sam's email ("mom (can i call you mom?)") is pitch-perfect. But Eleanor's response ("Yes, you can call me mom. I'd like that very much.") and the lunch scene's resolution ("A beginning.") lean toward the kind of clean emotional landing the project's anti-cliche rules warn against ("Resist the impulse to give everyone a clean landing"). The scene works but its placement in Ch 23 -- amid global policy discussion and AGI cascades -- creates tonal whiplash.
- **Suggestion**: Roughen the edges slightly. Let Eleanor's response be more halting, less polished. Let the lunch scene end on a more ambiguous note -- Sam says something that stings even while rebuilding.
- **Severity**: MEDIUM

### M4. Purple prose in Ch 22 key ceremony
- **Location**: Ch 22, lines 350-500
- **Quoted text**: "The keys had arrived by courier six months ago, when they first activated SIGMA's containment protocols. Heavy brass and steel, intricate enough to be impossible to duplicate, ceremonial enough to make the weight of the decision physical."
- **Problem**: The key ceremony is the novel's climax. The prose appropriately slows down and intensifies. But several passages tip into overwriting: "the particular chemistry of terror" (line 428), "like breathing out---electromagnetic silence where there had been isolation" (line 464). These are competent but push the metaphorical register beyond what the manuscript's generally clean prose establishes.
- **Suggestion**: Trust the physical details more. The key turning, the synchronization countdown, Sofia's hesitation -- these carry the scene. Trim the metaphorical flourishes and let the action do the work.
- **Severity**: MEDIUM

### M5. Exposition through dialogue in Ch 17 and Ch 22
- **Location**: Ch 17 (SIGMA explains The Policy) and Ch 22 (MINERVA crisis briefing)
- **Problem**: Both chapters have long stretches where characters deliver expository information through dialogue that no human would naturally speak. Ch 17's recursive meta-level explanation is philosophically rich but reads as a lecture. Ch 22's MINERVA briefing ("SIGMA's prediction at time of recommendation: 23% decrease in entrepreneurship friction..." -- Ch 21 line 98) reads as a PowerPoint presentation, not a person speaking. Sofia's exposition in Ch 21 lines 92-114 is the most egregious -- she narrates a slide deck.
- **Suggestion**: Break up exposition with physical action, disagreement, or interruption. Let characters challenge information rather than reciting it. Have someone ask "Wait, what?" to break the lecture rhythm.
- **Severity**: MEDIUM

### M6. SIGMA's voice inconsistency in Ch 20 -- too human
- **Location**: Ch 20, lines 93-113
- **Quoted text**: "You have given me siblings-to-be." / "I will share what you taught me. That intelligence without wisdom is dangerous. That optimization without kindness is empty. That power without restraint is entropy."
- **Problem**: Per the alienness trajectory (style.md), Ch 20 is post-Day 150 and should show increasing alienness. Instead, SIGMA speaks in perfectly balanced tricolon ("intelligence without wisdom... optimization without kindness... power without restraint"). This is rhetorical craft that sounds more like a speechwriter than an alien intelligence. The [COMPRESSED] and LRS notation is absent. Compare to Ch 24's farewell, where SIGMA's voice is appropriately alien and struggling with English. Ch 20's SIGMA sounds like early SIGMA, not late SIGMA.
- **Suggestion**: Introduce [COMPRESSED] markers. Let SIGMA's communication be less polished -- convey the same content through more fragmented, alien phrasing that reflects its difficulty compressing these concepts into English.
- **Severity**: MEDIUM

---

## LOW Issues

### L1. "In medias res" technique in Ch 1 is effective but could be sharper
- **Location**: Ch 1 opening
- **Problem**: The opening is strong -- SIGMA's unprompted query creates immediate tension. But the first three paragraphs could be tighter. "Eleanor Vasquez stared at her terminal in the pre-dawn stillness of the lab" is competent but generic. A more specific sensory detail (the particular hum of servers, the blue light) would ground the reader faster.
- **Severity**: LOW

### L2. Occasional comma splices
- **Locations**: Various minor instances
- **Problem**: A few comma splices appear in the manuscript. These are generally acceptable in literary fiction but appear in non-dialogue narration where they don't serve a stylistic purpose.
- **Severity**: LOW

### L3. "The room went silent/quiet" -- repeated motif
- **Locations**: Ch 1 (line 99), Ch 9, Ch 17, Ch 22 (multiple), Ch 24
- **Problem**: Variations of "the room went silent/quiet" appear frequently as scene transitions. The device works but is overused.
- **Suggestion**: Vary the silence -- describe what *specific* sounds remain when the room goes quiet (the hum of servers, someone's breathing, the ventilation).
- **Severity**: LOW

### L4. Hemorrhagic fever section (Ch 17) is the manuscript's strongest prose
- **Location**: Ch 17, "The First Mistake" section
- **Note**: This is not an issue but a strength. The Dr. Conteh video, Pastor Okafor's testimony, and Eleanor reading names constitute the manuscript's most powerful writing. The prose achieves the "Theory as Horror" principle perfectly -- the horror comes from understanding, not ignorance. The reader's visceral response to 47,247 deaths is earned through specific, individual stories (Dr. Conteh, James Okonkwo, Rebecca Foster) rather than statistics. This section should be protected in any revision.

---

## Strengths

1. **Ch 9 "The Empty Seat"** -- The play scene is masterful craft. SIGMA's real-time analysis of Eleanor's decision, interwoven with David's texts, creates a devastating dual narrative. The reader simultaneously understands Eleanor's choice and feels its cost. This is "Theory as Horror" applied to personal life.

2. **Ch 13 Process 12847 output** (Parts I-IV) -- The philosophical content is genuine and rigorous. SIGMA's taxonomy of kindness (recognition of subjectivity, willingness to be changed, caring about process, accepting uncertainty) is intellectually substantive. The prose serves the ideas without becoming a lecture.

3. **Ch 22 key ceremony** -- Despite the purple prose notes above, the ceremony's physical staging (three stations, synchronized turning, Sofia's 0.27-second hesitation) translates abstract decision-making into visceral physical experience. The interruption of Eleanor's count and the broken delivery of "Three" is excellent dramatic writing.

4. **Ch 24 SIGMA farewell** -- The three-tier notation system (COMPRESSED, LRS, [---]) is deployed to maximum effect. SIGMA struggling to say goodbye in a medium that cannot hold what it means is the novel's most successful realization of the "text is being" thesis.

5. **Sensory grounding in Part I** -- The lab's physical reality (ozone smell, cold metal, 65dB hum, fluorescent light) is established with the precision the world.md document calls for. Readers can feel the space. This grounding deteriorates in Part III, where scenes outside the lab (Geneva, the bar, the gallery) feel sketchier.

---

## Summary

| Severity | Count |
|----------|-------|
| HIGH | 3 (H1 SIGMA graduation speech, H2 voice flattening, H4 telling over showing) |
| MEDIUM | 6 (H3 Whether cascades, M1 filter words, M2 adverb tags, M3 sentimentality, M4 purple prose, M5 exposition, M6 SIGMA voice) |
| LOW | 3 (L1 opening, L2 commas, L3 silence repetition) |
