/**
 * make_docx.js — ממיר את ספר ה-LaTeX לקובץ Word ניתן לעריכה (book.docx)
 *
 * קורא את אותם קובצי .tex ש-XeLaTeX קורא, ולכן הטקסט זהה ל-PDF.
 * מספרי איורים, טבלאות ומשוואות נלקחים מ-main.aux (צריך לבנות את ה-PDF קודם).
 *
 * הרצה (מתיקיית הפרויקט):  node word/make_docx.js
 */
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, LevelFormat, BorderStyle, ShadingType, WidthType,
  TableOfContents, Footer, Header, PageNumber, PageBreak, VerticalAlign,
} = require("docx");

const ROOT = path.resolve(__dirname, "..");
const rd = (p) => fs.readFileSync(path.join(ROOT, p), "utf8");

// ---------------------------------------------------------------- צבעים וגופנים
const C = { night: "1B2A41", screen: "0FA3B1", notif: "F25F5C", sun: "FFB238", leaf: "3BB273", ink: "2E3440", muted: "6B7280" };
const BOX = {
  thinkbox: { color: "E8A21A", bg: "FFF4E0", title: "שאלה למחשבה", icon: "? " },
  factbox:  { color: C.screen, bg: "E3F5F7", title: "נתון מפתח", icon: "" },
  alertbox: { color: C.notif,  bg: "FDECEC", title: "שימו לב", icon: "! " },
  tipbox:   { color: C.leaf,   bg: "E8F6EE", title: "טיפ לאיזון", icon: "" },
  eqbox:    { color: C.night,  bg: "F1F3F6", title: "", icon: "" },
};
const BODY = "David", HEAD = "Gisha", LATIN = "Times New Roman";
const SZ = 24; // 12pt

// ---------------------------------------------------------------- תוויות ומקורות
const labels = {};
for (const m of rd("main.aux").matchAll(/\\newlabel\{([^}]+)\}\{\{([^}]*)\}/g)) labels[m[1]] = m[2];

const bib = {};
for (const m of rd("refs.bib").matchAll(/@(\w+)\{([^,]+),([\s\S]*?)\n\}/g)) {
  const f = { type: m[1].toLowerCase() };
  for (const fm of m[3].matchAll(/(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}/g)) f[fm[1].toLowerCase()] = fm[2].replace(/[{}]/g, "").trim();
  bib[m[2].trim()] = f;
}
// IEEE: אותו מספור כמו ב-PDF. הסדר נלקח מ-main.bbl שבנה biber (sorting=none)
const citeOrder = [...rd("main.bbl").matchAll(/\\entry\{([^}]+)\}/g)].map((m) => m[1]);
const ieee = (k) => citeOrder.indexOf(k) + 1 || "?";
const surname = (a) => (a.includes(",") ? a.split(",")[0] : a.split(" ").slice(-1)[0]).trim();
function citeName(k) {
  const e = bib[k]; if (!e) return k;
  const au = (e.author || e.editor || "").split(/\s+and\s+/).filter(Boolean);
  if (au.length === 1) return au[0].includes(",") || au[0].split(" ").length > 1 && !/[A-Z]{2,}/.test(au[0]) ? surname(au[0]) : au[0];
  if (au.length === 2) return `${surname(au[0])} & ${surname(au[1])}`;
  return `${surname(au[0])} et al.`;
}
const citeYear = (k) => (bib[k] && (bib[k].year || (bib[k].date || "").slice(0, 4))) || "n.d.";
function bibEntry(k) {
  const e = bib[k];
  const au = (e.author || "").split(/\s+and\s+/).map((a) => {
    if (!a.includes(",")) return a;
    const [s, g] = a.split(",").map((x) => x.trim());
    return `${s}, ${g.split(/[\s-]+/).filter(Boolean).map((x) => x[0] + ".").join(" ")}`;
  });
  const who = au.length > 1 ? au.slice(0, -1).join(", ") + ", & " + au.slice(-1) : au[0];
  const src = [e.journal || e.journaltitle, e.volume && (e.number ? `${e.volume}(${e.number})` : e.volume), e.pages,
               e.publisher || e.institution || e.organization].filter(Boolean).join(", ");
  const link = e.doi ? `https://doi.org/${e.doi}` : e.url || "";
  return { who, year: citeYear(k), title: e.title, src, link };
}

// ---------------------------------------------------------------- טקסט שורה → runs
function mathText(s) {
  const sub = { 0: "₀", 1: "₁", 2: "₂", 3: "₃", i: "ᵢ" }, sup = { 2: "²", 3: "³", "*": "*" };
  return s
    .replace(/\\frac\{([^}]*)\}\{([^}]*)\}/g, "$1/$2")
    .replace(/\\(beta|alpha|gamma|delta|Delta|sigma|mu)/g, (_, g) => ({ beta: "β", alpha: "α", gamma: "γ", delta: "δ", Delta: "Δ", sigma: "σ", mu: "μ" }[g]))
    .replace(/_\{?([0-9i])\}?/g, (_, d) => sub[d]).replace(/\^\{?([23*])\}?/g, (_, d) => sup[d])
    .replace(/\\cdot/g, "·").replace(/\\approx/g, "≈").replace(/\\times/g, "×").replace(/\\leq?/g, "≤").replace(/\\geq?/g, "≥")
    .replace(/\\(left|right|,|;|quad|qquad|text|mathrm)/g, " ").replace(/-/g, "−").replace(/[{}]/g, "").replace(/\s+/g, " ").trim();
}
function cleanText(s) {
  return s.replace(/\\%/g, "%").replace(/\\&/g, "&").replace(/\\_/g, "_").replace(/\\#/g, "#")
    .replace(/---/g, "—").replace(/--/g, "–").replace(/~/g, " ").replace(/``|''/g, '"')
    .replace(/\\LaTeX\{?\}?/g, "LaTeX").replace(/\\(quad|qquad|,|noindent|centering|small|large|Large)\b/g, " ")
    .replace(/\\\\/g, " ").replace(/\s+/g, " ");
}
/** מפרק טקסט LaTeX של שורה לרשימת קטעים {text, bold, latin} */
function parseInline(s, st = {}) {
  const out = [];
  let i = 0, buf = "";
  const flush = () => { if (buf) out.push({ text: cleanText(buf), ...st }); buf = ""; };
  const arg = (j) => { // מחזיר [תוכן, אינדקס אחרי] עבור {...} שמתחיל ב-j
    let d = 0, k = j;
    for (; k < s.length; k++) { if (s[k] === "{") d++; else if (s[k] === "}" && --d === 0) break; }
    return [s.slice(j + 1, k), k + 1];
  };
  while (i < s.length) {
    if (s[i] === "$") {
      const j = s.indexOf("$", i + 1); flush();
      out.push({ text: mathText(s.slice(i + 1, j)), ...st, latin: true, math: true }); i = j + 1; continue;
    }
    const m = /^\\([a-zA-Z]+)\*?/.exec(s.slice(i));
    if (m) {
      const cmd = m[1]; let j = i + m[0].length;
      while (s[j] === "[") j = s.indexOf("]", j) + 1; // מדלג על ארגומנטים אופציונליים
      const has = s[j] === "{";
      const [a, after] = has ? arg(j) : ["", j];
      flush();
      if (cmd === "textbf") out.push(...parseInline(a, { ...st, bold: true }));
      else if (["en", "textenglish", "LR", "num"].includes(cmd)) out.push(...parseInline(a, { ...st, latin: true }));
      else if (["emph", "textit", "RL", "heb", "mathheb", "mbox", "text"].includes(cmd)) out.push(...parseInline(a, st));
      else if (cmd === "parencite") out.push({ text: "[" + a.split(",").map((k) => ieee(k.trim())).join(", ") + "]", ...st, latin: true });
      else if (cmd === "textcite") out.push({ text: a.split(",").map((k) => `${citeName(k.trim())} [${ieee(k.trim())}]`).join("; "), ...st, latin: true });
      else if (cmd === "ref") out.push({ text: labels[a] || "?", ...st });
      else if (cmd === "eqref") out.push({ text: `(${labels[a] || "?"})`, ...st });
      else if (["label", "index", "Needspace", "needspace", "allowbreak"].includes(cmd)) { /* מושמט */ }
      else if (cmd === "LaTeX") out.push({ text: "LaTeX", ...st, latin: true });
      else if (has) out.push(...parseInline(a, st)); // פקודה לא מוכרת: שומרים את התוכן
      i = has ? after : j; continue;
    }
    buf += s[i++];
  }
  flush();
  return out.filter((r) => r.text !== "");
}
function runs(segs, base = {}) {
  return segs.map((g) => {
    const latin = g.latin && !/[֐-׿]/.test(g.text);
    return new TextRun({
      text: g.text, bold: g.bold || base.bold, boldComplexScript: g.bold || base.bold,
      italics: g.math, rightToLeft: !latin, color: base.color,
      font: base.font ? { ascii: base.font, hAnsi: base.font, cs: base.font } : { ascii: LATIN, hAnsi: LATIN, cs: BODY },
      size: base.size || SZ, sizeComplexScript: base.size || SZ,
    });
  });
}
const para = (text, o = {}) => new Paragraph({
  bidirectional: true, alignment: o.align || AlignmentType.BOTH, spacing: { after: 120, line: 300 },
  children: runs(typeof text === "string" ? parseInline(text) : text, o), ...o.p,
});

// ---------------------------------------------------------------- תמונות
function pngSize(file) {
  const b = fs.readFileSync(file);
  return [b.readUInt32BE(16), b.readUInt32BE(20)];
}
function image(rel, widthPx = 560) {
  const file = path.join(ROOT, rel);
  const [w, h] = pngSize(file);
  return new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { before: 120, after: 60 },
    children: [new ImageRun({ type: "png", data: fs.readFileSync(file), transformation: { width: widthPx, height: Math.round((widthPx * h) / w) } })],
  });
}
const caption = (kind, label, text) => new Paragraph({
  bidirectional: true, alignment: AlignmentType.CENTER, spacing: { after: 240 },
  children: [...runs([{ text: `${kind} ${labels[label] || ""}. ` }], { bold: true, color: C.screen, size: 20 }),
             ...runs(parseInline(text), { size: 20, color: C.muted })],
});
const FIG_IMG = { "attention-loop": "images/attention_loop.png" };

// ---------------------------------------------------------------- בלוקים
let chapterNo = 0, sectionNo = 0, listInstance = 0;
function between(lines, i, env) { // אוסף שורות עד \end{env} המתאים (כולל קינון)
  const body = []; let d = 1;
  for (i++; i < lines.length; i++) {
    if (lines[i].includes(`\\begin{${env}}`)) d++;
    if (lines[i].includes(`\\end{${env}}`) && --d === 0) break;
    body.push(lines[i]);
  }
  return [body, i];
}
function list(body, kind, level = 0, base = {}) {
  const items = []; let cur = null, nested = [];
  for (let k = 0; k < body.length; k++) {
    const l = body[k].trim();
    const b = /\\begin\{(itemize|enumerate|checklist)\}/.exec(l);
    if (b) { const [inner, e] = between(body, k, b[1]); items.push({ nested: list(inner, b[1], level + 1, base) }); k = e; continue; }
    if (l.startsWith("\\item")) { cur = { text: l.replace(/^\\item\s*/, "") }; items.push(cur); }
    else if (l && cur) cur.text += " " + l;
  }
  const ref = kind === "enumerate" ? "num" : kind === "checklist" ? "check" : "bullet";
  const instance = ++listInstance; // כל רשימה מתחילה מ-1
  return items.flatMap((it) => it.nested || [new Paragraph({
    bidirectional: true, alignment: AlignmentType.BOTH, numbering: { reference: ref, level, instance }, spacing: { after: 60, line: 290 },
    shading: base.bg ? { type: ShadingType.CLEAR, fill: base.bg, color: "auto" } : undefined,
    children: runs(parseInline(it.text)),
  })]);
}
function table(body) {
  const src = body.join("\n");
  const cap = /\\caption\{([^\n]*)\}\s*\n/.exec(src);
  const label = (/\\label\{([^}]+)\}/.exec(src) || [])[1];
  const inner = src.split("\\midrule")[1].split("\\bottomrule")[0];
  const header = src.split("\\toprule")[1].split("\\midrule")[0];
  const rows = [header, ...inner.split(/\\\\\s*\n/)].join("\\\\\n").split(/\\\\\s*\n/).map((r) => r.trim()).filter(Boolean)
    .map((r) => r.replace(/\\\\$/, "").split(/(?<!\\)&/).map((c) => c.trim()));
  const n = rows[0].length, W = 9000;
  const widths = n === 3 ? [2000, 2600, 4400] : Array(n).fill(Math.floor(W / n));
  const t = new Table({
    visuallyRightToLeft: true, width: { size: W, type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((r, ri) => new TableRow({ tableHeader: ri === 0, children: r.map((c, ci) => new TableCell({
      width: { size: widths[ci], type: WidthType.DXA }, verticalAlign: VerticalAlign.CENTER,
      shading: { type: ShadingType.CLEAR, color: "auto", fill: ri === 0 ? C.screen : ri % 2 ? "FFFFFF" : "F5F7FA" },
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      borders: { top: { style: BorderStyle.SINGLE, size: 4, color: "D9DEE5" }, bottom: { style: BorderStyle.SINGLE, size: 4, color: "D9DEE5" },
                 left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" } },
      children: [new Paragraph({ bidirectional: true, alignment: AlignmentType.RIGHT,
        children: runs(parseInline(c), ri === 0 ? { bold: true, color: "FFFFFF", size: 21 } : { size: 21 }) })],
    })) })),
  });
  return [caption("טבלה", label, cap ? cap[1] : ""), t, new Paragraph({ children: [] })];
}
function figure(src) {
  const cap = (/\\caption(?:\[[^\]]*\])?\{([\s\S]*)\}\s*\n\s*\\label/.exec(src) || [])[1] || "";
  const label = (/\\label\{([^}]+)\}/.exec(src) || [])[1];
  const g = /\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}/.exec(src);
  return [image(g ? g[1] : FIG_IMG[label.replace("fig:", "")]), caption("איור", label, cap)];
}
function equation(body) {
  const src = body.join(" ");
  const label = (/\\label\{([^}]+)\}/.exec(src) || [])[1];
  const tex = src.replace(/\\label\{[^}]+\}/, "");
  return new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { before: 120, after: 120 },
    children: [new TextRun({ text: mathText(tex), italics: true, size: 28, font: "Cambria Math" }),
               new TextRun({ text: label ? `        (${labels[label]})` : "", size: 22, font: LATIN })],
  });
}
function codeBox(opts, file, title) {
  const src = rd(file).split(/\r?\n/);
  const a = +((/firstline=(\d+)/.exec(opts) || [])[1] || 1), b = +((/lastline=(\d+)/.exec(opts) || [])[1] || src.length);
  const head = new Paragraph({ bidirectional: true, keepNext: true, spacing: { before: 200, after: 0 },
    shading: { type: ShadingType.CLEAR, color: "auto", fill: C.night },
    children: runs(parseInline(title), { bold: true, color: "FFFFFF", font: HEAD, size: 20 }) });
  const lines = src.slice(a - 1, b).map((line, i) => new Paragraph({
    alignment: AlignmentType.LEFT, spacing: { after: 0, line: 240 },
    shading: { type: ShadingType.CLEAR, color: "auto", fill: "F3F6F9" },
    children: [new TextRun({ text: String(a + i).padStart(3) + "  ", font: "Courier New", size: 15, color: "9AA3AF" }),
               new TextRun({ text: line || " ", font: "Courier New", size: 17 })] }));
  return [head, ...lines, new Paragraph({ spacing: { after: 160 }, children: [] })];
}
function box(kind, title, body) {
  const b = BOX[kind];
  const t = title || b.title;
  const side = { style: BorderStyle.SINGLE, size: 24, color: b.color, space: 8 };
  const out = [];
  if (t) out.push(new Paragraph({
    bidirectional: true, keepNext: true, spacing: { before: 200, after: 0 },
    shading: { type: ShadingType.CLEAR, color: "auto", fill: b.color }, border: { right: side },
    children: runs([{ text: b.icon + t }], { bold: true, color: "FFFFFF", font: HEAD, size: 22 }),
  }));
  for (const p of blocks(body, { bg: b.bg, side })) out.push(p);
  out.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
  return out;
}

/** הממיר הראשי: שורות LaTeX → אלמנטים של Word */
function blocks(lines, base = {}) {
  const out = []; let buf = [];
  const flush = () => {
    const t = buf.join(" ").trim(); buf = [];
    if (!t) return;
    out.push(new Paragraph({
      bidirectional: true, alignment: AlignmentType.BOTH, spacing: { after: base.bg ? 60 : 140, line: 300 },
      shading: base.bg ? { type: ShadingType.CLEAR, color: "auto", fill: base.bg } : undefined,
      border: base.side ? { right: base.side } : undefined, children: runs(parseInline(t)),
    }));
  };
  for (let i = 0; i < lines.length; i++) {
    const l = lines[i].replace(/(?<!\\)%.*$/, "").trim();
    let m;
    if (!l) { flush(); continue; }
    if ((m = /^\\chapter(\*?)\{(.*)\}/.exec(l))) {
      flush(); const star = m[1] === "*";
      if (!star) { chapterNo++; sectionNo = 0; }
      out.push(new Paragraph({ heading: HeadingLevel.HEADING_1, bidirectional: true, pageBreakBefore: true,
        children: runs([{ text: (star ? "" : `פרק ${chapterNo}: `) + cleanText(m[2]) }], { font: HEAD, size: 40, bold: true, color: C.night }) }));
    } else if ((m = /^\\section\*?\{(.*)\}/.exec(l))) {
      flush(); sectionNo++;
      out.push(new Paragraph({ heading: HeadingLevel.HEADING_2, bidirectional: true,
        children: runs([{ text: `${chapterNo}.${sectionNo}  ` }, ...parseInline(m[1])], { font: HEAD, size: 28, bold: true, color: C.screen }) }));
    } else if ((m = /^\\begin\{epigraph\}\{(.*)\}/.exec(l))) {
      flush(); const [body, e] = between(lines, i, "epigraph"); i = e;
      out.push(para(body.join(" "), { size: 26, color: C.night, p: { shading: { type: ShadingType.CLEAR, color: "auto", fill: "F5F7FA" },
        border: { right: { style: BorderStyle.SINGLE, size: 12, color: "8D95A1", space: 8 } }, spacing: { before: 120, after: m[1] ? 0 : 240 } } }));
      if (m[1]) out.push(para(`— ${m[1]}`, { size: 20, color: C.muted, align: AlignmentType.LEFT, p: { spacing: { after: 240 } } }));
    } else if ((m = /^\\begin\{(thinkbox|factbox|alertbox|tipbox|eqbox)\}(?:\[(.*)\])?/.exec(l))) {
      flush(); const [body, e] = between(lines, i, m[1]); i = e; out.push(...box(m[1], m[2], body));
    } else if ((m = /^\\begin\{(itemize|enumerate|checklist)\}/.exec(l))) {
      flush(); const [body, e] = between(lines, i, m[1]); i = e; out.push(...list(body, m[1], 0, base));
    } else if (/^\\begin\{table\}/.test(l)) {
      flush(); const [body, e] = between(lines, i, "table"); i = e; out.push(...table(body));
    } else if (/^\\begin\{figure\}/.test(l)) {
      flush(); const [body, e] = between(lines, i, "figure"); i = e; out.push(...figure(body.join("\n")));
    } else if ((m = /^\\begin\{(equation\*?|align\*?)\}/.exec(l))) {
      flush(); const [body, e] = between(lines, i, m[1]); i = e; out.push(equation(body));
    } else if ((m = /^\\input\{(chapters\/figures\/[^}]+)\}/.exec(l))) {
      flush(); out.push(...figure(rd(m[1] + ".tex")));
    } else if ((m = /^\\keywords\{(.*)\}/.exec(l))) {
      flush(); out.push(para([{ text: "מילות מפתח: ", bold: true }, ...parseInline(m[1])], { color: C.screen }));
    } else if ((m = /^\\pythonfile(?:\[([^\]]*)\])?\{([^}]+)\}\{(.*)\}/.exec(l))) {
      flush(); out.push(...codeBox(m[1] || "", m[2], m[3]));
    } else if (/^\\(begin|end)\{(sloppypar|center|flushright|otherlanguage)\}|^\\(markboth|addcontentsline|label|clearpage|newpage|vspace|medskip|bigskip|noindent)/.test(l)) {
      // עטיפות ופקודות פריסה: מדלגים
      if (/^\\label/.test(l) === false) continue;
    } else buf.push(l);
  }
  flush();
  return out;
}

// ---------------------------------------------------------------- בניית המסמך
const order = [...rd("main.tex").matchAll(/^\\input\{(chapters\/0[^}]+)\}/gm)].map((m) => m[1]);
const lines = (f) => rd(f + ".tex").split(/\r?\n/);
const abstract = blocks(lines(order[0]));
const chapters = order.slice(1).flatMap((f) => blocks(lines(f)));

const cover = [
  new Paragraph({ spacing: { before: 600 }, alignment: AlignmentType.CENTER,
    children: runs([{ text: "מחוברים תמיד" }], { font: HEAD, size: 72, bold: true, color: C.night }) }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 300 },
    children: runs([{ text: "טכנולוגיה וחיי היומיום" }], { font: HEAD, size: 36, color: C.screen }) }),
  image("images/cover_network.png", 420),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 300 },
    children: runs([{ text: "ספר שנכתב ב-LaTeX בעזרת צוות סוכני בינה מלאכותית" }], { font: HEAD, size: 24, color: C.ink }) }),
  new Paragraph({ alignment: AlignmentType.CENTER,
    children: runs([{ text: "שנהב סולימן  |  2026" }], { font: HEAD, size: 22, color: C.muted }) }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 400 },
    children: runs([{ text: "גרסת Word לעריכה. המקור הרשמי הוא קובצי ה-LaTeX וה-PDF שנבנה מהם." }], { size: 18, color: C.muted }) }),
];
const toc = [
  new Paragraph({ heading: HeadingLevel.HEADING_1, bidirectional: true, pageBreakBefore: true,
    children: runs([{ text: "תוכן העניינים" }], { font: HEAD, size: 40, bold: true, color: C.night }) }),
  new TableOfContents("תוכן העניינים", { hyperlink: true, headingStyleRange: "1-2" }),
];
const biblio = [
  new Paragraph({ heading: HeadingLevel.HEADING_1, bidirectional: true, pageBreakBefore: true,
    children: runs([{ text: "רשימת מקורות" }], { font: HEAD, size: 40, bold: true, color: C.night }) }),
  ...citeOrder.map(bibEntry).map((e, i) => new Paragraph({
    alignment: AlignmentType.LEFT, indent: { left: 720, hanging: 720 }, spacing: { after: 100 },
    children: [
      new TextRun({ text: `[${i + 1}]  ${e.who}, `, font: LATIN, size: 21 }),
      new TextRun({ text: `“${e.title},” `, font: LATIN, size: 21 }),
      new TextRun({ text: `${e.year}. `, font: LATIN, size: 21 }),
      new TextRun({ text: e.src ? `${e.src}. ` : "", font: LATIN, size: 21 }),
      new TextRun({ text: e.link, font: LATIN, size: 21, color: C.screen }),
    ],
  })),
];

const level = (lvl, fmt, text, color) => ({
  level: lvl, format: fmt, text, alignment: AlignmentType.START,
  style: { paragraph: { indent: { left: 540 + 420 * lvl, hanging: 300 } }, run: { color, bold: true } },
});
const doc = new Document({
  creator: "מחוברים תמיד", title: "מחוברים תמיד: טכנולוגיה וחיי היומיום",
  features: { updateFields: true },
  styles: {
    default: { document: { run: { font: { ascii: LATIN, hAnsi: LATIN, cs: BODY }, size: SZ, sizeComplexScript: SZ, color: C.ink, rightToLeft: true } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: HEAD, size: 40, bold: true, color: C.night },
        paragraph: { spacing: { before: 0, after: 300 }, keepNext: true, outlineLevel: 0,
          border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: C.screen, space: 6 } } } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: HEAD, size: 28, bold: true, color: C.screen },
        paragraph: { spacing: { before: 300, after: 120 }, keepNext: true, outlineLevel: 1 } },
    ],
  },
  numbering: { config: [
    { reference: "bullet", levels: [level(0, LevelFormat.BULLET, "●", C.screen), level(1, LevelFormat.BULLET, "◂", C.notif)] },
    { reference: "num", levels: [level(0, LevelFormat.DECIMAL, "%1.", C.screen), level(1, LevelFormat.DECIMAL, "%2.", C.screen)] },
    { reference: "check", levels: [level(0, LevelFormat.BULLET, "☐", C.leaf)] },
  ] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, bottom: 1300, left: 1300, right: 1300 } } },
    headers: { default: new Header({ children: [new Paragraph({ bidirectional: true, alignment: AlignmentType.LEFT,
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: C.screen, space: 4 } },
      children: runs([{ text: "מחוברים תמיד: טכנולוגיה וחיי היומיום" }], { font: HEAD, size: 18, color: C.muted }) })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ children: [PageNumber.CURRENT], font: HEAD, size: 20, color: C.night, bold: true })] })] }) },
    children: [...cover, ...abstract, ...toc, ...chapters, ...biblio],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(path.join(ROOT, "book.docx"), buf);
  console.log("book.docx written:", chapterNo, "chapters,", Object.keys(bib).length, "sources");
});
