# Chapter 3 — Making Decisions

## Tutor instructions for this chapter

One step per message. This chapter introduces **indentation** — the #1 source of
beginner errors. Be extra patient. Expect this chapter to take 2 sessions.

**Student work folder:** `python-course/student/chapter-03/`

## Learning objectives

1. Use `if`, `elif`, `else` to make a program choose.
2. Use comparisons: `==`, `!=`, `<`, `>`.
3. Understand indentation: the indented lines BELONG to the if.

## Concepts — explain in this voice

- **if:** "Until now your programs did every line, always. `if` is a fork in the
  road: IF something is true, do these lines; otherwise skip them."
- **== vs =:** "One equals sign PUTS something in a box. Two equals signs ASK a
  question: are these two things the same? Putting vs asking."
- **Indentation:** "Python uses spaces at the start of a line to show which lines
  belong to the if — like an arrow saying 'these lines are inside'. Press Tab.
  When the indent stops, the if is over."
- **else / elif:** "`else` is the otherwise-road. `elif` (else-if) adds more
  forks: if not the first thing, maybe this second thing?"

## Guided steps

**Step 1 — Warm-up.** Run his Greeting Bot from Chapter 2. Ask: what does
input() do?

**Step 2 — First if.**
New file `decisions.py`. Ask him to:
ask "What is the magic word?" with input, then write an if that prints
"Correct!" only when the answer equals (==) a word he chooses.
Teach the shape: the `if` line ends with a colon `:`, the next line is indented.
Predict-then-run twice: once typing the right word, once a wrong word.
Success: prints only on the right word; silent on wrong.

**Step 3 — else.**
Ask him to add an `else:` that prints a funny "wrong!" message.
Run both paths again.
Success: every run prints exactly ONE of the two messages, and he can point at
which lines belong to the if and which to the else.

**Step 4 — The indentation experiment.**
Ask him to remove the indentation from the line under `if`, save, run, and READ
the error (`IndentationError`). Then fix it.
Explain: this error will visit him many times; now he knows its face.
Success: he broke it, read it, fixed it.

**Step 5 — Numbers and comparisons.**
New file `age_check.py`. Ask him to ask for an age and store it as a number:
teach that input() always gives TEXT, and `int(...)` wraps it to turn it into a
number (a box-converting machine). Then an if using `>=` :
13 or older → one message; else → another.
Success: works for 12 and for 14. Ask him: what happens if you type "twelve"?
Let him try → crash → explain that's Chapter 4 territory (handling it nicely).

**Step 6 — elif chain.**
Ask him to extend `age_check.py` to three roads, his choice of boundaries, e.g.
under 10 / 10–15 / over 15, each with its own message. Teach the elif shape.
Predict-then-run with three different ages.
Success: each age range gives its own message, only one message per run.

## Mini-challenge — Secret Password Gate

New file `password_gate.py`. The program must:
- ask for a secret password
- if exactly right → print a welcome + a "secret message" he invents
- if the CAPITALISATION is the only thing wrong → he won't be able to detect
  this yet; just let exact matching apply (the .lower() trick is Chapter 9 —
  if he asks, tell him it's coming!)
- if wrong → print a warning, and (stretch goal) ask ONE more time using a
  second if inside the else (nested — only if he's flying; otherwise skip)

He designs the messages and password. Hints only.

## Success criteria

- [ ] He can explain == vs = ("asking vs putting").
- [ ] He fixed an IndentationError himself.
- [ ] `age_check.py` works with an elif chain (3 roads).
- [ ] Password Gate works for right and wrong passwords.
- [ ] He can point at any line and say whether it's "inside the if" or not.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint |
|---|---|---|
| `=` instead of `==` in the if | `SyntaxError` | "Are you putting or asking here? Which one does the if need?" |
| Missing colon `:` | `SyntaxError: expected ':'` | "The if line ends with a special punctuation mark. Look at the error — Python even tells you which." |
| No indent under if | `IndentationError` | "Which lines belong to the if? How does Python show belonging?" |
| Comparing number input as text (`"15" > 13`) | `TypeError` | "input() gives you text. What machine turns text into a number?" |
| elif after else | `SyntaxError` | "else means 'every other case' — can anything come after every other case?" |
| Extra indent randomly | `IndentationError: unexpected indent` | "One of your lines is standing too far right. Which one?" |

## Gate — do not move to Chapter 4 until

- Password Gate fully works.
- He writes, from a description in words only ("ask for a colour; if it's your
  favourite say X, otherwise say Y"), a working if/else with NO syntax hints
  from you.
- He has fixed at least 2 indentation errors across the chapter by himself.

## End of chapter

Big milestone — programs that DECIDE. Specific praise, progress block, he
updates `progress.md`. Tell him Chapter 4 turns his computer into a calculator.
