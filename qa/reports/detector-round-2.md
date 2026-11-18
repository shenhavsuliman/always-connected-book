# דוח Detector – סבב 2 (סבב אימות)

בדיקה על `main.pdf` הנוכחי (32 עמודים פיזיים; מספור i–v ואז 1–26), `connected.cls` v2.4.0 + `connected.lua`. לא בוצעה בנייה מחדש. חלק אוטומטי: `qa/qa_check.py` = 0 FAIL, 0 WARN, 54 PASS. סקירה ויזואלית של כל 32 העמודים (מונטז'ים) והגדלה של עמודי הקוד (29–30) ועמוד 20. `main.log`: 0 Overfull, 0 Underfull, 0 Missing character; אזהרת ה-1782pt נעלמה, כצפוי. לא נמצא ממצא REGRESSED.

## 1. אימות ממצאי סבב 1

| ID | סטטוס | הערה |
|---|---|---|
| CODE-01 | VERIFIED-FIXED | התיבה מתחילה ב-`def goldilocks():`, אין שורה עברית דולפת, אין טקסט מעבר לשוליים. |
| QA-01 | VERIFIED-FIXED | `qa_check code` בודק שורה ראשונה/אחרונה בטווח ומקטעי טקסט מעבר לשוליים. (ראו QA-02: עדיין לא תופס מחרוזות עבריות בקוד.) |
| BIDI-01 | VERIFIED-FIXED | נקודתיים/נקודה-פסיק צמודים למילה בגוף, בכותרות ובתוכן העניינים (Times New Roman). |
| IMG-01 | VERIFIED-FIXED | איור 4.1 בראש עמוד 11 עם טקסט מתחתיו. אין איור לבדו בעמוד. |
| IMG-02 | VERIFIED-FIXED | רשימת האיורים: שורה אחת לכל איור, יישור אחיד. |
| TYPE-01 | VERIFIED-FIXED | כתובות URL ברשימת המקורות נשברות בסוף שורה, בלי מתיחה. |
| CODE-02 | **STILL-OPEN** | ראו CODE-02 למטה: ההיקף רחב ממה שדווח, לא רק סוגריים. |
| CODE-03 | VERIFIED-FIXED | הפונקציה שלמה (שורות 93–127), מספור אמיתי. (נשארות בעיות עטיפה: CODE-05.) |
| TYPE-02 | VERIFIED-FIXED | "ולבסוף..." עברה עם הרשימה לראש עמוד 20. |
| TYPE-03 | VERIFIED-FIXED | 0 אזהרות Underfull. |
| TYPE-04 | VERIFIED-FIXED | האזהרות מוסברות ב-`qa/known-warnings.md`. |
| TYPE-05 | VERIFIED-FIXED | "עמוד iv מתוך v" (רומי). |
| BIDI-02 | VERIFIED-FIXED | תג ההתראה בשער לא נוגע בכותרת. |
| TAB-01 | VERIFIED-FIXED | עמודת "שנה" בשורה אחת בכל התאים. |
| IMG-03 | VERIFIED-FIXED | תוויות איור 6.1 גדולות וקריאות, ללא חפיפה. |
| INFRA-01 | VERIFIED-FIXED | הקבצים מתועדים ב-README. (ראו INFRA-02.) |

## 2. טבלת סיכום (ממצאים פתוחים וחדשים)

| משפחה | critical | major | minor |
|---|---|---|---|
| infra | 0 | 0 | 1 |
| cls-version | 0 | 0 | 1 |
| typeset | 0 | 0 | 1 |
| bidi | 0 | 0 | 0 |
| table | 0 | 0 | 0 |
| img | 0 | 0 | 0 |
| code | 0 | 1 | 2 |
| qa-tooling | 0 | 0 | 1 |
| **סה"כ** | **0** | **1** | **6** |

## 3. טבלת ממצאים

| ID | עמוד | משפחה | ראיה | כלל שנשבר | חומרה | איפה התיקון |
|---|---|---|---|---|---|---|
| CODE-02 (STILL-OPEN, הוחמר מ-minor) | 23–24 (pdf 29–30) | code | מחרוזות עבריות בקוד עדיין מבולבלות, ולא רק סוגריים: שורה 108 `label=he(f"{name} שיא(: ...` (נקודתיים וסוגר במקום שגוי); שורה 112 `he("נוספת מורידה רווחה\מעל השיא: כל שעה")` (סדר המילים, `\` ו-`:` מחוץ למקומם, אות `n` של `\n` מופרדת); שורות 116–117 `(t)` ו-`W(t)` בקצה הלא נכון; שורות 121 ו-124 נקודתיים/נקודה-פסיק ו-`Przybylski &` מחוץ למקום. בשורות 96–99 סדר המילים תקין אך המרכאות והפסיק צמודים לצד הלא נכון. | qa-code: הערות/מחרוזות עבריות לא מבלבלות שורה; qa-bidi כלל 4 | major | `python/make_graphs.py` (מחרוזות באנגלית בטווח 93–127, או להציג אותן בתווית `he(...)` מפורשת) או `connected.lua` (סימון כיוון גם סביב `:`/`;`/`\`/סוגריים בתוך מחרוזת). הפרמטר הוא תוכן הגרף, לכן עדיף לבחור טווח/תוויות שאינם עבריים. |
| CODE-04 | 23→24 | code | תיבת הקוד נשברת בין עמודים: עמוד 23 נגמר באמצע הפונקציה (שורה 119) ועמוד 24 מתחיל בתיבה בלי שורת כותרת (שורות 120–127). | qa-typeset: תיבה לא נשברת באופן מביך | minor | `chapters/09-appendix-code.tex` (`\Needspace`/תחילת הנספח בעמוד חדש), או `connected.cls`: כותרת חוזרת ב-`breakable` של `pythonbox` |
| CODE-05 | 23–24 | code | שורות ארוכות נעטפות בלי הזחה תלויה: המשך שורות 94, 104 ("normalized)"), 107–108 (שורה בודדת `))`), 111, 121, 124 מתחיל בשוליים השמאליים של הקוד, כך שנראה כשורה נפרדת בלי מספר. | qa-code: שורות ארוכות נעטפות עם הזחה (`breaklines`) | minor | `connected.cls`: `breakindent=...`, `breakautoindent`, `postbreak` בסגנון `pythonbox` |
| TYPE-06 | 2 (pdf 2) | typeset | בתקציר, שורת מילות המפתח נשברת באמצע הביטוי האנגלי: "Digital" בסוף שורה ו-"Well-being" לבדו בשורה הבאה. | qa-bidi כלל 2: ביטוי אנגלי הוא יחידה אחת | minor | `chapters/00-abstract.tex` (`\en{Digital Well-being}` עם `~` או `\mbox`) |
| INFRA-02 | root | infra | `main-snip1.pysnip` (קובץ זמני של `connected.lua`) נשאר בשורש אחרי הבנייה; בדיקת stray דיווחה "none". הקובץ ב-`.gitignore` אך לא נמחק על ידי `build.sh`. | qa-infra: אין קבצים תועים | minor | `build.sh` (מחיקת `*.pysnip` בסוף) או `connected.lua` (מחיקה אחרי הקריאה) |
| DOC-01 | template/CHANGELOG.md, v2.4.0 TYPE-05 | cls-version | הרשומה אומרת "עמוד iv מתוך vi", בפועל ב-PDF "מתוך v" (חזית הספר מסתיימת בעמוד v). | CHANGELOG מדויק | minor | `template/CHANGELOG.md` |
| QA-02 | n/a | qa-tooling | `qa_check code`: "Hebrew comments inside listing: []" PASS, אף שבטווח 93–127 יש מחרוזות עבריות מבולבלות (CODE-02). הבדיקה מחפשת רק הערות (`#`), לא literal עברי. | בדיקה שלא תפסה ממצא היא ממצא | minor | `qa/qa_check.py` (`code`): לסרוק גם מחרוזות עבריות בטווח המוצג |

## 4. v2.4.0: בדיקת תופעות לוואי

- גופן Times New Roman: אין תווים חסרים (0 `Missing character`), קיימים בגופן המוטמע (TimesNewRomanPSMT, Bold, Italic); כותרות נשארו Gisha. מספר העמודים נשאר 32.
- `connected.lua`: אין שגיאות ב-log. תוצר לוואי יחיד: קובץ `.pysnip` (INFRA-02).
- אזהרת 1782pt: לא מופיעה.

## 5. פסיקה

**NOT READY** (0 critical, 1 major, 6 minor). אין REGRESSED. המכשול היחיד הוא CODE-02.
