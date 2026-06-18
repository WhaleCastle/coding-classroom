# Python Course — Overview (for the tutor)

A year-long course for a Year 8 student, complete beginner. No previous coding
experience assumed. **The whole course builds ONE game: a text-mode RPG called
*The Crypt of Broken Keys*.** Every chapter adds the next slice of that game, so
the student always finishes a session with something that works and that he wants
to keep playing.

By the end he will have written — himself, by hand — character creation, a
dungeon maze, combat and conversation encounters, and a story that branches into
good and bad endings. In doing so he practises **every programming requirement in
the UK Key Stage 3–4 Computer Science curriculum** (see the coverage map below).

## What kind of game this is

- **Text mode, in the terminal.** The hero is a data record; the maze is a grid
  of symbols printed to the screen (`#` wall, `@` hero, `E` enemy, `N` person,
  `D` door, `X` exit); combat, conversation and endings are all text. Everything
  the student writes is plain Python — no graphics library needed.
- **The maze is the spine.** Standing on a cell tells the game what's there →
  that triggers a fight, a conversation, or sets a story flag → at the exit, the
  flags decide which ending he sees. This is how all four "pillars" connect.
- **Graphics are a bonus, never a hurdle.** A drawn hero sprite (and an optional
  move-it-around demo) live in `tutor/assets/` as **pre-made files the student is
  given**. He can tweak their values for fun (optional bonus chapter B1) but is
  never asked to write graphics code — it's beyond KS3–4.
- **Live movement (Chapter 14) is two techniques, split by the asset rule.**
  Walking the maze "for real" needs: (a) **clear-screen** — wipe and re-draw each
  step so the `@` looks like it moves; this is simple and the student WRITES it (a
  tiny helper, `print("\n" * 50)`, or a one-line ANSI version handed to him); and
  (b) **single-key w/a/s/d input** (no ENTER) — this needs low-level, per-OS code
  (`msvcrt` on Windows, `termios` on Mac/Linux), is well beyond KS3–4 and not
  cross-platform-writable, so it is a **given helper**, `get_key()`. (It currently
  lives inline in `assets/demo_play.py`; when ch 14 is written, factor it into
  `assets/controls.py` so the student's own maze can reuse it.) The student
  imports it in ONE line — `from controls import get_key`, just like
  `import random` — and calls it; he never writes or reads its internals. A
  one-line import is easier to learn than low-level terminal code in his own file.

## How to use this course

- Each chapter is one file: `01-...md`, `02-...md`, and so on. Follow the chapter
  script **in order, one step at a time** — explain, ask him to do one small
  thing, wait for his result.
- Each chapter file ends with a **Reference solution** — the author's version of
  that chapter's task. It is YOUR private reference for shaping hints and judging
  his standard. **Never show it** (root `AGENTS.md` rules 10–11).
- The student saves his work in `../student/chapter-XX/`.
- Chapters get gradually harder. Never skip the gate conditions at the end of
  each chapter.
- **Keep it playable.** Every chapter ends by inviting him to RUN his game-so-far
  and enjoy it — name the concrete new thing he can do. There is also a pre-made
  **trailer**, `tutor/assets/demo_play.py` (pure text, no install): a 2–3 minute
  playable taste of the finished game — name a hero, walk a dungeon, fight a
  goblin, talk to a hermit, reach an ending. Offer it on day one ("here's where
  we're heading") and again after the combat chapter (6) and the maze chapter
  (14). He PLAYS it; he never reads it to learn from — it's a given asset, like
  the sprite.

## Curriculum map (the RPG, chapter by chapter)

20 core chapters + 2 optional bonuses. The "RPG piece" is what the student builds.

| # | Chapter | Core ideas (KS3–4) | RPG piece he builds |
|---|---------|--------------------|---------------------|
| 1 | Hero & Title Screen | `print()`, strings, run a `.py` in the terminal | Game title screen + intro text |
| 2 | Name Your Hero | variables, `input()`, f-strings | Ask hero name/class, greet him |
| 3 | The First Choice | `if`/`elif`/`else`, comparisons, indentation | A fork / locked-door choice |
| 4 | Stats & Damage | int vs float, casting, arithmetic `+ - * / // % **` | Roll stats; a damage calculator |
| 5 | Game Rules (True/False) | Boolean type, `and`/`or`/`not`, relational ops | Gate logic; "is the hero alive?" |
| 6 | The Battle Loop | `while`, counters, `break`, infinite-loop danger | Turn-based fight until HP hits 0 |
| 7 | Counting & Rolling | `for`, `range()`, loop variable, nested-loop intro | HP bar / dice roller |
| 8 | The Inventory | lists: create, `append`, remove, index, `len`, loop | Backpack: add/drop/show items |
| 9 | The Character Sheet | dictionaries (records): key/value, lookup, update | Hero as a record + creator (shows sprite) |
| 10 | Actions as Functions | `def`, parameters, calling, why-modular | `attack()`, `heal()`, `show_status()` |
| 11 | Functions that Answer | `return`, local vs global variables, modules | `roll_damage()`, `is_alive()`; refactor battle |
| 12 | Random Encounters | `import random`, `randint`, `choice` | Random damage + a random monster |
| 13 | Reading Commands | strings: len/index/slice/concat/case, `ord`+`chr`, convert | Command parser + secret-scroll cipher |
| 14 | The Dungeon Map | 2D lists (arrays), nested loops, coordinates, collision | The walkable maze (layout given): move with w/a/s/d, screen clears each step |
| 15 | Talking to Characters | nested selection, dict dialogue, story flags | NPC conversation; choices set flags |
| 16 | Save Your Adventure | files: open / read / write / close | Save & load the hero and progress |
| 17 | Bullet-proof the Game | validation, sanitisation, authentication, test data, trace tables, error types | Hardened menus + a save password |
| 18 | Find & Sort the Loot | linear search + bubble sort (others named only) | Search the backpack; sort a leaderboard |
| 19 | Designing the Whole Game | decomposition, abstraction, pseudocode, flowcharts | Game design doc + flowchart + skeleton |
| 20 | Capstone: Your RPG | combine everything | Playable RPG: creation + maze + encounters + multiple endings + save/load |
| B1 | *(Optional)* Draw Your Hero | read & tweak a given PIL program | Recolour / restyle the given sprite |
| B2 | *(Optional)* Monster Database | SQL via `sqlite3` | Store & query monsters/items in a table |

## KS3–4 coverage map (check nothing is missed)

Sources: National Curriculum *Computing programmes of study, KS3 & KS4*; AQA GCSE
CS 8525; OCR GCSE CS J277. Where a chapter teaches a thing, it's listed.

- **Variables, constants, assignment** → 2, 4
- **Data types (int, real/float, Boolean, char, string) + casting** → 4 (numbers),
  5 (Boolean), 1–2 + 13 (string/char)
- **Operators — arithmetic / relational / Boolean** → 4 / 3 / 5
- **Sequence, selection (incl. nested), iteration (`for` + `while`)** → 1, 3, 6,
  7, 15
- **Input / output** → 1, 2
- **1D arrays (lists)** → 8 ; **2D arrays** → 14
- **Records / dictionaries** → 9
- **String handling (length, index, slice, concat, case, `ord`/`chr`, convert)**
  → 13 (+ str↔number in 4)
- **Subroutines: functions & procedures, parameters, return, local/global** →
  10, 11
- **Random numbers** → 12
- **File handling (open/read/write/close)** → 16
- **Searching: linear (built) / binary (named only)** → 18
- **Sorting: bubble (built) / merge & insertion (named only)** → 18
- **SQL / databases** → B2 (optional)
- **Validation, authentication, defensive design, testing (normal/boundary/
  erroneous), trace tables, syntax vs logic vs runtime errors** → 17
- **Computational thinking: decomposition, abstraction, algorithms, pseudocode,
  flowcharts** → 19 (and practised throughout)

**Deliberately capped for a Year 8 reaching into KS4:** binary search and
merge/insertion sort are *explained and traced* but not implemented by the
student; SQL is optional; classes/OOP are not required (we use dict "records",
which is GCSE-aligned). This gives KS4 breadth without the cliff-edges.

## Difficulty rules (apply across the whole course)

- **Chapters 1–5:** tiny steps, lots of repetition, instant wins. Heavy scaffolding.
- **Chapters 6–13:** steps get bigger; the student should **predict what code will
  do before running it** ("What do you THINK will happen?"). Introduce one new
  idea per chapter, anchored in a game feature he wants.
- **Chapters 14–20:** the tutor explains less and asks more; the student plans
  small pieces himself, then builds. Still: hints, never solutions. These are the
  KS4-level chapters — budget 2–3 sessions each and watch for fatigue.
- A session is ~30–45 minutes; chapters may take several sessions. Slow and solid
  beats fast and confused. If a chapter proves too steep in the pilot, slow it,
  split it, or drop a "named-only" item — nothing downstream depends on the hard
  extras.

## Status

- Meta scaffolding (template, rulebook, this overview, assets/folders): in place.
- Chapters **1–8 written** (each with a runnable reference solution). 9–20 + the
  two bonuses still to come, in confirmed batches (see `CLAUDE.md` build order).
  Pilot the early chapters and the maze chapter; fold feedback back in.
