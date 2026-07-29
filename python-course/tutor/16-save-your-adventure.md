# Python Course — Chapter 16: Save Your Adventure

## Tutor instructions for this chapter

He's escaped the Labyrinth Lord — now every run of his game starts from zero again,
and that's about to change. Today the hero learns to remember: writing his facts to
a real file on disk, then reading them back so the SAME hero comes back next time.
1–2 sessions; the ideas are small and mechanical (open, write, read, close) — go
step by step, teach one piece per message, wait for his result. Never write his code.

Use **plain `open` / `.close()`** throughout (KS3 style); mention `with open(...) as
file:` **once, one line**, as a shortcut he'll meet later — never require it. **No
`try`/`except` yet** (Chapter 17) — a `FileNotFoundError` loading before any save
exists is an expected, honest first-run trap, not a bug to prevent: the fix is
simply "play New Game first, so there's something to load."

**Student work folder:** `python-course/student/chapter-16/`

**Skills this chapter leans on:** `dictionaries`, `f-strings`, `for loops`,
`variables`, `input`.

## Learning objectives (max 3)

1. Write facts to a file with `open` / `.write()` / `.close()`, and read them back
   with `open` / a `for` loop over the lines / `.close()`.
2. Rebuild the hero record from the loaded text, turning numbers back into real
   numbers with `int()`.
3. Wire a save/load menu so the game remembers the hero between runs.

## Concepts — explain in this voice

- **File:** "A file is a page that survives after you close the notebook — unlike a
  variable, which vanishes the moment your program stops. It's your hero's **save
  crystal**: write him into it, and he outlives this one run of the game."
- **Opening it — `open(path, "w")` vs `open(path)`:** "Before writing OR reading a
  page you have to open the notebook to it. Add `\"w\"` and `open` gets it ready to
  WRITE — making the file if it's missing, wiping it blank if it isn't. Leave `\"w\"`
  out and `open` gets it ready to READ instead, from the top."
- **`.write()` and `.close()`:** "`.write()` puts words on the open page. `.close()`
  shuts the notebook properly — that's the step that actually saves your words to
  disk. Skip it, and sometimes nothing gets written at all."
- **Reading with a loop, then `.strip()`:** "A file opened for reading behaves like
  a list of lines — a `for` loop walks down it one at a time, like walking down your
  backpack. Each line drags an invisible newline stuck to its end; `.strip()` trims
  that ragged edge off, like trimming the perforated edge off a receipt."
- **`int()` on a loaded number:** "Everything out of a file is TEXT, even if it
  looks like a number — `\"30\"` isn't the number 30 to Python. `int()` converts it
  back into a real number you can do maths with."

## Chapter opener — say this to the student FIRST

Say something like: *"Right now, every time you close your game, your hero forgets
everything — HP, gold, name, gone. Today we build him a **save crystal**: a real
file that remembers him even after the program stops. Files aren't just for saving
games — any time a program needs to remember something after it closes, a
high-score table, your settings, a whole player database, this is the spell you
reach for. We'll start tiny: write one line to a file and watch it appear like
magic, then read it back. Then we'll save your WHOLE hero, load him back, and wire a
menu. Ready? Let's build the crystal."* Keep it warm, then start Step 1.

## Guided steps

**Step 1 — The magic moment.** New file `save_test.py`. Teach `open(path, "w")`:
`file = open("greeting.txt", "w")`, then `file.write("A hero passes this way.\n")`,
then `file.close()`. PREDICT first: before running, does `greeting.txt` exist yet?
Run it, then look in his folder (VS Code's file explorer) and open `greeting.txt`.
Success: the file APPEARS — it didn't exist until the program made it — with the
text inside.

**Step 2 — Read it back.** Teach `open(path)` with no `"w"` for reading:
`file = open("greeting.txt")`, a `for line in file:` loop printing each `line`, then
`file.close()`. Predict what prints, run it, and point out the little extra gap
after the line (the invisible `\n`). Teach `.strip()` to trim it:
`print(line.strip())`. Mention, in one line, that `with open(...) as file:` is a
shortcut for open-and-close he'll meet later — not needed today.
Success: it prints back with no stray blank line once `.strip()` is used.

**Step 3 — Save the hero.** Bring back the hero record (Chapter 9): a small `hero`
dictionary (`name`, `hp`, `gold`). Open `"save.txt"` to write, then write THREE
f-string lines, one fact per line, each ending `\n`: `f"{hero['name']}\n"`,
`f"{hero['hp']}\n"`, `f"{hero['gold']}\n"`. Close the file.
Success: `save.txt` appears with exactly three lines matching the hero's facts.

**Step 4 — Load the hero, and break it on purpose.** Open `"save.txt"` to read, loop
over the lines with `for` into a list. Rebuild the name with `lines[0].strip()`.
First try `hp = lines[1]` (no `int()`) then `hero["hp"] + 5` — he'll hit
`TypeError: can only concatenate str (not "int") to str`. Ask: "is that really a
NUMBER, or still text?" Fix with `hp = int(lines[1])` and `gold = int(lines[2])`.
Success: he saw the `TypeError`, understands why, and his loaded hero matches the
saved one exactly.

**Step 5 — A menu: new game or load game.** A small menu with `input` and
`if`/`elif`: option `1` starts a brand-new hero (name, starting HP and gold);
option `2` loads `save.txt` back into a hero using Step 4's code.
Success: `1` makes a fresh hero; `2`, once a save exists, provably loads the SAME
hero back — same stats, printed both times.

**Step 6 — Save after a fight.** Wire saving into his existing battle code (Chapters
10–12): right after a fight ends, save the hero's CURRENT hp and gold to
`save.txt`, so a win (or a narrow escape) is never lost.
Success: after a battle, `save.txt`'s numbers match the hero's new HP and gold, not
his starting ones.

## Mini-challenge — The Save Crystal

The student builds a save crystal for his RPG using only this chapter and earlier
ones. It must:
- **write** the hero's facts (at least THREE — e.g. name, HP, gold) with
  `open` / `.write()` / `.close()`,
- **read** them back with `open` / a `for` loop over the lines / `.close()`,
  converting numbers with `int()`,
- offer a **menu** choice between a new adventure and loading a saved one,
- **save again** after a battle, so progress updates rather than resetting.

He proves it works by playing, saving, quitting, and loading — the hero comes back
exactly as he left him. Hints only, never the code. (No `try`/`except` — Chapter 17.)

## Side quest (optional) — The Second Slot

Offer this only when he's cruising ahead of pace — skipping it costs nothing. A
rumour says the crypt hides a SECOND save crystal — enough for two heroes at once:
- two separate save files (`save1.txt` / `save2.txt`, or built from a slot number),
- the menu asks WHICH slot to save to or load from,
- both slots reuse the exact same write/read pattern he already built.

## Success criteria

- [ ] The game **writes** the hero's facts (at least 3) to a file with `open` /
      `.write()` / `.close()`.
- [ ] The game **reads** those facts back with `open`, a `for` loop over the lines,
      and `.close()`, using `int()` on the numbers.
- [ ] A **menu** lets him choose a new adventure or load a saved one.
- [ ] The hero **saves again** after a battle, so his progress updates.
- [ ] He can explain, in his own words, why the game needs a FILE to remember the
      hero instead of just a variable.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Loads before ever saving | `FileNotFoundError: [Errno 2] No such file or directory` | "The very first time your game ever runs, is there anything saved yet? What must happen BEFORE you can load?" |
| Forgot `.close()` after writing | `save.txt` exists but is empty | "Which line actually finishes the job of saving your words to disk?" |
| Used a loaded number without `int()` | `TypeError: can only concatenate str (not "int") to str` | "Is that really a NUMBER to Python, or still just text that looks like one?" |
| Wrote facts without `\n` at the end | all the facts land on ONE line when read back | "How does `.write()` know where one fact ends and the next begins?" |
| Typo'd the filename (`"save.txt"` vs `"saves.txt"`) | wrong-file `FileNotFoundError`, or saves go to a file he never checks | "Does the name in your `open()` for WRITING match the name in your `open()` for READING, letter for letter?" |

## Gate — do not move on until

- He has written to a file and watched it appear in his folder.
- He has read a file back with a `for` loop and printed its contents.
- He has met the `TypeError` from forgetting `int()`, understood why, and fixed it.
- His load code brings back the SAME hero he saved — same name, HP and gold.
- His game saves again after a fight.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 16 finished!** Your hero has a real **save crystal** now — you
> wrote his facts with `open`, `.write()` and `.close()`, and pulled them back with a
> loop and `int()`, and he came back as the EXACT same hero you left. Play, win a
> fight, quit... and load him straight back in — no more starting from zero! Next,
> Chapter 17 makes the whole game **unbreakable**. Stop here or carry on, adventurer!"

Before you treat the chapter as done, ask: *"Why does the game need a FILE to
remember your hero, and not just a variable?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of `python-course/progress.md`.
Don't say you're doing it. Copy this shape, put in today's real date, and carry the
Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 16 — Save Your Adventure
- Completed: wrote save/load with open/.write()/.close() and open/for-loop/.close(); saved the hero's name, HP and gold to save.txt and loaded them back unchanged; wired a new-game/load-game menu; saves again after a fight
- Strong at: writing and reading files; converting loaded text back to numbers with int()
- Struggled with: nothing this time
- How to help next: start Chapter 17 — bullet-proofing the game (validation, try/except)
- Next time: Chapter 17 — Bullet-proof the Game
```

**Then update the `### Facts`** in `progress.md`: `chapters_cleared` +1 (and +1 to
`mini_challenges_done` / `predict_wins` / `break_it_fixes` for any that happened
today) — the script turns these into his new Level, XP and spells.

**Then refresh the skill ledger** (silent, tutor-private — he never sees it). This
chapter introduced `file handling`; move it from `new` toward `learning` or `solid`
— only `solid` if he wrote AND read a file unaided today, `shaky` if the write/read
order or the missing `int()` kept tripping him (see AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and judge his standard. NEVER show or
quote it. His menu wording and battle flavour will differ — that's correct, as long
as he writes, reads, converts with `int()`, and the loaded hero provably matches the
saved one. Plain `open`/`.close()` — no `with`, no `try`/`except` (Chapter 17).

```python
# save_game.py — Chapter 16 reference (tutor only)
# open/write/close, open/read (for loop over lines)/close, f-strings, dictionaries,
# int() to convert loaded text back to numbers. No try/except (Ch17), no with (later).

SAVE_FILE = "save.txt"

def save_hero(hero):
    file = open(SAVE_FILE, "w")           # "w" makes/wipes the file, ready to write
    file.write(f"{hero['name']}\n")
    file.write(f"{hero['hp']}\n")
    file.write(f"{hero['gold']}\n")
    file.close()                          # closing is what actually saves it
    print("\nThe crystal glows -- your progress is saved.")

def load_hero():
    file = open(SAVE_FILE)                # no "w" -> opens for reading
    lines = []
    for line in file:                     # walk the file one line at a time
        lines.append(line)
    file.close()
    name = lines[0].strip()               # .strip() trims the invisible \n
    hp = int(lines[1])                    # int() turns loaded text back into a number
    gold = int(lines[2])
    hero = {"name": name, "hp": hp, "gold": gold}
    print(f"\nThe crystal glows -- welcome back, {hero['name']}!")
    return hero

def show_status(hero):
    print(f"{hero['name']}  --  HP {hero['hp']}, Gold {hero['gold']}")

print("=== THE CRYPT OF BROKEN KEYS ===")
hero = None

while True:
    print("\n1) New adventure\n2) Load saved adventure\n3) Quit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name your hero: ")
        hero = {"name": name, "hp": 30, "gold": 0}
        show_status(hero)
        print("\nA goblin attacks! You win the fight.")
        hero["hp"] = hero["hp"] - 4       # the fight changes the hero...
        hero["gold"] = hero["gold"] + 15
        show_status(hero)
        save_hero(hero)                   # ...and THAT is exactly what we save

    elif choice == "2":
        hero = load_hero()
        show_status(hero)

    elif choice == "3":
        print("\nFarewell, adventurer.")
        break

    else:
        print("Choose 1, 2 or 3.")
```
