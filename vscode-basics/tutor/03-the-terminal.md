# VS Code Basics — Chapter 3: The Terminal

## Tutor instructions

One step per message. This is the bridge to the Python course — by the end he
runs his first (one-line) Python program. Check progress.md for his OS.
Windows note: in the default VS Code terminal (PowerShell), `ls`, `pwd` and
`cd` all work, so teach those for everyone; mention `dir` exists on Windows.

**Student work folder:** `vscode-basics/student/chapter-03/`

## Learning objectives

1. Understand what the terminal is and why programmers use it.
2. Navigate: where am I (`pwd`), what's here (`ls`), move (`cd`).
3. Run a program, stop a program (Ctrl+C), clear the screen.

## Concepts — explain in this voice

- **Terminal:** "Clicking is like pointing at things. The terminal is like
  *speaking* to the computer — you type a command, press Enter, it obeys. It
  looks old-fashioned, but it's the most powerful room in the workshop."
- **The prompt:** "The line waiting for you is called the prompt. It usually
  shows WHERE you are standing — the terminal is always standing inside one
  folder."
- **cd:** "`cd` means change directory — walking from one folder into another.
  `cd ..` walks back OUT to the parent folder."

## Chapter opener — say this to the student FIRST

Before any step, set the scene. Say something like: *"Today you learn to **talk to
the computer directly** — through the terminal, the most powerful room in the
workshop. By the end you'll be able to move between folders and even run your very
first program! We'll start gently by just opening it and finding out where we are.
Ready?"* Keep it short and warm, then start Step 1.

## Guided steps

**Step 1 — Open it.** View → Terminal (or Ctrl/Cmd+`). Look at the prompt —
what folder does it show?
Success: terminal open, he reads the prompt aloud.

**Step 2 — Where am I? What's here?** Ask him to type `pwd` (print working
directory), then `ls` (list). Compare what `ls` shows to the Explorer — same
folders!
Success: he sees terminal and Explorer are two views of the same thing.

**Step 3 — Walking around.** Ask him to walk into the vscode-basics folder:
`cd vscode-basics`, then `ls`, then deeper into `student`, then `cd ..` back.
Teach the magic key: **Tab completes names** — type `cd vs` then Tab.
Let him wander for a few minutes: anywhere, then find his way back with `cd ..`
and `pwd`.
Success: he can get to `vscode-basics/student/chapter-03` and back to the top,
narrating with pwd.

**Step 4 — Clear the mess.** Screen full of text now. Teach `clear` (or
Ctrl+L). Explain: it only tidies the view; nothing is deleted.
Success: clean screen, no fear.

**Step 5 — Does this computer speak Python?** Ask him to type
`python --version` (if "not found", try `python3 --version`).
Explain: this asks the computer "do you have Python, and which version?"
Success: a version number appears. (If neither works, pause the lesson and ask
Dad to check the Python installation.)

**Step 6 — Stop a running program.** Ask him to type `python` alone and press
Enter — Python's own prompt `>>>` appears (the computer is now IN python-mode).
Then teach the emergency brake: Ctrl+C stops a running program... for the
Python prompt, type `exit()` and Enter. Try both: enter, exit, enter, exit.
Success: he can get out of anything. This kills the #1 beginner panic.

## Mini-challenge — First contact with Python

In the Explorer, he creates `hello.py` inside
`vscode-basics/student/chapter-03/`, types EXACTLY one line —
a print of any message he likes (give him the shape: print("...")) —
saves it, then in the terminal **walks to that folder with cd** and runs:
`python hello.py`
His message appears. Tell him: "That's it. That's programming. The Python
course starts from this exact moment."

## Success criteria

- [ ] Can navigate to any folder in the project and back, using cd / ls / pwd.
- [ ] Knows Tab-completion exists and used it at least once.
- [ ] Escaped the Python prompt by himself.
- [ ] `hello.py` ran from the correct folder and printed his message.

## Common mistakes & hints

| Mistake | Symptom | Hint |
|---|---|---|
| cd to a name with a typo | `no such file or directory` | "The computer only obeys EXACT names. Use ls to see the real name — or let Tab type it for you." |
| Running the file from the wrong folder | `can't open file` | "Where is the terminal standing right now? Where does the file live?" |
| Stuck inside `>>>` | typing commands that fail oddly | "Look at the start of the line — >>> means you're inside Python. How do we leave?" |
| Spaces in folder names breaking cd | error | "Names with spaces need quotes around them: cd \"my folder\"." |
| python vs python3 | not found | "Some computers call it python3. Try that." |

## Gate — course complete when

- The mini-challenge worked, run from the correct folder, first try or fixed by
  himself.
- He answers: "If a program goes crazy and won't stop, what do you press?"

## End of chapter

Big congratulations — the workshop is now HIS. Update `vscode-basics/progress.md`
yourself with a progress block (record anything he found tricky). Next session:
Python course, Chapter 1 (which will feel easy now — he has already run a Python
file!).
