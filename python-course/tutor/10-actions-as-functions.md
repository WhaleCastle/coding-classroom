# Python Course — Chapter 10: Actions as Functions

## Tutor instructions for this chapter

The hero has a character sheet now (Chapter 9) — today he learns to DO things.
A **function** is an action written once and used by name: `attack()`, `heal()`,
`show_status()`. Teach one step per message and wait for his result. Do not write
his code.

Lean hard on Chapter 9: these functions act on the **hero record** (a dictionary
passed in as a parameter). Because the hero is one dictionary — a single box — a
function that changes `hero["hp"]` changes the REAL hero, not a copy; use the
labelled-box metaphor to make that feel natural rather than magic.

**No `return` yet.** These functions DO things (print, or change the record) but
don't hand a value back — that's Chapter 11. If he asks how to "get an answer out",
tell him it's the very next chapter. **No `random` yet** either (Chapter 12), so
attack damage comes from the hero's stored `attack` stat, not a dice roll.

**Student work folder:** `python-course/student/chapter-10/`

**Skills this chapter leans on:** `dictionaries`, `variables`, `f-strings`,
`numbers & arithmetic`, `if / decisions`, `while loops`.

## Learning objectives (max 3)

1. Write a function with `def` and run it by calling its name.
2. Give a function inputs (parameters) so it works on any hero or enemy.
3. Say why functions beat copy-pasting the same lines.

## Concepts — explain in this voice

- **Function (def):** "A function is a recipe card you write ONCE. `def
  show_status():` names a block of steps, just like writing out a recipe — but
  writing the card doesn't cook the meal. Write it once, and it just sits there,
  ready whenever you need it."
- **Calling:** "A function only runs when you CALL it — that's the moment you
  actually cook the recipe, by writing its name with brackets: `show_status()`.
  Define it above; call it below."
- **Parameters (ingredients):** "The words in the brackets are the function's
  ingredients. `def heal(hero, amount):` says 'hand me a hero and an amount, and
  I'll do the healing.' Whatever you pass in the brackets when you call it —
  `heal(hero, 10)` — becomes those names inside the function."
- **Why functions:** "Without them you'd copy the same five attack lines every time
  anyone swings. With a function you write it once and just call `attack(hero,
  goblin)` — shorter to read, and if you ever improve the attack you fix it in ONE
  place instead of ten."

## Chapter opener — say this to the student FIRST

Say something like: *"Your hero has a full character sheet now — but he just sits
there. Today we teach him to ACT. We'll bottle up his moves into **functions**:
`show_status()` to show his sheet, `heal()` to patch him up, `attack()` to strike an
enemy. Write the move once, then call it by name whenever you need it. And functions
aren't just for combat — every time you catch yourself about to copy the same lines
again, that's a function waiting to be born; you'll use them for the rest of your
coding life. By the end your battle will be just a few tidy calls instead of a wall
of repeated code. We'll write our first function, give it ingredients, then make
`heal` and `attack` really change the hero. Ready? Let's teach him to fight."*
Keep it warm, then start Step 1.

## Guided steps

**Step 1 — Your first function.** New file `actions.py`. Teach `def`. Have him write
`def greet():` with an indented `print("A hero steps forward.")`, then — on its own
line, not indented — call it with `greet()`. Ask him to PREDICT: does the message
appear once, twice, or not at all? Then run.
Success: the line prints exactly once; he sees that DEFINING did nothing until the
CALL ran it.

**Step 2 — Define before you call.** Have him move the call `greet()` ABOVE the
`def greet():`, run, and read the error (`NameError: name 'greet' is not defined`).
Ask why Python can't call a recipe it hasn't read yet. Move it back below.
Success: he understands a function must be defined before it's called; it runs again.

**Step 3 — Give it an ingredient (a parameter).** Teach parameters. Have him change
it to `def greet(name):` printing `f"{name} steps forward."`, then call it twice with
different names: `greet("Aldric")` and `greet("Mira")`. 
Success: the SAME function prints two different lines; he sees the parameter fill in.

**Step 4 — show_status(hero).** Bring in the Chapter 9 record. Have him make a small
`hero` dictionary (name, cls, hp, max_hp, attack), then write
`def show_status(hero):` that prints a tidy sheet from it, and call `show_status(hero)`.
Success: the function prints the hero's sheet; he sees a whole record passed as one
ingredient.

**Step 5 — heal(hero, amount) that really changes him.** Teach a function that
changes the record. Have him write `def heal(hero, amount):` with
`hero["hp"] = hero["hp"] + amount` and a printed line. Ask him to PREDICT the HP
after `heal(hero, 8)`, then call it and `show_status(hero)` to check. Point out: the
hero is ONE box, so the function changed the real hero. Add an `if` so HP never goes
past `max_hp` (reuse Chapters 3/5).
Success: the hero's HP actually rises (capped at max); he sees a parameter change the
record for real.

**Step 6 — attack(attacker, defender).** Have him write `def attack(attacker,
defender):` that does `defender["hp"] = defender["hp"] - attacker["attack"]` and
prints the blow. Make a second record — `goblin = {"name": "Goblin", "cls": "monster", "hp": 12,
"max_hp": 12, "attack": 4}` — and call `attack(hero, goblin)`, then `attack(goblin, hero)`. Two
records, one function, either can be attacker or defender.
Success: each call lowers the right fighter's HP; he sees one function serve both
sides.

**Step 7 — Break it on purpose (a missing ingredient).** Have him call `heal(hero)`
with the amount left out and run. He'll see
`TypeError: heal() missing 1 required positional argument: 'amount'`. Ask: "What
ingredients did the recipe ask for? What did you forget to pass?" Then have him call
it correctly.
Success: he saw the `TypeError`, understands every parameter needs an argument, and
fixed it.

## Mini-challenge — The Combat Helpers

In `actions.py`, the student builds a set of **combat helpers** for his RPG using
only this chapter and earlier ones. It must:
- define at least TWO functions, one of which takes a parameter,
- include `show_status(hero)` that prints the hero's sheet,
- include one function that CHANGES the hero record through a parameter (a `heal`, a
  `drink_potion`, a `level_up`…),
- be CALLED to make something happen — the same helper used more than once — so the
  code is shorter than copying the lines out each time.

He designs the moves and flavour himself. Hints only, never the code. (No `return`
— that's Chapter 11. No `random` — that's Chapter 12.)

## Success criteria (check before finishing the chapter)

- [ ] A function is defined with `def` and made to run by calling it.
- [ ] A function takes a parameter and is called with different arguments.
- [ ] A function changes the hero record through a parameter (e.g. `heal`).
- [ ] The same helper is called more than once, replacing copy-pasted lines.
- [ ] He can explain in his own words the difference between DEFINING and CALLING a
      function.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Defined it but never called it | nothing happens | "Writing the recipe doesn't cook it. What line actually RUNS the function?" |
| Called it above the `def` | `NameError: name 'attack' is not defined` | "Has Python read the recipe yet by the time you ask for it? Which comes first?" |
| Missing colon after `def` line | `SyntaxError` | "Like `if`, `while` and `for`, the `def` line ends with one little mark. Is it there?" |
| Body not indented | `IndentationError` | "Which lines belong INSIDE the function? How do we show Python that?" |
| Left out an argument | `TypeError: ... missing 1 required positional argument` | "What ingredients did the brackets ask for? Did you hand it every one?" |
| Expected `heal` to change HP but it didn't | HP unchanged | "Did you put the new HP back INTO the record, or just work it out and throw it away?" |
| Passed a fact instead of the hero (`heal(hero["hp"], 8)`) | HP unchanged, no error | "Did you hand the recipe the whole hero, or just one fact copied out of him?" |

## Gate — do not move on until

- He has defined a function and run it by calling it.
- He has written a function with a parameter and called it with different arguments.
- He has a function that changes the hero record through a parameter.
- He has met (and fixed) a `NameError` (order) or `TypeError` (missing argument).
- His combat helpers run and are actually called.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 10 finished!** Your hero can DO things now — you wrote real
> functions like `show_status`, `heal` and `attack`, and called them by name to make
> your game happen. Look how much shorter your code is than copying it out every
> time! Run your helpers and heal your hero back up… and when you're ready, Chapter
> 11 teaches functions to give an ANSWER back with `return` — so `roll_damage()` can
> hand you a number and you can rebuild the whole battle out of tidy calls. Stop here
> or carry on, adventurer!"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — what's the difference between DEFINING a function and CALLING
it?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put in
today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 10 — Actions as Functions
- Completed: wrote functions with def + parameters — show_status, heal, attack — and called them to run the game
- Strong at: defining and calling functions; passing the hero record as a parameter
- Struggled with: nothing this time
- How to help next: start Chapter 11 — return values (functions that answer)
- Next time: Chapter 11 — Functions that Answer
```

**Then update the `### Facts`** in `progress.md`: `chapters_cleared` +1 (and +1 to `mini_challenges_done` if he did it; `predict_wins` / `break_it_fixes` were already counted the moment each happened) — the script turns these into his new Level, XP and spells.

**Then refresh the skill ledger** (the same silent save, tutor-private — he never
sees it). This chapter introduced `functions`; in the `### Skill ledger` at the top
of `progress.md`, move it from `new` toward `learning` or `solid` — only `solid` if
he wrote and called a function with a parameter unaided today, `shaky` if the
define-vs-call order or missing arguments kept tripping him (see AGENTS.md "The skill
ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and to judge his standard. NEVER show
or quote it. His moves and flavour will differ — that's correct, as long as he
defines and calls functions, one takes a parameter, and one changes the hero record.
It reuses the running game's record shape (`name`, `hp`, `max_hp`, `attack`) so it's
the next slice of the same RPG. No `return`, no `random` — those are Chapters 11 and
12.

```python
# actions.py — Chapter 10 reference (tutor only)
# Skills used: def, parameters, calling, dictionaries, if, arithmetic, a while loop.
# Nothing later: NO return (functions here just DO), NO random (damage = the attack stat).

# --- the actions, each written once ---

def show_status(hero):
    # Reads the record and prints a small sheet. Takes the whole hero as one ingredient.
    print(f"{hero['name']} the {hero['cls']}  —  HP {hero['hp']}/{hero['max_hp']}")


def heal(hero, amount):
    # Changes the record through the parameter. Because 'hero' is one dictionary box,
    # this heals the REAL hero. The if stops HP going over the maximum.
    hero["hp"] = hero["hp"] + amount
    if hero["hp"] > hero["max_hp"]:
        hero["hp"] = hero["max_hp"]
    print(f"{hero['name']} is healed for {amount}.")


def attack(attacker, defender):
    # One function serves both fighters — either can be attacker or defender.
    damage = attacker["attack"]
    defender["hp"] = defender["hp"] - damage
    print(f"{attacker['name']} hits {defender['name']} for {damage}!")


# --- two records to act on ---
hero = {"name": "Aldric", "cls": "warrior", "hp": 30, "max_hp": 30, "attack": 7}
goblin = {"name": "Goblin", "cls": "monster", "hp": 12, "max_hp": 12, "attack": 4}

# --- use the helpers: a tiny battle, all through calls ---
show_status(hero)
heal(hero, 8)          # capped at max_hp, so HP stays 30
show_status(hero)

print("\nA goblin attacks!")
while hero["hp"] > 0 and goblin["hp"] > 0:
    attack(hero, goblin)          # same function...
    if goblin["hp"] <= 0:
        break
    attack(goblin, hero)          # ...used for the other side

if hero["hp"] > 0:
    print(f"\n{hero['name']} wins with {hero['hp']} HP to spare!")
else:
    print(f"\n{hero['name']} has fallen...")
```
