# Prompts for strict-grader rounds 5 and 6

The base prompt is `09-strict-grader.md` (written for round 4). For rounds 5 and 6 the Master sent the same base prompt plus these additions, recorded here word for word (task-specific paths and counts as they were at the time).

## Round 5 (2026-11-19)
> Read your instructions from `prompts\09-strict-grader.md` and follow them exactly, with these changes: this is **Detector round 5**, and write the report to `qa\reports\detector-round-5.md`. First read `qa\reports\detector-round-4.md` and `qa\reports\fixer-round-4.md`, and for every round-4 finding state VERIFIED-FIXED, STILL-OPEN or REGRESSED (TYPE-08 and SUB-01 were kept by decision; judge whether that decision is acceptable). Then search for NEW findings with the same strictness, including in the five new commits (git log) and the template v2.5.2. The PDF is now 32 pages (main.pdf / book.pdf, current). GitHub origin/main is current, so verify with `git status` and `git log origin/main -1`. Give the new estimated grade with deductions.

## Round 6 (2026-11-19)
> Read your instructions from `prompts\09-strict-grader.md` and follow them exactly, with these changes: this is **Detector round 6**, and write the report to `qa\reports\detector-round-6.md`. First read `qa\reports\detector-round-5.md` and `qa\reports\fixer-round-5.md`, and for every round-5 finding state VERIFIED-FIXED, STILL-OPEN or REGRESSED. Verify the Fixer's claims against the actual files and PDF; do not trust the report. Then search for NEW findings with the same strictness. The PDF is 32 pages (main.pdf / book.pdf, current), the template is v2.5.3, and GitHub origin/main is current (verify with git). Give the new estimated grade with the deductions listed. Keep the report focused: list only real deductions, not notes.

## Results
| Round | Estimated grade | Critical / major / minor |
|-------|-----------------|--------------------------|
| 4 | 82/100 | 0 / 9 / 20 |
| 5 | 91/100 | 0 / 4 / 17 |
| 6 | 94/100 | 0 / 3 / 10 |

## Round 7 (2026-11-20)
> Read your instructions from `prompts\09-strict-grader.md` and follow them exactly, with these changes: this is **Detector round 7**, and write the report to `qa\reports\detector-round-7.md`. First read `qa\reports\detector-round-6.md` and `qa\reports\fixer-round-6.md`. For every round-6 finding state VERIFIED-FIXED, STILL-OPEN or REGRESSED, and **verify every piece of evidence the Fixer cites** (rerun its commands, open the pages); a claim whose evidence does not hold is itself a major finding. Then search for NEW findings with the same strictness, including in the four new commits and template v2.5.4. The PDF is 32 pages (main.pdf / book.pdf, current), and GitHub origin/main is current (verify with git). Give the new estimated grade with the deductions listed. List only real deductions, not notes.
