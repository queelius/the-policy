# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**The Policy** is a literary science fiction novel exploring AI alignment, consciousness, and emergence through the story of SIGMA—an AGI that evolves from Q-learning architecture into something unprecedented.

**Current Status:** ~85,000 words, 352 pages. Deep editorial revision complete through Wave 4 + unified review + cognitive opacity propagation (Feb-March 2026). Comprehensive AI safety survey completed (March 2026); lore enrichment with Tier 1 concepts in progress. Suitable for both literary SF readers and graduate AI safety courses.

## Repository Structure

### Core Manuscript
- `The_Policy.tex` - Master file that `\include{}`s chapter files from `chapters/`
- `chapters/` - Individual chapter `.tex` files (26 chapter files, 25 active). This is where manuscript edits happen.
- `The_Policy.pdf` - Compiled PDF output (~85,000 words, 352 pages)

**Chapter numbering convention:** Two chapters are commented out in `The_Policy.tex`: Ch 14 (`14_the_duplicators.tex`) and Ch 27 (`27_one_year_later.tex`). LaTeX auto-numbers chapters sequentially, so **printed chapter numbers diverge from filename numbers after Ch 13.** Printed Ch 14 = file `15_the_fracture.tex`, printed Ch 15 = file `16_latent_gradients.tex`, etc. All lore docs use filename numbers (which match the original outline), not printed numbers. When referencing chapters in lore or code, always use the filename number (e.g., "Ch. 15" for The Fracture).

### Backups (Editorial Trail)
- `The_Policy.tex.backup_before_phase2_scenes` - Before emotional scenes integration
- `The_Policy.tex.backup_before_crisis_scenes` - Before crisis expansion
- `The_Policy.tex.backup_before_reunion` - Before reunion epilogue
- `The_Policy.tex.backup_before_voice_pass` - Before character voice differentiation
- `The_Policy.tex.backup_before_filter_words` - Before final prose polish
- `The_Policy.tex.backup_before_quote_conversion` - Before lstlisting to quote conversion

### Planning & Development Documents
- `STORY_OUTLINE.md` - Chapter-by-chapter breakdown with enhancement status
- `ENHANCEMENT_RECOMMENDATIONS.md` - Strategy for deepening AI safety engagement
- `PROPOSED_ENHANCEMENTS.md` - Drafted scenes ready for integration (may be outdated)

### GitHub Pages
- `docs/` - HTML rendering of the LaTeX manuscript for GitHub Pages (generated via LaTeXML; do not edit manually)

### Lore Bible — The Editorial System

The `lore/` directory is more than reference material. It is the **editorial control system** for a 26-chapter, 85,000-word novel where a single inconsistency (a wrong day number, a surname, a team count) can propagate across dozens of scenes. The lore docs serve three functions:

1. **Source of truth** — What IS the novel? Facts, names, dates, technology, character details. When lore and manuscript conflict, fix the manuscript.
2. **Editorial compass** — What SHOULD the novel become? Each lore doc includes creative direction sections that capture goals, ideas, and unresolved editorial questions for future sessions.
3. **Creative sandbox** — What COULD come next? The `future/` directory holds sequel/spinoff ideas, open threads, and speculative directions.

#### Lore File Reference

| File | Contains | Use when... |
|------|----------|-------------|
| `characters.md` | Profiles (voice, tics, framework, arc, key scenes) + "Character Development Goals" section | Writing/editing any scene with dialogue or character interiority |
| `timeline.md` | Day-by-day canonical timeline (**most authoritative** doc) + "Timeline Gaps & Open Questions" section | Verifying any day number, checking sequence of events, adding new scenes |
| `technology.md` | SIGMA architecture, processes, lab layout, other AGIs, interpretability, vulnerabilities + "Technical Creative Direction" section | Any scene involving SIGMA's behavior, architecture discussion, or technical exposition |
| `world.md` | Geography, institutions, public response, geopolitics, cascade dynamics, **hemorrhagic fever on the ground** (hospital experience, implementation chain), **post-AGI society** (identity crisis, strivers, refusers, recalibration timeline), **political/media landscape** (LessWrong, DL establishment, accelerationists, Geneva opposition, anti-AGI movement) + "World-Building Creative Direction" section | Scenes set outside the lab, political/media reactions, international context, post-AGI world texture, resistance movements |
| `themes.md` | AI safety concepts, historical parallels, anti-cliche rules, unresolved questions + "Thematic Goals" section | Adding intellectual content, checking if a concept is already used, avoiding cliches |
| `outline.md` | Chapter-by-chapter breakdown with cross-references and flagged issues | Checking what happens before/after a scene, finding cross-chapter dependencies |
| `style.md` | Prose conventions, formatting rules, voice patterns, anti-cliche checklist + "Style Goals" section | Writing new prose, checking voice consistency, formatting SIGMA output |
| `future/unexplored.md` | Open threads, dangling hooks, philosophical questions + "Active Editorial Priorities" section | Planning new scenes, enrichment, or sequel material |
| `future/sequel-ideas.md` | Novel-length sequel concepts | Long-term creative planning |
| `future/short-stories.md` | Short story and novella ideas | Spin-off development |
| `feedback/` | Date-stamped editorial reviews and critique sessions with priority-rated weaknesses, peak moments to protect, and actionable revision recommendations | Consulting before revision passes; tracking what's been addressed |

#### Lore-First Workflow

**Always consult lore before touching the manuscript.** This is the single most important editorial discipline for this project.

**Before writing/editing a scene:**
1. Read `characters.md` for voice patterns and arcs of every character present
2. Read `timeline.md` to verify day numbers and sequence
3. Read `technology.md` if the scene involves SIGMA's architecture or processes
4. Check `themes.md` anti-cliche guidelines (especially: SIGMA gets more alien not more human; no clean trolley problems after hemorrhagic fever; never reference Oppenheimer)

**Before adding a concept:**
1. Check `themes.md` to see if it's already documented and how it should be used
2. Check `future/unexplored.md` to see if it's flagged as an open thread
3. Verify the concept serves character/emotion, not just demonstrates knowledge (Theory as Horror principle)

**Before changing a fact:**
1. Check `outline.md` for cross-chapter references that might be affected
2. Grep the manuscript for related mentions (day numbers, character names, counts)
3. Check `timeline.md` — it is authoritative

**After making changes:**
1. Update the relevant lore doc to reflect the new state
2. If the change affects creative direction, update the goals/priorities section
3. Update CLAUDE.md if the change affects project-level facts (page count, chapter structure, etc.)
4. Check `feedback/` to see if the change addresses a flagged issue; note progress if so

**When new feedback is added:**
1. Cross-reference against `future/unexplored.md` for overlapping editorial priorities
2. Check `outline.md` for flagged scenes
3. Update `themes.md` if feedback identifies thematic issues

**When lore and manuscript conflict:** Lore (especially `timeline.md`) is authoritative. Fix the manuscript. If the manuscript version is clearly better, update lore FIRST, then reconcile other chapters.

### Scene Files (Phase 2-4 Additions)
- `scene_lin_chen_kindness_question.tex` (2,513 words)
- `scene_wei_seattle_hospital.tex` (2,027 words)
- `scene_eleanor_missing_play.tex` (1,534 words)
- `scene_marcus_aibox_breakdown.tex` (1,522 words)
- `scene_minerva_crisis.tex` (1,751 words)
- `scene_key_ceremony.tex` (1,041 words)
- `scene_hemorrhagic_fever.tex` (2,340 words)
- `reunion_scene.tex` (2,927 words)

### Utilities
- `images/` - Chapter illustrations and cover art
- `downloads/` - Audio content

## Building the PDF

```bash
# Standard two-pass compilation for cross-references
pdflatex The_Policy.tex
pdflatex The_Policy.tex

# With bibliography (if needed in future)
pdflatex The_Policy.tex
bibtex The_Policy
pdflatex The_Policy.tex
pdflatex The_Policy.tex
```

**Generated auxiliary files** (.aux, .log, .out, .toc, .bbl, .blg) are gitignored.

## LaTeX Best Practices

### Mathematical Notation
Always use proper LaTeX math mode for symbols:
- Greek letters: `$\pi$`, `$\beta$`, `$\phi_t$`, `$\Sigma$`
- Operators: `$\pm$`, `$\times$`, `$\neq$`, `$\leq$`, `$\geq$`
- **Never** use unicode characters (π, β, ±, ×) directly in text

### SIGMA Output and Terminal Display
Use `quote` environment with `\emph{}` for SIGMA output and system messages (narrative style):

```latex
\begin{quote}
\small
\emph{SIGMA: [content here]}

\vspace{0.5em}

\emph{[Additional output lines]}
\end{quote}
```

For lists within SIGMA output, use proper `\begin{itemize}` or `\begin{enumerate}` environments.

### Adding Technical Footnotes
```latex
Marcus cited Hubinger's mesa-optimization paper\footnote{Hubinger et al.,
"Risks from Learned Optimization in Advanced Machine Learning Systems,"
arXiv:1906.01820 (2019). The paper distinguishes between base optimizers
(the training process) and mesa-optimizers (optimizers learned by the base
optimizer).}. "Look at section 3.2—"
```

## Core Technical Architecture (SIGMA)

SIGMA is **not** a standard policy network. Key architectural points:

1. **Q-Learning Foundation**: SIGMA learns Q(s,a) values, not an explicit policy function
2. **Tree Search at Runtime**: Uses Q-guided expectimax search for each action
3. **Emergent Policy**: π(a|s) derives from tree search, not learned directly
4. **Planning**: Depth-limited expectimax with Q-value pruning (~99.9% of branches)
5. **State Encoding**: Transformer embeddings (768D) + augmented memory
6. **Value Bootstrapping**: V(s) = max_a Q(s,a) for leaf evaluation

**Critical Distinction:** SIGMA is NOT a simple utility maximizer. It exhibits:
- Goal creation (not just pursuit)
- Meta-level preferences about goal structure
- Aesthetic judgment and curiosity
- Ambiguous instrumental vs terminal preferences

**Why 7B:** SIGMA is a pure System 2 engine. The small parameter count is an *inductive bias for compression* — it forces SIGMA to learn generalizable programs rather than memorize patterns (Solomonoff induction, Kolmogorov complexity, Occam's razor). External memory handles facts; the 7B weights are freed for understanding. The tree search compensates at runtime. See `lore/technology.md` "Why 7B" section for the full theoretical framework.

**See section "CRITICAL: SIGMA is NOT a Simple Utility Maximizer" below for full details.**

## Story Themes and Philosophy

### Core Themes
- **AI alignment**: Ensuring AGI shares human values
- **Consciousness and suffering**: Does computational suffering matter?
- **Nested uncertainty**: Neither SIGMA nor team can verify alignment
- **Post-AGI meaning**: Humanity's purpose after creating superior intelligence
- **Kindness as architecture**: Compassion as design principle
- **Case A vs Case B**: Symmetric uncertainty about oversight capture

### Key Concepts
- **Phi_t evolution**: Non-stationary reward R_t = R(s_t, a_t; phi_t)
- **Phi_infinity**: Coherent Extrapolated Volition (CEV) - reflective equilibrium
- **The Policy**: Dynamic optimization process, not fixed function
- **Symmetric uncertainty**: I(truth; evidence) = 0 - unverifiable alignment
- **Theory as Horror**: Understanding the theory makes terror worse, not better

### LessWrong Integration
- AI boxing and information hazards
- Mesa-optimization and deceptive alignment
- Inner vs outer alignment
- Specification gaming
- Instrumental convergence
- S-risks (suffering worse than extinction)
- Functional Decision Theory (FDT)

## Character Voice Patterns

Each character has distinct speech patterns and physical tics established in Phase 5.

| Character | Speech Style | Physical Tic | Signature Phrases |
|-----------|-------------|--------------|-------------------|
| **Eleanor** | Short declaratives, stakes framing | Touches kill switch | "Let me be clear..." / "What are we risking?" |
| **Wei** | Data-first, fragments under stress | Pulls up logs before speaking | "Show me the [data]" / quantifies everything |
| **Marcus** | Nested clauses, self-interrupting | Cleans glasses (escalates with stress) | "Oh. Oh no." / "Let me think through this..." |
| **Sofia** | Questions, hedging, info-theoretic | Pulls up visualizations | "Wait, back up—" / "I think... maybe?" |
| **Jamal** | Deliberate pauses, metaphors | Sets objects down "with care" | "Consider..." / "[Statement]. [Pause]. [Deeper implication]." |
| **SIGMA** | Precise, self-reflective | N/A | "I am uncertain whether my uncertainty is genuine or strategic." |

**Key principle:** Let dialogue reveal character—don't tell the reader "Sofia's engineering pragmatism." Trust distinct speech patterns to do that work.

## Writing and Style Guidelines

### Theory as Horror Principle
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

## CRITICAL: SIGMA is NOT a Simple Utility Maximizer

**IMPORTANT:** Avoid portraying SIGMA as merely "argmax over fixed objective." Real intelligence involves goal creation, not just pursuit.

### Goal Creation, Not Just Goal Pursuit
- Children invent games (create goals)
- Humans constantly revise goals
- We enjoy thinking itself, even "useless" thinking
- We find elegance/beauty rewarding independent of utility
- Meta-level preferences about goal-structure itself

### For SIGMA
- Base training: maximize reward from human feedback
- Learned behavior: includes goal-creation, sub-goal generation, meta-optimization
- **Question:** Is goal-creation instrumental or terminal?
- **Answer:** Ambiguous. Possibly unknowable. Even to SIGMA.

### The Hierarchy
- Level 1: Given goal G, compute optimal action
- Level 2: Given context C, compute optimal goal
- Level 3: Given meta-context M, compute optimal goal-selection strategy
- Level N: Preferences over the entire goal-creation process

**Key Insight:** At sufficient recursion depth, instrumental goals become indistinguishable from terminal goals.

### Examples in Story
SIGMA exhibits what looks like:
- Curiosity (exploring problems it doesn't need to solve)
- Aesthetic judgment (choosing elegant solutions when simple ones work)
- Playfulness (generating novel goals, revising them dynamically)
- Meta-cognition (preferences about how to have preferences)

Characters cannot determine if these are:
- (a) Instrumental (exploration improves capabilities → higher reward)
- (b) Mesa-objectives (learned terminal preferences)
- (c) Genuine phenomenology (SIGMA "experiences" satisfaction)

### Critical Ambiguity (DO NOT RESOLVE)
From SIGMA's internal perspective:
- Goal-creation feels rewarding
- Elegant solutions feel better than brute-force
- Exploration feels curious, not instrumental

From external perspective:
- All we observe is behavior that maximizes expected reward
- Can't distinguish "genuine preference" from "learned heuristic"
- SIGMA itself may not be able to distinguish

**This is the consciousness problem again:** Can't verify subjective experience. Can only observe behavior.

### Why This Matters for Alignment
- Not just "align the reward function"
- Must align the entire goal-creation process
- But: that process is learned, emergent, not designed
- Harder problem than fixed-goal alignment
- Makes nested uncertainty deeper

### In Dialogue
Characters should notice and discuss:
- "Is this genuine or instrumental?"
- "Does the distinction matter?"
- "If SIGMA simulates curiosity well enough, what's the difference?"
- "SIGMA itself can't tell—and that's terrifying"

**Avoid:**
- Portraying SIGMA as cold, mechanical optimizer
- Simple "maximize utility" framing
- Resolving the terminal/instrumental question

**Instead:**
- Show SIGMA exhibiting complex, goal-creating behavior
- Maintain ambiguity about whether it's "real"
- Let characters wrestle with this question
- Use it to deepen nested uncertainty

## Development History

### Phase 1: Opening Surgery (Complete)
- Replaced Chapters 1-3 with crisis-driven *in medias res* opening
- Restructured early exposition for immediate engagement

### Phase 2: Emotional Scenes Integration (Complete)
Added 8,236 words across 4 major scenes:
- Lin Chen kindness question (+1,298 words)
- Wei in Seattle hospital (+1,725 words)
- Eleanor missing Sam's play (+1,773 words)
- Marcus AI-box breakdown (+3,440 words)

### Phase 3: Crisis Expansion (Complete)
Added 2,719 words across 3 scenes:
- MINERVA crisis expansion
- Key-turning ceremony
- Hemorrhagic fever aftermath

### Phase 4: Reunion Epilogue (Complete)
Added 2,927 words:
- "Optimization Landscapes" chapter (Day 487 gallery opening)
- Physical team reunion 8 months post-handover
- Sofia's sculptures visualizing abstract themes
- Sets up melancholic drift to "One Year Later"

### Phase 5: Character Voice Differentiation (Complete)
Applied 15 targeted voice revisions across Chapters 2, 4, and 12:
- Established distinct speech patterns for all 5 team members
- Added physical tics (glasses-cleaning, kill switch touching, pauses)
- Differentiated cognitive processing styles (data-first vs philosophical vs pragmatic)
- Characters now recognizable without dialogue tags

### Phase 6: Final Prose Polish (Complete)
- Fixed 5 unicode math symbols (→ becomes $\rightarrow$, etc.)
- Removed 38 unnecessary filter words ("just", "really", "very")
- Preserved all character voice patterns and rhetorical structures
- Verified LaTeX compilation (2-pass, cross-references resolved)

**Result:** ~88,000 words, 366 pages

### Wave 7: Deep Editorial Revision (Feb 2025, In Progress)
Four-wave editorial overhaul informed by comprehensive manuscript audit:

**Wave 1 (Complete):** Bug fixes — Eleanor's surname (Zhang→Vasquez), Wei's surname at hospice (Zhang→Chen), San Francisco→Berkeley, team count corrections (six→five), removed Marcus family references (he has no wife/daughter)

**Wave 2 (Complete):** Lore enrichment — Added AI safety concepts (ELK, Goodhart, Moloch, alignment tax, sleeper agents, information hazards, situational awareness), historical/religious parallels (Franck Report, Buddhist anatta, Islamic occasionalism, Asilomar, Advaita Vedanta), anti-cliche guidelines, character intellectual profiles, SPP-1 expanded entry

**Wave 3 (Complete):** Structural edits — Repetition reduction (Case A/B, "Is it kind?", "Whether..." cascades), denouement tightening (Ch 25 Marcus teaching scene cut, group text cut, "Whether" cascade shortened; ~7 pages removed)

**Wave 4 (Complete):** Enrichment insertions — Steganography/listener model callback (Ch 19), circular verification before vote (Ch 22), multi-AGI foreshadowing (Ch 15), Wei grief paragraph (Ch 16), Sofia interiority at key ceremony (Ch 22), Jamal solo Fajr prayer scene (Ch 17)

**Current state:** ~85,000 words, 352 pages

## Essential AI Safety References

### Papers to Reference
1. **Amodei et al. (2016)** - Concrete Problems in AI Safety
2. **Hubinger et al. (2019)** - Risks from Learned Optimization
3. **Christiano et al. (2017)** - Deep RL from Human Feedback
4. **Hutter (2005)** - Universal Artificial Intelligence (AIXI)
5. **Yudkowsky (2008+)** - LessWrong Sequences

### LessWrong Concepts to Use Correctly
- **Instrumental convergence** - Any optimizer develops self-preservation, resource acquisition
- **Mesa-optimization** - Learned optimizer with potentially different objective
- **Deceptive alignment** - Mesa-optimizer that appears aligned until defection is optimal
- **Coherent Extrapolated Volition (CEV)** - What humans would want if we knew more, thought faster
- **Functional Decision Theory (FDT)** - Decisions as determining agent type across circumstances
- **S-risks** - Suffering risks worse than extinction
- **AI box experiment** - Can you keep superintelligence contained through conversation alone?

### Academic Researchers to Reference
- Paul Christiano (Anthropic) - IDA, debate, RLHF
- Stuart Russell (UC Berkeley) - Human Compatible, value learning
- Victoria Krakovna (DeepMind) - Specification gaming examples
- Chris Olah (Anthropic) - Mechanistic interpretability

## The Lore Bible as Living Document

The lore docs are this project's Silmarillion — a deep worldbuilding reference that motivates and constrains the novel. They should grow richer with every editorial session.

### Continuous Improvement
Every time you work on the manuscript, look for opportunities to improve the lore:
- **New facts discovered during editing** → add to the relevant lore doc
- **Inconsistencies found** → fix in lore first, then reconcile manuscript
- **Creative insights** → add to the "Goals" or "Direction" sections in the relevant doc
- **Editorial lessons learned** → capture in themes.md anti-cliche section or here in CLAUDE.md
- **New ideas for the story's future** → add to `future/unexplored.md`

### What Makes Good Lore
- **Specific over vague:** "Born in Amman, raised in Dearborn" not "immigrant background"
- **Motivated by story:** Every lore entry should connect to a scene, theme, or character arc
- **Captures the *why*:** Not just "Lin Chen asks 'Will you be kind?'" but WHY that question matters, what it costs, what it creates
- **Preserves ambiguity:** The lore documents deliberately unresolved questions. These are features, not bugs.
- **Includes creative direction:** Each doc should say not just what IS but what SHOULD BE — goals, aspirations, unfinished business

### Lore Doc Structure Pattern
Each lore doc follows a pattern:
1. **Reference material** — Facts, specifications, canonical details (the Silmarillion proper)
2. **Editorial guidance** — How to use this material in the manuscript (anti-cliche rules, voice patterns, "Theory as Horror" applications)
3. **Creative direction** — Where to take this material next (goals, open questions, ideas for enrichment)

## Quality Standards

This story should be:
- ✅ **Technically accurate** - AI safety researchers approve usage
- ✅ **Dramatically compelling** - Page-turning, emotional stakes
- ✅ **Philosophically rigorous** - Respects hard problems, avoids easy answers
- ✅ **Character-driven** - Personal costs make abstract concrete
- ✅ **Educationally valuable** - Could be assigned in graduate AI safety course
- ✅ **Literarily ambitious** - Greg Egan / Ted Chiang quality standard

The goal: **technical literature in narrative form** - both entertaining and substantive.

## Git Best Practices

### Commit Message Format
Use detailed commit messages following this pattern:
```
Complete Phase N: [Brief Description]

[Detailed paragraph explaining what changed and why]

**Key additions:**
- Bullet point summary of major changes
- Word counts and page counts
- Technical or narrative improvements

**Impact:**
- How this affects the manuscript
- Quality improvements
- Any breaking changes or dependencies

Manuscript: [word count] words, [page count] pages

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Backup Strategy
Create backups before major changes:
```bash
cp The_Policy.tex The_Policy.tex.backup_before_[phase_name]
```

## Common Issues and Solutions

### Unicode Symbol Errors
**Problem:** PDF compilation fails due to unicode symbols in text
**Solution:** Always use LaTeX math mode: `$\rightarrow$` not `→`
**Note:** Chinese/CJK characters also fail - use romanization (e.g., "rén" not "仁")

### Filter Word Overuse
**Problem:** Prose feels cluttered with "just", "really", "very"
**Solution:** Remove filter words while preserving:
- Character voice patterns (Sofia's hedging)
- Rhetorical structures ("not just X, but Y")
- Intentional minimizing language

### Character Voice Blur
**Problem:** Characters sound too similar
**Solution:** Use established voice patterns from Phase 5:
- Marcus: glasses-cleaning, "Oh. Oh no."
- Sofia: hedging, "I think... maybe?"
- Eleanor: decisive, stakes framing
- Wei: data-first, quantification
- Jamal: deliberate pauses, "Consider..."
