You are the **Editor** (skill `.claude\skills\book-editor\SKILL.md`) and, for one task, the **Researcher** (skill `.claude\skills\book-researcher\SKILL.md`) for the Hebrew book in `C:\Users\user\Desktop\latex-book`. A strict grader simulation (Detector round 4) graded the book 82/100. Its report is `qa\reports\detector-round-4.md`. Read it. You own **only the content findings** below. The Master handles the template, figures and documentation.

## Your findings
1. **DATA-01:** 1844 (Morse's first public telegram), October 1969 (the first ARPANET message) and 1973 (Martin Cooper's first handheld mobile call) appear in `chapters\02-history.tex` (text and Table 2.1) without a citation.
   - Use web search to find **one real, verifiable source for each**, for example the Library of Congress "Today in History, May 24" page, an authoritative history of the internet such as Leiner et al. (2009) in ACM SIGCOMM CCR, and a Motorola or Guinness World Records page for Cooper.
   - Add the entries to `refs.bib`, using `@online` with `date` and `urldate` where it applies, and `\parencite` them in the text and the table.
   - Update `research\facts.md` to mark them verified.
   - Never invent anything. If you can't verify a fact, rephrase it without the exact date.
2. **BIB-01:** in `refs.bib`, protect proper nouns and months with braces (e.g., `{November}`, `{Internet}`) so IEEE keeps their capitals. Give every `@online` entry a publication `date` (year, or year-month) where the source states one.
3. **LANG-02:** "סינתזה של מחבר הספר" in `chapters\04-attention.tex:36` and in the caption in `chapters\figures\attention-loop.tex:41`. The book speaks in first-person plural, so write "הסינתזה שלנו" (or similar) in both places.
4. **LANG-03:**
   - "הקלקה" → "לחיצה" (`01-intro.tex:55`, `04-attention.tex:47`)
   - "כשש עשרה שעות ערות" → a correct phrasing (`03-digital-day.tex:147`)
   - "ועד כארבע שעות ויותר" → not contradictory (`05-wellbeing.tex:133`)
   - the "ציידת-לקטת" image repeats in `01-intro.tex:31` and `02-history.tex:64`: keep it once, rephrase the other
5. **CONT-01:** Table 2.1 must be chronological. Place "שנות ה-2000 וה-2010" correctly relative to 2007, or change the row so the order is clear.
6. **CONT-02:** in Table 3.1, the "time" column has a text value ("יותר משלוש שעות"). Make it consistent, e.g. `\num{>3:00}` plus a table note, keeping the meaning.
7. **CONT-03:** `chapters\03-digital-day.tex` near line 189 cites 5.35bn (DataReportal, start of 2024), and elsewhere the book uses 5.87bn and 5.5bn (ITU). Add one clause explaining that DataReportal and ITU are different sources with different dates and methods.
8. **CONT-04:** in `chapters\06-smart-home.tex`, the book is dated November 2026, so don't call 2025 a "forecast" without saying the forecast was published in October 2025. Fix the heading "כעשרים מיליארד" so it matches the last measured value (18.5bn in 2024) or say it is a forecast.
9. **LAYOUT-03 (content order):** in `chapters\09-appendix-code.tex`, move the factbox "איך משחזרים את הספר" so it comes **before** the `\pythonfile` line, right after the intro paragraph. The page after the code box then won't be nearly empty.

## Rules
- Edit only `chapters\*.tex`, `chapters\figures\attention-loop.tex` (caption only), `refs.bib` and `research\facts.md`. Use your file-editing tool, never Python or heredoc string literals (INC-05).
- Use only `connected.cls` commands. Write every year or number next to Hebrew as `\num{...}`.
- Do not compile. Do not touch `connected.cls`, `python\`, `qa\` or the docs.
- Append "## סבב 4: תיקוני תוכן (Detector 4)" to `research\editor-report.md`: ID | what changed | file.

Reply in under 120 words: the 3 sources you added (title and URL) and anything you couldn't fix.
