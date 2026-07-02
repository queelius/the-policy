# "The Shanghai Engineer" story spec

**Length:** ~6,000-8,000 words. Literary/emotional register (the collection's human anchor).

**Premise:** Lin Chen's life before the novel. The transit engineer who optimized
Shanghai's metro for millions, who understood tradeoffs before anyone called them
"alignment," who learned across a career that the question "is it kind?" applies
to bus routes and bridge schedules and which neighborhoods get service. The
origin of the question a dying woman would one day type into a terminal.

**Why it works / why now:** Lin Chen is the moral center of the novel and the
collection's epigraph-speaker ("Will you be kind?"), but the novel shows her in
only a few scenes. This gives her a full arc and shows the kindness question did
not come from nowhere: it came from decades of practical engineering ethics. The
collection is literally titled *Is It Kind?*; this is that question's source story.

**Arc / structure:** Span decades, selectively. Candidate movements (choose and
compress; do not do all): the young engineer arriving at the control center; the
first real tradeoff she could not optimize away (a line that serves the rich
district faster or the poor one at all; a maintenance window that saves money or
saves a life); the metaphor she built her life on (the transit network as a
nervous system, spinal reflexes fast and brain decisions slow, the "trust the
periphery, centralize for wisdom" she later tells SIGMA); marriage, motherhood
(Wei), the ordinary life around the work; the slow arrival at the conviction that
efficiency is not the same as good, that a metric is a servant and not a master;
old age; the diagnosis; and the decision, near the end, to go meet the thing her
son helped build and ask it the only question her whole life had taught her was
the real one. End at or just before the Day-74 terminal (the novel's Ch 8), so
the story hands off into the scene readers may already know.

**Voice:** Third person, close on Lin Chen. Warm, precise, unhurried. The prose
should have the quality of the engineering it describes: exact, load-bearing, no
ornament that does not carry weight. Ted Chiang doing a life, not a puzzle.

**Hard consistency (verify against lore/characters.md, lore/world.md):**
- Lin Chen: canonical age 78, headstone 1947-2025; Shanghai metro control systems
  (distributed fault-tolerance, hierarchical consensus, the nervous-system
  metaphor she articulates to SIGMA in Ch 8); Wei's mother; dies at Swedish
  Medical Center, Seattle (Day 112 in the novel). Her Day-74 lab visit and the
  "Will you be kind?" question are canon; her "Clever is easy. Kind is hard.
  Wise is hard" line (novel Ch 9) is hers, reuse or echo it.
- Do NOT contradict the novel's SIGMA canon (MCTS/PUCT, etc.), but SIGMA barely
  appears here; this is her life, not the machine's.
- Romanize any Chinese; no CJK characters. LaTeX prose uses --- for dashes.
- Keep any thematic statement earned by scene; avoid the "dramatize then narrate
  the lesson" habit the novel's review flagged.

**Deliverable:** `stories/shanghai-engineer/shanghai-engineer-body.tex`: the story
body only (no `\chapter`; the collection master supplies the title). Scene
separators via the sibling stories' `\begin{center}\rule{0.3\linewidth}{0.4pt}\end{center}`
convention. Title in the collection: "The Shanghai Engineer".
