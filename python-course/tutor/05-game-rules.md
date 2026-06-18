# Chapter 5 — Game Rules (True/False)

## Tutor instructions for this chapter

Today the game learns to answer **yes/no questions** for itself — the foundation
of every game rule ("is the hero alive?", "can he open the door?"). The new value
type is the **Boolean**: only ever `True` or `False`. Teach one step per message
and wait for his result. Do not write his code.

He already met comparisons inside `if` (Chapter 3). The new idea here is that a
comparison like `hp > 0` **is a value on its own** — `True` or `False` — that he
can store in a variable and combine with `and` / `or` / `not`.

**Student work folder:** `python-course/student/chapter-05/`

## Learning objectives (max 3)

1. Know the Boolean type: a value that is only ever `True` or `False`.
2. Make Booleans with comparisons (`>`, `<`, `==`, `!=`, `>=`, `<=`).
3. Combine them with `and`, `or`, `not` to write game rules.

## Concepts — explain in this voice

- **Boolean:** "Some questions have only two answers: yes or no, on or off. Python
  has a special value for exactly that — `True` or `False` (capital first letter,
  no quotes). It's called a *Boolean*. Every rule in your game is really a Boolean:
  is the hero alive? `True` or `False`."
- **Comparisons make Booleans:** "When you write `hp > 0`, Python doesn't just use
  it in an `if` — it actually works out a `True` or `False` and hands it back. So
  you can save it: `is_alive = hp > 0`. Now `is_alive` holds the answer."
- **and / or / not:** "You join rules with three little words. `and` = BOTH must be
  true (`has_key and is_alive`). `or` = AT LEAST ONE is true (`has_sword or
  has_wand`). `not` = flip it (`not is_alive` is True when he's dead)."

## Chapter opener — say this to the student FIRST

Say something like: *"Your game can count now. Today it learns to **decide things
for itself** — the rules every game runs on: is the hero alive? does he have the
key AND the courage to go on? By the end you'll have a little **rule book** for
your RPG that answers these with a clean `True` or `False`. We'll meet Python's
yes/no value, make rules out of comparisons, then join them with `and`, `or` and
`not`. Ready? Let's write the laws of your world."* Keep it warm, then start
Step 1.

## Guided steps

**Step 1 — Meet True and False.** New file `rules.py`. Have him `print(10 > 3)`
and `print(2 > 5)`. Predict first, then run. Teach: Python answered each question
with `True` or `False` — a brand new kind of value.
Success: he sees `True` and `False` printed and knows they're Python's yes/no.

**Step 2 — Store a rule in a box.** Teach that the answer can be saved. Have him
write `hp = 8` then `is_alive = hp > 0` then `print(is_alive)`. Ask: what's inside
`is_alive`?
Success: `is_alive` prints `True`; he can explain it's holding the answer to
`hp > 0`.

**Step 3 — Both must be true (`and`).** Teach `and`. Have him make two rules of his
own (e.g. `has_key = True`, `is_alive = ...`) and a combined one
`can_open_door = has_key and is_alive`. Print it.
Success: `can_open_door` is `True` only when both parts are true.

**Step 4 — Flip it (`not`) and choose (`or`).** Teach `not` and `or` briefly. Ask
him to print `not is_alive` and an `or` rule of his own (e.g. `can_fight =
has_sword or has_wand`).
Success: he can predict the result of a `not` and an `or` before running.

**Step 5 — Predict-then-run.** Give him three expressions to predict BEFORE
running, e.g. `True and False`, `True or False`, `not (5 > 2)`. He writes his
guesses, then runs to check.
Success: he correctly predicts at least two of the three.

**Step 6 — Feed a rule into an `if`.** Tie it back to Chapter 3. Have him use one
of his Booleans in an `if`/`elif`/`else` to print a game message ("You stride on,
strong and ready." / "Careful — HP is low!" / "Game over.").
Success: changing the HP value changes which message prints.

## Mini-challenge — The Rule Book

In `rules.py`, the student builds a small **rule book** for his RPG using only
this chapter and earlier ones. It must:
- read or set at least two facts (e.g. `hp`, and whether he has the key),
- make at least two Booleans from comparisons (e.g. `is_alive`, `in_danger`),
- combine rules with `and`, `or`, or `not` at least once,
- use one of the Booleans inside an `if`/`elif`/`else` to print a game outcome.

He designs the rules himself. Hints only, never the code.

## Success criteria (check before finishing the chapter)

- [ ] The program makes Booleans from comparisons and prints `True`/`False`.
- [ ] It combines rules with `and`, `or`, or `not`.
- [ ] A Boolean drives an `if`/`elif`/`else` that prints a sensible outcome.
- [ ] He can explain in his own words the difference between `and` and `or`.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Used `=` instead of `==` to compare | `SyntaxError` or wrong result | "One equals sign PUTS a value in a box; how many do we use to ASK if two things are equal?" |
| Quoted it: `"True"` | rule always behaves 'true' | "`True` is a special value, not text. Does it need quotes? What colour does the editor show it in?" |
| lower-case `true` | `NameError: name 'true' is not defined` | "Python is fussy about the capital letter. How is `True` spelled?" |
| Thought `and` means 'either' | rule never true | "`and` needs BOTH sides true. Which word do we use for 'at least one'?" |
| Compared text to number by mistake | always `False`, no error | "Is `hp` a number or text right now? (Did it come from `input()`?)" |

## Gate — do not move on until

- He has stored a comparison's result in a variable and printed it.
- He has used `and`, `or`, and `not` at least once each across the chapter.
- He correctly predicted the result of at least one combined expression.
- His rule book runs and a Boolean drives an `if` outcome.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 5 finished!** Your game can think in rules now — true or
> false, just like a real game engine deciding what you're allowed to do. You
> made your own rules with comparisons and joined them with `and`, `or` and
> `not`. Run your rule book and try changing the HP or the key to watch the
> answers flip… and when you're ready, Chapter 6 is the big one — your first
> **loop**, a real turn-by-turn goblin fight. Stop here or charge on!"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — what's the difference between `and` and `or`?"* and wait for
his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put in
today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 5 — Game Rules (True/False)
- Completed: built a rule book — Booleans from comparisons, combined with and/or/not, driving an if
- Strong at: making rules from comparisons; predicting and/or results
- Struggled with: nothing this time
- How to help next: start Chapter 6 — the battle loop (while)
- Next time: Chapter 6 — The Battle Loop
```

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and to judge his standard. NEVER
show or quote it. His rules and flavour will differ — that's correct, as long as
it builds Booleans, combines them, and drives an `if`.

```python
# rules.py — Chapter 5 reference (tutor only)
# Skills used: booleans, comparisons, and/or/not, int(), if/elif/else. Nothing later.

hp = int(input("Hero HP? "))
has_key = input("Do you have the key? (yes/no) ").strip().lower() == "yes"

# A comparison IS a True/False value we can store.
is_alive = hp > 0
in_danger = is_alive and hp < 10          # alive AND low
can_open_door = has_key and is_alive      # need the key AND to be alive

print(f"Alive?         {is_alive}")
print(f"In danger?     {in_danger}")
print(f"Open the door? {can_open_door}")

# Feed a rule into a decision (Chapter 3).
if not is_alive:
    print("Game over, hero.")
elif in_danger:
    print("Careful — your HP is low!")
else:
    print("You stride on, strong and ready.")
```
