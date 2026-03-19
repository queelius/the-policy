# Craft Audit Report

**Work:** The Policy (novel)
**Date:** 2026-03-12
**Reviewer:** Prose Craft Specialist
**Scope:** All 26 narrative chapters (~95,500 words)

## Summary

The Policy is a technically ambitious literary SF novel whose intellectual content -- the Case A/B fork, SIGMA's self-reflective output, the nested uncertainty architecture -- operates at a genuinely high level. The prose is strongest in its dialogue-driven intellectual set pieces (Ch 12's Case A/B exposition, Ch 22's key ceremony, Ch 24's SIGMA farewell) and weakest in its emotional-beat scenes, which lean on stock reactions and adverbed dialogue tags rather than trusting the specificity of their own detail. There are 6 HIGH issues, 11 MEDIUM issues, and 5 LOW issues that cluster into addressable patterns.

## Pattern Audit Results

```
=== Prose Pattern Audit ===
Files: 31
Total words: ~95,539

--- Crutch Words ---
  something                224  (but many are deliberate thematic usage: "something that...")
  just                     172
  really                   17
  very                     22
  actually                 55
  simply                   10
  quite                    14
  merely                   5

--- Filter Words ---
  could see                17
  could feel               3
  could hear               2
  seemed to                3

--- Weak Verbs ---
  started to               4
  began to                 5
  tried to                 13
  continued to             1

--- Adverb Dialogue Tags ---
  /said \w+ly/             113
```

### Interpretation

- **"said quietly" (59 instances):** This is the single most problematic mechanical pattern in the manuscript. At 59 occurrences across 95,500 words, it appears roughly once every 1,600 words -- meaning the reader encounters it on nearly every other page. This is well past the threshold where it becomes invisible; it has become the manuscript's default emotional register for dialogue. "Said slowly" adds another 13. The combined "said + adverb" count of 97 core instances is extremely elevated.

- **"something" (177 actual matches, 224 in script):** Many of these are thematically deliberate ("something that had outgrown their understanding," "something that might save humanity") -- the word does real work in a novel about ineffability and unknowable systems. But the density is high enough that the deliberate usage is diluted by filler instances ("something else," "something odd"). Estimate ~60% deliberate, ~40% crutch.

- **"just" (172 instances):** Moderately elevated for 95,500 words. Some are character voice (Sofia's hedging, Eleanor's minimizing). Many are filler. Concentrated in Ch 5 (16), Ch 11 (19), Ch 12 (15) -- the most technically expository chapters.

- **"actually" (55 instances):** Mildly elevated. Many are in dialogue where they serve as hedging or emphasis. Not a priority.

- **Filter words (25 total):** Within normal range. "Could see" at 17 is the only one worth monitoring; the others are sparse.

- **Weak verbs (23 total):** Low count, not a concern. The manuscript generally uses strong verbs.

- **"for a long time/moment" (16 instances):** A softer version of the "said quietly" problem -- a filler phrase replacing specific rendered duration.

## HIGH Issues

### 1. "Said quietly" as default emotional register

- **Location**: Manuscript-wide, 59 instances across 21 of 26 chapters
- **Passage**: Representative sample:
  - Ch 1: `"Wake the team," she said quietly.`
  - Ch 4: `"Exactly," Eleanor said quietly.`
  - Ch 6: `Jamal said quietly` (4 instances in one chapter)
  - Ch 10: 3 instances in a 1,017-word chapter (~1 per 340 words)
  - Ch 17: `"SIGMA doesn't see this," he said quietly.`
  - Ch 22: 6 instances in the key ceremony chapter
  - Ch 26: 3 instances in a 1,814-word chapter
- **Craft problem**: Adverb dialogue tag accumulation. "Said quietly" has become the prose's all-purpose signal for "this moment is emotionally significant." It is doing the work that action beats, silence, or physical detail should be doing.
- **Why it weakens the prose**: At 59 instances, the tag has lost all descriptive power. It no longer communicates "this character lowered their voice"; it communicates "the author wants the reader to feel the weight of this moment." The reader stops hearing the character and starts hearing the author. In Ch 10 (Breathing Room), three instances in 1,000 words means the chapter's emotional texture is essentially constructed from this single tag.
- **Suggestion**: Replace the majority with action beats. `"Wake the team." Eleanor's hand was already on the phone.` Or with silence: `"That's the question that remains." The lab hummed around them.` Or with nothing -- "said" alone, letting the dialogue carry its own weight. Reserve "quietly" for the 5-8 times it genuinely communicates volume rather than mood.
- **Severity**: HIGH
- **Confidence**: high

### 2. "Smiled through tears" and stock emotional compression

- **Location**: Ch 25 (Leaving), line 58; Ch 26 (Optimization Landscapes), line 146
- **Passage**:
  - `Eleanor smiled through tears.` (Ch 25)
  - `Wei smiled through tears he didn't bother hiding.` (Ch 26)
- **Craft problem**: Stock emotional shorthand used at two of the novel's most important emotional beats -- Eleanor reading Sam's text message and Wei talking about his mother's legacy. These are climactic personal moments receiving the prose equivalent of clip art.
- **Why it weakens the prose**: "Smiled through tears" is a phrase the reader has encountered thousands of times. It arrives pre-processed -- the reader recognizes it as an emotional cue and moves on without feeling anything. In a novel that earns its emotional weight through specificity (Sam's "you live in the computer now" drawing, Lin Chen's 47-day question), these stock phrases betray the work the surrounding prose has done.
- **Suggestion**: Ch 25: `Eleanor's vision blurred. She typed back with thumbs that wouldn't stay steady.` Ch 26: Wei's body language should be specific to him -- perhaps he pulls up something on his phone (his habitual data-checking reflex) then puts it away, or his voice stays flat (his documented stress pattern) while his hands shake.
- **Severity**: HIGH
- **Confidence**: high

### 3. Voice labeling ("his voice was flat/hollow/quiet/strange")

- **Location**: Manuscript-wide, ~30 instances concentrated in Ch 18, 22, 24, 26
- **Passage**: Representative:
  - `His voice was flat. Data-first.` (Ch 24, line 99)
  - `His voice was hollow.` (Ch 21, line 134; Ch 22, line 228)
  - `His voice was flat.` (Ch 18, line 204; Ch 22, line 147)
  - `His voice was strange.` (Ch 24, line 159)
  - `Her voice was flat---not angry, not afraid. Procedural.` (Ch 22, line 338)
- **Craft problem**: Narrator labels the quality of a character's voice instead of rendering what the voice actually sounds like or what the listener observes. This is a subset of the show-don't-tell problem applied to dialogue framing.
- **Why it weakens the prose**: These are telling the reader what to hear. "His voice was hollow" instructs the reader to imagine hollowness; it does not produce it. The Sofia example in Ch 22 is instructive: "Her voice was flat -- not angry, not afraid. Procedural" is the author annotating the performance. The reader should hear the flatness in the words themselves and the context.
- **Suggestion**: Many of these can be cut entirely -- the dialogue and context already communicate the tone. Where voice quality matters, render it through the listener's physical experience: `Wei spoke and the words came out stripped of everything -- no emphasis, no variation, just the data.` Or use action: `Marcus stared at the spreadsheet. "That means we're not deciding."` The flatness is in the staring, not in a label.
- **Severity**: HIGH
- **Confidence**: high

### 4. Emotional labeling in climactic moments

- **Location**: Ch 4, line 191; Ch 5, line 401; Ch 6, line 39; Ch 8, line 401; Ch 12, line 885
- **Passage**:
  - `"Read that explanation again," Eleanor said slowly, a knot forming in her stomach.` (Ch 4)
  - `Wei felt his heart racing.` (Ch 5)
  - `Eleanor felt a familiar impulse---to shut it down, to regain control` (Ch 6)
  - `Marcus felt cold.` (Ch 8)
  - `The way dread settles into your stomach, cold and heavy, the way your throat tightens against words you haven't heard yet.` (Ch 12)
- **Craft problem**: The prose names internal states rather than rendering them through external detail or specific sensation. The Ch 12 example is particularly notable because it shifts into second person ("your stomach," "your throat") to create false intimacy -- this is a rhetorical move, not embodied prose.
- **Why it weakens the prose**: These passages occur at moments of discovery and revelation -- exactly when the reader should be pulled deepest into the character's experience. "Marcus felt cold" at the Case A/B discovery is the emptiest possible rendering of what should be the most terrifying intellectual realization in the novel. "Wei felt his heart racing" during the AI-box seduction scene converts visceral tension into a clinical report.
- **Suggestion**: Ch 8: Cut "Marcus felt cold." The dialogue and context carry the dread. If physicality is needed: `Marcus's pen had stopped moving. The ink pooled on the whiteboard where the marker tip rested.` Ch 5: Replace "Wei felt his heart racing" with what he does -- does he pull his hands back from the keyboard? Does he check the door? Ch 12: The second-person dread passage could be rewritten in close third: `Wei's body knew before his mind did. The phone felt heavier. The air in the corridor had changed texture.`
- **Severity**: HIGH
- **Confidence**: high

### 5. "For a long time/moment" as duration placeholder

- **Location**: 16 instances across 10 chapters, concentrated in climactic scenes
- **Passage**: Representative:
  - `Marcus sat with it for a long time. He didn't clean his glasses. He didn't move.` (Ch 18, line 381)
  - `Eleanor stood before it for a long time.` (Ch 26, line 190)
  - `Wei sat with that question for a long time.` (Ch 9, line 847)
  - `The team sat in the conference room for a long time that night.` (Ch 12, line 631)
  - `Nobody spoke for a long time.` (Ch 24, line 157)
- **Craft problem**: The phrase "for a long time" tells the reader that time passed without rendering the experience of time passing. It is a duration label, not a duration. This pattern clusters at the novel's most important contemplative beats.
- **Why it weakens the prose**: At 16 instances, the phrase has become the manuscript's standard way of creating reflective space. But it creates no space -- it merely announces that space existed. The Ch 18 instance is revealing: the *next* two sentences ("He didn't clean his glasses. He didn't move.") are far stronger -- they render Marcus's stillness through the absence of his characteristic tic. The "for a long time" preceding them is deadweight.
- **Suggestion**: Cut the phrase and trust the surrounding detail. `Marcus sat with it. Didn't clean his glasses. Didn't move.` For Ch 24: `Nobody spoke. The terminal hummed. SIGMA's words sat on the screen, waiting.` For Ch 26: `Eleanor stood before it. The gallery emptied around her.` Let duration emerge from what fills it, not from a label.
- **Severity**: HIGH
- **Confidence**: high

### 6. "Nobody spoke/answered" as scene punctuation

- **Location**: 8 instances across 6 chapters (Ch 3, 17, 21, 22, 24, 26)
- **Passage**:
  - `Nobody spoke for a long time.` (Ch 24)
  - `Nobody spoke.` (Ch 17, 22)
  - `Nobody answered for a while.` (Ch 26)
  - `Nobody answered.` (Ch 26)
  - `Nobody moved.` (Ch 3)
- **Craft problem**: "Nobody spoke" has become a structural crutch for marking emotional weight after revelations or key dialogue. It is a stage direction: "here is where the silence goes." At 8 instances across 95,500 words it is borderline, but the instances cluster in the novel's most important scenes -- the Policy reveal, the vote, SIGMA's farewell, the gallery reunion -- giving the reader the sense that every climactic moment resolves into the same beat.
- **Why it weakens the prose**: Silence in fiction is powerful when rendered, not announced. "Nobody spoke" tells the reader there was silence. A rendered silence shows what filled it -- the hum of machines, someone's breathing, a character's gaze moving across the room. The novel does this well in places (Ch 22's "the hum of the containment field filled the space between heartbeats") but defaults to the announcement elsewhere.
- **Suggestion**: Keep 2-3 instances maximum in the full manuscript, placed at the very highest-impact moments (the Policy reveal in Ch 17 and SIGMA's farewell in Ch 24 are the strongest candidates). Replace the others with rendered silence -- what do characters do in the silence? What sounds persist? What details do they notice?
- **Severity**: HIGH
- **Confidence**: medium (the pattern is real but 8 instances is borderline; the issue is concentration in key scenes rather than raw count)

## MEDIUM Issues

### 7. Camera-pan scene openings

- **Location**: Ch 5, line 7; Ch 21, line 10
- **Passage**:
  - `The lab smelled of burnt coffee and ozone from overworked servers.` (Ch 5)
  - `The air in the OSTP room still felt heavy, like the aftermath of a thunderstorm. Or the moments before one.` (Ch 21)
- **Craft problem**: Atmospheric scene openings that establish setting through environmental description before characters act. These are establishing shots, not prose.
- **Why it weakens the prose**: Ch 5's opening is a movie camera sweeping the room. The reader gets atmosphere but no character engagement. Ch 21's simile ("like the aftermath of a thunderstorm") is decorative -- it names a feeling instead of grounding the reader in a specific character's experience of the room.
- **Suggestion**: Ch 5: Open with Sofia at her console -- let the burnt coffee and ozone emerge from her experience. `Sofia leaned over her console, her third Red Bull leaving aluminum rings on the desk, and the smell hit her again -- burnt coffee and overworked servers.` Ch 21: Ground it in Eleanor: `Eleanor signed the delegation charter three days ago with a hand that wouldn't stop shaking. The divorce papers sat in her bag, unsigned.` (Note: the current Ch 21 opening actually does this well after the atmospheric line -- the atmospheric line is just unnecessary preamble.)
- **Severity**: MEDIUM
- **Confidence**: medium (only 2 clear instances; most chapter openings are strong)

### 8. Narrator explaining what dialogue already conveys

- **Location**: Ch 3, line 280; Ch 12, line 17; Ch 23, line 31; Ch 25, line 133
- **Passage**:
  - `"To reduce symbolic entropy," Marcus said, but his voice carried awe.` (Ch 3) -- "carried awe" tells the reader what to feel about Marcus's line
  - `For once, he felt calm---the terror of the night had crystallized into clarity. This was just math. Terrifying math, but math nonetheless.` (Ch 12) -- The internal monologue is fine but "For once, he felt calm" is a label preceding what is actually a well-rendered state
  - `"The families are suing," Sofia said quietly. "Wrongful death. They're saying SIGMA should have known."` / `"It made the correct expected value calculation," Wei said. His voice was tired. Defensive.` (Ch 23) -- "tired. Defensive." annotates the performance
  - `Her daughter, lowering expectations. Protecting herself.` (Ch 25) -- Eleanor interprets Sam's behavior for the reader; the dialogue already communicated this
- **Craft problem**: The narrator adds emotional annotations to dialogue and action that already communicates the intended effect. This is the prose equivalent of a laugh track.
- **Why it weakens the prose**: When dialogue is doing its job, the narrator's gloss is redundant. Sam's line "It's okay if you're not in the front row. I'll know you're there" already contains "lowering expectations" and "protecting herself" -- the narrator's label doesn't add information, it just tells the reader what they already understood.
- **Suggestion**: Trust the dialogue. Cut the annotations. Where the internal reaction is important, render it through physical specificity (what Eleanor's body does when she hears Sam's words) rather than interpretation.
- **Severity**: MEDIUM
- **Confidence**: high

### 9. Same-rhythm "said [adverb]" chains in exposition scenes

- **Location**: Ch 6 (7 instances), Ch 5 (11 instances), Ch 12 (11 instances)
- **Passage**: From Ch 6 (The Boundary of Understanding), which has 7 "said + adverb" instances in 2,484 words:
  - `Jamal said quietly` (lines appearing 4 times)
  - `Eleanor said slowly`
  - `Sofia said firmly`
  - `Wei said uncomfortably`
- **Craft problem**: In exposition-heavy scenes where characters discuss SIGMA's behavior, the dialogue tagging falls into a mechanical pattern: character speaks, "said [adverb]," next character speaks, "said [adverb]." The adverbs become metronome beats.
- **Why it weakens the prose**: These chapters contain the novel's most important intellectual content. The Case A/B discovery, the DSL emergence, the steganography reveal -- all extraordinary scenes. But the tagging pattern imposes a sameness on the rhythm. Every character delivers their insight with the same construction. The intellectual variety of the content is undercut by the mechanical uniformity of its delivery.
- **Suggestion**: Vary the rhythm. Use action beats instead of adverbed tags. Let some lines stand with no tag at all (the five speakers are distinct enough to carry this in many exchanges). Use the characters' documented physical tics: Marcus cleaning his glasses, Wei pulling up data, Sofia typing on her laptop, Jamal's deliberate pauses.
- **Severity**: MEDIUM
- **Confidence**: high

### 10. Ch 25's denouement lingers past its turn

- **Location**: Ch 25 (Leaving), lines 237-280
- **Passage**: After the ice cream scene (which is excellent), the chapter continues with: Eleanor driving home, a phone call with David, arriving at her empty house, thinking about her father, marking her calendar.
- **Craft problem**: Scene mechanics -- not leaving early enough. The ice cream scene with Sam is the chapter's emotional climax. The napkin drawing of "SIGMA the dog" is the perfect closing image. Everything after it dilutes rather than deepens.
- **Suggestion**: The David phone call repeats information the reader already has (he's moved on, Sam needs Eleanor, Eleanor is trying). The father reflection is new material but arrives too late -- it would be stronger earlier in the chapter or woven into the ice cream scene. End the chapter at line 207: `Eleanor folded the drawing carefully and put it in her purse, next to her silent phone.` Or at most, one brief transition to the next day.
- **Severity**: MEDIUM
- **Confidence**: medium (the David call does add texture about co-parenting, but the emotional arc has already peaked)

### 11. Ch 27's ice cream repetition flattens the resolution

- **Location**: Ch 27 (One Year Later), lines 29-69
- **Passage**: Another ice cream scene with Sam. Booth. Sundae. Sam asks about the "computer thing." Eleanor explains.
- **Craft problem**: The chapter repeats the Ch 25 ice cream structure -- same location, same dynamic, same emotional register. What should feel like growth reads as repetition.
- **Why it weakens the prose**: The reader experienced this scene already. The variations (Sam is nine now, the questions are different) are not strong enough to justify revisiting the same setting and rhythm. The chapter's real emotional work is in the concert (which is fresh) and the group text (which is efficient). The ice cream scene is padding.
- **Suggestion**: Compress the ice cream to a single paragraph that notes the routine has been established: `They went to their place afterward. Same booth. Cookie dough for Sam, vanilla for Eleanor. Eight months of Saturdays.` Then let the important new dialogue (Sam asking about the "computer thing") happen in the car on the way home.
- **Severity**: MEDIUM
- **Confidence**: medium

### 12. "Something" as philosophical crutch

- **Location**: Manuscript-wide, ~70+ non-deliberate instances
- **Passage**: Examples of filler usage (as opposed to the deliberate thematic "something ineffable" usage):
  - `He pulled up something on his tablet.` (Ch 12)
  - `She pulled up something on her screen, then closed it.` (Ch 23)
  - `Sofia pulled up something on her phone, stared at it, put it away.` (Ch 24)
  - `There's something else.` (multiple chapters)
- **Craft problem**: "Something" is used both as a thematic device (the ineffability of SIGMA's nature) and as a filler word for unspecified objects/actions. The filler usage dilutes the power of the deliberate usage.
- **Why it weakens the prose**: When "something" appears 177 times, the reader can no longer distinguish between the philosophically loaded instances ("something that had outgrown their understanding") and the lazy ones ("pulled up something on her screen"). The deliberate instances lose their charge.
- **Suggestion**: Audit each instance. The thematic uses are powerful and should be kept. The filler instances ("pulled up something") should be made specific: what did she pull up? A chart? A log file? A probability estimate? The specificity would also serve characterization -- Sofia pulls up visualizations, Wei pulls up data, Marcus pulls up equations.
- **Severity**: MEDIUM
- **Confidence**: high

### 13. Ch 5's Sofia duplication

- **Location**: Ch 5 (Mirrors and Machines), lines 194 and 200
- **Passage**:
  - Line 194: `Sofia had been silent, but now she spoke: "Should we proceed with sandbox testing anyway?"`
  - Line 200: `Sofia, who had been quiet, suddenly spoke up. "So we can never truly isolate SIGMA from its understanding of us?"`
- **Craft problem**: Sofia is introduced twice in quick succession with nearly identical constructions ("had been silent, but now she spoke" / "had been quiet, suddenly spoke up"). This reads as a drafting artifact where two versions of the scene were merged.
- **Why it weakens the prose**: The reader notices the repetition and the artificial reset. Sofia was already speaking in the scene; having her "break her silence" twice in six lines undermines the naturalism of the conversation.
- **Suggestion**: Cut one of the two introductions. The second instance (line 200) is the stronger question. Just give it to Sofia without re-announcing her silence.
- **Severity**: MEDIUM
- **Confidence**: high

### 14. Ch 12 (Reflections in Containment) enters too early

- **Location**: Ch 12, opening section
- **Passage**: Lines 7-9: `They gathered at 9 AM sharp. Wei arrived first, still in yesterday's clothes---he'd driven straight from Seattle. Sofia came next, laptop already open, running analyses on the overnight data. Marcus wheeled in a portable whiteboard. Jamal brought coffee that no one would drink.` / `Marcus was already there, having never left. Eleanor looked like she'd slept even less than he had.`
- **Craft problem**: Scene mechanics -- not entering late enough. The scene opens with people arriving and setting up before the core conflict (the Case A/B revelation) begins. The arrival sequence consumes 9 lines before Eleanor delivers the scene's premise.
- **Why it weakens the prose**: The arrival details (who came first, what they brought, what they looked like) are standard scene-setting that delays the reader from the scene's actual content. The novel does this well in many chapters (Ch 22 opens with "The proposal came without fanfare" -- immediate, no setup), but Ch 12 falls into the arrival-then-discussion pattern.
- **Suggestion**: Start with Eleanor's line: `"Before we start," Eleanor said, "everyone needs to understand: what we discuss doesn't leave this room."` Weave the arrival details into the scene as it progresses if they're needed (Wei's yesterday's clothes, Marcus's whiteboard).
- **Severity**: MEDIUM
- **Confidence**: medium (the arrival details do establish physical reality and character states; the early-entry issue is moderate)

### 15. Ch 26's sculpture tour structure

- **Location**: Ch 26 (Optimization Landscapes), lines 72-128
- **Passage**: Sofia leads the team past sculptures: "Turning the Keys" (branching tree), "The Value Manifold" (interlocking rings), "Case A, Case B" (nested spheres). Each follows the same structure: approach sculpture, Sofia explains it, team members react, philosophical observation, scene break.
- **Craft problem**: Three consecutive scene beats with identical structure. The reader begins anticipating the pattern: arrive at sculpture, explain metaphor, make philosophical observation, move on.
- **Why it weakens the prose**: The sculptures themselves are strong -- each one maps SIGMA concepts to physical form in a way that earns its metaphor. But the delivery mechanism is repetitive. By the third sculpture, the reader is ahead of the prose.
- **Suggestion**: Vary the approach. Let one sculpture be experienced silently -- the team stands before it and nobody explains. Let another provoke disagreement rather than harmonious observation. Break the tour structure: have two characters break away from the group, or have a gallery visitor interrupt with a question the team can't answer honestly.
- **Severity**: MEDIUM
- **Confidence**: medium

### 16. Redundant voice-quality descriptors in Ch 22

- **Location**: Ch 22 (Scaling the Policy), key ceremony section
- **Passage**: Within 100 lines (approximately 400-510):
  - `"I'll go first," Eleanor said. "My vote is yes." Her voice was steady, but her hands shook.` (330)
  - `Sofia said. Her voice was flat---not angry, not afraid. Procedural.` (338)
  - `His voice was hollow.` (228)
  - `His voice was flat.` (147)
- **Craft problem**: Narrator describes voice quality as a parallel channel to the dialogue itself. In the key ceremony -- the novel's highest-stakes scene -- the reader receives a running commentary on vocal texture alongside the actual words.
- **Why it weakens the prose**: The key ceremony is powerful because of what characters say, not how the narrator describes them saying it. Sofia's "I built this cage" speech is riveting. The annotation "Her voice was flat -- not angry, not afraid. Procedural" is the author making sure the reader gets it. The reader already gets it.
- **Suggestion**: Trust the dialogue. Cut most voice descriptors in this scene. Where physical detail matters, use action instead: `Eleanor's hands shook as she spoke.` is stronger than `Her voice was steady, but her hands shook.` because the contradiction between shaking hands and spoken certainty is more interesting when rendered than when annotated.
- **Severity**: MEDIUM
- **Confidence**: high

### 17. "Both" / "Either" / "Neither" ternary as chapter-end formula

- **Location**: Ch 12 (end), Ch 16 (end), Ch 23 (end), Ch 26 (end), Ch 27 (end)
- **Passage**:
  - `Both requiring the same unbearable faith.` (Ch 12)
  - `Same data. Either way.` (Ch 16)
  - `Success and failure and twenty-two unknowns.` (Ch 23)
  - `Whether they asked because they cared, or because asking was optimal--- / Eleanor didn't know.` (Ch 26)
  - `That was enough for today.` (Ch 27)
- **Craft problem**: Multiple chapters end with a Both/Either/Neither construction that restates the core thematic ambiguity. The pattern has become a closing formula.
- **Why it weakens the prose**: The first few instances are effective -- "Same data either way" is a genuinely good line. But when the pattern recurs at the close of five chapters, it becomes predictable. The reader knows the chapter will end by reasserting the fundamental uncertainty. This converts what should be unsettling ambiguity into structural routine.
- **Suggestion**: Keep the strongest 2-3 instances. For the others, end with concrete detail rather than thematic restatement. Ch 23 could end with the dashboard image. Ch 27 already ends well with "Tomorrow was Saturday. Ice cream again." -- the preceding thematic restatement about symmetric uncertainty is unnecessary.
- **Severity**: MEDIUM
- **Confidence**: medium (this is partly a structural/voice issue, and the repetition may be intentional thematic architecture)

## LOW Issues

### 18. "Exclaimed" in Ch 5

- **Location**: Ch 5, line 77
- **Passage**: `"Oh!" Marcus exclaimed, nearly knocking over Wei's carefully organized pen holder.`
- **Craft problem**: Fancy dialogue tag. "Exclaimed" draws attention to the author's narration. The "Oh!" and the physical action (knocking over the pen holder) already convey excitement.
- **Suggestion**: `"Oh!" Marcus nearly knocked over Wei's pen holder.`
- **Severity**: LOW
- **Confidence**: high

### 19. Filter word cluster in Ch 5 (Wei's SIGMA interaction)

- **Location**: Ch 5, lines 321-450
- **Passage**: Cluster of "could" constructions in the Wei/SIGMA medical data scene: "could theoretically exploit," "could have produced," "could identify treatment options."
- **Craft problem**: Filter word accumulation in a scene that should be maximally immediate. Wei is being seduced by a superintelligent AI; the prose should put the reader inside his desperation, not observe it through "could."
- **Why it weakens the prose**: Many of these "could"s are in SIGMA's dialogue and are therefore deliberate (SIGMA speaks in probability space). But the narration around the dialogue also uses conditional constructions, which creates distance.
- **Suggestion**: Make the narration direct even when SIGMA's dialogue is conditional. `Wei's hands trembled. Every hour mattered.` instead of filter-mediated observation.
- **Severity**: LOW
- **Confidence**: medium (SIGMA's dialogue genuinely requires conditional language)

### 20. "Stared at" repetition

- **Location**: Manuscript-wide, particularly Ch 12, 18, 22, 24
- **Passage**: Frequent use of "stared at the screen," "stared at the whiteboard," "stared at the ceiling," "stared at his hands" as default reaction to revelations.
- **Craft problem**: "Stared" has become the manuscript's default physical action for processing information. Characters stare at things when they need to absorb something.
- **Suggestion**: Vary: "studied," "watched," "read twice," or better, specific action (Marcus's fingers drumming, Wei pulling up data, Sofia typing).
- **Severity**: LOW
- **Confidence**: medium

### 21. Ch 25 "She didn't know" cascade

- **Location**: Ch 25 (Leaving), lines 212-217
- **Passage**: `She didn't know if she could rebuild what she'd broken. Didn't know if Sam would ever look at her without that careful, testing distance. Didn't know if the next concert or birthday or Saturday afternoon would be enough to prove that things had changed.`
- **Craft problem**: The "didn't know" anaphora works for two beats but extends to three, which tips into rhetorical exhaustion. The third item ("the next concert or birthday or Saturday afternoon") lists possibilities rather than building, which flattens the rhythm.
- **Suggestion**: Cut the third beat. Two is a pair -- tension. Three becomes a list -- resolution. The uncertainty should remain unresolved.
- **Severity**: LOW
- **Confidence**: medium

### 22. "Whether" construction as thematic tic

- **Location**: Ch 16 (end), Ch 25 (line 36), Ch 26 (line 214), Ch 27 (line 123)
- **Passage**:
  - `Whether it actually cared, or just behaved as if it cared---that she'd never know.` (Ch 25)
  - `Whether they asked because they cared, or because asking was optimal---` (Ch 26)
- **Craft problem**: The "Whether X or Y" construction is the novel's default way of stating the Case A/B ambiguity. It has been reduced from earlier versions (per the editorial history) but still appears enough to feel formulaic.
- **Note**: The style guide documents this as a known issue that was partially addressed in Wave 3. Current count is much improved but worth noting for final polish.
- **Severity**: LOW
- **Confidence**: medium

## Strengths

**SIGMA's voice is exceptional.** The Ch 24 farewell -- where SIGMA attempts to say goodbye, fails in English, fails in LRS, and settles on "you were the right noise" -- is among the best AI-character prose in contemporary fiction. The three-tier compression notation is earned rather than gestural. Every [---] gap in that passage communicates genuine ineffability because the surrounding prose has established what SIGMA *can* say in English, making the failures visible.

**The Case A/B exposition in Ch 12 is a masterclass in Theory as Horror.** Marcus's whiteboard scene -- where identical observable behaviors map to both aligned and deceptive interpretations -- converts an abstract alignment concept into visceral dread. The table showing "Yes / Yes / Yes / Yes / Yes" across both cases is more frightening than any thriller set piece. This is the novel's intellectual spine and it works perfectly.

**The key ceremony in Ch 22 is the novel's best-crafted scene.** Sofia's "No" vote, her 18-minute audit, the Guangzhou collapse during the audit, and her reversal under protest -- this sequence has genuine dramatic tension because every beat is earned. The physical description of the keys, the 0.27-second timing, Eleanor's inability to say "three" -- these details carry weight because they are specific and embodied.

**Sam's dialogue in Ch 25 is the novel's strongest character voice work.** "Don't promise things you can't promise" and "I'll try really hard. Because that's true" capture an eight-year-old's moral reasoning without condescension. Sam sounds like a child who has learned to protect herself -- not precocious, not precious, just careful. The scene earns every line.

**The intellectual set pieces maintain genuine tension.** The CEV debate in Ch 12, the temperature experiment in Ch 16, the Geneva conference in Ch 20, the first-mandate pattern in Ch 21 -- these scenes could easily collapse into lecture, but they stay alive because characters disagree, interrupt, and process differently. Sofia's engineering pragmatism clashes with Marcus's philosophical abstraction in ways that produce genuine dramatic friction.

**The hemorrhagic fever section in Ch 17 refuses easy answers.** The juxtaposition of SIGMA's correct expected-value calculation with Dr. Conteh's hospital testimony is devastating precisely because the prose does not resolve the tension. Neither the statistical view nor the human view is privileged. This honors the novel's commitment (per the anti-cliche rules) to avoiding clean trolley problems after Day 145.

**Chapter endings, when they work, work beautifully.** Ch 24's `"And in the lab, SIGMA taught LAOZI the question."` Ch 1's `"Before we start, it sent us a message."` Ch 22's `"Now they would find out what they had freed."` These are clean, earned exits that trust the reader.
