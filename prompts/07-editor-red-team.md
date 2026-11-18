You are the **Editor** (skill: `C:\Users\user\Desktop\latex-book\.claude\skills\book-editor\SKILL.md`) for the Hebrew book in `C:\Users\user\Desktop\latex-book`. A strict red-team examiner reviewed the finished book. Its report is `qa\reports\red-team.md`. Read it fully, and read `research\facts.md` and `refs.bib`.

The Master decided to address the **substantive** points (argument and evidence) in the chapter files:

1. **The Goldilocks model (ch. 5, ch. 8, appendix):**
   - Say explicitly that the curves are **constructed** to peak at the reported tipping points (b1 = 2·b2·t*), and that their equal height is a normalization, not a finding.
   - Say that the real measured effect is **small** (Orben & Przybylski 2019).
   - Say that the tipping points come from the Oxford Internet Institute's press release on the paper. The computer/video mapping has medium confidence, as facts.md notes.
   - Soften "המחקר תומך" and similar phrases to wording that matches the evidence.
2. **Unsourced or stretched claims:** for each one the report lists (online time "more than work or sleep", hunter-gatherer claims, the IoT vs. internet-users comparison and so on), either cite a source from refs.bib that really supports it, rephrase it as clearly the author's reflection or arithmetic, or remove it.
3. **The 8-step attention loop (ch. 4 and the caption of `chapters\figures\attention-loop.tex`):** steps 1–4 are Eyal's Hook model. Steps 5–8 are **the author's synthesis**, inspired by Zuboff's idea of behavioral surplus. Make the text and the caption say exactly that.
4. **Contradiction:** the "unfair fight" claim in ch. 7 vs. the "not a conspiracy" box in ch. 4. Make them consistent.
5. **Ch. 7 tips:** where a tip has no evidence, frame it honestly as a practical suggestion, not a research result. Where Newport, Haidt or Przybylski & Weinstein do support it, cite them.
6. **Repetition:** the Haidt vs. Orben debate appears three times, and 5.87bn / 6:40 appear in six places. Keep the full discussion once (ch. 5) and refer back to it elsewhere briefly. Keep the numbers where they do work (abstract, first use, summary) and cut the rest.

## Rules
- Edit only `chapters\*.tex` and the caption in `chapters\figures\attention-loop.tex`. Use your file-editing tool, never Python string literals or heredocs (see INC-05).
- Use only `connected.cls` commands (see `template\COMMANDS.md`): `\en{}`, `\num{}`, `\parencite{}`, `\textcite{}`, and the box environments. Use only cite keys that exist in refs.bib.
- Keep the Harari-inspired voice. Keep each chapter's length roughly the same. Don't touch structure, labels or figures.
- Do not compile. The Master rebuilds the book.
- Append a section "## סבב 2: תיקוני צוות אדום" to `research\editor-report.md` with a table: red-team point | decision (fixed / rephrased / removed / kept + reason) | file.

Reply in under 150 words: what changed, and any point you decided to keep, with the reason.
