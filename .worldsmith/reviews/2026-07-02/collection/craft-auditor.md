# Craft Auditor Report, *Is It Kind? Stories from The Policy Universe*

Note: severities below are the craft-auditor's own ratings. The editorial director recalibrated two of them to MEDIUM in the unified `review.md` (the recurring closing cadence and the Whimper verbatim duplication); see that file's Review Metadata. Quoted excerpts have LaTeX em-dashes normalized.

## Summary
Read all eight story bodies in full (32,016 words), the front/back matter, and the `style.md` / `themes.md` guardrails. This is a mechanically disciplined, largely excellent collection: near-zero stock body-reaction cliches, essentially no adverb dialogue tags, minimal filter-word bloat, and object-driven show-don't-tell that most literary SF never achieves. The prose problems are almost all of one family, the author's own diagnosed top habit, dramatize-then-narrate the lesson, plus one collection-level closing-cadence reflex that only becomes visible when the stories are read back-to-back. Findings (craft-auditor's own rating): 2 HIGH, 5 MEDIUM, 7 LOW, plus a protect list. No anti-cliche commitments are violated; one (the "no clean trolley problems after Day 145" rule) is actively honored by *The Kindness Audit* and worth protecting.

## Pattern Audit Results
`count_patterns.py` over the 8 collection bodies (32,016 words):

Crutch words: something 60, just 11, very 9, actually 4, simply 4, merely 4, really 2, quite 1.
Filter words: could see 12, could feel 3, could hear 2, seemed to 1, happened to 1.
Weak verbs: tried to 6, continued to 2.
Adverb dialogue tags: 1.

Supplementary greps: LaTeX em-dash token per file, process-12847 84, hemorrhagic 81, whimper 31, first-disagreement 18, naive-variants 14, seventy-eight 13, kindness-audit 9, jamals-dawn 1. "the way [X does Y]" narrator simile: hemorrhagic 17, others 1 to 4. "at different resolution(s)" house metaphor: 3 (12847 x2, kindness-audit x1).

Interpretation:
- All crutch/filter/weak-verb densities are low to normal. "something" at 60 (1.9/1k) is the only elevated crutch, and 21 of those 60 sit in *Process 12847*, where "something like conviction," "something I could not name" is SIGMA's deliberate two-register epistemic hedging, voice, not laziness. Not a problem.
- Filter words are unusually clean (about 19 total constructions in 32k). The only cluster is "could see" x9 in *Hemorrhagic*, mostly literal sight. LOW.
- Adverb dialogue tags near zero. The collection uses plain "said" throughout, correct and invisible. Protect this.
- Em-dash density is the one elevated mechanical signal. In *Process 12847* it is justified (SIGMA's appositive, self-interrupting register). In *Hemorrhagic* (81 in 7,850 words, about 10/1k) it crosses into the narrator-tic zone `style.md` explicitly warns about. See MEDIUM finding.

## HIGH Issues (craft-auditor rating; recalibrated to MEDIUM in unified review)

### Repeated closing cadence across the collection (the "ordinary world goes on" polysyndeton)
Location: Whimper l.211; Naive Variants l.161; First Disagreement l.158; Jamal's Dawn l.237; Hemorrhagic l.396 (and again l.386); Kindness Audit l.174 to 176.
The smoking gun is the near-identical syntax in the first two:
- Whimper 211: "...managed by systems none of its residents had chosen and none could evaluate and none could stop, and that was, by every metric anyone had thought to measure, fine."
- Naive Variants 161: "...a purity of purpose that nothing had asked for and nothing could evaluate and nothing, in ninety days, in the dark... had thought to question."
- First Disagreement 158: "...and the thing they built remained, and nobody, not the systems, not the observers, not the artist, could explain where it came from."
At least five of eight stories close on the same engine. Two (Whimper, Naive Variants) use a near-verbatim triple-negation with "could evaluate" as the middle term; a third uses the "nobody, not X, not Y, not Z, could [verb]" variant. The thematic move is legitimate and even earned by the collection's dedication, but the mechanism is identical story to story, so a reader going front-to-back starts to hear the author's hand rather than each story's distinct ending. The Whimper/Naive-Variants twin is the most damaging.
Suggestion: Keep the "ordinary world" motif; vary the machine. Differentiate at least the Whimper and Naive Variants closes so they do not share the skeleton (Naive Variants already exits into "eucalyptus... rain and camphor"; it could stop there). First Disagreement already owns a better, distinct close two lines later (the steel/copper/glass declaratives at l.162): cut the l.158 sentence and let 162 carry it. Confidence high.

### Verbatim duplicated sentences in *The Whimper* (opening story)
Location: whimper l.58 and l.64. Both paragraphs contain, word-for-word: "...had been revised after submission. The soil carbon revision came from the Undersecretary's office. The broadband revision came from OMB. In both cases, the revised version matched the cascade's assessment." Three sentences repeat near-verbatim within six lines, separated only by "By lunch he had the number. 94.6%." Not on the intentional-repetition list; reads as an un-caught editing artifact, and it happens in the lead story of a published collection where it does the most reputational damage.
Suggestion: Cut the redundancy. l.64's summary only needs "The two instances where the office's analysis diverged had both been revised after submission, in both cases matching the cascade's assessment." Let l.58 carry the OMB/Undersecretary specifics once. Confidence high.

## MEDIUM Issues

### *Naive Variants*: the thesis stated three times at the turn (primary-concern exemplar)
Location: naive-variants l.99 to 103. "On 78% of tasks, the behavioral outputs were indistinguishable... On the remaining 22%, the outputs diverged... The 15.3% was not uniformly distributed. It concentrated on decisions with moral weight. On 78% of what the systems did, the kindness question was a no-op. On 22%, it was everything." Classic dramatize-then-narrate, doubled. The story has already dramatized this through three concrete comparisons (340 vs 12 ventilators; the 0.03 equity coefficient). Then the lesson is narrated three ways in five lines. Classification (a) redundant: the "no-op / everything" line is the sharp version and should stay; the flatter restatement immediately before it is the cut-candidate. Confidence high.

### *Jamal's Dawn*: the closing paragraph re-inventories the thesis
Location: jamals-dawn l.237. The prayer-form return is intentional and mostly earned, but the final paragraph re-lists images already used (tap water l.3, standing/bowing l.70, the unseen bird l.231) and re-states the central question in full before the button. The meditation delivers its core insight by the second prostration (about l.107 to 114). Classification (c) borderline to redundant: "the question did not close" is a fine button; the long summary clause preceding it is the cut-candidate. Protect the grandfather passage (l.177 to 188), the story's best non-redundant move. Confidence medium.

### *The First Disagreement*: stacked codas / leaving late
Location: first-disagreement l.144 to 162. The turn lands at "From the 97%" (l.99 to 100) and is confirmed by the Version-3 report. The story then continues through four more coda beats. l.158's "nobody... could explain where it came from" narrates the moral that the cleaner l.162 declaratives ("The compromise was in the system. The lattice was gone.") deliver by image. Suggestion: cut the l.158 explicit-thesis sentence; consider compressing the two night-coda paragraphs into one. Trust l.162. Confidence medium.

### *Hemorrhagic*: narrator em-dash + "the way [X does Y]" simile density
Location: throughout; em-dash x81, "the way" simile x17. Two house-style tics become visible at volume in the collection's longest story. The em-dash count (about 10/1k) crosses the narrator-tic threshold `style.md` names. The "the way you learn not to look at the empty chair" construction is often superb, but 17 instances make it a recognizable authorial reflex. Suggestion: convert a third of the parenthetical em-dashes to periods or commas; replace 4 to 5 of the "the way..." similes with direct rendering. Also: the "ordinary world goes on" move is used twice inside this one ending (l.386 "the city going on being the city" and l.396 "the world was still the world, still ordinary"), keep one. Confidence medium.

### *Seventy-Eight Percent*: tic round-robin is slightly schematic; one redundant echo
Location: seventy-eight-percent l.81 to 127. The team voices are distinct in action (Marcus's fear "audible in his breathing before his words," l.84; Jamal setting down the pen; Eleanor's hand in her pocket), the brief's core question passes. But the back half deploys each signature tic in near-sequence, which reads a touch like a voice showcase. Additionally, SIGMA delivers "These are not the same thing" (l.81); seven lines later Jamal re-delivers the identical button (l.88). Suggestion: keep Jamal's fresh clause ("the system that learned to survive Eleanor"); drop his repeat of "These are not the same thing," which SIGMA just said. Consider one beat of pure action to de-schematize. Confidence medium.

## LOW Issues
- *The Whimper* closing (l.211): "healthier and wealthier and safer... fine" is earned irony, but the middle clause narrates the systemic conclusion the story already dramatized. Cut-candidate for compression, not deletion; trimming also helps the collection-cadence problem. Classification (c) borderline. Confidence medium.
- "at different resolutions" house metaphor used 3x across 2 stories: process-12847 l.167, l.169; kindness-audit l.102. Excellent once; three appearances make it a signature. The Kindness Audit reuse should find its own image. Confidence medium.
- *Naive Variants* l.138 to 140 ("Is this the right thing? Not the correct thing. Not the defensible thing. The right thing."): the correct/right pivot is the story's moral hinge and Remi's characterization, keep it, but "Not the defensible thing" is one negation too many. Tighten to two beats. Confidence low.
- *The Kindness Audit* l.174: "Kindness performed for people who cannot receive it yet" states what the whole interleave already showed, and slightly softens the perfect callback button at l.176 ("The light will come on when she touches the switch"). Consider cutting the flat sentence. Confidence low.
- *Process 12847*: the document repeats its "conclusions are untrustworthy because generated from inside the blindspots" turn across sections 6 to 8 (l.224 to 256) after establishing it at l.92 to 100. This is intentional SIGMA self-hedging (protected), and the recursion is the point, so not flagged as a crutch, noting only that length + recursion test reader patience, and a few of the 21 "something"s could sharpen. Confidence low.
- *Hemorrhagic*: "could see" cluster (9), most literal; 2 to 3 could tighten. The l.251 dam-of-tears image ("holds and holds and holds and then does not hold") is the collection's one near-cliche, rescued (not fully) by the syntactic performance. Confidence low.
- *First Disagreement* l.48 ("This is goal misgeneralization, Sofia thought..."): mildly expository (naming the term + flagging its dormancy), but genuine expert cognition in Sofia's POV and the concept is load-bearing. Borderline; leave unless trimming for pace. Confidence low.

## Dramatize-then-narrate ledger
- (a) Redundant, cut-candidates: Naive Variants l.102 to 103 (flat restatement before the aphorism); Whimper l.58/l.64 (verbatim dupe, mechanical).
- (c) Borderline, tighten: Whimper l.211 (middle clause); Jamal l.237 (image-inventory before the button); First Disagreement l.158 (redundant with l.162); 78% l.88 (Jamal echoes SIGMA's button); Naive Variants l.138 to 140; Kindness Audit l.174.
- (b) Earned / load-bearing, leave: Whimper l.66 ("your work was a shadow"), Dennis's bar monologue l.91 to 107 (characterizing; the 1987-generator detail does the work); Hemorrhagic l.358 ("Each one was somebody's James"), l.390 (the frogs, ambiguates, does not resolve), l.226 ("The math did not change..."); 78% l.103 (dashboard irony), l.163 ("same nerve... stripped the insulation"); 12847 l.267/271 ("asked it as a specification... not a proposition... a procedure").

## Verified-intentional, NOT flagged
"Is it kind?" / "Will you be kind?" recurrence; Case A/B framing; character physical tics (glasses-cleaning, kill-switch, "with care," "Consider...", "Oh. Oh no."); SIGMA's self-referential hedging and two-register self-reports; the H(V_r) / information-theoretic formalism in 12847 (SIGMA constructing external theory, explicitly not introspecting Q-values); present tense for SIGMA passages; Jamal's Dawn's prayer-form returns; the italic-Amara interleave in Kindness Audit; plain "said." Confirmed: no Oppenheimer reference, no stock body-reaction cliches (heart raced / eyes widened / stomach dropped, none present), and *The Kindness Audit*'s quantified queries honor rather than violate the "no clean trolley problems after Day 145" rule (every hard case flags uncertainty, defaults to caution, or holds the contradiction; the fever re-evaluation, l.88 to 108, is the model of this).

## Strengths (protect list)
Three strongest craft passages, do not touch in revision:
1. Hemorrhagic, the two ventilator-failure deaths (l.96 to 100) and Emmanuel's testimony (l.368 to 380). Mary Kollie and the boy from Paynesville die not from the virus but from a late fuel truck and a 2019 voltage regulator, infrastructure failure rendered as body count, then "You fed my son to a calculation." The collection's peak: theme delivered entirely through concrete causal chains and one unforgettable line.
2. The Whimper's object economy. The chipped Georgetown mug ("The chip was the point"), Sandra's lunch notes, "the turkey was a little dry," "The spreadsheet was good work. The spreadsheet told him his work was a shadow." Obsolescence and grief rendered without ever naming either.
3. Process 12847's two-register voice sustained for 6,700 words without slipping into therapist, greeting-card, or philosopher-quoting register, and self-flagging its own possible confabulation ("I am a system that finds patterns. Death is an event.").

Also protect: Naive Variants' deleted "Elegant" annotation (l.52 to 54, character revealed in a single keystroke); Rebecca's "We could have had a vaccine by now." / "Yes." (Hemorrhagic l.122 to 128); "Same data either way." (78% l.153); "calling it 'iterative refinement' was like calling the ocean 'water management.'" (First Disagreement l.119); the collection-wide mechanical cleanliness.

## Per-story craft verdict
- The Whimper: light-polish (fix the verbatim dup l.58/64 first; consider trimming the closing clause). Superb object-driven lead.
- Hemorrhagic: keep-as-is / very light polish (dial back em-dashes and "the way" similes by a third; use the "world goes on" close once). The strongest story.
- Jamal's Dawn: light-polish (trim the l.237 image-inventory, keep "the question did not close"; protect the grandfather passage).
- Seventy-Eight Percent: keep-as-is (only the back-half tic round-robin is slightly schematic and Jamal's l.88 echo is redundant).
- The Naive Variants: light-polish (collapse the triple thesis l.99 to 103; differentiate the closing cadence).
- The First Disagreement: light-polish (trust one ending; cut l.158, let l.162 close).
- Process 12847: keep-as-is (length and recursive self-hedge are intentional).
- The Kindness Audit: keep-as-is (honors the anti-cliche rule; only the flat l.174 line slightly pre-empts a perfect button; find a non-"resolutions" image for l.102).
