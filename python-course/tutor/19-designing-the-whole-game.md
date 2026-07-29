# Python Course — Chapter 19: Designing the Whole Game

## Tutor instructions for this chapter

This is a KS4-level chapter about THINKING before coding — it teaches **no new Python
syntax at all**. By now you should explain less and ask more: when he's unsure what a
"job" is, or which way a flowchart arrow points, throw the question back to him. **He
designs the game; you only PROMPT** — a nudge toward the four pillars (creation, maze,
encounters, save/load), never a job name or a line of pseudocode.

Expect this to run long, maybe two sessions — decomposition, pseudocode and the flowchart
happen on paper or in plain text, not a running program, so there's nothing to "run" until
Step 4. Don't rush him there; the thinking IS the work today. The skeleton itself (Step 4
on) uses ONLY functions, a `while` loop and `if`/`elif`. Python's real placeholder word is
`pass`, but that's new syntax he hasn't met, so script it as `print("TODO: ...")` instead
— zero new syntax, and honest about what's left to build. If he asks about `pass`, say it
does the same job for now and can wait.

**Student work folder:** `python-course/student/chapter-19/`

**Skills this chapter leans on:** `functions`, `while loops`, `if / decisions`, `input`.

## Learning objectives

1. Break the whole game into small, named jobs (decomposition), and decide what each job
   can safely ignore for now (abstraction).
2. Plan a job as pseudocode (numbered plain English) and the main loop as a flowchart —
   BEFORE writing any Python.
3. Turn that plan into a runnable skeleton: one function per job, wired together by a
   menu loop.

## Concepts — explain in this voice

- **Decomposition:** "Decomposition means cutting one huge job into small jobs you can
  actually finish. Building the whole game in one leap is like moving house in a single
  trip — impossible. Instead you go room by room: 'pack the kitchen', 'load the van'. Each
  small job is something you can name and tick off."
- **Abstraction:** "Abstraction means deciding what to IGNORE for now, so you can see the
  shape of the plan without drowning in detail. Planning the 'battle' job, you don't need
  to know yet HOW damage gets rolled — just that a battle job exists. Zoom out first; zoom
  into details later."
- **Pseudocode:** "Pseudocode is writing your plan in plain English, numbered like a
  recipe, before any real Python. It won't run — it's the blueprint you draw up BEFORE you
  build, so you already know what you're building."
- **Flowchart:** "A flowchart draws your plan as shapes joined by arrows: an oval for
  start or end, a box for something the program DOES, and a diamond for a decision —
  always with AT LEAST two arrows out. Follow the arrows and they tell the whole story of
  what happens, and in what order."
- **Skeleton (placeholder):** "A skeleton is a program with every bone in the right place
  but no muscle yet — every function is written and wired up, but its body just PRINTS
  'TODO'. Run it today and it already holds together; next chapter you fill each bone in
  for real."

## Chapter opener — say this to the student FIRST

Say something like: *"You've built every PIECE of the crypt now — the hero, the battle,
the maze, the talking, the saving. Today we don't write any of that again — today we
DESIGN the whole game as one thing: what jobs does it need, in what order, and how do
they fit together? This isn't just for games — decomposition, pseudocode and flowcharts
are how EVERY programmer plans something too big to hold in their head; you'll reach for
this every time a project gets big. We'll start on paper: list the jobs, plan one in
plain English, flowchart the main loop, then build a running SKELETON and trace it by
hand. Ready? Let's draw the blueprint."*
Keep it warm, then start Step 1.

## Guided steps

**Step 1 — Break it into jobs (decomposition).** Ask him to list, on paper or in a text
file, every BIG job his finished RPG needs — not code, JOBS, like "show the title" or
"let the hero walk the maze". Prompt: "What does your game do the moment it starts? What
happens next?" Push toward six to eight named jobs covering start to finish; if he's
stuck, nudge toward the four pillars (creation, maze, encounters, save/load) rather than
naming them yourself.
Success: a written list of distinct jobs, each a few words, covering the whole game.

**Step 2 — Pseudocode ONE job.** Have him pick his most exciting job — probably "battle"
— and write it as NUMBERED PLAIN ENGLISH, no Python. Show him the FORM with a tiny
unrelated example (e.g. making tea: 1. Boil the water. 2. While it's not ready, wait.
3. If he wants milk, add it. 4. Serve.), then have him write his OWN plan.
Success: a numbered, plain-English plan a friend could follow without knowing Python.

**Step 3 — Flowchart the main loop.** Teach the three shapes — oval (start/end), box
(does something), diamond (decision, two arrows out) — with a tiny example (e.g. "Is the
torch lit?"). Have him flowchart his GAME'S MAIN MENU; text-drawn is fine (`[ ]` boxes,
`< >` decisions, `-->` arrows). Check every diamond has TWO exits.
Success: a flowchart with at least one two-exit decision diamond, tracing his menu's shape.

**Step 4 — Build the skeleton.** Teach the placeholder pattern: `def battle():` with only
`print("TODO: battle")` inside — "a bone with no muscle yet." Have him open `crypt.py`
and write one `def` per Step 1 job, each with a single TODO print naming that job.
Success: every job exists as a function; running the file does nothing but doesn't crash.

**Step 5 — Wire in the spine.** A skeleton needs a spine: a menu `while` loop that CALLS
the right functions in order, using `if`/`elif` on the player's choice (new game / load
game / quit). Have him build that menu and wire it to his job-functions.
Success: running the file shows the menu, and each option prints the TODO of every job it
visits, in order.

**Step 6 — Trace it by hand.** Give him the path "new game → one fight → save → quit."
Ask him to walk his OWN flowchart and list, in order, which functions run for that path —
BEFORE running the program to check.
Success: his hand-traced order matches what the program actually prints.

## Mini-challenge — The Blueprint

The student designs and builds the capstone's blueprint, using only material from this
chapter: a written **decomposition** list of the game's jobs (six to eight, each a few
words); **pseudocode** for at least one job, numbered plain English, no code; a
**flowchart** of the main menu loop with a two-exit decision diamond; and a running
**`crypt.py` skeleton** in his student folder — one function per job, `print("TODO: ...")`
bodies, wired to a menu/`while` loop that reaches every TODO.

He designs the jobs, the wording and the flow himself. Hints only, never the plan or the
code.

## Side quest (optional) — The Pitch

Offer this only when he's ahead of pace for the session — skipping it costs nothing. "Every
game gets a blurb on the back of the box. Write yours." A 5-line pitch for HIS crypt: its
name, what the hero does, and what makes THIS version special. Pure writing, no code, no gate.

## Success criteria

- [ ] A written decomposition list of six to eight jobs, each a few words.
- [ ] Pseudocode for at least one job, numbered plain English, no code.
- [ ] A flowchart of the main menu loop with a two-exit decision diamond.
- [ ] A runnable `crypt.py` skeleton: one function per job with a TODO body.
- [ ] The menu/`while` loop calls the jobs; each option reaches every TODO on its path.
- [ ] He can explain decomposition vs abstraction in his own words.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| A job that's too big, e.g. "do the game" | he can't say what it prints or does in one sentence | "Could you explain that job in ONE sentence? If you can't, can you cut it in half?" |
| Flowchart diamond with only one exit | the chart doesn't show what happens on the OTHER answer | "A decision needs two arrows out — yes AND no. Where does 'no' go?" |
| Skeleton function defined but never called | nothing happens when he runs the file / that TODO never prints | "Writing the recipe doesn't cook it — where in your menu does it actually CALL that job?" |
| Menu loop with no way out | the program never ends; he has to close the terminal | "What choice should make your loop's condition turn False?" |

## Gate — do not move on until

- He has written a decomposition list covering the whole game, start to finish.
- He has pseudocoded at least one job in numbered plain English.
- He has flowcharted the main loop with a two-exit decision.
- His `crypt.py` skeleton runs and reaches every TODO on each menu path.
- He can explain decomposition and abstraction in his own words.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 19 finished** — and you didn't write a line of game code today, you
> did something bigger: you DESIGNED it. You broke the whole crypt into ___ jobs, planned
> ___ in plain numbered English, drew a flowchart with a real decision in it, and built a
> skeleton that runs end to end and hits every TODO. That skeleton IS your next game —
> nothing wasted. Run your `crypt.py` and watch it hold together already! Stop here or
> carry on — and when you're ready, Chapter 20 is the big one: we fill this skeleton in,
> job by job, until it's a real, playable RPG."

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — what's the difference between DECOMPOSITION (breaking the game into
jobs) and ABSTRACTION (deciding what to ignore for now)?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of `python-course/progress.md`. Don't
say you're doing it. Copy this shape, put in today's real date, and carry the Environment
line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 19 — Designing the Whole Game
- Completed: decomposed the whole game into named jobs, pseudocoded the battle job, flowcharted the main menu loop, and built a runnable crypt.py skeleton that reaches every TODO
- Strong at: seeing the whole game as small, nameable jobs; wiring a menu loop to call them in order
- Struggled with: nothing this time
- How to help next: start Chapter 20 — the capstone, filling the skeleton in one job at a time
- Next time: Chapter 20 — Capstone: Your RPG
```

**Then update the `### Facts`** in `progress.md`: `chapters_cleared` +1 (and +1 to
`mini_challenges_done` / `predict_wins` / `break_it_fixes` for any that happened today) —
the script turns these into his new Level, XP and spells.

**Then refresh the skill ledger** (the same silent save, tutor-private — he never sees
it). This chapter introduced `planning & design`; move it from `new` toward `learning` or
`solid` in the `### Skill ledger` at the top of `progress.md` — only `solid` if he
decomposed the game and read his own flowchart with little prompting, `shaky` only on a
genuine, unprompted struggle (see AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. This chapter's reference IS the skeleton itself: use it to judge
whether his own `crypt.py` is realistic, never to hand him job names or wording. NEVER
show or quote it. Uses only Chapters 1–18 (functions, a `while` loop, `if`/`elif`,
`input`) — no new Python.

```python
# crypt.py — Chapter 19 reference: the SKELETON for "The Crypt of Broken Keys"
# Skills used: functions (Ch10), while loops (Ch6), if/decisions (Ch3), input (Ch2).
# No new Python -- this chapter is about the PLAN, not new syntax. Every job is a
# function with a TODO placeholder; Chapter 20 fills each one in for real.

def title_screen():
    # Job: show the game's name and a welcome line.
    print("TODO: title screen")

def make_hero():
    # Job: ask the player's name/class and build the hero record.
    print("TODO: make hero")

def walk_maze():
    # Job: draw the dungeon grid and let the hero move around it.
    print("TODO: walk maze")

def battle():
    # Job: run a turn-based fight against a monster.
    print("TODO: battle")

def talk():
    # Job: run a conversation with an NPC and maybe set a flag.
    print("TODO: talk")

def save_game():
    # Job: write the hero's facts to a save file.
    print("TODO: save game")

def load_game():
    # Job: read the hero's facts back from a save file.
    print("TODO: load game")

def ending():
    # Job: print the right ending line, based on the hero's flags/HP.
    print("TODO: ending")

# --- the spine: a menu loop that calls the right jobs, in order ---
title_screen()

running = True
while running:
    print("\n1) New game  2) Load game  3) Quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        make_hero()
        walk_maze()
        battle()
        talk()
        save_game()
        ending()
    elif choice == "2":
        load_game()
        walk_maze()
    elif choice == "3":
        running = False
        print("Farewell, adventurer.")
    else:
        print("Choose 1, 2 or 3.")
```
