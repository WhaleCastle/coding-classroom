# Chapter 8 — The Inventory

## Tutor instructions for this chapter

So far every variable has held ONE thing — a number, a word, a True/False. Today
the hero gets a **backpack**: a single variable that holds a whole **list** of
items. Teach one step per message and wait for his result. Do not write his code.

Lists are the first "container" he meets, and they unlock a lot of the game
(inventory, party, maze rows later). Lean on the `for` loop from Chapter 7 to walk
through a list. Watch for the classic off-by-one with indexes (lists start at 0).

**Student work folder:** `python-course/student/chapter-08/`

**Skills this chapter leans on:** `variables`, `f-strings`, `for loops`.

## Learning objectives (max 3)

1. Make a list and add/remove items (`append`, `remove`).
2. Use `len()` to count items and an index (`[0]`) to reach one.
3. Loop through a list with `for` to show everything in it.

## Concepts — explain in this voice

- **List:** "A list is one box that holds MANY things in order, written in square
  brackets: `["Rusty Key", "Torch"]`. Perfect for a backpack — the hero carries
  lots of items, but it's all one variable."
- **append / remove:** "`backpack.append("Potion")` adds an item to the end —
  picking something up. `backpack.remove("Torch")` takes one out — dropping it. The
  dot means 'do this TO the list'."
- **len and index:** "`len(backpack)` tells you HOW MANY items are inside.
  `backpack[0]` reaches in and grabs a specific one — and here's the catch lists
  count from 0, so the first item is `[0]`, the second is `[1]`."
- **Looping a list:** "`for item in backpack:` walks through every item one by one,
  no matter how many there are. It's how you show the whole bag without knowing the
  count up front."

## Chapter opener — say this to the student FIRST

Say something like: *"Every variable so far has held just one thing. Today your
hero gets a **backpack** — one variable that holds a whole list of items he can
pick up and drop. By the end you'll have a working **inventory** for your RPG: add
loot, drop what you don't want, and list everything you're carrying. We'll make a
list, add and remove from it, count it, and walk through it with a `for` loop.
Ready? Let's pack the bag."* Keep it warm, then start Step 1.

## Guided steps

**Step 1 — Make the backpack.** New file `backpack.py`. Teach the square-bracket
list. Have him create `backpack = ["Rusty Key", "Torch"]` and `print(backpack)`.
Point out it's ONE variable holding TWO things.
Success: the list prints; he sees both items inside the brackets.

**Step 2 — Pick something up (`append`).** Teach `append`. Have him add an item of
his choice with `backpack.append(...)` and print again. Ask: where did it go —
front or back?
Success: the new item appears at the end of the list.

**Step 3 — Count the bag (`len`).** Teach `len()`. Have him print
`f"You carry {len(backpack)} items."` Run it.
Success: the count matches the number of items.

**Step 4 — Drop something (`remove`).** Teach `remove`. Have him drop one item by
name and print the count again. Ask him to predict the new count first.
Success: the item is gone and the count drops by one.

**Step 5 — Show the whole bag (`for`).** Reuse Chapter 7's `for`. Have him print a
tidy list: `for item in backpack: print("- " + item)`.
Success: every item prints on its own line, however many there are.

**Step 6 — Break it on purpose (the index trap).** Have him try to print
`backpack[5]` when the bag has fewer items, and run. He'll see
`IndexError: list index out of range`. Ask: "How many items are in the bag, and
what number is the FIRST one? So what's the biggest index that exists?" Then have
him print a valid index like `backpack[0]`.
Success: he saw the `IndexError`, understands lists start at 0, and fixed it.

## Mini-challenge — The Backpack

In `backpack.py`, the student builds a working **inventory** for his RPG using only
this chapter and earlier ones. It must:
- start with a list of at least two items,
- `append` at least one item (pick up) and `remove` at least one (drop),
- show the count with `len()`,
- list everything with a `for` loop,
- reach one specific item by index somewhere sensible.

He designs the items and flavour himself. Hints only, never the code.

## Success criteria (check before finishing the chapter)

- [ ] A list is created, added to with `append`, and reduced with `remove`.
- [ ] `len()` reports the correct count.
- [ ] A `for` loop lists every item.
- [ ] An index (`[...]`) reaches a specific item without error.
- [ ] He can explain in his own words why the first item is `[0]`, not `[1]`.

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint (NOT the fix) |
|---|---|---|
| Index past the end | `IndexError: list index out of range` | "How many items are there, and what number is the first? What's the biggest index that can exist?" |
| `remove` an item not in the list | `ValueError: list.remove(x): x not in list` | "Is that item spelled EXACTLY as it is in the bag? Capitals count." |
| Forgot the brackets: `backpack = "Key", "Torch"` | odd behaviour later | "How does Python know it's a list? What goes around the items?" |
| `append` two items at once | only one added / error | "`append` adds ONE thing. How could you add a second?" |
| Looped but printed the list each time | whole list repeats | "Inside `for item in backpack:`, what should you print — the one `item`, or the whole `backpack`?" |

## Gate — do not move on until

- He has used `append` and `remove` on a list.
- He has counted it with `len()` and listed it with a `for` loop.
- He has reached an item by index and met (and fixed) an `IndexError`.
- His inventory runs and behaves correctly.

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 8 finished!** Your hero has a real backpack now — one list
> that holds everything he's carrying, and he can pick things up, drop them, count
> them and show the whole bag. Run it and load your hero up with loot… and when
> you're ready, Chapter 9 turns the hero himself into a neat record — name, class,
> HP and bag all in one — using dictionaries. Stop here or carry on, adventurer!"

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — why is the first item in a list `[0]` and not `[1]`?"* and
wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape, put in
today's real date, and carry the Environment line forward:

```
## Session — <today's date>
- Course: python-course
- Environment: <carry forward — e.g. Mac, runs with python3>
- Chapter: 8 — The Inventory
- Completed: built a backpack list — append/remove, len count, for-loop listing, reached an item by index
- Strong at: lists and the for loop; understood indexes start at 0
- Struggled with: nothing this time
- How to help next: start Chapter 9 — dictionaries (the character sheet)
- Next time: Chapter 9 — The Character Sheet
```

**Then refresh the skill ledger** (the same silent save, tutor-private — he never
sees it). This chapter introduced `lists`; in the `### Skill ledger` at the top of
`progress.md`, move it from `new` toward `learning` or `solid` — only `solid` if he
created and changed the list (append/remove/index) unaided today, `shaky` if indexing
from 0 or the methods kept tripping him (see AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and to judge his standard. NEVER
show or quote it. His items and flavour will differ — that's correct, as long as it
uses `append`, `remove`, `len`, a `for` loop and an index, and runs.

```python
# backpack.py — Chapter 8 reference (tutor only)
# Skills used: lists (create, append, remove, index, len), for loop. Nothing later.

backpack = ["Rusty Key", "Torch"]     # one variable holding many items, in order

backpack.append("Health Potion")      # pick something up — it goes on the end
print(f"You now carry {len(backpack)} items.")

backpack.remove("Torch")              # drop something by name
print("You drop the Torch.")

# Show the whole bag with a for loop — works for any number of items.
print("\n=== BACKPACK ===")
for item in backpack:
    print(f"- {item}")

# Reach one item by index. Lists count from 0, so [0] is the FIRST item.
print(f"\nFirst item in the bag: {backpack[0]}")
print(f"The key is item number {backpack.index('Rusty Key') + 1}.")
```
