"""render_pages.py — מצלם עמודים מתוך PDF לתמונות PNG (ל-README ולבדיקה).
שימוש:  python python/render_pages.py book.pdf out_dir 1 5 9   (מספרי עמודים, מ-1)
         python python/render_pages.py book.pdf out.png --montage 1 3 4"""
import sys
from pathlib import Path
import fitz  # PyMuPDF

pdf, out, *rest = sys.argv[1:]
montage = "--montage" in rest
pages = [int(p) for p in rest if p != "--montage"]
doc = fitz.open(pdf)
pages = pages or list(range(1, doc.page_count + 1))
if montage:
    from PIL import Image
    ims = []
    for p in pages:
        pix = doc[p - 1].get_pixmap(dpi=55)
        ims.append(Image.frombytes("RGB", (pix.width, pix.height), pix.samples))
    W = sum(i.width for i in ims) + 8 * (len(ims) - 1)
    o = Image.new("RGB", (W, max(i.height for i in ims)), "#888")
    x = 0
    for i in ims:
        o.paste(i, (x, 0)); x += i.width + 8
    o.save(out)
else:
    Path(out).mkdir(parents=True, exist_ok=True)
    for p in pages:
        doc[p - 1].get_pixmap(dpi=110).save(f"{out}/page-{p:02d}.png")
print("pages:", doc.page_count)
