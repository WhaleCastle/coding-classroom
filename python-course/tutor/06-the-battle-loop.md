# Chapter 6 — The Battle Loop

## Tutor instructions for this chapter

This is a **milestone**. Today the game does something for the first time:
**repeats** — a real turn-by-turn fight that keeps going until someone drops. The
new tool is the `while` loop. Teach one step per message and wait for his result.
Do not write his code.

`while` is powerful and a little dangerous: a loop whose condition never becomes
false runs **forever**. Teach the emergency brake early — `Ctrl+C` stops a running
program (he met this in VS Code Basics) — and deliberately let him meet an
infinite loop ONCE, on purpose, so it never scares him later.

This is a milestone chapter: at the end you may offer the playable trailer
(`tutor/assets/demo_play.py`) as a "here's where we're heading" taste.

**Student work folder:** `python-course/student/chapter-06/`

**Skills this chapter leans on:** `variables`, `f-strings`, `if / decisions`, `comparisons`, `numbers & arithmetic`, `booleans & logic`.

## Learning objectives (max 3)

1. Use a `while` loop to repeat steps until a condition is false.
2. Change a variable inside the loop so the loop eventually ends.
3. Use `break` to leave a loop early, and recognise/stop an infinite loop.

## Concepts — explain in this voice

- **while loop:** "An `if` checks its question once. A `while` checks the SAME
  question over and over, and keeps running its indented block as long as the
  answer is `True`. It's like a referee shouting 'both still standing? then keep
  fighting!' after every blow."
- **Making it end:** "A loop only stops when its question finally becomes `False`.
  So something INSIDE the loop has to change toward that — the goblin's HP must go
  DOWN each turn, or the fight never ends. If nothing changes, the loop runs
  forever."
- **break:** "`break` is the escape hatch. The moment you hit it, Python jumps
  straight out of the loop, no matter what the question says. Handy for 'the
  goblin's dead — stop swinging'."
- **The emergency brake:** "If a program ever runs forever, don't panic — click
  the terminal and press `Ctrl+C`. That's the universal 'stop!' for a running
  program."

## Chapter opener — say this to the student FIRST

Say something like: *"Here's the big one. Until now your game ran each line once,
top to bottom. Today it learns to **repeat** — and that's how every real fight,
every game loop, every 'keep going until…' works. By the end you'll have a proper
**turn-by-turn battle**: your hero and a goblin trading blows until one of them
falls. We'll meet the `while` loop, make the goblin's HP drop each round so the
fight actually ends, and even peek at what happens when a loop forgets to stop.
Ready? Draw your sword."* Keep it warm, then start Step 1.

## Guided steps

**Step 1 — A loop that counts.** New file `battle.py`. Teach `while` with a simple
countdown first, so the shape is clear before combat. Have him write a counter
`n = 3`, then a `while n > 0:` loop that prints `n` and then does `n = n - 1`.
Run it.
Success: it prints 3, 2, 1 and stops.

**Step 2 — Meet the infinite loop (on purpose).** Ask him to DELETE the `n = n - 1`
line and predict what happens, then run. It prints forever. Teach the brake:
click the terminal, press `Ctrl+C`. Say: "The question never became false because
nothing changed. That's the one rule of loops — something inside must move toward
the end." Then have him put the line back.
Success: he saw the runaway loop, stopped it with `Ctrl+C`, and can say why it
happened.

**Step 3 — Set up the fighters.** Now the real thing. Have him make variables:
`hero_hp`, `goblin_hp`, `hero_attack`, `goblin_attack` (his own numbers). Print a
"FIGHT!" line.
Success: sensible starting values are set and printed.

**Step 4 — One exchange of blows.** Inside a `while hero_hp > 0 and goblin_hp > 0:`
loop, have him lower the goblin's HP by `hero_attack`, print the result, then lower
his own HP by `goblin_attack`, print that. (Reuse the `and` rule from Chapter 5.)
Run it.
Success: HP totals fall each turn and the loop ends when someone hits 0 or below.

**Step 5 — Stop swinging a dead goblin (`break`).** Point out a bug: after the
killing blow, the goblin still bites back. Teach `break`. Have him add, right after
the goblin's HP drops, `if goblin_hp <= 0: break`.
Success: once the goblin dies, the hero doesn't take a final bite.

**Step 6 — Who won?** After the loop, have him use an `if`/`else` (Chapter 3) on
`hero_hp` to print "Victory!" or "Game over." Run a few times with different
starting numbers.
Success: the right ending prints for different starting HP values.

## Mini-challenge — The Battle Loop

In `battle.py`, the student builds a **turn-by-turn fight** for his RPG using only
this chapter and earlier ones. It must:
- have a hero and an enemy with starting HP and attack values,
- use a `while` loop that runs until someone's HP reaches 0 or below,
- change HP **inside** the loop so the fight actually ends,
- use `break` somewhere sensible (e.g. stop when the enemy dies),
- print a clear win/lose message after the loop.

He designs the numbers and the flavour himself. Hints only, never the code.

## Success criteria (check before finishing the chapter)

- [ ] A `while` loop repeats turns and **ends on its own** (no infinite loop).
- [ ] HP values change inside the loop and drive the ending.
- [ ] `break` is used somewhere sensible.
- [ ] A correct win/lose message prints after the fight.
- [ ] He can explain in his own words why a loop needs something to change inside.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Forgot to change HP inside | loop runs forever | "What in the loop is moving toward making the question false? Press `Ctrl+C`, then look." |
| Missing colon after `while` | `SyntaxError` | "Every line that starts a block ends with one little mark. Does your `while` line have it?" |
| Body not indented | `IndentationError` | "How does Python know which lines belong to the loop? What did `if` need in Chapter 3?" |
| Used `if` instead of `while` | runs once, not repeatedly | "Does `if` repeat? Which word means 'keep going while…'?" |
| `=` instead of comparison in the condition | `SyntaxError` | "Are you SETTING a value or ASKING a question here? How many equals signs?" |

## Gate — do not move on until

- He has written a `while` loop that ends on its own.
- He has seen an infinite loop and stopped it with `Ctrl+C` himself.
- He has used `break` at least once.
- His battle runs to a correct win/lose message.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 6 finished** — and it's a huge one! Your game can REPEAT now:
> you just built a real turn-by-turn battle that fights all the way to a winner.
> You even tamed an infinite loop with `Ctrl+C`. Run your fight a few more times
> with different HP and watch it play out… and when you're ready, Chapter 7 adds
> the `for` loop — drawing HP bars and counting things neatly. Stop here or fight
> on!"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — why does a `while` loop need something to change inside it?"*
and wait for his answer.

This is a milestone chapter. If he'd enjoy it, you MAY offer the playable trailer
once as a "here's where we're heading" taste: in the terminal, run
`python python-course/tutor/assets/demo_play.py`. He PLAYS it — he is never shown
its code, and is never expected to write code like it.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put in
today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 6 — The Battle Loop
- Completed: built a turn-by-turn while-loop fight that ends on its own, with break and a win/lose message
- Strong at: while loops; saw and stopped an infinite loop with Ctrl+C
- Struggled with: nothing this time
- How to help next: start Chapter 7 — for loops and counting
- Next time: Chapter 7 — Counting & Rolling
```

**Then update the `### Facts`** in `progress.md`: `chapters_cleared` +1 (and +1 to `mini_challenges_done` / `predict_wins` / `break_it_fixes` for any that happened today) — the script turns these into his new Level, XP and spells.

**Then refresh the skill ledger** (the same silent save, tutor-private — he never
sees it). This chapter introduced `while loops`; in the `### Skill ledger` at the top
of `progress.md`, move it from `new` toward `learning` or `solid` — only `solid` if he
built the loop and its stop-condition unaided today, `shaky` if the loop ran forever or
the `break` confused him (see AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and to judge his standard. NEVER
show or quote it. His numbers and flavour will differ — that's correct, as long as
the loop ends on its own, uses `break`, and prints a win/lose result. Note: damage
is FIXED here — random arrives in Chapter 12, so no `random` yet.

```python
# battle.py — Chapter 6 reference (tutor only)
# Skills used: while, a counter, break, arithmetic, and, if/else. Nothing later.

hero_hp = 30
goblin_hp = 20
hero_attack = 7
goblin_attack = 4
turn = 0

print("A goblin blocks your path! FIGHT!")

# Keep fighting while BOTH are still standing (the 'and' rule from Chapter 5).
while hero_hp > 0 and goblin_hp > 0:
    turn = turn + 1
    print(f"\n--- Turn {turn} ---")

    # The hero swings first.
    goblin_hp = goblin_hp - hero_attack
    print(f"You hit the goblin for {hero_attack}. Goblin HP: {goblin_hp}")
    if goblin_hp <= 0:
        break                       # goblin is down — stop before it bites back

    # The goblin bites back.
    hero_hp = hero_hp - goblin_attack
    print(f"The goblin bites for {goblin_attack}. Your HP: {hero_hp}")

# Decide the outcome after the loop.
if hero_hp > 0:
    print("\nThe goblin falls! Victory!")
else:
    print("\nYou have fallen... Game over.")
```
