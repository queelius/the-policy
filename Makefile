# Makefile for The Policy LaTeX manuscript
# Targets: pdf, ebook, html, clean, all

MAIN = The_Policy
TEX2ANY = tex2any
PDFLATEX = pdflatex
BIBTEX = bibtex
EPUB = $(MAIN).epub
METADATA = kdp/metadata.yaml
CSS = kdp/kindle.css

# Output directories
HTML_DIR = docs

# LaTeX auxiliary files to clean
AUX_FILES = *.aux *.log *.out *.toc *.bbl *.blg *.lof *.lot *.fls *.fdb_latexmk *.synctex.gz *.latexml.log
CHAPTER_AUX = chapters/*.aux

.PHONY: all pdf ebook html clean clean-aux clean-all help wordcount check

# Default target
all: pdf ebook

# --- Ebook (Kindle via EPUB) ---
ebook: $(EPUB)

$(EPUB): $(MAIN).tex chapters/*.tex $(CSS) $(METADATA)
	pandoc $(MAIN).tex \
		-o $(EPUB) \
		--toc \
		--toc-depth=1 \
		--split-level=1 \
		--mathml \
		--css=$(CSS) \
		--metadata-file=$(METADATA) \
		--epub-title-page=true \
		--lua-filter=kdp/epub-filter.lua
	@echo "EPUB built: $(EPUB)"
	@echo "Test with: Kindle Previewer 3 or Calibre"

# --- PDF (two-pass for cross-references) ---
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

# --- Utilities ---
clean-aux:
	rm -f $(AUX_FILES)
	rm -f $(CHAPTER_AUX)

clean: clean-aux
	@echo "Cleaned auxiliary files (outputs preserved)"

# Remove everything including PDF, EPUB, and HTML
clean-all: clean-aux
	rm -f $(MAIN).pdf
	rm -f $(EPUB)
	rm -rf $(HTML_DIR)
	@echo "Cleaned all build artifacts"

# Word count
wordcount:
	@detex $(MAIN).tex 2>/dev/null | wc -w || \
		echo "Install detex for accurate word count"

# Quick check - just compile once (faster for editing)
check:
	$(PDFLATEX) -interaction=nonstopmode $(MAIN).tex
	@echo "Quick compile done (run 'make pdf' for full build)"

# Help target
help:
	@echo "Available targets:"
	@echo "  make all      - Build PDF + EPUB (default)"
	@echo "  make pdf      - Build PDF (two-pass compilation)"
	@echo "  make pdf-bib  - Build PDF with bibliography"
	@echo "  make ebook    - Build EPUB for Kindle/KDP"
	@echo "  make html     - Build HTML using tex2any"
	@echo "  make wordcount- Count words (requires detex)"
	@echo "  make check    - Quick single-pass compile"
	@echo "  make clean    - Remove auxiliary files (preserves PDF, EPUB, HTML)"
	@echo "  make clean-all- Remove everything including outputs"
	@echo "  make clean-aux- Remove only auxiliary files"
	@echo "  make help     - Show this help message"
