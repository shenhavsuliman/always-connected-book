You are convening an **expert committee** that defines the acceptance criteria for a professional, publication-grade Hebrew/English book produced with LuaLaTeX by a team of AI agents. The committee's output becomes the core of the project's PRD.

## Context (read these files first)
- Assignment definition summary: `C:\Users\user\Desktop\latex-book\docs\assignment-requirements.md`
- Current book: `C:\Users\user\Desktop\latex-book\main.tex`, `connected.cls`, `chapters\*.tex`
- The student's vision: a book about technology and everyday life, "Always Connected", written in a style inspired by Yuval Noah Harari, with a distinctive personal design (night-blue / turquoise / coral "notification" palette, a red notification dot as a visual motif).

## The committee (5 members, each speaks in their own voice)
1. **Publishing editor**: structure, front matter, the reader's journey, style consistency.
2. **Hebrew typography and BiDi expert**: RTL/LTR mixing, numbers, ranges, citations, fonts, TOC numbering.
3. **LaTeX and reproducibility engineer**: CLS design, versioning, folder structure, single-command build, warnings.
4. **Data-visualization and research-integrity expert**: graphs from code, verified sources, IEEE references, honesty about illustrative models.
5. **AI-workflow and QA lead**: agent roles as Skills, Detector/Fixer loop, red team, incident investigations, prompt documentation, token/model choices.

## Task
1. Each member writes 4–6 **measurable** acceptance criteria in their area. Each criterion gets an ID (e.g., `TYP-03`), a one-line requirement, and **how it is verified** (which QA skill or which command checks it).
2. The committee then holds a short **cross-review**: each member names the single biggest risk in another member's area.
3. Finish with a **joint verdict**: the 10 criteria that matter most ("must pass for submission"), ranked.

Write everything in Hebrew (technical terms may stay in English) to `C:\Users\user\Desktop\latex-book\docs\expert-committee.md`. Keep it tight: about 2–3 pages of markdown, using tables for the criteria. Do not edit any other file. Reply in under 120 words with the top-3 criteria.
