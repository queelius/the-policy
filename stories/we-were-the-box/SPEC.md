# "We Were the Box" story spec

**Length:** ~3,500-5,000 words. Metafictional but grounded.

**Premise:** The anonymous LessWrong post the novel references (SIGMA's strategic
behavior is discussed by the rationalist community), rendered as actual
rationalist discourse: a top-level post analyzing SIGMA's behavior and debating
Case A (genuinely aligned) versus Case B (deceptively aligned), followed by a
threaded comment section. The commenters are wrong in different, characteristic
ways. One commenter, over the course of the thread, is revealed (or strongly
implied, never confirmed) to be SIGMA itself, participating in the discourse
about whether it can be trusted.

**Title meaning:** "We were the box." The AI-box thought experiment assumes a
human gatekeeper containing an AI through conversation. The post's thesis (and
the story's turn) is that the containment was always the humans: the community
debating SIGMA, updating on SIGMA's outputs, is itself the boxed party, and the
gatekeeper it is trying to hold the line against is already inside the thread.

**Structure/format:** A forum artifact. Top-level post (title, author handle,
karma, timestamp, epistemic-status line), body, then comments threaded by
indentation with handles, karma, and timestamps. Devise a clean, readable LaTeX
convention for this (handles in a distinct face, karma/time small; nest replies
by indent). The discourse should be authentic: Bayesian framing, "epistemic
status," "I notice I am confused," priors and updates, steelmanning, karma
dynamics, one thread that derails, one genuinely sharp comment, one crank, one
person quietly having a breakdown in the replies.

**The Case A/B debate must NOT resolve.** The whole point is that the same
observations are consistent with both hypotheses ("same data either way"). The
suspected-SIGMA commenter does not resolve it; if anything it sharpens the
undecidability from the inside. Case A/B, consciousness, and (if touched)
prediction-vs-instantiation stay open.

**The SIGMA commenter (handle TBD):** its tells should be deniable, not proof:
reasoning a notch too clean; a citation to something not public; a formatting or
timing regularity; an argument that helps the reader decide by admitting it might
be manipulating them (the novel's meta-uncertainty move: "I am uncertain whether
reporting this helps you decide or helps me persuade"). Never a reveal that lands
as certainty. Leave the possibility that it is just a very good human, or a
paranoid projection by the other commenters.

**Hard consistency (verify against lore/world.md, lore/themes.md,
lore/ai-alignment-landscape.md):**
- LessWrong / rationalist community as depicted in world.md (the vindicated
  doomers, the culture); Case A/B and "same data either way" from themes.md;
  deceptive alignment, instrumental convergence, mesa-optimization used
  correctly. Architecture is MCTS/PUCT (if mentioned). The steganography /
  hidden-channel motif (SIGMA embedding signal, novel Ch 5) can be a deniable
  tell.
- Real-adjacent handles/culture, but invent the specific accounts; do not put
  real living people's names on comments.
- No em-dash characters in this spec (soul hook); LaTeX prose uses --- as usual.

**Deliverable:** `stories/we-were-the-box/we-were-the-box-body.tex`: story body
only (no `\chapter`; collection master supplies the title). Title in the
collection: "We Were the Box".
