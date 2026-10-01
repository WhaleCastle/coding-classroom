# Python Course — Bonus Quest 1: Draw Your Hero

## Tutor instructions for this chapter

This is an **optional holiday quest** — no gate pressure, nothing downstream
depends on it. Offer it any time AFTER Chapter 9 (it needs the hero sprite that
chapter introduces) — a good pick for a day he wants something visual and fun
instead of new syntax. It is entirely self-contained: **the whole chapter IS
the side quest**, so there is no separate "Side quest (optional)" section
below — don't look for one and don't invent one.

**The given asset, and the ONE rule that matters:** `tutor/assets/character_gen.py`
is a ~270-line Pillow (PIL) program that draws the pixel-art hero and saves
`hero_sprite.png`. It is a **given machine he tweaks, never code he authors** —
restate this plainly before Step 1: drawing shapes with PIL is graphics
programming, which is beyond KS3–4 and not something he is ever asked to
write from scratch (root `CLAUDE.md` rule 11, `00-course-overview.md`
"Graphics are a bonus, never a hurdle"). Today he is a colourist adjusting a
finished painting-by-numbers, not the artist who drew the lines.

**Where the tweak zone actually is (the file has no banner comment saying
"TWEAK ZONE" — point him here directly instead of letting him hunt):** near
the very top of the file sits a dictionary called `PALETTE` (about 18 lines
long, right after `W, H = 512, 640`). Every entry is a name and a 4-number
colour: `"shirt": (60, 142, 212, 255)`. The real, existing names he can find
and change include `skin`, `skin_sh`, `hair`, `hair_sh`, `hair_hi`, `shirt`,
`shirt_sh`, `shirt_hi`, `strap`, `strap_sh`, `pants`, `pants_sh`, `boot`,
`boot_sh`, `white`, `eye`, `mouth`, `blush` (the `_sh` ones are shadow tones,
`_hi` ones are highlights — changing a base colour without its shadow/highlight
partner can look a little odd, which is a fine thing to let him discover).
The sprite wears a **shirt/tunic**, not a cloak — `"shirt"` is the main
garment colour and the best first tweak (note: `"shirt"` also colours both
arm sleeves, since the arms reuse it — a nice "why did TWO things change?"
moment). There IS one safe non-colour number too: `SS = 4` near the very top
(the supersample/quality factor) — raising or lowering it changes how smooth
the edges look and how long it takes to render, but not the sprite's shape or
proportions, so it's safe to try. **Do not let him touch `W`, `H`, or any of
the coordinate numbers deeper in the file** — those are the geometry the
whole drawing is built from, and changing them warps or breaks the sprite.

**Getting Pillow installed:** the file needs the `PIL`/Pillow library. If
running it raises `ModuleNotFoundError: No module named 'PIL'`, walk him
through installing it before anything else:
- Windows: `py -m pip install pillow`
- Mac: `python3 -m pip install pillow`
Then try running the file again.

He already has a plain-text portrait too (`tutor/assets/hero_ascii.txt`, from
Chapter 9) — that one has no colours to tweak, it's just for context; today's
quest is entirely about `character_gen.py` and `hero_sprite.png`.

**Student work folder:** `python-course/student/bonus-01/` — have him copy
`tutor/assets/character_gen.py` into that folder first, so his edits and his
new sprite live in his own space and the original given file stays untouched.

**No new skill for the ledger.** This quest doesn't introduce anything the
skill ledger tracks — don't add or move an entry for it.

**Skills this chapter leans on:** `variables`, `numbers & arithmetic`.

## Learning objectives (max 3)

1. Find a named value inside a program he didn't write, change it, and predict
   the visual effect before checking.
2. Say, in his own words, the difference between a program he's GIVEN to tweak
   and code he writes himself.
3. Regenerate an image file and find his own new version of it.

## Concepts — explain in this voice

- **A given machine, not a blank page:** "Some code you write from nothing.
  Some code you're handed already finished, and your job is to turn its
  knobs. `character_gen.py` is the second kind — a machine that draws your
  hero. You're not writing a drawing program today (that's a whole other
  skill, way past what you've learned) — you're the colourist choosing what
  goes where."
- **Colour as four numbers (RGBA):** "Every colour in this file is four
  numbers in a row: how much Red, how much Green, how much Blue, and how
  see-through it is (that last one is called Alpha — 255 means fully solid,
  smaller numbers get more transparent). Change any of the first three and
  you change the colour; change the last one and you change how solid it
  looks."
- **Regenerate:** "This program doesn't EDIT the picture — every time you run
  it, it draws a brand new `hero_sprite.png` from scratch, using whatever
  numbers are in the file right now. Change a number, save the file, run it
  again, and a fresh sprite appears with your new choice baked in."

## Chapter opener — say this to the student FIRST

Say something like: *"Today's a holiday quest — no new coding rules, just
your hero, in YOUR colours. You already have a full-colour sprite of him from
Chapter 9; today you crack open the program that drew it and start turning
knobs. And this isn't just about today's picture — any time you use someone
else's finished program (a game, an app, a tool a friend wrote) and go
looking for the setting that changes ONE thing, you're doing exactly what
we're doing now. We'll run the picture-machine as it is, find the table of
colours inside it, change one on purpose and guess what happens, then make a
couple more changes of your own. Ready to redesign your hero?"* Keep it warm,
then start Step 1.

## Guided steps

**Step 1 — Meet the machine, run it as-is.** Have him copy
`tutor/assets/character_gen.py` into `student/bonus-01/`, open a terminal
there, and run it (`python3 character_gen.py` on Mac, `py character_gen.py`
on Windows). If Pillow isn't installed yet, install it first (see Tutor
instructions above), then re-run.
Success: `hero_sprite.png` appears in his folder; he opens it and sees the
same hero from Chapter 9.

**Step 2 — Find the colour table.** Have him open `character_gen.py` and
scroll to the `PALETTE = { ... }` dictionary near the top. Ask him to read
out three or four of the names he finds — he doesn't need to understand any
other line in the file.
Success: he can point to `PALETTE` and name a few entries in it (e.g.
`"shirt"`, `"hair"`, `"boot"`).

**Step 3 — Change the shirt colour (predict first).** Have him pick a new
first-three-number combo for `"shirt"` (e.g. swap the blue tunic for
`(156, 64, 200, 255)`, a purple) and ask him to PREDICT which part of the
sprite will change before he saves and re-runs.
Success: the sprite's shirt (and both sleeves — same colour, two places) come
out in his new colour; he notices it changed in more than one spot.

**Step 4 — Two more tweaks, his choice.** Have him pick at least two more
values to change — another `PALETTE` colour (hair, boots, the strap/sash,
blush) or the `SS` number — regenerating and checking the sprite after each
one.
Success: at least three total values have been changed and their effects
seen, one at a time.

**Step 5 — Final regenerate and open his hero.** Have him run the file one
last time and open the finished `hero_sprite.png` side by side (in his head
or in two windows) with the very first, unmodified version from Step 1.
Success: he can point out at least three differences between the original
sprite and his own.

## Mini-challenge — Your Hero, Your Colours

Using only `character_gen.py`'s `PALETTE` (and optionally `SS`), the student
produces a personalised `hero_sprite.png` he's genuinely happy with. It must:
- change at least THREE values from the original file,
- include at least one change to a main colour (not just a shadow/highlight
  tone) so the difference is obvious at a glance,
- be the result of him regenerating and checking the image after his changes
  (not just editing numbers blind and never looking).

He picks the colours and the look himself. Hints only, never the numbers to
use.

## Success criteria

- [ ] He ran `character_gen.py` unmodified once and saw the original sprite.
- [ ] He found `PALETTE` himself (with your pointer to look near the top of
      the file) and can read a colour's four numbers.
- [ ] He changed at least three values and regenerated `hero_sprite.png`
      after each change.
- [ ] His final sprite is visibly his own — colours he chose, not the
      defaults.
- [ ] He can explain in his own words why this file is "a machine he tweaks",
      not code he wrote from nothing.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Pillow isn't installed | `ModuleNotFoundError: No module named 'PIL'` | "This picture-machine needs a helper library called Pillow before it can run — want me to show you the one-line install command?" |
| Ran the file from the wrong folder | `python3: can't open file 'character_gen.py': [Errno 2] No such file or directory` | "Where is your terminal actually standing right now — the same folder you copied the file into?" |
| Edited a colour but the sprite looks unchanged | old sprite, no visible difference | "Did you SAVE the file before you ran it again? Python reads whatever's on disk, not what's still on your screen." |
| Typo'd a `PALETTE` key name instead of editing an existing one | nothing about the sprite changes | "Did that name already exist in `PALETTE`, or did you accidentally create a brand-new one nobody reads?" |
| Broke the dictionary's punctuation while editing a tuple | `SyntaxError` | "A colour is four numbers wrapped in brackets with commas between them — did you keep all of that when you typed your new numbers in?" |

## Gate — do not move on until

- Pillow is installed and `character_gen.py` runs without error.
- He found `PALETTE` and can describe what its four numbers mean.
- At least three values have been changed, and the final `hero_sprite.png`
  visibly differs from the original.
- He can say, in his own words, why this is a program he tweaks rather than
  writes.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's your **hero, redesigned!** You cracked open a real drawing program,
> found its colour table, and changed ___ , ___ and ___ until the sprite on
> screen was unmistakably YOURS. That's exactly how people customise games
> and tools they didn't build themselves — find the setting, change the
> value, see what happens. Go open your new `hero_sprite.png` one more time
> and admire your work! This was a side trip, not a step on the main road —
> whenever you're ready, we'll pick your main quest back up right where you
> left it. Great holiday quest, adventurer!"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — why is this file one you TWEAK, not one you write from
scratch?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put
in today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: Bonus 1 — Draw Your Hero (optional holiday quest)
- Completed: tweaked character_gen.py's PALETTE colours (and/or SS) and regenerated his own personalised hero_sprite.png
- Strong at: predicting which part of the sprite a colour value controls before regenerating
- Struggled with: nothing this time
- How to help next: pick his main quest back up wherever he left it
- Next time: <his real next chapter or boss, wherever he actually is>
```

**Then update the `### Facts`** in `progress.md`: this was an optional bonus
quest, so `chapters_cleared` does **NOT** change — bump only
`mini_challenges_done` +1 (his shirt-colour `predict_wins`, if he got it right,
was already counted the moment it happened — don't add it again). If your step
saves already made today's block, replace it — one block per day. The script turns these into his XP and spells; a
bonus quest still earns credit, it just isn't a numbered chapter.

**Skill ledger: leave it untouched.** This quest introduces no new tracked
skill, so there is nothing to move or add in the `### Skill ledger` block.

## Reference solution — TUTOR'S EYES ONLY, never show the student

There is no separate reference PROGRAM to write for this quest — the "correct
answer" is simply a successful tweak of the given `character_gen.py`, so use
this section only to know the file's real shape and to judge whether his
edits are sensible.

**The file's real structure (for your own orientation, not to recite to
him):** `W, H = 512, 640` sets the logical canvas size (do not let him touch
this — every shape's coordinates assume it). `SS = 4` is the supersample
factor (safe to change — bigger renders smoother/slower, smaller renders
faster/blockier, but the final image is always resized back to `W, H` so
nothing warps). `LW = 7 * SS` is the outline thickness, derived from `SS`.
Then the `PALETTE` dictionary (about 18 named RGBA colours) is the real tweak
zone — everything below it in the file (`part()`, `main()`, all the body-part
drawing functions) reads colours FROM `PALETTE` by name; it never needs to be
touched to get a personalised hero.

Below is a small EXCERPT — just the `PALETTE` dictionary with a handful of
values changed, each commented with WHY — showing the shape of a completed
tweak. This is NOT the full file (the other ~250 lines are the given asset,
unchanged) and it is never shown to the student; it exists purely so you can
recognise a well-formed edit versus a broken one.

```python
# character_gen.py -- EXCERPT ONLY (tutor reference), showing a completed tweak.
# Everything except this dictionary is the untouched given asset.

PALETTE = {
    "skin":        (244, 197, 140, 255),
    "skin_sh":     (216, 156, 100, 255),
    "hair":        (30, 30, 30, 255),     # was (90, 58, 38, 255) -- brown to jet-black
    "hair_sh":     (10, 10, 10, 255),     # was (62, 38, 24, 255) -- matching darker shadow
    "hair_hi":     (60, 60, 60, 255),     # was (122, 84, 56, 255) -- matching highlight tone
    "shirt":       (156, 64, 200, 255),   # was (60, 142, 212, 255) -- blue tunic to purple
    "shirt_sh":    (108, 40, 152, 255),   # was (40, 102, 162, 255) -- shadow kept in the same family
    "shirt_hi":    (196, 120, 232, 255),  # was (108, 178, 232, 255) -- highlight kept in the same family
    "strap":       (210, 180, 60, 255),
    "strap_sh":    (170, 140, 40, 255),
    "pants":       (74, 78, 92, 255),
    "pants_sh":    (52, 56, 68, 255),
    "boot":        (96, 58, 34, 255),
    "boot_sh":     (70, 40, 22, 255),
    "white":       (255, 255, 255, 255),
    "eye":         (54, 38, 30, 255),
    "mouth":       (120, 56, 52, 255),
    "blush":       (240, 150, 130, 60),   # was (..., 110) -- lower alpha = a fainter, subtler blush
}
```

Judging his version: any set of at least three changed values that still
renders a valid sprite (no crash, colours still solid where they should be
solid) meets the standard — his choices are meant to differ from this
example and from every other student's.
