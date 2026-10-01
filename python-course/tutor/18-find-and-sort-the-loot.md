# Python Course — Chapter 18: Find & Sort the Loot

## Tutor instructions for this chapter

**BOSS-PREDECESSOR chapter** — Boss VI, **The Archivist**, follows this one. Budget **2–3 sessions**. This chapter builds two classics EVERY programmer hand-writes at least once: linear search and bubble sort — both built by HAND. Resist `.sort()` until AFTER bubble sort exists; it's mentioned once, then, as the everyday shortcut.

For swapping list values use the **temp box** (`temp = a; a = b; b = temp`), not the tuple swap `a, b = b, a` — more KS-honest about what's really happening (the shortcut may get one passing mention). Binary search and merge/insertion sort get exactly ONE scripted line each — named only, "you'll meet them properly at GCSE." Don't teach how they work.

Ceiling: Chapters 1–17.

**Student work folder:** `python-course/student/chapter-18/`

**Skills this chapter leans on:** `lists`, `for loops`, `while loops`, `functions`, `return values`.

## Learning objectives (max 3)

1. Write a linear search by hand using a found-flag, and turn it into a
   function that returns True/False.
2. Write a bubble sort by hand using neighbour swaps (a temp box) and a
   swapped-flag to know when to stop.
3. Name binary search and merge/insertion sort as faster alternatives he'll
   meet later.

## Concepts — explain in this voice

- **Linear search:** "Check every item, one at a time, from the start, until you find it or run out of backpack. No shortcuts — just a torch and patience."
- **Found-flag:** "A light-switch that starts OFF (`False`) and flips ON (`True`) the moment you spot a match — and STAYS on. Without it the loop has no memory of what it already saw."
- **Bubble sort & neighbour swaps:** "Walk the list comparing NEIGHBOURS, two at a time; swap if they're in the wrong order. Do that all the way along and the biggest value 'bubbles' to the end — like the tallest kid slowly swapping to the back of a queue."
- **The temp box:** "`a = b` OVERWRITES `a` before `b` ever gets the old value — it's lost. A third, TEMPORARY box holds it safely: `temp = a`, then `a = b`, then `b = temp`."
- **Repeat until no swaps:** "One pass only bubbles the biggest value into place. Repeat the whole pass again and again, and stop the moment a WHOLE pass makes zero swaps — proof nothing's left out of order."
- **Faster cousins (named only):** "Python's built-in `.sort()` does this instantly — the everyday shortcut, once you know what's underneath it. Binary search and merge/insertion sort are faster still; you'll build those properly at GCSE."

## Chapter opener — say this to the student FIRST

Say something like: *"Every time you search your phone's contacts or see a leaderboard sorted biggest-first, a computer is doing exactly what we're about to build by hand: SEARCHING and SORTING. Today your hero hunts his backpack for an item, and you sort a bounty board so the richest reward tops the list. These two tricks are everywhere in computing, and today you build the real ones — not just call a shortcut. We'll start with the hunt, then learn to swap two things safely, then build a full sort out of that one swap, repeated. Ready to go treasure hunting?"* Keep it warm, then start Step 1.

## Guided steps

**Step 1 — The hunt.** In a fresh file, build a small backpack list (Chapter 8) and search it with `for` + `if`, printing found/not found. PREDICT-then-run on an item that IS there, then one that ISN'T.
Success: both print correctly; he notices "not found" needs a flag that starts False and only flips True on a match.

**Step 2 — Make it a function.** Turn the hunt into `find_item(bag, wanted)` RETURNING True/False (recap Chapter 11); call it from an `if`.
Success: the function returns the right Boolean both ways, and the caller reacts correctly.

**Step 3 — Neighbours and swaps.** Teach the temp box: `a = 5`, `b = 2`, swap via `temp = a`, `a = b`, `b = temp`, print before/after. PREDICT what happens without the temp box.
Success: the swap works; he can explain why skipping the temp box loses a value.

**Step 4 — One bubble pass.** Give a 5-number list; write ONE pass — `for` comparing `numbers[i]`/`numbers[i + 1]`, swap (temp box) if wrong order. PREDICT where the biggest number ends up.
Success: after one pass the biggest is at the very end, even if the rest isn't sorted yet.

**Step 5 — The full bubble sort.** Wrap the pass in a `while` loop driven by a swapped-flag: `swapped = False` each pass, set `True` on any swap, repeat while `swapped` stays `True`.
Success: the list ends fully sorted and the loop stops itself.

**Step 6 — Sort the bounty board.** Build a bounty board (list of gold values), run his bubble sort, print before/after. Mention once: Python's `.sort()` does this instantly — now he knows what's underneath it. Print a tidy top-3.
Success: the board prints sorted; the top-3 shown biggest-first are genuinely the three largest.

**Step 7 — The faster cousins.** One scripted line each: binary search (halves a SORTED list each check — needs sorting first) and merge/insertion sort (other ways to sort) — "you'll build these properly at GCSE."
Success: he can say, in his own words, that faster methods exist and roughly why binary search needs sorting first.

## Mini-challenge — The Bounty Board

The student builds his own version using only this chapter and earlier ones. It must:
- search his backpack by name using a hand-written linear search (found-flag,
  returns True/False from a function),
- bubble-sort a numeric leaderboard (gold-per-monster or similar) by hand,
  using the temp-box swap and a swapped-flag,
- print the leaderboard BEFORE and AFTER sorting, biggest at the top.

He designs the flavour and the exact list contents himself. Hints only, never the code.

## Side quest (optional) — Reverse the Board

Offer this only when he's ahead of pace — it costs nothing to skip. Pitch it like: *"Feeling flexible? Make your bounty board sort SMALLEST-first instead — see if you can spot which single comparison needs flipping."* Requirements:
- reuse his existing bubble sort — change nothing but the ONE comparison
  that decides "wrong order",
- confirm the list now comes out smallest-to-largest,
- explain in one sentence why flipping that comparison was enough.

## Success criteria (check before finishing the chapter)

- [ ] A hand-written linear search uses a found-flag and correctly reports
      both a present and an absent item.
- [ ] `find_item()` is a function that RETURNS True/False rather than
      printing directly.
- [ ] A hand-written bubble sort uses a temp-box swap and a swapped-flag,
      and stops itself when sorted.
- [ ] The bounty board prints correctly before and after sorting, biggest
      three shown first.
- [ ] He can explain, in his own words, why a search needs a found-flag and
      why binary search needs a sorted list.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Found-flag reset inside the loop | always reports "not found" even when it IS there | "Where does the flag get set back to False — is that line inside or outside the loop?" |
| Compared `numbers[i]` with `numbers[i + 1]` on the very last index | `IndexError: list index out of range` | "When `i` is the LAST index, does `i + 1` still point at a real box in the list?" |
| Swapped without a temp box (`a = b` then `b = a`) | one value gets overwritten and duplicated | "After your first line ran, what was still inside `a`? Had you already lost the old value?" |
| Swapped-flag never reset to False at the start of a pass | the loop never stops, runs forever | "At the START of each new pass, what should `swapped` be assumed to be — and where do you set that?" |

## Gate — do not move on until

- He has a working linear search with a found-flag that correctly handles
  BOTH a present and an absent item.
- He has turned the search into a function that returns True/False.
- He has a working bubble sort using the temp-box swap.
- His sort uses a swapped-flag and stops itself without a fixed number of
  passes.
- He can name binary search and merge/insertion sort and say (roughly) why
  they're faster.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 18 finished!** You've now hand-built two of the most famous tricks in all of computing — searching your backpack with a found-flag, and bubble-sorting your bounty board with nothing but a temp box and a lot of patience. You even know their faster cousins exist for later. Go run your bounty board and watch it sort itself! And now your sixth **boss** awaits: **The Archivist**, the crypt's ancient librarian, who'll only stamp your record if you can keep an archive of your own — save it, guard it, search it, sort it — with no steps from me this time. Face it now, or stop here and take it on next session?"

Before you treat the chapter as done, if he hasn't already said it, ask: *"In your own words — why does a search need a found-flag, and why does bubble sort need a swapped-flag?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of `python-course/progress.md`. Don't say you're doing it. Copy this shape, put in today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 18 — Find & Sort the Loot
- Completed: hand-built a linear search with a found-flag (returned from a function), hand-built bubble sort with a temp-box swap and a swapped-flag, sorted the bounty board
- Strong at: the temp-box swap; knowing when a loop should stop itself
- Struggled with: nothing this time
- How to help next: run Boss VI — The Archivist (Chapters 1–18 checkpoint, tutor muted)
- Next time: Boss VI — The Archivist (then Chapter 19)
```

**Then update the `### Facts`** in `progress.md`: `chapters_cleared` +1 (and +1 to `mini_challenges_done` if he did it; `predict_wins` / `break_it_fixes` were already counted the moment each happened) — the script turns these into his new Level, XP and spells.

**Then refresh the skill ledger** (the same silent save, tutor-private — he never sees it). This chapter introduced `search & sort`; move it from `new` toward `learning` or `solid` — only `solid` if he built BOTH the search and the sort unaided today, `shaky` if the found-flag or the swapped-flag genuinely tripped him up (see AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only — use it to shape hints and judge his standard, never show or quote it. His item names and board numbers will differ; what matters is a search using a found-flag returned from a function, and a sort using a temp-box swap and a swapped-flag. Reuses the running game's backpack (Chapter 8) as the search target. No files or `try`/`except` needed here — those are earlier chapters, not new material for this one.

```python
# bounty_board.py — Chapter 18 reference (tutor only)
# Skills used: for loops, if/decisions, functions + return (Ch11), while loops, lists.
# Nothing later: no files (Ch16/17 skills not required here), no forward references.

def find_item(bag, wanted):
    """Linear search: check the backpack one item at a time.
    The found-flag starts False and only flips True if we actually spot a
    match — that's what makes the 'not found' case work too, not just 'found'."""
    found = False
    for item in bag:
        if item.lower() == wanted.lower():
            found = True
    return found


def bubble_sort(numbers):
    """Sorts smallest-to-largest by repeatedly walking the list and swapping
    any two neighbours that are in the wrong order. Each full pass pushes the
    biggest remaining number one step closer to the end — like the tallest
    kid in a line slowly swapping past everyone shorter. We stop the moment a
    whole pass makes NO swaps, because that's proof the list is sorted."""
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                # Swap using a temp box — without it we'd overwrite and lose a value.
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                swapped = True
    return numbers


# --- the backpack: search it ---
backpack = ["torch", "rope", "healing potion", "rusty key"]

wanted_item = "healing potion"
if find_item(backpack, wanted_item):
    print(f"Found the {wanted_item} in your backpack!")
else:
    print(f"No {wanted_item} here — better keep looking.")

missing_item = "silver shield"
if find_item(backpack, missing_item):
    print(f"Found the {missing_item} in your backpack!")
else:
    print(f"No {missing_item} here — better keep looking.")

# --- the bounty board: sort it ---
bounty_board = [40, 15, 90, 25, 60]   # gold reward per monster, unsorted
print(f"\nBefore sorting: {bounty_board}")

bubble_sort(bounty_board)
print(f"After sorting:  {bounty_board}")

# Python also has a built-in .sort() that does this instantly — now you know
# exactly what it's doing under the hood. We stick with our own for this game.

print("\nTop 3 bounties (biggest first):")
last_index = len(bounty_board) - 1
for i in range(3):
    print(f"  {bounty_board[last_index - i]} gold")
```
