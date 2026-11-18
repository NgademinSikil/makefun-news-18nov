#!/usr/bin/env python3
"""Draw the news-image-20261118 entry: a one-page newspaper front page.

"THE WORLD — WEDNESDAY 18 NOVEMBER 2026": the Trump-Putin-Xi summit as
the lead story, four panel stories (Gulf strikes, Kerch Bridge, Ebola in
the DRC, Democrats take Alaska) and a bottom strip of three short items
(Cyclone Xavier, the Papua New Guinea quake, the World Court Myanmar case).

Everything is drawn with Pillow primitives at 1024x1024 — flat shapes,
serif headlines, red rules — so the page reads as a newspaper and stays
legible when the judge looks at it small.

Run:  python3 generate_entry.py   ->   entry.png (1024x1024, PNG)
"""
import textwrap

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 26
RED = (178, 24, 24)
INK = (12, 12, 12)
GREY = (70, 70, 70)
PAPER = (253, 252, 246)
BLUE = (28, 68, 150)
SKY = (168, 205, 235)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap of `text` to fit `width` pixels with font `fnt`."""
    lines = []
    for chunk in text.split("\n"):
        line = ""
        for word in chunk.split():
            trial = (line + " " + word).strip()
            if draw.textlength(trial, font=fnt) <= width:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def hrule(draw, y, x0=None, x1=None, color=RED, width=4):
    x0 = MARGIN if x0 is None else x0
    x1 = W - MARGIN if x1 is None else x1
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


def flag(draw, x, y, w, h, kind):
    """A small flat flag on a pole: us / ru / cn."""
    pole = 5
    draw.rectangle([x - pole, y - 14, x, y + h], fill=(60, 60, 60))
    if kind == "us":
        draw.rectangle([x, y, x + w, y + h], fill=(191, 10, 48))
        for i in range(1, 7, 2):
            draw.rectangle([x, y + i * h // 7, x + w, y + (i + 1) * h // 7],
                           fill=(255, 255, 255))
        draw.rectangle([x, y, x + w * 0.42, y + h * 4 // 7], fill=(0, 40, 104))
        for r in range(3):
            for c in range(4):
                cx = x + 8 + c * 15
                cy = y + 8 + r * 12
                draw.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=(255, 255, 255))
    elif kind == "ru":
        third = h // 3
        draw.rectangle([x, y, x + w, y + third], fill=(255, 255, 255))
        draw.rectangle([x, y + third, x + w, y + 2 * third], fill=(0, 57, 166))
        draw.rectangle([x, y + 2 * third, x + w, y + h], fill=(213, 0, 50))
    else:  # cn
        draw.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
        cx, cy = x + 14, y + 12
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(255, 222, 0))
        for sx, sy in [(x + 34, y + 6), (x + 40, y + 16), (x + 36, y + 28),
                       (x + 26, y + 30)]:
            draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 222, 0))
    draw.rectangle([x, y, x + w, y + h], outline=(0, 0, 0), width=1)


def summit_scene(draw, box):
    """Three flags behind a long summit table with three chairs."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(232, 238, 245))
    draw.rectangle([x0, y1 - 26, x1, y1], fill=(120, 140, 120))
    fw, fh = 84, 46
    gap = (x1 - x0 - 3 * fw) // 4
    for i, kind in enumerate(("us", "ru", "cn")):
        fx = x0 + gap + i * (fw + gap)
        flag(draw, fx, y0 + 16, fw, fh, kind)
    # three chairs behind the table
    ty = y0 + 100
    for cx in (x0 + 190, (x0 + x1) // 2, x1 - 190):
        draw.rectangle([cx - 26, ty - 34, cx + 26, ty - 4], fill=(40, 60, 110))
        draw.rectangle([cx - 4, ty - 4, cx + 4, ty + 8], fill=(40, 60, 110))
    # table
    draw.rectangle([x0 + 90, ty, x1 - 90, ty + 12], fill=(96, 58, 28))
    draw.rectangle([x0 + 110, ty + 12, x0 + 126, y1 - 26], fill=(70, 42, 20))
    draw.rectangle([x1 - 126, ty + 12, x1 - 110, y1 - 26], fill=(70, 42, 20))
    draw.text(((x0 + x1) // 2, y1 - 13), "SHENZHEN — THURSDAY",
              font=font(SANS_B, 18), fill=(255, 255, 255), anchor="mm")


def gulf_scene(draw, box):
    """Two jets over a dark sea, one drone dot intercepted."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=SKY)
    draw.rectangle([x0, y1 - 26, x1, y1], fill=(24, 68, 120))
    for jx, jy in ((x0 + 26, y0 + 26), (x0 + 66, y0 + 56)):
        draw.polygon([(jx, jy), (jx + 42, jy + 10), (jx + 8, jy + 16),
                      (jx + 2, jy + 26)], fill=(40, 40, 40))
        draw.line([(jx, jy + 13), (jx - 22, jy + 20)], fill=(120, 120, 120),
                  width=3)
    draw.ellipse([x1 - 30, y0 + 18, x1 - 18, y0 + 30], fill=RED)
    draw.line([(x1 - 40, y0 + 40), (x1 - 24, y0 + 24)], fill=RED, width=3)
    draw.text((x0 + 8, y1 - 21), "THE GULF",
              font=font(SANS_B, 13), fill=(255, 255, 255))


def kerch_scene(draw, box):
    """A bridge with its road span dropped into the strait; a train on rail."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=SKY)
    draw.rectangle([x0, y1 - 30, x1, y1], fill=(36, 110, 160))
    # piers standing on either side of the gap
    draw.rectangle([x0, y0 + 60, x0 + 34, y1 - 30], fill=(90, 90, 90))
    draw.rectangle([x1 - 34, y0 + 60, x1, y1 - 30], fill=(90, 90, 90))
    # broken deck stubs reaching into the gap from each pier
    draw.rectangle([x0, y0 + 54, x0 + 56, y0 + 62], fill=(60, 60, 60))
    draw.rectangle([x1 - 56, y0 + 54, x1, y0 + 62], fill=(60, 60, 60))
    draw.line([(x0 + 56, y0 + 58), (x0 + 64, y0 + 66)], fill=RED, width=3)
    draw.line([(x1 - 56, y0 + 58), (x1 - 64, y0 + 66)], fill=RED, width=3)
    # fallen road span lying tilted in the strait
    draw.polygon([(x0 + 44, y1 - 12), (x0 + 84, y1 - 20),
                  (x0 + 80, y1 - 30), (x0 + 40, y1 - 22)], fill=(70, 70, 70))
    draw.line([(x0 + 44, y1 - 17), (x0 + 82, y1 - 25)], fill=RED, width=3)
    # a train on the rail deck of the left pier
    draw.rectangle([x0 + 2, y0 + 32, x0 + 32, y0 + 54], fill=(178, 24, 24))
    draw.rectangle([x0 + 7, y0 + 38, x0 + 14, y0 + 46], fill=(255, 255, 255))
    draw.rectangle([x0 + 19, y0 + 38, x0 + 26, y0 + 46], fill=(255, 255, 255))


def ebola_scene(draw, box):
    """Two field tents with a red cross, under a pale sun."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(240, 232, 210))
    draw.ellipse([x1 - 34, y0 + 8, x1 - 10, y0 + 32], fill=(240, 190, 60))
    for tx, tw in ((x0 + 10, 58), (x0 + 66, 46)):
        top = (tx + tw // 2, y0 + 52)
        draw.polygon([top, (tx, y1 - 26), (tx + tw, y1 - 26)],
                     fill=(226, 214, 180), outline=(120, 100, 60))
        draw.line([top, (tx + tw // 2, y1 - 26)], fill=(120, 100, 60), width=2)
    cx, cy = x0 + 38, y0 + 78
    draw.rectangle([cx - 4, cy - 12, cx + 4, cy + 12], fill=RED)
    draw.rectangle([cx - 12, cy - 4, cx + 12, cy + 4], fill=RED)
    draw.rectangle([x0, y1 - 26, x1, y1], fill=(150, 120, 70))


def alaska_scene(draw, box):
    """A ballot box with a ballot going in and a big tick."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(228, 236, 228))
    draw.rectangle([x0 + 22, y0 + 58, x0 + 92, y1 - 20], fill=(150, 90, 40))
    draw.rectangle([x0 + 16, y0 + 48, x0 + 98, y0 + 58], fill=(120, 66, 28))
    draw.rectangle([x0 + 44, y0 + 51, x0 + 70, y0 + 55], fill=(20, 20, 20))
    # a white ballot sheet standing in the slot
    draw.rectangle([x0 + 47, y0 + 8, x0 + 67, y0 + 52],
                   fill=(255, 255, 255), outline=(0, 0, 0), width=1)
    draw.line([(x0 + 52, y0 + 18), (x0 + 62, y0 + 18)], fill=(0, 0, 0), width=2)
    draw.line([(x0 + 52, y0 + 26), (x0 + 62, y0 + 26)], fill=(0, 0, 0), width=2)
    draw.line([(x0 + 52, y0 + 40), (x0 + 57, y0 + 46), (x0 + 64, y0 + 34)],
              fill=(0, 140, 60), width=3)
    draw.line([(x1 - 44, y0 + 78), (x1 - 30, y0 + 96), (x1 - 4, y0 + 44)],
              fill=(0, 140, 60), width=7)
    draw.text((x0 + 8, y0 + 6), "56", font=font(SANS_B, 26), fill=BLUE)


def panel(draw, box, headline, body, scene):
    """One 2x2-grid panel: headline + body on the left, picture on the right."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, outline=INK, width=2)
    pic = (x1 - 132, y0 + 10, x1 - 10, y1 - 10)
    scene(draw, pic)
    tx = x0 + 12
    tw = (x1 - 132) - tx - 10
    hf = font(SANS_B, 25)
    lines = wrap(draw, headline, hf, tw)[:2]
    y = draw_lines(draw, lines, tx, y0 + 10, hf, INK, 30)
    bf = font(SANS, 19)
    blines = wrap(draw, body, bf, tw)[:4]
    draw_lines(draw, blines, tx, y + 4, bf, (30, 30, 30), 24)


def strip_item(draw, box, headline, body):
    x0, y0, x1, y1 = box
    hf = font(SANS_B, 20)
    lines = wrap(draw, headline, hf, x1 - x0)[:2]
    y = draw_lines(draw, lines, x0, y0, hf, INK, 24)
    bf = font(SANS, 17)
    blines = wrap(draw, body, bf, x1 - x0)[:3]
    draw_lines(draw, blines, x0, y + 3, bf, (30, 30, 30), 21)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---------------------------------------------------------
    d.text((W // 2, 30), "THE WORLD", font=font(SERIF, 88), fill=INK,
           anchor="ma")
    d.text((W // 2, 128), "WEDNESDAY 18 NOVEMBER 2026",
           font=font(SANS_B, 30), fill=INK, anchor="ma")
    hrule(d, 168)

    # --- lead story -------------------------------------------------------
    d.text((W // 2, 184), "THREE LEADERS MEET IN SHENZHEN",
           font=font(SERIF, 44), fill=INK, anchor="ma")
    lead = ("Trump, Putin and Xi meet Thursday in Shenzhen as the wars "
            "in Ukraine and the Gulf escalate.")
    lf = font(SANS, 22)
    lines = wrap(d, lead, lf, W - 2 * MARGIN - 20)
    y = draw_lines(d, lines, MARGIN + 10, 240, lf, (30, 30, 30), 28)
    summit_scene(d, (MARGIN, y + 8, W - MARGIN, y + 168))
    hrule(d, y + 182)

    # --- four panels, 2 x 2 ----------------------------------------------
    gy = y + 196
    pw = (W - 2 * MARGIN - 14) // 2
    ph = 196
    panels = [
        ("GULF STRIKES GO ON",
         "US confirms the Qeshm Island strike; Iran fires drones at US "
         "bases in Bahrain and Kuwait; Bahrain intercepts six drones.",
         gulf_scene),
        ("BRIDGE OUT, RAIL BACK",
         "Kerch Bridge road span lies in the strait; rail resumes on "
         "one track; the shipping channel is blocked.",
         kerch_scene),
        ("EBOLA'S TOLL ON CHILDREN",
         "DRC outbreak more than doubled: 11,000+ cases, 5,400 deaths; "
         "three in four infected children under five die.",
         ebola_scene),
        ("DEMOCRATS TAKE ALASKA",
         "Mary Peltola wins the Senate seat; Democrats reach 56 seats.",
         alaska_scene),
    ]
    for i, (head, body, scene) in enumerate(panels):
        px = MARGIN + (i % 2) * (pw + 14)
        py = gy + (i // 2) * (ph + 14)
        panel(d, (px, py, px + pw, py + ph), head, body, scene)

    # --- bottom strip -----------------------------------------------------
    sy = gy + 2 * ph + 14 + 16
    hrule(d, sy - 8)
    colw = (W - 2 * MARGIN - 28) // 3
    items = [
        ("CYCLONE XAVIER SLAMS COOK ISLANDS",
         "Category 5 hits the Northern Cook Islands."),
        ("6.0 QUAKE HITS PAPUA NEW GUINEA",
         "Magnitude 6.0 earthquake strikes Papua New Guinea."),
        ("WORLD COURT TO RULE ON MYANMAR CASE",
         "The World Court is to rule on the Myanmar genocide case."),
    ]
    for i, (head, body) in enumerate(items):
        x = MARGIN + i * (colw + 14)
        strip_item(d, (x, sy, x + colw, H - MARGIN), head, body)
        if i:
            d.line([(x - 7, sy), (x - 7, H - MARGIN - 6)], fill=(180, 180, 180),
                   width=1)

    img.save("entry.png", "PNG", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
