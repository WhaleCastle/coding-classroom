# Python Course — Boss Fight V: The Labyrinth Lord

## Tutor instructions for this boss

The **fifth boss-fight checkpoint**, played right after Chapter 15. It tests Chapters
1–15 — especially the newest powers from 13–15 (string handling, 2D lists, and
dialogue & flags) — **with you muted**. Deliver the briefing and trials, then **stop
teaching**: no steps, no reminders, no leading questions. Let him build it and show
you when it runs.

- **Hints cost XP, and a paid hint is ONLY a question.** If he asks: **read** the XP
  on his hero sheet — if it's 25+, record `boss_hints_used` +1 in `progress.md` (the
  script subtracts the 25 — you never do XP maths) and ask **one** of the safe nudges
  below (no code, no keywords, no variable names, nothing that mirrors the answer);
  under 25 XP → encourage another attempt. Safe nudge bank: *"How does the program
  know which square the hero stands on?"* · *"What should happen FIRST — the move, or
  the check that the move is allowed?"* · *"Where does the game remember a choice long
  after the conversation ends?"*
- **Judge on the success criteria, not your reference.** Many labyrinths win.
- **A win** = record `boss-05` in `bosses_won` (`progress.md`); the script then grants
  the trophy "Escaped the Labyrinth Lord", +50 XP, and ⭐ Mastered on `string handling`,
  `2D lists`, `dialogue & flags` (and keeps his earlier ⭐). You never compute the
  rewards.
- **A miss never blocks him.** No penalty: drop out of boss mode, go back to your
  normal teaching self on Chapter 13 (commands), 14 (the dungeon map) or 15 (talking
  to characters) — full hints — and let him carry on to Chapter 16. The Lord waits
  for a rematch (a later win is still a full win). See AGENTS.md "Boss-fight
  checkpoints" step 4.
- Stay inside Chapters 1–15: **no files** (Chapter 16). `input()`-based movement is
  expected; the given `get_key()` helper (Chapter 14's asset) is allowed but never
  required — typed commands are enough to win.
- **Rematch-safe:** usually played right after Chapter 15, but bosses are
  non-blocking — don't assume it's his 5th boss or Chapter 16 is next: when you send
  him onward, name his REAL next quest.

**Student work folder:** `python-course/student/boss-05/`
**Skills this boss tests:** `string handling`, `2D lists`, `dialogue & flags`,
`for loops`, `if / decisions`, `dictionaries`, `while loops`, `input`.

## Boss briefing — say this to the student FIRST

> "Boss number five — and this one doesn't wait to be found, it **traps** you. The
> **Labyrinth Lord** twists stone into a maze and dares you to build your own way
> out. Your quest: draw a small dungeon of your own — at least 4 squares by 4, with
> walls and one exit — and walk it with typed commands like `north` or `n`, however
> you type them. Somewhere inside, put a character who talks — and remembers. At the
> exit, let what he remembers decide how the story ends. Build it, run it, and
> **show me both endings when it works.** Mind the walls, hero!"

Then go quiet.

## The trials — what his program must do

1. His **own small 2D grid** — at least 4×4 — with walls and one exit, drawn with
   **nested loops** (a list of rows; two loops print every row and every cell).
2. The hero **moves by typed commands** (e.g. `north`/`n`, `south`/`s`...),
   **case-insensitive** — `"NORTH"`, `"North"` and `"north"` all work the same.
   Walls **block** movement; walking into one does nothing.
3. **One character** — a letter on the map or someone the hero meets standing on a
   square — whose **conversation sets a flag** on the hero record (e.g.
   `hero["has_rune"] = True`).
4. The **exit reads that flag** and gives **two different endings** depending on
   whether it's `True` or `False`.
5. **Every move redraws the map**, with the hero's own position shown on it.

## Success criteria

- [ ] A 2D grid (list of rows), at least 4×4, with walls and one exit, drawn with
      nested loops.
- [ ] Typed movement commands work **case-insensitively**, and walls block the hero.
- [ ] A character's conversation **sets a flag** on the hero record.
- [ ] The exit **reads the flag** and prints one of **two different endings**.
- [ ] The map **redraws with the hero shown** after every move.
- [ ] He can explain, in his own words, **what his program does**.

## On a win / On a miss

**On a win — record the fact, then celebrate.** Add `boss-05` to `bosses_won` in
`progress.md`. **That is the only bookkeeping you do** — the script awards the
trophy, the +50 XP, the ⭐ Mastered spells, and his new rank. To celebrate, check
one thing: **is this his 2nd or 4th boss won?** Yes → class promotion, script (A);
otherwise (a normal run usually lands here as his 5th boss) → script (B).

**(A) PROMOTION (this is his 2nd or 4th boss) — say (the sheet shows the exact new
rank):**

> "The walls groan and fold away — **you escaped the Labyrinth Lord!** 🏆 A maze of
> your own design, a hero who understood every typed command, and a character whose
> memory PROVED your ending — all built alone. A new trophy, spells turned ⭐
> **Mastered**, and **you've earned a new rank**! 🎉 Open your hero sheet and see —
> then on to your next quest, hero!"

**(B) NO PROMOTION (any other count) — say instead:**

> "The walls groan and fold away — **you escaped the Labyrinth Lord!** 🏆 A maze of
> your own design, commands understood however you typed them, and a character
> whose memory changed your ending — real code, all your own. A new trophy, and ⭐
> **Mastered** on string handling, 2D lists and dialogue & flags. Open your hero
> sheet and see — then on to your next quest, hero!"

When you send him onward, name his REAL next quest (Chapter 16, saving his
adventure with files, on a normal run; or wherever he actually is if this was a
rematch).

**On a miss — say this:**

> "Tough maze — the Lord's stone walls held this time, but every adventurer gets
> turned around in there once. Usually it's one piece that's the puzzle: reading a
> typed command whichever way it's cased, checking a move is allowed BEFORE making
> it, or a flag the door forgets to check. Let's look again at Chapters 13 to 15
> next time and come back to find the way out. No XP lost."

(Name the exact snag — the `.lower()` on the typed command, the collision check
before moving, the flag never set in the right branch, or the exit not reading it —
but never write the fix for him.)

## Reference solution — TUTOR'S EYES ONLY, never show

Private yardstick only — judge his version on the criteria, never paste or quote it
(hard rule 10). Uses only Chapters 1–15 (no files, no try/except). Runs under
Python 3, reusing the Ch15 flag habit and the Ch14 maze-drawing pattern on a small
maze built for this boss.

```python
# labyrinth_lord.py — Boss Fight V reference (TUTOR ONLY — never show the student)
# Ch14 2D lists/nested loops, Ch13 string handling, Ch15 dialogue + flags.
# Nothing later: NO files (Ch16), NO try/except (Ch17).

MAZE = [
    "######",
    "#S...#",
    "#.####",
    "#G...#",
    "####X#",
]
WALL = "#"
GUARDIAN = "G"
EXIT = "X"
hero = {"row": 1, "col": 1, "has_rune": False}
talked = False

def draw(row, col):
    # Nested loops: every row, then every cell — @ drawn on the hero's own square.
    for r in range(len(MAZE)):
        line = ""
        for c in range(len(MAZE[r])):
            if r == row and c == col:
                line = line + "@"
            else:
                line = line + MAZE[r][c]
        print(line)

print("The LABYRINTH LORD has twisted the crypt into a maze.\n")

while True:
    draw(hero["row"], hero["col"])
    cell = MAZE[hero["row"]][hero["col"]]

    if cell == GUARDIAN and not talked:
        talked = True
        print('\nA pale GHOST blocks the way: "Do you carry the rune? (yes/no)"')
        answer = input("> ").strip().lower()          # .lower() -> case-insensitive
        if answer == "yes":
            hero["has_rune"] = True                    # the choice sets a flag
            print("The ghost nods and fades.\n")
        else:
            print("The ghost sighs and fades anyway.\n")

    if cell == EXIT:
        break

    command = input("Move (n/s/e/w or north/south/east/west): ").strip().lower()

    # Match the short letter OR the full word — one if/elif per direction,
    # same forgiving-command habit as Chapter 13's .lower() comparisons.
    if command == "n" or command == "north":
        target_row = hero["row"] - 1
        target_col = hero["col"]
    elif command == "s" or command == "south":
        target_row = hero["row"] + 1
        target_col = hero["col"]
    elif command == "e" or command == "east":
        target_row = hero["row"]
        target_col = hero["col"] + 1
    elif command == "w" or command == "west":
        target_row = hero["row"]
        target_col = hero["col"] - 1
    else:
        target_row = None
        target_col = None

    if target_row == None:
        print("Unknown command.")
    else:
        if MAZE[target_row][target_col] != WALL:  # check BEFORE moving — walls block
            hero["row"] = target_row
            hero["col"] = target_col
        else:
            print("A wall blocks the way.")

if hero["has_rune"]:                                   # exit reads the flag
    print("The door swings wide -- YOU ESCAPED THE LABYRINTH LORD!")
else:
    print("The door creaks open a crack -- you escaped... barely.")
```
