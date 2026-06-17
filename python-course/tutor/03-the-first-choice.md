# Chapter 3 — The First Choice

## Tutor instructions for this chapter

One step per message. This chapter introduces **indentation** — the #1 source of
beginner errors. Be extra patient; expect it to take 2 sessions. Warm up by
running his Character Creator from Chapter 2.

Today the crypt gives the hero a real *choice* — a fork in the tunnel — and the
game does different things depending on what the player picks. This is the engine
of every decision and every ending later in the game. (We stick to *word* choices
like `left`/`right` here; comparing numbers comes next chapter.)

**Student work folder:** `python-course/student/chapter-03/`

## Learning objectives

1. Use `if`, `elif`, `else` to make the game choose what happens.
2. Compare text with `==` (same?) and `!=` (different?).
3. Understand indentation: the indented lines BELONG to the `if`.

## Concepts — explain in this voice

- **if:** "Until now your game did every line, always. `if` is a fork in the
  tunnel: IF something is true, do these lines; otherwise skip them."
- **== vs =:** "One equals sign PUTS something in a box. Two equals signs ASK a
  question: are these two things the same? `door == \"open\"` asks *is the door
  open?* Putting vs asking."
- **!= :** "`!=` is the opposite question: are these two things *different*?"
- **Indentation:** "Python uses spaces at the start of a line to show which lines
  belong to the `if` — like an arrow saying 'these lines are inside this fork'.
  Press Tab. When the indent stops, the fork is over."
- **else / elif:** "`else` is the otherwise-tunnel: do this when the `if` was not
  true. `elif` (else-if) adds more forks: if not the first thing, maybe this
  second thing?"

## Chapter opener — say this to the student FIRST

Before any step, set the scene. Say something like: *"So far your game does the
exact same thing every time you run it. Today it learns to make a **choice** — the
hero reaches a fork in the tunnel, and what happens next depends on what the player
picks. By the end you'll have a door that only opens for the right answer! We'll
build up one fork at a time. Ready?"* Keep it short and warm, then start Step 1.

## Guided steps

**Step 1 — Warm-up.** Run his Character Creator from Chapter 2. Ask: what does
`input()` do? What does an f-string do?

**Step 2 — The fork.**
New file `the_fork.py`. Ask him to greet the hero, then ask `Left tunnel or right
tunnel? ` with `input()` and store it. Then write an `if` that prints something
(treasure!) ONLY when the answer `== "left"`. Teach the shape: the `if` line ends
with a colon `:`, and the next line is indented.
Predict-then-run TWICE: once typing `left`, once typing `right`.
Success: it prints on `left`, stays silent on `right`.

**Step 3 — else.**
Ask him to add an `else:` that describes what's down the right tunnel instead. Run
both paths again.
Success: every run prints exactly ONE of the two outcomes, and he can point at
which lines belong to the `if` and which to the `else`.

**Step 4 — The indentation experiment (break it on purpose).**
Ask him to remove the indentation from the line under `if`, save, run, and READ
the error (`IndentationError`). Then fix it. Say: "This error will visit you many
times — now you know its face."
Success: he broke it, read it, fixed it.

**Step 5 — A third path with elif.**
Ask him to add a THIRD option to the question (e.g. `left` / `right` / `back`),
using `elif` for the middle case. Teach the elif shape (between `if` and `else`).
Predict-then-run with all three answers.
Success: each choice gives its own outcome; exactly one outcome per run.

**Step 6 — Same word, different case.**
Ask him to run it and type `Left` with a capital L. It falls through to `else`!
Discuss why: to Python, `"Left"` and `"left"` are different strings. Tell him
there's a neat trick to fix this fairly — and it's coming in a later chapter
(Chapter 13). For now, exact matching is fine.
Success: he can explain why `Left` didn't match `left`.

## Mini-challenge — The Locked Door

New file `locked_door.py`. The hero reaches a door with a riddle. The program must:
- ask the player for the **answer to a riddle** (he invents the riddle and the
  answer),
- if the answer is exactly right → the door opens and a short reward scene plays
  (his words),
- if it's wrong → a warning, and the door stays shut,
- have at least THREE outcomes somewhere in the game (use `elif`) — e.g. a right
  answer, a "close but wrong" answer, and everything else.

He designs the riddle, the answer, and the scenes. Hints only — never give him
the `if` lines.

## Success criteria

- [ ] He can explain `==` vs `=` ("asking vs putting") in his own words.
- [ ] He fixed an `IndentationError` himself.
- [ ] `the_fork.py` runs with an `if`/`elif`/`else` (three paths).
- [ ] The Locked Door works for a right answer and a wrong answer.
- [ ] He can point at any line and say whether it's "inside the if" or not.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint |
|---|---|---|
| `=` instead of `==` in the `if` | `SyntaxError` | "Are you *putting* or *asking* here? Which one does the `if` need — one equals or two?" |
| Missing colon `:` | `SyntaxError: expected ':'` | "The `if` line ends with a special punctuation mark. Read the error — Python even tells you which one is missing." |
| No indent under `if` | `IndentationError: expected an indented block` | "Which lines belong to the fork? How does Python show that a line is *inside* the `if`?" |
| Random extra indent | `IndentationError: unexpected indent` | "One line is standing too far to the right. Which one? Line it up with its neighbours." |
| `elif` after `else` | `SyntaxError` | "`else` means 'every other case'. Can anything come *after* every other case?" |
| Capital mismatch (`Left` vs `left`) | falls to `else` unexpectedly | "To Python, is `Left` the very same string as `left`? What's different about them?" |

## Gate — do not move on until

- The Locked Door fully works (right and wrong answers behave correctly).
- From a spoken description only ("ask for a colour; if it's your favourite say X,
  otherwise say Y"), he writes a working `if`/`else` with NO syntax hints from you.
- He has fixed at least 2 indentation errors across the chapter by himself.

## End of chapter

Big milestone — his game now *decides*. Praise something specific. **Play it:**
ask him to run his Locked Door a few times, trying the right answer and wrong ones,
and enjoy the game reacting differently to each choice. Update
`python-course/progress.md` yourself with a progress block (record any spots where
indentation or `==` tripped him up). Tease: next chapter the game learns to do
maths — hero stats, hit points and damage.

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and judge his standard. NEVER show or
quote it. His riddle, words and outcomes will differ — that's correct, as long as
it runs and has the three branches. Note: no numbers/`int()` here — that's Ch 4.

```python
# locked_door.py — Chapter 3 reference (tutor only)
# Skills used: input(), variables, f-strings, if/elif/else, == and !=. Nothing later.

hero = input("Your hero's name? ")
print(f"{hero} reaches a stone door carved with a riddle.")
print('Riddle: "I open every lock but the last. What am I?"')

answer = input("Your answer: ")

# == asks "are these the same?"  Exact text must match (Ch 13 will fix capitals).
if answer == "key":
    print("The door swings open. A golden key glints inside!")
elif answer == "keys":
    # a "close but not quite" branch shows off elif
    print("Almost... the door trembles but stays shut. Try the single word.")
else:
    print(f"Nothing happens. The door stays locked, {hero}.")
```
