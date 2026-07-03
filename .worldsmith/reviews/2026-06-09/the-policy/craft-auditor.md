# Craft Audit, The Policy (2nd-Edition Decision Support)

**Date:** 2026-06-09
**Auditor role:** Prose-craft maturity (the primary concern for this decision)
**Scope:** Full structural read plus sentence-level analysis of Ch 1, 3, 16, 17, 19, 24, 25, 26 (current text); mechanical pattern audit across all 25 active chapters.
**Question this serves:** Is the gap between this book's prose craft and a strong current literary-SF standard large enough to justify a paid 2nd-edition pass, and if so, what specifically, without flattening the book?

---

## VERDICT (craft grounds): OPTIONAL LIGHT-TOUCH, trending toward WARRANTED on production hygiene alone

On pure sentence-level craft, the gap to a current Chiang/Egan/Watts standard is real but moderate, and narrower than the author fears. The prose is not amateur. At its best (Ch 16 Sofia's ontological speech, Wei's negative-infinity Q-values; Ch 24 SIGMA's farewell; Ch 17 the Conteh video; Ch 25 the ice-cream scene) it is genuinely at-standard: controlled, restrained, doing real work. The weaknesses are not "bad writing." They are three repeatable habits (terminal-exchange dependency, declarative theme-narration, soft-adverb dialogue tags) plus a set of genuine production bugs that a published book should not ship with. None of these requires a rewrite. They require a disciplined editing pass.

The honest framing for the author: a 2nd edition is not needed to rescue the prose, because the prose mostly works. But a focused copy and line pass would visibly raise the floor and fix defects that currently undercut a strong book in front of paying readers. If the deciding factor is "is the writing embarrassing enough to demand a redo," the answer is no. If it is "would a bounded pass meaningfully raise quality per hour," the answer is yes, via the must-fix list below.

---

## The gap to current-standard literary SF: what specifically separates them

Three things, in order of impact:

1. **Mode monotony, not sentence quality.** Chiang and Egan vary how a scene delivers its idea. The Policy delivers ideas through one dominant mechanism, a human types, SIGMA answers in a `quote` block, humans gloss the answer aloud, roughly 40-plus times. The individual exchanges are often excellent; the sameness of the delivery vehicle is what reads as less mature. This is a structural-craft issue (see structure audit) but it shows up at the prose level as scenes that sound alike.

2. **The narrator over-explains the theme the scene just dramatized.** The strongest current SF trusts the image. The Policy frequently lands a beat through action or dialogue and then a sentence of narration states the lesson. Examples below. This is the single most fixable-and-worth-fixing craft gap.

3. **Dialogue-tag and stage-direction texture.** Soft-adverb tags ("said quietly" x13, "said slowly" x13, "said finally" x8, "asked quietly" x7) and recurring physical business (glasses, coffee-set-down-with-care) are still dense enough to register as a narrator's tic rather than character tags. The author already did one reduction pass; the floor is still above current-standard.

What does not separate them: ambition, idea density, the structural daring of the central conceit, the willingness to leave the core question unresolved, or the best set-pieces. Those are at or above standard.

---

## MUST-FIX (if reopened), ranked, with effort

### M1. Production bugs in the published artifact [HIGH, confidence HIGH]. Effort: LIGHT (hours)
These are defects in the shipped book, independent of any aesthetic question. They should be fixed regardless of whether a full 2nd edition happens.

- **Unescaped `%` in LaTeX deletes text.** A raw `%` comments out the rest of the line in LaTeX. Confirmed instances:
  - `chapters/17_the_policy_revealed.tex:17`, the line reads `pruning maybe 95%, exploring more broadly. Now it knows which branches are worth considering.''` Everything after `95`, to end of line, is commented out in the compiled PDF. The reader sees `pruning maybe 95` and the sentence dies.
  - `chapters/09_the_tipping_point.tex:101`, `SIGMA-naive} shows 30% less strategic modeling...` Same defect; text after `30` is dropped.
  - (Ch 15 lines 72-73, `99.97%` and `99.9999%`, appear inside a code-style display block; verify whether those render or also drop.)
- **Missing opening quotation mark**, `chapters/26_optimization_landscapes.tex:108`. The line renders as: I'm at the Global Health Initiative, Wei said. Using AGI recommendations to optimize resource allocation. Medical supplies, treatment protocols, epidemic response. It's good work. Important work. The second through fourth sentences sit outside the quotes; the closing quote mark has no partner. Reads as a punctuation error on the page.
- **Inconsistent `\texttt{SIGMA}` (monospace) versus plain SIGMA.** Eleven chapters render the AI's name in typewriter font via `\texttt{SIGMA}` (heaviest: Ch 10, 12, 16, 19, 22; also 6, 7, 9, 14, 15, 21), while Ch 1, 3, 17, 24, 25 use plain SIGMA. In a published book this is a visible typographic inconsistency: the protagonist's name changes font roughly half the time, sometimes mid-chapter. Pick one (plain, almost certainly) and normalize globally.

Why HIGH: these are objective defects a reader can see, or that have deleted prose, in a product currently on sale. A few hours of find-and-fix. This item alone is a respectable reason to cut a `v1.2` even if nothing else is touched.

### M2. Cut roughly 40 to 50 percent of declarative theme-narration [HIGH, confidence HIGH]. Effort: MEDIUM (1 to 2 days)
The recurring pattern: a scene shows the idea, then the narrator or a character states it. The statement is almost always the weaker line. Concrete current-text instances:

- Ch 1: after the whiteboard "Alignment Status: Uncertain," Wei says "We're in epistemic free-fall." The whiteboard already said it.
- Ch 17: after the Conteh video (which is devastating and self-sufficient): "The policy was correct. The death was unbearable." Then later: "That was the horror. Not that innocents died without understanding. That they understood perfectly and it changed nothing." The video is that horror; naming it twice dilutes it.
- Ch 17: Sofia's "This is what aligned AGI looks like. Not friendly. Not safe. Not comfortable." A thesis statement handed to the reader.
- Ch 26: "Whether they asked because they cared, or because asking was optimal, Eleanor didn't know." The dashboard (2.8M kindness queries per day) already poses this; the sentence narrates the ambiguity the image created.

Fix: keep the dramatized beat, delete or halve the narrated gloss. This is the highest-impact aesthetic pass; it is exactly what moves the prose toward Chiang's restraint. It is line-level surgery, not restructuring; roughly 1 to 2 focused days across 25 chapters. This is the pass most likely to make the book feel a tier more mature.

### M3. Thin the soft-adverb dialogue tags and de-duplicate physical tics [MEDIUM, confidence HIGH]. Effort: LIGHT-MEDIUM (half-day to 1 day)
Current counts (raw): `said slowly` 13, `said quietly` 13, `said finally` 8, `asked quietly` 7, `said simply` 5; `said [X]ly` total 57. Plus the named tics (glasses, "with care") still cluster. The author already did one reduction; it did not reach current-standard density.
Fix: target the soft adverbs specifically (quietly, slowly, softly, gently). Most can be cut outright or replaced with a beat. Preserve the intentional tics flagged in style.md (Eleanor and the kill switch, Marcus and glasses, Jamal and "with care") but reduce their frequency by roughly 30 to 40 percent so they tag emotion rather than appear on schedule. Cheap, visible improvement.

### M4. Break the terminal-exchange monotony at the prose level in 3 or 4 high-traffic chapters [MEDIUM, confidence MEDIUM]. Effort: MEDIUM-HEAVY (coordinate with structure audit)
This is primarily structural (see structure report), but on the craft side: the most exchange-dense chapters (Ch 16, 17) stack multiple long `quote` blocks with human glosses between each. Even 2 or 3 substitutions per chapter (render a SIGMA answer as reported speech filtered through a POV character's dread; or cut a confirm-the-obvious gloss) would reduce the "sounds the same" effect without losing content. Flagged MEDIUM because done carelessly it could flatten the deliberate texture (see Do-Not-Touch).

---

## NICE-TO-HAVE (lower-priority polish)

- **N1.** Crutch words: `something` 224, `just` 213, `actually` 53. Many `just` and `actually` are dialogue-natural; `something` is the more telling one (often vague where a concrete noun would land harder, for example "something in his eyes," "something died"). A targeted `something` and `just` pass would tighten, but yields diminishing returns after M2. Effort: light, optional. Do not blanket-strip; Sofia's hedging legitimately uses these.
- **N2.** Residual stock phrases. The prior review caught the worst ("stared into an abyss"). Spot-check survivors: Ch 19 "as if the sky itself had entered deliberation," and "the cursor blinking like a silent metronome." Competent but slightly purple against the book's otherwise spare register. Optional.
- **N3.** The SIGMA-as-parent metaphor is still drawn explicitly several times (Ch 17 "raised you? Like parents shape a child"; Ch 20 "raised, not built"; recurs in Geneva and the gallery). Prior review wanted two at most. Trimming one or two instances would help; low stakes.
- **N4.** Internal-monologue-versus-dialogue formatting occasionally blurs (style.md open question). A consistent convention (for example, italics reserved for true interiority) would sharpen a handful of moments. Optional, light.

---

## DO-NOT-TOUCH (rough-but-alive, preserve)

These are places where energy or voice would be lost by polishing. Be explicit with the author:

- **The best SIGMA outputs are at-standard. Leave them.** Ch 16 Sofia's "There is nothing behind this... we're either talking to someone, or we're talking to no one, and there's no third option"; Ch 24's "you were the right noise" and the bracketed-dash gaps; Ch 16 Wei's negative-infinity Q-values ("Not negative ten to the sixth. Negative infinity"); the temperature experiment's "like hearing a conversation in a room I was previously ignoring." This is the book's ceiling and it is high. Do not smooth the three-tier notation (COMPRESSED, LRS, the bracketed dash). Its strangeness on the page is the point and it is doing exactly what current SF does well.
- **The intentional repetitions are thesis-work, not crutches.** "Is it kind?" recurring; Case A and Case B returning each part; "Same data either way" as Ch 16's refrain; SIGMA's self-hedging signature. The pattern audit will flag these as repetition. They must not be counted against the book or varied for freshness. This is per style.md and it is correct.
- **The flat affect under grief is a feature.** Wei's data-register breaking for exactly one sentence ("She would have liked that") then re-arming. That control is mature. Do not add warmth.
- **Sam's dialogue.** "don't promise things you can't promise"; "always saturdays." Pitch-perfect; do not adjust.
- **The opening's raw forward drive.** Ch 1's terminal-and-family-text engine is alive even though it is the template that later fatigues. The opening earns it. Do not sand the urgency out of Ch 1 to 3 in the name of consistency.

---

## Finding counts
HIGH: 2 (M1 production bugs, M2 theme-narration). MEDIUM: 2 (M3 tags and tics, M4 exchange monotony). LOW/NICE: 4 (N1 to N4).

## Bottom line for the decision
The prose does not mandate a 2nd edition to avoid embarrassment; the author is underrating it. But M1 (defects, hours) plus M2 (theme-narration trim, 1 to 2 days) plus M3 (tags, about 1 day) is a bounded line pass of roughly 3 to 4 days that would raise the book a visible half-tier toward its Chiang/Egan target without touching the structure or the voice. That is the highest quality-per-hour intervention available, and it is the right scope: light-touch, defects-and-restraint, preserve the ceiling.
