# Python Course — Chapter 11: Functions that Answer

## Tutor instructions for this chapter

Chapter 10 taught functions that DO things — print, or change the hero record —
but they never handed anything back. Today they learn to ANSWER: `return` lets a
function hand back a value the rest of the program can catch, print, or test in an
`if`. Teach one step per message and wait for his result. Do not write his code.

Keep working in the SAME file as Chapter 10, `actions.py`, so he sees the old
`attack()` grow a returning helper inside it. **No `random` yet** (Chapter 12):
`roll_damage()` still returns a fixed number — only the SHAPE of the answer
changes. **No string methods yet** (Chapter 13).

The trickiest idea is **local vs global**: a name born inside a function only
exists inside that function's own walls. Reuse the labelled-box metaphor — a
local variable is a box on a workbench inside a closed room; once the function
finishes, the room is cleared out, and reaching for that box from outside gets you nothing.

**Student work folder:** `python-course/student/chapter-11/`

**Skills this chapter leans on:** `functions`, `if / decisions`, `while loops`,
`booleans & logic`, `dictionaries`, `f-strings`.

## Learning objectives (max 3)

1. Write a function that `return`s a value, and use that value (store it, print
   it, test it in an `if`).
2. Explain the difference between a function that returns and one that only
   prints, including what `None` means.
3. Explain why a name created INSIDE a function can't be read from outside it.

## Concepts — explain in this voice

- **return:** "Every function in Chapter 10 DID something and stayed quiet.
  `return` teaches a spell to ANSWER — the moment Python hits `return`, it hands
  that value back to wherever the function was called, like a shopkeeper handing
  you your change. Anything after `return` never runs; the spell is finished the
  second it answers. Catch the answer in a box — `damage = roll_damage(hero)` —
  or it's thrown away the instant it's returned."
- **None — 'nothing to report':** "Ask a function that never uses `return` for
  its answer and Python hands back a special value called `None` — it just means
  'this spell didn't answer anything.' Not an error; Python's polite way of
  saying there's no value here."
- **Local vs global:** "A name you create INSIDE a function only lives inside
  that function's own walls — the moment the function finishes, that name is
  gone. Try to read it from OUTSIDE and Python has never heard of it."

## Chapter opener — say this to the student FIRST

Say something like: *"Chapter 10 taught your hero to act — but every function
just DOES something and goes quiet. Today they learn to TALK BACK: instead of
only printing, they hand you a number or a True/False, so you can catch it,
check it, or use it to decide what happens next. This isn't just for combat —
any time you need to ask 'how much damage', 'is he still alive', a function
that returns is how you get the answer out, and you'll use this shape for the
rest of your coding life. We'll start tiny: one function that hands back a
number, then break it on purpose to see what 'no answer' looks like. Then we
build `roll_damage()` and `is_alive()` and rebuild the whole battle on them.
Ready? Let's teach your functions to talk back."* Keep it warm, then Step 1.

## Guided steps

**Step 1 — A function that returns.** In `actions.py`, away from the battle
code, have him write `def double(n):` with an indented `return n * 2`. Ask him
to PREDICT what `print(double(4))` will show, then run it.
Success: it prints `8`; the returned value flows straight into `print()`.

**Step 2 — Catch it, then break it (meet `None`).** Store the answer first:
`result = double(5)` then `print(result)` — `10`. Now break it on purpose: a
second function that only PRINTS, never returns —
`def shout(message): print(f"{message}!")` — then `answer = shout("Charge")`
followed by `print(answer)`. Ask him to PREDICT the second `print` before running.
Success: `"Charge!"` prints once, then `None` prints alone; he can say why —
`shout` never used `return`.

**Step 3 — `roll_damage(attacker)` returns a number.** Have him write
`def roll_damage(attacker):` with a local `weapon_bonus = 3` and
`return attacker["attack"] + weapon_bonus`, then call it on the Chapter 10 hero:
`dmg = roll_damage(hero)`, and print `dmg`.
Success: `dmg` holds a sensible number; a function calculates something and
hands back the RESULT, not just prints it.

**Step 4 — `is_alive(fighter)` returns True/False.** Have him write
`def is_alive(fighter):` with `return fighter["hp"] > 0`, then test it directly
in an `if`: `if is_alive(goblin): print("Still standing!")` — no variable
needed, the answer is used right inside the `if`'s question.
Success: the `if` reacts correctly to the goblin's HP; a returned `True`/`False`
drives a decision directly.

**Step 5 — Break it on purpose (local vs global).** Have him try, OUTSIDE any
function, to `print(weapon_bonus)`. He'll get
`NameError: name 'weapon_bonus' is not defined`. Ask: "That name worked FINE
inside `roll_damage`. Why does Python say it doesn't exist out here?"
Success: he connects the error to local-vs-global — the name was born inside
the function and died with it.

**Step 6 — Rebuild the battle on functions that answer.** Have him change
`attack(attacker, defender)` so damage comes from `roll_damage(attacker)`
instead of reading `attacker["attack"]` directly, and change the `while` loop
condition to `while is_alive(hero) and is_alive(goblin):`, replacing any direct
HP checks with calls to `is_alive()`.
Success: the battle looks the same to play, but two returning functions now
drive the damage AND the loop's stop condition.

## Mini-challenge — The Battle, Rebuilt

In `actions.py`, the student rewrites his Chapter 10 battle so it runs entirely
on **functions that answer**, using only this chapter and earlier ones. It must:
- define at least TWO functions that use `return` (e.g. `roll_damage`, `is_alive`),
- STORE or directly USE at least one returned value (not just call and discard it),
- have the `while` loop condition call a function that returns True/False,
  rather than checking HP directly,
- still end with a clear win/lose message.

He designs the numbers and flavour himself. Hints only, never the code. (Still
no `random` — that's Chapter 12.)

## Side quest (optional) — The Power Strike

Offer this only when he's ahead of pace — it costs nothing to skip. Pitch it in
tutor voice: *"Fancy a finishing move? Give your hero a Power Strike — one big
hit, at a cost."*
- Write `power_strike(attacker)` that `return`s DOUBLE what `roll_damage(attacker)` gives.
- Using it also costs the attacker 2 HP (change `attacker["hp"]` inside the
  function) — a big hit isn't free.
- Call it at least once from inside the battle and see the trade-off play out.

## Success criteria (check before finishing the chapter)

- [ ] A function is written with `return` and its answer is used (stored,
      printed, or tested).
- [ ] He can say what `None` means and when a function produces it.
- [ ] `roll_damage(attacker)` returns a number built from the hero's stats.
- [ ] `is_alive(fighter)` returns True/False and drives the battle's `while`
      loop or an `if` directly.
- [ ] He can explain in his own words why a name made INSIDE a function can't be
      read from outside it.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Printed a function that only prints, expecting the return value | `None` | "Did that function have a `return` line, or did it only `print`? What does Python hand back when there's no `return`?" |
| Wrote code AFTER the `return` line expecting it to run | that code never runs | "What does `return` do the instant Python reaches it? Can anything in the function run after that?" |
| Tried to read a local name outside its function | `NameError: name '...' is not defined` | "That name worked fine INSIDE the function. Where was it actually born — and does it survive once the function finishes?" |
| Called a returning function but forgot to store the answer | the value seems to vanish; a later line using it fails | "You called the function — but did you catch what it handed back anywhere? Where did the answer go?" |

## Gate — do not move on until

- He has written a function with `return` and used its returned value.
- He has seen a function's answer be `None` and met the local-name `NameError`.
- `roll_damage()` and `is_alive()` both work and drive the battle's loop.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 11 finished!** Your functions can TALK now — `roll_damage`
> hands back a number and `is_alive` hands back True or False, and your whole
> battle runs on those answers instead of raw HP checks. You even met `None` and
> tamed a local `NameError`. Run your rebuilt battle — same game, tidier code
> underneath. Next time: Chapter 12, Random Encounters — real dice enter the
> game, and no two fights will ever roll the same again. Stop here or carry on,
> adventurer!"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — what's the difference between a function that RETURNS a
value and one that just PRINTS it?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put in
today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 11 — Functions that Answer
- Completed: rebuilt the battle on returning functions — roll_damage() and is_alive() — used in the while loop condition
- Strong at: catching and using a returned value; spotting None on a function with no return
- Struggled with: nothing this time
- How to help next: start Chapter 12 — random dice rolls and a random monster
- Next time: Chapter 12 — Random Encounters
```

**Then update the `### Facts`** in `progress.md`: `chapters_cleared` +1 (and +1
to `mini_challenges_done` / `predict_wins` / `break_it_fixes` for any that
happened today) — the script turns these into his new Level, XP and spells.

**Then refresh the skill ledger** (tutor-private — he never sees it). This
chapter introduced `return values`; move it from `new` toward `learning` or
`solid` — only `solid` if he wrote and used a returning function unaided today,
`shaky` if `None` or the local/global `NameError` kept tripping him (see
AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and judge his standard. NEVER show
or quote it. His numbers and flavour will differ — that's correct, as long as at
least two functions return a value and one drives the battle's loop condition.
It reuses the record shape (`name`, `cls`, `hp`, `max_hp`, `attack`) and
rebuilds the Chapter 10 battle. Still no `random` — that's Chapter 12.

```python
# actions.py — Chapter 11 reference (tutor only)
# Skills used: def, parameters, return, local vs global, dictionaries, if, while,
# f-strings, arithmetic. Nothing later: NO random (Chapter 12), NO string methods
# (Chapter 13).

# --- functions that DO things (Chapter 10) ---
def show_status(hero):
    print(f"{hero['name']} the {hero['cls']}  —  HP {hero['hp']}/{hero['max_hp']}")

def heal(hero, amount):
    hero["hp"] = hero["hp"] + amount
    if hero["hp"] > hero["max_hp"]:
        hero["hp"] = hero["max_hp"]
    print(f"{hero['name']} is healed for {amount}.")

# --- functions that ANSWER (new this chapter) ---
def roll_damage(attacker):
    # weapon_bonus is LOCAL: born here, gone once this function ends. Reading
    # it from outside this function raises NameError.
    weapon_bonus = 3
    return attacker["attack"] + weapon_bonus

def is_alive(fighter):
    # Hands back True or False — the caller decides what to DO with the answer.
    return fighter["hp"] > 0

def attack(attacker, defender):
    # attack() now CALLS a returning function for its number, instead of
    # reading attacker["attack"] itself — one function using another's answer.
    damage = roll_damage(attacker)
    defender["hp"] = defender["hp"] - damage
    print(f"{attacker['name']} hits {defender['name']} for {damage}!")

# --- two records to act on ---
hero = {"name": "Aldric", "cls": "warrior", "hp": 30, "max_hp": 30, "attack": 7}
goblin = {"name": "Goblin", "cls": "monster", "hp": 12, "max_hp": 12, "attack": 4}

show_status(hero)
print("\nA goblin blocks your path!")

# The loop condition calls is_alive() on both fighters instead of checking
# hero["hp"] > 0 directly — the ANSWER drives the loop.
while is_alive(hero) and is_alive(goblin):
    attack(hero, goblin)
    if not is_alive(goblin):
        break
    attack(goblin, hero)

if is_alive(hero):
    print(f"\n{hero['name']} wins with {hero['hp']} HP to spare!")
else:
    print(f"\n{hero['name']} has fallen...")
```
