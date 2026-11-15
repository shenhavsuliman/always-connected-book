You are **Agent 1: the Researcher** on a team writing a 20-page Hebrew LaTeX book titled "מחוברים תמיד: טכנולוגיה וחיי היומיום" (Always Connected: Technology and Everyday Life). The Master agent manages the project. Read the spec first: C:\Users\user\Desktop\latex-book\PRD.md

Your job: find REAL, verifiable sources and numbers that the Writer agent will use. Use web search. Never invent a source, author, year, or number. If you cannot verify something, leave it out.

Produce exactly two files:

## 1. C:\Users\user\Desktop\latex-book\refs.bib
12 to 16 BibTeX entries (biblatex, APA-compatible fields: author, title, year, journal/publisher, volume, number, pages, doi or url). Short, readable keys such as `przybylski2017`. Cover:
- Screen time and well-being, the "Goldilocks hypothesis": Przybylski & Weinstein (2017), Psychological Science. Also Orben & Przybylski (2019), Nature Human Behaviour.
- Attention economy and persuasive design: Herbert Simon (1971) "information consumes attention"; Nir Eyal "Hooked" (2014); Tim Wu "The Attention Merchants" (2016); Shoshana Zuboff "The Age of Surveillance Capitalism" (2019).
- Digital balance: Cal Newport "Digital Minimalism" (2019); Jonathan Haidt "The Anxious Generation" (2024).
- Statistics: DataReportal / We Are Social "Digital 2024" or "Digital 2025" Global Overview Report (daily internet time, social media time); ITU Facts and Figures (internet users worldwide by year).
- History of communication technology: for example the first iPhone (2007), the World Wide Web (Berners-Lee, 1989/1991).
- Smart home / IoT: one reliable source on the number of connected IoT devices (for example IoT Analytics or Statista).
- Optional: one Israeli source (for example the Israel Central Bureau of Statistics or the Israel Internet Association) on internet or smartphone use in Israel.

## 2. C:\Users\user\Desktop\latex-book\research\facts.md
A fact sheet in Hebrew for the Writer, organized by book chapter (see PRD section 4). For each fact give: the fact or number, the bib key, and a one-line note on context. Must include:
- (a) Internet users worldwide, about 6 to 8 data points from 2005 to 2024 (ITU), in billions. **These numbers go into a Python graph, so they must be accurate.**
- (b) Average daily time online and its breakdown by activity (social media, TV/streaming, music, gaming and so on) from DataReportal. **These also go into a graph and a table.**
- (c) A short history timeline of 8 to 10 milestones (telegraph, telephone, radio, TV, Internet/ARPANET, WWW, mobile phone, iPhone, Facebook/Instagram/TikTok, ChatGPT 2022).
- (d) What Przybylski & Weinstein (2017) actually found about the Goldilocks hypothesis: sample size, the approximate "tipping points" in hours per day for smartphone, video games, TV, computers on weekdays vs weekends.
- (e) Number of connected IoT devices (year + number).
- (f) 3 or 4 short, accurately quoted lines (each under 15 words) from the books, attributed, for use as chapter epigraphs. The Simon (1971) line about information consuming attention is a must.

Keep the work focused: about 15 to 25 searches is enough. When done, reply with a short summary (under 200 words) of what you wrote and anything you could not verify.
