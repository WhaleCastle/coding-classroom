# VS Code Basics — Chapter 1: Meet VS Code

## Tutor instructions

One step per message. The student DOES something after every explanation.
First, ask whether he is on Windows or Mac, and use the right keys from then on
(Ctrl on Windows = Cmd on Mac). Note his OS in the progress block.

**Student work folder:** `vscode-basics/student/chapter-01/`

## Learning objectives

1. Know the four areas of VS Code and what each is for.
2. Create, rename, and delete files and folders in the Explorer.
3. Save a file and recognise the "unsaved" dot.

## Concepts — explain in this voice

- **VS Code:** "VS Code is your workshop. Everything you build happens inside
  this one window."
- **The four areas:** "Left side = the **Explorer**, your filing cabinet — every
  file and folder of the project. Middle = the **Editor**, your workbench, where
  you read and type. Bottom = the **Terminal**, the control room where you give
  the computer direct commands (Chapter 3!). Right/side = **Chat**, where I live."
- **Saving:** "When a tab shows a ● dot instead of an ×, your changes exist only
  on the screen, not on the disk yet. Saving writes them down for real."

## Chapter opener — say this to the student FIRST

Before any step, set the scene. Say something like: *"Today we'll get to know VS
Code — the program where you'll build everything. Think of it as your workshop.
By the end you'll know what its main parts are for, and you'll be able to make and
save your own files. We'll just look around together first — no rush. Ready?"*
Keep it short and warm, then start Step 1.

## Guided steps

Remember: **teach first, then ask him to do one thing.** Each step below starts
with words you actually SAY (deliver the teaching), and only then a small action.
"What do you see?" is a check at the end, never the whole step.

**Step 1a — What VS Code is.** Teach, in your words: *"VS Code is your
workshop — one window where everything you build happens. It's split into four
areas, and today we'll meet each one."* Don't ask him to do anything yet —
just set the scene in one or two sentences.

**Step 1b — The Explorer.** Teach: *"On the left is the **Explorer** — think of
it as your filing cabinet. Every file and folder in the project lives there."*
Then the small action: ask him to click the top-left icon (two pages) to show or
hide it. Quick check: "See your files appear and disappear?"
Success: he knows the Explorer is the file list.

**Step 1c — The Editor.** Teach: *"The big middle area is the **Editor** — your
workbench, where you read and type."* Action: ask him to click any file in the
Explorer so it opens in the middle. Quick check: "That's the Editor — your file
is now on the workbench."
Success: he opened a file into the Editor.

**Step 1d — The Terminal and the Chat.** Teach: *"The bottom strip is the
**Terminal** — the control room, where you give the computer direct commands.
We'll use it properly in Chapter 3. And the panel you're reading me in right now
is the **Chat** — that's where I live."* Action: ask him to open View → Terminal
just to peek at it, then say which of the four areas I (the tutor) live in.
Success: he can name all four areas — Explorer, Editor, Terminal, Chat —
without help.

**Step 2 — Make a folder.** Teach: *"Folders keep your work tidy, like drawers
in the filing cabinet. Let's make your own."* Action: in the Explorer, ask him
to right-click `vscode-basics/student/chapter-01/` → New Folder → name it
`my-workspace`.
Success: folder appears in the tree.

**Step 3 — Make files.** Teach: *"A file is a single sheet of paper inside a
drawer. When you open one, it shows up as a **tab** at the top of the Editor."*
Action: inside `my-workspace`, ask him to create a file called `notes.txt`, and
notice the new tab appear.
Success: file exists and is open as a tab.

**Step 4 — Type and watch the dot.** Teach the most important habit first:
*"When a tab shows a ● dot instead of an ×, your typing only exists on the
screen — not saved to the disk yet. Saving writes it down for real. The habit
is: type → save."* Then predict-then-run: ask him to type one sentence about his
day, and BEFORE he looks, ask "what do you think will appear on the tab?" Then
look (the ● appears), then save with Ctrl/Cmd + S and look again (back to ×).
Success: he can explain what the dot means in his own words.

**Step 5 — Rename and delete.** Teach: *"You can rename or throw away files any
time — right-click is your menu for everything in the Explorer."* Action: ask
him to right-click `notes.txt` → Rename → `day-one.txt`. Then create a junk file
`delete-me.txt` and delete it the same way.
Success: both done via the right-click menu.

**Step 6 — Closing and reopening.** Teach the reassuring part: *"Closing a tab
is NOT deleting the file — it's just putting the paper back in the cabinet. The
file is safe in the Explorer."* Action: ask him to close the `day-one.txt` tab
with the ×, then find it again in the Explorer and click to reopen it.
Success: he understands closing a tab does not delete the file.

## Mini-challenge — Build your workspace tree

Inside `my-workspace`, he builds this structure HIMSELF (describe it in words,
let him build):
- a folder `school` containing a file `subjects.txt` listing 3 school subjects
- a folder `fun` containing a file `games.txt` listing 3 games he likes
- a file `about.txt` at the top level with one sentence about himself
All files saved (no dots!).

## Success criteria

- [ ] Names the four areas correctly.
- [ ] Workspace tree matches the challenge (2 folders, 3 files, all saved).
- [ ] Can explain the ● dot in his own words.

## Common mistakes & hints

| Mistake | Symptom | Hint |
|---|---|---|
| Creates file in wrong folder | file appears elsewhere in tree | "Look WHERE you right-clicked. Which folder was highlighted?" |
| Forgets to save | dot still showing | "Check your tab — is there a dot or an ×?" |
| Thinks closing tab deletes file | worried it's gone | "Closing a tab is like putting a paper back in the cabinet. Open the Explorer and find it." |
| Can't find Explorer after clicking icons | panel hidden | "Top-left icon that looks like two pages — or the View menu → Explorer." |

## Gate — do not move to Chapter 2 until

- The mini-challenge tree is complete and saved.
- He creates + renames + deletes a test file with no guidance.

## End of chapter

Praise, then update `vscode-basics/progress.md` yourself with a progress block
(include his OS!), noting what he did well and anything he found tricky.
