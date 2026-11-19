# QA automatic report

| family | level | finding |
|---|---|---|
| infra | PASS | required file main.tex |
| infra | PASS | required file connected.cls |
| infra | PASS | required file refs.bib |
| infra | PASS | required file PRD.md |
| infra | PASS | required file PLAN.md |
| infra | PASS | required file TODO.md |
| infra | PASS | required file README.md |
| infra | PASS | required file book.pdf |
| infra | PASS | required file build.sh |
| infra | PASS | 10 chapter files in chapters/ |
| infra | PASS | 13 skills in .claude/skills/ |
| infra | PASS | stray or undocumented files in root: none |
| infra | PASS | required file connected.lua |
| infra | PASS | scanned 17 LaTeX sources for control characters |
| infra | PASS | checked relative links and images in README/PRD/PLAN/docs |
| infra | PASS | skill-count claims checked against 13 skills |
| cls-version | PASS | connected.cls v2.5.3 (standard: v2.5.3) |
| cls-version | PASS | CHANGELOG entry for v2.5.3 |
| typeset | PASS | boxes are unbreakable (no split box without a title) |
| typeset | PASS | 0 LaTeX errors [] |
| typeset | PASS | 0 undefined refs/cites [] |
| typeset | PASS | 0 overfull hbox > 5pt: [] |
| typeset | PASS | 0 overfull vbox |
| typeset | PASS | 0 underfull hbox: [] |
| typeset | PASS | 0 package warnings not in known-warnings.md: [] |
| typeset | PASS | footer numeral systems checked on every page |
| bidi | PASS | scanned 32 pages for reversed words, glued ranges, mirrored brackets, split prefixes |
| bidi | PASS | ':' or ';' set in font David (mis-spaced punctuation), pages [] |
| table | PASS | 2 tables in chapters |
| table | PASS | table 1: caption above the table |
| table | PASS | table 1: has \label |
| table | PASS | table 1: booktabs rules |
| table | PASS | table 2: caption above the table |
| table | PASS | table 2: has \label |
| table | PASS | table 2: booktabs rules |
| img | PASS | 5 figures |
| img | PASS | fig:smart-home: referenced in text 1x |
| img | PASS | fig:attention-loop: referenced in text 1x |
| img | PASS | fig:daily-time: referenced in text 1x |
| img | PASS | fig:goldilocks: referenced in text 2x |
| img | PASS | fig:internet-users: referenced in text 1x |
| img | PASS | image file images/smart_home.png exists |
| img | PASS | image file images/daily_time.png exists |
| img | PASS | image file images/goldilocks.png exists |
| img | PASS | image file images/internet_users.png exists |
| img | PASS | 0 'float too large' warnings |
| img | PASS | internet_users.png: label/legend overlaps none |
| img | PASS | daily_time.png: label/legend overlaps none |
| img | PASS | goldilocks.png: label/legend overlaps none |
| img | PASS | figure alone on a mostly empty page: pdf pages [] |
| img | PASS | 0 long captions in the list of figures (use \caption[short]{long}) |
| code | PASS | 1 pythonbox listings |
| code | PASS | listing source python/make_graphs.py exists |
| code | PASS | python/make_graphs.py: lines > 95 chars (wrap risk): [] |
| code | PASS | python/make_graphs.py: Hebrew text (comments or strings) inside listing: [] |
| code | PASS | python/make_graphs.py: listing is 31 lines (box is unbreakable, max ~38) |
| code | PASS | python/make_graphs.py: first source line of the range appears in the PDF ('def goldilocks():') |
| code | PASS | python/make_graphs.py: last source line of the range appears in the PDF ('plt.close(fig)') |
| code | PASS | text lines running past the page margins: pdf pages [] |
| code | PASS | pythonbox has its own background (codebg) |
| code | PASS | pythonbox is built inside an English (LTR) environment |

**Total: 0 FAIL, 0 WARN, 61 PASS**