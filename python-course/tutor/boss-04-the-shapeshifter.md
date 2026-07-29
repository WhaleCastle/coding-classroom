# Python Course — Boss Fight IV: The Shapeshifter

## Tutor instructions for this boss

The **fourth boss-fight checkpoint**, played right after Chapter 12. It tests Chapters
1–12 — especially the new powers from 10–12 (functions, `return` values, and `random`) —
**with you muted**. Deliver the briefing and trials, then **stop teaching**: no
steps, no reminders, no leading questions. Let him build it and show you when it runs.

- **Hints cost XP, and a paid hint is ONLY a question.** If he asks: **read** the XP on his
  hero sheet — if it's 25+, record `boss_hints_used` +1 in `progress.md` (the script subtracts
  the 25; you never do XP maths) and ask **one** of the safe nudges below (no code, no
  keywords, no variable names, nothing that mirrors the answer); under 25 XP → encourage
  another attempt. Safe nudge bank: *"Which container gives you ONE random thing from
  many?"* · *"What must a function do so its answer can be USED outside it?"* · *"What
  keeps the battle turning — and what makes it stop?"*
- **Judge on the success criteria, not your reference.** Many ledgers win.
- **A win** = record `boss-04` in `bosses_won` (`progress.md`); the script then grants the
  trophy "Unmasked the Shapeshifter", +50 XP, and ⭐ Mastered on `functions`,
  `return values`, `random` (and keeps his earlier ⭐). You never compute the rewards.
- **A miss never blocks him.** No penalty: drop out of boss mode, go back to your normal
  teaching self on Chapter 10 (functions), Chapter 11 (return values) or Chapter 12
  (random) — full hints — and let him carry on to Chapter 13. The Shapeshifter waits for a
  rematch (a later win is still a full win). See AGENTS.md "Boss-fight checkpoints" step 4.
- Stay inside Chapters 1–12: **no string methods, no 2D lists, no files** (those come from
  Chapter 13 onward). If he reaches for one, gently say "everything you need is from
  Chapter 12 or earlier." See AGENTS.md "Boss-fight checkpoints".
- **Rematch-safe:** this boss is *usually* played right after Chapter 12, but bosses are
  non-blocking — he may face it later. Don't assume it's his 4th boss or that Chapter 13 is
  next: the win scripts branch on bosses-slain, and the "next quest" line is generic — when
  you send him onward, name his REAL next quest.

**Student work folder:** `python-course/student/boss-04/`
**Skills this boss tests:** `functions`, `return values`, `random`, `dictionaries`,
`while loops`, `if / decisions`, `f-strings`, `variables`.

## Boss briefing — say this to the student FIRST

> "Boss number four, and this one **never wears the same face twice**. Deep in the crypt
> waits the **Shapeshifter** — a creature that shivers into a different monster every time
> someone dares to fight it. Your quest: write a program that keeps a **roster** of at
> least three monsters, has the Shapeshifter pick ONE at random and announce what it's
> become, then battle it with functions that **answer back** — one that RETURNS a random
> hit of damage, one that RETURNS whether a fighter is still standing. Run it a few times;
> the face should change, and so should the fight. Build it, run it, and **show me it run
> when it works.** Good luck, hero!"

Then go quiet.

## The trials — what his program must do

1. Store a **roster of at least three monsters** as **dictionaries** (name, hp, attack).
2. Use **`random.choice`** to pick ONE monster from the roster, and **announce it** by
   reading its facts back out of the record in an f-string.
3. Write a `roll_damage`-style **function** that **RETURNS** a random number of damage,
   built from a fighter's `attack` stat (e.g. with `random.randint`).
4. Write an `is_alive`-style **function** that **RETURNS** `True`/`False`, and use its
   answer directly to control a `while` battle loop.
5. Run a full battle between the hero and the chosen monster using those two functions,
   and print a win/lose message that reads facts back out of the records (names, HP).

## Success criteria

- [ ] A roster of **≥3 monster dictionaries** exists, and `random.choice` picks one.
- [ ] The chosen monster is announced by reading its record's facts.
- [ ] A function **RETURNS** a random damage number (uses `random`).
- [ ] A function **RETURNS** `True`/`False` and that answer drives the `while` loop.
- [ ] The battle runs to a finish and the ending message reads facts from the records.
- [ ] He can explain, in his own words, **what his program does**.

## On a win / On a miss

**On a win — record the fact, then celebrate.** Add `boss-04` to `bosses_won` in
`progress.md`. **That is the only bookkeeping you do** — the script then awards the trophy,
the +50 XP, and the ⭐ Mastered spells, and sets his new rank on the sheet. To celebrate,
check one thing: **is this his 2nd or 4th boss won?** On a normal (non-rematch) run,
beating Boss IV IS usually his 4th boss won — but never assume, always check the sheet's
actual count. If yes → say script (A); otherwise → say script (B).

**(A) PROMOTION (this is his 2nd or 4th boss) — say (the sheet shows the exact new rank):**

> "The mist can't hold its shape any longer — **you UNMASKED the Shapeshifter!** 🏆 A
> roster of monsters, a random pick, functions that hand back real answers to drive the
> whole fight — all yours. A new trophy, spells turned ⭐ **Mastered**, and **you've
> earned a new rank**! 🎉 Open your hero sheet and see your new title — then on to your
> next quest, hero!"

**(B) NO PROMOTION (any other count) — say instead:**

> "The mist can't hold its shape any longer — **you UNMASKED the Shapeshifter!** 🏆
> Functions that return real answers, random damage, a battle loop that trusts them —
> real code, all your own. A new trophy, and ⭐ **Mastered** on your `functions`, your
> `return values` and your `random`. Open your hero sheet and see — then on to your next
> quest, hero!"

When you send him onward, name his REAL next quest (Chapter 13, teaching him to read
strings letter by letter, on a normal run; or wherever he actually is if this was a
rematch).

**On a miss — say this:**

> "Slippery one, that Shapeshifter — it changed shape before you could pin the fight down,
> but every adventurer gets caught out by a shifting foe once. Usually it's one piece
> that's the puzzle: picking a random monster from the roster, a function that hands its
> answer BACK instead of just printing it, or the loop that trusts that answer to know
> when to stop. Let's look again at Chapters 10 to 12 next time and come back for a
> rematch. No XP lost."

(Name the exact snag — `random.choice` on the roster, a missing `return`, or the `while`
condition not using the function's answer — but never write the fix for him.)

## Reference solution — TUTOR'S EYES ONLY, never show

Private yardstick only — judge his version on the criteria, never paste or quote it (hard
rule 10). Uses only Chapters 1–12 (no string methods, no 2D lists, no files). Runs under
Python 3. It reuses the running game's record shape and the `roll_damage`/`is_alive`
helpers from Chapter 11, upgraded with `random` from Chapter 12.

```python
# shapeshifter.py -- Boss Fight IV reference (TUTOR ONLY -- never show the student)
# Skills used: functions + return (Ch10-11), random.choice/randint (Ch12),
#   dictionaries, while loops, if/decisions, f-strings, variables, lists.
#   Nothing from Chapter 13 onward (no string slicing/indexing, no 2D lists, no files).

import random

# Chapter 9/12: a roster of monster RECORDS -- the Shapeshifter wears one at random.
monster_roster = [
    {"name": "Goblin", "hp": 12, "attack": 4},
    {"name": "Skeleton", "hp": 16, "attack": 5},
    {"name": "Giant Rat", "hp": 8, "attack": 3},
    {"name": "Cave Troll", "hp": 24, "attack": 7},
]


def roll_damage(attacker):
    # Chapter 11: this function RETURNS an answer instead of just printing one.
    # Chapter 12: the answer is random, built from the attacker's own attack stat.
    low = attacker["attack"] - 2
    high = attacker["attack"] + 2
    if low < 1:
        low = 1
    return random.randint(low, high)


def is_alive(fighter):
    # Chapter 11: another function that RETURNS True/False -- the battle loop
    # below uses this answer directly instead of re-checking hp itself.
    return fighter["hp"] > 0


# Chapter 9: the hero as one record.
hero = {"name": "Aldric", "hp": 30, "attack": 6}

# Chapter 12: random.choice picks ONE shifted form from the whole roster.
shape = random.choice(monster_roster)
# Copy its fields into a fresh dict so this battle never edits the roster itself.
enemy = {"name": shape["name"], "hp": shape["hp"], "attack": shape["attack"]}

print("A shimmer in the dark -- the SHAPESHIFTER settles on a form...")
print(f"It becomes a {enemy['name']}!  HP {enemy['hp']}, ATK {enemy['attack']}.")
print(f"\n{hero['name']} steps up, HP {hero['hp']}.")

# The battle loop keeps turning as long as BOTH functions say "still alive".
while is_alive(hero) and is_alive(enemy):
    dmg = roll_damage(hero)
    enemy["hp"] = enemy["hp"] - dmg
    print(f"{hero['name']} hits the {enemy['name']} for {dmg}!")

    if not is_alive(enemy):
        break

    dmg = roll_damage(enemy)
    hero["hp"] = hero["hp"] - dmg
    print(f"The {enemy['name']} hits back for {dmg}!")

# The ending reads facts straight out of the records -- nothing hardcoded.
if is_alive(hero):
    print(f"\nThe {enemy['name']} shudders and dissolves into mist. "
          f"{hero['name']} wins with {hero['hp']} HP left!")
else:
    print(f"\n{hero['name']} has fallen to the Shapeshifter's {enemy['name']} form...")
```
