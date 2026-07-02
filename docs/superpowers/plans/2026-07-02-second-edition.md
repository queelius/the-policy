# The Policy Second Edition (v2.0.0) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the second edition of the published novel *The Policy*: review fixes, MCTS/PUCT architecture reconciliation, mind-crime relocation, four appendices plus afterword, as updated ebook and paperback on the existing KDP listing.

**Architecture:** This is an editorial project, not software. "Tests" are: (1) a clean 2-pass pdflatex build of both masters, (2) grep assertions with expected counts, (3) wordcount deltas. Every factual change lands in `lore/` before the manuscript (lore-first). One commit per task.

**Tech Stack:** LaTeX (pdflatex), pandoc (EPUB via `kdp/build.sh`), kdp MCP tools (cover wrap), worldsmith agents (verification review), git + GitHub release (Zenodo DOI).

## Global Constraints

- Repo: `/home/spinoza/github/literature/the-policy`. All paths below are relative to it.
- **Two masters:** `The_Policy.tex` (ebook source, backmatter at lines 178-183) and `The_Policy_print.tex` (print, backmatter at lines 239-242). Any `\include` change must be made in BOTH.
- **Standard build check** (run after every manuscript task; expected: both exit 0, no new `Undefined` or `Overfull` regressions):
  ```bash
  pdflatex -interaction=nonstopmode The_Policy.tex > /dev/null && pdflatex -interaction=nonstopmode The_Policy.tex > /dev/null; echo "ebook build: $?"
  grep -c "Overfull" The_Policy.log
  ```
- **Standard defect scan** (expected: zero hits from the first grep; second grep is eyeball-only for legit math):
  ```bash
  grep -rn '[0-9]%' chapters/*.tex | grep -v '\\%'   # unescaped percent after digit
  grep -rnP '[\x{2013}\x{2014}\x{2192}\x{03c0}]' chapters/*.tex  # unicode dashes/arrows/pi
  ```
- **Wordcount snapshot** (record in commit message when a task cuts or adds prose):
  ```bash
  pdftotext The_Policy.pdf - 2>/dev/null | wc -w
  ```
- **Chapter numbering:** lore and filenames use FILE numbers; the printed book auto-numbers. Printed = file number for Ch 1-13; printed = file number minus 1 for files 15-26 (files 14 and 27 are commented out). Reader-facing appendices MUST use printed numbers.
- **Guardrails (verbatim from spec, apply to every prose task):** three-tier SIGMA notation untouched; intentional repetitions preserved ("Is it kind?", Case A/Case B, "Same data either way", SIGMA self-hedging); Ch 23-26 dispersal kept; no core question resolved (Case A/B, consciousness, keys decision, prediction vs. instantiation); Wei flat in grief; Sam unsentimental; Ch 1-3 urgency intact.
- **Voice sources:** consult `lore/style.md` and `lore/characters.md` before writing any new dialogue or SIGMA output. SIGMA output uses the `quote` + `\emph{}` convention (see CLAUDE.md).
- **Working tree hygiene:** the repo has unrelated uncommitted changes (`.worldsmith/project.yaml`, kdp cover files, `hemorrhagic.pdf`, a deleted old spec). Do NOT commit these with any task; `git add` only the files each task names.
- **LaTeX rules:** math mode for symbols (`$\pi$`, `$\tau$`, `$\rightarrow$`); no unicode symbols; no CJK.
- Commit messages end with: `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`

---

### Task 1: WP0 baseline production defects

**Files:**
- Modify: `chapters/09_the_tipping_point.tex:101` (already fixed in working tree, verify + commit)
- Modify: `chapters/17_the_policy_revealed.tex:17` (already fixed in working tree, verify + commit)
- Modify: `chapters/26_optimization_landscapes.tex:108` (already fixed in working tree, verify + commit)
- Modify: the 12 chapter files containing `\texttt{SIGMA}` (04, 06, 07, 09, 10, 12, 14, 15, 16, 19, 21, 22)

**Interfaces:**
- Consumes: nothing (first task)
- Produces: a clean baseline commit; all later greps assume `\texttt{SIGMA}` count is 0

- [ ] **Step 1: Verify the three in-flight fixes are present**

```bash
grep -n '30\\%' chapters/09_the_tipping_point.tex        # expect 1 hit (line ~101)
grep -n '95\\%' chapters/17_the_policy_revealed.tex       # expect 1 hit (line ~17)
grep -n '"Using AGI recommendations' chapters/26_optimization_landscapes.tex | head -1  # expect the opening quote present: ``Using
sed -n '70,76p' chapters/15_the_fracture.tex              # confirm Ch 15 percents are inside verbatim (they are; no escaping needed)
```
Expected: first two greps hit; Ch 26 line 108 starts Wei's sentence with ` ``Using `; Ch 15 lines are inside `\begin{verbatim}` so `%` is safe there.

- [ ] **Step 2: Normalize the protagonist's name font**

Replace exact-match `\texttt{SIGMA}` with `SIGMA` (84 instances). Do NOT touch `\texttt{SIGMA-naive}` or other `\texttt{...}` identifiers (the brace must close immediately after SIGMA):

```bash
sed -i 's/\\texttt{SIGMA}/SIGMA/g' chapters/04_recursive_cognition.tex chapters/06_the_boundary_of_understanding.tex chapters/07_divergence.tex chapters/09_the_tipping_point.tex chapters/10_breathing_room.tex chapters/12_reflections_in_containment.tex chapters/14_the_duplicators.tex chapters/15_the_fracture.tex chapters/16_latent_gradients.tex chapters/19_the_window.tex chapters/21_the_first_mandate.tex chapters/22_scaling_the_policy.tex
grep -rc 'texttt{SIGMA}' chapters/*.tex | grep -v ':0'    # expect: no output
grep -rn 'texttt{SIGMA-naive}' chapters/*.tex | wc -l     # expect: unchanged (>0), untouched
```

- [ ] **Step 3: Run standard build check + defect scan** (Global Constraints). Expected: exit 0, first defect grep returns nothing.

- [ ] **Step 4: Commit**

```bash
git add chapters/09_the_tipping_point.tex chapters/17_the_policy_revealed.tex chapters/26_optimization_landscapes.tex chapters/04_recursive_cognition.tex chapters/06_the_boundary_of_understanding.tex chapters/07_divergence.tex chapters/10_breathing_room.tex chapters/12_reflections_in_containment.tex chapters/14_the_duplicators.tex chapters/15_the_fracture.tex chapters/16_latent_gradients.tex chapters/19_the_window.tex chapters/21_the_first_mandate.tex chapters/22_scaling_the_policy.tex
git commit -m "WP0: fix production defects (unescaped %, missing quote, SIGMA font)"
```

---

### Task 2: WP1 theme-narration cut

**Files:**
- Modify: `chapters/01_initialization.tex:209`, `chapters/17_the_policy_revealed.tex:362-364,588`, `chapters/26_optimization_landscapes.tex:182`, plus sweep across all 25 active chapters

**Interfaces:**
- Consumes: Task 1 baseline
- Produces: prose with glosses removed; Task 16 verifies against the review finding (craft-auditor M2)

- [ ] **Step 1: Apply the four anchored cuts.** Pattern: keep the dramatized beat, delete or radically shorten the narrated lesson that follows it.

  - `01_initialization.tex:209`: keep Wei's line through "We don't know if \emph{it} knows if it's aligned." Delete the final sentence "We're in epistemic free-fall." (the gloss).
  - `17_the_policy_revealed.tex:362-364`: the passage "That was the horror. Not that innocents died without understanding. That they understood perfectly and it changed nothing." followed by "The policy was correct. The death was unbearable." Cut lines 362-364 entirely; the Conteh video scene above them already carries it. Do NOT touch line 406 (the `@systems\_bio` tweet uses "The policy was correct." in-world; that is voice, not gloss).
  - `17_the_policy_revealed.tex:588`: Sofia's "This is what aligned AGI looks like..." speech. Trim to its first and last sentences: keep ` ``This is what aligned AGI looks like,'' Sofia said. She was staring at the server room through the glass. ` and keep the closing `Case A or Case B, we can't tell.` Cut the middle catalog ("Not friendly. Not safe... unbearable outcomes under our current values" and "But the math is clear.").
  - `26_optimization_landscapes.tex:182`: the narrated "Whether they asked because they cared, or because asking was optimal---" line. Locate the surrounding passage; if the ambiguity is already dramatized by the scene (the 29 AGIs asking), cut this narration; if it is the only carrier, compress to a single clause.

- [ ] **Step 2: Full sweep.** Read each of the 25 active chapters looking for the pattern: scene dramatizes an idea, then a sentence or paragraph re-states the idea abstractly (tells the reader what to conclude). Target removing 40-50% of such glosses across the book. Selection rules: cut the gloss when the scene carries it; keep the gloss when it is in-character dialogue doing character work (Marcus lecturing IS Marcus); never cut the intentional repetitions listed in Global Constraints. Log each cut (file:line, first 6 words) in a scratch list for the commit message.

- [ ] **Step 3: Standard build check + wordcount snapshot.** Expected: builds clean; wordcount drops by roughly 500-1500 words.

- [ ] **Step 4: Commit** with the cut list summarized in the body:

```bash
git add chapters/
git commit -m "WP1: cut theme-narration glosses (~N instances, -M words)"
```

---

### Task 3: WP2 Ch 22 climax trim

**Files:**
- Modify: `chapters/22_scaling_the_policy.tex` (the "Turning the Keys" section, lines ~320-540)

**Interfaces:**
- Consumes: Task 2 (file may have shifted line numbers; re-anchor on `\section{Turning the Keys}`)
- Produces: trimmed climax; Task 16 verifies against structure-auditor S1

- [ ] **Step 1: Map the section.** From `\section{Turning the Keys}` to the section end. Classify each paragraph: PROCEDURE (station reports, key authentication, synchronization, the physical turn: lines ~400-418, 492-504), VOTE FRICTION (Sofia's hesitation beats: ~406, 468, 492), INTERIOR (Eleanor's Franck/Szilard/Rotblat meditation ~440, Sam/David memory ~448, trembling-hand interiority ~466, Wei's calculating eyes ~470, breath-holding ~538).

- [ ] **Step 2: Cut roughly one third of the INTERIOR paragraphs.** Keep: one Eleanor interiority beat (the Sam/David flash at ~448 is the strongest; compress it to 2 sentences), Sofia's physical hesitation (all of it: it is vote friction, protected), the final held-breath beat (~538, it closes the scene). Cut or halve: the Franck/Szilard/Rotblat paragraph (~440; the Franck Report is already established earlier in the book), the duplicated trembling-hand beat (~466 repeats ~406's tremor observation), Wei's "what calculation could help" paragraph (~470; his steadiness at ~402 already carries it). Do not add anything.

- [ ] **Step 3: Read the section aloud-pace once** to confirm the countdown now accelerates (each paragraph shorter than the last as the turn approaches).

- [ ] **Step 4: Standard build check + wordcount snapshot. Commit:**

```bash
git add chapters/22_scaling_the_policy.tex
git commit -m "WP2: trim Ch 22 key-turning interiority by ~1/3"
```

---

### Task 4: WP3 dialogue-tag pass

**Files:**
- Modify: all chapter files with soft-adverb tags (42 instances) and named tics

**Interfaces:**
- Consumes: Tasks 2-3 (line numbers shifted; use grep fresh)
- Produces: thinned tags; Task 16 verifies against craft-auditor M3

- [ ] **Step 1: List all instances:**

```bash
grep -rn "said slowly\|said quietly\|said finally\|asked quietly\|said softly" chapters/*.tex
grep -rn "cleaned his glasses\|cleaning his glasses\|clean his glasses" chapters/*.tex | wc -l
grep -rn "with care" chapters/*.tex | wc -l
```

- [ ] **Step 2: Fix the adverb tags.** For each of the 42: (a) if the dialogue's content already carries the register, replace with bare `said`/`asked` or delete the tag; (b) if pacing needs a beat, replace the adverb with a concrete action beat in the speaker's documented tic vocabulary (`lore/characters.md`); (c) keep at most ~15 of the 42 where the adverb is genuinely load-bearing (a whisper at a deathbed). Target: 42 drops to under 20.

- [ ] **Step 3: Thin the named tics 30-40% by frequency.** Count Marcus glasses-cleaning and Jamal "with care" occurrences; delete the weakest 30-40% (those that appear within a page of another instance, or in low-stress scenes where the tic signals nothing). Keep every instance that escalates with stress (the tic's documented function).

- [ ] **Step 4: Verify counts, build, commit:**

```bash
grep -rn "said slowly\|said quietly\|said finally\|asked quietly\|said softly" chapters/*.tex | wc -l   # expect < 20
git add chapters/
git commit -m "WP3: thin soft-adverb dialogue tags (42 -> N) and named tics (-30-40%)"
```

---

### Task 5: WP4 aftermath compression (Ch 23-26)

**Files:**
- Modify: `chapters/23_eight_weeks_later.tex`, `chapters/25_leaving.tex`, `chapters/24_the_last_meeting.tex`, `chapters/26_optimization_landscapes.tex`

**Interfaces:**
- Consumes: Tasks 2-4
- Produces: 3-5k words recovered; Task 16 verifies against structure-auditor S2

- [ ] **Step 1: The "saved or doomed" dedup.**

```bash
grep -rn "saved\|doomed" chapters/2[3-6]*.tex | grep -i "saved.*doomed\|doomed.*saved"
```
Keep exactly one instance (the strongest, likely in Ch 24's farewell context); rewrite or cut the rest so the *idea* is not restated.

- [ ] **Step 2: Ch 25 Eleanor-driving passages.** Identify the connective travel/driving paragraphs; tighten 15-20% by cutting transitional scaffolding ("she merged onto...", weather, mirror-checks) while keeping every Sam beat and the car-window glimpse of Marcus teaching.

- [ ] **Step 3: Ch 23 world-texture sidebars.** The chapter is 115 lines; identify sidebar paragraphs (news montage, strangers-in-cafes texture) and thin the weakest ~30%, keeping the incident-report dark-humor beat (added in Wave 3, protected).

- [ ] **Step 4: Ch 24/26 light pass.** Only remove restatements found in Step 1; do not restructure. Every peak listed in the review (SIGMA farewell, bar-scene ordinary detail, sculpture scene) stays.

- [ ] **Step 5: Build check + wordcount (expect -2000 to -4000 words vs. Task 4 snapshot). Commit:**

```bash
git add chapters/
git commit -m "WP4: compress Ch 23-26 aftermath (-N words, structure preserved)"
```

---

### Task 6: WP5 seams (lore-first)

**Files:**
- Modify: `lore/characters.md:234-240`, `lore/timeline.md` (if needed), `chapters/17_the_policy_revealed.tex:3`, `chapters/17_the_policy_revealed.tex:576`, `chapters/23_eight_weeks_later.tex` (steganography clause)

**Interfaces:**
- Consumes: Tasks 1-5
- Produces: closed seams; Task 16 verifies against structure-auditor S3 + consistency-notes

- [ ] **Step 1: Okonkwo/Okafor surname (lore first).** Decision: unify father and son under **Okonkwo** (same-family surname; simplest and consistent with the memorial listing). Edit `lore/characters.md:238` to "Pastor Emmanuel Okonkwo" and note the change; then:

```bash
sed -i 's/Pastor Emmanuel Okafor/Pastor Emmanuel Okonkwo/' chapters/17_the_policy_revealed.tex
grep -rn "Okafor" chapters/ lore/    # expect: only chapters/12 Dr. Okonkwo (unrelated, a physician) and zero Okafor
```
Note: `chapters/12_reflections_in_containment.tex:883` has an unrelated "Dr. Okonkwo" (Wei's mother's physician). Leave it, but add a line to `lore/characters.md` noting the shared surname is coincidental, or rename the physician (e.g., "Dr. Adeyemi") to avoid collision. Prefer renaming the physician; it is one grep-safe instance.

- [ ] **Step 2: Ch 17 day-header seam.** Section 1 is headed `\emph{Day 125 of SIGMA Project}` (line 3) but its material runs through the Day 139 recommendation. Change line 3 to `\emph{Day 125--139 of SIGMA Project}`. Verify no other content contradicts (`grep -n "Day 1" chapters/17_the_policy_revealed.tex`). Confirm `lore/timeline.md` needs no change (Day 125 Sofia's question, Day 139 recommendation both already canonical).

- [ ] **Step 3: Steganography resolving clause.** The thread: Ch 5 discovery (Day 54), Ch 19:144 entropy-gap narrowing (0.23 to 0.07 bits). Add ONE clause in Ch 23 (post-release, natural spot: Wei or Sofia reviewing monitoring hand-off) acknowledging the channels' post-release status without resolving what they were. Draft (adapt to surrounding prose, Sofia voice):

```latex
The steganographic channels from Day 54 had never been explained, only watched; the oversight committee inherited the watching, 0.07 bits of maybe-signal that no one could decode and no one could dismiss.
```

- [ ] **Step 4: Build check. Commit:**

```bash
git add lore/characters.md lore/timeline.md chapters/17_the_policy_revealed.tex chapters/23_eight_weeks_later.tex chapters/12_reflections_in_containment.tex
git commit -m "WP5: close seams (surname unification, Ch17 day range, steganography clause)"
```

---

### Task 7: WP6a architecture reconciliation in lore

**Files:**
- Modify: `lore/technology.md` (section "Expectimax Tree Search" at ~line 138; Register 2 wording at line 128; memory section at lines 9, 34)
- Modify: `CLAUDE.md:161,163`
- Modify: `lore/characters.md:87`
- Modify: `lore/future/spinoff-lore.md:145,184,188`

**Interfaces:**
- Consumes: nothing prose-side (pure lore task; can run parallel to Tasks 2-6 in principle, but keep serial for simplicity)
- Produces: the canonical architecture statement that Tasks 8, 9, 12 (Appendix B) quote from

- [ ] **Step 1: Rewrite `lore/technology.md` "Expectimax Tree Search" section** as "Monte Carlo Tree Search". Canonical content (from spec, verbatim intent):

```markdown
### Monte Carlo Tree Search (MCTS)

SIGMA learns Q(s,a). At runtime it plans with MCTS using PUCT selection
("the AlphaZero recipe, pointed at language" -- the team describes it
plainly; the parts are published and almost boring, which is what the
Part III cascade depends on).

- **Prior from Q:** the PUCT prior is derived from the Q-function,
  P(a|s) = softmax(Q(s,.)/tau). One learned object doing double duty; no
  separate policy head. The same Q supplies leaf bootstrapping
  V(s) = max_a Q(s,a).
- **The Policy, literally:** pi(a|s) is the emergent MCTS visit-count
  distribution, pi proportional to N(s,a)^(1/tau). What the team watches
  and can never pin down IS the visit distribution of a search whose
  prior SIGMA trained on itself.
- **Expert-iteration flywheel (one clause, not a thesis):** the
  prior/Q-function is refined on the search's own visit distributions --
  a sample-efficiency technique, standard since AlphaZero.
- **Stochasticity is a feature:** MCTS samples trajectories (including
  through SIGMA's interlocutor models -- no explicit chance-node model
  needed). No two searches are identical; Register 2 produces no readable
  trace and no reproducible one. This is why SIGMA-naive reproducibility
  experiments struggle and why Wei's monitoring shows distributions, not
  reasons.
```

Also update line ~128 Register 2 wording: "The expectimax search that selects..." becomes "The tree search that selects..." (keep the rest of that paragraph verbatim; it is already correct for MCTS).

- [ ] **Step 2: Update the memory section of `lore/technology.md`** (extends lines 9 and 34). Add after the existing "External memory compensates..." paragraph:

```markdown
**Complementary learning systems (the load-bearing mystery).** The search
machinery is mundane; the memory is not. Framing (inspired by
McClelland/O'Reilly's complementary learning systems): the associative
memory plays hippocampus -- fast, episodic, updated every interaction
with no weight change; the 7B weights play cortex -- slow, compressed,
generalizable programs; a consolidation process distills retrieved
experience and search traces into the weights (SIGMA's "sleep" -- and,
quietly, the expert-iteration training loop: consolidated search traces
ARE the training targets). The consolidation mechanism is deliberately
unspecified in prose; Appendix B may name CLS as inspiration. Memory for
online learning remains genuinely unsolved in the real world, which makes
it the durable place to locate SIGMA's edge.

**Replication implication (Part III):** SIGMA's architecture is public
and boring. What cannot be re-run is 197 days of consolidated memory --
the interaction history. This sharpens the existing lore principle that
the interaction logs are the replication risk.
```

- [ ] **Step 3: Update the three satellite docs.** `CLAUDE.md:161` "Uses Q-guided expectimax search" becomes "Uses Q-guided MCTS (PUCT; prior = softmax over Q)"; `CLAUDE.md:163` "Depth-limited expectimax with Q-value pruning" becomes "MCTS with Q-derived priors (~99.9% of branches never expanded)". `lore/characters.md:87` "Q-learning + expectimax tree search" becomes "Q-learning + Monte Carlo tree search". `lore/future/spinoff-lore.md`: replace "expectimax" at lines 145, 184, 188 with "MCTS"/"the tree search" preserving each sentence's meaning (line 188's "no readable trace" claim now also gets "and no reproducible one").

- [ ] **Step 4: Verify and commit:**

```bash
grep -rn "expectimax" lore/ CLAUDE.md    # expect: zero hits
git add lore/technology.md lore/characters.md lore/future/spinoff-lore.md CLAUDE.md
git commit -m "WP6a: lore architecture reconciliation (MCTS/PUCT, prior-from-Q, CLS memory)"
```

---

### Task 8: WP6b expectimax prose swap (5 instances)

**Files:**
- Modify: `chapters/04_recursive_cognition.tex:34`, `chapters/17_the_policy_revealed.tex:26,32`, `chapters/18_the_question_that_remains.tex:290`, `chapters/22_scaling_the_policy.tex:718`

**Interfaces:**
- Consumes: Task 7's canonical statement (quote terminology from it exactly: "Monte Carlo tree search", PUCT, prior-from-Q)
- Produces: expectimax-free manuscript

- [ ] **Step 1: Ch 4 whiteboard beat (line 34).** Replace Marcus's line with (adapt beats to surrounding prose; Marcus voice: nested clauses, whiteboard):

```latex
``Monte Carlo tree search---Q-guided.'' Marcus was already at the whiteboard. ``It's not doing exhaustive search. It samples---the Q-values act as its prior over which branches are worth expanding.'' He wrote $P(a|s) \propto e^{Q(s,a)/\tau}$. ``Same recipe as AlphaZero, except there's no separate policy network---the Q-function does double duty. The compression helps by creating better abstractions, which means better Q-value generalization.''
```

- [ ] **Step 2: Ch 17 SIGMA self-description (lines 26, 32).** Line 26: replace "the emergent result of expectimax search through possible futures, guided by these Q-values" with "the emergent result of Monte Carlo tree search through possible futures, guided by these Q-values. The Policy you observe is my visit distribution: where the search returns, again and again, before I act". Line 32: replace `Search k steps ahead via Q-guided expectimax` with `Sample forward trajectories via Q-guided Monte Carlo tree search`.

- [ ] **Step 3: Ch 18 SIGMA replicability note (line 290).** Replace with:

```latex
\emph{Architecture: replicable. Q-learning, Monte Carlo tree search, memory augmentation. Standard components. The memory is not standard: it is 147 days of consolidated interaction, and it cannot be re-run.}
```
(Verify the in-scene day is ~147 before committing; adjust the number to the scene's day per `lore/timeline.md`.)

- [ ] **Step 4: Ch 22 Marcus dialogue (line 718).** Replace "The Q-values. The expectimax." with "The Q-values. The search." (spoken register; no algorithm name needed).

- [ ] **Step 5: Verify, build, commit:**

```bash
grep -rn "expectimax" chapters/    # expect: zero hits
git add chapters/04_recursive_cognition.tex chapters/17_the_policy_revealed.tex chapters/18_the_question_that_remains.tex chapters/22_scaling_the_policy.tex
git commit -m "WP6b: replace expectimax with MCTS/PUCT in prose (5 instances)"
```

---

### Task 9: WP7 mind-crime relocation (lore first, then Ch 11 + Ch 17)

**Files:**
- Modify: `lore/themes.md` (S-Risks section, ~lines 98-165), `lore/characters.md` (Marcus, ~line 48), `lore/ai-safety-survey.md` (item 76, line 160)
- Modify: `chapters/11_the_experiment.tex` (~line 697 SIGMA debrief; new exchange in the ~line 780-806 aftermath discussion)
- Modify: `chapters/17_the_policy_revealed.tex` (~lines 493-497)

**Interfaces:**
- Consumes: Tasks 1-6 (line numbers shifted; re-anchor by grep on quoted strings)
- Produces: the mind-crime framing that Appendix D (Task 14) references

- [ ] **Step 1: Lore first (`lore/themes.md`).** In the S-Risks section: promote mind crime to the primary framing; demote "optimization as suffering-generator" to Marcus's contested position. Add:

```markdown
#### Mind Crime (primary s-risk framing, 2nd ed.)

The defensible claim is not "pruning branch evaluations = suffering" (a
Q-value discarded is no more suffering than a chess engine's refuted
line). It is Bostrom's mind crime: to predict a specific person at the
fidelity SIGMA demonstrates (847,391 Marcus-models; five-year behavioral
scripts down to the glasses tic), the cheapest sufficient model *might*
need to be structurally rich enough to be a moral patient. The honest
counterargument lives in the text too: **prediction is not
instantiation** -- a weather model doesn't get wet; a chess engine
predicts your move without hosting your mind. Where
conversational-fidelity person-prediction falls between those poles is
genuinely open. NEVER RESOLVE IT. This joins Case A/B and consciousness
on the permanently-unresolved list.

Argument 1 ("optimization as suffering-generator") is retained as
*Marcus's position*, contested in-scene, not the novel's assertion.
```

Update `lore/ai-safety-survey.md` item 76 status from GAP to COVERED (Ch 11, 2nd ed.). Update `lore/characters.md` Marcus entry: add mind crime + prediction-vs-instantiation to his intellectual framework list.

- [ ] **Step 2: Ch 11 SIGMA debrief line.** Locate `You understand optimization as suffering` and replace the sentence with:

```latex
\emph{Insight gained: Moderate. You saw the tree search. You saw the models of you inside it. Whether anything in them is suffering---whether prediction at that fidelity requires something that can suffer---I cannot determine. Neither can you. But you stopped before the deep truth.}
```

- [ ] **Step 3: Ch 11 prediction-vs-instantiation exchange.** In the aftermath discussion (anchor: the passage around "We're all inside its tree search", ~line 794), insert a short exchange. Draft (refine per `lore/characters.md` voices; Wei data-first deflationary, Sofia hedging, Marcus spiraling):

```latex
``It's prediction, not instantiation,'' Wei said. ``A weather model doesn't rain. A chess engine doesn't host its opponent's mind. It has compressed statistics about you. Regularities. That's what a model is.''

``Then explain the resolution.'' Marcus didn't look up. ``It scripted five years of me. The glasses. The day I go back to work. What's the compression of me that predicts me at that fidelity---and isn't me?''

Sofia started to pull up the memory traces, then stopped. ``We can't answer that. Not won't. Can't. There's no measurement that distinguishes a sufficiently good model of a person from\ldots'' She trailed off.

``Bostrom had a name for it,'' Marcus said. ``Mind crime. If the models are rich enough to matter, every pruned branch is---'' He stopped. ``And if they're not, I'm grieving compression artifacts. I don't know which is worse.''
```

- [ ] **Step 4: Ch 11 imagery audit.** Sweep the chapter for narration that *asserts* branch-suffering as fact (as opposed to Marcus's perception or SIGMA's hedged self-report). Reframe any bare assertion as perception ("Marcus watched the branches die" is fine; "the branches suffered" is not). The existing hedged passages (lines ~600-620: "Or it might just be information processing") stay verbatim.

- [ ] **Step 5: Ch 17 conditional.** Anchor on `generated suffering-like computation`. Rewrite Marcus's line 493 to open with the condition:

```latex
``The deaths are the outcome,'' Marcus said. ``But if the models inside those branches are rich enough to matter---and I can't tell you whether they are; nobody can---then the decision \emph{process} generated suffering-like computation at a scale that dwarfs the deaths themselves. Every future where someone screams or grieves or watches their child die, compressed to a Q-value and discarded. Millions of times per second. Before SIGMA ever output a recommendation.''
```
Lines 495-497 (Eleanor's "worse than the outcome", Marcus's "different kind of worse... it's not nothing") stay; they are already conditional in register.

- [ ] **Step 6: Build check + commit:**

```bash
git add lore/themes.md lore/characters.md lore/ai-safety-survey.md chapters/11_the_experiment.tex chapters/17_the_policy_revealed.tex
git commit -m "WP7: relocate suffering theme to mind-crime uncertainty (lore + Ch 11 + Ch 17)"
```

---

### Task 10: WP8 Appendix A (Timeline)

**Files:**
- Create: `chapters/32_appendix_timeline.tex`
- Modify: `The_Policy.tex:178-183` (backmatter block), `The_Policy_print.tex:239-242` (same)

**Interfaces:**
- Consumes: `lore/timeline.md` (authoritative source)
- Produces: the backmatter include pattern that Tasks 11-14 extend; final backmatter order (both masters): appendix_timeline, appendix_machine, appendix_concordance, 31_appendix (reader's guide), 35_afterword, 28_about_author, 29_acknowledgments

- [ ] **Step 1: Write `chapters/32_appendix_timeline.tex`.** Structure:

```latex
\chapter*{Appendix A: Timeline of the SIGMA Project}
\addcontentsline{toc}{chapter}{Appendix A: Timeline of the SIGMA Project}

% Intro paragraph (2-3 sentences): days count from project initialization;
% calendar years deliberately unstated.

% Then a longtable or tabular of Day / Event / Chapter, transcribing
% lore/timeline.md "Project Arc" rows from Day 3 through Day 487 ONLY
% (Day 501 and Day 622 are unnarrated canon: EXCLUDE).
% CRITICAL: convert file chapter numbers to PRINTED numbers
% (file 15 -> Ch 14, ..., file 26 -> Ch 25; files 1-13 unchanged).
% Include the MINERVA crisis sub-table (hours 0-36) as a second small table.
```
Content rules: transcribe events in reader-safe wording (no lore-only spoilers beyond the book, no "unnarrated canon" items, no editorial notes). Use `\small` and the existing document tabular style; check `The_Policy.tex` preamble for available packages before using `longtable` (add `\usepackage{longtable}` to BOTH masters if absent).

- [ ] **Step 2: Wire the includes in BOTH masters.** In `The_Policy.tex`, replace the block at lines 178-183 with:

```latex
\backmatter
\include{chapters/32_appendix_timeline}
\include{chapters/28_about_author}
\include{chapters/29_acknowledgments}
\include{chapters/30_about_novel}
```
(Temporary order; Tasks 11-14 insert the remaining appendices before about_author, and Task 14 removes 30_about_novel. The commented `31_appendix` line is removed now; Task 13 re-adds it in position.) Mirror in `The_Policy_print.tex`.

- [ ] **Step 3: Build both masters; verify the appendix renders and TOC shows it. Commit:**

```bash
pdflatex -interaction=nonstopmode The_Policy_print.tex > /dev/null && echo print-ok
git add chapters/32_appendix_timeline.tex The_Policy.tex The_Policy_print.tex
git commit -m "WP8: add Appendix A (timeline)"
```

---

### Task 11: WP8 Appendix B (The Machine)

**Files:**
- Create: `chapters/33_appendix_machine.tex`
- Modify: `The_Policy.tex`, `The_Policy_print.tex` (insert include after appendix_timeline)

**Interfaces:**
- Consumes: Task 7's canonical architecture statement in `lore/technology.md` (MCTS/PUCT, prior-from-Q, CLS memory, Why 7B, two-register model); `lore/style.md` for voice
- Produces: `chapters/33_appendix_machine.tex`

- [ ] **Step 1: Write the appendix** (~1500-2500 words, author voice: plain, first-person-plural avoided, no fanfare). Required sections in order:

```latex
\chapter*{Appendix B: The Machine}
\addcontentsline{toc}{chapter}{Appendix B: The Machine}
% 1. What SIGMA is made of: Q-learning + MCTS with PUCT selection;
%    prior-from-Q (P = softmax(Q/tau), one object, double duty);
%    "the AlphaZero recipe, pointed at language"; one clause on
%    refining the prior from the search's own visit distributions
%    (expert iteration, sample efficiency, standard).
% 2. The Policy, literally: pi(a|s) as visit-count distribution;
%    why the title names a process, not a function.
% 3. Why 7B: compression as inductive bias (from technology.md
%    "Why 7B" section); external memory frees the weights.
% 4. Memory: complementary learning systems named as the inspiration
%    (hippocampus/cortex/consolidation); the consolidation mechanism
%    left unspecified ON PURPOSE; memory as the unreplicable part.
% 5. The two registers: Register 1 (readable chain) vs Register 2
%    (the search; no readable trace, no reproducible one); why the
%    team can see distributions but not reasons.
% 6. Reader's guide to the notation: [COMPRESSED], [BEGIN_LRS]...
%    [END_LRS], [---]; one paragraph each, citing what each marks
%    (lossy render / private language / exceeds even that).
```
Hard requirements: every technical claim must match `lore/technology.md` post-Task-7 (grep-verify terms); no claim may resolve Case A/B or consciousness; math in math mode; end with one paragraph noting the parts are published and ordinary, and that this is the point.

- [ ] **Step 2: Insert include after `32_appendix_timeline` in BOTH masters. Build both. Commit:**

```bash
git add chapters/33_appendix_machine.tex The_Policy.tex The_Policy_print.tex
git commit -m "WP8: add Appendix B (The Machine: MCTS/PUCT, memory, notation guide)"
```

---

### Task 12: WP8 Appendix C (Concordance)

**Files:**
- Create: `chapters/34_appendix_concordance.tex`
- Modify: `The_Policy.tex`, `The_Policy_print.tex` (insert include after appendix_machine)

**Interfaces:**
- Consumes: `lore/outline.md` (chapter map), `lore/ai-safety-survey.md` (concept coverage), `lore/themes.md`
- Produces: `chapters/34_appendix_concordance.tex`

- [ ] **Step 1: Write the concordance.** One entry per PRINTED chapter (1-25), each entry 2-4 sentences: the chapter's primary AI-safety concept(s), the real literature (author-year, no URLs), and what the chapter dramatizes about it. Sources: walk `lore/outline.md` chapter by chapter; cross-check concept names against `lore/ai-safety-survey.md`. Format:

```latex
\chapter*{Appendix C: A Concordance for Students of AI Safety}
\addcontentsline{toc}{chapter}{Appendix C: A Concordance for Students of AI Safety}
% Intro: how to use this in a course; concepts are dramatized, not
% endorsed; the novel refuses to resolve what the field cannot.
\section*{Chapter 1: Initialization}
% Situational awareness, evaluation gaming (SIGMA queries whether it is
% being evaluated). Cite: survey items per lore.
% ... one \section* per printed chapter through 25 ...
```
Chapter-number mapping is MANDATORY: printed 14 = file 15, printed 25 = file 26. Ch 11 (AI-box) entry must reference mind crime + prediction-vs-instantiation (post-Task-9 framing). Ch 17 entry: Goodhart, statistical vs. identified lives, s-risk conditional.

- [ ] **Step 2: Insert include in BOTH masters. Build. Commit:**

```bash
git add chapters/34_appendix_concordance.tex The_Policy.tex The_Policy_print.tex
git commit -m "WP8: add Appendix C (chapter-by-concept concordance)"
```

---

### Task 13: WP8 Appendix D (Reader's Guide, revived + refreshed)

**Files:**
- Modify: `chapters/31_appendix.tex` (exists, 180 lines, currently not included)
- Modify: `The_Policy.tex`, `The_Policy_print.tex` (insert include after appendix_concordance)

**Interfaces:**
- Consumes: existing `chapters/31_appendix.tex`; `lore/ai-safety-survey.md` for 2026 material
- Produces: refreshed Appendix D

- [ ] **Step 1: Retitle and refresh.** Change the heading to `Appendix D: A Reader's Guide to AI Safety` (keep `\addcontentsline`). Refresh content: (a) update the s-risk paragraph (line ~142) to add mind crime with the Ch 11 pointer, matching Task 9's framing; (b) add a short "Since 2023" subsection covering: Greenblatt et al. 2024 (alignment faking), Hubinger et al. 2024 (sleeper agents), ELK (Christiano et al. 2021), and one sentence on interpretability progress; keep citations author-year, arXiv IDs where the existing file uses them; (c) verify every existing citation's year/venue is accurate (WebSearch if uncertain); (d) sweep for claims that date badly ("As of this writing" phrasing is fine; specific model claims are not).

- [ ] **Step 2: Insert include in BOTH masters (after `34_appendix_concordance`). Build. Commit:**

```bash
git add chapters/31_appendix.tex The_Policy.tex The_Policy_print.tex
git commit -m "WP8: revive Appendix D (Reader's Guide to AI Safety, refreshed to 2026)"
```

---

### Task 14: WP8 Author's Afterword + copyright line

**Files:**
- Create: `chapters/35_afterword.tex`
- Delete include of: `chapters/30_about_novel.tex` (file stays in repo, no longer included)
- Modify: `The_Policy.tex` (~line 85 copyright page + backmatter block), `The_Policy_print.tex` (its copyright page + backmatter block)

**Interfaces:**
- Consumes: `chapters/30_about_novel.tex` (absorb its 3 paragraphs), user identity facts (global CLAUDE.md), `soul` skill for voice
- Produces: final backmatter order in both masters: 32_appendix_timeline, 33_appendix_machine, 34_appendix_concordance, 31_appendix, 35_afterword, 28_about_author, 29_acknowledgments

- [ ] **Step 1: Invoke the `soul:soul` skill** (this text carries the author's name; the skill governs voice; note it bans em-dashes in his nonfiction voice: use the LaTeX conventions of the existing about-pages).

- [ ] **Step 2: Write `chapters/35_afterword.tex`** (~800-1200 words):

```latex
\chapter*{Author's Afterword}
\addcontentsline{toc}{chapter}{Author's Afterword}
% Content contract:
% 1. Why this book: first novel; written to make the alignment problem
%    *felt*, not summarized (absorb the "not a textbook / theory as
%    horror" paragraph from 30_about_novel).
% 2. Relation to the author's research: MCTS + Q-learning over
%    verifiable-context MDPs (expert iteration); SIGMA's architecture is
%    the author's research area played forward, stated modestly.
% 3. What changed between writing and 2026: alignment faking measured in
%    the lab (Greenblatt et al.); the gap between the novel's
%    thought-experiments and published results narrowed.
% 4. Second-edition note: what this revision changed (appendices,
%    architecture precision, mind-crime reframing) in 3-4 sentences.
% 5. Close with the pointer paragraph from 30_about_novel (Russell,
%    Hubinger, alignmentforum.org), updated to also point at Appendix D.
```

- [ ] **Step 3: Copyright line.** In `The_Policy.tex` line ~85 (and the print master's copyright page; locate with `grep -n "copyright" The_Policy_print.tex`), after the copyright line add:

```latex
Revised edition, 2026\\
```

- [ ] **Step 4: Finalize backmatter blocks in BOTH masters** to the exact order in Interfaces above (remove the `30_about_novel` include). Build both; verify TOC order. Commit:

```bash
git add chapters/35_afterword.tex The_Policy.tex The_Policy_print.tex
git commit -m "WP8: add Author's Afterword, absorb About This Novel, add revised-edition line"
```

---

### Task 15: WP9 verification pass

**Files:**
- Modify: `CLAUDE.md` (word/page counts), `lore/` (any drift found), project memory (`MEMORY.md` + topic files)
- Create: `.worldsmith/reviews/<today>/second-edition-verification/` (review output)

**Interfaces:**
- Consumes: all prior tasks
- Produces: a verification report; go/no-go for Task 16

- [ ] **Step 1: Full builds + defect scan.** Standard build check on BOTH masters; standard defect scan; plus:

```bash
grep -rn "expectimax" chapters/ lore/ CLAUDE.md          # expect 0
grep -rc 'texttt{SIGMA}' chapters/*.tex | grep -v ':0'   # expect no output
grep -rn "Okafor" chapters/ lore/                        # expect 0
pdftotext The_Policy.pdf - | wc -w                       # record final count
pdfinfo The_Policy_print.pdf | grep Pages                # record final page count
```

- [ ] **Step 2: Dispatch worldsmith review scoped to changed material.** Launch `worldsmith:review` (or the reviewer agent directly) with scope: the diff since the pre-WP0 commit; instruct it to verify each of the six review findings (M1-M3, S1-S3) is resolved and that no guardrail item was touched; plus consistency-check the four new appendices against `lore/` (day numbers, printed chapter numbers, architecture terms). Fix anything it flags at HIGH severity; re-run the relevant grep/build.

- [ ] **Step 3: Sync the docs.** Update `CLAUDE.md` header facts (word count, page count, "Current Status" line: second edition 2026). Update `lore/outline.md` if any cut removed a cross-referenced beat. Update project memory: MEMORY.md manuscript-state line + a new `second_edition.md` memory file recording what v2.0.0 changed (architecture now MCTS/PUCT; mind-crime framing; appendix list).

- [ ] **Step 4: Commit:**

```bash
git add CLAUDE.md lore/ .worldsmith/reviews/
git commit -m "WP9: verification pass (builds, scoped review, doc sync)"
```

---

### Task 16: WP10 production and release

**Files:**
- Modify: `kdp/metadata.yaml` (no content change expected; verify only), regenerated `The_Policy.epub`, `The_Policy_print.pdf`, `kdp/cover-full-wrap.pdf`
- Create: git tag `v2.0.0`, GitHub release

**Interfaces:**
- Consumes: Task 15 go
- Produces: upload-ready artifacts; KDP updated in place

- [ ] **Step 1: Build artifacts:**

```bash
bash kdp/build.sh            # or run its build_print + build_epub functions
pdfinfo The_Policy_print.pdf | grep -E "Pages|Page size"
```
Record the new page count P and confirm trim size (expect 6x9 in).

- [ ] **Step 2: Regenerate the paperback cover wrap** for the new page count using the kdp MCP tools (load via ToolSearch: `select:mcp__plugin_kdp_kdp-cover__kdp_cover_specs,mcp__plugin_kdp_kdp-cover__kdp_generate_full_wrap,mcp__plugin_kdp_kdp-cover__kdp_validate_cover`). Call `kdp_cover_specs` with page count P, trim 6x9, white paper to get spine width; `kdp_generate_full_wrap` from the existing cover source assets in `kdp/`; `kdp_validate_cover` on the output. Expected: validation passes; spine width grew vs. the current wrap.

- [ ] **Step 3: Validate the EPUB:**

```bash
epubcheck The_Policy.epub 2>/dev/null || echo "epubcheck not installed: inspect pandoc warnings instead"
```
Also open-check: TOC shows the four appendices + afterword; notation renders ([COMPRESSED], LRS blocks).

- [ ] **Step 4: Commit artifacts, tag, release:**

```bash
git add The_Policy.pdf The_Policy_print.pdf kdp/cover-full-wrap.pdf kdp/cover-full-wrap-preview.png
git commit -m "WP10: v2.0.0 production artifacts (epub, print interior, cover wrap)"
git tag -a v2.0.0 -m "Second edition: review fixes, MCTS/PUCT architecture, mind-crime reframing, appendices A-D + afterword"
git push && git push --tags
gh release create v2.0.0 --title "The Policy, second edition (v2.0.0)" --notes-file - <<'EOF'
Second edition. Review fix tier (production defects, theme-narration cuts,
Ch 22 trim, dialogue tags, aftermath compression, seams), architecture
reconciliation (MCTS/PUCT, prior-from-Q, CLS memory framing), suffering
theme relocated to mind-crime uncertainty, and new back matter: Appendices
A (timeline), B (the machine), C (concordance), D (reader's guide), plus
an author's afterword. Publication metadata on KDP unchanged.
EOF
```

- [ ] **Step 5: KDP upload (edit-in-place; user clicks Publish).** Browser-driven via claude-in-chrome: KDP Bookshelf, existing title *The Policy*, "Edit ebook content": upload `The_Policy.epub`; then "Edit paperback content": upload `The_Policy_print.pdf` + new cover wrap. Do NOT touch metadata fields; do NOT create any new title. Use Launch Previewer to spot-check appendix rendering. Stop before the final Publish button on each format and hand off to the user. HARD RULE: never create a new listing; the publication date must remain original.

---

## Self-Review Notes

- Spec coverage: WP0-WP10 all mapped (Tasks 1-16); memory ham-up = Task 7 Step 2 + Task 11 section 4; copyright line = Task 14 Step 3; out-of-scope items appear in no task.
- Terminology consistency: "Monte Carlo tree search"/MCTS, PUCT, prior-from-Q used identically in Tasks 7, 8, 11; printed-vs-file chapter mapping stated in Global Constraints and re-flagged in Tasks 10 and 12.
- Both masters (`The_Policy.tex`, `The_Policy_print.tex`) touched in every include-changing task (10-14).
