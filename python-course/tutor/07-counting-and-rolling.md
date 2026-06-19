# Chapter 7 — Counting & Rolling

## Tutor instructions for this chapter

Last chapter's `while` loop repeats *until* something happens. Today's `for` loop
repeats a **known number of times** — perfect for drawing things and counting.
Teach one step per message and wait for his result. Do not write his code.

**Important — no randomness yet.** The course doesn't teach `random` until Chapter
12, so this chapter does NOT roll real dice. Here "rolling" means *counting* with a
loop (drawing an HP bar, adding up numbers). If he asks for true random dice, tell
him it's coming in Chapter 12 and keep him counting for now.

**Student work folder:** `python-course/student/chapter-07/`

**Skills this chapter leans on:** `variables`, `f-strings`, `numbers & arithmetic`.

## Learning objectives (max 3)

1. Use a `for` loop with `range()` to repeat a set number of times.
2. Use the loop variable (the number that changes each time round).
3. Recognise a simple nested loop (a loop inside a loop) for grids.

## Concepts — explain in this voice

- **for loop:** "A `while` loop says 'keep going UNTIL…'. A `for` loop says 'do
  this exactly N times'. It's the tool for 'draw ten hearts' or 'take three steps'
  — when you know the count up front."
- **range():** "`range(5)` is Python's way of saying 'the numbers 0, 1, 2, 3, 4' —
  five of them. `for i in range(5):` runs its block once for each, so five times.
  `range(1, 7)` counts 1, 2, 3, 4, 5, 6 — handy for the faces of a die."
- **The loop variable:** "The little name after `for` (often `i`) holds a DIFFERENT
  number each time round — first 0, then 1, then 2… You can use it, or just ignore
  it if you only care about repeating."
- **Nested loop:** "A loop can live inside another loop. The inside one runs all
  the way through every single time the outside one goes round once — like rows and
  columns of a grid: for each ROW, draw every COLUMN."

## Chapter opener — say this to the student FIRST

Say something like: *"Last time your loop fought until the goblin dropped. Today
you get the other kind of loop — one that repeats a set number of times, perfect
for **drawing**. By the end you'll have a proper **HP bar** for your RPG —
`♥ ♥ ♥ . .` — drawn by a loop, plus a neat way to count things up. We'll meet the
`for` loop and `range()`, use the changing number, and even peek at loops inside
loops to make a little grid. Ready? Let's draw some hearts."* Keep it warm, then
start Step 1.

## Guided steps

**Step 1 — Repeat N times.** New file `hp_bar.py`. Teach `for` with `range()`. Have
him write `for i in range(3):` with an indented `print("step")`. Predict how many
lines, then run.
Success: "step" prints exactly three times; he connects `range(3)` to three times.

**Step 2 — Watch the number change.** Have him change the body to `print(i)` and
run. Ask: what numbers, and why does it start at 0?
Success: he sees `0 1 2` and knows the loop variable changes each time.

**Step 3 — Draw an HP bar.** Teach building a string in a loop. Have him set
`hp = 7`, start `bar = ""`, then `for i in range(hp): bar = bar + "♥"`, and print
the bar. (He can pick his own symbol.)
Success: a row of his chosen symbol, one per HP, prints.

**Step 4 — Add the empty slots.** Have him add a second loop for the missing HP:
`for i in range(max_hp - hp): bar = bar + "."` (with `max_hp` he chooses). Print
`HP {hp}/{max_hp} [{bar}]`.
Success: a full bar like `HP 7/10 [♥♥♥♥♥♥♥...]` prints.

**Step 5 — Count with the loop variable.** Teach `range(1, 7)`. Have him add up the
faces of a die by COUNTING (not random): `total = 0`, then
`for face in range(1, 7): total = total + face`, then print the total. (It's 21.)
Make clear this is counting, and real random dice come later.
Success: it prints 21 and he can say what the loop added up.

**Step 6 — A tiny grid (nested loop).** Show a loop inside a loop. Have him print a
small patrol grid: `for row in range(3):` and inside it build a line with
`for col in range(3): line = line + "+ "`, then print the line.
Success: a 3×3 grid of symbols prints; he sees the inner loop runs fully each outer
turn.

## Mini-challenge — The HP / Stamina Bar

In `hp_bar.py`, the student builds a **stat bar** for his RPG using only this
chapter and earlier ones. It must:
- use a `for` loop with `range()` to repeat,
- draw a bar whose length depends on a number (HP, stamina, XP — his choice),
- use the loop variable OR a counting total somewhere,
- print the result clearly with an f-string.

He designs the look himself (symbols, what the bar measures). Hints only, never the
code. (No `random` — that's Chapter 12.)

## Success criteria (check before finishing the chapter)

- [ ] A `for` loop with `range()` repeats the right number of times.
- [ ] A bar (or count) is built whose size depends on a number.
- [ ] The loop variable or a running total is used.
- [ ] He can explain in his own words how `for` differs from `while`.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Expected `range(3)` to include 3 / start at 1 | off-by-one bar | "How many numbers does `range(3)` give, and what's the first one?" |
| Missing colon after `for` | `SyntaxError` | "Like `if` and `while`, the `for` line ends with one little mark. Is it there?" |
| Body not indented | `IndentationError` | "Which lines belong inside the loop? How do we show that to Python?" |
| Reset `bar = ""` inside the loop | bar never grows | "Where should the empty bar start — before the loop, or every time round?" |
| Asks for real random dice | (none) | "Great idea — real dice need `random`, and that's Chapter 12! For now we count. Want to make the bar fancier instead?" |

## Gate — do not move on until

- He has written a `for` loop with `range()` that repeats the right number of times.
- He has used the loop variable or a running total.
- His stat bar runs and its length depends on a number.
- He can explain when to reach for `for` vs `while`.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 7 finished!** Your game can draw and count with `for` loops
> now — you built an HP bar that grows with your hit points, and even a little
> grid with a loop inside a loop. Run it and try different HP values to watch the
> bar change… and when you're ready, Chapter 8 gives your hero a **backpack** — a
> list of items he can pick up and drop. Stop here or carry on!"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — when would you use a `for` loop instead of a `while` loop?"*
and wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put in
today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 7 — Counting & Rolling
- Completed: drew an HP bar with a for loop and range(), counted a total, made a small nested-loop grid
- Strong at: for loops and range(); building a string in a loop
- Struggled with: nothing this time
- How to help next: start Chapter 8 — lists (the backpack)
- Next time: Chapter 8 — The Inventory
```

**Then refresh the skill ledger** (the same silent save, tutor-private — he never
sees it). This chapter introduced `for loops`; in the `### Skill ledger` at the top of
`progress.md`, move it from `new` toward `learning` or `solid` — only `solid` if he
wrote the `for`/`range()` loop unaided today, `shaky` if counting or the nested loop
tripped him (see AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and to judge his standard. NEVER
show or quote it. His symbols and flavour will differ — that's correct, as long as
a `for` loop with `range()` builds something whose size depends on a number. No
`random` — that's Chapter 12.

```python
# hp_bar.py — Chapter 7 reference (tutor only)
# Skills used: for, range(), the loop variable, a simple nested loop. Nothing later.
# (No random yet — that's Chapter 12. Here we COUNT, we don't roll dice.)

hp = 7
max_hp = 10

# Draw the bar: one heart per HP, then a dot for each empty slot.
bar = ""
for i in range(hp):
    bar = bar + "♥"
for i in range(max_hp - hp):
    bar = bar + "."
print(f"HP {hp}/{max_hp}  [{bar}]")

# Count up the six faces of a die with the loop variable (1..6 add to 21).
total = 0
for face in range(1, 7):
    total = total + face
print(f"The six faces of a die add up to {total}.")

# A loop inside a loop draws a 3x3 patrol grid.
print("Patrol grid:")
for row in range(3):
    line = ""
    for col in range(3):
        line = line + "+ "
    print(line)
```
