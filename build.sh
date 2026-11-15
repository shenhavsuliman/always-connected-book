#!/usr/bin/env bash
# build.sh — בונה את הספר מאפס: גרפים → LaTeX → ביבליוגרפיה → PDF
# שימוש:  bash build.sh
set -e
cd "$(dirname "$0")"

echo "1/4  Python: images and graphs"
python python/make_images.py
python python/make_graphs.py

echo "2/4  XeLaTeX (pass 1)"
xelatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null

echo "3/4  Biber (bibliography)"
biber main > /dev/null

echo "4/4  XeLaTeX (passes 2-3: TOC, references)"
xelatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null
xelatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null

cp main.pdf book.pdf
python -c "import pymupdf; print('book.pdf:', pymupdf.open('book.pdf').page_count, 'pages')"
