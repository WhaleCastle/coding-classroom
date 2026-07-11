# Chapter 9 — The Character Sheet

## Tutor instructions for this chapter

Until now the hero has been scattered across loose variables — a `name` here, an
`hp` there. Today you gather the whole hero into ONE tidy record: a **dictionary**.
Teach one step per message and wait for his result. Do not write his code.

A dictionary remembers things by NAME (`hero["hp"]`), where a list remembers by
ORDER (`bag[0]`). Lean on Chapter 8's list — the backpack now lives *inside* the
record — and on f-strings from Chapter 2 to print a neat sheet. The classic new
error here is `KeyError` (asking for a label that isn't there): treat it exactly
like Chapter 8's `IndexError` — a chance to ask "which keys actually exist?"

At the end the creator prints a small **hero portrait**. That portrait is a
**given asset** (`tutor/assets/hero_ascii.txt`) — he PASTES it, he does not draw
it. Keep "picture you're given" and "record you author" clearly separate. (He also
has a full-colour drawing of his hero at `tutor/assets/hero_sprite.png` he can open
any time; he'll get to recolour it in the optional Bonus B1 — never asked to write
graphics code.)

**Student work folder:** `python-course/student/chapter-09/`

**Skills this chapter leans on:** `variables`, `f-strings`, `input`, `lists`.

## Learning objectives (max 3)

1. Make a dictionary of `key: value` pairs and read a value by its key.
2. Change an existing value and add a brand-new key.
3. Say why one record beats a pile of separate variables.

## Concepts — explain in this voice

- **Dictionary (record):** "A list remembers things by their ORDER — item 0, item
  1. A dictionary remembers them by NAME. Think of your hero's ID card: instead of
  `hero[0]` you ask for `hero['name']` or `hero['hp']` — you say WHICH fact you want
  by its label. It's written in curly brackets `{ }`, and every entry is a
  `"label": value` pair."
- **Look a value up:** "`hero['hp']` reaches into the record and reads the HP back.
  Same square brackets as a list — but inside them you put a *name in quotes*, not a
  number."
- **Change / add:** "Put the lookup on the LEFT of an `=` and you change it:
  `hero['hp'] = 25`. And if you assign to a label that isn't there yet, the
  dictionary GROWS a new entry — `hero['gold'] = 10` gives the hero a gold pouch he
  never had before."
- **Why a record:** "You *could* keep `name`, `hp`, `attack` as five separate
  variables — but then 'the hero' is five things to juggle. One dictionary keeps the
  whole hero in a SINGLE box, so from now on 'the hero' is one thing you can hand
  around in one go."

## Chapter opener — say this to the student FIRST

Say something like: *"Right now your hero is scattered — his name in one variable,
his HP in another, his bag in a third. Today we gather ALL of him into one neat
**character sheet**: a single record that holds his name, class, HP, attack and
backpack together. And a record like this isn't just for a hero — any time one
thing has lots of facts about it (a monster, a treasure, a save file) you'll reach
for a dictionary. By the end you'll have a real **hero creator** that asks who he
is, remembers everything about him, and even prints his portrait. We'll build the
record, read and change facts in it, tuck his backpack inside, and print the whole
sheet. Ready? Let's fill in his character sheet."* Keep it warm, then start Step 1.

## Guided steps

**Step 1 — Build the record.** New file `hero_sheet.py`. Teach the curly-bracket
dictionary. Have him write `hero = {"name": "Aldric", "cls": "warrior"}` (his own
name/class are fine) and `print(hero)`. Point out the curly brackets and that each
entry is a `"label": value` pair separated by a comma.
Success: the whole record prints, showing both label:value pairs inside `{ }`.

**Step 2 — Look one fact up.** Teach lookup by key. Have him print just the name:
`print(hero["name"])`, then a greeting with an f-string:
`print(f"{hero['name']} the {hero['cls']} enters the crypt.")`. Ask him to PREDICT
what `hero["cls"]` will show before he runs it.
Success: the single fact prints (not the whole record); the greeting reads well.

**Step 3 — Add the stats.** Teach growing the record. Have him give the hero numbers
by assigning new keys: `hero["hp"] = 30`, `hero["max_hp"] = 30`, `hero["attack"] = 7`.
Print the record again and notice it now holds five facts.
Success: the record has grown; the new keys appear with their values.

**Step 4 — Change a value (he takes a hit).** Teach updating in place. Have him
lower the HP: `hero["hp"] = hero["hp"] - 5`. Ask him to PREDICT the new HP first,
then print `f"HP is now {hero['hp']}/{hero['max_hp']}"`.
Success: the HP drops by 5 and prints correctly; he sees a value can be changed.

**Step 5 — Tuck the backpack inside.** Reuse Chapter 8's list — but now it lives in
the record. Have him add `hero["bag"] = ["Rusty Key", "Torch"]`, then pick something
up with `hero["bag"].append("Health Potion")`. Point out: a dictionary can hold a
list inside it.
Success: the bag is a key of the record; appending adds to the list within.

**Step 6 — Print the character sheet.** Reuse the Chapter 8 `for` loop to list the
bag. Have him print a tidy sheet — a title line, then f-string lines for name/class,
HP, attack, and a `for item in hero["bag"]:` loop for the backpack.
Success: a clean sheet prints all the hero's facts, bag included.

**Step 7 — Break it on purpose (the missing-key trap).** Have him ask for a key that
doesn't exist — `print(hero["luck"])` — and run. He'll see
`KeyError: 'luck'`. Ask: "Which labels does the record actually have? Point at where
you made them." Then have him read a real key like `hero["attack"]`.
Success: he saw the `KeyError`, understands a key must exist first, and fixed it.

## Mini-challenge — The Hero Creator

In `hero_sheet.py`, the student builds a working **hero creator** for his RPG using
only this chapter and earlier ones. It must:
- store the hero as ONE dictionary with at least `name`, `cls`, `hp`, `max_hp` and a
  `bag` (a list) — he may `input()` the name/class if he likes,
- change at least one value after creating it (he takes a hit, drinks a potion…),
- add at least one brand-new key that wasn't in the record to start,
- print a full **character sheet** that reads every fact and loops the bag,
- finish by printing the given hero **portrait** (see below).

He designs the hero and flavour himself. Hints only, never the code.

**The portrait is a given asset — he PASTES it, he doesn't draw it.** Hand him the
block from `tutor/assets/hero_ascii.txt` to paste as a multi-line string and print,
e.g. `HERO_ART = """ …paste… """` then `print(HERO_ART)`. Make clear it's a gift
(like the sprite): the code he AUTHORS is the record and the sheet.

## Success criteria (check before finishing the chapter)

- [ ] A dictionary is created with several `key: value` pairs.
- [ ] A value is read by its key and used in an f-string.
- [ ] An existing value is changed AND a new key is added.
- [ ] A full sheet prints, looping the bag list inside the record.
- [ ] He can explain in his own words how a dictionary differs from a list
      (name vs order).

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Key that doesn't exist | `KeyError: 'luck'` | "Which labels did you actually put in the record? Point at where each one was made." |
| Square brackets for the record | `[]` makes a list, not a record | "A record remembers by NAME, not order. What brackets go around `"label": value` pairs?" |
| Forgot quotes on a key | `NameError: name 'name' is not defined` | "Is `name` a label (text) or a variable? How do we show Python it's text?" |
| Comma missing between pairs | `SyntaxError` | "How does Python know where one `label: value` ends and the next begins?" |
| Looked up bag but printed the whole record | too much prints | "Which key holds JUST the backpack? Ask the record for that one." |
| Tried to `append` to the whole dict | `AttributeError` | "`append` is a list trick. Which key inside the record IS the list?" |

## Gate — do not move on until

- He has built a dictionary and read a value by its key.
- He has changed an existing value and added a new key.
- He has printed a sheet that loops the bag list held inside the record.
- He has met (and fixed) a `KeyError`.
- His hero creator runs and the sheet is correct.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 9 finished!** Your whole hero lives in one neat record now —
> name, class, HP, attack and backpack, all in a single character sheet you can read,
> change and grow. You even printed his portrait! Run your creator and make a hero
> you like. And now your third **boss** awaits: the **Hoard Keeper**, a
> treasure-guarding beast you must out-count on your own — build its ledger with no
> steps from me, and earn a trophy. Face it now, or stop here and take it on next
> session?"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — what's the difference between a list and a dictionary?"* and
wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put in
today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 9 — The Character Sheet
- Completed: built the hero as one dictionary — read/changed/added keys, tucked the bag inside, printed a full sheet + portrait
- Strong at: dictionaries; looking things up by name; printing a tidy sheet
- Struggled with: nothing this time
- How to help next: run Boss III — The Hoard Keeper (Chapters 1–9 checkpoint, tutor muted)
- Next time: Boss III — The Hoard Keeper (then Chapter 10)
```

**Then update the `### Facts`** in `progress.md`: `chapters_cleared` +1 (and +1 to
`mini_challenges_done` / `predict_wins` / `break_it_fixes` for any that happened
today) — the script turns these into his new Level, XP and spells.

**Then refresh the skill ledger** (the same silent save, tutor-private — he never
sees it). This chapter introduced `dictionaries`; in the `### Skill ledger` at the
top of `progress.md`, move it from `new` toward `learning` or `solid` — only `solid`
if he built the record and read/changed/added keys unaided today, `shaky` if the
`KeyError` or square-vs-curly brackets kept tripping him (see AGENTS.md "The skill
ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and to judge his standard. NEVER show
or quote it. His hero and flavour will differ — that's correct, as long as one
dictionary holds the hero, a value is read/changed, a new key is added, and a sheet
loops the bag. It reuses the running game's record shape (`name`, `cls`, `hp`,
`max_hp`, `attack`, `bag`) so it's the next slice of the same RPG. No functions,
no `random` — those are Chapters 10 and 12.

```python
# hero_sheet.py — Chapter 9 reference (tutor only)
# Skills used: dictionaries (create, look up, change, add key), lists inside a dict,
# a for loop, f-strings, input. Nothing later (no functions, no random).

# The hero portrait is a GIVEN asset (tutor/assets/hero_ascii.txt) — pasted, not drawn.
HERO_ART = """
      _____
     ( ~~~ )
     | o o |
     |  >  |
     | '-' |
      |===|
    (=|   |=)
      | # |
      |___|
      |   |
      |_|_|
"""

# Build the hero as ONE record. Each entry is a "label": value pair.
name = input("Name your hero: ").strip() or "Aldric"
cls = input("Class (warrior/mage/rogue): ").strip() or "warrior"
hero = {
    "name": name,
    "cls": cls,
    "hp": 30,
    "max_hp": 30,
    "attack": 7,
    "bag": ["Rusty Key", "Torch"],   # a list lives INSIDE the record
}

# Change a value: the hero takes a knock on the way in.
hero["hp"] = hero["hp"] - 5

# Add a brand-new key that wasn't there to start — a gold pouch.
hero["gold"] = 10

# Pick something up — append to the list held under the "bag" key.
hero["bag"].append("Health Potion")

# Print the character sheet — read every fact by its name, loop the bag.
print(HERO_ART)
print("=== CHARACTER SHEET ===")
print(f"Name  : {hero['name']} the {hero['cls']}")
print(f"HP    : {hero['hp']}/{hero['max_hp']}")
print(f"Attack: {hero['attack']}")
print(f"Gold  : {hero['gold']}")
print("Backpack:")
for item in hero["bag"]:
    print(f"  - {item}")
```
