# דוח Fixer, סבב 4 (תיקוני סימולציית הבודק המחמיר)

**קלט:** `qa/reports/detector-round-4.md`: 0 קריטיים, 9 מהותיים ו-20 קלים. ציון משוער: 82/100.
**מבצעים:**
- תוכן: סוכן העורך, לפי `prompts/10-editor-round4.md`
- תבנית, בדיקות, איור ומסמכים: ה-Master, לפי `qa-fixer`

**עיקרון:** כל ממצא שחוזר בכמה מקומות תוקן בתבנית (v2.5.2) או בבדיקה. ממצא במקום אחד תוקן באותה שורה. כל סוג שינוי עלה ב-commit נפרד (INC-20).

| ID | חומרה | איפה תוקן | מה השתנה | סטטוס |
|----|-------|-----------|----------|-------|
| REPO-01 | major | git | commit ו-push של ההגהה, הפרומפטים 08–10 והדוחות. push בסוף כל סבב (INC-21) | FIXED |
| PROC-01 | major | תהליך | commits נפרדים: תוכן, תבנית, בדיקות, מסמכים. חקר אירוע INC-20 | FIXED |
| PROC-02 | major | `docs/incidents.md` | INC-17 עד INC-21 לממצאי סבבים 2–4 | FIXED |
| TYPE-07 | major | תבנית v2.5.2 | תיבות אינן נשברות בין עמודים. בדיקה ב-`qa-typeset` | FIXED |
| BIDI-04 | major | תבנית v2.5.2 | `\exhyphenpenalty=10000`. בדיקה גאומטרית ב-`qa-bidi` (INC-19) | FIXED |
| IMG-03 | major | `python/make_images.py` | התווית "Lock" בשורה אחת, והשורה התחתונה הוגבהה. שום תווית לא חוצה את הקיר | FIXED |
| DATA-01 | major | `refs.bib`, `02-history.tex` | מקורות ל-1844 (Library of Congress), 1969 (Kleinrock, ICANN) ו-1973 (Guinness) | FIXED |
| REPO-02 | major | README, PLAN, TODO, master prompt | 13 Skills בכל המסמכים. בדיקת ספירה ב-`qa-infra` | FIXED |
| LAYOUT-03 | major | `09-appendix-code.tex` | משפט השחזור מוזג לפסקת הפתיחה, והנספח נכנס בעמוד אחד. בדיקת מילוי עמוד ב-`qa-typeset` (INC-18). ב-CHANGELOG נרשם תיקון לטענה של v2.5.1 | FIXED |
| REPO-03 | minor | `make_agents_chart.py` | הגרף נוצר מחדש עם כל הריצות | FIXED |
| REPO-04 | minor | README, TODO | סבב 3: "1 מהותי ו-4 קלים" | FIXED |
| REPO-05 | minor | README, PRD | שורת מגיה בטבלאות, ו"8 פרקים ותקציר" | FIXED |
| REPO-06 | minor | README | Segoe UI נוסף לרשימת הגופנים | FIXED |
| REPO-07 | minor | `qa/known-warnings.md` | השורה הריקה בטבלה הוסרה | FIXED |
| REPO-08 | minor | `tests/` | `bash build.sh test` רץ על v2.5.2 ועבר | FIXED |
| BIB-01 | minor | `refs.bib` | `{November}`, `{Internet}`, תאריכי פרסום ל-`@online` כשהמקור מציין אותם. מירכאות כפולות ב-[4] הוסרו | FIXED |
| LANG-02 | minor | פרק 4, איור 4.1 | "הסינתזה שלנו" | FIXED |
| LANG-03 | minor | פרקים 1, 2, 3, 4 ו-5 | "לחיצה", "שש-עשרה שעות ערות", "ועד ארבע שעות", והדימוי של הציידת-לקטת מופיע פעם אחת | FIXED |
| CONT-01 | minor | טבלה 2.1 | סדר כרונולוגי | FIXED |
| CONT-02 | minor | טבלה 3.1 | `>3:00` והערת טבלה | FIXED |
| CONT-03 | minor | פרק 3 | משפט שמסביר את ההבדל בין DataReportal ל-ITU | FIXED |
| CONT-04 | minor | פרק 6 | "תחזית שפורסמה באוקטובר 2025", וכותרת שתואמת את הערך האחרון שנמדד | FIXED |
| TYPE-08 | minor | — | סופי פרקים דלילים מותרים לפי כלל העימוד. הוחלט להשאיר | KEPT |
| TYPE-09 | minor | תבנית v2.5.2 | רווח בלתי שביר לפני `\parencite` | FIXED |
| CODE-06 | minor | תבנית v2.5.2 | ניגודיות גבוהה יותר להערות ולמספרי שורות | FIXED |
| QA-04 | minor | `qa/qa_check.py` | 5 בדיקות חדשות: תחילית בסוף שורה, ציטוט שפותח שורה, מילוי עמוד, תיבה שנשברת, וספירות וקישורים במסמכים. כל אחת **תפסה את הממצא שלה על ה-PDF הישן** | FIXED |
| PROC-03 | minor | `qa/reports/` | הדוח הזה | FIXED |
| PROC-04 | minor | README | סיכום טוקנים לפי מודל | FIXED |
| SUB-01 | minor | — | הגשה ביחיד אושרה על ידי המרצה. קוד הקבוצה באחריות הסטודנטית | KEPT |

**אחרי התיקונים:** `bash build.sh test` עבר, הספר 32 עמודים, ו-`qa_check.py` מראה **0 FAIL ו-0 WARN**.
