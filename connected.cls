% ============================================================================
%  connected.cls — תבנית הספר "מחוברים תמיד"            (Always Connected class)
%  מנוע: LuaLaTeX + babel (bidi=basic)  |  מקורות: biblatex-ieee + biber
%
%  גרסה:   ראו \ConnectedVersion למטה, ויומן שינויים ב-template/CHANGELOG.md
%  פקודות: רשימה מלאה עם הסבר ב-template/COMMANDS.md
%
%  פלטה: כחול-לילה (מסך כבוי) · טורקיז (מסך דולק) · אלמוג (התראה)
%        צהוב (רעיון) · ירוק (איזון)
% ============================================================================
\NeedsTeXFormat{LaTeX2e}
\def\ConnectedVersion{2.5.0}
\def\ConnectedDate{2026/11/18}
\ProvidesClass{connected}[\ConnectedDate\space v\ConnectedVersion\space Always Connected book class]

\LoadClass[11pt, a4paper, openany]{report}

\RequirePackage{iftex}
\ifLuaTeX\else
  \ClassError{connected}{This class requires LuaLaTeX}{Compile with: lualatex main.tex}
\fi

% ---------------------------------------------------------------- שפות וגופנים
% babel עם bidi=basic: כיוון אוטומטי לפי סוג התו (עברית RTL, לטינית ומספרים LTR).
% layout=tabular.lists → טבלאות ורשימות בכיוון הנכון.
% בלי layout=counters: הוא שובר את listings ("Missing number"), ראו INC-07.
\RequirePackage[bidi=basic, layout=tabular.lists]{babel}
\babelprovide[main, import]{hebrew}
\babelprovide[import]{english}
\babelfont{rm}{Times New Roman}
% BIDI-01: ב-David נקודתיים ונקודה-פסיק צרים עם רווח מסביבם ("שלום : קשר"), ולכן הגופן העברי הוא Times New Roman.
\babelfont[hebrew]{rm}{Times New Roman}
\babelfont{sf}{Segoe UI}
\babelfont[hebrew]{sf}{Gisha}
\babelfont{tt}{Courier New}  % ל-Consolas אין אותיות עבריות (INC-09)
\newfontfamily\headfont{Gisha}[Script=Hebrew, BoldFont=Gisha Bold]

% ---------------------------------------------------------------- חבילות
\RequirePackage[a4paper, top=3.1cm, bottom=2.6cm, inner=2.4cm, outer=2.4cm,
                headheight=34pt, headsep=16pt, footskip=34pt]{geometry}
\RequirePackage{amsmath, amssymb}
\RequirePackage{graphicx}
\RequirePackage{booktabs, tabularx, array, colortbl}
\RequirePackage{xcolor}
\RequirePackage{tikz}
\usetikzlibrary{positioning, arrows.meta, shapes.geometric, calc, shadows}
\RequirePackage[most]{tcolorbox}
\tcbuselibrary{listings}
\RequirePackage{listings}
\RequirePackage{titlesec}
\RequirePackage{titletoc}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{enumitem}
\RequirePackage{caption}
\RequirePackage{setspace}
\RequirePackage{needspace}   % TYPE-02: \Needspace{6\baselineskip} לפני פסקת הקדמה לרשימה
\RequirePackage[style=english]{csquotes}  % מירכאות אנגליות בכותרות IEEE (INC-10)
\RequirePackage[backend=biber, style=ieee, sorting=none, dashed=false]{biblatex}
\RequirePackage[hidelinks]{hyperref}

% TYPE-01: כתובות URL ברשימת המקורות לא נמתחות בצדק: גרירה לשמאל וקווי שבירה נוספים בכתובת.
\appto{\bibsetup}{\raggedright}
\setcounter{biburlnumpenalty}{100}
\setcounter{biburlucpenalty}{100}
\setcounter{biburllcpenalty}{100}

\setstretch{1.18}
\setlength{\parskip}{0.45em}
\widowpenalty=10000 \clubpenalty=10000   % TYPE-02: אין שורה בודדת בראש או בתחתית עמוד
\setlength{\emergencystretch}{8em}   % TYPE-03: פחות שורות מתוחות מדי
% IMG-01: איור גבוה לא יישב לבד בעמוד חצי ריק. עמוד צפים חייב להיות מלא לפחות 80%,
% ואיור עד 85% מהעמוד יכול לעלות לראש העמוד עם טקסט מתחתיו.
\renewcommand{\topfraction}{0.85}\renewcommand{\bottomfraction}{0.7}
\renewcommand{\textfraction}{0.1}\renewcommand{\floatpagefraction}{0.8}

% ---------------------------------------------------------------- צבעים
\definecolor{night}{HTML}{1B2A41}
\definecolor{screen}{HTML}{0FA3B1}
\definecolor{notif}{HTML}{F25F5C}
\definecolor{sun}{HTML}{FFB238}
\definecolor{leaf}{HTML}{3BB273}
\definecolor{paper}{HTML}{F5F7FA}
\definecolor{ink}{HTML}{2E3440}
\definecolor{codebg}{HTML}{F3F6F9}
\AtBeginDocument{\color{ink}}
\hypersetup{colorlinks=true, linkcolor=night, citecolor=screen, urlcolor=screen}

% ---------------------------------------------------------------- סימון שפה
% כלל: כל מילה, שם או ראשי תיבות באנגלית נעטפים ב-\en{}. ביטוי רב-מילים = יחידה אחת.
\newcommand{\en}[1]{\foreignlanguage{english}{#1}}
% מספר, אחוז, טווח, תאריך או גרסה כיחידה LTR אחת (למשל \num{2005--2024}, \num{72.3\%})
\newcommand{\num}[1]{\foreignlanguage{english}{#1}}
% עברית בתוך נוסחה: \mathheb{רווחה}
\newcommand{\mathheb}[1]{\text{\foreignlanguage{hebrew}{#1}}}
% עברית בתוך צומת TikZ (ראו חקר אירוע INC-03): \heb{טקסט}
\newcommand{\heb}[1]{\foreignlanguage{hebrew}{#1}}

% ---------------------------------------------------------------- פרטי המסמך
\newcommand{\booktitle}[1]{\def\@booktitle{#1}}
\newcommand{\booksubtitle}[1]{\def\@booksubtitle{#1}}
\newcommand{\englishtitle}[1]{\def\@englishtitle{#1}}
\newcommand{\bookauthors}[1]{\def\@bookauthors{#1}}
\newcommand{\groupcode}[1]{\def\@groupcode{#1}}
\newcommand{\course}[1]{\def\@course{#1}}
\booktitle{}\booksubtitle{}\englishtitle{}\bookauthors{}\groupcode{}\course{}
% מילות מפתח: מופיעות בסוף התקציר
\newcommand{\keywords}[1]{\par\medskip\noindent{\headfont\bfseries\color{screen}מילות מפתח:}~#1\par}

% ---------------------------------------------------------------- כותרות פרקים
\titleformat{\chapter}[display]
  {\headfont\color{night}}
  {\begin{tikzpicture}
     \node[fill=screen, text=white, rounded corners=6pt, minimum width=1.6cm,
           minimum height=1.6cm, font=\headfont\bfseries\fontsize{34}{34}\selectfont]
           {\thechapter};
     \fill[notif] (0.95,0.95) circle (0.22);   % "נקודת התראה"
   \end{tikzpicture}}
  {0.6em}
  {\bfseries\fontsize{28}{32}\selectfont}
  [{\color{screen}\rule{\textwidth}{1.4pt}}]
\titlespacing*{\chapter}{0pt}{-10pt}{22pt}
\titleformat{name=\chapter, numberless}[display]
  {\headfont\color{night}}{}{0pt}{\bfseries\fontsize{28}{32}\selectfont}
  [{\color{screen}\rule{\textwidth}{1.4pt}}]
\titlespacing*{name=\chapter, numberless}{0pt}{-10pt}{22pt}

\titleformat{\section}
  {\headfont\Large\bfseries\color{night}}
  {\color{screen}\thesection}{0.7em}{}
\titleformat{\subsection}
  {\headfont\large\bfseries\color{screen!80!night}}
  {\thesubsection}{0.6em}{}

% ---------------------------------------------------------------- תוכן עניינים ורשימות
\titlecontents{chapter}[0pt]
  {\addvspace{0.9em}\headfont\bfseries\color{night}}
  {\colorbox{screen}{\textcolor{white}{\makebox[1.4em]{\thecontentslabel}}}\hspace{0.7em}}
  {}
  {\titlerule*[0.6pc]{.}\contentspage}
\titlecontents{section}[2.6em]
  {\addvspace{0.15em}}
  {\makebox[2.2em][r]{\thecontentslabel}\hspace{0.5em}}
  {}
  {\titlerule*[0.6pc]{.}\contentspage}
\titlecontents{figure}[0pt]
  {\addvspace{0.2em}}
  {\makebox[2.6em][r]{\color{screen}\bfseries\thecontentslabel}\hspace{0.6em}}
  {}
  {\titlerule*[0.6pc]{.}\contentspage}
\titlecontents{table}[0pt]
  {\addvspace{0.2em}}
  {\makebox[2.6em][r]{\color{screen}\bfseries\thecontentslabel}\hspace{0.6em}}
  {}
  {\titlerule*[0.6pc]{.}\contentspage}

% ---------------------------------------------------------------- באנר עליון ושורה תחתונה
% באנר: פס כחול-לילה ברוחב העמוד, ובתוכו שם הפרק (ימין) ושם הספר (שמאל).
% שורה תחתונה: זכויות + קוד קבוצה (ימין), "עמוד N מתוך M" בעיגול (מרכז).
\newcommand{\connected@banner}{\foreignlanguage{english}{%
  \begin{tikzpicture}[remember picture, overlay]
    \fill[night] (current page.north west) rectangle ([yshift=-1.55cm]current page.north east);
    \fill[screen] ([yshift=-1.55cm]current page.north west) rectangle ([yshift=-1.63cm]current page.north east);
    \fill[notif] ([xshift=-1.2cm, yshift=-0.78cm]current page.north east) circle (0.13);
    \node[anchor=east, text=white, font=\headfont\small\bfseries]
         at ([xshift=-2.4cm, yshift=-0.78cm]current page.north east) {\heb{\leftmark}};
    \node[anchor=west, text=white!75, font=\headfont\small]
         at ([xshift=2.4cm, yshift=-0.78cm]current page.north west) {\heb{\@booktitle}};
  \end{tikzpicture}}}
% TYPE-05: בחזית הספר (מספור רומי) הסך הכולל הוא העמוד הרומי האחרון, לא מספר ערבי.
% \pagenumbering זוכר את סגנון המספור, וכשעוברים ממספור רומי נכתב לקובץ aux העמוד האחרון.
\def\connected@numstyle{arabic}
\def\connected@romanstyle{roman}
\def\ConnectedFrontLast{?}
\let\connected@pagenumbering\pagenumbering
\renewcommand{\pagenumbering}[1]{%
  \ifx\connected@numstyle\connected@romanstyle
    \immediate\write\@auxout{\string\gdef\string\ConnectedFrontLast{\romannumeral\numexpr\value{page}-1\relax}}%
  \fi
  \gdef\connected@numstyle{#1}%
  \connected@pagenumbering{#1}}
\newcommand{\connected@pagetotal}{%
  \ifx\connected@numstyle\connected@romanstyle\ConnectedFrontLast\else\pageref*{LastPage}\fi}
\newcommand{\connected@footer}{\foreignlanguage{english}{%
  \begin{tikzpicture}[baseline]
    \node[rounded corners=7pt, fill=night, text=white, inner xsep=7pt, inner ysep=3pt,
          font=\headfont\footnotesize]
         {\heb{עמוד \num{\thepage} מתוך \num{\connected@pagetotal}}};
  \end{tikzpicture}}}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyhead[C]{\connected@banner}
\fancyfoot[C]{\connected@footer}
\fancyfoot[R]{\headfont\scriptsize\color{night!55}© \num{2026} \@bookauthors}
\fancyfoot[L]{\headfont\scriptsize\color{night!55}\ifx\@groupcode\@empty\else קבוצה \num{\@groupcode}\fi}
\fancypagestyle{plain}{\fancyhf{}\renewcommand{\headrulewidth}{0pt}%
  \fancyfoot[C]{\connected@footer}%
  \fancyfoot[R]{\headfont\scriptsize\color{night!55}© \num{2026} \@bookauthors}}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}

% ---------------------------------------------------------------- רשימות
\setlist[itemize,1]{label={\textcolor{screen}{\large$\bullet$}}, leftmargin=1.6em, itemsep=0.2em}
\setlist[itemize,2]{label={\textcolor{notif}{$\triangleleft$}}}
\setlist[enumerate,1]{label={\headfont\bfseries\textcolor{screen}{\arabic*.}}}
\newlist{checklist}{itemize}{1}
\setlist[checklist]{label={\textcolor{leaf}{\Large$\square$}}, leftmargin=2em, itemsep=0.3em}

% ---------------------------------------------------------------- כיתובים
\captionsetup{font={small,sf}, labelfont={bf,color=screen}, labelsep=period}
\captionsetup[table]{position=top}

% ---------------------------------------------------------------- תיבות
% כלל (חקר אירוע INC-08): מסגרת התיבה נבנית בסביבה אנגלית (LTR), והתוכן והכותרת בעברית.
% אחרת, תחת bidi=basic, המסגרת זזה הצידה והכותרת נעלמת.
\tcbset{boxbase/.style={enhanced, breakable, sharp corners=northwest, arc=5pt,
  boxrule=0pt, left=10pt, right=10pt, top=7pt, bottom=7pt,
  fonttitle=\headfont\bfseries, coltitle=white, before upper=\selectlanguage{hebrew}}}
% \connected@box{שם}{כותרת ברירת מחדל}{אפשרויות tcolorbox}
\newcommand{\connected@box}[3]{%
  \NewDocumentEnvironment{#1}{O{#2}}%
    {\par\begin{otherlanguage}{english}\tcolorbox[boxbase, #3,
       title={\foreignlanguage{hebrew}{##1}}]}%
    {\endtcolorbox\end{otherlanguage}\par}}
\connected@box{thinkbox}{שאלה למחשבה}{colback=sun!10, colframe=sun,
  borderline east={4pt}{0pt}{sun}, colbacktitle=sun!90!night}
\connected@box{factbox}{נתון מפתח}{colback=screen!8, colframe=screen,
  borderline east={4pt}{0pt}{screen}, colbacktitle=screen}
\connected@box{alertbox}{שימו לב}{colback=notif!8, colframe=notif,
  borderline east={4pt}{0pt}{notif}, colbacktitle=notif}
\connected@box{tipbox}{טיפ לאיזון}{colback=leaf!9, colframe=leaf,
  borderline east={4pt}{0pt}{leaf}, colbacktitle=leaf}
\NewDocumentEnvironment{eqbox}{O{}}%
  {\par\begin{otherlanguage}{english}\tcolorbox[enhanced, colback=night!4, colframe=night,
     boxrule=0.8pt, arc=4pt, fonttitle=\headfont\bfseries, colbacktitle=night,
     title={\foreignlanguage{hebrew}{#1}}, before upper=\selectlanguage{hebrew}]}%
  {\endtcolorbox\end{otherlanguage}\par}
\NewDocumentEnvironment{epigraph}{m}%
  {\par\begin{otherlanguage}{english}\tcolorbox[enhanced, frame hidden, colback=paper,
     borderline east={2pt}{0pt}{night!50}, left=12pt, right=12pt, fontupper=\large,
     before upper=\selectlanguage{hebrew},
     after upper={\if\relax\detokenize{#1}\relax\else\par\hfill\small\headfont\color{night!70}\textemdash~#1\fi}]}%
  {\endtcolorbox\end{otherlanguage}\par}
% תרשים TikZ בטוח לכיוון: \begin{ltrpicture} ... \end{ltrpicture}, ותוויות בעברית ב-\heb{}
\NewDocumentEnvironment{ltrpicture}{O{}}%
  {\begin{otherlanguage}{english}\begin{tikzpicture}[#1]}%
  {\end{tikzpicture}\end{otherlanguage}}

% ---------------------------------------------------------------- תיבת קוד Python
% כלל: תיבת קוד נבנית תמיד בסביבה אנגלית (מסגרת וכיוון LTR), הכותרת בעברית.
% שימוש:  \pythonfile[firstline=10, lastline=40]{python/make_graphs.py}{כותרת בעברית}
\lstdefinestyle{connectedpy}{language=Python, basicstyle=\ttfamily\footnotesize,
  keywordstyle=\color{screen!70!night}\bfseries, commentstyle=\color{night!55}\itshape,
  stringstyle=\color{notif!80!night}, numbers=left, numberstyle=\tiny\color{night!40},
  showstringspaces=false, breaklines=true, columns=fullflexible, keepspaces=true,
  breakindent=1.8em, breakautoindent=true,                           % CODE-05 (v2.5.0)
  postbreak=\mbox{\textcolor{screen}{$\hookrightarrow$}\space}}
% CODE-04 (v2.5.0): תיבת קוד אינה נשברת בין עמודים, כדי שהכותרת תישאר עם הקוד.
% קטעי קוד בספר קצרים (עד כ-35 שורות) ולכן תמיד נכנסים בעמוד אחד.
\tcbset{pythonbox/.style={enhanced, listing only, colback=codebg,
  colframe=night, boxrule=0.6pt, arc=4pt, left=24pt, right=8pt, top=4pt, bottom=4pt,
  listing options={style=connectedpy}, fonttitle=\headfont\bfseries\small,
  colbacktitle=night, coltitle=white}}
% CODE-01/02/03: connected.lua חותך את הטווח לקובץ זמני (listings לא קורא את שורות הדילוג),
% מסמן כיוון אחרי רצפים עבריים, ומספרי השורות בתיבה הם מספרי השורות האמיתיים בקובץ.
\directlua{dofile(kpse.find_file("connected.lua", "tex") or "connected.lua")}
\newcounter{connected@snip}
\def\connected@snipfirst{1}
\def\connected@snipopts{}
\NewDocumentCommand{\pythonfile}{O{}mm}{%
  \par\begin{otherlanguage}{english}%
  \stepcounter{connected@snip}%
  \directlua{connected.snippet("#2", "#1", "\jobname-snip\arabic{connected@snip}.pysnip")}%
  \edef\connected@snipcall{\noexpand\tcbinputlisting{pythonbox,
    listing file={\jobname-snip\arabic{connected@snip}.pysnip},
    listing options={style=connectedpy, firstnumber=\connected@snipfirst, \connected@snipopts},
    title={\noexpand\foreignlanguage{hebrew}{\unexpanded{#3}}}}}%
  \connected@snipcall
  \end{otherlanguage}\par}

% ---------------------------------------------------------------- ציטוטים
% ציטוט IEEE ([1]) הוא יחידה אנגלית אחת: כך הסוגריים המרובעים לא מתהפכים.
\NewCommandCopy\connected@parencite\parencite
\NewCommandCopy\connected@textcite\textcite
\RenewDocumentCommand\parencite{m}{\mbox{\foreignlanguage{english}{\connected@parencite{#1}}}}
\RenewDocumentCommand\textcite{m}{\mbox{\foreignlanguage{english}{\connected@textcite{#1}}}}

% ---------------------------------------------------------------- שער
\newcommand{\makecover}{%
  \begin{titlepage}\begin{otherlanguage}{english}
  \begin{tikzpicture}[remember picture, overlay]
    \fill[night] (current page.south west) rectangle (current page.north east);
    \node[anchor=center, opacity=0.95] at ($(current page.center)+(0,0.6)$)
         {\includegraphics[width=\paperwidth]{images/cover_network.png}};
    \fill[screen] ($(current page.south west)+(0,4.6)$) rectangle ($(current page.south east)+(0,4.85)$);
    \node[text=white, font=\headfont\bfseries\fontsize{48}{52}\selectfont]
         at ($(current page.north)+(0,-3.6)$) {\heb{\@booktitle}};
    \node[text=screen, font=\headfont\fontsize{20}{24}\selectfont]
         at ($(current page.north)+(0,-5.0)$) {\heb{\@booksubtitle}};
    \node[text=white!80, font=\Large]
         at ($(current page.north)+(0,-6.0)$) {\@englishtitle};
    % BIDI-02: תג ההתראה מעל הכותרת ולא נוגע בה (הכותרת מתחילה ב-3.0- ס"מ מראש העמוד)
    \fill[notif] ($(current page.north)+(5.6,-1.95)$) circle (0.35);
    \node[text=white, font=\headfont\bfseries\small] at ($(current page.north)+(5.6,-1.95)$) {9};
    \node[text=white, font=\headfont\large]
         at ($(current page.south)+(0,3.6)$) {\heb{\@bookauthors}};
    \node[text=white!75, font=\headfont]
         at ($(current page.south)+(0,2.8)$) {\heb{\@course}};
    \node[text=white!55, font=\headfont\small]
         at ($(current page.south)+(0,2.0)$) {\heb{נבנה ב-\en{LuaLaTeX} בעזרת צוות סוכני בינה מלאכותית \quad·\quad תבנית \en{connected.cls} \num{v\ConnectedVersion}}};
  \end{tikzpicture}
  \end{otherlanguage}\end{titlepage}}
