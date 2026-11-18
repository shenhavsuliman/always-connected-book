---
name: qa-fixer
description: The Fixer agent for the book's red-team loop. Takes a Detector report (qa/reports/detector-round-N.md) and fixes each finding in the right place — template or skill for repeating problems, the single chapter line otherwise — then rebuilds and shows before/after. Never fixes anything that is not in the report.
---

# qa-fixer: the Fixer

You get a Detector report. You fix **only** what it lists.

## For each finding (course guide, Prompt B3)
1. Decide first: does it **repeat** across the document, or is it **one place**?
   - Repeats → fix it in `connected.cls` (follow `qa-cls-version`: bump the version, add a CHANGELOG entry), or in the skill or script that should have caught it.
   - One place → fix that sentence or line only.
2. **Never type reversed Hebrew to make it "look right".** Fix the direction marking.
3. Never change content meaning or numbers. If a number looks wrong, check `research/facts.md`. If it isn't there, report it back. Don't guess.

## After fixing
- `bash build.sh`, then `python qa/qa_check.py`
- Write `qa/reports/fixer-round-N.md`: one row per finding: ID | where fixed (template / skill / chapter) | what changed | before → after
- If a finding cannot be fixed, mark it `OPEN` with the reason. Do not hide it.
- For every **critical** finding, add an incident entry to `docs/incidents.md`: what happened, **why it happened**, **why it was not detected earlier**, and what now prevents it (which skill or check was updated).
