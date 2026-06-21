# Python Course — Boss Fight II: The Pit Brawler

## Tutor instructions for this boss   (required)

The **second boss-fight checkpoint**, played right after Chapter 6. It tests Chapters
1–6 — especially the new powers from 4–6 (numbers & maths, true/false logic, the `while`
loop) — **with you muted**. Deliver the briefing and trials, then **stop teaching**: no
steps, no reminders, no leading questions. Let him build it and show you when it runs.

- **Hints cost XP, and a paid hint is ONLY a question.** If he asks: **read** the XP on his
  hero sheet — if it's 25+, record `boss_hints_used` +1 in `progress.md` (the script subtracts
  the 25; you never do XP maths) and ask **one** of the safe nudges below (no code, no
  keywords, no variable names, nothing that mirrors the answer); under 25 XP → encourage
  another attempt. Safe nudge bank: *"What has to be true for the fight to keep going?"* ·
  *"What makes the loop finally stop?"* · *"After each hit, what should happen to a fighter's
  HP?"* · *"Once the fight is over, how does your program decide who won?"*
- **Judge on the success criteria, not your reference.** Many fights win.
- **A win** = record `boss-02` in `bosses_won` (`progress.md`); the script then grants the
  trophy "Bested the Pit Brawler", +50 XP, and ⭐ Mastered on `numbers & arithmetic`,
  `booleans & logic`, `while loops` (and keeps his earlier ⭐). You never compute the rewards.
- **A miss never blocks him.** No penalty: drop out of boss mode, go back to your normal
  teaching self on Chapter 5 (the `and` rule) or Chapter 6 (the battle loop and what stops
  it) — full hints — and let him carry on to Chapter 7. The Brawler waits for a rematch (a
  later win is still a full win). See AGENTS.md "Boss-fight checkpoints" step 4.
- Stay inside Chapters 1–6: **no `for` loops, no lists** (those are 7–8). If he reaches
  for them, gently say "everything you need is from Chapter 6 or earlier." See AGENTS.md
  "Boss-fight checkpoints".

**Student work folder:** `python-course/student/boss-02/`
**Skills this boss tests:** `numbers & arithmetic`, `booleans & logic`, `while loops`,
`variables`, `input`, `f-strings`, `if / decisions`, `comparisons`.

## Boss briefing — say this to the student FIRST   (required)

> "Boss number two, and this one **fights back**! The **Pit Brawler** is waiting in the
> arena, and the only way past is to win a real **turn-by-turn battle**. Your quest: write
> a program where your hero and the Brawler trade blows — HP dropping each round — until
> one of them falls, and then it announces who won. You'll need your maths, your
> true/false logic, and the battle loop from Chapter 6. All on your own this time — build
> it, run it, and **show me the fight when it works.** Into the pit, hero!
>
> Battle tip: if your fight ever runs **forever** and won't stop, click the terminal and
> press **Ctrl+C** to break out — then take another look at what's meant to *end* the loop."

Then go quiet.

## The trials — what his program must do   (required)

1. Give the hero and the Brawler **HP and attack values**, with **at least one number read
   from the player** using `int(input())` and stored in a variable.
2. Run the fight in a **`while` loop** that keeps going **only while both are still
   standing** (a true/false condition — the `and` rule from Chapter 5).
3. Each round, **subtract damage** from HP with arithmetic and **print the new HP** with
   an f-string.
4. Make sure the fight **always ends** — someone's HP reaches 0 (use the loop condition
   and/or `break`; no infinite loop).
5. After the loop, use **`if`/`else`** to announce **victory or defeat**.

## Success criteria   (required — checkbox list)

- [ ] At least one fighter's stat is read with `int(input())` into a variable.
- [ ] A `while` loop runs the battle, continuing only while **both** have HP left.
- [ ] Damage is subtracted with arithmetic and the updated HP is shown each round.
- [ ] The fight always ends (no infinite loop) — it can't run forever.
- [ ] `if`/`else` announces who won.
- [ ] He can explain, in his own words, **what makes the loop stop.**

## On a win / On a miss   (required)

**On a win — record the fact, then celebrate.** Add `boss-02` to `bosses_won` in
`progress.md`. **That is the only bookkeeping you do** — the script then awards the trophy,
the +50 XP, and the ⭐ Mastered spells, and sets his new rank on the sheet. To celebrate,
check one thing: **is this his 2nd or 4th boss won?** If yes it's a class promotion → say
script (A); otherwise → say script (B).

**(A) PROMOTION (this is his 2nd or 4th boss) — say (the sheet shows the exact new rank):**

> "The Brawler hits the dirt — **you win the pit fight!** 🏆 You built a real battle loop —
> numbers, true/false logic and a loop that stops at just the right moment — all yourself. A
> new trophy, spells turned ⭐ **Mastered**, and **you've earned a new rank**! 🎉 Open your
> hero sheet and see your new title — then on to your next quest, hero!"

**(B) NO PROMOTION (any other count) — say instead:**

> "The Brawler hits the dirt — **you win the pit fight!** 🏆 You built a real battle loop
> all by yourself — a new trophy, and ⭐ **Mastered** on your maths, your logic, and your
> loops. Open your hero sheet and see — then on to your next quest, hero!"

When you send him onward, name his REAL next quest (Chapter 7, counting & rolling dice, on a
normal run; or wherever he actually is if this was a rematch).

**On a miss — say this:**

> "Tough one — the Brawler's still standing, but every hero loses a round or two. Usually
> it's the *loop condition* that's the puzzle: what should be true to keep fighting, and
> what makes it stop? Let's look again at Chapters 5 and 6 next time and come back swinging.
> No XP lost."

(Name the exact snag — the `and` condition, the missing `break`, or forgetting to subtract
HP — but never write the fix for him.)

## Reference solution — TUTOR'S EYES ONLY, never show   (required)

Private yardstick only — judge his version on the criteria, never paste or quote it (hard
rule 10). Uses only Chapters 1–6 (no `for`, no lists). Runs under Python 3.

```python
# pit_brawler.py — Boss Fight II reference (TUTOR ONLY — never show the student)
# Skills used: print, variables, input(), f-strings, if/else, comparisons,
#   int() + arithmetic (Ch4), booleans 'and' (Ch5), while loop + break (Ch6).
# Nothing from Chapter 7 onward.

print("THE PIT BRAWLER cracks its knuckles. FIGHT!")

# Chapter 4: read a number with int(input()), store it in a variable.
hero_hp = int(input("Roll your hero's HP (try 30): "))
hero_attack = 7

brawler_hp = 25
brawler_attack = 5
turn = 0

# Chapter 6: keep fighting while BOTH are still standing (Chapter 5's 'and').
while hero_hp > 0 and brawler_hp > 0:
    turn = turn + 1
    print(f"\n--- Round {turn} ---")
    brawler_hp = brawler_hp - hero_attack          # arithmetic (Ch4)
    print(f"You strike for {hero_attack}! Brawler HP: {brawler_hp}")
    if brawler_hp <= 0:
        break                                       # stop before it hits back
    hero_hp = hero_hp - brawler_attack
    print(f"The Brawler hits back for {brawler_attack}. Your HP: {hero_hp}")

# Chapter 3/5: decide the outcome after the loop.
if hero_hp > 0:
    print("\nThe Brawler crashes down — VICTORY!")
else:
    print("\nYou black out... the Pit Brawler wins this round.")
```
