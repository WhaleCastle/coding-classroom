# Python Course — Chapter 17: Bullet-proof the Game

## Tutor instructions for this chapter

Budget **2–3 sessions** — the game learns GCSE-level **defensive design**,
surviving whatever a real player types at it. **`try`/`except ValueError` is
brand new** — script it plainly: "a safety net: TRY this, and if it
explodes, do this instead." Pair it with the ONE error it's meant to catch —
never a bare `except:`.

`.lower()` recaps Chapter 13; `.strip()` is new — "it trims stray spaces and
the invisible newline `input()` leaves behind." Builds on Chapter 16's save
crystal, which now gets a password — confirm save/load code exists before
Step 5. Ceiling: Chapters 1–16 plus `try`/`except` and `.strip()`. No
search/sort yet — that's Chapter 18.

**Student work folder:** `python-course/student/chapter-17/`

**Skills this chapter leans on:** `file handling`, `functions`, `while loops`,
`if / decisions`, `string handling`, `dictionaries`.

## Learning objectives (max 3)

1. Guard a number input with `try`/`except ValueError` inside a re-asking
   `while` loop.
2. Validate and sanitise text input (`.strip()`, `.lower()`) and add a save
   password.
3. Name the three kinds of error (syntax / runtime / logic) and test input as
   normal / boundary / erroneous data.

## Concepts — explain in this voice

- **try/except — the safety net:** "Some lines can EXPLODE while running — like turning `"banana"` into a number, a RUNTIME error (readable code that breaks mid-run — different from a SYNTAX error, unreadable code, like a missing colon). `try` attempts the risky line; `except ValueError:` catches THAT one error instead of crashing — a safety net under a tightrope."
- **Validation — the stubborn gatekeeper:** "A `while` loop that keeps re-asking until input passes the test — a gatekeeper who won't let bad data through."
- **Sanitisation:** "`.strip()` trims stray spaces and the invisible newline `input()` leaves on the end; `.lower()` (Chapter 13) flattens capitals away. Clean input BEFORE you check it."
- **Authentication:** "Prove you're allowed in — the save crystal remembers a password, and loading only unlocks the hero record if it matches."
- **Testing & trace tables:** "Test on purpose with three kinds of data — NORMAL (sensible), BOUNDARY (right on the edge), ERRONEOUS (deliberately wrong) — and trace your code by hand, one line at a time, to hunt the sneakiest bug of all: a LOGIC error, where nothing crashes but the answer is just wrong."

## Chapter opener — say this to the student FIRST

Say something like: *"Right now your game trusts the player completely — type a real number or it crashes. Today we make it BULLET-PROOF: it'll survive "banana" where a number goes, refuse a nonsense menu choice politely, and lock your save crystal behind a password. This matters everywhere, not just here — EVERY program a real person types into needs this defence, from a bank login to a rocket launch sequence. We'll crash it on purpose first, then build a safety net, a gatekeeper loop, the password lock, and test it properly like a pro. Ready to make your game unbreakable?"* Keep it warm, then start Step 1.

## Guided steps

**Step 1 — Crash it on purpose.** Type `banana` into an existing number input (`int(input(...))`) — Python shows `ValueError: invalid literal for int() with base 10: 'banana'`, a RUNTIME error, unlike a SYNTAX error (unreadable code) or a LOGIC error (runs fine, wrong answer — ask him to recall one from earlier chapters).
Success: he's seen the traceback and can name all three error kinds.

**Step 2 — The safety net.** Wrap that line in `try`/`except ValueError`, printing a friendly message on failure instead of crashing; run again with `banana`.
Success: it no longer crashes — the `except` block catches it.

**Step 3 — The stubborn gatekeeper.** Combine it with `while True:` that only `break`s once a real number lands. PREDICT: three `banana`s in a row, then what?
Success: it re-asks every time on bad input, moves on only once valid.

**Step 4 — Menu validation.** Build (or harden) a menu accepting only `"1"`/`"2"`/`"3"` — `.strip().lower()` first, then check membership, in a re-asking loop.
Success: `"5"`, `" 1 "` and `"ONE"` are all handled correctly.

**Step 5 — The password.** Saving now writes a password line; loading asks for it and only returns the hero if it matches (`.strip()` both sides).
Success: the right password loads the hero; a wrong one is refused, not a crash.

**Step 6 — Test like a pro.** Fill a 3-row test table (normal / boundary / erroneous) for one guarded input — predict each row, then run to check.
Success: a filled table where every prediction matched reality.

**Step 7 — Trace table.** Hand-walk one run of the re-ask loop on paper: each line, every variable's value, whether the loop condition still holds.
Success: the trace matches what the program actually does.

## Mini-challenge — The Unbreakable Menu

The student hardens his own game using only this chapter and earlier ones. It
must:
- have a menu that only accepts its valid choices — anything else re-asks,
  never crashes,
- have a number input guarded with `try`/`except ValueError` inside a
  re-asking loop,
- have a save file locked behind a password (wrong password refused, not
  crashed),
- come with a filled 3-row test table (normal / boundary / erroneous).

He designs which parts of his own game to harden. Hints only, never the code.

## Side quest (optional) — The Three Tries

Offer this only when he's ahead of pace — it costs nothing to skip. Pitch it
like: *"Feeling ruthless? Give your save crystal a temper — only 3 password
attempts before it seals shut and taunts him."* Requirements:
- a counter that increases on every wrong password attempt,
- a `while` loop that keeps asking until the password is right OR 3 attempts
  are used up,
- on the 3rd miss, print a taunting locked-out message instead of asking
  again.

## Success criteria (check before finishing the chapter)

- [ ] A guarded number input survives `banana`-style garbage without
      crashing.
- [ ] A menu only accepts its valid choices, sanitised with
      `.strip()`/`.lower()`.
- [ ] The save file is password-protected; a wrong password is refused, not
      crashed past.
- [ ] A filled 3-row test table (normal / boundary / erroneous) exists.
- [ ] He can explain, in his own words, the difference between a syntax, a
      runtime and a logic error.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Wrote `except` before `try`, or a `try` with no `except` | `SyntaxError` | "Which comes first — trying the risky line, or catching what goes wrong with it?" |
| Caught every possible error with a bare `except:` | bugs go silent, hard to find later | "Which ONE error do you actually expect here? What might a blanket `except` be hiding from you?" |
| Re-ask loop that never exits even on good input | infinite loop, program hangs | "Inside the loop, what has to happen for it to finally stop asking? Is anything actually changing?" |
| Compared the password before `.strip()`ing it | `"sword "` typed correctly still fails | "Could there be an invisible character on the end of what he typed? What cleans that up?" |

## Gate — do not move on until

- He has written a `try`/`except ValueError` around a real input line, run
  with garbage, and seen it survive.
- He has a re-asking validation loop (number or menu) that only lets good
  input through.
- His save file has a working password check.
- He has filled in and run a 3-row test table.
- He can name all three error kinds unaided.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 17 finished!** Your game is bullet-proof now — nonsense typed at menus or number prompts gets calmly re-asked instead of crashing, and your save crystal won't open without the right password. You even tested it like a pro, on purpose, with normal, boundary AND erroneous data. Go try to BREAK your own game — that's the fun part now! Next up, Chapter 18 teaches your hero to search his backpack and sort his loot. Stop here or carry on, adventurer!"

Before you treat the chapter as done, if he hasn't already said it, ask: *"In your own words — what's the difference between a runtime error and a logic error?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of `python-course/progress.md`. Don't say you're doing it. Copy this shape, put in today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 17 — Bullet-proof the Game
- Completed: guarded number input (try/except + re-ask loop), validated the menu, password-locked the save crystal, filled a normal/boundary/erroneous test table
- Strong at: try/except; telling syntax, runtime and logic errors apart
- Struggled with: nothing this time
- How to help next: start Chapter 18 — search & sort (find items, sort a leaderboard)
- Next time: Chapter 18 — Find & Sort the Loot
```

**Then update the `### Facts`** in `progress.md`: `chapters_cleared` +1 (and +1 to `mini_challenges_done` / `predict_wins` / `break_it_fixes` for any that happened today).

**Then refresh the skill ledger** (the same silent save, tutor-private — he never sees it). This chapter introduced `defensive design`; move it from `new` toward `learning` or `solid` — only `solid` if he built the try/except guard, the re-ask loop AND the password check unaided today, `shaky` if `try`/`except` ordering or the infinite re-ask loop kept tripping him (see AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only — use it to shape hints and judge his standard, never show or quote it. What matters is a guarded number input surviving garbage via try/except in a re-ask loop, a validated menu, and a password-protected save. Reuses the Chapter 16 save pattern and a subset hero record (`name`, `hp`, `gold`). No search/sort — that's Chapter 18.

```python
# harden_the_menu.py — Chapter 17 reference (tutor only)
# Skills used: try/except (ValueError, FileNotFoundError), while-loop
# validation, .strip()/.lower(), file save/load (Ch16), if/decisions,
# functions, f-strings, dictionaries.
# Nothing later: no search/sort (Chapter 18).

SAVE_FILE = "save.txt"


def get_valid_gold(prompt):
    # Safety net + stubborn gatekeeper combined: keep asking until int()
    # doesn't explode AND the number is inside the allowed range.
    while True:
        typed = input(prompt).strip()
        try:
            gold = int(typed)
            if gold < 0 or gold > 100:
                print("Starting gold must be between 0 and 100.")
            else:
                return gold
        except ValueError:
            print(f"'{typed}' isn't a whole number. Try again.")


def get_menu_choice():
    # Sanitise first (.strip removes stray spaces/newline, .lower ignores
    # CAPS), THEN check it's a choice we actually accept.
    while True:
        choice = input("1) New game   2) Load game   3) Quit\n> ").strip().lower()
        if choice in ["1", "2", "3"]:
            return choice
        print("Please type 1, 2 or 3.")


def save_hero(hero, password):
    # One fact per line (Ch16) — the password line locks the file.
    save_file = open(SAVE_FILE, "w")
    save_file.write(f"{hero['name']}\n{hero['hp']}\n{hero['gold']}\n{password.strip()}\n")
    save_file.close()
    print("Saved to the crystal.")


def load_hero():
    try:
        save_file = open(SAVE_FILE)
    except FileNotFoundError:
        print("No save crystal found yet — start a new game first.")
        return None

    lines = []
    for line in save_file:
        lines.append(line.strip())
    save_file.close()
    name = lines[0]
    hp_text = lines[1]
    gold_text = lines[2]
    real_password = lines[3]

    if input("Password for this save: ").strip() != real_password:
        print("Wrong password. The crystal stays sealed.")
        return None
    hero = {"name": name, "hp": int(hp_text), "gold": int(gold_text)}
    print(f"Welcome back, {hero['name']}!")
    return hero


def new_game():
    print("\n--- New Game ---")
    name = input("Name your hero: ").strip()
    gold = get_valid_gold("Starting gold (0-100): ")
    hero = {"name": name, "hp": 30, "gold": gold}
    save_hero(hero, input("Choose a save password: "))
    return hero


# --- the hardened menu itself ---
print("=== The Crypt of Broken Keys — Hardened Menu ===")
hero = None
while hero == None:
    choice = get_menu_choice()
    if choice == "1":
        hero = new_game()
    elif choice == "2":
        hero = load_hero()
    else:
        print("Farewell, adventurer.")
        break

if hero != None:
    print(f"\n{hero['name']} enters the crypt with {hero['gold']} gold and {hero['hp']} HP.")
```
