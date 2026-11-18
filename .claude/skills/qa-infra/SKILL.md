---
name: qa-infra
description: Checks that the LaTeX project has the required structure for submission — main.tex, one .tex per chapter, connected.cls, refs.bib, PRD.md, PLAN.md, TODO.md, README.md, the skills folder, prompts folder, the final PDF, a single-command build, and no stray files. Use as part of qa-super or before committing.
---

# qa-infra: project structure

## Automatic part
`python qa/qa_check.py infra` checks the required files and the chapter count, confirms that every chapter is `\input` in `main.tex`, counts the skills in `.claude/skills/`, and flags stray files such as old `.sty` or `_test*`.

## Also check by hand
- `bash build.sh` rebuilds `book.pdf` from a clean checkout (reproducibility).
- `.gitignore` excludes build artifacts (`*.aux`, `*.log`, `main.pdf`, `node_modules/`) but **keeps** `book.pdf`.
- `prompts/` holds every agent prompt. `docs/incidents.md` holds the incident investigations.
- The repository is **new** (not the one from assignment 01) and is public or shared with the lecturer.
- No secrets, tokens or personal files are in the repository.
