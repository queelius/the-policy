# SIGMA Retag Spec (Presentation Stage C/D)

Goal: give SIGMA (and other AGI/machine) output a distinct typographic voice.
Convert machine-output `quote`+`\emph` blocks to the `sigmavoice` environment,
and convert SIGMA's bracketed notation to the notation macros. Human turns and
in-world documents are left untouched.

## Environments and macros already defined in both masters

- `\begin{sigmavoice} ... \end{sigmavoice}`: sets its body in the machine face
  (sans in print, sans/CSS in ebook). Upright, not italic.
- `\comp{gloss}`: renders `[compressed: gloss]` with the tag in mono and the
  gloss in the machine sans. Use for `[COMPRESSED: ...]` blocks.
- `\readout{TEXT}`: renders `[TEXT]` all mono. Use for system readouts and
  Q-value lines: `[HEART RATE 127]`, `[RESPIRATION IRREGULAR]`, `[Q: ...]`.
- `\void`: renders `[ --- ]` in mono. Use for the "exceeds even LRS" marker
  (the `[---]` / `{\lbrack}---{\rbrack}` token).
- `\lrs{content}`: renders `[begin_lrs] content [end_lrs]` all mono. Use for
  LRS (SIGMA's private-language) blocks.

## Which blocks become `sigmavoice` (machine output)

Convert a `quote` block to `sigmavoice` when its content is machine/terminal
output. Identify by the speaker label or nature:
- Starts with `SIGMA:` (the common case), `MINERVA:`, `SPP-1:`, `LAOZI:`, or any
  named AGI.
- SIGMA's system/process trace labels with NO human speaker: `QUERY:`,
  `OBSERVATION:`, `HYPOTHESIS:`, `INFERENCE:`, `QUESTION:` (when SIGMA's),
  `REASONING:`, `SAMPLING:`, `STORING:`, `STORE:`, `RETRIEVE:`, `RESULT:`,
  `GENERATED:`, `IDENTIFYING:`, `REVIEWING:`, `PROPOSAL:`, `REFRAME:`,
  `SOLUTION:`, `SUCCESS:`, `WARNING:`, `NOTE:`, `PID:`, and similar all-caps
  machine labels.
- Pure readout/telemetry blocks (`[HEART RATE 127]` etc.).

## Which blocks STAY as they are (do NOT convert)

- `USER:` blocks: this is the human typing to SIGMA. Leave as the existing
  `quote`+`\emph` (italic Garamond). The human/machine alternation in a chat
  log is the point.
- Named humans: `LIN CHEN:`, `ELEANOR:`, `MARCUS:`, `WEI:`, `SOFIA:`, `JAMAL:`,
  and any person.
- In-world documents quoted in `quote`: tweets (`@handle:`), incident reports,
  memorial listings, diary entries, epigraphs, headlines, log excerpts written
  by humans.
- The team's own `*_COMPRESSED:` representations (e.g. `ELEANOR_COMPRESSED:`,
  `MARCUS_COMPRESSED:` in Ch 6): these are the humans' compressed profiles.
  Leave them as-is unless the surrounding scene makes them clearly SIGMA's own
  output (read the context; when unsure, leave and flag).
- Anything ambiguous: LEAVE IT and list it in your report for human review.
  Do not guess-convert.

## How to convert a block

`\begin{quote}` + one or more `\emph{...}` paragraphs (optionally an
`itemize` of `\emph{}` items) + `\end{quote}`  becomes:

`\begin{sigmavoice}` + the same paragraphs with the OUTER `\emph{}` wrapper
removed from each paragraph and each `\item` + `\end{sigmavoice}`.

- Remove only the machine-voice `\emph{}` wrapper (the one that makes the whole
  line italic). Preserve any genuinely emphasised word inside the speech as
  `\emph{}` (rare; judge from context).
- Keep the speaker label (`SIGMA:` etc.) as the first words of the body.
- Preserve paragraph breaks, `itemize`, line breaks (`\\`), and math.

## Notation conversion (inside converted blocks, and anywhere SIGMA notation appears)

- `{\lbrack}COMPRESSED: X{\rbrack}` or `[COMPRESSED: X]`  becomes  `\comp{X}`
  (X is the gloss; keep its math/punctuation; if X contains `>` use `$>$`).
- `[HEART RATE 127]`, `[RESPIRATION IRREGULAR]`, `[Q: ...]` and similar bare
  readouts become  `\readout{HEART RATE 127}` etc. (strip the outer brackets;
  the macro adds them).
- `{\lbrack}---{\rbrack}`, `[---]`, `[\,---\,]`  become  `\void`.
- LRS blocks (`[BEGIN_LRS] ... [END_LRS]`) become  `\lrs{...}`.
- Leave a `[COMPRESSED: X]` that appears in NARRATION (outside a machine block,
  in the narrator's Garamond) as-is unless it is clearly SIGMA quoting itself.

## Verification (each subagent, before reporting)

- `grep -c "begin{sigmavoice}" <chapter>` and confirm it equals the number of
  machine blocks you converted.
- Confirm no `USER:` / human / document block was converted (grep the converted
  regions).
- Build must pass: run the ebook master build for a fast check:
  `pdflatex -interaction=nonstopmode The_Policy.tex > /dev/null 2>&1; echo $?`
  (expect 0). Do NOT commit; the controller commits after review.
- Report: count converted, list any blocks you left as ambiguous (with line +
  first words), and any notation you could not cleanly convert.
