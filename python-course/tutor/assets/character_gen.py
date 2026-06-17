"""
Comic-style game character sprite generator.

Draws a fully vector-style cartoon hero with bold outlines, flat cel-shaded
colors and a transparent background, then exports a game-ready PNG.

Render is done at SS x supersampling and downscaled with LANCZOS for clean,
antialiased edges. Everything is composed from reusable part-functions so you
can recolor / re-pose to make sprite variations.
"""

from PIL import Image, ImageDraw

# ----------------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------------
W, H = 512, 640          # logical canvas
SS = 4                   # supersample factor
CW, CH = W * SS, H * SS  # render canvas

OUTLINE = (26, 22, 24, 255)
LW = 7 * SS              # outline width

PALETTE = {
    "skin":        (244, 197, 140, 255),
    "skin_sh":     (216, 156, 100, 255),
    "hair":        (90, 58, 38, 255),
    "hair_sh":     (62, 38, 24, 255),
    "hair_hi":     (122, 84, 56, 255),
    "shirt":       (60, 142, 212, 255),
    "shirt_sh":    (40, 102, 162, 255),
    "shirt_hi":    (108, 178, 232, 255),
    "strap":       (210, 180, 60, 255),
    "strap_sh":    (170, 140, 40, 255),
    "pants":       (74, 78, 92, 255),
    "pants_sh":    (52, 56, 68, 255),
    "boot":        (96, 58, 34, 255),
    "boot_sh":     (70, 40, 22, 255),
    "white":       (255, 255, 255, 255),
    "eye":         (54, 38, 30, 255),
    "mouth":       (120, 56, 52, 255),
    "blush":       (240, 150, 130, 110),
}


def S(*vals):
    """Scale logical coordinates to the supersampled canvas."""
    return tuple(v * SS for v in vals)


def part(silhouette_fn, fills_fn):
    """
    Build a body part on its own RGBA layer.

    silhouette_fn(draw): draws the solid white silhouette (the part's shape).
    fills_fn(draw): draws color fills / shading freely; everything is then
    clipped to the silhouette so shading never spills outside the shape.
    Returns (layer, mask) so the caller can paste then stroke the outline.
    """
    sil = Image.new("L", (CW, CH), 0)
    silhouette_fn(ImageDraw.Draw(sil))

    color = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    fills_fn(ImageDraw.Draw(color))

    layer = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    layer.paste(color, (0, 0), sil)
    return layer, sil


def main():
    img = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    def stroke_ellipse(box, w=LW, col=OUTLINE):
        d.ellipse(S(*box), outline=col, width=w)

    def stroke_poly(pts, w=LW, col=OUTLINE):
        sp = [S(x, y) for (x, y) in pts]
        d.line(sp + [sp[0]], fill=col, width=w, joint="curve")
        # round the vertices so thick joints look smooth
        r = w // 2
        for (x, y) in sp:
            d.ellipse([x - r, y - r, x + r, y + r], fill=col)

    P = PALETTE

    # ---- helper to paste a built part then we stroke outline separately ----
    def place(layer):
        img.alpha_composite(layer)

    # ========================================================================
    # BACK HAIR (behind head)
    # ========================================================================
    def back_hair_sil(dr):
        dr.ellipse(S(168, 78, 344, 250), fill=255)
    def back_hair_fill(dr):
        dr.rectangle(S(0, 0, CW, CH), fill=P["hair_sh"])
    place(part(back_hair_sil, back_hair_fill)[0])
    stroke_ellipse((168, 78, 344, 250))

    # ========================================================================
    # LEGS + BOOTS  (drawn before torso so torso overlaps the hips)
    # ========================================================================
    def leg(cx):
        # leg silhouette: thigh -> calf
        top = 392
        knee = 500
        ankle = 560
        hw_top, hw_kn, hw_an = 34, 26, 24
        pts = [
            (cx - hw_top, top), (cx + hw_top, top),
            (cx + hw_kn, knee), (cx + hw_an, ankle),
            (cx - hw_an, ankle), (cx - hw_kn, knee),
        ]
        def sil(dr): dr.polygon([S(x, y) for x, y in pts], fill=255)
        def fill(dr):
            dr.rectangle(S(0, 0, CW, CH), fill=P["pants"])
            dr.polygon([S(cx, top), S(cx + hw_top, top),
                        S(cx + hw_kn, knee), S(cx + hw_an, ankle),
                        S(cx, ankle)], fill=P["pants_sh"])
        place(part(sil, fill)[0])
        stroke_poly(pts)

        # boot
        bpts = [
            (cx - hw_an - 3, ankle - 6), (cx + hw_an + 3, ankle - 6),
            (cx + hw_an + 6, ankle + 30), (cx + hw_an + 28, ankle + 30),
            (cx + hw_an + 28, ankle + 50), (cx - hw_an - 10, ankle + 50),
            (cx - hw_an - 10, ankle + 30),
        ]
        def bsil(dr): dr.polygon([S(x, y) for x, y in bpts], fill=255)
        def bfill(dr):
            dr.rectangle(S(0, 0, CW, CH), fill=P["boot"])
            dr.rectangle(S(cx - hw_an - 10, ankle + 38, cx + hw_an + 28, ankle + 50),
                         fill=P["boot_sh"])
        place(part(bsil, bfill)[0])
        stroke_poly(bpts)

    leg(220)
    leg(292)

    # ========================================================================
    # TORSO (tunic)
    # ========================================================================
    torso_pts = [
        (196, 250), (316, 250),       # shoulders
        (340, 300), (330, 392),       # right side
        (182, 392), (172, 300),       # left side
    ]
    def torso_sil(dr): dr.polygon([S(x, y) for x, y in torso_pts], fill=255)
    def torso_fill(dr):
        dr.rectangle(S(0, 0, CW, CH), fill=P["shirt"])
        # center-left highlight
        dr.polygon([S(196, 250), S(256, 250), S(256, 392), S(182, 392), S(172, 300)],
                   fill=P["shirt"])
        # right-side shade
        dr.polygon([S(256, 250), S(316, 250), S(340, 300), S(330, 392), S(256, 392)],
                   fill=P["shirt_sh"])
        # chest highlight stripe
        dr.ellipse(S(206, 262, 250, 340), fill=P["shirt_hi"])
    place(part(torso_sil, torso_fill)[0])
    stroke_poly(torso_pts)

    # shoulder strap (sash) for comic-hero flair
    strap_pts = [(196, 252), (236, 252), (322, 392), (286, 392)]
    def strap_sil(dr): dr.polygon([S(x, y) for x, y in strap_pts], fill=255)
    def strap_fill(dr):
        dr.rectangle(S(0, 0, CW, CH), fill=P["strap"])
        dr.polygon([S(216, 252), S(236, 252), S(322, 392), S(304, 392)], fill=P["strap_sh"])
    place(part(strap_sil, strap_fill)[0])
    stroke_poly(strap_pts)

    # belt
    d.rectangle(S(178, 386, 334, 410), fill=P["pants_sh"])
    d.rectangle(S(178, 386, 334, 410), outline=OUTLINE, width=LW)
    d.rectangle(S(244, 388, 268, 408), fill=P["strap"])
    d.rectangle(S(244, 388, 268, 408), outline=OUTLINE, width=LW // 2)

    # ---- ARMS (clean version, drawn over torso sides) ----
    def clean_arm(sx, sy, ex, ey, hx, hy):
        seg_w = 40  # arm thickness
        # outline underlay (slightly wider), then color fill on top
        d.line([S(sx, sy), S(ex, ey), S(hx, hy)], fill=OUTLINE,
               width=seg_w + LW, joint="curve")
        d.line([S(sx, sy), S(ex, ey), S(hx, hy)], fill=P["shirt"],
               width=seg_w, joint="curve")
        rr = seg_w // 2
        for px, py in [(sx, sy), (ex, ey)]:
            cx0, cy0 = S(px, py)
            d.ellipse([cx0 - rr, cy0 - rr, cx0 + rr, cy0 + rr], fill=P["shirt"])
        # hand
        d.ellipse(S(hx - 26, hy - 22, hx + 26, hy + 30), fill=P["skin"],
                  outline=OUTLINE, width=LW)
        d.chord(S(hx - 26, hy - 22, hx + 26, hy + 30), 20, 160, fill=P["skin_sh"])

    clean_arm(196, 262, 168, 330, 176, 392)   # character's right arm (image left)
    clean_arm(316, 262, 346, 330, 338, 392)   # character's left arm (image right)

    # ========================================================================
    # NECK
    # ========================================================================
    d.rectangle(S(236, 214, 276, 252), fill=P["skin"], outline=OUTLINE, width=LW)
    d.rectangle(S(236, 244, 276, 252), fill=P["skin_sh"])

    # ========================================================================
    # HEAD + FACE
    # ========================================================================
    head_box = (181, 80, 331, 240)
    def head_sil(dr): dr.ellipse(S(*head_box), fill=255)
    def head_fill(dr):
        dr.rectangle(S(0, 0, CW, CH), fill=P["skin"])
        dr.ellipse(S(256, 80, 331, 240), fill=P["skin"])
        dr.chord(S(*head_box), 300, 80, fill=P["skin_sh"])  # right cheek shade
        # blush
        dr.ellipse(S(196, 178, 226, 200), fill=P["blush"])
        dr.ellipse(S(286, 178, 316, 200), fill=P["blush"])
    place(part(head_sil, head_fill)[0])
    stroke_ellipse(head_box)

    # ears
    for ex in (181, 331):
        d.ellipse(S(ex - 12, 150, ex + 12, 186), fill=P["skin"], outline=OUTLINE, width=LW)

    # eyebrows
    d.line([S(206, 150), S(238, 146)], fill=OUTLINE, width=LW)
    d.line([S(274, 146), S(306, 150)], fill=OUTLINE, width=LW)

    # eyes (whites)
    for cx in (222, 290):
        d.ellipse(S(cx - 20, 158, cx + 20, 200), fill=P["white"], outline=OUTLINE, width=LW)
        # iris
        d.ellipse(S(cx - 12, 166, cx + 12, 196), fill=P["eye"])
        # pupil highlight
        d.ellipse(S(cx - 9, 168, cx + 1, 178), fill=P["white"])

    # nose
    d.line([S(256, 178), S(250, 196), S(262, 196)], fill=P["skin_sh"], width=LW, joint="curve")

    # mouth (cheeky grin)
    d.arc(S(228, 196, 284, 224), 10, 170, fill=OUTLINE, width=LW)
    d.line([S(228, 204), S(284, 204)], fill=OUTLINE, width=LW // 2)

    # ========================================================================
    # FRONT HAIR (over forehead)
    # ========================================================================
    hair_pts = [
        (176, 150), (172, 96), (206, 120), (214, 84),
        (244, 116), (256, 78), (270, 116), (300, 84),
        (308, 120), (340, 96), (336, 150),
        (314, 132), (300, 150), (286, 130),
        (256, 150), (226, 130), (212, 150), (198, 132),
    ]
    def hair_sil(dr): dr.polygon([S(x, y) for x, y in hair_pts], fill=255)
    def hair_fill(dr):
        dr.rectangle(S(0, 0, CW, CH), fill=P["hair"])
        # shade on the right
        dr.polygon([S(256, 78), S(340, 96), S(336, 150), S(256, 150)], fill=P["hair_sh"])
        # glossy highlight streaks on left bangs
        dr.line([S(206, 100), S(212, 140)], fill=P["hair_hi"], width=8 * SS)
        dr.line([S(228, 98), S(232, 124)], fill=P["hair_hi"], width=5 * SS)
    place(part(hair_sil, hair_fill)[0])
    stroke_poly(hair_pts)

    # ========================================================================
    # Finish: downscale with antialiasing
    # ========================================================================
    out = img.resize((W, H), Image.LANCZOS)
    out.save("hero_sprite.png")
    print("saved hero_sprite.png", out.size)


if __name__ == "__main__":
    main()