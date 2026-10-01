# Python Course — Chapter 15: Talking to Characters

## Tutor instructions for this chapter

A boss follows this chapter — **Boss V, The Labyrinth Lord**. This means the
End-of-chapter teaser AND the progress block's `How to help next` / `Next
time` lines must point at that BOSS, not at Chapter 16. Get this right; if the
tutor reads "Chapter 16" next session it will skip the checkpoint.

Teach one step per message, wait for his result, never write his code. From
Chapter 14 onward explain less and ask more; he should be able to predict
which lines will run before you tell him.

Ceiling: everything in Chapters 1–14, plus **nested selection (an `if` inside
an `if`)** and **story flags**. No files (Chapter 16), no `try`/`except`
(Chapter 17), and no need to redraw the maze — this scene picks up right where
Chapter 14 left the hero: standing in front of the person marked `N` on the
map, about to reach the locked door `D`. He does not need to re-walk the grid
to build this chapter's program.

**The key new idea is the story flag.** A flag is just a `True`/`False` fact
tucked into the hero's dictionary (`hero["has_key"]`), set by ONE piece of
code and read by a completely different piece of code later — that's new,
and worth being explicit about: "the record remembers, even after the
conversation that set it is long over."

**Student work folder:** `python-course/student/chapter-15/`

**Skills this chapter leans on:** `dictionaries`, `if / decisions`,
`booleans & logic`, `input`, `f-strings`.

## Learning objectives (max 3)

1. Nest an `if` inside another `if` and predict which lines run for a given
   path through it.
2. Store dialogue lines in a dictionary and look up a reply by the player's
   choice.
3. Set a story flag in the hero record now, and have different code read it
   later to change what happens.

## Concepts — explain in this voice

- **Nested selection (a fork inside a fork):** "You already know `if` is a
  fork in the road. A **nested if** is a fork that only APPEARS once you've
  already taken one branch of an earlier fork — a second decision, hidden
  inside the first. You show Python it's nested the same way you show
  anything is inside a block: another level of indentation."
- **Story flag (a light-switch in the record):** "Some facts about your hero
  aren't numbers, they're switches: ON or OFF, `True` or `False`. `hero["has_
  key"] = False` starts the switch OFF. Later — maybe minutes of gameplay
  later — some other bit of code can flip it ON, and ANY code after that can
  check it. The record remembers the switch long after the moment that
  flipped it."
- **Dialogue dictionary:** "Instead of a pile of `if choice == "egg": ... elif
  choice == "key": ...`, you can store every possible reply in ONE dictionary,
  keyed by the choice itself, and look it up: `replies[choice]`. Same trick as
  looking up a hero's `hp` — just this time the 'record' is a script."
- **Consequence:** "A good story remembers. The choice you make with the
  hermit today can change a locked door you haven't even reached yet — because
  the flag it set is still sitting in the hero record, waiting to be read."

## Chapter opener — say this to the student FIRST

Say something like: *"You can WALK your dungeon now — today you make it
TALK back. An old hermit is waiting on your map, and how you treat him will
matter LATER: a choice you make right now can unlock a door you haven't even
reached yet. That's the trick of a **story flag** — a switch the game
remembers long after the conversation that flipped it. And this isn't just
for one hermit: any time a choice needs to be remembered for later — a shop
that trusts you, a guard who recognises you, a secret you found — you'll
reach for exactly this pattern. We'll build it in order: first the flag
itself, then a real conversation with a choice, then a FOLLOW-UP question
nested inside it, then a whole line of dialogue stored in a dictionary, then
the reward, and finally a door that opens or doesn't depending on what you
chose. Ready? Someone's waiting for you in the dark."* Keep it warm, then
start Step 1.

## Guided steps

**Step 1 — A flag of your own.** New file (e.g. `hermit.py`) in `student/chapter-15/`. Have him build a small hero record with a flag switched off: `hero = {"name": "Aldric", "has_key": False}`. Have him write an `if hero["has_key"]:` / `else:` that prints a different line for each, and run it once with the flag `False`.
Success: he sees the `else` branch run because the flag starts `False`; he can say what a flag is in his own words.

**Step 2 — The first exchange.** Teach a real choice. Have him print an NPC line (`print("Hermit: \"I've had nothing but crusts for a week.\"")`), read a choice with `input()`, and write a plain `if`/`else` that prints a different reply for "yes" vs anything else.
Success: both replies are seen (run it twice, once per answer); the choice visibly changes what prints.

**Step 3 — Nest it: a follow-up question.** Have him put a SECOND question INSIDE the "yes" branch only — e.g. a riddle the hermit asks — with its own `input()` and its own `if`/`else` for right/wrong. Before running, ask him to PREDICT: if he answers "no" at Step 2, does the riddle even get asked?
Success: the riddle only appears down the "yes" path; the doubled indentation is visibly correct; his prediction is checked.

**Step 4 — A dialogue dictionary.** Teach storing several replies in ONE dictionary keyed by the possible answers, e.g. `RIDDLE_REPLIES = {"egg": "...", "key": "...", "promise": "..."}`, then looking the player's answer up in it (`RIDDLE_REPLIES[answer]`) instead of a chain of `elif`s. Have him check the answer IS a key in the dictionary before looking it up (`if answer in RIDDLE_REPLIES:`) — otherwise a typo would crash the lookup.
Success: the right reply prints for each possible answer, from ONE dictionary lookup rather than several `elif`s.

**Step 5 — The reward: set the flag.** Have him find the ONE correct branch (the right riddle answer) and add `hero["has_key"] = True` there — nowhere else. Ask him to PREDICT what `hero["has_key"]` will be if he answers wrong or says "no" at Step 2, then check it by printing the record.
Success: the flag is `True` on exactly the winning path and stays `False` on every other path.

**Step 6 — The door reads the flag.** Have him write the door scene: an `if hero["has_key"]:` that prints an "opens" message, `else:` a "locked" message — completely separate code from Steps 2–5, reading a flag that was set earlier. Run it once each way (change the flag by hand first if it's faster than replaying the whole conversation) to see both endings.
Success: both endings are seen; he can explain that the door never "knows" about the conversation — it only reads the flag.

## Mini-challenge — The Hermit's Riddle

Using only this chapter and earlier ones, the student writes the FULL
hermit encounter in one program. It must:
- greet the player and offer at least TWO choice points, one of which is
  NESTED inside the other (a follow-up that only appears down one branch),
- store at least one set of replies in a dialogue DICTIONARY, looked up by
  the player's choice,
- set a story flag (e.g. `hero["has_key"]`) on exactly the path that earns it,
- end with a door scene that reads the flag with an `if`/`else` and prints
  TWO genuinely different endings depending on it.

He designs the hermit's words and the riddle himself. Hints only, never the
code.

## Side quest (optional) — The Grudge

Offer this only when he's ahead of pace — it costs nothing to skip. Pitch:
"What if the hermit remembers being INSULTED, too?" Requirements:
- add a second flag, `hero["hermit_angry"]`, starting `False`,
- give the player a way to insult the hermit (a choice that sets it `True`),
- have the door scene's WORDING change when `hermit_angry` is `True`, even if
  the ending (locked/open) stays governed by `has_key`.

## Success criteria (check before finishing the chapter)

- [ ] A story flag is created in the hero record, starting `False`.
- [ ] A conversation has at least two choice points, with one `if` nested
      inside another.
- [ ] A dialogue dictionary stores replies, looked up by the player's choice.
- [ ] The flag is set to `True` on exactly one (correct) path, and nowhere
      else.
- [ ] The door scene is separate code that reads the flag and shows two
      different endings.
- [ ] He can explain in his own words what a story flag is and why the door
      still "remembers" a choice from earlier.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Nested `if` indented at the wrong level | it runs even when it shouldn't, or a `IndentationError` | "Which earlier `if` is this question supposed to belong to? How far in should a line be to sit INSIDE that branch?" |
| Looked up a choice that isn't in the dialogue dict | `KeyError: 'maybe'` | "Which keys does your dictionary actually have? What could you check BEFORE looking the answer up?" |
| Set the flag in the wrong branch | door opens even on the "wrong" path, or never opens at all | "Walk through your own code path by path — on WHICH exact line does `hero[\"has_key\"] = True` sit? Is that really the winning branch only?" |
| Used `=` instead of `==` in a check | `SyntaxError`, or the flag gets overwritten instead of compared | "Is this line ASKING 'are these equal?' or TELLING Python 'make these equal'? Which symbol means which?" |
| Door scene reads the flag before it's ever set | door always looks locked, even on the winning path | "In what ORDER does your program run — does the conversation happen before or after you check the door?" |

## Gate — do not move on until

- He has a hero record with at least one story flag.
- He has written a nested `if` (an `if` inside another `if`'s branch) and
  correctly predicted which lines would run.
- He has looked something up in a dialogue dictionary.
- He has met (and fixed) a `KeyError` from an unchecked dictionary lookup, OR
  can explain how to avoid one.
- His door scene shows two different endings depending on the flag.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 15 finished!** Your dungeon TALKS now — you built a real
> conversation with the hermit, nested a follow-up question inside it, stored
> his lines in a dialogue dictionary, and set a story flag that your door
> scene reads to give you TWO different endings. Play it through both ways —
> earn the key, then try it without. And now your fifth **boss** awaits: the
> **Labyrinth Lord**, who won't let you pass until you build a small maze of
> your OWN, with a character and a flag-driven ending — completely unaided,
> no steps from me. Face it now, or stop here and take it on next session?"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — what's a story flag, and how does the game 'remember'
it after the conversation that set it is over?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put
in today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 15 — Talking to Characters
- Completed: built the hermit conversation — nested if, a dialogue dict, a story flag (has_key) set on the winning path, and a door scene with two flag-driven endings
- Strong at: nested selection; reading and setting flags in the hero record
- Struggled with: nothing this time
- How to help next: run Boss V — The Labyrinth Lord (Chapters 1–15 checkpoint, tutor muted)
- Next time: Boss V — The Labyrinth Lord (then Chapter 16)
```

**Then update the `### Facts`** in `progress.md`: `chapters_cleared` +1 (and
+1 to `mini_challenges_done` if he did it; `predict_wins` / `break_it_fixes` were already counted
the moment each happened) — the script turns these into his new Level, XP and spells.

**Then refresh the skill ledger** (the same silent save, tutor-private — he
never sees it). This chapter introduced `dialogue & flags`; in the `### Skill
ledger` at the top of `progress.md`, move it from `new` toward `learning` or
`solid` — only `solid` if he built the nested if and the flag largely unaided,
`shaky` if the nesting or where-to-set-the-flag kept tripping him up (see
AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and to judge his standard.
NEVER show or quote it. His hermit, riddle and wording will differ — that's
correct, as long as there's a nested `if`, a dialogue dictionary, a flag set
on exactly the winning path, and a door scene with two real endings. It reuses
the running hero record and picks up narratively right where Chapter 14 left
the hero — no maze code needed. No files (Chapter 16), no `try`/`except`
(Chapter 17).

```python
# hermit.py — Chapter 15 reference (tutor only)
# Skills used: dictionaries, nested if, booleans, f-strings, input.
# Nothing later: no files (Ch16), no try/except (Ch17).

hero = {
    "name": "Aldric",
    "cls": "warrior",
    "hp": 30,
    "max_hp": 30,
    "attack": 7,
    "has_key": False,       # a story flag: starts OFF, like a light switch
    "hermit_angry": False,  # side-quest flag: also starts OFF
}

# Replies to the hermit's riddle, stored once and looked up by answer.
RIDDLE_REPLIES = {
    "egg": "The hermit shakes his head. \"Close... but no.\"",
    "key": "The hermit's eyes light up. \"YES. A key must be TURNED before it opens anything.\"",
    "promise": "The hermit smiles sadly. \"True enough — but not the answer I need.\"",
}

print(f"An old hermit blocks the path, {hero['name']}.")
print("Hermit: \"I've had nothing but crusts for a week. Share your rations with me?\"")

choice = input("Share your rations? (yes/no): ").strip().lower()

if choice == "yes":
    print("Hermit: \"Kind soul. Answer me this, and the key behind me is yours...\"")
    print("Hermit: \"What must be broken before you can use it?\"")

    # NESTED if: this whole riddle only exists because choice was "yes" above
    # — a fork that only appears once you've already taken the first fork.
    answer = input("Your answer (egg/key/promise): ").strip().lower()

    if answer in RIDDLE_REPLIES:          # check the key exists before looking it up
        print(RIDDLE_REPLIES[answer])
        if answer == "key":               # the ONE winning branch, nested again
            hero["has_key"] = True
            print("The hermit presses a rusty key into your hand.")
    else:
        print("Hermit: \"...that's not even a word I know.\"")

else:
    print("Hermit: \"Selfish, like all the others.\"")
    grudge = input("Insult him back? (yes/no): ").strip().lower()
    if grudge == "yes":
        hero["hermit_angry"] = True
        print("The hermit's face darkens. He will remember this.")

# --- the door scene: separate code, reading flags set minutes ago ---
print()
print("=== THE LOCKED DOOR ===")

if hero["has_key"]:
    print("You slide the rusty key into the door. It grinds open.")
    if hero["hermit_angry"]:
        print("A cold draft follows you through — some things aren't forgiven so easily.")
    else:
        print("Beyond it, torchlight and the smell of fresh air. You press on.")
else:
    print("The door is locked tight, and you have no key.")
    if hero["hermit_angry"]:
        print("Somewhere behind you, the hermit laughs. You'll have to find another way.")
    else:
        print("You'll have to find another way round — or another way to earn his trust.")
```
