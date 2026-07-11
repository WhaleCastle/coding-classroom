# Python Course — Boss Fight III: The Hoard Keeper

## Tutor instructions for this boss   (required)

The **third boss-fight checkpoint**, played right after Chapter 9. It tests Chapters
1–9 — especially the new powers from 7–9 (the `for` loop, lists, and dictionaries) —
**with you muted**. Deliver the briefing and trials, then **stop teaching**: no
steps, no reminders, no leading questions. Let him build it and show you when it runs.

- **Hints cost XP, and a paid hint is ONLY a question.** If he asks: **read** the XP on his
  hero sheet — if it's 25+, record `boss_hints_used` +1 in `progress.md` (the script subtracts
  the 25; you never do XP maths) and ask **one** of the safe nudges below (no code, no
  keywords, no variable names, nothing that mirrors the answer); under 25 XP → encourage
  another attempt. Safe nudge bank: *"How could you show every item without knowing how many
  there are?"* · *"Where does the running total start, and what happens to it for each
  coin-stack?"* · *"When you want a fact back by its NAME, which kind of container do you
  reach for?"* · *"What's the difference between the whole record and just one fact inside
  it?"*
- **Judge on the success criteria, not your reference.** Many ledgers win.
- **A win** = record `boss-03` in `bosses_won` (`progress.md`); the script then grants the
  trophy "Outwitted the Hoard Keeper", +50 XP, and ⭐ Mastered on `for loops`, `lists`,
  `dictionaries` (and keeps his earlier ⭐). You never compute the rewards.
- **A miss never blocks him.** No penalty: drop out of boss mode, go back to your normal
  teaching self on Chapter 7 (the `for` loop), Chapter 8 (lists) or Chapter 9 (the hero
  record) — full hints — and let him carry on to Chapter 10. The Keeper waits for a rematch
  (a later win is still a full win). See AGENTS.md "Boss-fight checkpoints" step 4.
- Stay inside Chapters 1–9: **no functions / `def`** (that's Chapter 10). If he reaches for
  one, gently say "everything you need is from Chapter 9 or earlier." See AGENTS.md
  "Boss-fight checkpoints".
- **Rematch-safe:** this boss is *usually* played right after Chapter 9, but bosses are
  non-blocking — he may face it later. Don't assume it's his 3rd boss or that Chapter 10 is
  next: the win scripts branch on bosses-slain, and the "next quest" line is generic — when
  you send him onward, name his REAL next quest.

**Student work folder:** `python-course/student/boss-03/`
**Skills this boss tests:** `for loops`, `lists`, `dictionaries`, `variables`, `input`,
`f-strings`, `if / decisions`, `numbers & arithmetic`.

## Boss briefing — say this to the student FIRST   (required)

> "Boss number three, and this one doesn't punch — it **counts**. The **Hoard Keeper**
> is a great scaly beast curled on a mountain of stolen treasure, and it lets nobody pass
> who can't keep a proper adventurer's **ledger**. Your quest: write a program that holds
> your hero as a record, keeps a backpack you can add to and empty, lists everything you
> carry, and TALLIES a pile of the Keeper's gold — then prints a tidy ledger of it all.
> You'll need your `for` loop, your lists, and your dictionaries — all on your own this
> time. Build it, run it, and **show me the ledger when it works.** Mind the hoard, hero!"

Then go quiet.

## The trials — what his program must do   (required)

1. Store the hero as a **dictionary** with at least `name`, `hp` and `gold`, and **announce
   him** by reading values **out of the record by their key** in an f-string.
2. Give the hero a **backpack** — a **list** of at least three items — and change it:
   **`append`** at least one item (loot picked up) and **`remove`** at least one (junk
   dropped).
3. Use a **`for` loop** to show the whole backpack — every item on its own line, however
   many there are.
4. The Keeper tips out its hoard — a **list of coin-stacks (numbers)**. Use a **`for` loop**
   to add them all into a **total**, and store that total back in the hero's record (e.g.
   `hero["gold"]`).
5. Print a final **ledger** that reads the hero's facts back out of the dictionary
   (name, hp, gold, and how many items he carries).

## Success criteria   (required — checkbox list)

- [ ] The hero is stored as a **dictionary** and at least one value is read by its key.
- [ ] A **list** backpack is created, with an item **appended** AND one **removed**.
- [ ] A **`for` loop** prints every backpack item, however many there are.
- [ ] A **`for` loop** adds a list of numbers into a **total** that is stored in the record.
- [ ] A final **ledger** prints facts read back out of the dictionary.
- [ ] He can explain, in his own words, **what his program does**.

## On a win / On a miss   (required)

**On a win — record the fact, then celebrate.** Add `boss-03` to `bosses_won` in
`progress.md`. **That is the only bookkeeping you do** — the script then awards the trophy,
the +50 XP, and the ⭐ Mastered spells, and sets his new rank on the sheet. To celebrate,
check one thing: **is this his 2nd or 4th boss won?** If yes it's a class promotion → say
script (A); otherwise (a normal 3rd-boss run lands here) → say script (B).

**(A) PROMOTION (this is his 2nd or 4th boss) — say (the sheet shows the exact new rank):**

> "The Keeper's eyes narrow — your ledger balances, and **you beat the Hoard Keeper!** 🏆
> You held your hero in a record, kept a backpack, looped through the loot and tallied the
> whole hoard — all yourself. A new trophy, spells turned ⭐ **Mastered**, and **you've
> earned a new rank**! 🎉 Open your hero sheet and see your new title — then on to your next
> quest, hero!"

**(B) NO PROMOTION (any other count) — say instead:**

> "The Keeper's eyes narrow — your ledger balances, and **you beat the Hoard Keeper!** 🏆
> Records, lists, a loop that counts the whole hoard — real code, all your own. A new
> trophy, and ⭐ **Mastered** on your `for` loops, your lists and your dictionaries. Open
> your hero sheet and see — then on to your next quest, hero!"

When you send him onward, name his REAL next quest (Chapter 10, teaching his hero to ACT
with functions, on a normal run; or wherever he actually is if this was a rematch).

**On a miss — say this:**

> "Tough hoard — the Keeper's still counting, but every adventurer fumbles a tally now and
> then. Usually it's one piece that's the puzzle: looping through the bag, adding the
> coin-stacks up, or pulling a fact back out of the record by its name. Let's look again at
> Chapters 7 to 9 next time and come back to balance the books. No XP lost."

(Name the exact snag — the `for` loop over the list, the running total, the `append`/`remove`,
or a `KeyError` reading the record — but never write the fix for him.)

## Reference solution — TUTOR'S EYES ONLY, never show   (required)

Private yardstick only — judge his version on the criteria, never paste or quote it (hard
rule 10). Uses only Chapters 1–9 (no functions, no `random`). Runs under Python 3. It reuses
the running game's record shape (`name`, `hp`, `gold`, `bag`) so it's the same RPG.

```python
# hoard_keeper.py — Boss Fight III reference (TUTOR ONLY — never show the student)
# Skills used: dictionaries (Ch9), lists + append/remove (Ch8), for loops (Ch7),
#   f-strings, input, arithmetic. Nothing from Chapter 10 onward (no functions, no random).

print("THE HOARD KEEPER uncoils on its mountain of gold.")
print('"Prove you can keep a ledger, little one, or you keep NOTHING."')

# Chapter 9: the hero is ONE record; read facts back out by their key.
name = input("\nName your adventurer: ").strip() or "Aldric"
hero = {"name": name, "hp": 30, "gold": 0}
print(f"\n{hero['name']} steps up, HP {hero['hp']}.")

# Chapter 8: a backpack list — pick loot up, drop the junk.
backpack = ["Rusty Key", "Torch", "Mouldy Bread"]
backpack.append("Gold Ring")        # looted from the hoard
backpack.remove("Mouldy Bread")     # dropped

# Chapter 7: show the whole bag, however many items it holds.
print("\n=== BACKPACK ===")
for item in backpack:
    print(f"- {item}")

# Chapter 7 + 8: total the Keeper's coin-stacks with a for loop, then store it in the record.
coin_stacks = [12, 5, 20, 8, 3]
total = 0
for stack in coin_stacks:
    total = total + stack
hero["gold"] = total

# Chapter 9: the final ledger — every fact read back out of the record.
print("\n=== LEDGER ===")
print(f"Name : {hero['name']}")
print(f"HP   : {hero['hp']}")
print(f"Gold : {hero['gold']}")
print(f"Items: {len(backpack)}")

if hero["gold"] > 0:
    print(f'\nThe Keeper bows its great head. "A true bookkeeper. Pass, {hero["name"]}."')
```
