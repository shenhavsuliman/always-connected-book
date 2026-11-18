---
name: qa-table
description: Checks tables in the Hebrew LaTeX book — first column on the right, caption above with label, booktabs rules, width inside the text block, header row styling, numbers marked LTR. Use as part of qa-super or after adding a table.
---

# qa-table: tables

## Automatic part
`python qa/qa_check.py table` checks that the caption is above, `\label` exists and booktabs rules are used.

## Visual part, for each table
- The **first column is on the right**. It is never mirrored by hand.
- The table width stays inside the text block. No overfull box from a `tabular` (cross-check `qa-typeset`).
- The caption is **above**, in Hebrew, with "טבלה N.M." in turquoise.
- Every number, year and range inside the table is LTR (`\num{}`), and every English name uses `\en{}`.
- No row is split across pages. Long cells wrap inside an `X` or `p{}` column.
- The table is referenced in the text (`טבלה~\ref{...}`).

## Where fixes belong
- Width or first-column problems that repeat → template (`layout=tabular` in `connected.cls`)
- One table's column spec → that chapter file
