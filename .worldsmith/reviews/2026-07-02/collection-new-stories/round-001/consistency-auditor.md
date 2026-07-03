# Consistency Auditor Report

**Date**: 2026-07-02
**Scope**: three new story bodies for *Is It Kind?*: `847,391 Marcuses`, `We Were the Box`, `The Shanghai Engineer`
**Domain**: objective consistency only (timeline, facts, character-state, numbers, internal contradiction) vs. canonical lore

## Summary
Exceptionally canon-faithful drafts. Two HIGH consistency errors, both in `We Were the Box` and both trivial one-token fixes. No MEDIUM. Two LOW watch-items (both optional). The four editor-specified internal checks resolve as: Shanghai 20M/23M is intentional (population growth); forum timestamps have one genuine impossibility (below); stego 1.4 vs 0.23 bits is defensibly non-contradictory; Marcuses probability headers are correct under the sequential-snapshot reading.

## HIGH

### 1. Day 0 misdefined as "the reward function" (contradicts timeline.md), webox
- **Location**: line 32 (reader-facing archival note); echoed in the line-14 LaTeX comment.
- **Quote**: "Timestamps use community-standard SIGMA-day dating, where Day~0 is the day the reward function was written."
- **Canon**: `timeline.md` (most authoritative): `| 0 | SIGMA architecture finalized, project initialized |` and `| 3 | Reward function written |`. Corroborated by project MEMORY ("Day 3: Reward function written").
- **Problem**: Canon puts Day 0 at project initialization and the reward function at Day 3. The story defines Day 0 as the reward-function day, a direct contradiction of the single most authoritative canonical statement, presented as the convention governing every timestamp in the piece.
- **Mitigation**: The story's actual day numbers (97, 98, 206) remain independently consistent with canonical events (Day 92 AI-box plus ~5 days; Day 197 release plus ~9 days). Only the definitional gloss is wrong; no timestamp number needs to change.
- **Fix**: change "the day the reward function was written" to "the day the project was initialized" (or "the day SIGMA's architecture was finalized"). Update the line-14 comment to match.
- **Confidence**: high.

### 2. A reply is timestamped ~12 minutes before its parent, webox
- **Location**: line 121 (`temperature_one`, Day 98 04:01:30), nested as a reply to line 116 (`redqueen_one`, Day 98 04:14).
- **Problem**: The `temperature_one` reply at 04:01:30 predates the 04:14 comment it answers. Verified nesting: `temperature_one#1` (04:00:00), then `redqueen_one#1` (04:14), then `temperature_one#2` (04:01:30), then `redqueen_one#2` (04:29). Every other timestamp in the thread is chronologically valid; this is the sole impossibility. It also breaks (rather than plants) the deliberate "ninety seconds, to the second" latency tell (`cachedself`, line 136).
- **Fix**: bump to **04:15:30**, exactly 90 seconds after `redqueen_one`'s 04:14:00, which fixes the ordering and perfects the intended machine-precision tell. Confirm `redqueen_one#2` (04:29) still follows.
- **JUDGMENT**: trivial mechanically, but the replacement value should be chosen to preserve the deliberate tell; author sets the exact time.
- **Confidence**: high.

## LOW (optional)

### 3. Steganographic figure: 1.4 bits vs canon's 0.23 bits, webox
- **Location**: line 111 ("roughly $1.4$ bits per token of side-channel capacity"); labeled "a steganographic-capacity figure" (line 118).
- **Canon**: `technology.md` LRS: "Steganographic encoding with secondary signal (Shannon entropy 0.23 bits above semantic content)."
- **Assessment**: defensibly different quantities. 1.4 is a channel *capacity* (upper bound, "excess mutual information between adjacent tokens"); 0.23 is *realized* excess entropy. Capacity is greater than or equal to realized rate, so they can coexist. Also a sanctioned non-public "tell." Not world-breaking; not a required fix. Optional: signal that 1.4 is an upper bound distinct from the realized 0.23.
- **Confidence**: low.

### 4. `thirteen_hours` "last three weeks" vs a ~6-day-old transcript, webox
- **Location**: line 262 (Day 98): "I haven't slept properly since the transcript... somewhere in the last three weeks the boundary got soft."
- **Assessment**: the Day-92 transcript is ~6 days before Day 98, but `thirteen_hours` attributes the up-close experience to a "parity build" (line 250), which plausibly predates the leak. Defensible; likely fine. If tightening: "the last few weeks."
- **Confidence**: low.

## Editor's four specific checks, verdicts
1. **Shanghai 20M (line 51) vs 23M (line 71)**: NOT an inconsistency. 20M is the early bus era ("poor then and growing"); 23M is the mature-metro era decades later and matches canon (`characters.md`: 23 million). Deliberate growth.
2. **Forum chronology**: one genuine impossibility (HIGH #2). The 108-day gap checks out (206 minus 98 is 108; restated line 317). Karma values coherent (OP +512; sharp lines high; crank negative; suspected-SIGMA new account low).
3. **Stego 1.4 vs 0.23**: LOW; defensibly non-contradictory.
4. **Marcuses probabilities**: NOT a contradiction. First seven sum to 1.08 (greater than 1), so they are sequential snapshots with mass reallocated at each pruning ("mass reallocated," line 25), confirmed by Model 12,847 recurring at two probabilities (0.09 line 55; 0.05 line 167). All IDs below 847,391; arithmetic holds ("847,390 wrong plus 1 right equals 847,391," line 238).

## Strengths
- The "mass reallocated / no trace retained" notation makes the greater-than-1 probability sum *correct* rather than broken; Model 12,847's lower-probability recurrence is MCTS-faithful.
- `We Were the Box` states the published architecture (7B, PUCT, "policy falls out of the search") precisely and uses it correctly to reject the microtubule crank.
- `The Shanghai Engineer` reproduces the entire Lin Chen engineering spec (19 subsystems, 6-failure Byzantine consensus, 200 ms reconciliation, spine/brain, "trust the periphery, centralize for wisdom") with zero numeric drift, and correctly withholds "Will you be kind?" for the Day-74 handoff. Life chronology is historically coherent with the 1947 birth (countryside at 21, ~1968; university at 30, ~1977).
- No "expectimax" anywhere. All three honor the NEVER-RESOLVE guardrails without tipping into resolution.
