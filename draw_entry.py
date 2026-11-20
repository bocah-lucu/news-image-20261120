#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news image (1024x1024 PNG).

Flat, newspaper-style layout: a navy header naming the day, one large
lead story, four smaller story panels, a climate strip and a footer.
All text is drawn with DejaVu fonts; all icons are plain Pillow shapes.
Run: python3 draw_entry.py  -> writes entry.png next to this file.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (15, 42, 68)
NAVY2 = (23, 62, 96)
PAPER = (247, 245, 239)
WHITE = (255, 255, 255)
INK = (24, 24, 24)
GREY = (90, 90, 90)
BORDER = (205, 205, 198)
RED = (178, 34, 34)
TEAL = (14, 110, 105)
BLUE = (30, 100, 170)
AMBER = (176, 124, 0)
GREEN = (34, 120, 60)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def kicker(draw, x, y, text, color):
    f = font(BOLD, 19)
    draw.text((x, y), text, font=f, fill=color)
    return y + 26


def globe(draw, cx, cy, r, sea=BLUE, land=GREEN):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=sea, outline=NAVY, width=3)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=3)
    # meridians
    draw.ellipse([cx - r // 3, cy - r, cx + r // 3, cy + r], outline=WHITE, width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=WHITE, width=2)
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 180, fill=WHITE, width=2)
    # land blobs
    draw.ellipse([cx - r + 8, cy - r + 14, cx - 6, cy - 4], fill=land)
    draw.ellipse([cx + 2, cy + 6, cx + r - 10, cy + r - 12], fill=land)


def cyclone_icon(draw, cx, cy, r):
    # spiral of arcs, storm-grey on pale blue
    for i, rr in enumerate(range(r, 8, -14)):
        a0 = i * 70
        draw.arc([cx - rr, cy - rr, cx + rr, cy + rr], a0, a0 + 220,
                 fill=(70, 110, 150), width=7)
    draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=RED)


def talks_icon(draw, x, y, w, h):
    # two overlapping circles: EU (teal) and RU (white), for "talks"
    draw.ellipse([x, y, x + 58, y + 58], fill=TEAL, outline=NAVY, width=2)
    draw.ellipse([x + 42, y + 6, x + 100, y + 64], fill=WHITE,
                 outline=NAVY, width=2)
    draw.text((x + 10, y + 16), "EU", font=font(BOLD, 22), fill=WHITE)
    draw.text((x + 54, y + 22), "RU", font=font(BOLD, 22), fill=NAVY)


def calendar_icon(draw, x, y, w, h):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=WHITE,
                           outline=NAVY, width=3)
    draw.rectangle([x, y, x + w, y + 26], fill=RED)
    draw.text((x + 8, y + 2), "JAN", font=font(BOLD, 18), fill=WHITE)
    draw.text((x + 12, y + 34), "2027", font=font(BOLD, 26), fill=NAVY)


def chart_icon(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=WHITE, outline=NAVY, width=2)
    # falling market line (red)
    pts = [(x + 8, y + 18), (x + 28, y + 30), (x + 48, y + 26),
           (x + 68, y + 52), (x + 88, y + 62)]
    draw.line(pts, fill=RED, width=5, joint="curve")
    # one rising green bar (the IPO)
    draw.rectangle([x + w - 22, y + 14, x + w - 10, y + h - 8], fill=GREEN)


def sun_icon(draw, cx, cy, r):
    for a in range(0, 360, 45):
        import math
        x1 = cx + int((r + 4) * math.cos(math.radians(a)))
        y1 = cy + int((r + 4) * math.sin(math.radians(a)))
        x2 = cx + int((r + 14) * math.cos(math.radians(a)))
        y2 = cy + int((r + 14) * math.sin(math.radians(a)))
        draw.line([x1, y1, x2, y2], fill=AMBER, width=4)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(240, 180, 40),
                 outline=AMBER, width=2)


def panel(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=WHITE, outline=BORDER, width=2)
    return x + 16, y + 12, w - 32


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- header ----
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((32, 22), "FRIDAY  20  NOVEMBER  2026", font=font(BOLD, 46), fill=WHITE)
d.text((32, 84), "THE WORLD IN ONE IMAGE  ·  WORLD NEWS",
       font=font(BOLD, 24), fill=(180, 205, 225))
d.text((W - 32, 30), "20 NOV", font=font(BOLD, 34), fill=(255, 210, 90),
       anchor="ra")
d.text((W - 32, 76), "2026", font=font(BOLD, 34), fill=(255, 210, 90),
       anchor="ra")

# ---- lead story: the Shenzhen summit ----
lx, ly, lw, lh = 32, 164, W - 64, 252
d.rectangle([lx, ly, lx + lw, ly + lh], fill=WHITE, outline=BORDER, width=2)
d.rectangle([lx, ly, lx + lw, ly + 6], fill=RED)
globe(d, lx + 78, ly + 128, 62)
tx = lx + 168
ty = ly + 18
kicker(d, tx, ty, "THE LEAD  ·  SHENZHEN, CHINA", RED)
d.text((tx, ty + 30), "The big three meet",
       font=font(BOLD, 36), fill=INK)
para(d, tx, ty + 76,
     "Trump, Xi and Putin hold the first-ever three-way summit "
     "and issue a “peace declaration”, pledging talks to cut "
     "nuclear risk — but no arms deal. The declaration does "
     "not mention Ukraine or Iran.",
     font(REG, 22), lw - 184, 29)

# ---- four panels, 2 x 2 ----
pw, ph = (W - 64 - 16) // 2, 196
px, py = 32, 432
panels = [
    ("CYCLONE  ·  INDIA", TEAL, "Akvan hits Odisha",
     "Severe Cyclone Akvan makes landfall near Gopalpur at noon, "
     "with winds to 110 km/h. Some 300,000 people are moved to safety.",
     "cyclone"),
    ("UKRAINE  ·  BERLIN", BLUE, "Europe ready to talk",
     "At a Berlin summit, Ukraine’s allies say they are ready for "
     "negotiations with Russia — with a united position.",
     "talks"),
    ("IRAN  ·  WASHINGTON", RED, "No Iran call until 2027",
     "Trump says the US will “see what happens” on Iran after "
     "January 1, and will take no new decision this year.",
     "calendar"),
    ("MARKETS  ·  NEW YORK", AMBER, "Stocks slide 2%",
     "The Dow falls 1,100 points, below 50,000, even as Anthropic’s "
     "record $81bn IPO jumps 17% on its first day.",
     "chart"),
]
for i, (kick, col, head, body, icon) in enumerate(panels):
    x = px + (i % 2) * (pw + 16)
    y = py + (i // 2) * (ph + 16)
    ix, iy, iw = panel(d, x, y, pw, ph)
    kicker(d, ix, iy, kick, col)
    d.text((ix, iy + 28), head, font=font(BOLD, 27), fill=INK)
    # icon at right of headline row
    if icon == "cyclone":
        cyclone_icon(d, x + pw - 52, iy + 52, 30)
    elif icon == "talks":
        talks_icon(d, x + pw - 118, iy + 34, 96, 62)
    elif icon == "calendar":
        calendar_icon(d, x + pw - 104, iy + 32, 84, 66)
    elif icon == "chart":
        chart_icon(d, x + pw - 118, iy + 32, 100, 66)
    # body text starts below the icon row so nothing overlaps
    para(d, ix, iy + 106, body, font(REG, 19), iw, 24)

# ---- climate strip ----
cx0, cy0, cw, ch = 32, 856, W - 64, 96
d.rectangle([cx0, cy0, cx0 + cw, cy0 + ch], fill=(232, 244, 232),
            outline=BORDER, width=2)
sun_icon(d, cx0 + 44, cy0 + 48, 22)
d.text((cx0 + 84, cy0 + 12), "CLIMATE",
       font=font(BOLD, 19), fill=GREEN)
para(d, cx0 + 84, cy0 + 36,
     "COP31’s new draft drops every mention of fossil fuels, "
     "a day before the summit closes — as Fiji declares a "
     "state of disaster over an El Niño drought.",
     font(REG, 19), cw - 100, 25)

# ---- footer ----
d.text((32, 972), "make.fun  ·  news-image-20261120",
       font=font(BOLD, 17), fill=GREY)
d.text((W - 32, 972), "Sources: Reuters, BBC, AP, IMD",
       font=font(REG, 17), fill=GREY, anchor="ra")

img.save("entry.png", "PNG", optimize=True)
print("saved entry.png", img.size)
import os
print("bytes:", os.path.getsize("entry.png"))
