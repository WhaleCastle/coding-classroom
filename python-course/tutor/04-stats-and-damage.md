# Chapter 4 — Stats & Damage

## Tutor instructions for this chapter

This is the student's first time with **numbers**. Until now everything has been
text (strings). Today the game learns to do MATHS — the engine behind hit points
and damage. Teach the steps in order, one per message, and wait for his result.
Do not write his code.

The big new idea is that **text and numbers are different things to Python**, and
`input()` always hands back text — so to do maths on what someone types, we have
to *convert* it with `int()`. Expect this to be the sticky point; go slow there.

**Student work folder:** `python-course/student/chapter-04/`

## Learning objectives (max 3)

1. Tell the difference between a number (`int`/`float`) and text (a string).
2. Turn typed text into a number with `int()` and do arithmetic with it.
3. Use `+ - * /` plus `//` (whole division) and `%` (remainder).

## Concepts — explain in this voice

- **Numbers vs text:** "Python keeps two kinds of value apart. `7` is a *number*
  it can do maths with. `"7"` with quotes is *text* — just the shape of a seven,
  like a sticker. You can't add stickers together and get 14. So when you type an
  answer, Python hands it to you as text, and we have to turn it into a real
  number first."
- **int():** "`int()` is a converter. You feed it text that looks like a whole
  number and it hands back a real number you can do maths with. `int("7")` gives
  you `7`. Think of it as melting the sticker down into a real coin."
- **Arithmetic:** "Python does maths with `+` add, `-` take away, `*` times (a
  star, not an x), and `/` divide. Two extra ones are handy for games: `//` gives
  the *whole* number of times something fits (how many full hits to kill a
  goblin), and `%` gives what's *left over*."

## Chapter opener — say this to the student FIRST

Say something like: *"Up to now your game could only talk. Today it learns to
**count** — and that's how every game knows your hit points, your damage, your
score. By the end you'll have a little **damage calculator** for your RPG: tell
it your level and it works out your stats, then it works out how hard you hit.
We'll start by seeing how Python tells numbers and text apart, then teach it to
turn typed answers into real numbers, then do battle maths. Ready? Let's give
your hero some muscle."* Keep it warm and short, then start Step 1.

## Guided steps

**Step 1 — Numbers need no quotes.** Open a new file `stats.py` in his chapter
folder. Have him `print(10 + 5)` and run it. Then have him `print("10" + "5")`
and predict first: what will he see? Let him discover `15` vs `105`. Teach: with
quotes it's text, and `+` on text just sticks it together.
Success: he can say why one gave `15` and the other gave `105`.

**Step 2 — Ask for a number (the trap).** Teach `input()` returns text. Have him
write `level = input("Level? ")` then `print(level + 1)` and run it. It will
CRASH. Let him read the error (`TypeError`). Ask: "Python says it can't add a
number to text — what is `level` really holding?"
Success: he sees the crash and can explain that `input()` gave him text.

**Step 3 — Melt it into a number.** Now teach `int()`. Have him change the line to
`level = int(input("Level? "))` and run again. It works. Teach the shape: the
`input(...)` happens first, then `int(...)` wraps around it.
Success: `print(level + 1)` now prints a real number.

**Step 4 — Build the stats.** Teach arithmetic with `*`. Ask him to compute the
hero's stats from the level and print them, e.g. `max_hp = 20 + level * 5` and an
`attack` of his own design. Let HIM choose the formula numbers.
Success: entering a level prints sensible HP and attack values.

**Step 5 — Do battle maths (// and %).** Teach `//` and `%` with a goblin: if a
goblin has 30 HP and he hits for `damage`, `30 // damage` is how many full hits
it takes and `30 % damage` is the leftover. Ask him to print both.
Success: the numbers make sense (e.g. damage 7 → 4 full hits, 2 left over).

**Step 6 — Break it on purpose.** Ask him to type a word like `five` when the
program asks for a number, and run. He'll see `ValueError: invalid literal for
int()`. Say: "`int()` can only melt down text that's *shaped* like a number —
`'five'` isn't. Errors like this are Python being careful, not mean." Then run it
again with a real number.
Success: he saw the `ValueError`, understands why, and recovered.

## Mini-challenge — The Damage Calculator

In `stats.py` (or a fresh `damage.py`), the student builds a small **damage
calculator** for his RPG using only this chapter and earlier ones. It must:
- ask for at least one number with `int(input(...))`,
- work out a result with arithmetic (e.g. `damage = attack + weapon_bonus - armour`),
- use `//` or `%` somewhere meaningful (e.g. "that's N full hits"),
- print the results in a clear, game-flavoured sentence with an f-string.

He designs the formulas himself. You give hints, never the code.

## Success criteria (check before finishing the chapter)

- [ ] The program reads at least one number with `int(input(...))` and runs with
      no error on valid input.
- [ ] It computes and prints a damage or stats result with arithmetic.
- [ ] It uses `//` or `%` in a way that makes sense for the game.
- [ ] He can explain in his own words why `input()` needs `int()` before maths.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Forgot `int()` on input | `TypeError: can ... only ... str (not "int")` | "What kind of value does `input()` always give back? What do we do to it before maths?" |
| Typed a word for a number | `ValueError: invalid literal for int()` | "`int()` can only melt down text shaped like a number. What did you type?" |
| Used `x` instead of `*` | `SyntaxError` / `NameError` | "How does Python spell 'times'? It's not the letter x." |
| Divided by zero | `ZeroDivisionError` | "What happens in real life if you share something between zero people? Python feels the same way." |
| Mismatched brackets in `int(input())` | `SyntaxError` | "Count your opening and closing brackets — does every `(` have its partner?" |

## Gate — do not move on until

- He has read a number with `int(input(...))` and used it in real arithmetic.
- He has used `//` or `%` at least once and can say what each does.
- He hit (and recovered from) at least one `TypeError` or `ValueError` himself.
- His damage calculator runs and prints a sensible result.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 4 finished!** Your game can do MATHS now — it works out
> stats and damage just like a real RPG engine. You taught Python the difference
> between text and numbers, fixed that `int()` trap yourself, and built your own
> damage formula. Run your calculator one more time and try a few different
> levels… and when you're ready, Chapter 5 is where your game learns to ask
> true-or-false questions — 'is the hero still alive?'. Stop here or keep going!"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — why does `input()` need `int()` before we can do maths?"*
and wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put in
today's real date, and carry the Environment line forward from the last session:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 4 — Stats & Damage
- Completed: built a damage calculator — reads numbers with int(input()), works out stats and damage, uses // and %
- Strong at: arithmetic; understood why input() needs int()
- Struggled with: nothing this time
- How to help next: start Chapter 5 — true/false game rules
- Next time: Chapter 5 — Game Rules (True/False)
```

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and to judge whether his calculator
is up to standard. NEVER show or quote it. His formulas and flavour will differ —
that's correct, as long as it reads a number, does arithmetic, uses `//` or `%`,
and runs.

```python
# stats.py — Chapter 4 reference (tutor only)
# Skills used: numbers (int/float), int(), arithmetic + - * / // %. Nothing later.

print("=== HERO STATS ===")
# input() hands back TEXT; int() melts it into a real number we can do maths with.
level = int(input("Hero level (1-10)? "))

# Stats are just arithmetic on the level.
max_hp = 20 + level * 5          # base 20, +5 per level
attack = 3 + level * 2           # base 3, +2 per level
print(f"HP: {max_hp}   Attack: {attack}")

print("\n=== DAMAGE ===")
weapon_bonus = int(input("Weapon bonus? "))
enemy_armour = int(input("Enemy armour? "))
damage = attack + weapon_bonus - enemy_armour
print(f"You hit for {damage} damage!")

# // gives the WHOLE number of hits; % gives what's LEFT OVER.
goblin_hp = 30
hits = goblin_hp // damage
leftover = goblin_hp % damage
print(f"That's {hits} full hits on a {goblin_hp} HP goblin, with {leftover} HP left over.")
```
