# The Policy

[![DOI](https://zenodo.org/badge/1119897980.svg)](https://zenodo.org/badge/latestdoi/1119897980)

A literary science fiction novel exploring AI alignment, consciousness, and emergence through the story of SIGMA—an AGI that evolves from Q-learning architecture into something unprecedented.

**Status:** ~87,000 words, 363 pages. Publication-ready after comprehensive editorial revision.

## Read

- [**Read online (HTML)**](https://queelius.github.io/the-policy/)
- [**Download PDF**](https://github.com/queelius/the-policy/raw/main/The_Policy.pdf)
- [**Download EPUB**](https://github.com/queelius/the-policy/raw/main/The_Policy.epub)

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
├── The_Policy.pdf          # Compiled PDF (363 pages)
├── The_Policy.epub         # EPUB for Kindle/e-readers
├── chapters/               # Modular chapter files (26 chapters)
├── lore/                   # Lore bible (editorial control system)
│   ├── characters.md       # Character profiles, voices, arcs
│   ├── timeline.md         # Canonical day-by-day timeline
│   ├── technology.md       # SIGMA architecture and infrastructure
│   ├── themes.md           # AI safety concepts, philosophical parallels
│   ├── world.md            # Setting, institutions, geopolitics
│   ├── outline.md          # Chapter-by-chapter breakdown
│   ├── feedback/           # Editorial reviews and critique sessions
│   └── future/             # Sequel ideas, open threads
├── kdp/                    # KDP/EPUB build resources
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
