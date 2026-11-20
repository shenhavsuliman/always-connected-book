"""
make_images.py — יוצר את התמונות של הספר באמצעות קוד (generative art).
  1. images/cover_network.png  — רשת של "מסכים" זוהרים לעמוד השער
  2. images/smart_home.png     — איור של בית חכם ומכשירים מחוברים

הרצה:  python python/make_images.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Polygon, Circle

OUT = Path(__file__).resolve().parent.parent / "images"
OUT.mkdir(exist_ok=True)

NIGHT, SCREEN, NOTIF, SUN, LEAF = "#1B2A41", "#0FA3B1", "#F25F5C", "#FFB238", "#3BB273"
rng = np.random.default_rng(2026)


def cover_network():
    """רשת אנשים-מסכים: כל נקודה היא מכשיר, כל קו הוא חיבור."""
    fig, ax = plt.subplots(figsize=(8.27, 8.27), dpi=220)
    fig.patch.set_facecolor(NIGHT)
    ax.set_facecolor(NIGHT)
    n = 170
    # נקודות בצורת "ענן" סביב מרכז, צפוף יותר במרכז
    r = np.sqrt(rng.random(n)) * 1.0
    t = rng.random(n) * 2 * np.pi
    x, y = r * np.cos(t) * 1.25, r * np.sin(t)
    # קווי חיבור בין שכנים קרובים
    for i in range(n):
        d = np.hypot(x - x[i], y - y[i])
        for j in np.argsort(d)[1:4]:
            ax.plot([x[i], x[j]], [y[i], y[j]], color=SCREEN,
                    alpha=0.18 + 0.25 * (1 - r[i]), lw=0.7, zorder=1)
    # הילה + מכשיר
    sizes = 10 + 70 * (1 - r) ** 2
    ax.scatter(x, y, s=sizes * 6, color=SCREEN, alpha=0.06, zorder=2, linewidths=0)
    ax.scatter(x, y, s=sizes, color=SCREEN, alpha=0.9, zorder=3, linewidths=0)
    # כמה "התראות" אדומות
    k = rng.choice(n, 14, replace=False)
    ax.scatter(x[k], y[k], s=sizes[k] * 1.4, color=NOTIF, zorder=4, linewidths=0)
    # סמארטפון במרכז
    phone = FancyBboxPatch((-0.17, -0.3), 0.34, 0.6, boxstyle="round,pad=0.02,rounding_size=0.06",
                           fc=NIGHT, ec="white", lw=2.2, zorder=5)
    ax.add_patch(phone)
    ax.add_patch(FancyBboxPatch((-0.135, -0.235), 0.27, 0.47, boxstyle="round,pad=0,rounding_size=0.02",
                                fc=SCREEN, ec="none", alpha=0.85, zorder=6))
    ax.add_patch(Circle((0.15, 0.29), 0.045, color=NOTIF, zorder=7))
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(OUT / "cover_network.png", facecolor=NIGHT, bbox_inches="tight", pad_inches=0)
    plt.close(fig)


def smart_home():
    """בית חכם: בית במרכז, מכשירים מחוברים לרכזת (hub) ולענן."""
    plt.rcParams["font.family"] = ["Gisha", "Arial"]   # Hebrew-capable font for the labels
    fig, ax = plt.subplots(figsize=(9, 5.6), dpi=200)
    fig.patch.set_facecolor("white")
    # הבית
    # round 6: walls and roof raised so the top-row labels sit inside the house
    ax.add_patch(Polygon([[-3.6, -2.75], [3.6, -2.75], [3.6, 1.45], [0, 3.75], [-3.6, 1.45]],
                         closed=True, fc="#F5F7FA", ec=NIGHT, lw=3, zorder=1))
    # הענן
    for cx, cy, rr in [(0, 4.95, 0.55), (-0.6, 4.75, 0.42), (0.62, 4.75, 0.45), (0.25, 5.25, 0.4)]:
        ax.add_patch(Circle((cx, cy), rr, fc=SCREEN, ec="none", alpha=0.9, zorder=2))
    ax.text(0, 4.85, "ענן", ha="center", va="center", color="white", fontsize=16,
            fontweight="bold", zorder=3)
    # רכזת
    ax.add_patch(Circle((0, 0), 0.55, fc=NIGHT, ec=SCREEN, lw=3, zorder=4))
    ax.text(0, 0, "רכזת", ha="center", va="center", color="white", fontsize=15, fontweight="bold", zorder=5)
    ax.plot([0, 0], [0.55, 4.4], color=SCREEN, lw=2, ls="--", zorder=1)
    # מכשירים: (x, y, צבע, תווית, צורה)
    # Round 5: Hebrew labels (the figure was English-only inside a Hebrew book).
    # IMG-03: bottom row raised, one-line labels, so no label crosses the wall.
    devices = [(-2.1, 1.1, SUN, "תאורה\nחכמה"), (2.1, 1.1, NOTIF, "מצלמה"),
               (-2.2, -1.3, LEAF, "תרמוסטט"), (2.2, -1.3, SCREEN, "רמקול"),
               (-0.75, -1.45, NOTIF, "מנעול"), (0.8, -1.45, SUN, "מקרר"),
               (-1.0, 1.6, LEAF, "שקע"), (1.0, 1.6, SCREEN, "טלוויזיה")]
    for x, y, c, lab in devices:
        # IMG-06 (round 6): each link starts at the hub's edge (r = 0.55), not under its label
        d = np.hypot(x, y)
        ax.plot([0.55 * x / d, x], [0.55 * y / d, y], color=c, lw=1.6, alpha=0.7, zorder=3)
        for k in (1, 2, 3):  # "גלי" Wi-Fi
            ax.add_patch(Circle((x, y), 0.32 + 0.12 * k, fc="none", ec=c, lw=1, alpha=0.35 / k, zorder=3))
        ax.add_patch(Circle((x, y), 0.32, fc=c, ec="white", lw=2, zorder=6))
        # top-row devices get their label ABOVE the node, so the link to the hub (which
        # leaves the node downwards) cannot cross it (IMG-06: "טלוויזיה" sat on its own link)
        above = y > 1.5
        ax.text(x, y + 0.62 if above else y - 0.62, lab, ha="center", va="bottom" if above else "top",
                fontsize=12, color=NIGHT, zorder=7)
    # בעלים עם סמארטפון
    ax.add_patch(FancyBboxPatch((4.2, -0.7), 0.6, 1.1, boxstyle="round,pad=0.03,rounding_size=0.1",
                                fc=NIGHT, ec=SCREEN, lw=2, zorder=6))
    ax.add_patch(Circle((4.75, 0.36), 0.09, color=NOTIF, zorder=7))
    ax.annotate("", xy=(4.15, -0.15), xytext=(0.6, -0.1),
                arrowprops=dict(arrowstyle="<->", color=NIGHT, lw=1.5, ls=":"))
    ax.text(4.5, -0.95, "אתם", ha="center", va="top", fontsize=14, fontweight="bold", color=NIGHT)
    ax.set_xlim(-4.0, 5.2)
    ax.set_ylim(-3.1, 5.8)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(OUT / "smart_home.png", bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)


if __name__ == "__main__":
    import overlap_check                    # IMG-06 (round 6): illustrations are checked too
    overlap_check.install(OUT)
    cover_network()
    smart_home()
    print("images written to", OUT)
