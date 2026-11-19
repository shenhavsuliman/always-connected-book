# אזהרות הידור מוכרות

כל אזהרה שמופיעה כאן נבדקה ויזואלית, ויש לה הסבר. `qa-typeset` מסמן אותה כ"מוכרת" במקום כתקלה. אזהרה שאינה ברשימה היא ממצא.

| אזהרה | מקור | למה היא לא תקלה | נבדק |
|-------|------|-----------------|------|
| `Package biblatex Warning: Language 'nil' not supported` ו-`Language 'hebrew' not supported` | `biblatex` (טעינה, שורה 16 בקובץ ה-aux) | ל-biblatex אין תרגום (localization) לעברית. רשימת המקורות נבנית בסביבה אנגלית (`otherlanguage{english}`) בסגנון IEEE, והמחרוזות שלה ("Accessed", "Online. Available") באנגלית. אין מחרוזת עברית ברשימה שה-biblatex צריך לתרגם. | 2026-11-18, ויזואלית, עמודי רשימת המקורות |

| `Underfull \hbox (badness 1221) in paragraph at lines 17--18` | `chapters/02-history.tex`: הציטוט `\en{"What hath God wrought"}` | מ-v2.5.1 ביטוי אנגלי לא נשבר, ולכן השורה שלפניו מעט מרווחת. זה המחיר המכוון של כלל BiDi 2, ביטוי אנגלי כיחידה אחת. | 2026-11-19, ויזואלית, עמוד 8 |

**הערה (v2.4.0):** האזהרה `Overfull \hbox (1782pt)` של `\pythonfile` נעלמה. מ-v2.4.0 `connected.lua` חותך את טווח השורות לפני ש-`listings` קורא אותו, והיא הייתה הסימן לדליפת שורות הדילוג (CODE-01). אם היא חוזרת, זה ממצא ולא אזהרה מוכרת.
