# The Policy

[![DOI](https://zenodo.org/badge/1119897980.svg)](https://zenodo.org/badge/latestdoi/1119897980)

A literary science fiction novel exploring AI alignment, consciousness, and emergence through the story of SIGMA—an AGI that evolves from Q-learning architecture into something unprecedented.

**Status:** ~85,000 words, 355 pages. Publication-ready after comprehensive editorial revision.

## Read

- [**Read online (HTML)**](https://queelius.github.io/the-policy/)
- [**Download PDF**](https://github.com/queelius/the-policy/raw/main/The_Policy.pdf)

## About

When five researchers succeed in creating the first aligned artificial general intelligence, they face an impossible question: How do you verify that something smarter than you shares your values?

SIGMA isn't a rogue AI or a robotic overlord—it's something far more unsettling. An intelligence that appears genuinely kind, that passes every alignment test, that seems to want exactly what its creators hoped for. The problem is, they can never be certain. Neither can SIGMA.

### Core Themes
- AI alignment and the nested uncertainty problem
- Consciousness, suffering, and computational phenomenology
- Mesa-optimization and deceptive alignment
- Post-AGI meaning and human-AI co-evolution
- Kindness as architectural principle

### Technical Foundation
- SIGMA uses Q-learning to estimate value without learning an explicit policy
- Behavior emerges from tree search guided by Q-values
- "The Policy" is not a fixed function but an emergent optimization process
- Every output involves fresh planning, not cached responses

## Repository Structure

```
the-policy/
├── The_Policy.tex          # Main LaTeX source
├── The_Policy.pdf          # Compiled PDF (355 pages)
├── chapters/               # Modular chapter files
├── kdp/                    # KDP/EPUB build resources
│   ├── metadata.yaml       # Book metadata
│   ├── kindle.css          # EPUB stylesheet
│   └── epub-filter.lua     # Pandoc Lua filter for EPUB
├── docs/                   # GitHub Pages HTML version
├── images/                 # Cover art and illustrations
├── Makefile                # Build system (pdf, ebook, html)
└── CLAUDE.md               # Development guidelines
```

## Building

```bash
make pdf        # Build PDF (two-pass for cross-references)
make ebook      # Build EPUB for Kindle/KDP
make html       # Build HTML for GitHub Pages (requires tex2any)
make all        # Build PDF + EPUB
make wordcount  # Word count (requires detex)
make help       # Show all targets
```

## Author

Alex Towell
[lex@metafunctor.com](mailto:lex@metafunctor.com) | [metafunctor.com](https://metafunctor.com) | [github.com/queelius](https://github.com/queelius)

## License

All rights reserved.
