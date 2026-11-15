"""חותך את תרשים הבלוקים מתוך word/diagram.pdf ושומר כ-images/attention_loop.png."""
from pathlib import Path
import pymupdf

root = Path(__file__).resolve().parent.parent
page = pymupdf.open(root / "word" / "diagram.pdf")[0]
rect = None
for d in page.get_drawings():
    rect = d["rect"] if rect is None else rect | d["rect"]
rect = (rect + (-8, -8, 8, 8)) & page.rect
page.get_pixmap(dpi=250, clip=rect).save(root / "images" / "attention_loop.png")
print("diagram:", rect)
