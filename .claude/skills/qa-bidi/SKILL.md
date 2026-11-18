---
name: qa-bidi
description: Checks RTL/LTR correctness in the Hebrew/English book PDF — reversed English words, flipped numbers/ranges/decimals, mirrored brackets in citations, Hebrew inside English units, TOC numbering, headers and footers. Use as part of qa-super or whenever mixed Hebrew/English text is added.
---

# qa-bidi: Hebrew/English direction

## Automatic part
`python qa/qa_check.py bidi`. It catches Hebrew words starting with a final letter (ךםןףץ), glued/reversed ranges and mirrored `]n[` citations.

## Visual part: on every page image, look for
| What you see | Cause | Where the fix belongs |
|---|---|---|
| English word or acronym reversed (e.g. NOSJ) | word not marked | wrap in `\en{}` in the chapter |
| several English words in wrong order | phrase not marked as one unit | one `\en{...}` around the whole phrase |
| `0.1` instead of `1.0`, `02-01` instead of `10-20` | number/range not one unit | `\num{}` |
| `]1[` or `)ITU, 2026(` | citation not LTR | template: `\parencite` wrapper in `connected.cls` |
| Hebrew inside an English unit reversed | Hebrew placed inside `\en{}` | move the Hebrew outside the `\en{}` |
| Hebrew word order reversed inside a TikZ node | node built in RTL | `ltrpicture` + `\heb{}` (template) |
| box frame shifted, title missing | box built in RTL | template: boxes are LTR frames with Hebrew content |
| section numbers `1.2` instead of `2.1` in TOC | counter direction | template |
| Hebrew inside a formula reversed | missing `\mathheb{}` | `\mathheb{}` |

## Rules (from the course guide, Prompt B1)
1. Every English word, name and acronym is marked as English.
2. A multi-word English phrase is one unit.
3. Every number, decimal, range, percent, date, currency amount and version is one LTR unit, with its symbol.
4. Never put Hebrew inside an English-marked unit.
5. Hebrew inside a formula uses `\mathheb{}`.
6. Every diagram and every code box is built in an English environment: the frame is LTR and the content is RTL.
7. In tables, the first column is on the right.
8. Use only the template's commands. Do not invent new ones.

**Never "fix" reversed Hebrew by typing it backwards.** Fix the direction marking.
