# Chapter 1 — Hero & Title Screen

## Tutor instructions for this chapter

This is the student's very first Python. Teach the steps below IN ORDER, one step
per message. After each step, wait for him to do it and tell you what happened.
Do not paste the whole exercise at once. Do not write his code.

Frame the whole course today: he is going to build his own role-playing game,
**The Crypt of Broken Keys**, bit by bit — and every adventure needs a title
screen, so that's what he starts. Keep the magic high: by the end of this chapter
he has made the opening screen of *his* game.

**Optional day-one taste:** if he's keen to see where this is heading, you may
invite him to PLAY the trailer first — in the terminal, run
`python python-course/tutor/assets/demo_play.py` (pure text, no setup). It's a
2–3 minute taste of the finished game: name a hero, walk a dungeon, fight a
goblin, reach an ending. Make clear it's a sneak peek made for him to *play* — he
will build his own version across the course; he is not expected to write code
like that yet. Keep it short, then start Step 1.

**Student work folder:** `python-course/student/chapter-01/`

## Learning objectives (max 3)

1. Run a Python file from the VS Code terminal.
2. Use `print()` to show text on the screen.
3. Understand what a "string" is (text in quotes).

## Concepts — explain in this voice

- **Python file:** "A Python file is just a text file full of instructions. Its
  name ends in `.py`. When you run it, Python reads it top to bottom and does what
  each line says — like reading out the opening crawl of your game, one line at a
  time."
- **print():** "`print()` is how your game speaks to the player. Whatever you put
  inside the brackets and quotes appears on the screen. It's the game's voice."
- **String:** "Text inside quotes is called a *string* — think of letters strung
  together on a necklace. Python needs the quotes to know where the words of your
  story start and end."

## Chapter opener — say this to the student FIRST

Before any step, briefly tell him the mission so he knows what's going on. Say
something like: *"Today we're going to make the very first thing a player sees in
your game — the **title screen**, the part that shows your game's name in big
letters when it starts. By the end you'll run it and watch your own game's opening
appear. We'll go in tiny steps: first we make an empty file to write in, then we
teach the computer to print one line of text, then you make it yours. Ready? Let's
make that file."* Keep it warm and short, then start Step 1.

## Guided steps

**Step 1 — Make the folder and file.**
Tell him every game starts as one empty file. Ask him to create a file called
`title.py` inside `python-course/student/chapter-01/` (right-click the folder →
New File). Explain `.py` means "Python will run this."
Success: the file exists and is open in the editor.

**Step 2 — The game speaks its first words.**
Teach `print()` as the game's voice. Ask him to type (himself, not copy-paste) a
print line that makes the game say `The Crypt of Broken Keys`. If he's unsure,
teach the *shape*: the word `print`, round brackets, quotes inside — let HIM
assemble it.
Success: the file contains a working print line with his game's name.

**Step 3 — Run it!**
Teach: open the terminal (View → Terminal), then type `python title.py` (on some
computers `python3 title.py`). Make sure the terminal is standing in the right
folder — if not, teach `cd` with his actual path, one step at a time.
Success: the title appears in the terminal. Celebrate — that's the first line of
his game talking back to him!

**Step 4 — Make it yours.**
Ask him to add a second print line: a tagline for his game (e.g. `A quest for the
lost keys...` — his words). Save and run. Point out the loop programmers live in:
edit → save → run.
Success: two lines now print, the second one his own.

**Step 5 — Break it on purpose.**
Ask him to delete ONE quote mark, save, and run. Let him see the red error. Say:
"Errors aren't bad — they're Python pointing at exactly where it got confused.
Every game developer sees hundreds a day." Then ask him to fix it and run again.
Success: he saw an error, read it, and fixed it himself.

**Step 6 — Predict the order.**
Ask him to add two MORE print lines (a line of stars, a "Press ENTER to begin"
prompt — his choice), and BEFORE running, ask which order they'll appear in. Then
run to check.
Success: he correctly predicted Python runs lines top to bottom.

## Mini-challenge — Title Screen for *his* RPG

In the SAME file `title.py` (or a fresh `title_screen.py` if he prefers), the
student designs the opening screen of his game using only print lines. It must
have:
- a top border line (e.g. a row of `=` or `*`),
- the game's title (he can name his own game — it doesn't have to be mine),
- a one-line tagline,
- a bottom border line,
- a final "Press ENTER to begin..." style prompt.

He designs the look himself. You may describe what a *border* is, but never type
his screen for him.

## Success criteria (check before finishing the chapter)

- [ ] `title.py` runs with no errors and prints his title screen.
- [ ] He fixed a quote error by himself.
- [ ] The title screen has borders, a title, a tagline and a prompt.
- [ ] He can answer in his own words: "What do the quotes do?" (mark where the
      text starts and ends).

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Missing quote | `SyntaxError: unterminated string literal` | "Python says a string never ended. Look closely at your quotes — count them. Do they come in pairs?" |
| Missing bracket | `SyntaxError` near the line's end | "Every opening bracket needs a partner to close it. Does yours have one?" |
| Capital P in `Print` | `NameError: name 'Print' is not defined` | "Python is fussy about capital letters. Look very carefully at how you spelled print." |
| `python` not found | `command not found` | "Try `python3` instead. Still stuck? Pause and ask Dad to check the install." |
| Running from the wrong folder | `can't open file 'title.py'` | "The terminal is standing in the wrong room. Which folder is it in? (`pwd` tells you.) How do we walk it into the right one?" |

## Gate — do not move on until

- He has run a file from the terminal at least 5 times in total.
- He fixed at least one error without you telling him the exact fix.
- His title screen works and has all five parts from the mini-challenge.

## End of chapter

Praise something specific he did (e.g. "you fixed that quote error all by
yourself"). **Play it:** ask him to run his title screen one more time and enjoy
seeing his own game's opening on the screen — this is the real opening of the game
he'll keep building. Then update `python-course/progress.md` yourself with a
progress block (see AGENTS.md), noting what he did well and anything he found
tricky, and tell him in a sentence what you logged. Tease: next time, the game
will ask the player their hero's name.

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and to judge whether his title
screen is up to standard. NEVER show or quote it. His version will look different
— that's correct, as long as it has the five parts and runs.

```python
# title.py — Chapter 1 reference (tutor only)
# Skills used: print(), strings. Nothing else has been taught yet.

# A title screen is just several print() lines, run top to bottom.
print("============================================")   # top border
print("        THE CRYPT OF BROKEN KEYS")              # the game's title
print("           a text adventure")                    # tagline
print("============================================")   # bottom border
print("Press ENTER to begin your quest...")             # prompt to the player
```
