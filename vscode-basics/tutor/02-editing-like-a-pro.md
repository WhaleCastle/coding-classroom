# VS Code Basics — Chapter 2: Editing Like a Pro

## Tutor instructions

One step per message. This chapter is about *editing confidence* — undo fear is
what slows beginners down. Check progress.md for his OS (Ctrl vs Cmd).

**Student work folder:** `vscode-basics/student/chapter-02/`

## Learning objectives

1. Use the survival shortcuts: Save, Undo/Redo, Copy/Paste, Find.
2. Work with multiple tabs without getting lost.
3. Fix up a messy text file quickly and confidently.

## Concepts — explain in this voice

- **Undo:** "Undo (Ctrl/Cmd+Z) is your time machine. NOTHING you type is ever a
  disaster, because you can always step backwards. Brave typing beats careful
  typing."
- **Find:** "Find (Ctrl/Cmd+F) is a torch. In a big file, don't scroll and
  squint — shine the torch on the word you want."
- **Tabs:** "Each open file is a tab, like fingers holding several pages of a
  book at once."

## Chapter opener — say this to the student FIRST

Before any step, set the scene. Say something like: *"Today you'll become fast and
fearless at editing — saving, undo, redo, copy, paste and find. Here's the big
secret: nothing you type is ever a disaster, because Undo is a time machine. By the
end you'll tidy up a deliberately messy file in seconds. First we'll make that
messy file to practise on. Ready?"* Keep it short and warm, then start Step 1.

## Guided steps

**Step 1 — Set up the messy file.** Ask him to create `messy-story.txt` in the
chapter-02 folder, then type 5–6 short lines of a silly story, deliberately
making it messy: some words doubled doubled, a line in the wrong order, a name
spelled wrong 3 times (e.g. "Pyhton"). He invents the story.
Success: a genuinely messy file exists. (This is fun — let it be silly.)

**Step 2 — Undo / redo drill.** Ask him to delete a whole line… then undo it
back. Type a word… undo… redo (Ctrl/Cmd+Shift+Z or Ctrl+Y on Windows).
Success: he can confidently go back and forth in time.

**Step 3 — Find.** His misspelled name appears 3 times. Ask him to press
Ctrl/Cmd+F, type the wrong spelling, and watch all of them light up; jump
between them with Enter. Then fix each one.
(Replace-all exists, but make him fix these manually — Find is the lesson.)
Success: all 3 fixed, found via Find, not scrolling.

**Step 4 — Select, copy, move.** Teach: click at a line start, hold Shift,
click at the end → selected. Then Ctrl/Cmd+X (cut) and Ctrl/Cmd+V (paste) to
move the out-of-order line to its right place.
Success: story now in correct order.

**Step 5 — Two files side by side.** Ask him to open his `day-one.txt` from
Chapter 1 as a second tab. Then drag one tab to the right half of the editor to
split the screen. Look at both at once, then drag it back.
Success: he split and un-split the editor.

**Step 6 — Zoom.** Eyes matter: Ctrl/Cmd + (plus) and Ctrl/Cmd + - (minus) to
zoom the whole window. Find his comfortable size.
Success: he picked a size he likes.

## Mini-challenge — The Editor Test

Ask him to create `challenge.txt` and, with you giving ONLY the task list (not
the how), he must within the file:
1. type a 4-line list of his favourite foods
2. move line 4 to the top (cut/paste)
3. double the last line (copy/paste)
4. use Find to jump to one specific word
5. undo the doubling… and redo it
6. save with the shortcut
He narrates which shortcut he's using at each step.

## Success criteria

- [ ] All 6 challenge tasks done with shortcuts, not menus.
- [ ] He can say what Undo, Find, and the dot do without prompting.
- [ ] No fear: he deletes and restores text casually.

## Common mistakes & hints

| Mistake | Symptom | Hint |
|---|---|---|
| Uses right-click menu for everything | slow | "Menus work, but the keyboard is faster. Which shortcut does this?" |
| Loses the Find box | panic | "Press Escape to close it, Ctrl/Cmd+F to open it again — it's always there." |
| Edits the wrong tab | confusion | "Look at the tab names — which file are you actually inside?" |
| Redo shortcut differs on Windows | redo 'not working' | "On Windows try Ctrl+Y." |

## Gate — do not move to Chapter 3 until

- The Editor Test passed in one go (or a clean second attempt).

## End of chapter

Praise, then update `vscode-basics/progress.md` yourself with a progress block
(note what clicked and what was tricky). Tease Chapter 3: "Next time you learn to
command the computer directly — the Terminal."
