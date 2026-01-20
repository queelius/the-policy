# Makefile for The Policy LaTeX manuscript
# Targets: pdf, html, clean, all

MAIN = The_Policy
TEX2ANY = tex2any
PDFLATEX = pdflatex
BIBTEX = bibtex

# Output directories
HTML_DIR = docs

# LaTeX auxiliary files to clean
AUX_FILES = *.aux *.log *.out *.toc *.bbl *.blg *.lof *.lot *.fls *.fdb_latexmk *.synctex.gz *.latexml.log
CHAPTER_AUX = chapters/*.aux

.PHONY: all pdf html clean clean-aux help

# Default target
all: pdf

# Build PDF (two-pass for cross-references)
pdf: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex chapters/*.tex
	$(PDFLATEX) -interaction=nonstopmode $(MAIN).tex
	$(PDFLATEX) -interaction=nonstopmode $(MAIN).tex

# Build PDF with bibliography (if needed)
pdf-bib: $(MAIN).tex chapters/*.tex
	$(PDFLATEX) -interaction=nonstopmode $(MAIN).tex
	$(BIBTEX) $(MAIN)
	$(PDFLATEX) -interaction=nonstopmode $(MAIN).tex
	$(PDFLATEX) -interaction=nonstopmode $(MAIN).tex

# Build HTML using tex2any
html: $(MAIN).tex chapters/*.tex
	@rm -rf $(HTML_DIR)
	$(TEX2ANY) $(MAIN).tex -f html -o $(HTML_DIR) --theme clean
	@echo "HTML generated at $(HTML_DIR)/index.html"

# Clean auxiliary files only
clean-aux:
	rm -f $(AUX_FILES)
	rm -f $(CHAPTER_AUX)

# Full clean (aux + generated outputs)
clean: clean-aux
	rm -f $(MAIN).pdf
	rm -rf $(HTML_DIR)

# Help target
help:
	@echo "Available targets:"
	@echo "  make pdf      - Build PDF (default, two-pass compilation)"
	@echo "  make pdf-bib  - Build PDF with bibliography"
	@echo "  make html     - Build HTML using tex2any"
	@echo "  make clean    - Remove all generated files"
	@echo "  make clean-aux- Remove only auxiliary files"
	@echo "  make all      - Build PDF (same as 'make pdf')"
	@echo "  make help     - Show this help message"
