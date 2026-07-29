# Python Course — Bonus Quest 2: Monster Database

## Tutor instructions for this chapter

This is an **optional quest** — offer it any time from Chapter 16 onward
(it assumes he's comfortable with the idea of saving data to disk; SQL's
`sqlite3` module IS Python's built-in file-based database, so this is a
natural next step after "Save Your Adventure"). Like Bonus 1, this whole
chapter is a self-contained side trip — there's no separate "Side quest
(optional)" section to look for here either.

**Unlike Bonus 1, no install is needed.** `sqlite3` ships inside Python
itself (unlike `PIL`/Pillow) — `import sqlite3` just works, nothing to `pip
install`. Worth saying to him: one less thing to set up today.

**What's given, and what's actually taught.** The Python PLUMBING —
`import sqlite3`, opening a connection, getting a cursor, calling
`.execute(...)`, `.fetchall()`, `.commit()`, `.close()` — is a **small,
copyable recipe you hand him directly**, the same way `open()`/`.close()`
was handed to him in Chapter 16. Don't make him invent it; script it, have
him type it, move on. **The SQL text INSIDE the quotes is what this chapter
actually teaches** — `CREATE TABLE`, `INSERT`, `SELECT ... WHERE ...`,
`SELECT ... ORDER BY ...`, and one `UPDATE`. Treat SQL as a small, separate
language living inside a Python string, not more Python syntax.

**The given recipe (script this to him near Step 1):**
```python
import sqlite3

conn = sqlite3.connect("bestiary.db")   # opens the archive file (creates it if missing)
cur = conn.cursor()                     # your "finger" for pointing at rows

cur.execute("...")                      # any SQL statement goes here as text
conn.commit()                           # actually saves any changes to disk

conn.close()                            # done for now
```
Every step below just changes what goes in the `"..."`.

**The data lives on disk (`bestiary.db`) and PERSISTS between runs** —
that's the whole point, unlike a list that resets every time the program
starts. Warn him up front: if he wants a clean slate, deleting `bestiary.db`
resets everything (there is no undo for that — say so plainly). Re-running
his script WITHOUT deleting the file will add the roster again on top of
what's already there (harmless, just duplicate rows) — that's expected, not
a bug, unless he deletes the file first.

**The classic "ran it twice" crash — teach it as a deliberate break-it
step, not something to dodge.** The first time he writes `CREATE TABLE
monsters (...)`, have him run the script, then run it again on purpose.
He'll hit `sqlite3.OperationalError: table monsters already exists`. That's
the moment to teach `CREATE TABLE IF NOT EXISTS monsters (...)` as the fix —
a guarding clause, the SQL equivalent of "only do this if it isn't already
done."

**Student work folder:** `python-course/student/bonus-02/`

**No new skill for the ledger.** SQL is optional and outside the tracked
skill list — don't add or move a ledger entry for it.

**Skills this chapter leans on:** `dictionaries`, `lists`, `for loops`,
`f-strings`.

## Learning objectives (max 3)

1. Use `sqlite3` to `CREATE TABLE`, `INSERT` rows, and `SELECT` them back out.
2. Narrow a `SELECT` with `WHERE` and order one with `ORDER BY`.
3. `UPDATE` an existing row, and say why a table beats a pile of loose
   dictionaries once there's a lot of related data to keep straight.

## Concepts — explain in this voice

- **A table is a ledger with labelled columns:** "Picture the crypt's old
  librarian keeping a big ledger book — one row per monster, and every row
  has exactly the same labelled columns: name, hp, attack, gold. No
  scattered notes on scraps of paper, one tidy ledger anyone can read the
  same way."
- **SQL — the ledger's own tiny language:** "SQL isn't Python — it's a small
  separate language just for talking to a table, and you write it as TEXT
  inside Python's `.execute("...")`. `CREATE TABLE` draws the columns,
  `INSERT` writes a new row, `SELECT` reads rows back out."
- **SELECT is asking the librarian:** "Every `SELECT` is a question you ask
  out loud — 'show me every monster that hits harder than 5' — and `WHERE`
  is how you narrow which rows get to answer. `ORDER BY` tells the librarian
  what order to read the answers back in."
- **UPDATE changes a row that's already there:** "`INSERT` writes a brand
  new line in the ledger. `UPDATE` finds a row that already exists and
  changes ONE of its columns — like the crypt keeper crossing out an old
  stat and writing in a new one after a monster gets nerfed."

## Chapter opener — say this to the student FIRST

Say something like: *"Today's quest is small but it's a real programmer's
tool: a DATABASE. Your game already has monsters — today we give the crypt
its own bestiary, a proper ledger stored in a file, that remembers itself
between runs without you writing a single line of save/load code by hand.
This isn't just for monsters — the moment any program has LOTS of related
things to track (players, scores, orders, messages), a table like this is
how real software does it, way beyond just games. We'll build the ledger,
stock it with monsters, then ask it a few real questions and even edit one
row after the fact. Ready to open the archive?"* Keep it warm, then start
Step 1.

## Guided steps

**Step 1 — Open the archive, draw the columns.** Have him create
`bestiary.py`, type the given recipe (import, connect, cursor), then fill in
the first `.execute(...)` with
`CREATE TABLE monsters (name TEXT, hp INTEGER, attack INTEGER, gold INTEGER)`,
followed by `conn.commit()`. Run it. Ask him to PREDICT: will anything print?
Success: nothing prints, but a new `bestiary.db` file appears in his folder —
the "magic moment", like Chapter 16's first file write.

**Step 2 — Break it on purpose.** Have him run the exact same script again,
unchanged. He'll see `sqlite3.OperationalError: table monsters already
exists`. Ask why Python is happy to run the SAME code twice but the ledger
isn't. Then have him change the statement to
`CREATE TABLE IF NOT EXISTS monsters (...)` and run it twice more to prove
it no longer crashes.
Success: he understands the crash, and `IF NOT EXISTS` stops it for good.

**Step 3 — Stock the bestiary.** Have him build a small Python list of
monster dictionaries (reusing Chapter 9's record shape — `name`, `hp`,
`attack`, `gold`), then loop over it with a `for`, calling
`cur.execute("INSERT INTO monsters VALUES (?, ?, ?, ?)", [m["name"], m["hp"], m["attack"], m["gold"]])`
for each one, then `conn.commit()`. Explain the `?` marks: placeholders the
real values slot into, safer than typing them straight into the SQL text.
Success: at least 4 monsters get inserted without error.

**Step 4 — Read the whole ledger back.** Have him
`cur.execute("SELECT * FROM monsters")`, then `cur.fetchall()` into a
variable and loop over it with a `for`, printing each row. Ask him to
PREDICT what shape each row will print in before running.
Success: every monster prints as a small row of values in brackets; he
recognises it as "one row per monster, in order."

**Step 5 — Ask the librarian two questions.** Have him write one `SELECT`
with `WHERE` (e.g. `SELECT name, attack FROM monsters WHERE attack > 5`) and
one with `ORDER BY` (e.g. `SELECT name, gold FROM monsters ORDER BY gold
DESC` for richest-first). PREDICT which monsters should answer each question
before running.
Success: both queries return sensible, correctly-filtered/ordered results.

**Step 6 — Nerf a monster (UPDATE).** Have him pick one monster and lower
its `attack` with
`cur.execute("UPDATE monsters SET attack = ? WHERE name = ?", [new_value, "Goblin"])`
followed by `conn.commit()`, then re-run his Step 5 `WHERE` query (or a fresh
one) to prove the change actually stuck in the ledger.
Success: the updated stat shows the new value on the next read — the change
survived, not just printed once.

## Mini-challenge — The Bestiary

In `bestiary.py`, the student builds his own crypt bestiary using only
`sqlite3` and this chapter's SQL. It must:
- `CREATE TABLE` (with `IF NOT EXISTS`) a `monsters` table with at least
  `name`, `hp`, `attack`, `gold`,
- `INSERT` at least FOUR monsters,
- ask the ledger at least THREE different questions in SQL, with AT LEAST
  one using `WHERE` and AT LEAST one using `ORDER BY`,
- `UPDATE` at least one monster's stat, proven by reading it back afterward.

He picks his own monster roster and questions. Hints only, never the SQL
text itself.

## Success criteria

- [ ] A `monsters` table exists (`CREATE TABLE IF NOT EXISTS`) and the
      script can be run more than once without crashing.
- [ ] At least four monsters are `INSERT`ed with name, hp, attack and gold.
- [ ] A `SELECT ... WHERE ...` answers a real question about the roster.
- [ ] A `SELECT ... ORDER BY ...` answers another real question.
- [ ] An `UPDATE` changes one monster's stat, and a follow-up `SELECT` proves
      it stuck.
- [ ] He can explain in his own words what a table is and what `WHERE` does
      to a `SELECT`.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Ran `CREATE TABLE` (without `IF NOT EXISTS`) a second time | `sqlite3.OperationalError: table monsters already exists` | "What word could you add to `CREATE TABLE` that means 'only if it isn't already there'?" |
| Forgot `conn.commit()` after an `INSERT` | he reopens the archive later and the new row is just gone | "Writing to the ledger and SAVING the ledger are two different steps — did you do both?" |
| Missing comma between `?` placeholders in an `INSERT` | `sqlite3.OperationalError: near "?": syntax error` | "Count the placeholders against the commas between them — do they match up?" |
| Compared a text column to an unquoted word (e.g. `WHERE name = Goblin`) | `sqlite3.OperationalError: no such column: Goblin` | "In SQL, text needs quotes around it, just like Python strings do — did you quote the monster's name?" |
| Misspelled a column name in `WHERE`/`ORDER BY` | `sqlite3.OperationalError: no such column: atk` | "What are the EXACT column names you typed when you `CREATE TABLE`d? Do they match here?" |

## Gate — do not move on until

- `bestiary.db` exists and the table was created with `IF NOT EXISTS`.
- At least four monsters have been inserted and can be read back with
  `SELECT`.
- He has written a working `WHERE` query and a working `ORDER BY` query.
- He has used `UPDATE` and proven the change stuck with a fresh `SELECT`.
- He can explain what a table and a `WHERE` clause are, in his own words.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's the **Bestiary built!** You created a real database table, stocked
> it with ___ monsters, asked it real questions with `WHERE` and
> `ORDER BY`, and even updated one after the fact — and it's all still
> sitting there in `bestiary.db`, waiting for you, even after the program
> ends. That's a genuine professional tool, the same shape real apps use to
> store thousands of things. This was the last of the two secret side
> quests this course offers — from here on, it's your crypt: keep playing
> it, keep adding to it, keep making it more YOURS. Fantastic work,
> adventurer."

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — what's a table, and what does `WHERE` do when you
`SELECT` from one?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put
in today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: Bonus 2 — Monster Database (optional quest)
- Completed: built a monsters table with sqlite3 — CREATE TABLE IF NOT EXISTS, INSERT, SELECT with WHERE and ORDER BY, and one UPDATE
- Strong at: writing SQL questions (WHERE, ORDER BY) once the recipe was in place
- Struggled with: nothing this time
- How to help next: pick his main quest back up wherever he left it
- Next time: <his real next chapter or boss, wherever he actually is>
```

**Then update the `### Facts`** in `progress.md`: this was an optional bonus
quest, so `chapters_cleared` does **NOT** change — bump only
`mini_challenges_done` +1 (and `break_it_fixes` +1 for fixing the "table
already exists" crash, and `predict_wins` +1 if his `WHERE`/`ORDER BY`
prediction was correct). The script turns these into his XP and spells; a
bonus quest still earns credit, it just isn't a numbered chapter.

**Skill ledger: leave it untouched.** This quest introduces no new tracked
skill, so there is nothing to move or add in the `### Skill ledger` block.

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and to judge his standard.
NEVER show or quote it. His roster and questions will differ — that's
correct, as long as the table exists, at least four monsters are inserted,
one `WHERE` and one `ORDER BY` query both work, and one `UPDATE` is proven
to stick. Reuses the roster shape and monster names from Boss IV (`name`,
`hp`, `attack`), adding `gold`. Uses only `sqlite3`'s given plumbing plus
dictionaries, lists, for loops and f-strings — nothing from Chapters 17–20 is
required.

```python
# bestiary.py -- Bonus Quest 2 reference (tutor only)
# Skills used: sqlite3 (given pattern), dictionaries, lists, for loops.
# The plumbing (connect/cursor/execute/commit/close) is copied straight from
# the recipe; the SQL strings inside execute() are what this quest teaches.

import sqlite3

# --- connect to the crypt's archive (creates bestiary.db if it isn't there yet) ---
conn = sqlite3.connect("bestiary.db")
cur = conn.cursor()

# --- draw the ledger's columns, but only if they aren't already drawn ---
# IF NOT EXISTS is the fix for the classic "run it twice" crash: without it,
# running this script a second time raises
# sqlite3.OperationalError: table monsters already exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS monsters (
        name TEXT,
        hp INTEGER,
        attack INTEGER,
        gold INTEGER
    )
""")
conn.commit()

# --- the crypt's roster, as records the game already knows how to build (Ch9) ---
monster_roster = [
    {"name": "Goblin", "hp": 12, "attack": 4, "gold": 5},
    {"name": "Skeleton", "hp": 16, "attack": 5, "gold": 8},
    {"name": "Giant Rat", "hp": 8, "attack": 3, "gold": 2},
    {"name": "Cave Troll", "hp": 24, "attack": 7, "gold": 15},
]

# The ? marks are placeholders -- the list after the SQL fills them in safely,
# so we never have to hand-type quotes around text values ourselves.
for m in monster_roster:
    cur.execute(
        "INSERT INTO monsters VALUES (?, ?, ?, ?)",
        [m["name"], m["hp"], m["attack"], m["gold"]],
    )
conn.commit()
# Note: running this whole script again (without deleting bestiary.db first)
# adds this roster a second time -- that's expected, not a bug; deleting the
# file is how you start the ledger fresh.

# --- ask the librarian a few questions ---

print("=== Every monster in the archive ===")
cur.execute("SELECT * FROM monsters")
for row in cur.fetchall():
    print(row)

print("\n=== Monsters tough enough to hit for more than 5 (WHERE) ===")
cur.execute("SELECT name, attack FROM monsters WHERE attack > 5")
for row in cur.fetchall():
    print(row)

print("\n=== Richest monster first (ORDER BY) ===")
cur.execute("SELECT name, gold FROM monsters ORDER BY gold DESC")
for row in cur.fetchall():
    print(row)

# --- the crypt keeper nerfs the Cave Troll after a balance patch (UPDATE) ---
cur.execute("UPDATE monsters SET attack = ? WHERE name = ?", [5, "Cave Troll"])
conn.commit()

print("\n=== Cave Troll after the nerf (proving the UPDATE stuck) ===")
cur.execute("SELECT name, attack FROM monsters WHERE name = ?", ["Cave Troll"])
for row in cur.fetchall():
    print(row)

conn.close()
print("\nSaved to bestiary.db -- delete that file any time you want a fresh archive.")
```
