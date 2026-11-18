---
name: qa-cls-version
description: Verifies the book uses the standard version of connected.cls, that the version has a CHANGELOG entry and the COMMANDS list is current, and that chapter files use only commands the template defines (no polyglossia-era \RL, \LR, \textenglish). Use as part of qa-super, after any template change, and before fixing a repeating problem.
---

# qa-cls-version: template version

## Automatic part
`python qa/qa_check.py cls-version` checks that:
- `\ConnectedVersion` in `connected.cls` equals the standard version (`REQUIRED_CLS` in `qa/qa_check.py`)
- `template/CHANGELOG.md` has a `## vX.Y.Z` entry for that version
- no chapter uses commands from the old engine: `\RL{`, `\LR{`, `\textenglish`, `polyglossia`

## Before any fix to a repeating problem (course guide, Prompt C2)
1. Check the template version against the standard version.
2. Search `template/CHANGELOG.md`: was this already fixed?
3. If yes, upgrade the template and recompile. **Do not edit the text.**
4. If no, propose one fix in the template, and say which documents it affects, before changing anything.

## When the template changes
- Raise `\ConnectedVersion` (patch for a fix, minor for a new command).
- Add a CHANGELOG entry: what changed, why, and the incident ID if there is one.
- Update `template/COMMANDS.md` if a command was added or changed.
- Update `REQUIRED_CLS` in `qa/qa_check.py`.
