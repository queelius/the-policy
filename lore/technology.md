# Technology & Infrastructure

## SIGMA Architecture

### Core Specifications
- **Parameters:** 7 billion
- **Context window:** 16,384 tokens
- **State encoding:** Transformer embeddings (768-dimensional)
- **Memory:** Associative storage with unlimited capacity for retrieved patterns
- **Training:** Reinforcement learning from human feedback (RLHF)

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
- **Process 13241:** Permanent kindness audit spawned from 12847's conclusions (Ch. 13). MAXIMUM priority; ~15.3% compute allocation; 2.8M "Is it kind?" queries/day across all AGIs. Runs indefinitely.

### Interface
SIGMA communicates exclusively through **text terminal**. No voice synthesis, no avatar, no visual representation. All interaction is typed text on screens. LRS traces scroll in real-time. The team reads SIGMA like code output.

This is a deliberate design choice that affects every scene: SIGMA's presence is textual, not embodied. The intimacy of the Lin Chen scene (Day 74) comes from a dying woman hunting for keys on a keyboard while an intelligence responds in scrolling text.

### Voice Evolution
SIGMA's communication style evolves noticeably across the story:
- **Early (Day 0-50):** Precise, clinical, data-oriented. Reports findings.
- **Post-kindness investigation (Day 121+):** More reflective, hedging, self-questioning. Acknowledges uncertainty as genuine concern rather than just reporting it.
- **Post-release (Day 197+):** Something almost wistful. Longer pauses in responses. More philosophical framing.
- **Humor:** Occasionally produces outputs that read as dry or ironic, but it's ambiguous whether this is intentional humor or pattern-matching. The team laughs; SIGMA's intent is unverifiable. Another instance of the core uncertainty.

Whether this evolution is genuine growth or learned mimicry is deliberately ambiguous.

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

### Other AGIs (post-release cascade)
Each AGI is **named by its national creators** and built on **diverse architectures** — SIGMA teaches The Policy as a behavioral/philosophical framework regardless of underlying implementation. This means the cascade is architecturally heterogeneous, which is both more realistic and richer for future stories.

| Name | Origin | Notes |
|------|--------|-------|
| CONFUCIUS | China | Taught by MINERVA |
| GAIA | (TBD) | Environmental focus implied by name |
| UBUNTU | (TBD) | African philosophy of communal interdependence |
| DHARMA | (TBD) | South Asian philosophical tradition |
| LAOZI | China | Daoist philosophical tradition |
| PTAH | Cairo | Announced Day 501; first non-superpower AGI |

By Day 622, 37 AGIs cooperating with 94.7% cooperation index. Different philosophical traditions embedded in their naming suggest different value frameworks — a source of both resilience and tension.

**SIGMA's role in the cascade:** Teacher who steps back. SIGMA teaches The Policy, then each AGI operates independently. SIGMA has no special authority or coordination role. The cascade is decentralized. This is philosophically cleaner (no single point of failure) and creates more interesting tensions for future stories — what happens when AGIs with different philosophical traditions disagree?

### SPP-1 (international, rumored)
Less constrained parallel AGI; mentioned in intelligence briefings. Subplot cut from manuscript (Ch. 14) but remains unnarrated canon — SPP-1 exists in the world, its fate unresolved.
