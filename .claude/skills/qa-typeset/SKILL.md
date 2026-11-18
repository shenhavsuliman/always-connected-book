---
name: qa-typeset
description: Reads the LuaLaTeX log of the book and reports errors, undefined references or citations, overfull/underfull hbox and vbox warnings, widows/orphans and headings stranded at page bottom. Use as part of qa-super or after every build.
---

# qa-typeset: compile warnings and page layout

## Automatic part
`python qa/qa_check.py typeset` parses `main.log`:
- every line that starts with `!` → **critical**
- undefined reference or citation → **critical**
- `Overfull \hbox` wider than **5pt** → **major** (with source line numbers)
- `Overfull \vbox` → **major**

## Visual part (course guide, §19.4)
- A section heading never sits in the bottom four lines of a page.
- No single line or word is stranded at the top of a page (widow).
- No box or table splits awkwardly across pages.
- There are no nearly empty pages, except before a new chapter.
- The TOC, abstract, each chapter and the bibliography start on a new page.

## Where fixes belong
- Spacing or float policy that repeats → `connected.cls`
- One long word or URL → that sentence (rephrase, or `\allowbreak`)
- Known benign warning (for example listings' internal paragraph width) → document it in `qa/known-warnings.md` with the reason. Never ignore one silently.
