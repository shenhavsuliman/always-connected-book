# דוח Fixer – סבב 1

קלט: `qa/reports/detector-round-1.md` (16 ממצאים: 0 critical, 6 major, 10 minor). תבנית: `connected.cls` **v2.3.0 → v2.4.0** (נוסף גם `connected.lua`). אחרי התיקונים: `bash build.sh` עבר (32 עמודים), `python qa/qa_check.py`: **0 FAIL, 0 WARN**, ולא נשארו אזהרות Underfull או Overfull ב-`main.log`. כל תיקון נבדק ויזואלית על ה-PDF.

**סיכום: 15 FIXED, 1 OPEN (minor).**

| ID | איפה תוקן | מה שונה | לפני → אחרי | סטטוס |
|---|---|---|---|---|
| CODE-01 | template: `connected.lua`, `\pythonfile` ב-`connected.cls` | הטווח נחתך לקובץ זמני (`*.pysnip`) לפני ש-`listings` קורא אותו | שורה 1 עברית מבולבלת חורגת מהתיבה → תיבה שמתחילה ב-`def goldilocks():` | FIXED |
| QA-01 | `qa/qa_check.py` (`code`), `qa/known-warnings.md` | נוספו: בדיקה ששורה ראשונה ואחרונה של הטווח מופיעות ב-PDF, ובדיקת טקסט החורג משולי העמוד. ההערה על האזהרה המוכרת תוקנה. | PASS שגוי → הבדיקה הייתה נכשלת על הדליפה | FIXED |
| BIDI-01 | template: גופן עברי (`\babelfont[hebrew]{rm}`); `qa/qa_check.py` (`bidi`) | David הוחלף ב-Times New Roman (ב-David הגליפים `:` ו-`;` צרים עם רווח סביבם). נוספה בדיקה שנכשלת אם `:` או `;` מוצבים ב-David. | "השימוש : קשר" → "השימוש: קשר" (טקסט, כותרות, תוכן עניינים) | FIXED |
| IMG-01 | template: `\topfraction`, `\textfraction`, `\floatpagefraction`; `qa/qa_check.py` (`img`) | עמוד צפים חייב להיות מלא 80%, ואיור יכול לעלות לראש עמוד עם טקסט מתחתיו. נוספה בדיקת "איור לבד בעמוד". | איור 4.1 לבד בעמוד חצי ריק → איור בראש עמוד 11 עם טקסט מתחתיו | FIXED |
| IMG-02 | `chapters/figures/*.tex` ו-`06-smart-home.tex` (`\caption[קצר]{ארוך}`), `qa/qa_check.py` (`img`) | כיתוב קצר לכל חמשת האיורים. נוספה בדיקה לכיתובים ארוכים ב-`main.lof`. | רישום שבור וארוך ברשימת האיורים → שורה אחת לכל איור | FIXED |
| TYPE-01 | template: `\appto{\bibsetup}{\raggedright}` ועונשי שבירה ל-URL | רשימת המקורות בלי צדק, וכתובות נשברות בקווים נוספים | "https : / / datareportal . com" → כתובת רציפה שנשברת בסוף שורה | FIXED |
| CODE-02 | template: `connected.lua` (סימון כיוון LRM/RLM אחרי רצפים עבריים בקוד) | המרכאה והפסיק שאחרי מחרוזת עברית נשארים במקומם, וסדר המילים בתוך המחרוזת נכון | `("סמארטפון", ...` מבולבל → מחרוזות עבריות קריאות | OPEN: נשארו סוגריים בתוך שתי מחרוזות (`"מחשב (פנאי)"` ו-`(שיא: ...`) שמוצגים מחוץ למקומם. `bidi=basic` לא מזווג סוגריים. תיקון מלא דורש לשנות את תוויות הגרף (תוכן), ולכן לא בוצע. |
| CODE-03 | `chapters/09-appendix-code.tex` (`lastline=127`), `python/make_graphs.py` (פיצול שלוש שורות ארוכות, בלי שינוי לוגי), template (`firstnumber`, `left=24pt`) | כל הפונקציה מוצגת, מספרי השורות אמיתיים (93-127), ולא נחתכים | פונקציה נחתכת ושורות מ-1 → פונקציה שלמה בשורות 93-127; אזהרת שורות ארוכות נעלמה | FIXED |
| TYPE-02 | `chapters/07-balance.tex` (`\Needspace{6\baselineskip}`), template (`needspace`, `\widowpenalty`, `\clubpenalty`) | פסקת ההקדמה עוברת יחד עם הרשימה. נוסף מניעת שורה בודדת בראש או בתחתית עמוד. | "ולבסוף..." לבדה בתחתית עמוד 20 → עוברת לעמוד הבא עם הרשימה | FIXED |
| TYPE-03 | template: `\emergencystretch` 3em → 8em; `qa/qa_check.py` (`typeset`) | פחות שורות מתוחות. הבדיקה סופרת עכשיו Underfull. | 3 אזהרות Underfull → 0 | FIXED |
| TYPE-04 | `qa/known-warnings.md`, `qa/qa_check.py` (`typeset`) | האזהרות של biblatex על שפה לא נתמכת מוסברות (רשימת המקורות באנגלית). הבדיקה דורשת שכל אזהרת חבילה תופיע ברשימה. | אזהרה לא מוסברת → מוסברת, ו-qa_check עובר | FIXED |
| TYPE-05 | template: `\pagenumbering` ו-`\connected@pagetotal`; `qa/qa_check.py` (`typeset`) | בחזית הספר הסך הכולל הוא העמוד הרומי האחרון (נכתב ל-aux). נוספה בדיקה לערבוב סוגי מספור. | "עמוד iv מתוך 26" → "עמוד iv מתוך v" | FIXED |
| BIDI-02 | template: `\makecover` | תג ההתראה הועלה מ-2.5 ל-1.95 ס"מ מראש העמוד | התג נוגע באות בכותרת → רווח ברור מעל הכותרת | FIXED |
| TAB-01 | `chapters/02-history.tex` (מפרט עמודות) | עמודת "שנה" הורחבה מ-2.7 ל-3.9 ס"מ | תאים בשתי ושלוש שורות → תא בשורה אחת | FIXED |
| IMG-03 | `python/make_images.py`, `chapters/06-smart-home.tex` | גופני התוויות הוגדלו (9→12, 13→16, 12→15, 10→14), הבית הורחב, ורוחב האיור 0.72→0.85 | תוויות זעירות → תוויות קריאות בהדפסה, בלי חפיפות | FIXED |
| INFRA-01 | `qa/qa_check.py` (`infra`), README | בדיקת stray: כל קובץ בשורש שאינו תוצר בנייה חייב להופיע ב-README או ברשימת המבנה. `book.docx` ו-`word/` כבר מתועדים ב-README (שורות 10, 95, 118), ולכן נשארו. | "none" שגוי → הבדיקה הכללית עובדת ולא מדווחת על קבצים מתועדים | FIXED |

## חריגה מההגדרה המקורית

- הגופן העברי הוחלף. הוא משפיע על מראה הספר כולו (David ל-Times New Roman), אבל לא על התוכן. מספר העמודים נשאר 32.
- `connected.lua` הוא קובץ חדש בשורש, ונדרש ליד `connected.cls`. הוא מוסבר ב-`template/CHANGELOG.md` וב-`template/COMMANDS.md`.

## מה שנוסף

- `template/CHANGELOG.md`: רשומה v2.4.0 עם מזהי הממצאים. `REQUIRED_CLS = "2.4.0"` ב-`qa/qa_check.py`. `template/COMMANDS.md` עודכן.
- `docs/incidents.md`: INC-13 עד INC-16 (שורות דילוג של listings ואזהרה מוכרת שהסתירה אותן; פיסוק מרווח ב-David; פערי בדיקה אוטומטיים; סקריפט שיצר תווי בקרה בתבנית).
- `.gitignore`: נוספו `*.pysnip`, `*.lof`, `*.lot`.
- נמחקו כל קובצי ה-PNG הזמניים ב-`qa/reports/`.
