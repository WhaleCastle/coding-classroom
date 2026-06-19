# Chapter 2 — Name Your Hero

## Tutor instructions for this chapter

One step per message. Wait for the student's result each time. Never write his
code. Begin by asking him to run his `title.py` from Chapter 1 once — a quick
warm-up and a reminder that we're building a game.

Today the game stops being a one-way speech and starts to *listen*: it will ask
the player what their hero is called and greet that hero by name. That's the first
piece of **character creation**.

**Student work folder:** `python-course/student/chapter-02/`

**Skills this chapter leans on:** `print / strings`, `running a file in the terminal`.

## Learning objectives

1. Store information in a variable and use it later.
2. Get text from the player with `input()`.
3. Drop variables into messages with f-strings.

## Concepts — explain in this voice

- **Variable:** "A variable is a labelled box. You put something in the box and
  stick a name on it. Later you ask for the box by name and Python hands you what's
  inside. `hero = \"Marcus\"` puts the text Marcus into a box labelled hero — now
  the game remembers who the hero is."
- **input():** "`input()` makes your game pause and wait for the player to type
  something, then it hands you back whatever they typed. It's how the player talks
  *to* the game."
- **f-string:** "An f-string is a message with holes in it. You write `f` before
  the quotes, and `{hero}` where you want Python to pour in what's inside the box.
  So `f\"Welcome, {hero}!\"` becomes `Welcome, Marcus!`."

## Chapter opener — say this to the student FIRST

Before any step, set the scene. Say something like: *"Right now your game only
talks AT the player. Today it's going to **listen**: it'll ask the player what
their hero is called and then greet that hero by name — that's the very start of
building a character. We'll do it in little steps: first we make a box to hold a
name, then we get the player to type one in, then we drop it into a friendly
message. Ready?"* Keep it short and warm, then start Step 1.

## Guided steps

**Step 1 — Warm-up.** Ask him to run `title.py` from Chapter 1. Quick chat: what
does `print()` do? What are the quotes for?

**Step 2 — The hero's name box.**
New file `hero.py` in the chapter-02 folder. Ask him to make a variable holding a
hero name (any name), then print the variable — no quotes around the variable name
inside print. Predict-then-run: "What will appear on screen?"
Success: the name prints, and he can say why there are no quotes inside print.

**Step 3 — Quotes vs no quotes.**
Ask him to print the same word WITH quotes and then WITHOUT: `print("hero")` vs
`print(hero)`. Run both. Discuss: quotes = the literal letters h-e-r-o; no quotes
= "open the box called hero and show what's inside."
Success: he explains the difference in his own words.

**Step 4 — The box can change.**
Ask him to give the variable a NEW value on a later line (the hero gets renamed!),
printing it before and after. Predict-then-run.
Success: he sees the box's contents can change — that's why it's called a
*variable* (it varies).

**Step 5 — Ask the player.**
New file `name_your_hero.py`. Teach `input()`: ask him to make a variable that gets
its value from `input("What is your hero's name? ")`, then greet the hero with a
print. Teach the shape: `box = input("question ")`. Let him assemble it.
Success: the game asks, he types a name, the game greets that name.

**Step 6 — f-strings.**
His Step 5 greeting is probably clunky (two prints, or string-gluing). Show the
f-string *concept* with a DIFFERENT example (e.g. a sword: `f"You found the {sword}"`),
then ask him to upgrade his greeting to one f-string like `f"Welcome, {hero}! Your
quest begins."`.
Success: the greeting uses `f"...{hero}..."` and runs.

**Step 7 — Choose a class.**
Ask him to add a SECOND question — the hero's class (warrior, mage, rogue… his
choice of options) — store it in another box, then print ONE final sentence that
uses BOTH boxes, e.g. `f"{hero} the {hero_class} steps into the crypt."`.
Success: one sentence, two holes, both filled correctly.

## Mini-challenge — Character Creator

New file `character_creator.py`. The game must:
- ask at least 3 questions about the hero (name + 2 of his choice — class, weapon,
  home village, anything),
- reply with at least 2 sentences (f-strings) that use the answers to introduce
  the hero,
- have some flavour — he decides the tone (heroic? funny? spooky?).

He plans the questions first (ask him to TELL you the 3 questions before he codes).
Then he builds it. Hints only.

## Success criteria

- [ ] He can explain "labelled box" back to you in his own words.
- [ ] `name_your_hero.py` works with `input()` + an f-string greeting.
- [ ] Character Creator asks 3+ questions and uses every answer in its reply.
- [ ] He can answer: "What's the difference between `print("hero")` and
      `print(hero)`?"

## Common mistakes & the hints to give

| Mistake | What he'll see | Your hint |
|---|---|---|
| Quotes around the variable in an f-string `{"hero"}` | the literal word, not the value | "Inside the curly brackets Python wants the box's *name*, not letters in quotes. Take the quotes out." |
| Forgot the `f` before the quotes | `{hero}` prints literally | "Your message printed the hole instead of filling it. What letter goes before the quote to tell Python this string has holes?" |
| Space in a variable name (`hero name`) | `SyntaxError` | "Box labels can't have spaces. Programmers join words with an underscore `_` instead." |
| Used a box before making it | `NameError: name 'hero' is not defined` | "Python reads top to bottom. Did you ask for the box before you'd filled it?" |
| `=` vs `==` (may appear) | varies | "One `=` means PUT INTO the box. (Two `==` comes later — it means *compare*.)" |

## Gate — do not move on until

- Character Creator works fully (asks 3+, greets using every answer).
- He can predict the output of a short 3-line variable program BEFORE running it
  (test him with a tiny example you describe in words — he writes and runs it to
  check his prediction).

## End of chapter

Once the Gate above is met, finish like this.

**Say this** — one warm message; swap the blanks for what he actually did:

> "That's **Chapter 2 finished!** You just built character creation — the heart
> of any RPG. Your game asks the player questions, remembers the answers, and
> greets your hero by name. Run it once more and meet the hero you made come to
> life… and when you're ready, Chapter 3 is where the crypt makes your hero
> *choose* — and choices have consequences. We can stop here or keep going."

Before you treat the chapter as done, if he hasn't already said it, ask:
*"In your own words — what is a variable?"* and wait for his answer.

**Then save his progress** — add a block to the TOP of
`python-course/progress.md`. Don't say you're doing it. Copy this shape and put
in today's real date:

```
## Session — <today's date>
- Course: python-course
- Chapter: 2 — Name your hero
- Completed: built the character creator — asks for name/class/weapon with input(), greets the hero with an f-string
- Strong at: storing answers in variables; using f-strings to drop them into a sentence
- Struggled with: nothing this time
- How to help next: start Chapter 3 — branching the story with if/else
- Next time: Chapter 3 — The first choice
```

**Then refresh the skill ledger** (the same silent save, tutor-private — he never
sees it). This chapter introduced `variables`, `input` and `f-strings`; in the
`### Skill ledger` at the top of `progress.md`, move each from `new` toward `learning`
or `solid` — only `solid` if he used it unaided today, `shaky` if he kept struggling
(see AGENTS.md "The skill ledger").

## Reference solution — TUTOR'S EYES ONLY, never show the student

Private reference only. Use it to shape hints and judge his standard. NEVER show or
quote it. His questions and flavour will differ — that's correct.

```python
# character_creator.py — Chapter 2 reference (tutor only)
# Skills used: variables, input(), f-strings, print(). Nothing later than ch 2.

print("=== Create your hero ===")

# input() asks a question and hands back whatever the player types.
# We store each answer in its own labelled box (a variable).
hero = input("What is your hero's name? ")
hero_class = input("What is your hero's class (warrior/mage/rogue)? ")
weapon = input("What weapon do they carry? ")

# f-strings drop the box contents into a sentence using {box_name}.
print(f"Welcome, {hero} the {hero_class}!")
print(f"Armed with a {weapon}, {hero} steps into the Crypt of Broken Keys.")
```
