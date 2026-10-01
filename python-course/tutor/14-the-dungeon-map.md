# Python Course — Chapter 14: The Dungeon Map

## Tutor instructions for this chapter

Budget **2–3 sessions**, not one — this is the biggest thing he's built yet.
From here on you explain less and ask more; let him plan small pieces before
he types them. Teach one step per message, wait for his result, never write
his code.

Ceiling: Chapters 1–13, plus **2D lists and nested loops**. No files (Chapter
16), no `try`/`except` (Chapter 17) — a wall bump is handled with a plain
`if`, not error-handling.

**Two GIVEN ASSETS, not code he writes**, from `python-course/tutor/assets/`:
`maze_layout.py` (`MAZE`, symbol names, `find_start()`) and `controls.py`
(`get_key()`, one keypress, no ENTER). Before Step 3 have him **copy both
files** into `python-course/student/chapter-14/` so `from maze_layout import
MAZE` finds them. Given, not authored — exactly like `hero_ascii.txt` in
Chapter 9. `controls.py` especially: one-line import, same shape as `import
random`; he never opens it. That low-level keyboard code is genuinely beyond
KS3–4 — that's why it's a gift, not a lesson.

**Student work folder:** `python-course/student/chapter-14/`

**Skills this chapter leans on:** `lists`, `for loops`, `while loops`,
`if / decisions`, `input`, `functions`.

## Learning objectives (max 3)

1. Read a cell of a 2D list with two indexes, `grid[row][col]`.
2. Use a nested loop (rows, then columns) to draw a whole grid, and check a
   target cell BEFORE moving into it.
3. Import a given helper file in one line, without reading its insides.

## Concepts — explain in this voice

- **2D list (a grid of boxes):** "A normal list is a row of boxes. A **2D
  list** is a list where each box holds ANOTHER list — a grid, like a chess
  board. You reach one square with TWO numbers: which row, then which column
  — `grid[row][col]`. Row first, always, like 'go down, then go across.'"
- **Nested loop:** "To visit every square of a grid you need a loop inside a
  loop. The OUTER loop walks down the rows; for EACH row, the INNER loop
  walks across every column in it. Outer says 'next row'; inner says 'next
  square.' Together they touch every square exactly once."
- **Coordinates:** "Your hero lives at ONE pair of numbers now, `(row, col)`
  — exactly which square he's standing on. Move him by changing that pair."
- **Collision check (look before you leap):** "Before you move the hero, work
  out where he'd LAND and ask the map 'is that a wall?' Only move if the
  answer is no — check first, move second, or he'll walk through stone."

## Chapter opener — say this to the student FIRST

Say something like: *"So far your dungeon only existed in your head — today
we put him INSIDE it, walking around for real, walls that actually stop him.
This isn't just a maze trick — any time data is shaped like a GRID (a
spreadsheet, a chess board, a seating plan) you'll reach for exactly this
pattern: a 2D list and a loop inside a loop. First a tiny grid you design,
then the real dungeon (I'll hand you the map), then your hero walking it
with walls that block him, and finally real single-key controls, no ENTER.
This one takes a few sessions — that's normal. Ready? Let's step into the
crypt."* Keep it warm, then start Step 1.

## Guided steps

**Step 1 — A grid of your own.** New file (e.g. `dungeon_map.py`) in `student/chapter-14/`. Have him type a tiny 3×3 grid where each row is itself a list, e.g. `grid = [[".", ".", "#"], [".", "@", "."], [".", ".", "."]]`. Ask him to PREDICT `grid[0][2]` and `grid[1][1]` before printing them.
Success: both predictions check out; he states "row first, then column."

**Step 2 — Draw it with a nested loop.** Have him write an outer `for row in range(len(grid)):` and, inside it, build one line of text with an inner `for col in range(len(grid[row])):`, printing the line once the inner loop ends.
Success: the 3×3 grid prints as three rows, built entirely by the loop.

**Step 3 — Bring in the real dungeon.** Explain the GIVEN asset. Have him copy `maze_layout.py` and `controls.py` into his folder, then add `from maze_layout import MAZE, WALL, EXIT, find_start`. Point out: this maze writes each ROW as one STRING, not a list of characters — but `MAZE[row][col]` still reaches one character the same way. Reuse his Step 2 loop to print `MAZE`.
Success: the real dungeon prints, drawn by the same nested-loop pattern.

**Step 4 — Find the hero, draw the hero.** Have him call `hero_row, hero_col = find_start(MAZE)` and change the drawing loop: for each `(row, col)`, print `"@"` if it matches the hero's position, else whatever `MAZE[row][col]` already has.
Success: `@` shows at the correct square; the underlying `MAZE` never changes.

**Step 5 — Move, but check first (collision).** Have him read a direction with `input()` (w/a/s/d), work out the TARGET row/col, and only update the hero's real position if `MAZE[target_row][target_col]` is not `WALL`. Ask him to PREDICT what happens walking straight at a wall before trying it.
Success: floor moves the `@`; a `#` does nothing — position stays put. That "nothing happens" IS the win.

**Step 6 — Wipe and redraw.** Have him write his OWN function: `def clear_screen(): print("\n" * 50)`, and call it right before drawing on every loop, so each move wipes the old picture first.
Success: each move shows ONE clean maze, not a scrolling tower of old ones.

**Step 7 — Real controls: swap in `get_key()`.** Have him add `from controls import get_key` and replace `input()` with `key = get_key()` — no prompt text needed, it just waits for one keypress. He never opens `controls.py`, same as he's never opened `random`'s insides.
Success: w/a/s/d move the hero instantly, no ENTER key needed.

## Mini-challenge — The Walkable Crypt

Using only this chapter and earlier ones, the student assembles the full
**walkable dungeon**. It must:
- import the GIVEN `MAZE` (and `find_start`) from his copied `maze_layout.py`,
- draw the whole grid every turn with a nested loop, showing `@` at the
  hero's real position,
- move the hero with `get_key()` (imported from `controls.py`) in w/a/s/d,
- check the TARGET square before moving — walls always block him,
- clear the screen before every redraw,
- print a victory line and end the moment the hero reaches `X`.

He may keep the dungeon shape as given or (see the side quest) redesign it.
Hints only, never the code.

## Side quest (optional) — Cartographer

Offer this only when he's ahead of pace — it costs nothing to skip. Pitch:
"Fancy making the dungeon truly YOURS? Redraw the map." Requirements:
- edit the `MAZE` rows in his OWN copied `maze_layout.py`,
- keep every row the SAME length and the outer ring solid `#`,
- make sure the walk from `@` to `X` is still actually possible.

## Success criteria (check before finishing the chapter)

- [ ] A 2D list/grid is read correctly with `grid[row][col]`.
- [ ] A nested loop draws the whole maze, not hand-written `print`s.
- [ ] The hero's `(row, col)` is tracked and drawn as `@` at the right square.
- [ ] Moving into a wall is blocked by a check made BEFORE the move happens.
- [ ] His own `clear_screen()` wipes the screen before each redraw.
- [ ] `get_key()` (from the copied `controls.py`) drives real w/a/s/d
      movement with no ENTER.
- [ ] Reaching `X` prints a victory line and ends the program.
- [ ] He can explain why the game checks a move BEFORE making it, not after.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Forgot to copy the asset files into his folder | `ModuleNotFoundError: No module named 'maze_layout'` | "Where does Python look for a file you `import`? Is a copy of `maze_layout.py` actually sitting next to your program?" |
| Swapped row and column | hero appears in the wrong place, or moves sideways when he meant up/down | "Which index did you change for w/a/s/d — the first one or the second? Which one is row, which is column?" |
| No collision check before moving | the hero walks straight through `#` walls | "Before you update the hero's position, did you ask the map what's AT the new square first?" |
| Walked off the printed grid | `IndexError: list index out of range` | "Does every row of your maze have a solid wall all the way round? What if the target square isn't inside the grid at all?" |
| Didn't call `clear_screen()` each loop | old mazes pile up, scrolling the screen | "How many times does your drawing code run before you clear anything? Before or after you draw?" |

## Gate — do not move on until

- He has read a 2D cell with `[row][col]` and predicted it correctly once.
- He has written a nested loop that draws a whole grid.
- He has copied both given asset files and imported from them without
  opening `controls.py`'s insides.
- He has a working collision check — walking into a wall visibly does
  nothing.
- His finished program clears the screen each move and reaches `X` with a
  working `get_key()`.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 14 finished!** — and it was a big one. You built a real
> **2D dungeon**, drew it with a nested loop, and walked your own hero
> through it with instant w/a/s/d controls, walls that actually stop him. Go
> walk your whole crypt right now, wall to `X` — you EARNED that. Since
> you've just built your first real walkable dungeon, if you'd like a
> two-minute peek at where the whole game is heading I can also show you the
> demo trailer — totally optional. When you're ready, Chapter 15 teaches
> your dungeon to TALK back: an NPC with choices that change what happens
> later. Stop here or carry on, adventurer!"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — why does the game check a move BEFORE it happens,
instead of moving the hero and checking afterwards?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put
in today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 14 — The Dungeon Map
- Completed: built the walkable dungeon — 2D grid, nested-loop drawing, hero position, wall collision, clear_screen, real w/a/s/d controls via get_key
- Strong at: reading grid[row][col]; nested loops; the look-before-you-move collision check
- Struggled with: nothing this time
- How to help next: start Chapter 15 — nested if, dialogue dictionaries, story flags
- Next time: Chapter 15 — Talking to Characters
```

**Then update the `### Facts`** in `progress.md`: `chapters_cleared` +1 (and
+1 to `mini_challenges_done` if he did it; `predict_wins` / `break_it_fixes` were already counted
the moment each happened) — the script turns these into his new Level, XP and spells.

**Then refresh the skill ledger** (the same silent save, tutor-private — he
never sees it). This chapter introduced `2D lists`; move it from `new`
toward `learning` or `solid` — only `solid` if he built the drawing loop and
collision check largely unaided, `shaky` if row/col mix-ups kept tripping
him up (see AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and judge his standard. NEVER
show or quote it. Uses ONLY concepts taught this chapter or earlier: 2D
lists, nested loops, `if`, a `while` loop, a function (Chapter 10), `input`.
No files (Chapter 16), no `try`/`except` (Chapter 17).

The STUDENT's real version imports the GIVEN maze and controls instead
(`from maze_layout import ...` and `from controls import get_key`). This
reference defines its own small copy of the maze INLINE and reads moves with
plain `input()` instead, so it runs and checks cleanly with no asset files or
keyboard attached — same shape, same rules, only where the data comes from
differs (see the comment at the `input()` line).

```python
# dungeon_map.py — Chapter 14 reference (tutor only)
# Skills used: 2D lists, nested for loops, coordinates, if, while, a function.
# Nothing later: no files (Ch16), no try/except (Ch17).

# A copy of the given dungeon shape (normally imported from maze_layout.py).
MAZE = [
    "##########",
    "#@..#...E#",
    "#.#.#.##.#",
    "#.#...#N.#",
    "#.####.#.#",
    "#....D..X#",
    "##########",
]

WALL = "#"
EXIT = "X"

def find_start(maze):
    # Scan every row, then every column in it, looking for the '@'.
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "@":
                return [row, col]
    return [1, 1]  # fallback — should never be needed on a well-formed map

def clear_screen():
    # The KS3-friendly "wipe": push old text off the top with blank lines.
    print("\n" * 50)

def draw(maze, hero_row, hero_col):
    # Nested loop: OUTER walks the rows, INNER walks the columns of that row.
    for row in range(len(maze)):
        line = ""
        for col in range(len(maze[row])):
            if row == hero_row and col == hero_col:
                line = line + "@"          # draw the hero over whatever's there
            else:
                line = line + maze[row][col]
        print(line)


hero_start = find_start(MAZE)
hero_row = hero_start[0]
hero_col = hero_start[1]

while True:
    clear_screen()
    draw(MAZE, hero_row, hero_col)

    if MAZE[hero_row][hero_col] == EXIT:
        print("You step into the light — you found the way out!")
        break

    # The student's version replaces this line with: key = get_key()
    key = input("Move (w/a/s/d): ").strip().lower()

    # Work out the TARGET row/col from the key — one if/elif per direction.
    if key == "w":
        target_row = hero_row - 1
        target_col = hero_col
    elif key == "s":
        target_row = hero_row + 1
        target_col = hero_col
    elif key == "a":
        target_row = hero_row
        target_col = hero_col - 1
    elif key == "d":
        target_row = hero_row
        target_col = hero_col + 1
    else:
        # Not a move key — target stays right where the hero already is.
        target_row = hero_row
        target_col = hero_col

    # Look before you leap: check the TARGET cell BEFORE moving into it.
    if MAZE[target_row][target_col] != WALL:
        hero_row = target_row
        hero_col = target_col
```
