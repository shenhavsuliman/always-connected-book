You are the **Editor/Researcher** (skills `.claude\skills\book-editor\SKILL.md` and `.claude\skills\book-researcher\SKILL.md`) for the Hebrew book in `C:\Users\user\Desktop\latex-book`. The strict grader simulation (round 5, `qa\reports\detector-round-5.md`) now estimates 91/100. Read the report. You own **only these content findings**. The Master does the template, graphs, figure 6.1 and the docs.

1. **DATA-02:** chapter 5 says the tipping points come from the Oxford Internet Institute press release, but cites only the paper. Use web search to find the real OII press release (January 2017) about Przybylski & Weinstein's "Goldilocks" study and add it to `refs.bib` (`@online`, with author/organization, title, date, url, urldate). Cite it where the tipping points are given (ch. 5, the `fig-goldilocks` caption, and the appendix if it mentions the press release). Keep the paper citation too. Never invent anything.
2. **Chapter 1 chapter list:** the roadmap in `chapters\01-intro.tex` numbers the chapters 1–7, but they are chapters 2–8. Use `\ref` to chapter labels if they exist (see `\label{ch:...}` in the chapter files), otherwise fix the numbers.
3. **Hebrew slips (round 5):**
   - mixed tenses in ch. 6
   - in ch. 5, β0 "היא" against β1/β2 "מתאר": make the symbol descriptions consistent
   - the attention-loop figure (`chapters\figures\attention-loop.tex`) addresses the reader in the singular ("הקשב שלך", "יחזיק אותך"), but the book uses the plural ("אתם"): change the node labels to plural, keeping the `\heb{}` wrappers and the structure
   - a box title with straight ASCII quotes: use Hebrew quotation marks
   - anything else in the report's minor LANG/CONT findings that is content (not template or docs)
4. **Figure 2.1 annotation:** the caption or text states the COVID cause as fact, while elsewhere it is "our interpretation". Make the caption consistent with the text, as an interpretation.
5. **BIB-01:** biblatex-ieee does not print the publication `date` of `@online` entries. For each `@online` entry whose source has a known publication date, make the date appear in the bibliography in a way IEEE accepts. For example, add `note = {Published Jan. 9, 2007}`, or use `@misc` with `howpublished = {Online}` plus `url` and `date`. Keep it consistent across all entries.

## Rules
- Edit only `chapters\*.tex`, `chapters\figures\*.tex` (captions and node text only), `refs.bib` and `research\facts.md`. Use your file-editing tool only, never Python or heredoc string literals (INC-05).
- Use only `connected.cls` commands. Put numbers next to Hebrew in `\num{}`.
- Do not compile. Do not touch the template, `python\` or the docs.
- Append "## סבב 5: תיקוני תוכן" to `research\editor-report.md` (with the file-editing tool): ID | change | file.

Reply in under 100 words: the OII source (title and URL), plus anything you couldn't fix.
