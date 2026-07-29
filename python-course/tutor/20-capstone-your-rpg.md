# Python Course — Chapter 20: Capstone — Your RPG

## Tutor instructions for this chapter

This is it — the whole game, assembled. There is nothing new to TEACH here; every
idea already lives in Chapters 1–19 and the Chapter 19 skeleton. Your job changes
shape: from here on you are **review and hints only** — he plans, he types, he
debugs, he decides. Resist the urge to steer; ask what HE thinks a piece should do
before he writes it, and let him be wrong sometimes. Never write his code, same as
always.

Budget **3–4 sessions** and say so up front. Structure sessions as assembly
milestones, not lecture steps — this file's Guided steps map onto them:
**Session 1** — title screen, hero creation, the maze walkable end-to-end.
**Session 2** — the `E` and `N` symbols wired to real encounters.
**Session 3** — the locked door, both endings, save/load, hardening.
**Session 4** — full playthroughs and fixes. Still deliver ONE step per message and
wait for his result — "least-teaching" does not mean "unattended"; you're still
watching every result and still giving hints, just fewer unprompted lectures.

**This chapter doubles as the course's Final Boss** (see `00-course-overview.md`'s
boss table) — there is no separate `boss-07` file. The Gate below IS the test: a
full, witnessed playthrough reaching both endings. Passing it sets `game_complete:
yes`, and the sheet crowns him **Code Archmage** — the last title on his ladder.

If he still has his Chapter 19 skeleton file, work from that. If it's gone, have
him start a fresh `crypt.py` with the same eight empty functions plus a menu loop
— rebuilding that shape from memory is itself good practice.

**Student work folder:** `python-course/student/chapter-20/`

**Skills this chapter leans on:** `print / strings`, `running a file in the terminal`,
`variables`, `input`, `f-strings`, `if / decisions`, `comparisons`,
`numbers & arithmetic`, `booleans & logic`, `while loops`, `for loops`, `lists`,
`dictionaries`, `functions`, `return values`, `random`, `string handling`,
`2D lists`, `dialogue & flags`, `file handling`, `defensive design`, `search & sort`,
`planning & design`. Every one of these gets used today. Skim the ledger before you
start — anything marked `shaky` is worth ten seconds of "remember when we did
this?" before he leans on it again, but don't turn it into a re-lesson.

## Learning objectives (max 3)

1. Assemble every earlier piece — creation, maze, combat, dialogue, a locked door,
   save/load — into ONE working game, filled into his own Chapter 19 skeleton.
2. Wire the maze's map symbols to the right encounters and read/set flags so two
   genuinely different endings are reachable depending on his choices.
3. Explain, in his own words, how any one piece of his finished game actually works.

## Concepts — explain in this voice

- **Integration:** "You've forged every piece of this sword separately — the
  hilt, the blade, the edge. Today you weld them into ONE weapon. Integration
  means taking pieces that already work on their own and wiring them together so
  they work as a single program. Your skeleton's functions stop being lonely
  stubs and start actually calling each other."
- **The skeleton becomes the game:** "Every `def` you wrote in Chapter 19 was a
  promise — 'the battle will happen here'. Today you keep every promise. When the
  last `print(\"TODO...\")` is replaced with real code, the skeleton and the
  finished game are the same file."
- **Playtesting:** "A game isn't done when it runs without crashing — it's done
  when you've actually PLAYED it, start to finish, more than once, on purpose
  trying different choices. That's playtesting: you become your own first
  player, hunting for the path nobody's walked yet."

## Chapter opener — say this to the student FIRST

Say something like: *"Every piece is built. Your hero, your dungeon, your monsters,
your hermit, your locked door, your save crystal — Chapters 1 through 19 already
taught you every single one. Today we don't learn anything new. Today we WIRE IT
ALL TOGETHER into one finished game: **The Crypt of Broken Keys**, your version,
playable start to finish, with two different endings only your choices can decide.
This is a bigger skill than it looks — every real program, every app, every game
you'll ever build is made of small working pieces bolted together exactly like
this; you'll do this again and again for the rest of your coding life. This will
take a few sessions, so here's the plan: first we get the title, your hero and a
walkable maze running together. Then we wire your monster and your hermit into the
map. Then the locked door, both endings, and saving your progress. Then we play
it — really play it — start to finish, more than once. From here on, YOU drive; I'm
just watching, cheering, and nudging. Ready to finish your crypt?"* Then start
Step 1.

## Guided steps

**Step 1 — Session 1: Gather your skeleton and assets.** Have him open his
Chapter 19 skeleton (or start a fresh `crypt.py` with the same eight empty
functions and a menu loop if it's gone), in `student/chapter-20/`. Have him copy
`maze_layout.py` and `controls.py` in from `tutor/assets/` again, next to it — same
copy-in as Chapter 14. Ask him to list out loud what each skeleton function is
FOR before touching any of them.
Success: the folder has his skeleton plus both asset files, and it still runs,
even if every function just prints a TODO line.

**Step 2 — Session 1: Fill in `title_screen()` and `make_hero()`.** Ask what his
title should say — his crypt, his words. Then bring back Chapter 9's hero record:
name, class, stats, built from his own `input()`. No forward planning needed here;
this is the easiest piece, a good warm-up for the session.
Success: running the file shows his title and builds a real hero record from what
he types.

**Step 3 — Session 1: Fill in `walk_maze()` and actually walk it.** Bring back all
of Chapter 14: draw the grid with nested loops, track `(row, col)`, move with
w/a/s/d (his own `input()` version, or `get_key()` if he wants no-ENTER play),
check the target cell BEFORE moving so walls block him. This is the biggest step
of the session — let it take the rest of the time.
Success: **Session 1 milestone.** Running his file shows the title, builds a hero,
and lets him walk his maze on screen with walls actually blocking him. That's a
real, working slice — say so before you stop for the day.

**Step 4 — Session 2: Wire the `E` symbol to `battle()`.** When `walk_maze` steps
onto an `E`, it should call `battle()`, built on his Chapter 11/12 helpers —
`roll_damage()` returning random damage, `is_alive()` driving the fight. A monster
should step out of a roster with `random.choice`, same as Chapter 12.
Success: walking onto `E` starts a real fight with random damage each time, and
that square doesn't fight him again once it's over.

**Step 5 — Session 2: Wire the `N` symbol to `talk()` and a flag.** A short
conversation, at least one choice, and one path that sets a flag on the hero
record (`hero["has_key"]` or his own name for it) — same shape as Chapter 15.
Success: **Session 2 milestone.** Talking to his person can change the flag,
provably — have him print it before and after, or run the conversation twice
choosing differently each time.

**Step 6 — Session 3: The door, two endings, save/load, hardening.** The biggest
session — pace it across several short exchanges rather than one huge push:
(a) the `D` symbol only lets him through if the flag from Step 5 is set, blocked
otherwise; (b) `ending()` reads the flag (and HP) and prints one of at least TWO
different texts; (c) `save_game()`/`load_game()` genuinely work, guarded — a
missing or broken save file must not crash the game (`try`/`except`, Chapter 16/17);
(d) harden the menu and any number prompt with validation and `try`/`except
ValueError`, then deliberately throw silly input at everything — letters where a
menu number goes, nonsense where a direction goes, gibberish at the hermit.
Success: **Session 3 milestone.** The door respects the flag, two different runs
print two different endings, saving then reloading really works, and nothing he
types anywhere crashes the game.

**Step 7 — Session 4: The full playthrough.** Predict-then-run, twice: before each
run, ask which ending he expects given the choices he's about to make, THEN play
it out. Reach each ending at least once, across separate runs. Fix whatever breaks
along the way — that's normal, not a failure.
Success: both endings witnessed with you watching, and he can point to the exact
line in his code that decided which one happened.

## Mini-challenge — The Crypt of Broken Keys (his version)

This chapter's mini-challenge IS the finished game. Assembled from his skeleton and
everything he's built, his `crypt.py` must have:
- a title screen;
- character creation that builds a hero record from his own input;
- a walkable maze (the given layout, or his own redesign) with working collision;
- at least one combat encounter using random damage through functions;
- at least one conversation encounter that sets a flag;
- a locked door that only opens for the right flag;
- save and load, guarded against a missing or broken save file;
- at least TWO different endings, decided by his flags and/or HP at the exit;
- and it must survive silly input everywhere it asks for something.

He designs the exact flavour, names and dialogue himself. Hints only, never the
code.

## Side quest (optional) — The Dungeon Master's Cut

Offer this only if he's cruising ahead of pace in Session 3 or 4 — skipping it
costs nothing and doesn't touch the mini-challenge. Say something like: *"Want to
add one flourish that's entirely YOUR idea?"* Requirements:
- it uses only concepts he already has — nothing from beyond Chapter 19;
- it doesn't break any of the required features above;
- he can explain what it does and why he added it.

Ideas if he's stuck for one: a tiny shop before the dungeon that spends his gold,
a second monster wave, a hidden room reachable only one way, a running score
printed with the ending.

## Success criteria (check before finishing the chapter)

- [ ] A title screen prints when the game starts.
- [ ] Character creation builds a hero record from his own input.
- [ ] The maze is walkable; walls block movement; the map redraws as he moves.
- [ ] At least one combat encounter uses random damage through functions.
- [ ] At least one conversation encounter sets a flag that later code reads.
- [ ] The locked door only opens when the right flag is set.
- [ ] The game saves and loads the hero, guarded against a missing/broken save.
- [ ] Reaching the exit gives one of at least TWO different endings, decided by
      his flags and/or HP.
- [ ] The game survives silly input everywhere it asks for something, without
      crashing.
- [ ] He can explain, in his own words, how one piece of his choice actually
      works.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Wrote `battle()`/`talk()` but never called them from `walk_maze()` | walking onto `E` or `N` does nothing | "Which function is supposed to run the moment the hero lands on that symbol — and where does your code actually CALL it?" |
| The flag change doesn't stick | the door stays locked even after he "got" the key | "Is the dictionary you changed in `talk()` the SAME one the door check reads afterwards, or a copy?" |
| `ending()` checks branches in the wrong order | he always sees the same ending no matter what he chooses | "Walk through your `if`/`else` by hand for a run WITHOUT the flag set — which branch does Python actually take?" |
| A number prompt crashes on text | `ValueError: invalid literal for int() with base 10` | "Which chapter taught you a safety net for exactly this kind of crash? Where could it wrap this line?" |
| Loads before anything's ever been saved | `FileNotFoundError` traceback | "What's true about the save file the very first time the game has ever been run?" |
| Re-fighting or re-talking the same square | the `E` or `N` cell triggers again every time he walks back onto it | "Once that event has happened, is the square still an enemy or a person — or should your code change what's there?" |

## Gate — do not move on until

- The whole game runs start to finish with no crash, on at least one full
  playthrough you witnessed.
- BOTH endings have been reached by him, across separate runs (not necessarily
  the same run).
- Save and load genuinely work — he can prove it: save, quit, relaunch, load,
  same hero comes back.
- Silly input has been thrown at the menu, at least one number prompt, and
  movement — nothing crashed.
- He can explain one piece of his own game, in his own words.

Only once every line above is true: record `game_complete: yes` in the `### Facts`
block of `progress.md`.

## End of chapter

Once the Gate above is met, this is the biggest finish of the whole course —
deliver it as the finale it is.

**Say this** — one warm message; swap the blanks for what he actually built:

> "___, this is it — **THE CRYPT OF BROKEN KEYS IS COMPLETE**, and you built the
> whole thing with your own two hands: the title screen, ___'s character sheet, a
> real dungeon you can walk, a fight decided by real dice, a conversation that
> changes the story, a door that only opens for the worthy, a save crystal that
> remembers him, and TWO different endings that exist only because of choices
> YOU coded. That is a finished game. Go show it to your family — hand someone the
> keyboard and watch them play YOUR crypt. And this earns you the very last title
> on your journey: you are now a **Code Archmage**. There's no 'next chapter' —
> only two optional epilogues whenever you feel like more: Bonus 1 lets you
> recolour your hero's sprite, and Bonus 2 teaches you a first taste of real
> databases for a monster bestiary. But right now? Go play your game."

Before you treat the chapter as done, ask: *"Pick ONE piece of your game — the
battle, the door, the endings, anything — and tell me in your own words how it
actually works."* and wait for his answer.

**Then save his progress** — add a block to the TOP of `python-course/progress.md`.
Don't say you're doing it. Copy this shape, put in today's real date, and carry
the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 20 — Capstone: Your RPG
- Completed: wired his Chapter 19 skeleton into the full game — title, hero
  creation, the walkable maze, a combat encounter, a conversation encounter with
  a flag, the locked door, save/load, and two different endings — and completed
  full playthroughs reaching both
- Strong at: assembling separate pieces into one working program; predicting
  which ending a run would reach before playing it out
- Struggled with: nothing this time
- How to help next: none needed for the core course — offer Bonus 1 or Bonus 2
  whenever he wants more
- Next time: (optional) Bonus 1 — Draw Your Hero, or Bonus 2 — Monster Database
```

**Then update the `### Facts`**: `chapters_cleared` +1, `mini_challenges_done` +1,
`predict_wins` +1 for each correct predict-then-run guess in Step 7, and
`break_it_fixes` +1 for the hardening pass in Step 6 — and, because this chapter's
Gate is the whole game, also set **`game_complete: yes`**. The script turns all of
this into his final Level, XP, and — because of `game_complete` — the Code
Archmage title on his sheet.

**Then refresh the skill ledger.** This chapter introduces no new skill — instead,
look back over the ledger and nudge toward `solid` any skill still sitting at
`learning` or `shaky` that genuinely got real, unaided use while assembling this
game today (he touched nearly all of them). Leave anything he didn't actually
exercise today exactly as it was.

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and to judge his standard — never
paste it, quote it, or read it aloud. His version will look different in every
detail (his own names, dialogue, maze, class choices) and that's correct; what
matters is that the same pieces are present and wired together. This file is also
copied, unchanged, to `python-course/tutor/reference/rpg/crypt.py` as the
cumulative reference for the whole course. It has been run under Python 3 with a
full winning playthrough, a run reaching the other ending, and a run of nothing
but silly input at every prompt — all three completed with no crash.

```python
"""
crypt.py -- THE CRYPT OF BROKEN KEYS

Tutor-only reference solution for Chapter 20 (the capstone) -- and the
CUMULATIVE reference for the whole python-course: one complete run of the
RPG, assembled from every piece taught in Chapters 1-19. NEVER shown to the
student (root AGENTS.md hard rule 10) -- use only to shape hints and judge
his build. His game will differ in the details (names, dialogue, maze,
class choices) -- that's correct; what matters is the same pieces, wired
together: title screen, hero creation, a walkable maze, a combat encounter,
a conversation encounter, a locked door, save/load, and two endings.

Skills used, all earlier chapters, nothing forward-referenced: dictionaries
(9), functions + parameters (10), return values (11), random (12), 2D
lists + nested loops (14), nested if + dialogue dict + story flags (15),
file open/write/read/close (16), try/except ValueError + .strip() + input
validation (17).

Needs no asset file to run: the maze below is the SAME data as the given
tutor/assets/maze_layout.py, copied in as plain data so this file is
standalone. His own game instead writes `from maze_layout import MAZE`
after copying that asset in, exactly as Chapter 14 taught -- and Chapter
14's `controls.py` (`get_key()`) can replace the input()-based moves below
for real no-ENTER w/a/s/d play; this reference uses input() so it can be
tested with plain typed lines. Run: python3 crypt.py
"""

import random

# THE DUNGEON MAP (Chapter 14) -- a list of rows, read as maze[row][col].
WALL = "#"
FLOOR = "."
START = "@"
ENEMY = "E"
PERSON = "N"
DOOR = "D"
EXIT = "X"

MAZE_TEMPLATE = [
    "##########",
    "#@..#...E#",
    "#.#.#.##.#",
    "#.#...#N.#",
    "#.####.#.#",
    "#....D..X#",
    "##########",
]

def find_start(grid):
    """Nested for loop over the grid: return the [row, col] of '@'."""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == START:
                return [row, col]
    return [1, 1]

def clear_screen():
    # A cheap screen-wipe: push everything up out of view with blank lines.
    # In real play you'd call this after every step of walk_maze() so the
    # map redraws in the same spot (Chapter 14). Called only once here, at
    # the title, so a piped test run of this file stays easy to read.
    print("\n" * 50)

# SETUP -- title screen and hero creation (Chapters 1, 2, 4, 9).
def title_screen():
    clear_screen()
    print("=" * 44)
    print("     THE CRYPT OF BROKEN KEYS")
    print("=" * 44)
    print("A locked door. A wandering monster. A hermit with a riddle.")
    print("Somewhere below, the crypt still keeps its last key.\n")

def make_hero():
    """Ask the player's name and class, build the hero record (Ch 9)."""
    name = input("What is your hero's name? ").strip()
    if name == "":
        name = "Aldric"          # a friendly default -- never crash on blank input

    print("Choose a class: (1) Warrior  (2) Rogue")
    choice = input("> ").strip()
    if choice == "2":
        cls = "Rogue"
        hp = 24
        attack = 5
    else:
        cls = "Warrior"                      # anything but "2" -- a safe default
        hp = 30
        attack = 7

    hero = {
        "name": name, "cls": cls, "hp": hp, "max_hp": hp,
        "attack": attack, "gold": 0, "has_key": False,
    }
    print(f"\n{hero['name']} the {hero['cls']} enters the crypt. "
          f"HP {hero['hp']}/{hero['max_hp']}.\n")
    return hero

# COMBAT -- functions that answer, and real dice (Chapters 10, 11, 12).
MONSTERS = [
    {"name": "Goblin", "attack": 4, "hp": 12, "gold": 5},
    {"name": "Skeleton", "attack": 5, "hp": 10, "gold": 6},
    {"name": "Giant Rat", "attack": 2, "hp": 6, "gold": 2},
    {"name": "Cave Troll", "attack": 7, "hp": 20, "gold": 15},
]

def roll_damage(attacker):
    """RETURN a random hit built from the attacker's attack stat (Ch 11/12)."""
    low = max(1, attacker["attack"] - 2)
    high = attacker["attack"] + 2
    return random.randint(low, high)

def is_alive(fighter):
    """RETURN True while a fighter still has HP left (Ch 11)."""
    return fighter["hp"] > 0

def battle(hero):
    """A random monster steps out of the dark (Ch 12). Fight to the end."""
    picked = random.choice(MONSTERS)
    # Build a fresh dict field by field -- a copy, so the roster's own
    # monster record never gets hurt when we subtract HP from it below.
    enemy = {
        "name": picked["name"],
        "attack": picked["attack"],
        "hp": picked["hp"],
        "gold": picked["gold"],
    }
    print(f"A {enemy['name']} blocks the way! (HP {enemy['hp']})")

    while is_alive(hero) and is_alive(enemy):
        dmg = roll_damage(hero)
        enemy["hp"] -= dmg
        print(f"You strike the {enemy['name']} for {dmg}.")
        if not is_alive(enemy):
            break                              # it fell -- it doesn't get a last swing
        dmg = roll_damage(enemy)
        hero["hp"] -= dmg
        print(f"The {enemy['name']} hits back for {dmg}. (HP {max(hero['hp'], 0)})")

    if is_alive(hero):
        hero["gold"] += enemy["gold"]
        print(f"You defeated the {enemy['name']} and found {enemy['gold']} gold!\n")
        return True
    hero["hp"] = 0
    print(f"\n{hero['name']} has fallen in the dark...\n")
    return False

# CONVERSATION -- a dialogue dict and a story flag (Chapter 15).
HERMIT_LINES = {
    "1": "The hermit smiles: \"Kindness opens more doors than force, adventurer.\"",
    "2": "The hermit frowns: \"Then find your own way through the dark.\"",
}

def talk(hero):
    """The Hermit of the Crypt: answer kindly and he hands over the key."""
    print("\nAn old hermit blocks the path. \"Answer me true,\" he says,")
    print("\"and the rusty key to the far door is yours.\"")
    print("(1) Speak kindly and ask for his help.")
    print("(2) Demand the key.")
    choice = input("> ").strip()

    if choice == "1" or choice == "2":
        print(HERMIT_LINES[choice])
    else:
        print("The hermit waits, unimpressed. That wasn't an answer at all.")
        choice = "2"              # a silly reply counts as rude, not a crash

    if choice == "1":
        print("He presses a small rusty key into your hand.\n")
        hero["has_key"] = True    # the flag later code (the door, the ending) reads
    else:
        print("He turns away and says nothing more.\n")
        hero["has_key"] = False

# THE DUNGEON -- 2D list, nested loops, coordinates, collision (Chapter 14).

def draw_map(grid, pos):
    """Nested for loop: print every row, swapping the hero's cell for '@'."""
    for r in range(len(grid)):
        line = ""
        for c in range(len(grid[r])):
            line += START if [r, c] == pos else grid[r][c]
        print(line)

def walk_maze(hero):
    """Walk the crypt. Returns 'exit', 'quit' or 'dead'."""
    # A mutable copy we can edit as he explores -- for loop + append,
    # turning each row STRING into its own list of characters.
    grid = []
    for row in MAZE_TEMPLATE:
        row_chars = []
        for ch in row:
            row_chars.append(ch)
        grid.append(row_chars)

    pos = find_start(grid)
    grid[pos[0]][pos[1]] = FLOOR                  # the start square is just floor underneath

    print("Move with w (up) a (left) s (down) d (right). q saves and quits.\n")
    draw_map(grid, pos)

    while True:
        key = input("move> ").strip().lower()

        # Work out the TARGET square from the key -- one if/elif per
        # direction, same pattern as Chapter 14. Anything else stays put.
        if key == "q":
            return "quit"
        elif key == "w":
            target = [pos[0] - 1, pos[1]]
        elif key == "s":
            target = [pos[0] + 1, pos[1]]
        elif key == "a":
            target = [pos[0], pos[1] - 1]
        elif key == "d":
            target = [pos[0], pos[1] + 1]
        else:
            target = None

        if target == None:
            print("That's not a direction I know. Try w a s d, or q.")
        else:
            cell = grid[target[0]][target[1]]

            if cell == WALL:                      # check BEFORE moving -- collision (Ch 14)
                print("A solid wall. No way through.")
            elif cell == DOOR and not hero["has_key"]:
                print("The door is locked. You need a key.")
            else:
                pos = target                       # the move is allowed -- step onto it

                if cell == DOOR:
                    print("The rusty key turns. The door creaks open.")
                    grid[pos[0]][pos[1]] = FLOOR
                elif cell == ENEMY:
                    grid[pos[0]][pos[1]] = FLOOR   # this fight only happens once
                    if not battle(hero):
                        return "dead"
                elif cell == PERSON:
                    grid[pos[0]][pos[1]] = FLOOR   # this chat only happens once
                    talk(hero)
                elif cell == EXIT:
                    return "exit"

                draw_map(grid, pos)

# THE ENDING -- decided by his flags and HP (Chapters 5, 11, 15).
def ending(hero):
    print("\n" + "=" * 44)
    if hero["has_key"] and is_alive(hero):
        print(f"{hero['name']} unlocks the far door and finds the crypt's")
        print("hoard glittering in torchlight.       *** THE GOLDEN ENDING ***")
    else:
        print(f"{hero['name']} slips past the crypt's secrets and out into")
        print("daylight, alive but empty-handed.      *** THE NARROW ESCAPE ***")
    print(f"Final gold: {hero['gold']}")
    print("=" * 44 + "\n")

# SAVE CRYSTAL -- files (Ch 16), guarded against missing/bad data (Ch 17).
SAVE_FILE = "save.txt"

def save_game(hero):
    f = open(SAVE_FILE, "w")
    f.write(f"{hero['name']}\n")
    f.write(f"{hero['cls']}\n")
    f.write(f"{hero['hp']}\n")
    f.write(f"{hero['max_hp']}\n")
    f.write(f"{hero['attack']}\n")
    f.write(f"{hero['gold']}\n")
    f.write(f"{hero['has_key']}\n")
    f.close()
    print("The save crystal glows. Your progress is stored.\n")

def load_game():
    """Read the save file back into a hero dict. None if it can't be read."""
    try:
        f = open(SAVE_FILE)
        lines = []
        for line in f:
            lines.append(line.strip())
        f.close()
        hero = {
            "name": lines[0], "cls": lines[1],
            "hp": int(lines[2]), "max_hp": int(lines[3]),
            "attack": int(lines[4]), "gold": int(lines[5]),
            "has_key": lines[6] == "True",
        }
        print(f"The crystal remembers {hero['name']}. Welcome back.\n")
        return hero
    except FileNotFoundError:
        print("No save crystal found yet -- starting a new adventure.\n")
        return None
    except ValueError:
        print("The save crystal is cracked and unreadable -- starting fresh.\n")
        return None
    except IndexError:
        print("The save crystal is cracked and unreadable -- starting fresh.\n")
        return None

# THE MENU -- validated, safety-netted (Chapter 17).
def main_menu():
    while True:
        print("1) New Game   2) Load Game   3) Quit")
        raw = input("> ").strip()
        try:
            choice = int(raw)
            if choice in [1, 2, 3]:
                return choice
            print("That's not one of the choices. Try again.")
        except ValueError:
            print("Numbers only, please -- 1, 2 or 3.")

def main():
    title_screen()
    while True:
        choice = main_menu()
        if choice == 3:
            print("Farewell, adventurer.")
            return
        if choice == 2:
            hero = load_game()
        else:
            hero = make_hero()

        if hero != None:                          # None means nothing was loaded
            result = walk_maze(hero)
            if result == "exit":
                ending(hero)
                save_game(hero)
                return
            if result == "dead":
                print("Game over -- your crystal was not updated.\n")
                return
            if result == "quit":
                save_game(hero)
                print("Until next time, adventurer.\n")
                return
            # else: back to the top of the loop -- nothing to load, ask again

if __name__ == "__main__":
    main()
```
