<div dir="rtl">

# 📱 מחוברים תמיד: טכנולוגיה וחיי היומיום
### *Always Connected: Technology and Everyday Life*

ספר מקצועי בעברית ואנגלית משולבת, ברמת הוצאה לאור, 32 עמודים: שער לא ממוספר, ועוד 31 עמודים ממוספרים ("עמוד N מתוך 31"). הוא הופק כולו בקוד:
- **LuaLaTeX**, עם תבנית `.cls` משלי
- **Python** לגרפים ולאיורים
- **TikZ** לתרשימים

את העבודה עשה **צוות של 8 תפקידי סוכנים** (ועדת מומחים, חוקר, כותב, עורך, מגיה, Detector, Fixer וצוות אדום), ומעליהם סוכן Master.
**כלל התיקון ("חוק הברזל" של המטלה):** אף בעיית **עיצוב, עימוד או כיוון** לא תוקנה ישירות בטקסט. היא תוקנה בתבנית או בסקיל, כדי שלא תחזור. רק **תוכן** (ניסוח, נתון או מקור) תוקן בטקסט עצמו, כי שם הוא נמצא:
- **תקלה שחוזרת** (BiDi, עימוד, תיבות או ציטוטים) תוקנה בתבנית `connected.cls`, ומספר הגרסה עלה. היסטוריית הגרסאות ב-[CHANGELOG](template/CHANGELOG.md).
- **תקלה במקום אחד** (ניסוח, נתון, סדר בטבלה או מיקום תווית באיור) תוקנה בשורה עצמה. בסבבים 1 עד 5 התיקונים נעשו על ידי סוכן העורך ונרשמו ב-[editor-report](research/editor-report.md). בסבבים 6 ו-7 הם נעשו על ידי ה-Master ונרשמו בדוחות ה-Fixer ([fixer-round-6](qa/reports/fixer-round-6.md), [fixer-round-7](qa/reports/fixer-round-7.md)).

📕 **[book.pdf](book.pdf)**: הספר הסופי &nbsp;·&nbsp; 📋 **[PRD.md](PRD.md)** &nbsp;·&nbsp; 🗺️ **[PLAN.md](PLAN.md)** &nbsp;·&nbsp; ✅ **[TODO.md](TODO.md)** &nbsp;·&nbsp; 📝 [book.docx](book.docx) (גרסת Word לקריאה)

> **הקול האישי:** הספר נכתב **בהשראת הסגנון של יובל נח הררי**: מבט היסטורי רחב, משפטים קצרים ושאלות פתוחות לקורא.
> **השפה העיצובית היא של "מסך":** כחול-לילה למסך כבוי, טורקיז למסך דולק, ו**נקודת התראה אדומה** שחוזרת בשער, בכותרות הפרקים ובבאנר.

---

## 🖼️ מתוך הספר

| שער | פתיחת פרק + באנר | תרשים בלוקים (TikZ, 8 שלבים) |
|:---:|:---:|:---:|
| <img src="docs/screenshots/01-cover.png" width="260"> | <img src="docs/screenshots/03-chapter.png" width="260"> | <img src="docs/screenshots/06-diagram.png" width="260"> |
| **נוסחה בתיבה + גרף Python** | **טבלה: ציר זמן** | **תיבת קוד (pythonbox)** |
| <img src="docs/screenshots/07-formula.png" width="260"> | <img src="docs/screenshots/04-table.png" width="260"> | <img src="docs/screenshots/11-code.png" width="260"> |
| **תוכן עניינים** | **רשימת תיוג ותיבות** | **מקורות IEEE** |
| <img src="docs/screenshots/02-toc.png" width="260"> | <img src="docs/screenshots/09-checklist.png" width="260"> | <img src="docs/screenshots/10-bibliography.png" width="260"> |
| **גרף Python: זמן יומי ברשת** | **איור מקוד: הבית החכם** | |
| <img src="docs/screenshots/05-graph.png" width="260"> | <img src="docs/screenshots/12-smart-home.png" width="260"> | |

**איורים וגרפים**, כולם נוצרו בקוד ואין בהם תמונה מהאינטרנט:

<p align="center">
<img src="images/attention_loop.png" width="330">&nbsp;<img src="images/goldilocks.png" width="430">
</p>

---

## 🤖 צוות הסוכנים בפעולה

<p align="center"><img src="docs/screenshots/agents-in-action.png" width="820"></p>
<p align="center"><em>נתוני ריצה אמיתיים של כל סוכן: זמן, טוקנים ומודל (מתוך <a href="docs/agent-runs.json">docs/agent-runs.json</a>)</em></p>

```
                          ┌───────────────────────────────┐
                          │    MASTER (מנהל, Opus)         │
                          │ תבנית · גרפים · אינטגרציה · Git │
                          └───────────────┬───────────────┘
   ┌──────────────┬───────────────┬───────┴──────┬───────────────────────────────┐
   ▼              ▼               ▼              ▼                               ▼
┌────────┐   ┌─────────┐    ┌──────────┐   ┌──────────┐          ┌──────────────────────────────┐
│ ועדת   │   │ חוקר    │──▶│ כותב      │──▶│ עורך      │──────▶  │    לולאת "צוות אדום"           │
│ מומחים │   │ Sonnet  │    │ Opus     │   │ Opus     │          │ Detector ──▶ Fixer ──▶ Detector │
│ →PRD   │   │ 20 מקורות│    │ 8 פרקים  │   │ 19 תיקונים│          │ (qa-super)  (qa-fixer) (אימות) │
└────────┘   └─────────┘    └──────────┘   └──────────┘          │        + red-team (בוחן)      │
                                                                  └──────────────────────────────┘
```

| סוכן | Skill | מודל | מה עשה |
|------|-------|------|--------|
| **ועדת מומחים** | [04-expert-committee](prompts/04-expert-committee.md) | Sonnet | 5 מומחים, 28 קריטריוני קבלה מדידים, והם הבסיס ל-PRD ([docs/expert-committee.md](docs/expert-committee.md)) |
| **חוקר** | [book-researcher](.claude/skills/book-researcher/SKILL.md) | Sonnet | 20 מקורות אמיתיים, וגיליון עובדות שמסמן מה **לא** אומת |
| **כותב** | [book-writer](.claude/skills/book-writer/SKILL.md) | Opus | 8 פרקים ותקציר בסגנון הררי, רק עם נתונים מאומתים |
| **עורך** | [book-editor](.claude/skills/book-editor/SKILL.md) | Opus | 19 תיקוני עובדות ושפה וציון 7.5/10; בסבבים 2 ו-4 תיקן את ממצאי התוכן |
| **מגיה** | [book-editor](.claude/skills/book-editor/SKILL.md) ([08-proofreader](prompts/08-proofreader.md)) | Opus | הגהה מלאה: 33 תיקוני דקדוק, סגנון וכיוון, ומילון מונחים אחיד |
| **Detector** | [qa-super](.claude/skills/qa-super/SKILL.md) + 7 סקילים | Sonnet | מגלה תקלות ואינו מתקן |
| **Fixer** | [qa-fixer](.claude/skills/qa-fixer/SKILL.md) | Sonnet | מתקן במקום הנכון: תבנית, סקיל או שורה בודדת |
| **צוות אדום** | [red-team](.claude/skills/red-team/SKILL.md) | Sonnet | מחפש את 10 נקודות התורפה של הספר, בלי מחמאות |

**ניהול משאבים:** משימות של חיפוש ובדיקה רצו על Sonnet, שזול יותר. כתיבה, עריכה, הגהה והבודק המחמיר רצו על Opus. כל הסוכנים רצו ברקע, במקביל לעבודת ה-Master.
**סך הכול:** הנתונים המלאים לכל ריצה ב-[docs/agent-runs.json](docs/agent-runs.json), והם לא כוללים את ה-Master.

**עלות משוערת:**
- **מחירים** (API, נובמבר 2026): Sonnet 5.5 עולה ‎$2‎ למיליון טוקני קלט ו-‎$10‎ למיליון טוקני פלט. Opus 5.5 עולה ‎$4‎ ו-‎$20‎.
- **הנחה:** רוב הטוקנים בריצות של סוכנים הם קלט, כלומר קריאת קבצים והקשר. לכן הטווח מחושב בין 0% ל-10% פלט.
- **תוצאה:** 17 ריצות, כ-2.42 מיליון טוקנים (כ-0.86 מיליון ב-Sonnet וכ-1.57 מיליון ב-Opus). העלות המשוערת היא כ-‎$8‎ עד ‎$11‎ לכל ריצות הסוכנים יחד. העבודה בוצעה במנוי Claude, לא בחיוב לפי API, ולכן זו המחשה של סדר הגודל ולא חשבון בפועל.
- **בחירת המודלים** (Sonnet לבדיקה, Opus לעברית) חסכה כ-18% לעומת הרצה של הכול על Opus. החישוב: הטוקנים של Sonnet במחיר של Opus היו מוסיפים כ-‎$1.7‎ עד ‎$2.4‎.

---

## 📸 תהליך העבודה והקוד: צילומי מסך

צילומים אמיתיים של המאגר, הדוחות והקוד, כפי שהם מוצגים ב-GitHub, ופלט של הרצה אמיתית.

### התהליך
| היסטוריית העבודה: commit נפרד לתבנית, לבדיקות, לתוכן ולמסמכים | הבודק המחמיר, סבב 4: הציון 82/100 וטבלת הניכויים |
|:---:|:---:|
| <img src="docs/screenshots/process/01-commits.jpg" width="420"> | <img src="docs/screenshots/process/02-strict-grader-82.jpg" width="420"> |
| **דוח Fixer, סבב 7: לכל תיקון יש ראיה (INC-28, ‏INC-30)** | **13 ה-Skills ב-`.claude/skills/`** |
| <img src="docs/screenshots/process/03-fixer-evidence.jpg" width="420"> | <img src="docs/screenshots/process/04-skills.jpg" width="420"> |

### הקוד
| התבנית `connected.cls`: גרסה, תאריך ובדיקת LuaLaTeX | התבנית: תיבות עם מסגרת LTR ותוכן עברי (INC-08) |
|:---:|:---:|
| <img src="docs/screenshots/process/05-code-cls-header.jpg" width="420"> | <img src="docs/screenshots/process/06-code-cls-boxes.jpg" width="420"> |
| **`qa_check.py`: בדיקת BiDi גאומטרית (תחיליות, ציטוטים)** | **`overlap_check.py`: בדיקת חפיפות באיורים ובגרפים** |
| <img src="docs/screenshots/process/07-code-qa-bidi.jpg" width="420"> | <img src="docs/screenshots/process/08-code-overlap-check.jpg" width="420"> |
| **`make_graphs.py`: מילון תוויות עברי והפונקציה `goldilocks()`** | **הרצה אמיתית: בנייה, עמוד בדיקה, QA ו-git log** |
| <img src="docs/screenshots/process/09-code-graphs.jpg" width="420"> | <img src="docs/screenshots/process/10-build-and-qa-run.png" width="420"> |

> הסוכנים עצמם רצו ברקע, ולכן אין צילום מסך של הרגע שבו הם רצו. העדות לעבודתם היא הגרף "צוות הסוכנים בפעולה" שלמעלה, שנבנה מנתוני הריצה האמיתיים, והדוחות שכל סוכן כתב ב-[qa/reports/](qa/reports).

---

## 🔴 לולאת בקרת האיכות: Detector ⇄ Fixer

| סבב | מי | תוצאה | דוח |
|-----|----|-------|-----|
| 1 | Detector | 0 קריטיים · 6 מהותיים · 10 קלים, **NOT READY** | [detector-round-1](qa/reports/detector-round-1.md) |
| 1 | Fixer | 15 תוקנו, 1 פתוח (קל ומתועד). התבנית עלתה ל-v2.4.0 | [fixer-round-1](qa/reports/fixer-round-1.md) |
| 2 | Detector | 15 תיקונים אומתו, 0 נסיגות. 1 מהותי ו-6 קלים חדשים | [detector-round-2](qa/reports/detector-round-2.md) |
| — | red-team | 10 נקודות תורפה בתוכן ובטיעון | [red-team](qa/reports/red-team.md) |
| 2 | עורך + Master | תיקון נקודות הצוות האדום בתוכן. התבנית עלתה ל-v2.5.0 | [editor-report](research/editor-report.md) |
| 3 | Detector (שער סופי) | כל ממצאי סבב 2 אומתו, 0 נסיגות. 1 מהותי ו-4 קלים | [detector-round-3](qa/reports/detector-round-3.md) |
| 3 | Master | כל ממצאי סבב 3 תוקנו. התבנית עלתה ל-v2.5.1 | [CHANGELOG](template/CHANGELOG.md) |
| 4 | מגיה | הגהה מלאה: 33 תיקוני דקדוק, סגנון וכיוון | [editor-report](research/editor-report.md) |
| 4 | Detector מחמיר (Opus) | סימולציה של בודק לציון 100: **82/100**, 9 מהותיים ו-20 קלים | [detector-round-4](qa/reports/detector-round-4.md) |
| 4 | Fixer (עורך + Master) | 27 תוקנו ו-2 נשארו בהחלטה מנומקת. תבנית v2.5.2, ו-5 בדיקות אוטומטיות חדשות | [fixer-round-4](qa/reports/fixer-round-4.md) |
| 5 | Detector מחמיר (Opus) | **91/100**. 22 תיקונים אומתו, ונמצאה נסיגה אחת (BIDI-05) | [detector-round-5](qa/reports/detector-round-5.md) |
| 5 | Fixer (עורך + Master) | תבנית v2.5.3, בדיקת חפיפה בגרפים, מקור OII, ו-INC-22 עד INC-24. **4 שורות סומנו FIXED בטעות**, ותוקנו בסבב 6 (INC-28) | [fixer-round-5](qa/reports/fixer-round-5.md) |
| 6 | Detector מחמיר (Opus) | **94/100**. 13 תיקונים אומתו, 0 נסיגות, 3 מהותיים ו-10 קלים | [detector-round-6](qa/reports/detector-round-6.md) |
| 6 | Fixer (Master) | כל ממצא עם ראיה. תבנית v2.5.4, בדיקת חפיפה גם באיורים, בדיקת כיוון לרשימות, ו-INC-25 עד INC-29 | [fixer-round-6](qa/reports/fixer-round-6.md) |
| 7 | Detector מחמיר (Opus) | **96/100**. 0 קריטיים, 2 מהותיים ו-7 קלים. כל ראיה של ה-Fixer הורצה מחדש | [detector-round-7](qa/reports/detector-round-7.md) |
| 7 | Fixer (Master) | כל הממצאים תוקנו או נשארו בהחלטה מנומקת (BIB-01). INC-30 | [fixer-round-7](qa/reports/fixer-round-7.md) |

> הציונים בטבלה הם **הערכה פנימית של סוכן הבודק**, ששימשה למדידת התקדמות בין הסבבים. הם לא ציון ולא טענה על הציון.

**חוק הברזל:** כל תיקון שחוזר בכמה מקומות בספר בוצע ב-[connected.cls](connected.cls), ו**הגרסה עלתה**. היסטוריית הגרסאות נמצאת ב-[CHANGELOG](template/CHANGELOG.md). כשה-Detector מצא תקלה שהבודק האוטומטי פספס, הבודק עצמו ([qa/qa_check.py](qa/qa_check.py)) תוקן כדי שיתפוס אותה בפעם הבאה.

### 🔍 חקרי אירוע
לכל תקלה נשאלו שתי שאלות: **למה היא קרתה**, ו**למה היא לא התגלתה קודם**. מהתשובות נגזר מנגנון המניעה. **30 חקרי אירוע** נמצאים ב-[docs/incidents.md](docs/incidents.md), ומתוכם, למשל:
- **INC-05:** סקריפט Python כתב `\r`, `\f` ו-`\b` כתווי בקרה בקובצי LaTeX, **שלוש פעמים**. הלקח נשאר הערה בפרומפט ולא הפך לבדיקה, ולכן לא נעצר. עכשיו `qa-infra` סורק כל קובץ.
- **INC-11:** הגרסה הראשונה נבנתה לפי תמלול משובש של השיעור, עם XeLaTeX ו-APA, במקום המסמך הרשמי (LuaLaTeX ו-IEEE). העורך בדק את הספר **מול אותו PRD שגוי**, ולכן לא תפס את הטעות.
- **INC-13:** "אזהרה מוכרת" הסתירה דליפת קוד. **אזהרה שמסבירים אותה לפני שבודקים היא תקלה מוסתרת.**

---

## 🧰 ה-Skills (13)

| Skill | תפקיד |
|-------|-------|
| [qa-super](.claude/skills/qa-super/SKILL.md) | אורקסטרטור, ה-Detector. מריץ את כל משפחת ה-QA בסדר קבוע |
| [qa-bidi](.claude/skills/qa-bidi/SKILL.md) | עברית ואנגלית: מילים הפוכות, מספרים, טווחים, סוגריים |
| [qa-table](.claude/skills/qa-table/SKILL.md) | עמודה ראשונה מימין, כיתוב מעל, רוחב |
| [qa-code](.claude/skills/qa-code/SKILL.md) | רקע של pythonbox, גלישת שורות, גופן עם עברית |
| [qa-img](.claude/skills/qa-img/SKILL.md) | כיתוב, הפניה, מיקום, אין זכויות יוצרים |
| [qa-typeset](.claude/skills/qa-typeset/SKILL.md) | שגיאות, overfull ו-underfull, כותרות יתומות |
| [qa-infra](.claude/skills/qa-infra/SKILL.md) | מבנה פרויקט, קבצים נדרשים, תווי בקרה |
| [qa-cls-version](.claude/skills/qa-cls-version/SKILL.md) | גרסת התבנית מול התקן, CHANGELOG, פקודות מותרות |
| [qa-fixer](.claude/skills/qa-fixer/SKILL.md) | ה-Fixer |
| [red-team](.claude/skills/red-team/SKILL.md) | בוחן קפדן |
| [book-researcher](.claude/skills/book-researcher/SKILL.md) · [book-writer](.claude/skills/book-writer/SKILL.md) · [book-editor](.claude/skills/book-editor/SKILL.md) | סוכני התוכן |

כל הפרומפטים ששלחתי לסוכנים נמצאים ב-[prompts/](prompts), מהמשימה הראשונה ועד הצוות האדום.

---

## 🛠️ בנייה ורפרודוסיביליות

**דרישות:**
- MiKTeX עם LuaLaTeX ו-biber
- Python 3 עם `matplotlib>=3.11 numpy pymupdf`
- גופני Windows: Times New Roman, Gisha, Segoe UI, Courier New

> **מגבלה ידועה:** התבנית משתמשת בגופנים שמגיעים עם Windows. על Mac או Linux צריך להתקין אותם, או להחליף אותם ב-`abelfont` שבראש `connected.cls`.

```bash
bash build.sh          # גרפים → lualatex → biber → lualatex ×2 → book.pdf
bash build.sh test     # וגם עמוד הבדיקה של התבנית (tests/stress-test.tex)
python qa/qa_check.py  # הבדיקות האוטומטיות של כל משפחות ה-QA
```

## 📁 מבנה הפרויקט
```
always-connected-book/
├── main.tex                    ← הקובץ הראשי
├── connected.cls  connected.lua ← התבנית (v2.5.4) ועזר Lua לתיבות הקוד
├── refs.bib                    ← 20 מקורות (IEEE)
├── chapters/                   ← תקציר, 8 פרקים, נספח קוד, figures/
├── python/                     ← make_graphs · make_images · make_agents_chart · render_pages
├── images/                     ← כל האיורים, מקוד בלבד
├── template/                   ← CHANGELOG.md · COMMANDS.md
├── tests/stress-test.tex       ← עמוד בדיקה לתבנית (Prompt B4 בחוברת)
├── .claude/skills/             ← 13 Skills
├── qa/                         ← qa_check.py · known-warnings.md · reports/
├── prompts/                    ← כל הפרומפטים לסוכנים
├── research/                   ← facts.md · editor-report.md
├── docs/                       ← expert-committee · incidents · assignment-requirements · screenshots
├── word/                       ← make_docx.js: ממיר LaTeX → Word (book.docx)
├── PRD.md · PLAN.md · TODO.md · README.md · build.sh
└── book.pdf                    ← התוצר הסופי
```

</div>
