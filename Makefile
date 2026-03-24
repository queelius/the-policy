# Makefile for The Policy universe
# Multi-work project: 1 novel, 10 stories (2 drafted, 8 in spec).
# Each story lives in stories/<name>/ with its own lore/ subdirectory.
# Shared lore in lore/ at project root.
#
# Story .tex files are auto-discovered. Drop a .tex in any stories/*/
# directory and `make stories` picks it up.

# --- Configuration ---
PDFLATEX = pdflatex -interaction=nonstopmode
BIBTEX   = bibtex

# Novel
NOVEL_MAIN  = The_Policy
NOVEL_TEX   = $(NOVEL_MAIN).tex
NOVEL_PDF   = $(NOVEL_MAIN).pdf
NOVEL_EPUB  = $(NOVEL_MAIN).epub
NOVEL_DEPS  = $(NOVEL_TEX) $(wildcard chapters/*.tex)

# Stories: auto-discover all .tex files in stories/*/
# Excludes stories/*/lore/ subdirectories
STORY_TEX   = $(wildcard stories/*/*.tex)
STORY_PDF   = $(STORY_TEX:.tex=.pdf)
STORY_EPUB  = $(STORY_TEX:.tex=.epub)

# EPUB settings (novel uses full KDP pipeline; stories use lightweight pandoc)
EPUB_META = kdp/metadata.yaml
EPUB_CSS  = kdp/kindle.css
EPUB_LUA  = kdp/epub-filter.lua

# HTML output
HTML_DIR = docs

# Aux file patterns
AUX_EXTS = aux log out toc bbl blg lof lot fls fdb_latexmk synctex.gz latexml.log

# --- Default ---
.DEFAULT_GOAL := novel

# --- Phony targets ---
.PHONY: all novel stories pdf print epub ebook html pdf-bib check \
        clean distclean clean-novel clean-stories \
        wordcount wc-novel wc-stories list help

# --- Aggregate targets ---
all: novel stories

novel: pdf epub print

stories: $(STORY_PDF) $(STORY_EPUB)
	@if [ -z "$(STORY_TEX)" ]; then \
		echo "No story .tex files found."; \
	else \
		echo "All stories built."; \
	fi

# --- Novel PDF (two-pass) ---
pdf: $(NOVEL_PDF)

# --- Print-ready PDF (6x9 trade paperback) ---
print: The_Policy_print.pdf

The_Policy_print.pdf: The_Policy_print.tex $(wildcard chapters/*.tex)
	$(PDFLATEX) The_Policy_print.tex
	$(PDFLATEX) The_Policy_print.tex
	@echo "Print PDF built: The_Policy_print.pdf ($(shell pdfinfo The_Policy_print.pdf 2>/dev/null | grep Pages | awk '{print $$2}') pages, 6x9)"

$(NOVEL_PDF): $(NOVEL_DEPS)
	$(PDFLATEX) $(NOVEL_TEX)
	$(PDFLATEX) $(NOVEL_TEX)
	@echo "Novel PDF built: $(NOVEL_PDF)"

# Novel PDF with bibliography
pdf-bib: $(NOVEL_DEPS)
	$(PDFLATEX) $(NOVEL_TEX)
	$(BIBTEX) $(NOVEL_MAIN)
	$(PDFLATEX) $(NOVEL_TEX)
	$(PDFLATEX) $(NOVEL_TEX)

# Quick single-pass compile for editing
check: $(NOVEL_DEPS)
	$(PDFLATEX) $(NOVEL_TEX)
	@echo "Quick compile done (run 'make pdf' for full build)"

# --- Novel EPUB ---
epub: $(NOVEL_EPUB)
ebook: epub

$(NOVEL_EPUB): $(NOVEL_DEPS) $(EPUB_CSS) $(EPUB_META)
	pandoc $(NOVEL_TEX) \
		-o $(NOVEL_EPUB) \
		--toc \
		--toc-depth=1 \
		--split-level=1 \
		--mathml \
		--css=$(EPUB_CSS) \
		--metadata-file=$(EPUB_META) \
		--epub-title-page=true \
		--lua-filter=$(EPUB_LUA)
	@echo "EPUB built: $(NOVEL_EPUB)"

# --- Novel HTML (GitHub Pages) ---
html: $(NOVEL_DEPS)
	@rm -rf $(HTML_DIR)
	tex2html $(NOVEL_TEX) -f html -o $(HTML_DIR) --theme clean
	@echo "HTML built: $(HTML_DIR)/index.html"

# --- Pattern rules for all stories ---
# PDF: compile in the story's directory
stories/%.pdf: stories/%.tex
	cd $(dir $<) && $(PDFLATEX) $(notdir $<) && $(PDFLATEX) $(notdir $<)
	@echo "Built: $@"

# EPUB: pandoc from .tex
stories/%.epub: stories/%.tex
	pandoc $< -o $@ --mathml -M author="Alex Towell"
	@echo "Built: $@"

# --- Word counts ---
wordcount: wc-novel wc-stories

wc-novel:
	@printf "%-35s " "The Policy (novel):"
	@if command -v detex >/dev/null 2>&1; then \
		detex $(NOVEL_TEX) 2>/dev/null | wc -w | tr -d ' '; \
	else \
		cat chapters/*.tex | wc -w | tr -d ' '; \
	fi

wc-stories:
	@echo ""
	@echo "Drafted stories:"
	@for f in $(STORY_TEX); do \
		name=$$(echo "$$f" | sed 's|stories/||' | sed 's|/.*||'); \
		words=$$(wc -w < "$$f"); \
		printf "  %-33s %s\n" "$$name:" "$$words"; \
	done
	@echo ""
	@echo "Design specs (not yet drafted):"
	@for f in stories/*/spec.md; do \
		name=$$(echo "$$f" | sed 's|stories/||' | sed 's|/.*||'); \
		words=$$(wc -w < "$$f"); \
		printf "  %-33s %s\n" "$$name:" "$$words"; \
	done 2>/dev/null || true

# --- List all works ---
list:
	@echo "The Policy Universe"
	@echo ""
	@echo "Novel:"
	@printf "  %-35s %s\n" "The Policy" "chapters/ ($(words $(wildcard chapters/*.tex)) files)"
	@echo ""
	@echo "Stories (drafted):"
	@for f in $(STORY_TEX); do \
		name=$$(echo "$$f" | sed 's|stories/||' | sed 's|/.*||'); \
		printf "  %-35s %s\n" "$$name" "$$f"; \
	done
	@echo ""
	@echo "Stories (spec only):"
	@for d in stories/*/; do \
		if [ ! -f "$$d"*.tex ] 2>/dev/null && [ -f "$$d/spec.md" ]; then \
			name=$$(basename "$$d"); \
			printf "  %-35s %s\n" "$$name" "spec.md"; \
		fi; \
	done 2>/dev/null || true

# --- Clean ---
clean: clean-novel clean-stories
	@echo "Cleaned auxiliary files (outputs preserved)"

clean-novel:
	@for ext in $(AUX_EXTS); do rm -f *.$$ext; done
	@rm -f chapters/*.aux

clean-stories:
	@for ext in $(AUX_EXTS); do \
		find stories -name "*.$$ext" -delete 2>/dev/null; \
	done

distclean: clean
	rm -f $(NOVEL_PDF) $(NOVEL_EPUB)
	rm -f $(STORY_PDF) $(STORY_EPUB)
	rm -rf $(HTML_DIR)
	@echo "Cleaned all build artifacts"

# --- Help ---
help:
	@echo "The Policy Universe -- Build System"
	@echo ""
	@echo "Novel:"
	@echo "  make novel       Build novel PDF + EPUB (default)"
	@echo "  make pdf         Build novel PDF (two-pass)"
	@echo "  make epub        Build novel EPUB"
	@echo "  make pdf-bib     Build novel PDF with bibliography"
	@echo "  make html        Build HTML for GitHub Pages"
	@echo "  make check       Quick single-pass compile"
	@echo ""
	@echo "Stories:"
	@echo "  make stories     Build all story PDFs + EPUBs"
	@echo "  make stories/<name>/<name>.pdf  Build one story"
	@echo ""
	@echo "Utilities:"
	@echo "  make all         Build everything (novel + stories)"
	@echo "  make list        Show all works and their status"
	@echo "  make wordcount   Word counts for all works"
	@echo "  make clean       Remove auxiliary files"
	@echo "  make distclean   Remove all generated files"
	@echo "  make help        Show this message"
