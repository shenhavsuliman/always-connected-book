"""
overlap_check.py: shared figure-overlap check (QA-04 / IMG-04 / IMG-06).

Used by make_graphs.py AND make_images.py. Before every figure is saved, it reports
  - a legend or text label that covers drawn line points, including the interior of
    straight segments (a line drawn from A to B has only two vertices, so each segment
    is densified before testing; this is what caught IMG-06 in figure 6.1);
  - two text labels whose boxes overlap;
  - a text label that overlaps a filled patch it does not belong to (a node circle).
The results go to images/overlap-report.json, and qa-img FAILs on any finding.

    import overlap_check; overlap_check.install(OUT)   # once, at the start of __main__
"""
import itertools
import json
from pathlib import Path

import numpy as np
from matplotlib.figure import Figure
from matplotlib.patches import Circle
from matplotlib.text import Text

_report = {}


def _densify(xy, n=60):
    if len(xy) < 2:
        return xy
    out = [np.linspace(a, b, n) for a, b in zip(xy[:-1], xy[1:])]
    return np.vstack(out)


def findings(fig):
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    found = []
    for ax in fig.axes:
        ab = ax.get_window_extent(r)
        boxes = [("legend", ax.get_legend().get_window_extent(r).padded(12))] if ax.get_legend() else []
        # text labels: 2px margin; an annotation's arrow is excluded (it is meant to touch its point)
        boxes += [(f"text '{t.get_text()[:25]}'", Text.get_window_extent(t, r).padded(2))
                  for t in ax.texts if t.get_text().strip()]
        pts = [ln.get_transform().transform(_densify(np.asarray(ln.get_xydata(), float)))
               for ln in ax.lines if len(ln.get_xydata()) and ln.get_visible()]
        # outlines of polygons (e.g. the house's walls and roof) count as drawn lines too
        from matplotlib.patches import Polygon
        for p in ax.patches:
            if isinstance(p, Polygon) and p.get_linewidth() > 0:
                xy = p.get_xy()
                pts.append(p.get_transform().transform(_densify(np.vstack([xy, xy[:1]]))))
        pts = np.vstack(pts) if pts else np.empty((0, 2))
        pts = pts[(pts[:, 0] >= ab.x0) & (pts[:, 0] <= ab.x1) & (pts[:, 1] >= ab.y0) & (pts[:, 1] <= ab.y1)]
        for name, bb in boxes:
            inside = ((pts[:, 0] > bb.x0) & (pts[:, 0] < bb.x1) & (pts[:, 1] > bb.y0) & (pts[:, 1] < bb.y1)).sum()
            if inside:
                found.append(f"{name} covers {inside} drawn line points")
        for (n1, b1), (n2, b2) in itertools.combinations(boxes, 2):
            if b1.overlaps(b2):
                found.append(f"{n1} overlaps {n2}")
        # node circles (filled, opaque) that a label touches, other than the label's own centre
        for p in ax.patches:
            if isinstance(p, Circle) and p.get_fill() and p.get_alpha() in (None, 1):
                cb = p.get_window_extent(r)
                for name, bb in boxes:
                    if name != "legend" and bb.overlaps(cb):
                        cx, cy = (cb.x0 + cb.x1) / 2, (cb.y0 + cb.y1) / 2
                        if not (bb.x0 < cx < bb.x1 and bb.y0 < cy < bb.y1):  # label ON its node is fine
                            found.append(f"{name} touches a node circle")
    return found


def install(out_dir):
    """Wrap Figure.savefig so every figure is checked before it is written."""
    out_dir = Path(out_dir)
    save = Figure.savefig

    def checked(self, fname, *a, **k):
        _report[Path(fname).name] = findings(self)
        rep = out_dir / "overlap-report.json"
        old = json.loads(rep.read_text(encoding="utf-8")) if rep.exists() else {}
        old.update(_report)
        rep.write_text(json.dumps(old, ensure_ascii=False, indent=1), encoding="utf-8")
        return save(self, fname, *a, **k)
    Figure.savefig = checked
