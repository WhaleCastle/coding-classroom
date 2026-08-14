# Coding Classroom

An AI-tutored coding classroom for young beginners. It runs in **VS Code**
(with OpenAI Codex or GitHub Copilot) or in **Google Antigravity** (with
Gemini) — pick whichever you have; the course behaves the same in all of them,
and you can switch between them whenever you like without losing progress. The
AI is the tutor; the student types every line of code himself.

## How it works

- `AGENTS.md` — the tutor's rulebook, and the **only** one: teaching style, hard
  rules ("never write the student's code"), session flow, and how the tutor keeps
  its own log. Codex, Copilot, Antigravity and Cursor all read it automatically,
  which is why the same folder becomes the same tutor in any of them. There is
  deliberately no second, tool-specific copy of the rules to drift out of sync.
- `.github/copilot-instructions.md` — a three-line pointer telling Copilot to go
  read `AGENTS.md`. It contains no rules of its own.
  (The student's D&D-style `hero-sheet.md` is generated from `progress.md` by a
  small script, `tools/render_sheet.py` — the tutor never edits the sheet itself.)
- `python-course/`, `vscode-basics/` — one folder per course. Each contains
  `tutor/` (one fully-scripted lesson file per chapter), `student/` (the
  student's own work, one folder per chapter), and `progress.md` (the tutor's
  memory between sessions — the tutor keeps it updated, logging what he learned
  and where he struggled).
  **Do `vscode-basics` first** — a short 3-chapter course on the editor and
  terminal — then the main `python-course`.

The tutor opens each session by **suggesting** the next step based on progress
(the student can ask for a different chapter or a review instead), and it stays
strictly in role: anything unrelated to the courses is politely declined.

## Setup (one-time, ~15 minutes)

1. Install [Python 3](https://www.python.org/downloads/) (tick "Add to PATH" on
   Windows), then **one** of:
   [VS Code](https://code.visualstudio.com/) or
   [Antigravity](https://antigravity.google/).
2. Install the AI tutor's engine — again, whichever you have:
   - **VS Code:** the **Python** extension, plus either the **Codex** extension
     (sign in with a ChatGPT account) or **GitHub Copilot**.
   - **Antigravity:** nothing to install; Gemini is built in. Add the **Python**
     extension for the editor niceties.
3. Clone or download this repo and open the `coding-classroom` folder
   (File → Open Folder). When asked **"Do you trust the authors of this
   folder?"**, choose **Yes**.
4. Open the chat panel and pick a model. **No agent setup is needed in any of
   them** — the tutor's whole personality lives in `AGENTS.md`, which each one
   reads by itself when the folder opens:
   - **Codex:** set the panel to *work locally*. The course is scripted so even
     small models teach well; a mid-tier model is a comfortable choice.
   - **Copilot:** any chat model. It picks up `AGENTS.md` plus the pointer in
     `.github/copilot-instructions.md`.
   - **Antigravity:** a current Gemini model (Gemini 3.7 Flash is a good fit —
     fast replies matter more than deep reasoning when a child is waiting).
5. **(One-time) Let the tutor save its log without nagging.** The tutor's memory
   between sessions is `*/progress.md`, which it writes itself. If the tool asks
   permission for every file edit and nobody clicks **Approve**, the session is
   forgotten. Fix it once, in whichever tool you use:
   - **Codex:** switch the approval mode to **Auto-edit** (the panel's mode
     picker, or type `/mode auto-edit`). File edits then apply automatically
     while running commands still asks first — which is what we want, since the
     student runs his own code himself. Codex can't auto-approve a single file.
   - **Copilot:** already handled — `.vscode/settings.json` in this repo
     auto-approves edits to `**/progress.md` and nothing else.
   - **Antigravity:** set the agent's approval/autonomy setting so file edits
     apply without a click (it is per-machine, like Codex's).

   If you'd rather approve everything by hand, that's fine too — just teach the
   student that when the tutor says it's saving the log, he clicks **Approve**.
6. **The hero character sheet builds itself.** `python-course/hero-sheet.md` (his
   D&D Level / XP / spells / trophies) is generated from `progress.md` by
   `tools/render_sheet.py`. A VS Code task (in `.vscode/tasks.json`) starts a small
   background **watcher** when you open the folder, which re-renders the sheet within
   a couple of seconds of any change to `progress.md` — so a level-up shows up the
   moment the tutor saves. **The first time, VS Code asks "Allow Automatic Tasks?" —
   choose Allow** (otherwise the sheet won't auto-update). To force a one-off render:
   Terminal → Run Task… → **Render hero sheet (once)**, or run
   `python3 tools/render_sheet.py`. (The tutor only records the facts in
   `progress.md`; it never edits the sheet.)
7. The student types: `Hi! I'm ready for my Python lesson.` — and off you go.

> **Switching tools, or using two?** You can — and nothing is lost. Everything
> that remembers the student lives in plain files inside the course folder
> (`progress.md`, his own code under `student/`, and the hero sheet), not inside
> any one editor. Open the same folder in VS Code on Monday and Antigravity on
> Thursday and the tutor picks up exactly where it left off, because it reads the
> same `progress.md` either way. The only per-tool step is the approval setting in
> step 5 — do it once in each tool you actually use.
>
> **One rule if you do:** don't run two tutors on the folder at the same time.
> Both would write `progress.md` and the last one to save wins.

## Daily session

1. Open the folder and open the chat panel (Codex, Copilot, or Antigravity —
   whichever you set up).
2. Greet the tutor. It reads the progress files and suggests today's plan —
   accept it, or ask for a different chapter or a review.
3. Your work goes in the course's `student/chapter-XX/` folder; run code
   yourself in the terminal (`python yourfile.py`).
4. At the end, the tutor updates that course's `progress.md` itself — noting what
   you did and where you struggled — so it remembers next time.
5. (Optional but great habit) Commit your work:
   `git add . && git commit -m "Chapter 2 session"`

## Rules of the classroom

- The tutor explains, hints, and reviews. It never writes your code.
- You run everything in the terminal yourself.
- Errors are normal. Read them — they're clues, not punishments.

## Course status

- **vscode-basics**: complete (3 short chapters) — start here.
- **python-course**: a year-long **"build your own RPG"** course. Across 20
  chapters (+2 optional bonuses) the student builds one text-mode role-playing
  game — character creation, a dungeon maze, combat and conversation encounters,
  and a story that branches into different endings — and along the way practises
  every programming skill in the **UK Key Stage 3–4 Computer Science**
  curriculum. Full chapter map and coverage in
  `python-course/tutor/00-course-overview.md`. All 20 chapters, the 6 boss-fight
  checkpoints and both bonus quests are written; they're piloted with a real
  student and refined from session feedback.
- **php-course**: planned.

## License

MIT — share, adapt, teach.
