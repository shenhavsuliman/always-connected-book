"""
make_agents_chart.py: "the agent team in action" for the README.
Reads the real run log docs/agent-runs.json (duration, tokens and tool calls per agent run)
and draws docs/screenshots/agents-in-action.png.

Run:  python python/make_agents_chart.py
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
runs = json.loads((ROOT / "docs" / "agent-runs.json").read_text(encoding="utf-8"))
OUT = ROOT / "docs" / "screenshots" / "agents-in-action.png"

# colorblind-validated palette (same as make_graphs.py); one color per model
MODEL = {"opus": "#5B5FC7", "sonnet": "#00939F"}
INK, MUTED, GRID = "#2E3440", "#6B7280", "#E5E7EB"
plt.rcParams.update({"font.family": ["Segoe UI", "Arial"], "font.size": 10,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": GRID, "xtick.color": MUTED, "ytick.color": INK})

labels = [f"{r['agent']}  ·  {r['skill']}" for r in runs][::-1]
secs = [r["seconds"] / 60 for r in runs][::-1]
toks = [r["tokens"] / 1000 for r in runs][::-1]
cols = [MODEL[r["model"]] for r in runs][::-1]

fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.5, 0.42 * len(runs) + 1.6), sharey=True,
                             gridspec_kw={"wspace": 0.08})
for ax, vals, title, unit in [(a1, secs, "Run time", "min"), (a2, toks, "Tokens used", "k")]:
    bars = ax.barh(labels, vals, color=cols, height=0.62, edgecolor="white", linewidth=2)
    for b, v in zip(bars, vals):
        ax.text(b.get_width() + max(vals) * 0.015, b.get_y() + b.get_height() / 2,
                f"{v:.1f} {unit}" if unit == "min" else f"{v:.0f}{unit}", va="center", fontsize=9, color=INK)
    ax.set_title(title, loc="left", fontsize=11, fontweight="bold", color=INK)
    ax.grid(axis="x", color=GRID)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    ax.set_xlim(0, max(vals) * 1.22)
handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in MODEL.values()]
fig.legend(handles, [f"Claude {m.capitalize()}" for m in MODEL], loc="lower center", ncol=2,
           frameon=False, bbox_to_anchor=(0.5, -0.02))
total_t = sum(r["tokens"] for r in runs) / 1000
fig.suptitle(f"The agent team in action: {len(runs)} agent runs, {total_t:,.0f}k tokens "
             f"({sum(r['tools'] for r in runs)} tool calls)", x=0.02, ha="left",
             fontsize=12.5, fontweight="bold", color=INK)
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=170, bbox_inches="tight")
print("written", OUT)
