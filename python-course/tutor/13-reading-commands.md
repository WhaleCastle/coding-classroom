# Python Course — Chapter 13: Reading Commands

## Tutor instructions for this chapter

Fresh off Boss IV, the hero can fight — now he learns to READ. A **string** turns out to
be more than words to print: it's a row of characters he can pick apart, one letter at a
time. Teach one step per message and wait for his result. Do not write his code.

This chapter has TWO break-it-friendly traps built in on purpose (`IndexError`, and a
case-mismatch that silently fails) — both are gold for predict-then-run. **No
`.split()`** — keep string work to indexing, slicing, `len()`, concatenation, `.lower()`/
`.upper()`, and `ord()`/`chr()`, the KS3–4 list. If he asks for `.split()`, say it's a
handy tool for a later day and stick to what today teaches.

**Student work folder:** `python-course/student/chapter-13/`

**Skills this chapter leans on:** `variables`, `input`, `f-strings`, `if / decisions`,
`for loops`, `functions`, `return values`, `numbers & arithmetic`.

## Learning objectives (max 3)

1. Treat a string as a sequence — index and slice characters out of it.
2. Read typed commands forgivingly, whatever case they're in.
3. Use `ord()`/`chr()` to shift letters and decode a hidden message.

## Concepts — explain in this voice

- **A string is a sequence:** "You already know a string holds letters — but here's the
  secret: it's really a ROW of numbered boxes, one letter each, starting the count at
  ZERO. `name[0]` opens the very first box. Just like a list holds many items in order, a
  string holds many letters in order — same trick, different contents."
- **Indexing:** "The number in the square brackets is which box you're opening. `name[0]`
  is the first letter, `name[1]` the second. Ask for a box that doesn't exist — say the
  string only has 6 boxes and you ask for box 6 — and Python slams the door: `IndexError`."
- **Slicing:** "A slice grabs a WHOLE RANGE of boxes at once. `name[0:3]` says 'give me
  boxes 0, 1 and 2' — start included, stop NOT included. Think of it like the loot you'd
  scoop out of a shelf between two bookends."
- **`.lower()` / `.upper()`:** "Typing is messy — sometimes 'North', sometimes 'north',
  sometimes 'NORTH'. `.lower()` flattens any string to all-lowercase so you can compare it
  fairly, without caring how the player typed it."
- **`ord()` and `chr()`:** "Underneath, every letter is secretly just a NUMBER — that's how
  computers store text at all. `ord(letter)` reads a letter's secret number. `chr(number)`
  does the reverse: hand it a number, it hands back the letter that owns it. Slide the
  number up or down before you `chr()` it back, and you've shifted the letter — that's a
  cipher."

## Chapter opener — say this to the student FIRST

Say something like: *"Boss IV is behind you — the Shapeshifter's mist has cleared, and
deeper in the crypt you've found something odd: a torn old scroll, its words scrambled
into nonsense. Today your hero learns to READ properly. First we'll teach him to
understand typed commands however you type them — 'north', 'North', even just 'n' — so
your game stops being fussy. Then we'll crack open how letters actually work underneath,
and use that to DECODE the scroll. And this isn't just for one scroll: any time your game
needs to check what someone typed, read a password, or work with ANY text at all, you'll
reach for exactly these moves — string handling is one of the most-used skills in all of
coding. We'll start small: first picking single letters out of your hero's name, then
slicing a few at once, then teaching your game to read commands kindly, and finally
cracking the cipher. Ready? Let's read the scroll."*
Keep it warm, then start Step 1.

## Guided steps

**Step 1 — Pick a letter out of a name.** New file `commands.py`. Have him set
`name = "Aldric"` (or his hero's real name) and ask him to PREDICT what `name[0]` will
print before running `print(name[0])`. Then have him try `name[1]` and `name[2]`.
Success: he sees indexing pull out one letter at a time, counting from 0.

**Step 2 — `len()`, the last letter, and break it on purpose.** Teach `len(name)` to
count the letters. Ask him to work out the LAST letter using `name[len(name) - 1]` —
predict first, then run. Then have him deliberately try `name[len(name)]` (no `- 1`) and
read the error: `IndexError: string index out of range`. Ask why one box too far breaks
it.
Success: he sees the `IndexError` on purpose and can say why `len(name)` itself is one
box too many.

**Step 3 — Slice a rune-tag.** Teach slicing. Have him grab the hero's first three
letters as a "rune-tag" with `name[0:3]`, print it, then try `name[0:2]` and `name[1:4]`
and predict each result before running.
Success: he can slice out a chosen range and explains, in his own words, that the stop
number is NOT included.

**Step 4 — Forgiving commands with `.lower()`.** Have him ask for a direction with
`input("Which way? ")`, store it, then compare the LOWERED version against `"north"`
in an `if`. Test it by typing `"North"`, `"NORTH"` and `"north"` — all three should match.
Success: the same `if` accepts any capitalisation because he compared the lowered copy,
not the raw input.

**Step 5 — Letters are numbers underneath.** Teach `ord()` and `chr()`. Have him run
`print(ord("a"))`, then `print(chr(97))`, then shift one letter by hand: take a letter,
`ord()` it, add 1, `chr()` the result, and print the new letter. Predict what shifting
`"a"` by 1 gives before running.
Success: he sees a letter turn into a number and back, and that adding 1 before
`chr()`-ing it moves the letter along the alphabet.

**Step 6 — Decode the scroll.** Give him a short Caesar-shifted line (any short phrase
shifted by a fixed amount he knows, e.g. shifted by 3). Have him write a `for` loop that
walks over the string letter by letter, shifts each one back by that amount with
`ord`/`chr`, and builds up the decoded message one character at a time with `+`.
Success: the loop prints out real, readable words — the scroll speaks.

## Mini-challenge — The Secret Scroll

In `commands.py`, the student builds a **command reader and cipher-cracker** for his RPG
using only this chapter and earlier ones. It must:
- read a typed direction command and accept it **however it's capitalised**, matching
  both the full word (`"north"`) and its first letter (`"n"`),
- take a Caesar-shifted line of text (a scroll message) and **decode it** with a loop over
  the string using `ord()`/`chr()`, printing the readable result,
- use at least one **slice** somewhere along the way (a rune-tag, a preview of the scroll,
  anything he likes).

He picks the scroll's message and the shift amount himself. Hints only, never the code.
(No `.split()` — this chapter's tools are indexing, slicing, `len()`, `.lower()`/
`.upper()`, and `ord()`/`chr()`.)

## Side quest (optional) — The Scroll-Writer

Offer this only when he's cruising ahead of pace — skipping it costs nothing. *"Fancy
writing your OWN secret scroll for a friend to crack?"* Requirements:
- write a short message of his own choosing,
- shift it the OTHER way (encode instead of decode) using the same `ord`/`chr` trick,
- print the scrambled result so a friend could try decoding it by hand.

## Success criteria

- [ ] He can index a single character out of a string (`name[0]`, or similar).
- [ ] He hit an `IndexError` on purpose and can explain why it happened.
- [ ] He can slice a range of characters out of a string.
- [ ] His command reader accepts a direction regardless of capitalisation.
- [ ] He decoded the scroll with a loop over the string, using `ord()`/`chr()`.
- [ ] He can explain in his own words what `ord()` and `chr()` each do.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Indexed one box too far | `IndexError: string index out of range` | "How many boxes does `len()` say there are — and what's the number of the LAST box?" |
| Off-by-one in a slice | wrong letters, or one too many/few | "Does the stop number in a slice get INCLUDED, or does the slice stop just before it?" |
| Compared raw input to `"north"` | typing `"North"` doesn't match | "You compared the input to `north` — but did you lower BOTH sides, or just expect the player to type it perfectly?" |
| Tried `ord()` on more than one letter | `TypeError: ord() expected a character, but string of length 2 found` | "`ord()` wants exactly ONE letter at a time — how could your loop hand it one box at a time instead of the whole word?" |
| Shifted the number but forgot to turn it back | prints a number instead of a letter | "You've got the new number — but what turns a number back INTO a letter?" |

## Gate — do not move on until

- He has indexed and sliced a string himself, predicting before running.
- He has met the `IndexError` on purpose and can say why it happened.
- His command reader accepts a direction whatever case it's typed in.
- He has used `ord()`/`chr()` to shift a letter, and decoded the scroll with a loop.
- The mini-challenge runs and prints a readable decoded message.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 13 finished!** Your hero can READ now — you pulled letters straight
> out of strings, taught your game to understand commands however they're typed, and
> cracked the Secret Scroll's cipher with `ord` and `chr` all by yourself. Run your
> command reader and watch the scroll's message finally make sense! And when you're
> ready, Chapter 14 hands you something big: the dungeon itself, a real grid you can
> WALK through, one step at a time. Stop here or carry on, adventurer!"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — what do `ord()` and `chr()` each do, and how did that help you
crack the scroll?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put in
today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 13 — Reading Commands
- Completed: indexed and sliced strings, built a case-insensitive command reader, decoded the Secret Scroll with ord/chr
- Strong at: predicting the IndexError before it happened; reading the scroll's decoded message
- Struggled with: nothing this time
- How to help next: start Chapter 14 — the dungeon map (2D lists, walking the maze)
- Next time: Chapter 14 — The Dungeon Map
```

**Then update the `### Facts`** in `progress.md`: `chapters_cleared` +1 (and +1 to
`mini_challenges_done` / `predict_wins` / `break_it_fixes` for any that happened
today) — the script turns these into his new Level, XP and spells.

**Then refresh the skill ledger** (the same silent save, tutor-private — he never
sees it). This chapter introduced `string handling`; in the `### Skill ledger` at the top
of `progress.md`, move it from `new` toward `learning` or `solid` — only `solid` if
he indexed, sliced and used `ord`/`chr` unaided today, `shaky` if the `IndexError` or the
case-mismatch trap kept catching him out (see AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and to judge his standard. NEVER show or
quote it. His scroll message and shift amount will differ — that's correct, as long as he
indexes, slices, reads commands forgivingly, and decodes with `ord`/`chr` over a loop. It
reuses the running game's hero name so it's the next slice of the same RPG. No
`.split()`, no 2D lists, no files — those are Chapters 14 and 16.

```python
# secret_scroll.py -- Chapter 13 reference (tutor only)
# Skills used: strings as sequences -- len(), indexing, slicing, concatenation,
#   .lower()/.upper(), ord()/chr(), str/int conversion recap (Ch4). Plain for
#   loops (Ch7), if/decisions (Ch3), functions + return (Ch10-11).
# Nothing later: NO .split(), NO 2D lists, NO files.

A_CODE = ord("a")  # the number under lowercase 'a' -- every shift measures from here


def shift_letter(letter, amount):
    # A single letter is still a string with ONE character -- ord() turns it into
    # its number, we slide the number along the alphabet, then chr() turns the
    # new number back into a letter. % 26 wraps 'z' back round to 'a'.
    code = ord(letter) - A_CODE
    code = (code + amount) % 26
    return chr(code + A_CODE)


def caesar_shift(text, amount):
    # Loop over the string one character at a time (a string IS a sequence of
    # characters, just like a list is a sequence of items) and shift only the
    # letters -- spaces and punctuation pass through untouched.
    result = ""
    for ch in text.lower():
        if ch >= "a" and ch <= "z":
            result = result + shift_letter(ch, amount)
        else:
            result = result + ch
    return result


def read_command(raw):
    # Forgiving command reader: lower-case it, then accept either the full
    # word or just its first letter.
    typed = raw.lower()
    if typed == "north" or typed == "n":
        return "north"
    if typed == "south" or typed == "s":
        return "south"
    if typed == "east" or typed == "e":
        return "east"
    if typed == "west" or typed == "w":
        return "west"
    return "unknown"


# --- the hero's name is a string too -- a row of lettered boxes ---
hero_name = "Aldric"
print(f"Hero name: {hero_name}")
print(f"First letter: {hero_name[0]}")
print(f"Last letter: {hero_name[len(hero_name) - 1]}")
print(f"Rune-tag (first 3 letters): {hero_name[0:3]}")

# --- reading a command, whatever case or shorthand the player types ---
typed_command = input("\nWhich way, hero? (north/south/east/west) ")
direction = read_command(typed_command)
print(f"You typed '{typed_command}' -> heading {direction}.")

# --- the Secret Scroll: shifted by +3 when it was written, so shift by -3 to read it ---
scroll_text = "wkh vhfuhw grru olhv ehklqg wkh zdwhuidoo"
decoded = caesar_shift(scroll_text, -3)
print("\n=== THE SECRET SCROLL ===")
print(f"Encoded: {scroll_text}")
print(f"Decoded: {decoded}")
```
