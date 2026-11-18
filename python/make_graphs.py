"""
make_graphs.py — יוצר את שלושת הגרפים של הספר מנתונים מאומתים (research/facts.md).
  1. images/internet_users.png  — משתמשי אינטרנט בעולם 2005–2024 (ITU)
  2. images/daily_time.png      — זמן יומי ברשת לפי מדינה (DataReportal 2024)
  3. images/goldilocks.png      — המחשה של השערת גולדילוקס (Przybylski & Weinstein 2017)

הרצה:  python python/make_graphs.py
דרישות: pip install "matplotlib>=3.11" numpy
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "images"
OUT.mkdir(exist_ok=True)

# פלטה שעברה בדיקת עיוורון צבעים (validate_palette.js: כל 6 הבדיקות PASS)
TEAL, CORAL, INDIGO, AMBER = "#00939F", "#E5484D", "#5B5FC7", "#B87A00"
INK, MUTED, GRID = "#2E3440", "#6B7280", "#E5E7EB"

plt.rcParams.update({
    "font.family": ["Gisha", "Arial"],
    "font.size": 11,
    "axes.edgecolor": GRID, "axes.labelcolor": MUTED,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "savefig.dpi": 220, "savefig.bbox": "tight",
})


def he(text: str) -> str:
    """matplotlib 3.11+ מסדר עברית ימין-לשמאל בעצמו, אז אין צורך ב-python-bidi.
    (בגרסאות ישנות: return bidi.algorithm.get_display(text))"""
    return text


# ------------------------------------------------------------------ 1
def internet_users():
    # ITU, Regional and global key ICT indicator aggregates, Nov 2026 (itu2026data)
    years = [2005, 2010, 2015, 2019, 2020, 2021, 2022, 2023, 2024]
    users = [1.02, 1.98, 2.96, 4.18, 4.72, 5.06, 5.38, 5.65, 5.87]
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.fill_between(years, users, color=TEAL, alpha=0.10, lw=0)
    ax.plot(years, users, color=TEAL, lw=2.2, marker="o", ms=7,
            mfc=TEAL, mec="white", mew=2, zorder=3)
    for x, y, lab in [(2005, 1.02, "1.02"), (2015, 2.96, "2.96"), (2024, 5.87, "5.87")]:
        ax.annotate(lab, (x, y), xytext=(0, 10), textcoords="offset points",
                    ha="center", color=INK, fontsize=11, fontweight="bold")
    ax.annotate(he("הקפיצה של הקורונה"), xy=(2020, 4.72), xytext=(2012.2, 4.9),
                color=MUTED, fontsize=10, ha="center",
                arrowprops=dict(arrowstyle="->", color=MUTED, lw=1))
    ax.set_ylabel(he("מיליארדי משתמשים"))
    ax.set_ylim(0, 6.8)
    ax.set_xticks([2005, 2010, 2015, 2020, 2024])
    ax.grid(axis="x", visible=False)
    ax.set_title(he("אנשים שמשתמשים באינטרנט בעולם"), loc="right", color=INK,
                 fontsize=13, fontweight="bold")
    fig.text(0.99, -0.05, he("מקור: ITU, מהדורת נובמבר 2026"), ha="right", color=MUTED, fontsize=8.5)
    fig.savefig(OUT / "internet_users.png")
    plt.close(fig)


# ------------------------------------------------------------------ 2
def daily_time():
    # DataReportal, Digital 2024 Global Overview (kemp2024): שעות:דקות ביום
    data = [("דרום אפריקה", 9, 24), ("ברזיל", 9, 13), ("הפיליפינים", 8, 52),
            ("ממוצע עולמי", 6, 40), ("דרום קוריאה", 5, 19), ("דנמרק", 5, 8)]
    data = data[::-1]  # הגבוה למעלה
    names = [he(n) for n, _, _ in data]
    hours = [h + m / 60 for _, h, m in data]
    colors = [CORAL if n == "ממוצע עולמי" else TEAL for n, _, _ in data]
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    bars = ax.barh(names, hours, color=colors, height=0.62, edgecolor="white", linewidth=2)
    for b, (_, h, m) in zip(bars, data):
        ax.text(b.get_width() + 0.12, b.get_y() + b.get_height() / 2, f"{h}:{m:02d}",
                va="center", color=INK, fontsize=10.5, fontweight="bold")
    ax.set_xlim(0, 10.6)
    ax.set_xlabel(he("שעות ביום ברשת (משתמש אינטרנט טיפוסי, גילאי 16 עד 64)"))
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0, labelsize=11, labelcolor=INK)
    ax.set_title(he("כמה זמן אנחנו מבלים ברשת כל יום?"), loc="right", color=INK,
                 fontsize=13, fontweight="bold")
    fig.text(0.99, -0.07, he("מקור: DataReportal, Digital 2024"), ha="right", color=MUTED, fontsize=8.5)
    fig.savefig(OUT / "daily_time.png")
    plt.close(fig)


# ------------------------------------------------------------------ 3
# Hebrew labels live here, apart from the plotting code, so the function shown in the
# book's appendix is plain left-to-right code (CODE-02: bidi scrambles Hebrew strings).
LABELS = {
    "phone": "סמארטפון", "games": "משחקי וידאו", "video": "סרטונים וטלוויזיה",
    "pc": "מחשב (פנאי)", "peak": "שיא", "tstar": "נקודת המפנה = t*",
    "above": "מעל השיא: כל שעה\nנוספת מורידה רווחה",
    "xlabel": "שעות שימוש ביום חול (t)", "ylabel": "רווחה נפשית יחסית W(t)",
    "title": "השערת גולדילוקס: לא מעט מדי ולא יותר מדי",
    "note": "המחשה בלבד: העקומות בנויות כך שהשיא ייפול על נקודות המפנה "
            "שדווחו (Przybylski & Weinstein, 2017); הגובה מנורמל",
}


def goldilocks():
    # Weekday tipping points t* in hours (Przybylski & Weinstein 2017, OII press release).
    # The curves ILLUSTRATE W(t) = b0 + b1*t - b2*t^2. They are built to peak at t*
    # and are normalized to height 1, so they show WHERE the peak is, not how big.
    series = [("phone", 1 + 57 / 60, TEAL, "o"), ("games", 1 + 40 / 60, CORAL, "s"),
              ("video", 3 + 41 / 60, INDIGO, "D"), ("pc", 4 + 17 / 60, AMBER, "^")]
    t = np.linspace(0, 8, 400)
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.axhline(0, color=MUTED, lw=1)
    for key, ts, c, mk in series:
        b2 = 1 / ts ** 2            # curvature (normalizes the peak height to 1)
        b1 = 2 * b2 * ts            # dW/dt = b1 - 2*b2*t = 0  ->  peak at t = t*
        w = b1 * t - b2 * t ** 2    # b0 = 0: the curves are relative
        hhmm = f"{int(ts)}:{round((ts % 1) * 60):02d}"
        ax.plot(t, w, color=c, lw=2, label=f"{LABELS[key]} ({LABELS['peak']}: {hhmm})")
        ax.plot([ts], [1], marker=mk, color=c, ms=9, mec="white", mew=2, zorder=4)
        ax.vlines(ts, -0.9, 1, color=c, lw=1, ls=(0, (3, 3)), alpha=0.8)
    ax.text(0.15, 1.12, LABELS["tstar"], color=INK, fontsize=10, fontweight="bold")
    ax.text(5.6, -0.55, LABELS["above"], color=MUTED, fontsize=9.5, ha="center")
    ax.set(xlim=(0, 8), ylim=(-0.9, 1.3), yticks=[])
    ax.set_xlabel(LABELS["xlabel"])
    ax.set_ylabel(LABELS["ylabel"])
    ax.grid(axis="y", visible=False)
    ax.legend(loc="lower left", frameon=False, fontsize=9.5)
    ax.set_title(LABELS["title"], loc="right", color=INK, fontsize=13, fontweight="bold")
    fig.text(0.99, -0.07, LABELS["note"], ha="right", color=MUTED, fontsize=8.5)
    fig.savefig(OUT / "goldilocks.png")
    plt.close(fig)


if __name__ == "__main__":
    internet_users()
    daily_time()
    goldilocks()
    print("graphs written to", OUT)
