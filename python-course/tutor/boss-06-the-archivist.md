# Python Course — Boss Fight VI: The Archivist

## Tutor instructions for this boss

The **sixth boss-fight checkpoint**, played right after Chapter 18. It tests Chapters
1–18 — especially the new powers from 16–18 (file handling, defensive design, and
search & sort) — **with you muted**. Deliver the briefing and trials, then **stop
teaching**: no steps, no reminders, no leading questions. Let him build it and show
you when it runs.

- **Hints cost XP, and a paid hint is ONLY a question.** If he asks: **read** the XP on his
  hero sheet — if it's 25+, record `boss_hints_used` +1 in `progress.md` (the script subtracts
  the 25; you never do XP maths) and ask **one** of the safe nudges below (no code, no
  keywords, no variable names, nothing that mirrors the answer); under 25 XP → encourage
  another attempt. Safe nudge bank: *"What should the program do FIRST the very first time
  it runs, when there's nothing to load?"* · *"How does a hand-made search know when to
  STOP looking?"* · *"In one pass of your sort, where does the biggest value end up?"*
- **Judge on the success criteria, not your reference.** Many ledgers win.
- **A win** = record `boss-06` in `bosses_won` (`progress.md`); the script then grants the
  trophy "Outsorted the Archivist", +50 XP, and ⭐ Mastered on `file handling`,
  `defensive design`, `search & sort` (and keeps his earlier ⭐). You never compute the
  rewards.
- **A miss never blocks him.** No penalty: drop out of boss mode, go back to your normal
  teaching self on Chapter 16 (files), Chapter 17 (guards) or Chapter 18 (search & sort) —
  full hints — and let him carry on to Chapter 19. The Archivist waits for a rematch (a
  later win is still a full win). See AGENTS.md "Boss-fight checkpoints" step 4.
- Stay inside Chapters 1–18: **no binary search, no merge/insertion sort** (Chapter 18
  only NAMED those — a hand-written linear search and bubble sort are what count here),
  no classes/OOP, no SQL. If he reaches for one, gently say "everything you need is from
  Chapter 18 or earlier." See AGENTS.md "Boss-fight checkpoints".
- **Rematch-safe:** *usually* played right after Chapter 18, but bosses are non-blocking —
  don't assume it's his 6th boss or that Chapter 19 is next; name his REAL next quest. Same
  for class promotion: it only fires on his **2nd or 4th boss won**, no "6th boss" special
  case — always read the sheet's actual count, never assume.

**Student work folder:** `python-course/student/boss-06/`
**Skills this boss tests:** `file handling`, `defensive design`, `search & sort`, `lists`,
`for loops`, `while loops`, `functions`, `return values`.

## Boss briefing — say this to the student FIRST

> "Boss number six, and this one doesn't fight — it FILES. Deep in the crypt's driest
> chamber sits the **Archivist**, a dusty keeper who has logged every treasure ever found
> down here, and he refuses to stamp your record until you can keep an archive as well as
> he can. Your quest: write a program that **saves** a list of treasures to a file,
> **loads** it back without ever crashing — not on a torn page, not on a missing ledger —
> **searches** it by name, and **sorts** it richest-first. All on your own this time.
> Build it, run it, and **show me the archive when it works.** Mind the dust, hero!"

Then go quiet.

## The trials — what his program must do

1. A **treasure list** of at least five name + value entries (parallel lists or a list of
   dictionaries) is **saved to a file** and **loaded back** from it.
2. The loading is **guarded**: a missing file or a broken/non-number line is handled
   without the program crashing (`try`/`except` or a check).
3. A **hand-written linear search** finds a treasure by name (a `for` loop and an `if`,
   not `.index()` or `in`).
4. A **hand-written bubble sort** orders the treasures by value, printed biggest first.
5. At least one **input is validated** — it re-asks until the answer is acceptable, never
   crashing and never accepting nonsense.

## Success criteria

- [ ] A treasure list of **5+ entries** is saved to a file, then loaded back from that file.
- [ ] Loading survives a **missing file** and a **broken/non-number line** without crashing.
- [ ] A **hand-written linear search** (`for` + `if`) finds a treasure by name.
- [ ] A **hand-written bubble sort** prints the treasures **biggest-value first**.
- [ ] At least one input **re-asks until valid**.
- [ ] He can explain, in his own words, **what his program does**.

## On a win / On a miss

**On a win — record the fact, then celebrate.** Add `boss-06` to `bosses_won` in
`progress.md`. **That is the only bookkeeping you do** — the script then awards the trophy,
the +50 XP, and the ⭐ Mastered spells, and sets his new rank on the sheet. To celebrate,
check one thing: **is this his 2nd or 4th boss won?** If yes it's a class promotion → say
script (A); otherwise (a normal 6th-boss run lands here) → say script (B).

**(A) PROMOTION (this is his 2nd or 4th boss) — say (the sheet shows the exact new rank):**

> "The Archivist's quill finally stops scratching — **you OUTSORTED the Archivist!** 🏆
> You saved a whole archive to a file, guarded it against every torn page, hunted a name
> down by hand, and sorted the hoard richest-first — all yourself. A new trophy, spells
> turned ⭐ **Mastered**, and **you've earned a new rank**! 🎉 Open your hero sheet and
> see your new title — then on to your next quest, hero!"

**(B) NO PROMOTION (any other count) — say instead:**

> "The Archivist's quill finally stops scratching — **you OUTSORTED the Archivist!** 🏆
> A file that saves and loads, a guard that shrugs off bad data, a hand-built search and
> a hand-built sort — real code, all your own. A new trophy, and ⭐ **Mastered** on your
> `file handling`, your `defensive design` and your `search & sort`. Open your hero sheet
> and see — then on to your next quest, hero!"

When you send him onward, name his REAL next quest (Chapter 19, designing the whole game,
on a normal run; or wherever he actually is if this was a rematch).

**On a miss — say this:**

> "Tough archive — the Archivist's still squinting at your ledger, but every adventurer
> fumbles a filing system now and then. Usually it's one piece that's the puzzle: guarding
> the load against a bad line, walking the list by hand to find a name, or swapping
> neighbours correctly in the sort. Let's look again at Chapters 16 to 18 next time and
> come back to settle the archive. No XP lost."

(Name the exact snag — a crash on a missing/bad file, a search with no found-flag, or a
sort that loses a value on the swap — but never write the fix for him.)

## Reference solution — TUTOR'S EYES ONLY, never show

Private yardstick only — judge his version on the criteria, never paste or quote it (hard
rule 10). Uses only Chapters 1–18 (hand-written search/sort, plain `open`/`try`/`except`,
no binary search, no merge/insertion sort, no classes, no SQL). Runs under Python 3.

```python
# archivist.py — Boss Fight VI reference (TUTOR ONLY — never show the student)
# Skills used: file handling (Ch16), defensive design (Ch17), search & sort (Ch18),
#   lists, for/while loops, functions, return values. Nothing from Chapter 19 onward.

FILENAME = "treasures.txt"

def save_treasures(treasures):
    # Ch16: one FACT per line — a name line, then its value line, the
    # same shape Chapter 16's save crystal taught (not one comma-row).
    file = open(FILENAME, "w")
    for t in treasures:
        file.write(f"{t['name']}\n")
        file.write(f"{t['value']}\n")
    file.close()

def load_treasures():
    # Ch16+17: GUARDED — missing file gets defaults; a smudged value or a
    # torn trailing line is skipped, not a crash.
    try:
        file = open(FILENAME)
    except FileNotFoundError:
        print("No archive found yet — the Archivist starts a fresh ledger.")
        defaults = [{"name": "Ruby", "value": 120}, {"name": "Silver Chalice", "value": 60},
                    {"name": "Ancient Coin", "value": 15}, {"name": "Emerald", "value": 200},
                    {"name": "Rusty Dagger", "value": 5}]
        save_treasures(defaults)
        return defaults

    # Read every non-blank line, stripped, into one flat list: name, value,
    # name, value, ...
    lines = []
    for line in file:
        stripped = line.strip()
        if stripped != "":
            lines.append(stripped)
    file.close()

    loaded = []
    i = 0
    while i + 1 < len(lines):
        name = lines[i]
        try:
            value = int(lines[i + 1])
            loaded.append({"name": name, "value": value})
        except ValueError:
            print(f"Archivist frowns at a smudged number: '{lines[i + 1]}' — skipped.")
        i = i + 2

    if len(lines) % 2 == 1:
        print(f"Archivist frowns at a torn page: '{lines[len(lines) - 1]}' — skipped.")

    return loaded

def find_treasure(treasures, wanted):
    # Ch18: hand-written LINEAR search — walk the list, compare names, found-flag.
    found = False
    for t in treasures:
        if t["name"].lower() == wanted.lower():
            found = True
            print(f"Found it! {t['name']} is worth {t['value']} gold.")
            break
    if not found:
        print(f"No treasure named '{wanted}' in the archive.")

def sort_treasures(treasures):
    # Ch18: hand-written BUBBLE sort, biggest first — temp-box swap, passes until none.
    n = len(treasures)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if treasures[i]["value"] < treasures[i + 1]["value"]:
                temp = treasures[i]
                treasures[i] = treasures[i + 1]
                treasures[i + 1] = temp
                swapped = True
    return treasures

def ask_menu_choice():
    # Ch17: VALIDATED input — keeps re-asking until 1, 2 or 3 is typed.
    choice = input("1) Search  2) Sorted list  3) Quit: ").strip()
    while choice not in ["1", "2", "3"]:
        print("The Archivist only understands 1, 2 or 3.")
        choice = input("1) Search  2) Sorted list  3) Quit: ").strip()
    return choice

print("THE ARCHIVIST looks up from a mountain of dusty ledgers.")
print('"Prove you can keep MY archive, or you get no stamp."')

treasures = load_treasures()
print(f"\n{len(treasures)} treasures loaded from the archive.")

running = True
while running:
    choice = ask_menu_choice()
    if choice == "1":
        wanted = input("Search for which treasure? ").strip()
        find_treasure(treasures, wanted)
    elif choice == "2":
        sort_treasures(treasures)
        print("\n=== TREASURES, BIGGEST FIRST ===")
        for t in treasures:
            print(f"{t['name']}: {t['value']} gold")
    else:
        running = False

print('\nThe Archivist stamps a fresh page. "Your archive is safe with me."')
```
