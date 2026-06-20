# Python Course — Boss Fight I: The Gate Guardian

## Tutor instructions for this boss   (required)

This is the **first boss-fight checkpoint**, played right after Chapter 3. It tests
everything from Chapters 1–3 — **with you muted**. Deliver the briefing and the trials,
then **stop teaching**: no steps, no concept reminders, no leading questions, no "have
you tried…". Let him build it alone and ask him to show you when it runs.

- **Hints cost XP, and a paid hint is ONLY a question.** If he asks: 25+ XP → for 25 XP
  ask **one** of the safe nudges below (no code, no keywords, no variable names, nothing
  that mirrors the answer); under 25 XP → cheer him to try again. Safe nudge bank:
  *"Which line decides what the Guardian says back?"* · *"How does your program tell one
  answer apart from another?"* · *"Where do you keep the player's reply so you can check
  it?"* · *"What should happen for a *wrong* answer — and where would that go?"*
- **Judge on the success criteria below, not on your reference.** Many programs win.
- **A win** = +50 XP, Level +1, the trophy "Slew the Gate Guardian", and ⭐ Mastered on
  `print / strings`, `variables`, `input`, `f-strings`, `if / decisions`, `comparisons`.
- **A miss never blocks him.** No penalty: drop out of boss mode, go back to your normal
  teaching self on Chapter 2 (name/f-strings) or Chapter 3 (if/elif/else) — full hints —
  and let him carry on to Chapter 4. The Guardian waits for a rematch (a later win is still
  a full win). See AGENTS.md "Boss-fight checkpoints" step 4.
- Stay strictly inside Chapters 1–3: no numbers/`int()`, no loops, no `and`/`or`. If he
  reaches for those, gently say "you won't need anything past Chapter 3 here." See
  AGENTS.md "Boss-fight checkpoints".

**Student work folder:** `python-course/student/boss-01/`
**Skills this boss tests:** `print / strings`, `variables`, `input`, `f-strings`,
`if / decisions`, `comparisons`.

## Boss briefing — say this to the student FIRST   (required)

> "Time for your **first boss**, hero! A stone **Gate Guardian** blocks the only path
> onward — and it only opens for someone clever. Your quest: write a little program
> where the Guardian learns your hero's name, asks a riddle, and then **reacts
> differently** depending on the answer — opening the gate for the right one and turning
> away the wrong one. This one's all you — I won't be giving steps. Use everything from
> Chapters 1 to 3. Build it, run it, and **show me when it works.** Good luck!
>
> One fair warning from the Guardian: **computers are exact.** If your code checks for a
> certain word, the player has to type it *exactly* that way — capital letters and all —
> or it won't count. (That's just how `==` works for now; Chapter 13 teaches the trick to
> forgive capitals.)"

Then go quiet.

## The trials — what his program must do   (required)

1. Ask for the player's **hero name**, store it in a variable, and **greet him by name**
   using an f-string.
2. Have the Guardian **ask a question**, and read the player's answer into a variable.
3. Use **`if` / `elif` / `else`** with **at least three branches** to react to the answer,
   deciding with a **comparison** (`==` or `!=`).
4. Make the outcomes **clearly different**: the right answer opens the gate; a wrong
   answer is turned away — different messages print for different answers.
5. Use the hero's **name in at least one of the reactions** (another f-string).

## Success criteria   (required — checkbox list)

- [ ] Running it asks for the hero's name and greets him by name with an f-string.
- [ ] The Guardian asks a question and the answer is stored in a variable.
- [ ] An `if`/`elif`/`else` with three or more branches reacts using a comparison.
- [ ] The right answer visibly **opens the gate**; a wrong answer is visibly **turned
      away** (the output really changes with the answer).
- [ ] He can explain, in his own words, **what decides which message appears.**

## On a win / On a miss   (required)

**On a win — say this** (swap the blanks):

> "The gate grinds open — **you beat the Gate Guardian!** 🏆 Your program greeted the
> hero, asked its riddle, and chose its reply all on its own — that's real code, written
> by *you*, no help. You've earned the trophy **Slew the Gate Guardian**, **+50 XP**, and
> you're now **Level ___** — and six of your spells just turned ⭐ **Mastered**. Want to
> see your character sheet? Then onward to Chapter 4, where your game learns *maths*."

Then update `hero-sheet.md` (XP, level, trophy, ⭐ skills) and show it off.

**On a miss — say this:**

> "So close, hero — the Guardian's still standing, but that's no shame; bosses are meant
> to be tough. The trick is in how the answer *decides* the reply — let's revisit
> Chapter 3 next time and come back for the rematch. No XP lost; the gate will wait."

(Point him at the exact thing that tripped him — Chapter 2 for names/f-strings, Chapter 3
for the `if`/`elif`/`else` — without writing any of it for him.)

## Reference solution — TUTOR'S EYES ONLY, never show   (required)

Private yardstick only — judge his version against the success criteria, never paste or
quote this (hard rule 10). Uses only Chapters 1–3 (no numbers, no `int()`, no loops, no
`and`/`or`, no `.lower()` — exact-text matching, exactly as Chapter 3 teaches; Chapter 13
is where capitalisation gets handled). Runs under Python 3.

```python
# gate_guardian.py — Boss Fight I reference (TUTOR ONLY — never show the student)
# Skills used: print, strings, variables, input(), f-strings, if/elif/else, == / !=.
# Nothing from Chapter 4 onward.

print("=" * 30)
print("   THE GATE GUARDIAN")
print("=" * 30)

# Chapter 2: ask the hero's name, store it, greet him with an f-string.
name = input("State your name, traveller: ")
print(f"\nThe Guardian's stone eyes open. \"{name}... we shall see if you are worthy.\"")

# Chapter 3: the Guardian poses a riddle and reads the answer.
print("\nGuardian: \"What has keys, but opens no doors?\"")
answer = input("Your answer: ")

# Chapter 3: react with if / elif / else, deciding with a comparison.
if answer == "piano":
    print(f"\nThe gate swings wide. \"Pass, {name}. You have a true hero's wit.\"")
elif answer == "keyboard":
    print(f"\n\"A clever guess, {name} — but not my answer. The gate stays shut.\"")
else:
    print(f"\nThe Guardian folds its arms. \"No, {name}. Return when you are wiser.\"")
```
