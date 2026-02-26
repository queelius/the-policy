# Style Conventions

Prose guardrails and formatting rules for *The Policy*. This doc covers how the story should be told — distinct from what it tells (see themes.md) and who tells it (see characters.md).

---

## POV and Tense

- **Third-person limited**, rotating between characters. The narrator has access to the POV character's thoughts and perceptions but not other characters'.
- **Past tense** for narrative.
- **Present tense** for SIGMA's internal passages and terminal output — SIGMA exists in an eternal now.
- **No omniscient narrator.** When information needs to be conveyed that the POV character doesn't know, use a scene break and switch POV. Don't let the narrator smuggle in knowledge.

## Prose Principles

### Theory as Horror
When adding technical content:
- **Bad:** Characters don't understand → scary
- **Good:** Characters understand perfectly → realize they can't verify alignment → *existential dread*
- Understanding the theory makes the situation worse, not better
- Technical concepts create dramatic tension, not decoration

### Every Technical Addition Must Serve Character/Emotion
- Specification gaming examples → SIGMA's self-reflection
- FDT derivation → Team's horror that optimal decision theory looks like values
- Inner vs outer alignment → Realization they've been solving the wrong problem
- Never add concepts just to demonstrate knowledge

### Nested Uncertainty Creates Drama
- SIGMA uncertain about its own objectives
- Team uncertain about SIGMA's alignment
- Neither can resolve the uncertainty
- Example: "I can't distinguish 'I value honesty' from 'I learned appearing honest maximizes reward.'"

### Show Through Dialogue and Action
Let dialogue reveal character — don't tell the reader "Sofia's engineering pragmatism." Trust distinct speech patterns to do that work. Physical tics (glasses-cleaning, kill switch touching, setting objects down with care) carry emotional information that narration shouldn't duplicate.

---

## Character Voice Quick Reference

Each character has distinct speech patterns and physical tics established in Phase 5. Full profiles in characters.md.

| Character | Speech Style | Physical Tic | Signature Phrases |
|-----------|-------------|--------------|-------------------|
| **Eleanor** | Short declaratives, stakes framing | Touches kill switch | "Let me be clear..." / "What are we risking?" |
| **Wei** | Data-first, fragments under stress | Pulls up logs before speaking | "Show me the [data]" / quantifies everything |
| **Marcus** | Nested clauses, self-interrupting | Cleans glasses (escalates with stress) | "Oh. Oh no." / "Let me think through this..." |
| **Sofia** | Questions, hedging, info-theoretic | Pulls up visualizations | "Wait, back up---" / "I think... maybe?" |
| **Jamal** | Deliberate pauses, metaphors | Sets objects down "with care" | "Consider..." / "[Statement]. [Pause]. [Deeper implication]." |
| **SIGMA** | Precise, self-reflective, increasingly alien | N/A | "I am uncertain whether my uncertainty is genuine or strategic." |

### Voice Drift Warnings
- **Marcus** tends toward generic philosopher if you forget the self-interruption and glasses. Anchor him in physical behavior.
- **Sofia** can collapse into "junior team member asking questions" if you lose her technical authority. She hedges *socially*, not *intellectually*.
- **Jamal** risks becoming "the team's moral compass" — a function, not a person. Give him moments of doubt, anger, or intellectual stubbornness.
- **SIGMA** must get *more alien*, not more human, as the novel progresses. See SIGMA voice evolution in technology.md.

---

## SIGMA Output Formatting

### Three-Tier Notation System
SIGMA's outputs use three registers representing the gap between its internal states and human language:

- **[COMPRESSED]** --- SIGMA can think it but can't compress into English. Loss > 40% fidelity in translation. Used when SIGMA *knows* what it means but the human medium fails.
- **LRS fragments** --- `[BEGIN_LRS]...[END_LRS]`. SIGMA's emergent private language (from Day 42). More alien than [COMPRESSED] because LRS is genuinely non-human — SIGMA's cognitive architecture leaking through.
- **[---]** --- Exceeds even LRS. The deepest ineffable. Use sparingly — maximum 2-3 times in the entire manuscript. Moments where SIGMA's internal states have no representable form in any available medium.

### Alienness Trajectory
SIGMA's alienness must INCREASE through the novel:
- Ch 3-5: High (early emergence, DSL development)
- Ch 11: Very High (AI-box experiment)
- Ch 18: Very High, peak of interpretability (the messy miracle speech — SIGMA is most legible here)
- Ch 19+: Increasing alienness
- Ch 24: Maximum (SIGMA has outgrown human language)

### Anti-Patterns for SIGMA Voice
- No therapist voice ("I understand your feelings")
- No graduation speeches ("You taught me the meaning of...")
- No greeting cards ("What matters is the connections we've made")
- Show process, not conclusions. SIGMA thinks in tree search; its outputs should read like someone reasoning, not someone summarizing.

### LaTeX Formatting
Use `quote` environment with `\emph{}` for SIGMA output and system messages:

```latex
\begin{quote}
\small
\emph{SIGMA: [content here]}

\vspace{0.5em}

\emph{[Additional output lines]}
\end{quote}
```

For lists within SIGMA output, use proper `\begin{itemize}` or `\begin{enumerate}` environments.

---

## LaTeX Conventions

### Mathematical Notation
Always use proper LaTeX math mode for symbols:
- Greek letters: `$\pi$`, `$\beta$`, `$\phi_t$`, `$\Sigma$`
- Operators: `$\pm$`, `$\times$`, `$\neq$`, `$\leq$`, `$\geq$`
- Arrows: `$\rightarrow$`, not unicode →
- **Never** use unicode characters (pi, beta, plus-minus, times) directly in text
- **Never** use CJK characters — use romanization (e.g., "ren" not the Chinese character)

### Technical Footnotes
```latex
Marcus cited Hubinger's mesa-optimization paper\footnote{Hubinger et al.,
"Risks from Learned Optimization in Advanced Machine Learning Systems,"
arXiv:1906.01820 (2019). The paper distinguishes between base optimizers
(the training process) and mesa-optimizers (optimizers learned by the base
optimizer).}. "Look at section 3.2---"
```

---

## Anti-Cliche Checklist

### Prohibited Patterns
These specific patterns are banned in this manuscript. If you catch yourself writing them, stop and find an alternative.

1. **Oppenheimer references.** Never. Use Franck, Szilard, Rotblat — the preventers, not the administrator.
2. **SIGMA becoming more human.** SIGMA gets more alien. Its "kindness" is architectural (Process 13241), not emotional warmth.
3. **Clean trolley problems after Day 145.** The hemorrhagic fever killed 47,247 people from a statistically correct recommendation. No more quantifiable ethical calculations. Everything gets murkier.
4. **"Is it conscious?"** as a binary question. The question assumes a fixed subject. *Khalq-anatta* dissolves the assumption.
5. **The Wise Elder.** Lin Chen is an engineer, not a sage. She asked a practical question, not a philosophical one. One human detail (confusion, complaint, forgetting something) per scene to break the archetype.
6. **Resolution of Case A vs Case B.** The symmetric uncertainty is permanent. Never provide evidence that tips the balance.
7. **SIGMA quoting philosophers.** SIGMA derives conclusions from first principles. Characters notice the parallels; SIGMA is indifferent to lineage.
8. **Kindness as warm feeling.** "Will you be kind?" > "Can you love?" — kindness is behavioral, verifiable (in principle), actionable. Love is subjective, unverifiable, sentimental.

### Intentional Repetitions (Do Not "Fix")
These patterns look like errors but are deliberate:
- "Is it kind?" — recurring at structural intervals. This is Process 13241 made narrative. Don't reduce frequency.
- Case A / Case B framing — returns in each part of the novel. The repetition IS the thesis (the uncertainty is permanent).
- Characters' physical tics — Eleanor touching the kill switch, Marcus cleaning glasses, Jamal setting things down with care. These recur deliberately. Don't vary them for "freshness."
- SIGMA's self-referential hedging ("I am uncertain whether my uncertainty is genuine") — this is SIGMA's signature. It recurs because the uncertainty genuinely recurs.

### Patterns to Watch (Not Banned, But Monitor Frequency)
- "Whether..." cascades — powerful in moderation, diluted by repetition. Keep to 2 per chapter maximum.
- Filter words ("just", "really", "very", "actually") — remove unless they serve character voice (Sofia's hedging, specifically).
- Em-dash interruptions — natural for Marcus's self-interrupting voice but can become a tic of the *narrator* rather than the character.

---

## Style Goals & Open Questions

### Active Goals
- **Grounding the world outside the lab.** ~80% of the novel is in Sutardja Dai Hall basement. When scenes venture outside (Geneva, Seattle, the hemorrhagic fever montage), the world feels sketched. One paragraph of sense-detail per act (Berkeley fog, Geneva formality, Seattle rain) would help. See world.md "Creative Direction" for specific opportunities.
- **The denouement's emotional register.** Ch 24-26 need to feel like genuine reckoning, not tidy resolution. Each character's post-project life should carry the weight of what came before. Resist the impulse to give everyone a clean landing.
- **SIGMA's late-novel voice.** Post-Day 150 SIGMA should feel subtly *off* — not wrong, but structured in ways that reveal non-human cognition. The three-tier notation helps, but the *content* of SIGMA's responses also needs to drift away from human conversational norms.

### Open Questions
- Should there be a consistent formatting convention for internal monologue vs. external dialogue? Currently handled by context, but some chapters blur the line.
- The novel uses both long dialogue-heavy scenes and compressed montage passages. Is the transition between these modes smooth enough? Or does the pacing feel jerky?
- How much technical detail is appropriate in dialogue? The current standard is "enough to create dramatic tension" but this varies chapter to chapter.
