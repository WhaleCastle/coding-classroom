# Chapter 2 — Variables & Input

## Tutor instructions for this chapter

One step per message. Wait for the student's result each time. Never write his
code. Begin by asking him to run his `about_me.py` from Chapter 1 once — a quick
warm-up and memory refresh.

**Student work folder:** `python-course/student/chapter-02/`

## Learning objectives

1. Store information in a variable and use it later.
2. Get text from the user with `input()`.
3. Mix variables into messages with f-strings.

## Concepts — explain in this voice

- **Variable:** "A variable is a labelled box. You put something in the box and
  stick a name on it. Later, you ask for the box by name and Python hands you
  what's inside. `name = "Marcus"` puts the text Marcus into a box labelled name."
- **input():** "`input()` makes your program stop and wait for the user to type
  something. Whatever they type goes into your box."
- **f-string:** "An f-string is a message with holes in it. You write `f` before
  the quotes, and `{boxname}` where you want Python to pour in what's inside the
  box."

## Guided steps

**Step 1 — Warm-up.** Ask him to run `about_me.py` from Chapter 1. Quick chat:
what does print do? What are the quotes for?

**Step 2 — First variable.**
New file `boxes.py` in the chapter-02 folder. Ask him to:
make a variable holding his name, then print the variable (no quotes around the
variable name in print!).
Predict-then-run: "What will appear?"
Success: his name prints, and he can say why there are no quotes inside print.

**Step 3 — Quotes vs no quotes.**
Ask him to print the same word WITH quotes: `print("name")` vs `print(name)`.
Run both. Discuss: quotes = the literal text; no quotes = open the box.
Success: he explains the difference in his own words.

**Step 4 — Changing the box.**
Ask him to give the variable a NEW value on a later line, and print it before
and after. Predict-then-run.
Success: he sees the box's contents can change — that's why it's called a
*variable* (it varies!).

**Step 5 — input().**
New file `greet.py`. Ask him to:
make a variable that gets its value from `input("What is your name? ")`,
then print a hello message using it.
Teach the shape: variable = input("question "). Let him assemble it.
Success: program asks, he types, it greets.

**Step 6 — f-strings.**
His Step 5 print probably looks clunky. Show the f-string *concept* with a
DIFFERENT example (e.g. about a pet: `f"My pet is called {pet}"`), then ask him
to upgrade his greeting to an f-string.
Success: greeting uses `f"...{name}..."` and runs.

**Step 7 — Two inputs.**
Ask him to add a second question (favourite food, hobby — his choice) and make
one final sentence that uses BOTH variables in one f-string.
Success: one sentence, two holes, both filled correctly.

## Mini-challenge — Greeting Bot

New file `greeting_bot.py`. The bot must:
- ask at least 3 questions (name + 2 of his choice)
- reply with at least 2 sentences that use the answers (f-strings)
- have some personality — he decides the bot's style (polite? cheeky? robot-y?)

He plans the questions first (ask him to TELL you the 3 questions before
coding). Then he builds it. Hints only.

## Success criteria

- [ ] He can explain "labelled box" back to you in his own words.
- [ ] `greet.py` works with input + f-string.
- [ ] Greeting Bot asks 3 questions and uses all answers in its replies.
- [ ] He can answer: "What's the difference between `print("name")` and
      `print(name)`?"

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint |
|---|---|---|
| Quotes around variable in f-string `{"name"}` | literal odd output | "Inside the curly brackets, Python wants the box's name, not text in quotes." |
| Forgot the `f` before the quotes | `{name}` prints literally | "Your message printed the hole instead of filling it. What letter tells Python this string has holes?" |
| Spaces in variable name | `SyntaxError` | "Box labels can't contain spaces. Programmers use the underscore _ instead." |
| Variable used before created | `NameError: 'x' is not defined` | "Python reads top to bottom. Did you ask for the box before you made it?" |
| = vs == confusion (may appear early) | varies | "One = means PUT INTO the box. (Two == comes later — it means compare.)" |

## Gate — do not move to Chapter 3 until

- Greeting Bot works fully.
- He can predict the output of a 3-line variable program BEFORE running it
  (test him with a tiny example you describe in words — he writes & runs it to
  check his prediction).

## End of chapter

Specific praise, progress block, he updates `progress.md` himself.
