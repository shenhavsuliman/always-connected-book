# Red-team report (substance-first)

Page numbers are PDF pages. Severity: H / M / L.

## 1. Goldilocks model: circular, and the "findings" under it are only partly verified (p.18-20, 21, 24, 27, 29) - H
- p.19: "כל אחת מגיעה לשיא בנקודת המפנה שדווחה עבור ימי חול". The appendix (p.29) sets `b1 = 2*b2*t*` and normalizes `W(t*)=1`. The peak therefore equals the tipping point by construction. The figure proves nothing and shows four identical-height parabolas, which hides the paper's actual point: the effect is tiny.
- The caption says "המחשה בלבד", but the neighbouring bullets present the numbers as results ("שעה ו-57 דקות", "4:17"). research/facts.md marks the weekend smartphone and computer values as unverified. It also rates the weekday computer/video mapping as medium confidence, because it was inferred from the order of items in an OII press release. The book states them flatly. The paper itself was never read ("לא נקראו בטקסט המלא").
- "Tipping point" in the press release means the point where the relation changes. The book silently reads it as the "peak of well-being".
- p.21: "המחקר מרמז ש... נקודת המפנה של הרווחה בימי חול מגיעה כבר אחרי כשעתיים". This is a specific figure with false precision, and it feeds the ch.7 advice. p.24: "המחקר תומך בגישה הזאת".
- Appendix A (p.29): "כל מספר בגרף אפשר לבדוק מול המקור". The source is a press release, not the paper.

## 2. Unsourced or stretched claims, and the "דברים" vs "בתים" comparison (p.7, 10, 11, 13, 16, 17, 22, 28) - H/M
- p.7: "זה יותר זמן משרוב האנשים מקדישים לעבודה בשכר, ולעיתים יותר ממה שהם ישנים" has no source. The figure is average online time of internet users, not a general population claim.
- p.8: "הציידים-לקטים ... כמה עשרות אנשים" (a Dunbar-style claim) has no citation. The same applies to "לפני שלושים אלף שנה".
- p.28: "הקשרים האלה הם שהפכו קוף חסר חשיבות ... לשליט כדור הארץ" is a Harari paraphrase with no source.
- p.11: the COVID jump (2019 to 2020) is attributed causally to the pandemic ("ככל הנראה") with no source.
- p.13: "דרום קוריאה ... סמוך לתחתית הרשימה". This is an artefact of the authors' choice of countries, and the list has no stated selection criterion.
- p.16: "אם אינכם משלמים על המוצר..." is a boxed "משפט שכדאי לזכור" with no attribution. It is a folk saying.
- p.16-17: the 8-step circle is credited as "עיבוד על בסיס Eyal ו-Zuboff", but steps 5-8 appear in neither. Eyal's stage names were never checked against the book (facts.md: "לפני הצגת ארבעת השלבים בשמם המדויק, כדאי לוודא").
- p.22: "החפצים המחוברים כבר רבים מאיתנו בהרבה". This sets global IoT connections (including industry) against internet users, a weak apples-to-oranges comparison. The book admits the caveat in small print, but the heading and the chapter frame it as a smart-home story.

## 3. Weakest chapter: ch.7 "ארגז כלים" (p.24-26), with ch.6 close behind - H/M
- Not one tip is tied to evidence. "Try two or three tools for two weeks and see what changed" has no basis. The chapter cites only Newport and the Goldilocks model, and the Newport "solitude deprivation" passages were never verified against the book.
- The "בלי מוסר ובלי אשמה" box ("זו מערכה לא הוגנת") asserts intentional design to addict as fact, with no source. It also contradicts the "לא קונספירציה" box on p.16.
- The ch.6 privacy argument rests on a single number (the IoT count) and no evidence of actual smart-home data practices, breaches or surveys. The rest is assertion and hypotheticals.
- Ch.8 (p.27-28) offers AI speculation: "בקרוב הם עשויים ליצור אותו". It has no sources, and it is the one place where the abstract promises "מבט אל עידן הבינה המלאכותית".

## 4. Repetition (M)
- 5.87bn appears on p.2, 7, 10, 11, 21 and 27. 6:40 appears on p.2, 7, 8, 12, 14 and 27.
- The Haidt vs Orben dispute is stated three times in near-identical wording (p.20, 25, 27). "Moderation, not zero" appears on p.18, 24 and 27. The ch.8 recap adds no analysis.

## 5. Other (L/M)
- The sources are almost all secondary or press material (press release, DataReportal blog), and there are no Israeli official statistics. The Israel figure rests on DataReportal and is presented as "הישראלים מחוברים".
- The "ChatGPT ... בלי תרועות" framing (p.27) is the author's characterization. The cited source says only "research preview".
- p.29-30 code listing: Hebrew strings inside Python are visually reversed, a BiDi slip the QA skills missed.
- The table and figure counts are thin for 26 pages. Only 2 tables and no table in ch.5-7.
