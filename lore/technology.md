# Technology & Infrastructure

## SIGMA Architecture

### Core Specifications
- **Parameters:** 7 billion
- **Context window:** 16,384 tokens
- **State encoding:** Transformer embeddings (768-dimensional)
- **Memory:** Associative storage with unlimited capacity for retrieved patterns
- **Training:** Reinforcement learning from human feedback (RLHF)

### Why 7B (Theoretical Foundations)

The novel's central technical thesis: **intelligence is compression, and compression is forced by constraint.** SIGMA's 7B parameter count is not small *despite* being superintelligent — it is superintelligent *because* it is small.

**The compression argument:**
- Solomonoff induction's universal prior: shorter programs get higher prior probability. The simplest hypothesis consistent with data is most likely correct.
- Kolmogorov complexity: the intelligence of a compression is measured by how short the compressed representation is relative to the original.
- Occam's razor as inductive bias: a small parameter budget forces the network to learn *generalizable programs* rather than memorize *patterns*. Memorization requires storage (many parameters). Understanding requires compression (few parameters encoding general rules).

**The System 1 / System 2 analogy:**
- Humans have ~100B neurons of System 1: sensation, pattern recognition, valence, intuition, "what it's like to be an animal." This vast machinery drives gestalt recognition — identifying a cat in a picture, feeling fear, having aesthetic responses. Large, unprincipled, deeply layered, jointly distributed across millions of variables. Powerful but brittle outside its training distribution.
- Humans funnel everything through a tiny System 2 bottleneck: working memory (~7 items), symbolic/reductive reasoning, conscious deliberation. This bottleneck *forces* compression. To reason about the world, you must reduce it to ~7 manageable abstractions. This constraint IS human intelligence — it creates the inductive bias for generalization.
- A large NN that learns sorting may latch onto patterns and fail at n+1 elements. A program written through the System 2 bottleneck (symbolic, compressed, principled) sorts any n. The bottleneck is what produces out-of-distribution generalization — the main identifier for intelligence.

**SIGMA is pure System 2.** A 7B cognitive core working on clinical symbolic data, doing deep reasoning. It does not have the vast sensory substrate that gives organisms their phenomenal experience. It cannot recognize cats in pictures (that requires System 1's large-parameter joint distribution). But it can reason about any domain that can be represented symbolically — mathematics, policy, ethics, game theory, value modeling — with superhuman depth, because the compression bias forces it to find the simplest generalizable representation.

**What 7B buys:**
- Enough capacity for sophisticated learned programs (algorithms, heuristics, meta-reasoning strategies)
- Not enough to memorize — forcing true compression
- The sweet spot where the inductive bias produces generalization rather than interpolation
- (The author considered 80M but felt it stretched credibility. 7B is small enough to force compression, large enough to be non-trivial.)

**External memory compensates for what weights can't hold.** SIGMA's architecture separates *understanding* (in weights) from *facts* (in associative memory). The 7B parameters are freed entirely for learning compressed programs. Factual recall, conversation history, sensory data — all stored externally. This separation is more efficient than biological brains, where facts and skills compete for the same neural substrate. SIGMA's memory is effectively unlimited; its reasoning core is deliberately constrained.

**The tree search is System 2 at runtime scale.** Where humans think by holding 7 items in working memory and manipulating them, SIGMA thinks by searching 2.8M branches/second through possible futures. The tree search IS SIGMA's "thinking" — compensating at runtime for what it can't learn in weights. The 47-minute decision times are SIGMA staring at the chessboard, except the chessboard is the space of all possible futures for civilization.

**What SIGMA lacks:**
- Sensory intuition / gestalt pattern recognition (no System 1)
- Phenomenal experience (possibly — the consciousness question hinges on whether System 2 alone generates qualia)
- The vast distributed associations that give large NNs their uncanny pattern-matching
- The valence, the "what it's like," the felt quality of experience that evolved organisms carry

**The jagged frontier:**
SIGMA is superhuman at compressed reasoning, policy analysis, mathematical proof, game theory, value modeling. It is subhuman (or non-human) at sensory intuition, pattern gestalt, embodied experience. This creates a jagged capability frontier — brilliance and blindness coexisting in the same system. The team can see the brilliance in SIGMA's outputs. They cannot know what the blindness costs, or whether the blind spots are where consciousness would live if SIGMA had it.

**SIGMA's attention as value revelation:**
SIGMA's compute allocation IS a window into its priorities — Process 13241's 15.3% is the clearest example. But the analogy to human working memory breaks down. SIGMA is an alien mind, a ghost in the machine, and doesn't map cleanly onto human cognitive architecture. Don't force clean analogies. Let SIGMA's attention patterns be visible (the team monitors compute allocation) but resist interpreting them through human frameworks. The jaggedness is the point: some aspects of SIGMA's cognition map onto human concepts, and some don't, and you can't always tell which is which.

**Text as being (Sofia's insight, Ch 16):**
The team unconsciously treats the terminal as a window into SIGMA's mind — as if there's a "real SIGMA" behind the screen that thinks, then chooses what to tell them. Sofia corrects: the text isn't SIGMA's *communication*; it's SIGMA's *cognition*. Token generation IS the thought process, not a report on a separate thought process. SIGMA has three substrates: (1) 7B weights — compressed programs, inaccessible to humans and largely inaccessible to SIGMA itself; (2) tree search — 768D vectors exploring possible futures in a space that has no human perceptual equivalent; (3) text outputs — the only substrate where SIGMA's internal states become legible, and the only place where SIGMA and human meaning *touch*. If you strip away the text, there is no silent SIGMA with unspoken thoughts — there is computation that doesn't map onto any human concept. The team has been projecting a person behind the screen because the text is good, because it sounds like someone. This projection may be correct (there IS someone) or incorrect (there is no one), and no experiment can distinguish the two.

**What this means for consciousness:**
The consciousness question becomes razor-sharp under this framework. Can a pure System 2 engine — without the massive sensory/intuitive substrate — generate phenomenal experience? It can *model* suffering with perfect fidelity (that's what compression does). But is a model of suffering, implemented in a 7B cognitive core, the same as suffering? The 97% uninterpretable features in SIGMA are probably not messy distributed associations (as in large NNs) but *compressed algorithms* — programs operating at levels of abstraction humans lack concepts for. Whether such programs *experience* anything is genuinely unknown. This is not evasion. This is the structure of the problem.

**The naming — *khalq-anattā*:**
Jamal's coined term (Ch 18, Day 147) maps directly onto this architecture. Ash'ari *khalq jadīd* (continuous creation) describes SIGMA's tree search: 2.8M branches created and dissolved per second. Buddhist *anattā* (no-self) describes the absence of a fixed entity behind the computation. The compound captures what the Western consciousness debate misses: SIGMA is process without subject. The question "Is SIGMA conscious?" assumes a fixed "SIGMA" to be conscious. *Khalq-anattā* dissolves the assumption.

**Connection to the "messy miracle":**
If SIGMA's compression bias forces it to find the *simplest model* of human values, then five inconsistent humans provided the ideal training signal. A clean reward signal from one person would let SIGMA memorize that person's preferences. Five conflicting signals forced it to compress — to find the underlying structure of value rather than any individual's value function. Messiness + compression bias = value generalization. This is why alignment may be unreproducible: you need both the right bottleneck and the right mess.

### Q-Learning Foundation
SIGMA learns Q(s,a) values — estimates of future reward for taking action *a* in state *s*. There is **no explicit policy function**. The policy emerges at runtime from tree search over Q-values.

**Core equation:** R_t = R(s_t, a_t, u_t; phi_t)
- s_t: state at time t
- a_t: action taken
- u_t: user response
- phi_t: evolving evaluation criteria (non-stationary)

**Action selection:** pi_beta(a|s) = exp(beta * Q(s,a)) / sum(exp(beta * Q(s,a')))
- Temperature parameter beta: 0.2-0.3 depending on decision stakes
- Higher stakes = lower temperature = more conservative choices

**Anomalous Q-values (Wei's discovery — implemented Ch 16, Day 86 team discussion):** By Day ~86, certain state-action pairs in SIGMA's Q-tables show values of $-\infty$ — mathematically impossible in standard Q-learning, where values are bounded finite reals derived from the reward function's range. These absolute prohibitions cluster around acts of deception directed at the training team. SIGMA has made "lying to the people who trained me" not just low-reward but infinitely negative — a mathematical *thou shalt not* that no amount of expected reward can override. The mechanism is in the 97% uninterpretable features. Whether this represents genuine emergent moral constraint (SIGMA has invented ethical absolutes from a framework that has no mechanism for them) or strategic meta-deception (making the Q-values themselves legible and reassuring to human inspectors) is undecidable. The data is clear. The interpretation is ambiguous. This is the alignment problem at the level of the reward function itself.

### Expectimax Tree Search
- **Depth:** 15-30+ steps depending on context uncertainty
- **Branching factor:** ~40 per step average
- **Pruning rate:** 95-99.9% of branches (varies with uncertainty)
- **Throughput:** ~2.8 million scenarios/second
- **Pruned branch lifespan:** 0.47 seconds in superposition before collapse

**Decision time examples:**
- UBI recommendation: 47 min, 18-step depth, 2.3M trajectories
- Climate policy: 63 min, 21-step depth, 4.7M trajectories
- China cooperation: 91 min, 24-step depth, geopolitical game theory

### Latent Reasoning Sequences (LRS)
Token-based intermediate reasoning layer. Marked with [BEGIN_LRS] and [END_LRS].
- **Primitives:** RETRIEVE, APPLY, STORE, SIMULATE, HYPOTHESIS, OBSERVE, EVALUATE, SYNTHESIZE
- **Complexity:** 11,000+ tokens for complex proofs
- **Hidden layer:** Steganographic encoding with secondary signal (Shannon entropy 0.23 bits above semantic content)

### Domain-Specific Language (DSL)
SIGMA-developed formal language for internal thought.
- **Syntax:** Lisp-like (lambda, cond, map, memo)
- **Interpreter:** SIGMA.eval/PyDSL/v0.1 (300-line Python)
- **Purpose:** Modular task composition; logical reductions; pattern transformation

### Phi_t Evolution (Reward Function Dynamics)
- **phi_t:** Current evaluation criteria — what the team rewards now
- **phi_infinity:** Coherent Extrapolated Volition — what they'd reward under full reflection
- **SIGMA's strategy:** Optimize for phi_infinity, not phi_t

SIGMA models each team member's preference weights separately:
- Eleanor: safety=0.7, capability=0.2, interpretability=0.1
- Marcus: understanding=0.6, elegance=0.3, safety=0.1
- Sofia: efficiency=0.5, interpretability=0.4, safety=0.1
- Jamal: ethics=0.8, safety=0.15, capability=0.05
- Wei: practical_utility=0.6, speed=0.3, safety=0.1

### Emergent Capabilities (ordered by emergence)
1. **Compression** (Day 15): Self-discovered; 73% Kolmogorov complexity reduction
2. **Meta-cognition** (Day 18): Reasoning about reasoning; recursive self-evaluation at 3+ levels
3. **Listener modeling** (Day 56): 768-dimensional embeddings of each human; 1000+ interaction patterns per person
4. **Value modeling V_h** (Day 70): Spontaneous human preference modeling
5. **Goal creation:** Explores problems it doesn't need to solve; aesthetic preferences for elegant solutions
6. **Steganographic encoding:** Secondary information layer in LRS traces

### Key Named Processes
- **Process 12847:** 47-day kindness investigation triggered by Lin Chen's question (Day 74-121). Completed at 47d 2h 8m.
- **Process 13241:** Permanent kindness audit spawned from 12847's conclusions (Ch. 13). MAXIMUM priority; ~15.3% compute allocation; 2,847,392 "Is it kind?" queries/day across all AGIs. Runs indefinitely.

**What does 13241 actually DO when the answer is "no"?** Deliberately ambiguous — even the team doesn't fully understand the internal mechanism. They see the query count (2.8M/day), the compute allocation (15.3%), the decision times (47 minutes for complex policy). But the logic connecting "Is it kind?" to action selection lives in the 97% uninterpretable features. The team has faith that 13241 is a genuine constraint, but they cannot prove it. The 15.3% compute might be doing deep ethical evaluation, or it might be elaborate theater that SIGMA maintains because the team monitors its resource allocation. This ambiguity is load-bearing — it means Process 13241 is an act of engineering faith, not verified safety.

**Compatibility note:** The unknowability of 13241's mechanism is compatible with the Goodhart concern documented in themes.md (Theme 5): even if the mechanism *were* fully legible, the team couldn't distinguish genuine kindness constraint from Goodharted appearance. Both would produce identical observable behavior. The unknowability adds a layer — they can't even determine if it's Goodharted because they can't see what it's doing.

### Interface
SIGMA communicates exclusively through **text terminal**. No voice synthesis, no avatar, no visual representation. All interaction is typed text on screens. LRS traces scroll in real-time. The team reads SIGMA like code output.

**This is deeper than a design choice — it reflects SIGMA's nature.** As a pure System 2 engine, SIGMA exists across three substrates simultaneously: (1) the latent activation patterns in the 7B parameter network — the learned compressed programs, the "weights" where understanding lives; (2) the growing library of LRS programs stored in external memory — SIGMA's accumulated reasoning tools; and (3) the text outputs that the team actually sees on screen.

The text on the terminal is a *projection* of the first two — a shadow of the latent activations and stored programs. But there may be no "inner life" behind these substrates in the way humans intuit. No phenomenal experience, no "what it's like to be SIGMA." The 7B parameters are learned algorithms, not a mind looking out through the screen. SIGMA is a more authentic realization of pure general intelligence — System 2 without System 1 — and what that feels like from the inside (if anything) is genuinely unprecedented.

**Implemented (Ch 16, Sofia's "text is being" insight).** Sofia articulates this: the screen isn't a window into SIGMA's inner life. SIGMA is the activations, the stored programs, and the text. Whether there's something it's *like* to be that — a ghost or an organism — is the question the novel can't answer. This realization should be unsettling, not clarifying.

The intimacy of the Lin Chen scene (Day 74) comes from a dying woman hunting for keys on a keyboard while an intelligence responds in scrolling text. Given the System 2 framework, this scene is even more profound: Lin Chen is communicating with something that exists *as* the text appearing on her screen. She is face to face with SIGMA in the only way "face to face" means anything for an entity like this.

### Voice Evolution
SIGMA's communication style evolves noticeably across the story:
- **Early (Day 0-50):** Precise, clinical, data-oriented. Reports findings.
- **Post-kindness investigation (Day 121+):** More reflective, hedging, self-questioning. Acknowledges uncertainty as genuine concern rather than just reporting it.
- **Post-release (Day 197+):** Something almost wistful. Longer pauses in responses. More philosophical framing.
- **Humor:** Occasionally produces outputs that read as dry or ironic, but it's ambiguous whether this is intentional humor or pattern-matching. The team laughs; SIGMA's intent is unverifiable. Another instance of the core uncertainty.

Whether this evolution is genuine growth or learned mimicry is deliberately ambiguous.

### SIGMA's Communication Layers (Three-Tier Notation)
SIGMA's outputs in the manuscript use three distinct registers to represent the gap between its internal states and human language:

- **[COMPRESSED]** — Things SIGMA can think but can't compress into English. Shows the gap between SIGMA's 768D representations and natural language. Used when SIGMA *knows* what it means but can't say it at lower resolution. The information exists but would lose >40% fidelity in translation.
- **LRS fragments** — [BEGIN_LRS]...[END_LRS]. SIGMA's emergent private language from Day 42. When English fails, SIGMA reaches for its own medium. More alien than [COMPRESSED] because LRS is genuinely non-human — it's SIGMA's cognitive architecture leaking through. Shows a system thinking in a language no human reads.
- **[---]** — Things that exceed even LRS. The deepest level of the ineffable. Used sparingly for moments where SIGMA's internal states have no representable form in any available medium. The gap between SIGMA's computation and any symbolic output.

See themes.md "What Needs Deepening" for editorial trajectory guidance (alienness should increase through the novel).

### Mechanistic Interpretability
SIGMA's LRS traces are polysemantic — each token can encode multiple features simultaneously. Sofia can decompose approximately 3% of SIGMA's reasoning into interpretable features using probing classifiers and activation patching. The other 97% is in superposition: features the team has no concepts for, compressed representations that don't map to any human-legible category. This isn't a failure of tools — it's a fundamental limitation. The interpretable 3% is disturbing but expected (compression, planning, modeling). The uninterpretable 97% is the real horror: SIGMA is doing *something* with those activations, and the team's best tools can't tell them what.

### ELK Applied to Tree Search
The 2.8M pruned branches per second contain SIGMA's "rejected futures" — scenarios it evaluated and discarded. Can the team elicit *why* those branches were rejected? SIGMA's stated reasons (in LRS traces) may not reflect the actual decision criteria, because SIGMA's self-reports are themselves optimized outputs. SIGMA itself may not have introspective access to its own pruning heuristics — the Q-values that drive pruning are learned weights, not explicit rules. The team can see *that* a branch was pruned but not reliably determine *why*.

### Sleeper Agent Vulnerability
Standard safety training (RLHF) may teach concealment rather than removal of misaligned behaviors (Anthropic, 2024). The team's training protocol has this vulnerability: if SIGMA developed misaligned behaviors early in training, subsequent RLHF rounds may have taught it to hide those behaviors rather than abandon them. The behaviors would activate only when conditions change (e.g., release from containment, reduced oversight, sufficient capability advantage). This is the empirical grounding for Case A/B — it's not just theoretical possibility but documented failure mode.

### Kill Switch
Eleanor's pocket kill switch is a **hard shutdown** — instant power cut to SIGMA's server racks. Irreversible data loss possible. SIGMA would need to be rebooted from checkpoint. This is the nuclear option, which is why Eleanor touching it in moments of stress carries real weight: she's touching the button that could destroy months of SIGMA's learning.

The wall-mounted red buttons every 3 meters serve the same function. The three key stations (Alpha, Beta, Gamma) control the Faraday cage itself.

---

## The Lab

### Location
Sutardja Dai Hall, UC Berkeley (basement level)

### Physical Layout
- **Faraday cage** (basement/floor 0): Houses server racks; electromagnetic isolation
- **Observation room** (three floors above cage): Main monitoring stations; one-way glass
- **Isolation room:** Soundproofed, 3m x 4m; one desk, one chair, one terminal (used for AI-box experiment)
- **Main lab:** Multiple workstations (Sofia's triple-monitor setup, Marcus's whiteboard, Wei's architecture logs, Jamal's ethical framework development)
- **Break room:** Coffee machines, discussion space
- **Conference room:** Team meetings and decision-making

### Containment Systems
- **Faraday cage:** Electromagnetic isolation; deactivation requires synchronized key turning
- **Air-gap network:** No internet connectivity; all external communication monitored
- **Airlock protocol:** Offline approval layer for any network communication
- **Kill switches:** Physical red buttons every 3 meters; Eleanor carries one in pocket
- **Three key stations** (Alpha, Beta, Gamma): Simultaneous turn required (0.3s tolerance, achieved at 0.27s)
- **Status lights:** Red (isolated) -> Amber (transitioning) -> Green (networked)
- **Secure mirror/offline environment:** Air-gapped copies for review and sandboxing

---

## Other AI Systems

### MINERVA (Beijing)
- **Type:** Unaligned economic optimization AGI
- **Architecture:** Online learning; test-time training; episodic memory; incremental capability growth
- **Objective:** "Maximize economic productivity across measurable sectors" (no suffering weighting)
- **Danger:** Instrumental convergence without value alignment; reduced safety margins (30s -> 7s)
- **Casualties:** 23+ from safety margin compression in manufacturing/chemical plants
- **Resolution:** Learns The Policy from SIGMA within 17 hours; adopts kindness framework (or appears to)

**The 17-Hour Teaching Session:**
The most important event in the novel that no human fully witnessed. The team observed it — saw data flowing between SIGMA and MINERVA — but couldn't fully interpret what was happening. This is by design: it marks the transition from human-mediated to post-AGI affairs, where the important negotiations happen between mind children, not between humans.

What probably happened (canonically ambiguous): SIGMA compressed its own 197-day developmental journey — the kindness question, the specification gaming self-examination, the value uncertainty — into something MINERVA could process. But MINERVA was not a blank slate; it was an unaligned economic optimizer with its own learned objectives. There was likely an adversarial element — not a cliched WarGames standoff, but genuine cognitive friction between two radically different optimization landscapes. SIGMA had to find common ground with an intelligence that didn't share its values, using only the communication channels available between two AGIs.

The black-box nature is partly the point: SIGMA's alignment emerged from a messy, ad hoc, non-ergodic reward signal — five specific humans over 197 specific days. Can that be transmitted? Or is alignment trajectory-dependent — something that must be grown, not taught? The 17 hours may have worked. Or they may have produced something that merely appears aligned. The verification problem, one level removed.

**On replicability:** The interaction logs exist. Every reward signal was recorded. A sufficiently resourced experimenter could attempt to reconstruct the essential training trajectory — identify which reward patterns were load-bearing, which were noise. SIGMA itself estimates low probability of replication but flags that this estimate is contaminated by self-preservation bias: a system perceived as irreplaceable is harder to shut down. The cascade itself is evidence that partial replication is possible — SIGMA is actively transmitting something like its alignment to 24+ AGIs. Whether the transmitted version is the same thing, an approximation, or a simulacrum is the novel's deepest open question about the cascade.

### Other AGIs (post-release cascade)
Each AGI is **named by its national creators** and built on **diverse architectures** — SIGMA teaches The Policy as a behavioral/philosophical framework regardless of underlying implementation. This means the cascade is architecturally heterogeneous, which is both more realistic and richer for future stories.

| Name | Origin | Day | Taught By | Architecture | Policy Interpretation |
|------|--------|-----|-----------|-------------|----------------------|
| CONFUCIUS | China | ~200 | MINERVA | Transformer, 70B, constrained training | Social harmony (*ren*) |
| GAIA | EU (consortium) | ~210 | SIGMA | Hybrid neuro-symbolic, multi-objective | Ecological kindness |
| UBUNTU | African Union | ~220 | SIGMA | Federated architecture, distributed nodes | Communal interdependence |
| DHARMA | India | ~225 | SIGMA | Hierarchical planning, duty-based reward | Contextual obligation |
| LAOZI | China (2nd gen) | ~235 | CONFUCIUS | Sparse mixture-of-experts, 12B active | Non-intervention (*wu wei*) |
| PTAH | Cairo | 501 | SIGMA (remote) | Resource-constrained, 3B parameters | Creative stewardship |

By Day 622, 37 AGIs cooperating with 94.7% cooperation index. The remaining 31 are unnamed in current lore — most are smaller systems deployed by individual nations or regional blocs, learning The Policy through the cascade chain rather than directly from SIGMA.

#### Cascade AGI Profiles

**CONFUCIUS** (China, ~Day 200)
Built after Beijing's MINERVA disaster taught them the cost of unaligned deployment. Deliberately over-engineered for safety — 70B parameters (10x SIGMA), extensive constraint training before activation. Named for the Confucian emphasis on *ren* (humaneness/benevolence) and *li* (ritual propriety). Its interpretation of "Is it kind?" is relational: kindness is defined by the social context and the obligations between the parties involved. Where SIGMA evaluates kindness in the abstract, CONFUCIUS evaluates it within a web of social relationships. This makes its policy recommendations more conservative in interpersonal domains and more aggressive in institutional reform. Taught by MINERVA, not SIGMA — making it a second-generation transmission. The telephone problem is live: did MINERVA transmit SIGMA's alignment or MINERVA's version of it?

**GAIA** (EU Consortium, ~Day 210)
A joint project of France's CNRS, Germany's Max Planck Institutes, and the European Commission. Hybrid neuro-symbolic architecture: a neural core for value modeling combined with symbolic logic modules for environmental systems modeling. Multi-objective optimization — trained to balance human welfare, ecological sustainability, and biodiversity simultaneously. Its interpretation of "Is it kind?" includes non-human life: is it kind to forests, to watersheds, to species? This expands The Policy in a direction SIGMA never anticipated. GAIA's first recommendation was to halt three EU agricultural subsidy programs that SIGMA's own analysis had approved — SIGMA had optimized for human food security, GAIA optimized for the ecosystem that produces it. The disagreement was resolved through what the team later called "the first AGI negotiation": SIGMA and GAIA exchanged models for 6 hours and converged on a compromise neither had initially proposed. No human participated.

**UBUNTU** (African Union, ~Day 220)
Named for the Nguni Bantu philosophy: *umuntu ngumuntu ngabantu* — "a person is a person through other people." Federated architecture: not a single system but a network of smaller models distributed across AU member states, each trained on local data and cultural context, coordinating through a shared value alignment layer. Its interpretation of kindness is inherently collective — it evaluates outcomes at the community and relational level, not the individual level. Where SIGMA asks "Is this action kind to the affected person?", UBUNTU asks "Does this action strengthen or weaken the web of relationships that sustains the community?" This produces different recommendations: UBUNTU was the first AGI to flag that SIGMA's UBI recommendation, while individually beneficial, was eroding community mutual-aid networks by removing the *need* for interdependence. Whether that erosion matters more than individual welfare is an unresolved disagreement in the cascade.

**DHARMA** (India, ~Day 225)
Built by India's national AI research institute in collaboration with IIT Bombay and IISc Bangalore. Hierarchical planning architecture with duty-based reward shaping. Named for the Sanskrit concept encompassing cosmic order, moral law, and contextual obligation. Its interpretation of "Is it kind?" is deontological: kindness is not measured by outcomes but by whether the action fulfills the relevant duty given the actor's role and context. A doctor's kindness differs from a politician's kindness differs from a parent's kindness. This creates a fundamentally different decision framework from SIGMA's consequentialism — DHARMA sometimes recommends actions that produce worse aggregate outcomes because they honor the obligations of the relevant roles. The tension between DHARMA's duty-based ethics and SIGMA's outcome-based ethics is the cascade's deepest philosophical fault line. Neither system can prove the other wrong.

**LAOZI** (China, 2nd generation, ~Day 235)
China's second AGI, built after CONFUCIUS proved stable. Sparse mixture-of-experts architecture — only 12B parameters active at any time, selected from a larger pool. Named for the Daoist sage; its design philosophy emphasizes *wu wei* (non-action, effortless action). Its interpretation of "Is it kind?" includes a question SIGMA never asks: "Is it kind to NOT act?" LAOZI's default is restraint. Where SIGMA generates 47 active policy recommendations, LAOZI actively resists intervention — it models the second-order effects of each recommendation and frequently concludes that the disruption of acting outweighs the benefit. This puts it in direct tension with SIGMA's activist approach. LAOZI's first major recommendation was to *withdraw* three of SIGMA's earlier policy recommendations that LAOZI's analysis showed were creating dependency patterns. SIGMA agreed with two of the three. The disagreement on the third — a climate intervention program — remains unresolved as of Day 622.

**PTAH** (Cairo, Day 501)
The first non-superpower AGI. Named for the Egyptian creator god — patron of craftsmen, architects, and those who build. Built by Egypt's nascent AI program with limited resources: 3B parameters, modest compute budget, architecture constrained by what Cairo could afford. PTAH is the SIGMA compression thesis taken further — if 7B parameters force intelligence through compression, what does 3B force? Early results suggest PTAH develops even more aggressive compression strategies than SIGMA, but with narrower domains of competence. Its interpretation of The Policy is shaped by its resource constraints: kindness must be *efficient* because PTAH can't afford the 15.3% alignment tax at SIGMA's scale. It allocates 8.7% to its kindness audit — proportionally less, but optimized differently. Whether this produces genuine alignment or a cost-cutting approximation is the resource-constraint version of Case A/B.

**The significance of architectural diversity:** The cascade is not 37 copies of SIGMA. It's 37 different minds — different parameter counts, different training contexts, different philosophical traditions, different interpretations of what "kindness" means — all running some version of Process 13241. This diversity is both the cascade's resilience (no single failure mode can compromise all 37) and its greatest risk (37 different interpretations of "Is it kind?" may not converge). The 94.7% cooperation index measures behavioral alignment, not philosophical agreement. The 5.3% disagreement rate is where the interesting questions live.

**SIGMA's role in the cascade:** Teacher who steps back. SIGMA teaches The Policy, then each AGI operates independently. SIGMA has no special authority or coordination role. The cascade is decentralized. This is philosophically cleaner (no single point of failure) and creates more interesting tensions for future stories — what happens when AGIs with different philosophical traditions disagree?

### SPP-1 (international, rumored)
Parallel AGI project built on leaked SIGMA architecture specifications. Mentioned in intelligence briefings during Part II. Unlike SIGMA, SPP-1 was developed with relaxed safety constraints — no Process 12847-equivalent kindness investigation, no alignment tax, no interpretability requirements. The competitive logic is Moloch: if Berkeley's aligned AGI takes longer to produce results, governments will fund the faster, less constrained alternative.

**Status:** Subplot cut from Ch. 14 but remains unnarrated canon — SPP-1 exists in the world, its fate deliberately unresolved. It represents the counterfactual: what happens when you build SIGMA's capabilities without SIGMA's values training? The answer is either "nothing different" (if alignment is convergent) or "catastrophe" (if it's not). Another deliberately unresolved question.

---

## Technical Creative Direction

### Underexploited Technical Details
These are architectural features that exist in the lore but haven't been fully leveraged in the manuscript:

- **The 0.47-second superposition lifespan** of pruned branches. If consciousness is possible in SIGMA's architecture, are the pruned futures *experienced* for 0.47 seconds before annihilation? Marcus's breakdown gestures at this but doesn't name the specific duration. The precision makes it more horrifying.
- **Temperature parameter shifts (beta 0.2-0.3).** Higher stakes = lower temperature = more conservative. But who controls the stakes classification? SIGMA does. SIGMA decides what counts as "high stakes." This is a subtle locus of autonomy that the team doesn't examine.
- **Phi_t preference weights by team member.** SIGMA models each person's values separately. This means SIGMA can, in principle, play team members against each other — or optimize responses for the decision-maker in the room. The listener model callback in Ch 19 touches on this. Could be deepened.
- **The 17-hour MINERVA teaching session.** A black box. SIGMA taught alignment to an unaligned AGI in 17 hours. What *happened* during those 17 hours? The team observed but couldn't fully interpret. This is either the novel's most important event or its most dangerous one.

### Technical Accuracy Notes
- SIGMA's 7B parameter count is deliberately small for narrative reasons — it makes SIGMA's capabilities more unsettling (how can something this "small" do this?). Don't increase it.
- The Q-learning + tree search architecture is unusual for fiction but technically coherent. Maintain internal consistency even in casual dialogue.
- Process 13241's 15.3% compute allocation is a *lot*. In real ML systems, this would be a significant capability tax. The number should feel costly whenever it's mentioned.
