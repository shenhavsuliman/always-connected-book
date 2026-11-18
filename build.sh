#!/usr/bin/env bash
# build.sh — בונה את הספר מאפס: גרפים → LaTeX → ביבליוגרפיה → PDF
# שימוש:  bash build.sh
set -e
cd "$(dirname "$0")"

echo "1/4  Python: images and graphs"
python python/make_images.py
python python/make_graphs.py

echo "2/4  LuaLaTeX (pass 1)"
lualatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null

echo "3/4  Biber (bibliography)"
biber main > /dev/null

echo "4/4  LuaLaTeX (passes 2-3: TOC, references)"
lualatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null
lualatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null

cp main.pdf book.pdf
rm -f ./*.pysnip   # INFRA-02: temporary code snippets written by connected.lua
python -c "import pymupdf; print('book.pdf:', pymupdf.open('book.pdf').page_count, 'pages')"

# bash build.sh test -> also compile the template stress test (tests/stress-test.tex)
if [ "$1" = "test" ]; then
  echo "test: stress-test.tex"
  lualatex -interaction=nonstopmode -halt-on-error -output-directory=tests tests/stress-test.tex > /dev/null
  biber tests/stress-test > /dev/null
  lualatex -interaction=nonstopmode -halt-on-error -output-directory=tests tests/stress-test.tex > /dev/null
  echo "stress test OK"
fi
