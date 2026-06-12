# Chapter 1 — Hello, Python

## Tutor instructions for this chapter

Teach the steps below IN ORDER, one step per message. After each step, wait for
the student to do it and tell you what happened. Do not paste the whole exercise
at once. Do not write his code.

**Student work folder:** `python-course/student/chapter-01/`

## Learning objectives (max 3)

1. Run a Python file from the VS Code terminal.
2. Use `print()` to show text on the screen.
3. Understand what a "string" is (text in quotes).

## Concepts — explain in this voice

- **Python file:** "A Python file is just a text file full of instructions.
  Its name ends in `.py`. When you run it, Python reads it top to bottom and
  does what each line says — like following a recipe."
- **print():** "`print()` is Python's way of saying something out loud. Whatever
  you put inside the brackets and quotes appears on the screen."
- **String:** "Text inside quotes is called a *string* — think of letters strung
  together on a necklace. Python needs the quotes to know where the text starts
  and ends."

## Guided steps

**Step 1 — Make the folder and file.**
Ask the student to create a file called `hello.py` inside
`python-course/student/chapter-01/` (right-click the folder → New File).
Success: file exists and is open in the editor.

**Step 2 — First line of code.**
Ask him to type (himself, not copy-paste):
a print line that shows the text `Hello, world!`.
If he doesn't know how, teach the shape of it: the word `print`, round brackets,
quotes inside. Let HIM assemble it.
Success: the file contains a working print line.

**Step 3 — Run it!**
Teach: open the terminal (View → Terminal), then type `python hello.py`
(on some computers `python3 hello.py`). Make sure the terminal is in the right
folder — if not, teach `cd` with his actual path, one step at a time.
Success: `Hello, world!` appears in the terminal. Celebrate this — it's his
first ever program!

**Step 4 — Make it yours.**
Ask him to change the message to say hello to himself by name, save, and run
again. Point out: edit → save → run is the loop programmers repeat all day.
Success: his own message appears.

**Step 5 — Break it on purpose.**
Ask him to delete ONE quote mark, save, and run. Let him see the red error.
Explain: "Errors are not bad — they're Python telling you exactly where it got
confused. Every programmer sees hundreds of these a day."
Then ask him to fix it and run again.
Success: he saw an error, read it, and fixed it himself.

**Step 6 — Multiple lines.**
Ask him to add two MORE print lines (anything he likes), and predict the order
they will appear BEFORE running. Then run.
Success: he correctly predicted top-to-bottom order.

## Mini-challenge — "About Me" card

In a NEW file `about_me.py` (same folder), the student builds a card about
himself using only print lines. It should have:
- a top border line (like `==============`)
- at least 4 facts about him (name, age, favourite game, anything)
- a bottom border line

He designs it himself. You may show what a *border* idea looks like, but never
type his card for him.

## Success criteria (check before finishing the chapter)

- [ ] `hello.py` runs with no errors and prints his own message.
- [ ] He fixed a quote error by himself.
- [ ] `about_me.py` runs and shows a card with borders and 4+ facts.
- [ ] He can answer: "What do the quotes do?" (mark where text starts/ends)

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Missing quote | `SyntaxError: unterminated string` | "Python says the string never ended. Look closely at your quotes — count them." |
| Missing bracket | `SyntaxError` pointing near the line end | "Every opening bracket needs a friend. Does yours have one?" |
| Capital P in Print | `NameError: name 'Print' is not defined` | "Python is fussy about capital letters. Look at how you spelled print." |
| `python` not found in terminal | `command not found` | Try `python3` instead. If still failing, pause and ask Dad to check the install. |
| Running from wrong folder | `can't open file` | "The terminal is standing in the wrong room. Which folder is it in? (`pwd` shows you)" |

## Gate — do not move to Chapter 2 until

- He has run a file from the terminal at least 5 times in total.
- He fixed at least one error without you telling him the exact fix.
- The About Me card works.

## End of chapter

Praise something specific he did. Then output the progress block (see AGENTS.md)
and ask him to copy it into `python-course/progress.md`.
