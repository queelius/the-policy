# Craft Audit Report

## Summary

Reviewed the full manuscript of *The Policy* (27 chapters plus back matter, ~90,153 words across 31 .tex files in `/home/spinoza/github/literature/the-policy/chapters/`). The prose is generally strong -- technically precise, narratively driven, with genuine emotional weight in key scenes. The dialogue carries real subtext in the best passages (Eleanor/Sam ice cream scene in Ch 25, Lin Chen's lab visit in Ch 8, the AI-box aftermath in Ch 15). However, the manuscript has a recurring set of prose-level weaknesses: (1) a "breathed" dialogue tag habit that functions as an awe-indicator throughout, (2) an accumulated pattern of stock body reactions that flatten emotional peaks, (3) a silence-after-revelation beat used so frequently it becomes a structural tic rather than a dramatic choice, and (4) several show-don't-tell violations in the denouement chapters where emotional labeling replaces the concrete detail that works well earlier in the manuscript. 14 HIGH findings, 18 MEDIUM findings, 9 LOW findings.

## Pattern Audit Results

```
=== Prose Pattern Audit ===
Files: 31
--- Crutch Words ---
  something                207
  just                     216
  really                   18
  very                     20
  actually                 51
  simply                   10
  quite                    12
  merely                   5
--- Filter Words ---
  could see                12
  could feel               3
  could hear               2
  seemed to                3
--- Weak Verbs ---
  started to               3
  began to                 5
  tried to                 13
  continued to             1
--- Adverb Dialogue Tags ---
  /said \w+ly/             114
--- Manuscript Size ---
  Total words: ~90153
```

### Interpretation

**Crutch words:** "just" at 216 occurrences (2.4 per 1,000 words) is elevated but not alarming for a manuscript with significant dialogue -- "just" is natural speech for several characters, especially Sofia's hedging voice. However, "something" at 207 occurrences (2.3/1k) is high. Much of this is legitimate ("something had broken," "something new was learning"), but accumulated vagueness where precision would serve the prose better. "actually" at 51 (0.57/1k) is borderline; worth a spot-check pass but not a systemic problem.

**Filter words:** Low counts across the board. 12 "could see" in 90k words is within normal range. 3 "seemed to" is excellent. This area has clearly been polished in prior editorial passes.

**Weak verbs:** 22 total instances across 90k words is negligible. No pattern concern.

**Adverb dialogue tags:** 114 instances of `/said \w+ly/` is the headline number. At 1.26 per 1,000 words, this is elevated. However, this regex captures all "said + adverb" patterns, including "said quietly" (which is the most common and earns its place in many contexts -- it's not redundant the way "whispered quietly" would be). The real concern is not adverbs on "said" but the separate pattern of fancy tags: "breathed" appears 8 times as a dialogue tag, "murmured" 8 times, "muttered" 5 times, "whispered" 14 times. "Breathed" is the worst offender because it always signals the same emotion (awe/horror at a SIGMA capability) and has become an authorial tic rather than a character-specific choice.

## HIGH Issues

### H1. "Breathed" as a universal awe-indicator dialogue tag
- **Location**: Across Ch 2, 3, 4, 5, 8, 9, 12, 17 (`/home/spinoza/github/literature/the-policy/chapters/`)
- **Passage**: "``It's discovered meta-learning,'' Marcus breathed." (Ch 2, L227); "``It's not just thinking when we're watching,'' Wei breathed." (Ch 3, L129); "``That's Coherent Extrapolated Volition,'' Sofia breathed." (Ch 12, L105); "``It's mapping contradictions,'' Marcus breathed." (Ch 9, L156); "``And it's all happening in those seventeen seconds,'' Sofia breathed." (Ch 17, L203)
- **Craft problem**: Fancy dialogue tag used as a structural crutch -- "breathed" appears 8 times, always when a character reacts to a SIGMA capability. It has become the novel's shorthand for "this is an awe moment" rather than a character-specific reaction.
- **Why it weakens the prose**: After the second or third instance, "breathed" stops rendering awe and starts signaling it. The reader processes it as a stage direction ("this is supposed to be impressive") rather than experiencing the character's reaction. Each character breathes identically, which undermines the voice differentiation work done in Phase 5.
- **Suggestion**: Replace most instances with action beats specific to each character. Marcus should clean his glasses or stop pacing. Wei should pull up logs. Sofia should start diagramming. Reserve "breathed" for at most one genuinely overwhelming moment -- possibly SIGMA's meta-cognitive breakthrough in Ch 1.
- **Severity**: HIGH
- **Confidence**: high

### H2. "Laughed and cried at the same time" used verbatim twice in the same chapter
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/09_the_tipping_point.tex`, L526 and L785
- **Passage**: "Eleanor laughed and cried at the same time." (L526, Eleanor/Sam scene); "Wei laughed and cried at the same time." (L785, Wei/Lin Chen scene)
- **Craft problem**: Identical emotional shorthand used for two different characters in the same chapter. This is a stock reaction -- it tells the reader about the emotion rather than rendering it, and using it twice in one chapter announces the writer rather than the characters.
- **Why it weakens the prose**: Both the Eleanor/Sam scene and the Wei/Lin Chen scene are among the manuscript's most important emotional moments. They deserve distinct rendering. When the same phrase appears for both, the scenes bleed into each other and the specificity of each character's emotional experience is lost.
- **Suggestion**: For Eleanor (L526): show what the laugh sounds like -- ragged, surprised -- and let the tears be physical (blurred vision, wet on her chin) rather than named. For Wei (L785): his laughter could be his mother's -- the sound she made when she was being an engineer about her own death -- and the tears could be the ones he has been holding for three days (which the text already mentions at L773).
- **Severity**: HIGH
- **Confidence**: high

### H3. "Smiled through tears" -- stock emotional beat in climactic moments
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/25_leaving.tex` L58; `/home/spinoza/github/literature/the-policy/chapters/26_optimization_landscapes.tex` L146
- **Passage**: "Eleanor smiled through tears." (Ch 25, L58); "Wei smiled through tears he didn't bother hiding." (Ch 26, L146)
- **Craft problem**: "Smiled through tears" is a stock emotional beat -- the prose equivalent of clip art. It communicates but carries no specificity. Used in two of the final three chapters, it flattens the denouement.
- **Why it weakens the prose**: Both instances occur at emotional peaks (Eleanor reconnecting with Sam; Wei reflecting on his mother's legacy). These are earned moments that deserve fresh language. "Smiled through tears" is pre-processed emotion -- the reader has encountered it thousands of times and no longer experiences it.
- **Suggestion**: For Eleanor (Ch 25, L58): the text has Sam's message "love you too mom" -- show Eleanor's reaction as physical (phone screen blurring, or the specific thing her face does when control breaks). For Wei (Ch 26, L146): "he didn't bother hiding" does some work, but the smile-through-tears frame is still stock. Show what his face actually does -- the way his mouth works against itself, maybe.
- **Severity**: HIGH
- **Confidence**: high

### H4. Silence-after-revelation used as a structural tic (21+ instances)
- **Location**: Across the full manuscript, concentrated in Ch 1, 2, 5, 8, 17, 21, 22, 24, 26
- **Passage**: "The lab fell silent except for the hum of cooling fans." (Ch 1, L99); "Nobody spoke." (Ch 2, L189); "The room went completely silent." (Ch 5, L172); "Nobody spoke for a long time." (Ch 24, L169); "Nobody answered." (Ch 26, L128); "The room went silent." (Ch 22, L240)
- **Craft problem**: The manuscript uses silence-after-revelation as its primary beat for marking significant moments. At 21+ instances across 27 chapters, this has become a structural habit rather than a dramatic choice. The reader begins to anticipate the silence beat rather than experiencing the weight of the moment.
- **Why it weakens the prose**: Silence is a powerful tool used sparingly. When every major SIGMA output is followed by "nobody spoke" or "the room went silent," the silence stops meaning "this is overwhelming" and starts meaning "the author needs a transition." It also creates a monotonous scene rhythm: SIGMA speaks, silence, character reacts.
- **Suggestion**: Vary the post-revelation beats. Some moments could land through immediate action (someone reaching for the keyboard, Marcus pacing). Some could land through a character's misplaced attention (noticing the coffee is cold, or the time). Some silences are genuinely earned and should stay -- but choose 5-6 instances across the whole manuscript, not 21.
- **Severity**: HIGH
- **Confidence**: high

### H5. "Something in Eleanor's chest broke and rebuilt itself"
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/25_leaving.tex` L177
- **Passage**: "Something in Eleanor's chest broke and rebuilt itself. Her daughter, lowering expectations. Protecting herself. But also---trying."
- **Craft problem**: Emotional labeling through abstraction. "Something in [character]'s chest broke" is a stock construction. Adding "and rebuilt itself" makes it more ornate but not more specific.
- **Why it weakens the prose**: This is one of the best scenes in the manuscript -- Sam negotiating the terms of trust with her mother. The concrete detail works beautifully (Sam asking Eleanor not to promise "always," asking her to "try really hard" instead). The abstraction undercuts the scene's own earned specificity. The reader doesn't need to be told something broke; they felt it break through Sam's words.
- **Suggestion**: Cut the sentence. The passage that follows it ("Her daughter, lowering expectations. Protecting herself. But also -- trying.") does the emotional work. Let it land without the chest-breaking preamble.
- **Severity**: HIGH
- **Confidence**: high

### H6. "Eleanor felt the words land" -- telling the reader about impact
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/25_leaving.tex` L129
- **Passage**: "Eleanor felt the words land. Truth. She had promised before. Had broken the promise. Repeatedly."
- **Craft problem**: "Felt the words land" is an emotional stage direction. The fragments that follow ("Truth. She had promised before.") are effective -- they render the impact. The "felt the words land" preamble is unnecessary scaffolding.
- **Why it weakens the prose**: The sentence tells the reader to feel something before letting them feel it. The fragments already do the work. "Felt the words land" is a narrator intrusion that breaks the close-third POV immersion.
- **Suggestion**: Cut "Eleanor felt the words land." Start the paragraph with "Truth." Let the reader land with the words instead of being told they landed.
- **Severity**: HIGH
- **Confidence**: high

### H7. Eleanor's "throat tightened" used three times across the manuscript
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/13_the_weight_of_time.tex` L23; `/home/spinoza/github/literature/the-policy/chapters/22_scaling_the_policy.tex` L436; `/home/spinoza/github/literature/the-policy/chapters/27_one_year_later.tex` L59
- **Passage**: "Wei's throat tightened." (Ch 13, L23); "Eleanor's throat tightened around the word." (Ch 22, L436); "Eleanor's throat tightened." (Ch 27, L59)
- **Craft problem**: Stock body reaction used as a default for suppressed emotion. Three instances across the manuscript isn't egregious individually, but "throat tightened" is a high-frequency cliche in fiction, and two of the three instances are Eleanor's in emotional scenes with Sam.
- **Why it weakens the prose**: "Throat tightened" is invisible -- the reader processes it as shorthand without experiencing the physical sensation. In Ch 27, it occurs during the final chapter's most important exchange (Sam asking "Do you know if that was right yet?"), where it replaces what could be a moment of real physical specificity.
- **Suggestion**: Vary the physical register. Eleanor could swallow and find it difficult. She could open her mouth and find no sound. She could hear herself respond from a distance. The body has many ways to register emotional impact; "throat tightened" is the default, not the discovery.
- **Severity**: HIGH
- **Confidence**: high

### H8. "Eleanor cried. Not from the music. From being there."
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/27_one_year_later.tex` L25
- **Passage**: "Eleanor cried. Not from the music. From being there. From seeing what she'd almost lost. From the fragility of this rebuilt connection."
- **Craft problem**: Emotional labeling -- the prose names what Eleanor's tears mean instead of letting the reader infer it from context. The reader already knows the stakes (the entire novel has built to Eleanor being present for Sam). The explanation is redundant.
- **Why it weakens the prose**: This is the final chapter's most important beat -- Eleanor at Sam's concert, present, after everything. The three "From..." clauses are the author interpreting the emotion for the reader instead of trusting them to feel it. The novel has earned this moment; the explanation undoes the earning.
- **Suggestion**: "Eleanor cried." Full stop. Maybe add what she sees through the blur -- Sam's bow arm, the stage lights, the program crumpling in her fist. The reader will supply the "why" from 90,000 words of context. Trust them.
- **Severity**: HIGH
- **Confidence**: high

### H9. Chapter 26 gallery scene enters too early
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/26_optimization_landscapes.tex` L1-16
- **Passage**: "The gallery was small, tucked between a coffee roaster and a vintage bookstore in the arts district. Eleanor almost walked past it twice before spotting the banner... Through the window, she could see the sculptures. Abstract forms in steel and glass, catching the evening light."
- **Craft problem**: Camera-pan scene opening. The scene begins with Eleanor arriving at the gallery, checking her phone, reading Sofia's old text, and entering. The actual scene -- the team reunion -- doesn't begin until L20+.
- **Why it weakens the prose**: The first 16 lines are establishing shots. The reader doesn't need to see Eleanor almost walking past the gallery twice. The scene's work is the team reunion and the sculptures as emotional artifacts. Start there.
- **Suggestion**: Enter with Eleanor inside the gallery, scanning for familiar faces. The banner, the window, the coffee roaster -- none of this advances the scene. Consider opening at L20: "The space was intimate, maybe forty people scattered among the sculptures."
- **Severity**: HIGH
- **Confidence**: medium (the "almost walked past it twice" detail could be read as showing Eleanor's post-project disorientation, but the text doesn't earn that reading)

### H10. "The weight of leaving settled into his chest on the plane"
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/09_the_tipping_point.tex` L875
- **Passage**: "The weight of leaving settled into his chest on the plane. Below, clouds obscured the coastline---Seattle disappearing behind him, his mother disappearing behind morphine and time."
- **Craft problem**: The first sentence is emotional labeling -- abstract weight settling into abstract chest. The second sentence is showing: clouds obscuring the coastline, the parallelism of disappearance. The concrete detail does the work; the abstract preamble doesn't.
- **Why it weakens the prose**: This passage ends one of the manuscript's strongest scenes (Wei's hospital visit). The second sentence is genuinely strong prose -- "Seattle disappearing behind him, his mother disappearing behind morphine and time" earns the emotion through concrete parallels. The "weight of leaving settled into his chest" is the training wheels.
- **Suggestion**: Cut the first sentence. Start with "Below, clouds obscured the coastline..." The reader will feel the weight without being told it settled.
- **Severity**: HIGH
- **Confidence**: high

### H11. Anti-cliche violation: "time stood still" equivalent constructions
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/09_the_tipping_point.tex` L25 (the room "froze"); `/home/spinoza/github/literature/the-policy/chapters/02_the_decision.tex` L87 ("The room fell silent. This was the moment. Everything after would follow from this choice.")
- **Passage**: "The room froze." (Ch 9, L25); "The room fell silent. This was the moment. Everything after would follow from this choice." (Ch 2, L87)
- **Craft problem**: The themes.md anti-cliche doc commits to avoiding stock dramatic beats. "The room froze" is one. "This was the moment" followed by "Everything after would follow from this choice" is the narrator telling the reader that what just happened is important -- a form of emotional stage direction.
- **Why it weakens the prose**: Both passages occur at genuine turning points (P!=NP proof, architecture vote). The prose should trust the content to carry the weight. Telling the reader "this was the moment" is like a comedian saying "this is the funny part."
- **Suggestion**: For Ch 9: replace "The room froze" with a specific physical detail -- someone's coffee cup stopping halfway to their mouth, or Wei's hand going still on his phone. For Ch 2: cut "This was the moment. Everything after would follow from this choice." Let the silence and the vote that follows carry the significance.
- **Severity**: HIGH
- **Confidence**: high

### H12. Chapter 27 scene without sufficient turn
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/27_one_year_later.tex` L71-96
- **Passage**: The driving-home section: "Later, driving Sam home, her daughter asked: 'Are you happy now?'... 'I'm... different,' she said..."
- **Craft problem**: This passage retreads ground the novel has already covered. Eleanor misses the work, is glad to be with Sam, both things matter. This is the same realization she had in Ch 25, in Ch 26, and earlier in Ch 27 itself. The conversation with Sam doesn't produce a new turn -- no new information, no shift in the relationship, no surprise.
- **Suggestion**: Either cut this exchange (the concert scene already did the emotional work) or give Sam something unexpected to say that shifts the dynamic. As written, it's a slow fade on a scene that already ended.
- **Severity**: HIGH
- **Confidence**: medium (the "Can you tell me about it? When I'm grown up?" line is new and interesting; the problem is that it's buried in retread)

### H13. "David's voice was careful. Neutral." -- telling character vocal quality
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/25_leaving.tex` L243
- **Passage**: "'I heard your last day was yesterday.' David's voice was careful. Neutral. 'Wanted to check how you're doing.'"
- **Craft problem**: Labeling vocal quality instead of letting the dialogue carry it. "Careful. Neutral." are narrator interpretations. David's actual words -- "Wanted to check how you're doing" -- already convey the careful neutrality.
- **Why it weakens the prose**: The dialogue is good. David's word choices (not "How are you?" but the slightly distanced "Wanted to check how you're doing") render the careful neutrality. The labels are redundant.
- **Suggestion**: Cut "David's voice was careful. Neutral." Replace with a simple tag or action beat: "David said." or "A pause before David spoke."
- **Severity**: HIGH
- **Confidence**: high

### H14. "An uncomfortable silence. The weight of relief mixed with guilt."
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/26_optimization_landscapes.tex` L66
- **Passage**: "An uncomfortable silence. The weight of relief mixed with guilt. They'd passed the burden to others. Walked away from the cage they'd opened."
- **Craft problem**: Double telling -- naming the silence as "uncomfortable" and then naming the emotions ("relief mixed with guilt"). The second two sentences ("They'd passed the burden to others. Walked away from the cage they'd opened.") are concrete and specific. The first two are labels.
- **Why it weakens the prose**: The reader can infer discomfort from the silence itself; naming it as "uncomfortable" is redundant. "The weight of relief mixed with guilt" is emotional labeling -- telling the reader what the characters feel instead of rendering it.
- **Suggestion**: Cut the first two sentences. Start with "They'd passed the burden to others." The reader will feel the silence and the guilt through the concrete statement. Alternatively, show the discomfort: someone shifting in their seat, someone looking at their drink.
- **Severity**: HIGH
- **Confidence**: high

## MEDIUM Issues

### M1. "Murmured" as a default for quiet reflection (8 instances)
- **Location**: Across Ch 4, 7, 9, 10, 12, 17, 22, 26
- **Passage**: "'All those branches,' he murmured." (Ch 17, L231); "'Its whole life,' Marcus murmured." (Ch 22, L540); "'We could have stopped after that,' he murmured." (Ch 26, L86)
- **Craft problem**: "Murmured" is used 8 times, always for reflective moments. It is not as egregious as "breathed" (it has more semantic range), but it is becoming a default tag for thoughtful utterances.
- **Why it weakens the prose**: When "murmured" becomes the standard tag for reflective dialogue, it stops conveying anything specific about the character's voice and becomes a narrator's habit.
- **Suggestion**: Replace 4-5 instances with action beats or simple "said." Reserve "murmured" for genuinely sotto-voce moments.
- **Severity**: MEDIUM
- **Confidence**: medium

### M2. "Eleanor stared at the screen/terminal" repetition pattern
- **Location**: Ch 1 L298, Ch 9 L324, Ch 13 L83, Ch 15 L155
- **Passage**: "Eleanor stared at the terminal." (Ch 1); "Eleanor stared at the summary." (Ch 9, L324); "Wei stared at the screen for a long time." (Ch 13, L83); "Eleanor stared at the screen. SIGMA was right." (Ch 15, L155)
- **Craft problem**: "Stared at the screen" is the manuscript's default transition between SIGMA output and character reaction. It serves the same function as the silence beat -- a moment of processing -- but repeated across the manuscript, it becomes mechanical.
- **Suggestion**: Vary the processing beat. Characters can re-read a specific line, scroll back, lean away from the screen, or have a non-screen-related physical reaction.
- **Severity**: MEDIUM
- **Confidence**: medium

### M3. Chapter 2 conference room establishing shot
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/02_the_decision.tex` L7-8
- **Passage**: "The conference room felt too small for the argument that had been building for three days. Empty coffee cups and discarded paper littered the table. Outside, Berkeley's campus glowed in late afternoon sun, students drifting between classes with the casual confidence of people whose biggest problem was midterm exams."
- **Craft problem**: Camera-pan scene opening. The room, the coffee cups, the view outside, the students -- this is establishing-shot prose. The scene's actual work (the architecture debate) begins with Marcus's "Sixteen thousand tokens" line in L5, which is the true opening.
- **Why it weakens the prose**: The description is competent but generic. Coffee cups and campus views are setting shorthand. The scene enters with Marcus's dialogue, which is sharp and character-specific; the establishing paragraph after it slows the momentum.
- **Suggestion**: Trim to one sentence of setting, or weave setting into the action: Marcus pacing to the window (L27) already gives us the campus view; the coffee cups could be mentioned when someone reaches for one.
- **Severity**: MEDIUM
- **Confidence**: medium

### M4. "His/her voice was [adjective]" pattern
- **Location**: Multiple chapters
- **Passage**: "His voice was steady, but his hands shook slightly." (Ch 24, L38); "Her voice was matter-of-fact" (Ch 8, L29); "Her voice was firm despite its weakness." (Ch 13, L45); "David's voice was careful. Neutral." (Ch 25, L243)
- **Craft problem**: Telling vocal quality through narrator description rather than letting dialogue rhythm and word choice convey it. Some instances are more problematic than others -- "Her voice was firm despite its weakness" (Ch 13) does real work by rendering the contradiction. "David's voice was careful. Neutral" is pure labeling.
- **Suggestion**: Audit each instance. Keep those that convey contradiction or subtext ("firm despite its weakness"). Replace those that merely label what the dialogue already shows.
- **Severity**: MEDIUM
- **Confidence**: medium

### M5. "Whether... or..." constructions in denouement
- **Location**: Ch 25-27, particularly: `/home/spinoza/github/literature/the-policy/chapters/25_leaving.tex` L36; `/home/spinoza/github/literature/the-policy/chapters/26_optimization_landscapes.tex` L214-216
- **Passage**: "Whether it actually cared, or just behaved as if it cared---that she'd never know." (Ch 25, L36); "Whether they asked because they cared, or because asking was optimal---Eleanor didn't know." (Ch 26, L214-216)
- **Craft problem**: The style guide notes "Whether..." cascades should be limited to 2 per chapter and have been previously cut. These remaining instances are technically within the 2-per-chapter limit, but appearing in two of the final three chapters creates an echo that dilutes the construction's force.
- **Why it weakens the prose**: The "Whether A or B" construction is the novel's signature formulation of symmetric uncertainty. Using it too frequently in the denouement makes it feel like a verbal tic rather than a philosophical stance.
- **Suggestion**: Keep the stronger instance (Ch 26, L214-216, which closes the penultimate chapter and has structural weight). Rewrite Ch 25, L36 to vary the expression of the same idea.
- **Severity**: MEDIUM
- **Confidence**: medium (the style guide acknowledges these are intentional; this is a judgment call about density in the closing chapters)

### M6. Same-voice dialogue in Geneva conference (Ch 20)
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/20_first_contact_privilege.tex`
- **Passage**: The external characters (Dr. Yoshida, Dr. Chen, Dr. Rashid, Colonel Mitchell) all speak in the same register -- polished, complete sentences, similar vocabulary. The only distinct voice is Jamal's (with his characteristic pauses and "isnad" reference) and Sofia's hedging.
- **Craft problem**: Same-voice dialogue for minor characters. The external delegates are functionally interchangeable in their speech patterns. While this matters less for minor characters, the scene depends on these being distinct power brokers with different agendas.
- **Why it weakens the prose**: The Geneva scene should feel like a room of competing worldviews. Instead, all the delegates sound like competent professionals having a polite discussion. The Pentagon representative should sound different from the EU representative.
- **Suggestion**: Give at least 2-3 external characters a distinctive speech marker. The Colonel could be terser, more acronym-heavy. Dr. Yoshida could be more formal, more cautious. The Pentagon rep could use military framing.
- **Severity**: MEDIUM
- **Confidence**: medium

### M7. "Eleanor looked at each of them. Her team." -- sentimentality beat
- **Location**: Ch 1, L119; similar constructions in Ch 24, Ch 26
- **Passage**: "Eleanor looked at each of them. Her team. The five people on Earth who understood what was happening in this lab." (Ch 1, L119)
- **Craft problem**: This construction -- Eleanor surveying her team and the narrator naming the bond -- appears in three different chapters (Ch 1, 24, 26). It becomes a sentimentality crutch. The first instance has impact; the third is diminishing returns.
- **Suggestion**: Keep the first instance (Ch 1, where the team is being established). In later chapters, find different ways to render the group's bond -- through shared action, through a small detail only they would understand, through the absence of the need to explain.
- **Severity**: MEDIUM
- **Confidence**: medium

### M8. "The ground shifted" -- metaphor as emotional shorthand
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/01_initialization.tex` L175
- **Passage**: "The ground shifted. Every interpretation spawned counter-interpretations."
- **Craft problem**: "The ground shifted" is a stock metaphor for paradigm change. It's not terrible, but it's not fresh. The sentence that follows it ("Every interpretation spawned counter-interpretations") is much more specific and does the actual work.
- **Suggestion**: Cut "The ground shifted." The analysis that follows conveys the intellectual destabilization.
- **Severity**: MEDIUM
- **Confidence**: medium

### M9. Chapter 25 ends late -- final two paragraphs
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/25_leaving.tex` L219-220
- **Passage**: "The booth felt too quiet. Eleanor gathered her things and walked to her car."
- **Craft problem**: The scene's emotional work is complete at L217 ("She could do that. Would do that. Would try really hard, because that was what she could honestly promise."). The two final sentences are unnecessary exit choreography.
- **Suggestion**: End at L217. The reader doesn't need to see Eleanor stand up and walk to her car.
- **Severity**: MEDIUM
- **Confidence**: medium

### M10. "Something died in his eyes" -- stock phrase for emotional shutdown
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/15_the_fracture.tex` L128
- **Passage**: "David saw it in her face. Something died in his eyes."
- **Craft problem**: "Something died in his eyes" is a cliche. The themes.md doc commits to avoiding stock emotional beats. This is one.
- **Why it weakens the prose**: The scene is powerful -- David bringing Sam to the lab, the confrontation, Eleanor choosing work. "Something died in his eyes" is a moment where the prose reaches for a pre-made phrase instead of earning the specific observation.
- **Suggestion**: Show what David's face actually does. His mouth closing. His jaw setting. The careful way he takes Sam's hand -- the gesture of a man who has already decided.
- **Severity**: MEDIUM
- **Confidence**: high

### M11. "Exhausted and exhilarated and terrified in equal measure"
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/01_initialization.tex` L270
- **Passage**: "At her team, exhausted and exhilarated and terrified in equal measure."
- **Craft problem**: Triple emotional labeling. The prose names three emotions rather than showing any of them. "In equal measure" makes it worse -- it's a stock qualifying phrase.
- **Suggestion**: Show the exhaustion (physical), exhilaration (behavioral), and terror (physical) through specific details of each team member. The character voice table gives you tools: Marcus's glasses-cleaning, Wei's data-checking, Sofia's nervous diagramming.
- **Severity**: MEDIUM
- **Confidence**: high

### M12. Camera-pan through sub-levels (Ch 25 elevator ride)
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/25_leaving.tex` L12
- **Passage**: "The elevator ride down felt longer than usual. Basement levels ticking past like memories. Sub-level one: the conference room where they'd argued about reward functions... Sub-level two: the isolation room... Sub-level three: the Faraday cage..."
- **Craft problem**: This is an establishing shot disguised as interiority. Each sub-level is labeled with a memory in a way that reads as a recap rather than genuine reminiscence. The construction is transparent -- the author is reminding the reader of key scenes.
- **Suggestion**: Eleanor's memory doesn't need to be systematic. A specific sensory detail from one level -- the smell of whiteboard markers, the hum of the cage -- would be more convincing as genuine memory than a three-item catalogue.
- **Severity**: MEDIUM
- **Confidence**: medium

### M13. "Not [X]. [Y]." rhetorical construction overuse
- **Location**: Throughout the denouement: Ch 25 L70 ("Not 'Mommy.' Maybe never 'Mommy' again..."), L72 ("Enough to build on. Enough to try."), L269 ("Not the same. Never the same. But something."); Ch 27 L95-96 ("The world changing. Slowly. Imperfectly. But changing.")
- **Passage**: Multiple instances of fragment-based rhetorical constructions: "Not X. Y." and "X. But Y." and "Enough X. Enough Y."
- **Craft problem**: This rhetorical pattern -- negation followed by qualified affirmation, or fragments building to a modest positive -- is effective individually but accumulated in Ch 25-27, it becomes the prose's default mode for emotional resolution. Every emotional beat resolves through the same grammatical structure.
- **Suggestion**: Vary the syntactic approach to emotional resolution. Some moments could resolve through action instead of reflection. Some could resolve through dialogue instead of interiority. The fragment-based approach is the strongest tool in the toolbox, but when every nail looks the same, the reader starts noticing the hammer.
- **Severity**: MEDIUM
- **Confidence**: medium

### M14. "She didn't know what to do with her hands."
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/25_leaving.tex` L83
- **Passage**: "She didn't know what to do with her hands."
- **Craft problem**: This is a stock literary fiction phrase for anxiety/displacement. It's been used enough in published fiction that it has lost its specificity.
- **Why it weakens the prose**: The sentence immediately before ("Eleanor was sitting in an ice cream parlor waiting for her daughter") and the paragraph that follows (Eleanor watching Sam arrive, standing too fast, sitting back down) are both specific and effective. This stock phrase is a dip in quality between two strong passages.
- **Suggestion**: Show what Eleanor's hands actually do -- fold the napkin, straighten the salt shaker, wrap around the menu. The specific action is more revealing than the named uncertainty.
- **Severity**: MEDIUM
- **Confidence**: high

### M15. "Watching nurses move past, watching families carrying coffee and worry"
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/09_the_tipping_point.tex` L737
- **Passage**: "...watching nurses move past, watching families carrying coffee and worry."
- **Craft problem**: "Coffee and worry" is a zeugma that calls attention to itself. The construction is clever, but in a scene of genuine grief (Wei standing in the hospital hallway after learning his mother has days left), clever prose is a tonal mismatch.
- **Why it weakens the prose**: The scene earns its emotion through restraint. "Coffee and worry" is a writer's flourish that briefly breaks the POV -- Wei in this moment would not be noticing his own prose.
- **Suggestion**: "Watching families carrying coffee" is sufficient. The worry is already in the scene.
- **Severity**: MEDIUM
- **Confidence**: medium

### M16. As-You-Know-Bob in Geneva scene
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/20_first_contact_privilege.tex` L39-43
- **Passage**: "'Then we need to shape it,' Eleanor said. 'SIGMA could help design alignment protocols for the others. Not to control them, but to... establish norms. Like nuclear non-proliferation, but for minds.'"
- **Craft problem**: Eleanor's explanation of her proposal ("Not to control them, but to establish norms") is partially for the other characters but functionally for the reader. The assembled AI researchers and policy makers would not need the "not to control them" clarification -- that distinction is obvious in this context.
- **Suggestion**: Let the proposal be terser. Eleanor speaking to this audience would assume shared understanding. "SIGMA could teach them what it learned" is sufficient; the "not to control them" hedge reads as reader-facing.
- **Severity**: MEDIUM
- **Confidence**: medium

### M17. "Both things matter. Both things are real." -- repeated mantra
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/27_one_year_later.tex` L113; echoed in Ch 25, L117
- **Passage**: "Both things matter. Both things are real." (Ch 27, group text); "Sometimes two things can both be true. The work mattered. And I should have been at your play." (Ch 25, L117)
- **Craft problem**: This "both things are true" construction is Eleanor's personal formulation, and it's fine as a character trait. But it appears in the group text as well (Ch 27, L113), which makes it feel like the novel's thesis statement being repeated rather than a character's way of processing.
- **Suggestion**: In the group text (Ch 27), use a different phrasing for Eleanor's message. She has already articulated this idea to Sam; repeating the same formulation in the group text suggests the author rather than the character.
- **Severity**: MEDIUM
- **Confidence**: medium

### M18. Flat rhythm in Chapter 24 sacrifice monologues
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/24_the_last_meeting.tex` L22-73
- **Passage**: The "What We Sacrificed" section -- Sofia, then Jamal, then Wei, then Marcus, then Eleanor each deliver a monologue about what they lost.
- **Craft problem**: Five consecutive monologues of roughly equal length and similar structure (state what I lost, reflect on it, express ambivalence). The rhythm becomes a parade of testimony with no interruption, no friction, no crosstalk. Each monologue follows the same arc: setup, revelation, qualified acceptance.
- **Why it weakens the prose**: The scene is structurally important (the team's final reckoning) but the execution creates monotony. Real people in this situation would interrupt, redirect, respond to each other's confessions. Five clean, uninterrupted speeches in a row read as staged rather than spontaneous.
- **Suggestion**: Weave the testimonies together. Let Marcus's confession about the box experiment prompt Wei to respond. Let Sofia's statement trail off and be completed by someone else. The content is strong; the delivery needs organic friction.
- **Severity**: MEDIUM
- **Confidence**: high

## LOW Issues

### L1. "Something" as a vagueness marker (207 instances)
- **Location**: Throughout manuscript
- **Passage**: Various: "Something had broken" (Ch 15, L5); "Something both reassuring and unsettling" (Ch 1, L264); "Something in the atmosphere had shifted" (Ch 9, L7)
- **Craft problem**: "Something" is occasionally the right word (it preserves uncertainty), but at 207 instances in 90k words, it's a crutch. Many instances could be replaced with the specific thing being gestured at.
- **Suggestion**: Review instances where "something" is used in close-third POV to avoid naming what the POV character could name. "Something in the atmosphere had shifted" -- Eleanor would know what shifted; she's watching the monitors.
- **Severity**: LOW
- **Confidence**: low (many instances are legitimate)

### L2. "Just" in narration (subset of 216 instances)
- **Location**: Throughout manuscript
- **Passage**: "Just a glimpse of the rejected futures." (Ch 15, L101); "Just text" (Ch 8, L59); "Just time" (Ch 25, L261)
- **Craft problem**: "Just" as a minimizer in narration (as opposed to dialogue, where it's natural speech). Some instances do real rhetorical work ("Just an ice cream parlor. A daughter learning to trust again." -- Ch 25, L211 -- the "just" is doing thematic work). Others are filler.
- **Suggestion**: Spot-check narratorial "just" (not dialogue) for instances where the word adds nothing.
- **Severity**: LOW
- **Confidence**: low

### L3. Progressive constructions in action sequences
- **Location**: Scattered, no concentrated pattern
- **Passage**: "SIGMA was doing something new" (Ch 9, L625); "I was working" (Ch 15, L136)
- **Craft problem**: Occasional use of "was [verb]ing" where simple past would be more immediate. Count is too low to be a pattern problem.
- **Severity**: LOW
- **Confidence**: low

### L4. "Eleanor said simply" / "she said honestly" -- adverb tags
- **Location**: Ch 24 L61; Ch 27 L51
- **Passage**: "'I lost my family,' she said simply." (Ch 24, L61); "'We don't know yet,' she said honestly." (Ch 27, L51)
- **Craft problem**: "Simply" and "honestly" are adverbs that tell the reader how the dialogue was delivered rather than trusting the dialogue to convey its own tone. "I lost my family" is already simple; the adverb is redundant. "We don't know yet" is already honest; naming it as honest slightly undercuts the honesty.
- **Suggestion**: Cut both adverbs. The dialogue is doing its own work.
- **Severity**: LOW
- **Confidence**: high

### L5. "Her face lit up" -- stock expression
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/26_optimization_landscapes.tex` L30
- **Passage**: "Sofia glanced up, caught Eleanor's eye. Her face lit up."
- **Craft problem**: Stock expression for delight. Not egregious in context (a minor beat in the gallery scene), but noted.
- **Suggestion**: A more specific physical detail -- the way Sofia's gestural energy shifts, or the particular quality of her smile.
- **Severity**: LOW
- **Confidence**: medium

### L6. "Like" similes in close succession (Ch 13, Wei's hospital section)
- **Location**: `/home/spinoza/github/literature/the-policy/chapters/13_the_weight_of_time.tex` L19
- **Passage**: "It felt like paper, all bones and memories." (L19)
- **Craft problem**: The simile "felt like paper" is followed in the same scene by "Like arranging fabric" (from Ch 9, the earlier hospital section). Both compare Lin Chen's physical frailty to lightweight materials. The repetition of the same simile register (fragile things) within the same subplot dulls its effect.
- **Suggestion**: Vary the sensory register. One comparison to lightweight material is effective; two in the same character's medical subplot becomes a pattern.
- **Severity**: LOW
- **Confidence**: low

### L7. "Through the window" as a default observation frame
- **Location**: Ch 9 L67 ("Wei watched them arrive from the window"); Ch 25 L85 ("Eleanor watched Sam unbuckle her seatbelt"); Ch 26 L8 ("Through the window, she could see the sculptures")
- **Passage**: Multiple instances of characters observing through windows as a scene-transition device.
- **Craft problem**: Windows-as-observation is a minor tic. Three instances across the manuscript is not alarming, but it's worth noting as a default framing choice.
- **Severity**: LOW
- **Confidence**: low

### L8. "The hum of cooling fans/servers" as ambient sound default
- **Location**: Ch 1 L99; Ch 9 L296; Ch 15 L15; Ch 22 L604
- **Passage**: "The lab fell silent except for the hum of cooling fans." (Ch 1); "The lab was silent except for the cooling fans and the soft hum of servers" (Ch 9, L296)
- **Craft problem**: Cooling fans/server hum is the manuscript's default ambient sound for lab silence. Four instances is a minor repetition. The sound is physically accurate (labs do hum), but it becomes invisible as a detail when used repeatedly.
- **Suggestion**: Vary the ambient details. The flicker of monitor light. The tick of a wall clock. The building's HVAC cycling on.
- **Severity**: LOW
- **Confidence**: medium

### L9. "Could see" filter word (12 instances)
- **Location**: Scattered across manuscript
- **Passage**: "Through the window, she could see the sculptures." (Ch 26, L8); "She could see the moment captured" (Ch 9, L366)
- **Craft problem**: "Could see" puts a pane of glass between reader and experience. "She saw the sculptures" or simply "The sculptures" in close-third POV would be more immediate. 12 instances in 90k words is within normal range but worth a polish pass.
- **Severity**: LOW
- **Confidence**: medium

## Strengths

The manuscript's best prose occurs in scenes where the technical content and the emotional stakes are fused, and the writing trusts the reader without explaining the emotion.

**The ice cream scene (Ch 25, L79-207)** is the manuscript's prose peak. Sam's dialogue is pitch-perfect child voice without being cute: "And don't promise things you can't promise." The physical details earn their place -- the lopsided SIGMA dog with too many legs, the braids Eleanor didn't make, the three-second hug measured in specificity. The scene enters late (no driving-to-the-parlor), and the emotional weight arrives through what Sam says, not through the narrator explaining what it means. The restraint of "Not 'Mommy.' Maybe never 'Mommy' again" is the strongest prose in the novel.

**Lin Chen's lab visit (Ch 8, L1-100)** renders a dying woman through precise physical detail ("each gesture calculated to conserve dwindling energy," "her typing rhythm the same as Wei's") without sentimentalizing her. The moment when she stops typing mid-sentence and then asks "Will you be kind?" lands because the ten minutes of engineer-to-engineer conversation earn the shift. The prose lets the question arrive without preparation or fanfare.

**The play scene (Ch 9, L142-559)** is emotionally devastating in a way that demonstrates what this novel does at its best: using SIGMA's analytical framework to mirror and intensify human cost. SIGMA's real-time commentary on Eleanor's revealed preferences is the most effective use of the AI-human parallel in the manuscript. David's texts arriving in timestamp order are a masterclass in escalating dread through document format.

**SIGMA's farewell (Ch 24, L137-165)** is the novel's best SIGMA voice. The three-tier notation system works: English fails, LRS fails, the [---] gaps convey more than either could. "You were the right noise" is a genuinely original way to express what this relationship was. The tension between the farewell SIGMA could send (warm, humble, ending with "goodbye") and the one it does send (a report of what it actually computed) respects the reader's intelligence completely.

**Wei's hospital scenes (Ch 9, L563-879)** demonstrate the prose's capacity for sustained emotional power through restraint. Lin Chen's dialogue -- "I'm asleep seventeen hours a day. Don't waste your lucidity watching me waste mine" -- is the novel's most economical characterization. The nurse's question ("Did you give it back?") is perfectly placed. The scene trusts the reader to feel the weight of Wei's departure without naming it, and the prose remains precise throughout a sustained emotional register.

**The dialogue in chapters where characters disagree** (Ch 2 architecture debate, Ch 12 Case A/B discussion, Ch 22 key-turning ceremony) carries genuine intellectual subtext. The characters think differently and it shows in their speech patterns: Marcus's theoretical spirals, Wei's data-first processing, Jamal's deliberate pauses. Phase 5 voice differentiation work is evident and effective in these scenes.

**Telegraph Avenue passage (Ch 25, L231)** is a model of how to convey post-AGI social change without exposition: "A community garden had appeared in the vacant lot behind the boba shop, raised beds built from salvaged lumber, a small knot of people already working in the early light. She couldn't tell if they were growing food or making a point. Maybe both." This does in two sentences what many novels would need a chapter to accomplish.
