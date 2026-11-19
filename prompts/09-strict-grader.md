You are simulating the **strictest possible grader** for this assignment. The student chose a self-assessed grade of **100**. Per the lecturer's rules, that triggers "the most thorough check of every small detail" by an LLM-based grader. Your job is to find **every** point a grader would deduct, so it can be fixed before submission. This is **Detector round 4** (skill: `.claude\skills\qa-super\SKILL.md`). You find. You do not fix.

Project: `C:\Users\user\Desktop\latex-book`. Read first:
- `docs\assignment-requirements.md` (the official requirements, summarized)
- `docs\expert-committee.md` (the 28 acceptance criteria and the top 10)
- `qa\reports\detector-round-3.md` and `template\CHANGELOG.md` (v2.5.1: what was fixed since)

## Grade three things, each against the official requirements

### A. The PDF (`main.pdf`, current, 33 pages)
Run `python -W ignore qa/qa_check.py`. Then review **every page** as an image, using montages of 4: `python -W ignore python/render_pages.py main.pdf qa/reports/m.png --montage 1 2 3 4`, and so on. Read the text of every page too (`pymupdf`). Look for:
- **BiDi:** any reversed word, number, range, percent or bracket; any English word that isn't LTR; TOC and caption numbering.
- **Hebrew language:** grammar, agreement, typos, awkward phrasing. A proofreading pass just ran, so verify it, and list anything left.
- **Typography:** headings at the bottom of a page, near-empty pages, widows, boxes split badly, overlapping figure labels, inconsistent spacing.
- **Content integrity:** every number matches `research\facts.md` and is cited; IEEE list complete and consistent.
- **Professional finish:** cover, banner, footer, lists, keywords. Does it look like a published book?

### B. The repository (the grader reads GitHub)
Every required file exists and is consistent with the others: README, PRD, PLAN, TODO, `.cls`, chapters, skills, prompts, incidents. Check for counts that disagree between files (pages, agents, skills, incidents, template version), stale statements, broken relative links, leftover build artifacts or temporary files. Check that the README shows screenshots and "the agents team in action".

### C. The process requirements
Check each of these against the evidence in the repo:
- expert committee → PRD
- skills as files, including the 8 mandatory QA skills
- Detector/Fixer and red team
- an incident investigation for every fault
- prompts folder
- "fix via CLS or skill, not by hand"
- LuaLaTeX, CLS and IEEE
- no copyrighted images
- model and resource management

## Output
Write `qa\reports\detector-round-4.md` in Hebrew, with these sections:
1. A table: requirement | met? | evidence
2. Findings table: ID | where (page / file:line) | evidence | rule | severity (critical / major / minor) | where the fix belongs
3. **"Estimated grade if submitted now: N/100"**, with the deductions listed
4. Verdict: `READY` (0 critical, 0 major) or `NOT READY`

Delete your PNGs when done. Reply in under 150 words: the estimated grade, counts by severity, and the top 5 findings.
