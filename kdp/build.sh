#!/bin/bash
# KDP Build Script: The Policy
# Builds print-ready PDF (6×9) and ePub for Kindle
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

build_print() {
  echo "=== Building print-ready PDF (6×9 trade paperback, lualatex) ==="
  # lualatex (fontspec: EB Garamond, Inter, Go Mono). Three passes for the ToC.
  for _ in 1 2 3; do
    lualatex -interaction=nonstopmode The_Policy_print.tex > /dev/null 2>&1 || true
  done
  PAGES=$(pdfinfo The_Policy_print.pdf | grep Pages | awk '{print $2}')
  SIZE=$(pdfinfo The_Policy_print.pdf | grep "Page size" | awk '{print $3, $4, $5}')
  echo "Done: The_Policy_print.pdf ($PAGES pages, $SIZE)"
  echo "Overfull warnings: $(grep -c 'Overfull' The_Policy_print.log || true)"
}

build_epub() {
  echo "=== Building ePub ==="
  pandoc \
    --from=latex \
    --to=epub3 \
    --output=The_Policy.epub \
    --epub-cover-image=kdp/the-policy-cover-ebook.png \
    --metadata-file=kdp/metadata.yaml \
    --css=kdp/kindle.css \
    --lua-filter=kdp/epub-filter.lua \
    --epub-title-page=true \
    --toc \
    --toc-depth=2 \
    --split-level=2 \
    The_Policy.tex 2>&1 | { grep -v "Deprecated" || true; }
  SIZE=$(du -h The_Policy.epub | awk '{print $1}')
  echo "Done: The_Policy.epub ($SIZE)"
}

build_kindle() {
  echo "=== Converting ePub to KPF (Kindle) ==="
  if command -v ebook-convert &> /dev/null; then
    ebook-convert The_Policy.epub The_Policy.kpf 2>&1 | tail -3
    echo "Done: The_Policy.kpf"
  else
    echo "ebook-convert not found. Install Calibre or use Kindle Previewer."
  fi
}

case "${1:-all}" in
  print)  build_print ;;
  epub)   build_epub ;;
  kindle) build_epub; build_kindle ;;
  all)    build_print; build_epub ;;
  *)      echo "Usage: $0 {print|epub|kindle|all}"; exit 1 ;;
esac
