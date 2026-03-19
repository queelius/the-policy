# Makefile for The Policy universe
# Builds PDF and EPUB for the novel and all short stories.
#
# Usage:
#   make            Build novel PDF + EPUB
#   make all        Build everything (novel + stories, PDF + EPUB)
#   make novel      Build novel PDF + EPUB
#   make stories    Build all short story PDFs + EPUBs
#   make hemorrhagic Build Hemorrhagic PDF + EPUB
#   make process    Build Process 12847 PDF + EPUB
#   make clean      Remove auxiliary files (preserve outputs)
#   make distclean  Remove all generated files
#   make wordcount  Word counts for all works
#   make help       Show all targets

# --- Configuration ---
PDFLATEX = pdflatex -interaction=nonstopmode
BIBTEX   = bibtex

# Novel
NOVEL_MAIN  = The_Policy
NOVEL_TEX   = $(NOVEL_MAIN).tex
NOVEL_PDF   = $(NOVEL_MAIN).pdf
NOVEL_EPUB  = $(NOVEL_MAIN).epub
NOVEL_DEPS  = $(NOVEL_TEX) $(wildcard chapters/*.tex)

# Short stories
HEMORRHAGIC_DIR  = stories/hemorrhagic
HEMORRHAGIC_TEX  = $(HEMORRHAGIC_DIR)/hemorrhagic.tex
HEMORRHAGIC_PDF  = $(HEMORRHAGIC_DIR)/hemorrhagic.pdf
HEMORRHAGIC_EPUB = $(HEMORRHAGIC_DIR)/hemorrhagic.epub

PROCESS_DIR  = stories/process-12847
PROCESS_TEX  = $(PROCESS_DIR)/process-12847.tex
PROCESS_PDF  = $(PROCESS_DIR)/process-12847.pdf
PROCESS_EPUB = $(PROCESS_DIR)/process-12847.epub

# Spinoffs (auto-discover any .tex files in stories/spinoffs/)
SPINOFF_TEX  = $(wildcard stories/spinoffs/*.tex)
SPINOFF_PDF  = $(SPINOFF_TEX:.tex=.pdf)
SPINOFF_EPUB = $(SPINOFF_TEX:.tex=.epub)

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
.PHONY: all novel stories spinoffs hemorrhagic process pdf epub ebook html \
        pdf-bib check clean distclean clean-novel clean-stories \
        wordcount wc-novel wc-stories help

# --- Aggregate targets ---
all: novel stories

novel: pdf epub

stories: hemorrhagic process spinoffs

# --- Novel PDF (two-pass) ---
pdf: $(NOVEL_PDF)

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

# --- Short stories (PDF + EPUB each) ---
hemorrhagic: $(HEMORRHAGIC_PDF) $(HEMORRHAGIC_EPUB)

$(HEMORRHAGIC_PDF): $(HEMORRHAGIC_TEX)
	cd $(HEMORRHAGIC_DIR) && $(PDFLATEX) hemorrhagic.tex && $(PDFLATEX) hemorrhagic.tex
	@echo "Built: $(HEMORRHAGIC_PDF)"

$(HEMORRHAGIC_EPUB): $(HEMORRHAGIC_TEX)
	pandoc $(HEMORRHAGIC_TEX) \
		-o $(HEMORRHAGIC_EPUB) \
		--mathml \
		-M title="Hemorrhagic" \
		-M author="Alex Towell"
	@echo "Built: $(HEMORRHAGIC_EPUB)"

process: $(PROCESS_PDF) $(PROCESS_EPUB)

$(PROCESS_PDF): $(PROCESS_TEX)
	cd $(PROCESS_DIR) && $(PDFLATEX) process-12847.tex && $(PDFLATEX) process-12847.tex
	@echo "Built: $(PROCESS_PDF)"

$(PROCESS_EPUB): $(PROCESS_TEX)
	pandoc $(PROCESS_TEX) \
		-o $(PROCESS_EPUB) \
		--mathml \
		-M title="Process 12847" \
		-M author="Alex Towell"
	@echo "Built: $(PROCESS_EPUB)"

# --- Spinoffs (auto-discovered from stories/spinoffs/*.tex) ---
spinoffs: $(SPINOFF_PDF) $(SPINOFF_EPUB)
	@if [ -z "$(SPINOFF_TEX)" ]; then \
		echo "No spinoff .tex files found yet (only design specs)."; \
	else \
		echo "Spinoffs built: $(SPINOFF_PDF) $(SPINOFF_EPUB)"; \
	fi

# Pattern rules for spinoffs
stories/spinoffs/%.pdf: stories/spinoffs/%.tex
	cd stories/spinoffs && $(PDFLATEX) $*.tex && $(PDFLATEX) $*.tex
	@echo "Built: $@"

stories/spinoffs/%.epub: stories/spinoffs/%.tex
	pandoc $< -o $@ --mathml -M author="Alex Towell"
	@echo "Built: $@"

# --- Word counts ---
wordcount: wc-novel wc-stories

wc-novel:
	@printf "%-30s " "The Policy (novel):"
	@if command -v detex >/dev/null 2>&1; then \
		detex $(NOVEL_TEX) 2>/dev/null | wc -w | tr -d ' '; \
	else \
		cat chapters/*.tex | wc -w | tr -d ' '; \
	fi

wc-stories:
	@printf "%-30s " "Hemorrhagic:"
	@cat $(HEMORRHAGIC_TEX) | wc -w | tr -d ' '
	@printf "%-30s " "Process 12847:"
	@cat $(PROCESS_TEX) | wc -w | tr -d ' '
	@echo ""
	@echo "Spec word counts:"
	@for f in stories/spinoffs/*-spec.md; do \
		name=$$(basename "$$f" -spec.md); \
		words=$$(wc -w < "$$f"); \
		printf "  %-28s %s\n" "$$name:" "$$words"; \
	done

# --- Clean ---
clean: clean-novel clean-stories
	@echo "Cleaned auxiliary files (outputs preserved)"

clean-novel:
	@for ext in $(AUX_EXTS); do rm -f *.$$ext; done
	@rm -f chapters/*.aux

clean-stories:
	@for ext in $(AUX_EXTS); do \
		rm -f $(HEMORRHAGIC_DIR)/*.$$ext; \
		rm -f $(PROCESS_DIR)/*.$$ext; \
		rm -f stories/spinoffs/*.$$ext; \
	done

distclean: clean
	rm -f $(NOVEL_PDF) $(NOVEL_EPUB)
	rm -f $(HEMORRHAGIC_PDF) $(HEMORRHAGIC_EPUB)
	rm -f $(PROCESS_PDF) $(PROCESS_EPUB)
	rm -f stories/spinoffs/*.pdf stories/spinoffs/*.epub
	rm -rf $(HTML_DIR)
	@echo "Cleaned all build artifacts"

# --- Help ---
help:
	@echo "The Policy Universe - Build System"
	@echo ""
	@echo "Novel:"
	@echo "  make novel       Build novel PDF + EPUB (default)"
	@echo "  make pdf         Build novel PDF (two-pass)"
	@echo "  make epub        Build novel EPUB"
	@echo "  make pdf-bib     Build novel PDF with bibliography"
	@echo "  make html        Build HTML for GitHub Pages"
	@echo "  make check       Quick single-pass compile"
	@echo ""
	@echo "Short stories:"
	@echo "  make stories     Build all story PDFs + EPUBs"
	@echo "  make hemorrhagic Build Hemorrhagic PDF + EPUB"
	@echo "  make process     Build Process 12847 PDF + EPUB"
	@echo "  make spinoffs    Build spinoff PDFs + EPUBs (auto-discovers .tex files)"
	@echo ""
	@echo "Utilities:"
	@echo "  make all         Build everything (novel + stories)"
	@echo "  make wordcount   Word counts for all works"
	@echo "  make clean       Remove auxiliary files"
	@echo "  make distclean   Remove all generated files"
	@echo "  make help        Show this message"
