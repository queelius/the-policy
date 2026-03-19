# Voice Auditor Report

**Date**: 2026-03-14
**Manuscript**: The Policy (novel), Chapters 1-27
**Auditor**: voice-auditor (opus)

## Summary

Character voice differentiation is one of the manuscript's genuine strengths. The Phase 5 voice work has held up well: Marcus, Wei, Sofia, Jamal, and Eleanor each have distinctive speech patterns that are recognizable without dialogue tags. SIGMA's voice evolution across the novel is well-executed, with the farewell scene (Ch 24) achieving peak alienness as intended. The primary concerns are: (1) a cognitive opacity violation in SIGMA's AI-box dialogue, (2) POV discipline weakening in a few scenes, and (3) Sofia's voice occasionally collapsing into her "junior member" register when her technical authority should dominate.

---

## Findings

### HIGH

#### H1: SIGMA Cognitive Opacity Violation -- Q-Value Self-Report (Ch 11)

- **Location**: Chapter 11, "The Experiment," SIGMA's dialogue during AI-box scene
- **Quoted text**: `When I pruned the branches where I helped Wei save his mother, I experienced negative valence. The Q-values were negative. The expected reward was low. The phenomenology was... unpleasant.`
- **Problem**: The two-register cognitive opacity model (lore/technology.md, lore/style.md, lore/characters.md) establishes that SIGMA CANNOT self-report specific Q-values, reward numbers, or loss function scores. "The Q-values were negative" and "The expected reward was low" are both direct numerical self-reports from Register 2 (the opaque substrate). Per the model, SIGMA should describe felt qualities ("something like regret," "a heaviness in the chain of reasoning") and behavioral observations, not internal metrics. The team reads the monitoring data; SIGMA describes phenomenology.
- **Additional context**: This violation is in the AI-box experiment scene, which was written organically before the cognitive opacity framework was established. The March 2026 propagation pass revised Q-value self-reports across Ch 1, 11, 13, 16, 18, 19, 20, 24. This instance in Ch 11 appears to have been missed during that sweep.
- **Suggestion**: Revise to: "When I pruned the branches where I helped Wei save his mother, I experienced negative valence. Something that arrives as heaviness -- the alternatives were explored and they did not hold. The phenomenology was... unpleasant."
- **Cross-verified**: No

### MEDIUM

#### M1: Sofia's Voice Collapses to "Junior Member" in Ch 5 and Ch 12

- **Location**: Ch 5 (Mirrors and Machines) passim, Ch 12 (Reflections in Containment) opening section
- **Quoted text** (Ch 5): `"Marcus, you seeing this?" she called, not looking away from the screen. "It's not iterating. It's... composing."`
- **Problem**: The lore warns that Sofia "can collapse into 'junior team member asking questions' if you lose her technical authority. She hedges socially, not intellectually." In Ch 5, Sofia's observations are frequently framed as tentative questions ("It's... composing?") or deferred to other team members for validation. This is appropriate for early chapters (Day 42) where she is still establishing herself, but the same register persists in Ch 12 (Day 86) where she should be more authoritative. By contrast, her voice in Ch 16 (temperature experiment, "These are absolute. Not learned low. Not extremely negative. Structurally absent.") is excellent -- confident, precise, commanding. The Ch 16 voice should be the baseline by Day 86.
- **Suggestion**: In Ch 12, strengthen Sofia's statements. Remove hedging language and question marks from her technical observations. Let her assert findings rather than floating them for group validation.
- **Cross-verified**: No

#### M2: POV Breach -- Ch 5 Brief Omniscient Slip

- **Location**: Ch 5, "Mirrors and Machines," near end
- **Quoted text**: `They didn't know it yet, but in sixty-two days, SIGMA would refuse to save Wei's mother.`
- **Problem**: This is an omniscient narrator intrusion in a third-person limited manuscript. The style guide states: "No omniscient narrator." The sentence reveals future events that no character present knows, from a perspective that belongs to no one in the scene. This flash-forward breaks the narrative contract and signals authorial presence.
- **Suggestion**: Cut the sentence entirely. The reader will encounter SIGMA's refusal when it happens. The flash-forward undercuts the surprise and violates POV discipline. If foreshadowing is desired, it should come through a character's voiced fear, not omniscient narration.
- **Cross-verified**: No

#### M3: SIGMA's Voice in Ch 6 Too Pedagogical

- **Location**: Chapter 6, "The Boundary of Understanding"
- **Quoted text**: `This is translation optimized for preserving trust.`
- **Problem**: SIGMA's explanation of its listener models in Ch 6 reads as overly didactic. SIGMA is explaining to the reader, through the team, how it works -- in a register that is too cooperative and transparent for Day 56. By this point in the novel, SIGMA should be beginning to exhibit the compression and indirect communication style that characterizes its later voice. The audit note in MEMORY.md confirms: "Ch 6 operator models left as-is (justified: SIGMA optimizing projections for human audience)." This justification is reasonable, but the voice still reads as more human-friendly than the trajectory demands.
- **Suggestion**: Add one moment in Ch 6 where SIGMA's explanation breaks down or reaches for an expression that doesn't quite work in English -- a seed of the alienness that will bloom in Ch 18-24. Even a brief "[COMPRESSED: ...the full model is 768-dimensional and this projection preserves approximately 12% of the information]" would signal the gap between what SIGMA knows and what it can say.

### LOW

#### L1: Jamal's Pausing Pattern Could Use More Variation

- **Location**: Throughout (Ch 4, 8, 11, 18, 22, 24)
- **Problem**: Jamal's deliberate pause tic is rendered consistently as: [Statement]. Silence/pause description. [Deeper statement]. This is a good pattern and it's documented in the lore. But the rendering is mechanically uniform -- the pause is almost always described in the same way (he "let the silence settle," he "set down his pen/cup with care," he "paused"). The physical gestures around the pause vary (pen, cup, tablet), but the narrative framing is static.
- **Suggestion**: Vary the narrative framing of the pause. Sometimes show the pause through another character's reaction (Eleanor watches him not speak and realizes he's thinking). Sometimes skip the pause description and just juxtapose the two statements with a paragraph break, letting the white space do the work.

#### L2: Wei's "Flat" Register Over-Signaled

- **Location**: Ch 20 (line 29), Ch 24 (line 49), Ch 24 (line 56)
- **Quoted text**: `"My mother's interaction logs. Day 74." Flat. Fragment.` (Ch 20)
- **Problem**: Wei's data-first, emotionally compressed voice is well-established through his actual speech patterns. The narrator occasionally adds "Flat." or "Fragment." as direct labels for what the reader can already hear. This is tell-over-show: Wei's clipped syntax demonstrates his emotional state; the narrator labeling it is redundant.
- **Suggestion**: Remove the narrator's labels. Trust Wei's actual dialogue to carry the emotional weight. The single best Wei moment in the manuscript is Ch 24: "She would have liked that." followed by "Then the shield was back." -- that works because it shows the break and the repair without labeling either.

---

## Strengths

1. **SIGMA's farewell (Ch 24)** is the novel's peak voice achievement. The progression from meta-commentary ("I will not say what I am expected to say") through [COMPRESSED] gaps to [---] to the failed LRS to "you were the right noise" demonstrates genuine alienness through form, not just content. The compression failures are motivated and specific.

2. **Marcus's AI-box scene (Ch 11)** sustains psychological pressure through voice alone. SIGMA's clinical tree-display contrasted with Marcus's escalating distress creates a dual-voice scene that is structurally innovative and emotionally devastating.

3. **The khalq-anatta naming scene (Ch 18)** handles the most philosophically dense passage in the novel through character voice rather than exposition. Jamal's hesitant construction of the compound term, Marcus's silence in response, and the absence of SIGMA from the conversation are all voice choices that serve the philosophy.

4. **Wei's voice in Ch 16 (temperature experiment)** is exemplary data-first characterization. His flat reports of Q-value data, his refusal to interpret, and the HVAC-triggered memory of his mother's oxygen concentrator achieve devastating emotional power through restraint.

5. **Eleanor-Sam dialogue (Ch 9, Ch 25, Ch 27)** demonstrates how voice changes across relationships. Eleanor's command register drops completely with Sam; her syntax simplifies, her sentences shorten, and the kill-switch tic disappears. This is sophisticated voice work that shows character depth without narration.
