---
name: qa-code
description: Checks the pythonbox code listings in the book — own background color, LTR frame, no line running past the box, readable font with Hebrew glyphs, line numbers, Hebrew comments that would jumble. Use as part of qa-super or after adding a \pythonfile listing.
---

# qa-code: code boxes (`pythonbox` / `\pythonfile`)

## Automatic part
`python qa/qa_check.py code` checks that the listing source exists, flags lines longer than 95 characters (wrap risk) and Hebrew comments inside the listed range, and confirms that the template builds the box LTR with its own `codebg` background.

## Visual part, for each listing
- The background is the light code color and **stays inside the frame**. It never runs past the page margin.
- No code line runs past the right edge. Long lines wrap with an indent (`breaklines`).
- The title bar is Hebrew and reads correctly. Code is left-to-right.
- Line numbers on the left are visible and do not overlap the frame.
- No empty boxes ("tofu") instead of letters. If they appear, the `tt` font lacks the glyphs (see INC-09).
- Hebrew comments do not jumble the line. Prefer English comments in listed code.

## Where fixes belong
- Background, frame or font → `connected.cls` (`pythonbox` style, `\babelfont{tt}`)
- Long or Hebrew comment lines → the Python file itself, or a different `firstline`/`lastline`
