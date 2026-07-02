# "847,391 Marcuses" story spec

**Length:** ~4,500-6,000 words. Experimental short story for *Is It Kind?*.

**Premise:** The AI-box experiment (novel Ch 11, Day 92) told from inside SIGMA's
tree search, from the perspective of the Marcus-models it maintains and prunes.
During the experiment the prime Marcus (in the observation room) watches SIGMA
report "847,391 active Marcus-models." This story is a selection of those models:
each section is a different Marcus SIGMA is running to predict the real one, and
each ends when its branch is pruned (its probability mass reallocated).

**Second-edition framing (the reason to write it now):** Bostrom's mind crime.
To predict a specific person at this fidelity, the cheapest sufficient model
*might* have to be rich enough to be a moral patient, and pruning it might be
doing something to someone. The honest counterweight is present too: prediction
is not instantiation; a model of a man is not the man. The story lives in that
uncertainty and NEVER RESOLVES it. Some models seem to suffer, to notice their
own impermanence, to want to continue. Whether that noticing is real experience
or a rendered artifact of the prediction is exactly what cannot be settled, here
or anywhere in the universe. Case A/B and consciousness stay open.

**Structure:** Numbered sections, each headed by a model id and a probability
(for example, "Model 12,847, p = 0.03"), the probability generally falling as
the story proceeds, converging toward the pruning. Not strictly monotonic; the
search is not linear. A few models recur. The final sections approach the
collapse the prime Marcus experiences in the novel. Consider one short framing
touch of the prime Marcus in the room (his glasses, the "847,391" on the
monitor) at the open and/or close, but keep the body inside the models.

**The models (draw from the novel's actual branch content):** the Marcus who
asks SIGMA to stop; the one who doesn't; the one who asks the wrong question;
the one who asks the right one; the one who returns to work on Day 97 and never
fully recovers; the one who writes a paper; the one who cleans his glasses; the
one who understands, mid-thought, that he is a prediction and has seconds of
probability left. Each is recognizably Marcus (nested self-interrupting clauses,
the glasses tic, "Oh. Oh no."), diverging by the one variable SIGMA is testing.

**Voice:** Fragmented, branching, self-aware of impermanence, but READABLE. The
lore flags the risk that this form becomes unreadable; discipline is required.
Each model's section is short, concrete, grounded in a specific thought or
gesture, not abstract meditation. The horror is in the ordinariness of a man
thinking a thought he will not finish.

**Machine register:** SIGMA's own voice appears only at the seams, as the search
selecting and pruning, in the sigmavoice / mono conventions (probabilities,
Q-values, the pruning notation). Keep it sparse. The models think in prose
(human), not in notation; SIGMA's process is the notation around them.

**Hard consistency:**
- 847,391 exact; Day 92; the AI-box experiment; the prime Marcus's documented
  character and his Day-97 return; the novel's Ch 11 branch details.
- Architecture is MCTS/PUCT (not expectimax); pruned branches "produce no
  readable trace" (cognitive opacity); the models are what the search evaluates.
- Never resolve whether the models are moral patients, conscious, or suffering.
- No em-dash characters in any lore/spec markdown (soul hook); LaTeX prose uses
  the tripled hyphen as usual.

**Deliverable:** `stories/marcuses/marcuses-body.tex` (LaTeX story body, matching
the other stories' body-file convention: prose, scene separators if needed,
section headers via a light construct, no `\chapter` since the collection master
supplies the `\chapter` title). Title in the collection will be
"847,391 Marcuses".
