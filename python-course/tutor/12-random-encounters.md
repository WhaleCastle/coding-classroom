# Python Course — Chapter 12: Random Encounters

## Tutor instructions for this chapter

Real dice enter the game today. Every fight so far has been exactly the same
every time it runs — today `random` breaks that: damage varies, and the enemy
itself is chosen from a roster. Teach one step per message and wait for his
result. Do not write his code.

Keep working in `actions.py`, the same file from Chapters 10–11 — `roll_damage()`
upgrades from a fixed number to a randomised one, and a fixed goblin becomes a
random pick from a monster roster. **No string methods yet** (Chapter 13), **no
2D lists** (Chapter 14). This chapter is followed by **Boss IV — The
Shapeshifter**, so make sure `import random`, `randint` and `choice` all feel
solid before you finish — see "End of chapter" for the hand-off.

**Student work folder:** `python-course/student/chapter-12/`

**Skills this chapter leans on:** `functions`, `return values`, `dictionaries`,
`lists`, `while loops`, `f-strings`.

## Learning objectives (max 3)

1. Use `random.randint(a, b)` to get a random whole number, inclusive of both ends.
2. Use `random.choice(a_list)` to pick one random item from a list.
3. Rebuild `roll_damage()` and the enemy pick so no two battles play out the same.

## Concepts — explain in this voice

- **import:** "Python doesn't hand you every tool by default — some live in
  toolboxes you have to open first. `import random` at the very top of the file
  unlocks a toolbox of randomness you didn't have before. Without it, Python has
  never heard the word `random`."
- **random.randint(a, b):** "Rolls a dice with however many faces you choose.
  `random.randint(1, 6)` rolls a six-sided die — BOTH 1 and 6 can come up, and
  everything in between, all with a fair chance. Roll it twice, expect two
  different answers."
- **random.choice(a_list):** "Reaches into a list and pulls out ONE item at
  random, like drawing a card from a shuffled deck. Every item gets a fair
  chance — works on a list of names just as well as a list of whole records."
- **Randomness inside a returning function:** "`roll_damage()` still `return`s
  one number, same as Chapter 11 — but now it comes from `random.randint`
  instead of a fixed sum, so calling it twice in a row can give two different
  answers. The SHAPE hasn't changed; only where the number comes from."

## Chapter opener — say this to the student FIRST

Say something like: *"Every fight you've built so far plays out exactly the
same way, every single time. Today that changes forever: real dice enter your
game. We'll bring in Python's `random` toolbox, roll actual dice for damage, and
let a random monster step out of the dark instead of always the same goblin.
And `random` isn't just for battles — any time a real game needs unpredictability,
a shuffled deck, a coin flip, a lucky drop, this is the toolbox you reach for.
We'll start small: one dice roll, run it a few times, then upgrade
`roll_damage()` to roll for real and let `random.choice()` pick your next
enemy. Ready? Let's roll the dice."* Keep it warm, then start Step 1.

## Guided steps

**Step 1 — First roll.** At the very top of `actions.py`, have him add
`import random`. Then, away from the battle code: `roll = random.randint(1, 6)`
then `print(roll)`. Run it several times. Ask him to PREDICT first: could it
ever show `0`? Could it ever show `7`?
Success: he sees different numbers across runs, all between 1 and 6 inclusive,
and can say why 0 and 7 are impossible.

**Step 2 — A d20 with flavour.** Have him roll a twenty-sided die and print it
with an f-string: `d20 = random.randint(1, 20)` then
`print(f"You rolled a {d20} on the d20!")`. Run it a few times.
Success: a fresh number and message print each run.

**Step 3 — Upgrade `roll_damage()`.** Have him rewrite `roll_damage(attacker)`
from Chapter 11 so the number comes from a range built off the attack stat:
`low = attacker["attack"] - 2`, `high = attacker["attack"] + 2`, then
`return random.randint(low, high)`. Have him PREDICT whether two calls in a
row will match, then call it 3–4 times and print each result.
Success: the results vary but stay near the hero's attack stat; he sees the
SAME function now hand back a different answer each time.

**Step 4 — `random.choice()` picks a monster.** First the simple case: a list
`monster_names = ["Goblin", "Skeleton", "Giant Rat", "Cave Troll"]`, then
`print(random.choice(monster_names))` a few times. Then the real thing — a
roster of monster DICTIONARIES reusing the record shape:
`monsters = [{"name": "Goblin", "hp": 12, "attack": 4}, ...]` (3–4 entries).
Have him write `enemy = random.choice(monsters)` and print
`f"A {enemy['name']} steps out of the dark!"`.
Success: different monster names appear across runs, picked from a list of
whole records, not just names.

**Step 5 — Break it on purpose (swapped bounds).** Have him PREDICT, then run,
`random.randint(5, 1)`. He'll get
`ValueError: empty range in randrange(5, 2)`. Ask: "Which number has to come
first — the small one or the big one? What do you think Python is complaining
about?"
Success: he sees the `ValueError` and can explain that the low bound must come
before the high bound.

**Step 6 — Wire it into the battle.** Have him replace the fixed `goblin`
record with `enemy = random.choice(monsters)` at the start of the fight, and
make sure `attack()` (from Chapter 11) is still calling the now-random
`roll_damage()`. Run the whole battle several times.
Success: each run picks a different enemy and rolls different damage, but the
battle still plays fair to a clean win/lose message every time.

## Mini-challenge — The Wandering Monsters

In `actions.py`, the student builds a battle where **every run is different**,
using only this chapter and earlier ones. It must:
- pick the enemy with `random.choice()` from a roster of at least THREE monster
  dictionaries,
- have `roll_damage()` return a randomised number via `random.randint()`, built
  from a stat,
- run the fight loop (from Chapter 11's `is_alive()`) all the way to a clear
  win/lose message.

He designs the roster and flavour himself. Hints only, never the code.

## Side quest (optional) — The Critical Hit

Offer this only when he's ahead of pace — it costs nothing to skip. Pitch it in
tutor voice: *"Fancy a lucky strike? Give your hero a chance at a critical hit."*
- Roll a separate `random.randint(1, 20)` alongside the normal damage roll.
- If it lands on `20`, DOUBLE the damage from `roll_damage()` and print a
  special "CRITICAL HIT!" message before applying it.

## Success criteria (check before finishing the chapter)

- [ ] `import random` is used and `random.randint(a, b)` produces a number
      including both ends.
- [ ] `roll_damage()` returns a randomised number built from a stat.
- [ ] `random.choice()` picks one random monster from a list of records.
- [ ] He met and can explain the `ValueError` from swapped `randint` bounds.
- [ ] The battle runs to a win/lose message with a random enemy and random
      damage.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Forgot `import random` | `NameError: name 'random' is not defined` | "Where does Python keep tools it doesn't load by default? What line unlocks the dice-rolling toolbox?" |
| Swapped the bounds, e.g. `random.randint(5, 1)` | `ValueError: empty range in randrange(5, 2)` | "Which number should come first in `randint` — the small one or the big one? Which order did you write them in?" |
| Called `random.choice()` on an empty list | `IndexError: Cannot choose from an empty sequence` | "Can you draw a card from an empty deck? What does your list need before you choose from it?" |
| Wrote `random.randint` without the brackets and arguments | a strange value like `<bound method ...>` instead of a number | "Did you actually CALL the dice roll, or just point at the tool itself? What's missing after `randint`?" |

## Gate — do not move on until

- `random.randint(a, b)` works and he can say both ends are possible.
- `roll_damage()` returns a randomised number built from a stat.
- `random.choice()` picks a random monster from a list of dictionaries.
- He has met the swapped-bounds `ValueError`.
- The battle runs to a win/lose message with a random enemy and random damage.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 12 finished!** Real dice are rolling now — `roll_damage()`
> hands back a different number every time, and `random.choice()` sends a
> different monster out of the dark on every run. No two fights will ever play
> out the same again. Run your battle a few more times and watch it change.
> Now a real test blocks the way: **Boss IV, the Shapeshifter** — a creature
> that never wears the same face twice, and you must out-build it entirely on
> your own, no steps from me. Face it now, or stop here and take it on next
> session?"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — what does `random.randint(a, b)` promise about the
numbers it can give you?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put in
today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 12 — Random Encounters
- Completed: brought random into the game — randint()-based damage and choice()-based monster picks, wired into the battle
- Strong at: predicting the range of a randint roll; reading the swapped-bounds ValueError
- Struggled with: nothing this time
- How to help next: run Boss IV — The Shapeshifter (Chapters 1–12 checkpoint, tutor muted)
- Next time: Boss IV — The Shapeshifter (then Chapter 13)
```

**Then update the `### Facts`** in `progress.md`: `chapters_cleared` +1 (and +1 to `mini_challenges_done` if he did it; `predict_wins` / `break_it_fixes` were already counted the moment each happened) — the script turns these into his new Level, XP and spells.

**Then refresh the skill ledger** (tutor-private — he never sees it). This
chapter introduced `random`; move it from `new` toward `learning` or `solid` —
only `solid` if he wrote a working `randint`/`choice` call unaided today,
`shaky` if the swapped-bounds error or the missing `import` kept tripping him
(see AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and judge his standard. NEVER show
or quote it. His roster and flavour will differ — that's correct, as long as
`roll_damage()` uses `randint` and the enemy is picked with `choice()` from a
list of records. It reuses the record shape (`name`, `hp`, `attack`) and
rebuilds the Chapter 11 battle. No string methods, no 2D lists yet.

```python
# actions.py — Chapter 12 reference (tutor only)
# Skills used: import, random.randint, random.choice, return, dictionaries,
# lists, while, f-strings. Nothing later: NO string methods (Ch13), NO 2D lists
# (Ch14).

import random

# --- functions that DO things (Chapter 10) ---
def show_status(hero):
    print(f"{hero['name']} the {hero['cls']}  —  HP {hero['hp']}/{hero['max_hp']}")

# --- functions that ANSWER (Chapter 11), now RANDOM (Chapter 12) ---
def roll_damage(attacker):
    # The range is built from the attacker's own stat, so a strong fighter
    # still hits harder on average — but never the exact same number twice.
    low = attacker["attack"] - 2
    high = attacker["attack"] + 2
    return random.randint(low, high)

def is_alive(fighter):
    return fighter["hp"] > 0

def attack(attacker, defender):
    damage = roll_damage(attacker)
    defender["hp"] = defender["hp"] - damage
    print(f"{attacker['name']} hits {defender['name']} for {damage}!")

# --- the hero and a roster of monsters (records, same shape) ---
hero = {"name": "Aldric", "cls": "warrior", "hp": 30, "max_hp": 30, "attack": 7}
monsters = [
    {"name": "Goblin", "hp": 12, "attack": 4},
    {"name": "Skeleton", "hp": 15, "attack": 5},
    {"name": "Giant Rat", "hp": 8, "attack": 3},
    {"name": "Cave Troll", "hp": 25, "attack": 8},
]

# random.choice() picks ONE record from the whole roster — a different
# enemy is possible every time this line runs.
enemy = random.choice(monsters)

show_status(hero)
print(f"\nA {enemy['name']} steps out of the dark!")

while is_alive(hero) and is_alive(enemy):
    attack(hero, enemy)
    if not is_alive(enemy):
        break
    attack(enemy, hero)

if is_alive(hero):
    print(f"\n{hero['name']} defeats the {enemy['name']} with {hero['hp']} HP to spare!")
else:
    print(f"\n{hero['name']} has fallen to the {enemy['name']}...")
```
