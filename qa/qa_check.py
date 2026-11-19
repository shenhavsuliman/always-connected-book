"""
qa_check.py: automatic checks for the QA skills (one function per skill family).

Usage (from the project root, after building):
    python qa/qa_check.py              -> runs all families, writes qa/reports/qa-auto.md
    python qa/qa_check.py bidi typeset -> runs only those families

Each check prints PASS / WARN / FAIL with page number and evidence.
The QA skills (.claude/skills/qa-*) run this script first, then do the visual
page-by-page review that a script cannot do.
"""
import re
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
PDF, LOG, CLS = ROOT / "main.pdf", ROOT / "main.log", ROOT / "connected.cls"
REQUIRED_CLS = "2.5.2"            # the "standard" template version (qa-cls-version)
HEB = "\u0590-\u05FF"
FINALS = "ךםןףץ"

results = []                       # (family, level, message)


def add(fam, level, msg):
    results.append((fam, level, msg))


def pdf_pages():
    return [p.get_text() for p in pymupdf.open(PDF)]


# ------------------------------------------------------------------ qa-infra
def infra():
    must = ["main.tex", "connected.cls", "refs.bib", "PRD.md", "PLAN.md", "TODO.md",
            "README.md", "book.pdf", "build.sh"]
    for f in must:
        add("infra", "PASS" if (ROOT / f).exists() else "FAIL", f"required file {f}")
    chapters = sorted((ROOT / "chapters").glob("0*.tex"))
    add("infra", "PASS" if len(chapters) >= 8 else "FAIL", f"{len(chapters)} chapter files in chapters/")
    main = (ROOT / "main.tex").read_text(encoding="utf-8")
    for c in chapters:
        if f"chapters/{c.stem}" not in main:
            add("infra", "FAIL", f"{c.name} is not \\input in main.tex")
    skills = sorted((ROOT / ".claude" / "skills").glob("*/SKILL.md"))
    add("infra", "PASS" if len(skills) >= 8 else "FAIL", f"{len(skills)} skills in .claude/skills/")
    # INFRA-01: every root entry must be a build product (main.*, *.pysnip, dotfiles) or be
    # mentioned in README.md. A file nobody documented is a stray file.
    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    stray = [p.name for p in ROOT.glob("_test*")] + [p.name for p in ROOT.glob("*.sty")]
    for p in ROOT.iterdir():
        if p.name.startswith((".", "main.", "_")) or p.suffix == ".pysnip" or p.name == "__pycache__":
            continue
        if p.name in must or p.name in ("connected.lua", "qa", "template", "tests"):
            continue                       # structure required by the assignment / by the class
        if p.name not in readme and p.name not in stray:
            stray.append(p.name)
    add("infra", "WARN" if stray else "PASS", f"stray or undocumented files in root: {stray or 'none'}")
    for f in ("connected.lua",):   # helper the class loads (v2.4.0)
        add("infra", "PASS" if (ROOT / f).exists() else "FAIL", f"required file {f}")
    # INC-05: a script wrote "\r", "\f", "\b" as control characters into LaTeX sources
    src_files = [ROOT / "connected.cls", ROOT / "main.tex", *(ROOT / "chapters").rglob("*.tex"),
                 *(ROOT / "tests").glob("*.tex")]
    for f in src_files:
        bad = [hex(ord(c)) for c in f.read_text(encoding="utf-8") if ord(c) < 32 and c not in "\n\r\t"]
        cr = f.read_bytes().count(b"\r") - f.read_bytes().count(b"\r\n")
        if bad or cr > 0:
            add("infra", "FAIL", f"{f.name}: control characters {sorted(set(bad))[:4]} / lone CR x{cr} (INC-05)")
    add("infra", "PASS", f"scanned {len(src_files)} LaTeX sources for control characters")
    # README / PRD / docs: every relative link and image must exist in the repository
    for md in [ROOT / "README.md", ROOT / "PRD.md", ROOT / "PLAN.md", *(ROOT / "docs").glob("*.md")]:
        if not md.exists():
            continue
        txt = md.read_text(encoding="utf-8")
        links = re.findall(r"\]\(([^)#\s]+)", txt) + re.findall(r'src="([^"]+)"', txt)
        for ln in links:
            if ln.startswith(("http", "mailto")):
                continue
            target = (md.parent / ln).resolve()
            if not target.exists():
                add("infra", "FAIL", f"{md.name}: broken link -> {ln}")
    add("infra", "PASS", "checked relative links and images in README/PRD/PLAN/docs")
    # REPO-02 (round 4): every "N Skills" / "N סקילים" claim in the docs matches the real count
    real = len(skills)
    for md in [ROOT / "README.md", ROOT / "PLAN.md", ROOT / "TODO.md", ROOT / "PRD.md"]:
        if md.exists():
            for claimed in re.findall(r"(\d+)\s*(?:Skills|סקילים)|Skills \((\d+)\)", md.read_text(encoding="utf-8")):
                c = int(next(x for x in claimed if x))
                if c not in (real, 8, 7):  # 8 = mandatory QA family; 7 = "qa-super + 7 skills"
                    add("infra", "FAIL", f"{md.name}: claims {c} skills, repository has {real}")
    add("infra", "PASS", f"skill-count claims checked against {real} skills")


# ------------------------------------------------------------------ qa-cls-version
def cls_version():
    src = CLS.read_text(encoding="utf-8")
    m = re.search(r"\\def\\ConnectedVersion\{([\d.]+)\}", src)
    ver = m.group(1) if m else "?"
    add("cls-version", "PASS" if ver == REQUIRED_CLS else "FAIL",
        f"connected.cls v{ver} (standard: v{REQUIRED_CLS})")
    log = CHANGELOG = ROOT / "template" / "CHANGELOG.md"
    has = CHANGELOG.exists() and f"## v{ver}" in CHANGELOG.read_text(encoding="utf-8")
    add("cls-version", "PASS" if has else "FAIL", f"CHANGELOG entry for v{ver}")
    for f in (ROOT / "chapters").rglob("*.tex"):
        t = f.read_text(encoding="utf-8")
        for bad in (r"\RL{", r"\LR{", r"\textenglish", r"\setRTL", r"polyglossia"):
            if bad in t:
                add("cls-version", "FAIL", f"{f.name}: uses '{bad}' (not a connected.cls command)")


# ------------------------------------------------------------------ qa-typeset
def typeset():
    log = LOG.read_text(encoding="utf-8", errors="ignore")
    # QA-04 / LAYOUT-03 (round 4): a nearly empty page that is NOT the last page of a chapter
    # (the next page does not open a chapter, i.e. has no title span >= 26pt)
    doc = pymupdf.open(PDF)

    def opens_chapter(pg):
        return any(s["size"] >= 26 for b in pg.get_text("dict")["blocks"] for l in b.get("lines", [])
                   for s in l["spans"] if s["text"].strip())
    for i in range(1, doc.page_count - 1):
        pg = doc[i]
        chars = len(re.sub(r"\s", "", pg.get_text()))
        # how far down the page the content reaches (footer excluded): catches a page where
        # a box was pushed to the next page, even when the page still holds some text
        bottoms = [b[3] for b in pg.get_text("blocks") if b[3] < pg.rect.height * 0.9]
        fill = (max(bottoms) / (pg.rect.height * 0.9)) if bottoms else 0
        if (chars < 450 or fill < 0.6) and not opens_chapter(doc[i + 1]):
            add("typeset", "WARN", f"p{i + 1}: page only {fill:.0%} filled ({chars} chars) and does not end a chapter")
    # TYPE-07 (round 4): boxes must not break across pages (connected.cls boxbase)
    cls = CLS.read_text(encoding="utf-8")
    base = cls.split("boxbase/.style={", 1)[1].split("}}", 1)[0] if "boxbase/.style={" in cls else ""
    add("typeset", "FAIL" if "breakable" in base else "PASS", "boxes are unbreakable (no split box without a title)")
    errs = re.findall(r"^! .*", log, re.M)
    add("typeset", "FAIL" if errs else "PASS", f"{len(errs)} LaTeX errors {errs[:3]}")
    undef = re.findall(r"(?:Reference|Citation) `([^']+)' .*undefined", log)
    add("typeset", "FAIL" if undef else "PASS", f"{len(undef)} undefined refs/cites {sorted(set(undef))[:5]}")
    over = [(float(w), l) for w, l in re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\) .*?lines? ([\d-]+)", log)]
    known_file = ROOT / "qa" / "known-warnings.md"
    known = known_file.read_text(encoding="utf-8") if known_file.exists() else ""
    kn = [o for o in over if o[0] > 5 and f"lines {o[1]}" in known]
    if kn:
        add("typeset", "PASS", f"{len(kn)} known, documented warnings (qa/known-warnings.md): {[f'{w:.0f}pt@{l}' for w, l in kn]}")
    big = [o for o in over if o[0] > 5 and o not in kn]
    add("typeset", "WARN" if big else "PASS",
        f"{len(big)} overfull hbox > 5pt: {[f'{w:.0f}pt@{l}' for w, l in big[:6]]}")
    vbox = re.findall(r"Overfull \\vbox", log)
    add("typeset", "WARN" if vbox else "PASS", f"{len(vbox)} overfull vbox")
    # TYPE-03: underfull lines are stretched lines; the Detector counts them as findings
    under = [u for u in re.findall(r"Underfull \\hbox \(badness (\d+)\) .*?lines? ([\d-]+)", log)
             if f"badness {u[0]}) in paragraph at lines {u[1]}" not in known]
    add("typeset", "WARN" if under else "PASS", f"{len(under)} underfull hbox: {[f'{b}@{l}' for b, l in under[:6]]}")
    # TYPE-04: any package warning must be explained in qa/known-warnings.md
    pkg = sorted(set(re.findall(r"^Package (\w+) Warning: (.*?)\.?$", log, re.M)))
    unk = [(p, m) for p, m in pkg if m[:40] not in known]
    add("typeset", "WARN" if unk else "PASS", f"{len(unk)} package warnings not in known-warnings.md: {unk[:4]}")
    # TYPE-05: front matter footer "page iv of 26" mixes roman and arabic numerals
    for n, page in enumerate(pymupdf.open(PDF), 1):
        foot = " ".join(s["text"] for b in page.get_text("dict")["blocks"] for l in b.get("lines", [])
                        for s in l["spans"] if s["bbox"][1] > page.rect.height - 70)
        m = re.search(r"עמוד\s*([ivxl]+|\d+)\s*מתוך\s*([ivxl]+|\d+)", foot)
        if m:
            a, b = m.groups()
            if a.isdigit() != b.isdigit():
                add("typeset", "FAIL", f"p{n}: footer mixes numeral systems ('{a}' of '{b}')")
    add("typeset", "PASS", "footer numeral systems checked on every page")


# ------------------------------------------------------------------ qa-BiDi
def bidi():
    pages = pdf_pages()
    for n, t in enumerate(pages, 1):
        # Hebrew word that *starts* with a final letter = reversed word
        for w in re.findall(rf"(?<![{HEB}])[{FINALS}][{HEB}]+", t):
            add("bidi", "FAIL", f"p{n}: Hebrew word starts with a final letter: '{w}'")
        # reversed decimal like '0.1' where source had '1.0' is undetectable here; check split ranges
        for r in re.findall(r"\b(\d{2})(\d{4})\b", t):
            if 1900 <= int(r[1]) <= 2030:
                add("bidi", "WARN", f"p{n}: possibly glued/reversed range '{r[0]}{r[1]}'")
        if re.search(r"\)\s*\]\d+\[", t) or re.search(r"\]\d+\[", t):
            add("bidi", "FAIL", f"p{n}: mirrored citation bracket ']n['")
    # QA-04 (round 4), geometric: text extraction splits LTR runs into separate "lines", so
    # visual lines are rebuilt from word positions. In an RTL line the LEFTMOST word ends it
    # and the RIGHTMOST word opens it.
    doc = pymupdf.open(PDF)
    for n, pg in enumerate(doc, 1):
        if n == 1 or "Accessed:" in pg.get_text():          # cover / IEEE list: LTR layout
            continue
        lines = {}
        for x0, y0, x1, y1, w, *_ in pg.get_text("words"):
            w = w.replace("\xad", "")        # soft hyphens are extracted as their own "words"
            if w:
                lines.setdefault(round(y1 / 3), []).append((x0, w))
        body = [ws for ws in lines.values() if len(ws) >= 4]  # body text lines only
        for ws in body:
            ws.sort()
            end_word, start_word = ws[0][1], ws[-1][1]
            # BIDI-04: Hebrew prefix ("ב-", "ה-", "ו-") stranded at the end of a line
            # (the hyphen is not part of the extracted word; a lone prefix letter is the signal:
            #  Hebrew has no one-letter words other than these prefixes)
            if re.fullmatch(r"[בהוכלמש]-?", end_word):
                add("bidi", "FAIL", f"p{n}: Hebrew prefix '{end_word}' split from its word at line end")
            # TYPE-09: an IEEE citation "[n]" opening a line, cut off from its word
            if re.fullmatch(r"\[\d+(?:,\d+)*\][.,]?", start_word):
                add("bidi", "WARN", f"p{n}: citation '{start_word}' opens a line, cut off from its word")
    add("bidi", "PASS", f"scanned {len(pages)} pages for reversed words, glued ranges, mirrored brackets, split prefixes")
    # BIDI-01: in David the ':' and ';' glyphs are narrow with wide gaps ("shalom : kesher").
    # Text extraction cannot see a gap inside a glyph, so we forbid the font for punctuation.
    bad_font = []
    for n, page in enumerate(pymupdf.open(PDF), 1):
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    if "David" in s["font"] and re.search(r"[:;]", s["text"]):
                        bad_font.append(n)
    add("bidi", "FAIL" if bad_font else "PASS",
        f"':' or ';' set in font David (mis-spaced punctuation), pages {sorted(set(bad_font))[:8]}")


# ------------------------------------------------------------------ qa-table
def table():
    src = "".join(f.read_text(encoding="utf-8") for f in (ROOT / "chapters").glob("0*.tex"))
    tabs = re.findall(r"\\begin\{table\}(.*?)\\end\{table\}", src, re.S)
    add("table", "PASS" if tabs else "FAIL", f"{len(tabs)} tables in chapters")
    for i, t in enumerate(tabs, 1):
        ok_cap = t.find(r"\caption") < t.find(r"\begin{tabular")
        add("table", "PASS" if ok_cap else "FAIL", f"table {i}: caption above the table")
        add("table", "PASS" if r"\label" in t else "FAIL", f"table {i}: has \\label")
        add("table", "PASS" if r"\toprule" in t and r"\bottomrule" in t else "WARN", f"table {i}: booktabs rules")


# ------------------------------------------------------------------ qa-img
def img():
    src = "".join(f.read_text(encoding="utf-8") for f in (ROOT / "chapters").rglob("*.tex"))
    figs = re.findall(r"\\begin\{figure\}(.*?)\\end\{figure\}", src, re.S)
    add("img", "PASS" if figs else "FAIL", f"{len(figs)} figures")
    labels = re.findall(r"\\label\{(fig:[^}]+)\}", src)
    for lab in labels:
        refs = src.count(r"\ref{" + lab + "}")
        add("img", "PASS" if refs else "FAIL", f"{lab}: referenced in text {refs}x")
    for g in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", src):
        add("img", "PASS" if (ROOT / g).exists() else "FAIL", f"image file {g} exists")
    log = LOG.read_text(encoding="utf-8", errors="ignore")
    floats = re.findall(r"Float too large for page", log)
    add("img", "WARN" if floats else "PASS", f"{len(floats)} 'float too large' warnings")
    # IMG-01: a page whose only content is a figure/table plus caption and that is mostly empty.
    # The last page of a chapter is exempt (the next page starts with a chapter heading).
    doc = pymupdf.open(PDF)
    alone = []
    for n in range(2, len(doc)):
        page, nxt = doc[n - 1], doc[n]
        H = page.rect.height
        words = [w for w in page.get_text("words") if 60 < w[1] < H - 60]
        caption = any(w[4] in ("איור", "טבלה") for w in words)
        has_art = bool(page.get_images() or len(page.get_drawings()) > 8)
        nxt_head = any(s["size"] >= 24 for b in nxt.get_text("dict")["blocks"] for l in b.get("lines", [])
                       for s in l["spans"])   # a chapter title (28pt) opens the next page
        if caption and has_art and len(words) < 90 and not nxt_head:
            alone.append(n)
    add("img", "WARN" if alone else "PASS", f"figure alone on a mostly empty page: pdf pages {alone}")
    # IMG-02: the list of figures must use short captions
    lof = ROOT / "main.lof"
    if lof.exists():
        long_ = [len(m) for m in re.findall(r"\\contentsline \{figure\}\{(.*?)\}\{\d+\}\{", lof.read_text(encoding="utf-8", errors="ignore"))
                 if len(m) > 150]
        add("img", "WARN" if long_ else "PASS", f"{len(long_)} long captions in the list of figures (use \\caption[short]{{long}})")


# ------------------------------------------------------------------ qa-code
def code():
    src = "".join(f.read_text(encoding="utf-8") for f in (ROOT / "chapters").rglob("*.tex"))
    calls = re.findall(r"\\pythonfile(?:\[([^\]]*)\])?\{([^}]+)\}", src)
    add("code", "PASS" if calls else "FAIL", f"{len(calls)} pythonbox listings")
    for opts, f in calls:
        p = ROOT / f
        add("code", "PASS" if p.exists() else "FAIL", f"listing source {f} exists")
        if p.exists():
            lines = p.read_text(encoding="utf-8").splitlines()
            a = int((re.search(r"firstline=(\d+)", opts or "") or [0, 1])[1])
            b = int((re.search(r"lastline=(\d+)", opts or "") or [0, len(lines)])[1])
            seg = lines[a - 1:b]
            long_ = [i + a for i, l in enumerate(seg) if len(l) > 95]
            add("code", "WARN" if long_ else "PASS", f"{f}: lines > 95 chars (wrap risk): {long_[:5]}")
            # QA-02 (round 2): any Hebrew inside the listed range, in comments AND string
            # literals, gets scrambled by bidi inside an LTR code box. Keep it out of the range.
            heb = [i + a for i, l in enumerate(seg) if re.search(rf"[{HEB}]", l)]
            add("code", "FAIL" if heb else "PASS", f"{f}: Hebrew text (comments or strings) inside listing: {heb[:6]}")
            longest = max(len(seg), 1)
            add("code", "WARN" if longest > 38 else "PASS", f"{f}: listing is {len(seg)} lines (box is unbreakable, max ~38)")
            # QA-01: check what the PDF actually shows, not only the source range.
            shown = re.sub(r"\s+", "", "".join(pdf_pages()))
            nonblank = [l.strip() for l in seg if l.strip()]
            for label, line in (("first", nonblank[0]), ("last", nonblank[-1])):
                key = re.sub(r"\s+", "", line)[:14]
                add("code", "PASS" if key in shown else "FAIL",
                    f"{f}: {label} source line of the range appears in the PDF ('{line[:30]}')")
    # QA-01 / CODE-01: no text may run past the page margins (a leaked line ran off the box and the page)
    over = []
    for n, page in enumerate(pymupdf.open(PDF), 1):
        if n == 1:
            continue                       # the cover is a full-bleed design
        W = page.rect.width
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                x0, y0, x1, y1 = l["bbox"]
                if 60 < y0 < page.rect.height - 60 and (x1 > W - 30 or x0 < 30):
                    over.append(n)
    add("code", "FAIL" if over else "PASS", f"text lines running past the page margins: pdf pages {sorted(set(over))[:8]}")
    cls = CLS.read_text(encoding="utf-8")
    add("code", "PASS" if "colback=codebg" in cls else "FAIL", "pythonbox has its own background (codebg)")
    add("code", "PASS" if "otherlanguage}{english}" in cls.split("pythonfile")[-1] else "FAIL",
        "pythonbox is built inside an English (LTR) environment")


FAMILIES = {"infra": infra, "cls-version": cls_version, "typeset": typeset,
            "bidi": bidi, "table": table, "img": img, "code": code}

if __name__ == "__main__":
    want = sys.argv[1:] or list(FAMILIES)
    for w in want:
        try:
            FAMILIES[w]()
        except Exception as e:  # a crashed check is itself a finding
            add(w, "FAIL", f"check crashed: {e!r}")
    out = ["# QA automatic report", "", "| family | level | finding |", "|---|---|---|"]
    out += [f"| {f} | {lvl} | {m.replace('|', '/')} |" for f, lvl, m in results]
    fails = sum(r[1] == "FAIL" for r in results)
    warns = sum(r[1] == "WARN" for r in results)
    out += ["", f"**Total: {fails} FAIL, {warns} WARN, {len(results) - fails - warns} PASS**"]
    rep = ROOT / "qa" / "reports"
    rep.mkdir(parents=True, exist_ok=True)
    (rep / "qa-auto.md").write_text("\n".join(out), encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    for f, lvl, m in results:
        if lvl != "PASS":
            print(f"[{lvl}] {f}: {m}")
    print(f"TOTAL: {fails} FAIL, {warns} WARN -> qa/reports/qa-auto.md")
