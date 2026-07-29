# Coding Classroom

An AI-tutored coding classroom for young beginners, designed to run inside
**VS Code with OpenAI Codex** (works with GitHub Copilot or Cursor too). The
AI is the tutor; the student types every line of code himself.

## How it works

- `AGENTS.md` — the tutor's rulebook: teaching style, hard rules ("never write
  the student's code"), session flow. Codex reads it automatically (it is
  Codex's native instructions file); Copilot and Cursor read it too.
- `.github/agents/tutor.agent.md` — an optional custom tutor agent for VS Code
  Copilot Chat (Codex doesn't need it — `AGENTS.md` is enough). It is told
  never to write the student's code or run his programs — it
  only edits its own `progress.md` log — so the student always does the work.
  (His D&D-style `hero-sheet.md` is generated from `progress.md` by a small
  script, `tools/render_sheet.py` — the tutor never edits the sheet itself.)
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
   Windows) and [VS Code](https://code.visualstudio.com/).
2. In VS Code, install the **Python** extension and the **Codex** extension
   (sign in with your ChatGPT account). GitHub Copilot works too — see the
   note after these steps.
3. Clone or download this repo and open the `coding-classroom` folder in
   VS Code (File → Open Folder). When VS Code asks **"Do you trust the authors
   of this folder?"**, choose **Yes**.
4. Open the Codex chat panel and set it to **work locally**. Pick a solid model
   — the course is scripted so even small models teach well; a mid-tier model
   (e.g. GPT-5.6-Terra Medium) is a comfortable choice. No agent setup is
   needed: Codex reads `AGENTS.md` by itself and becomes the tutor.
5. **(One-time) Let the tutor save its log without nagging.** Codex's default
   *Suggest* approval mode asks for an **Approve** click on every file edit —
   including the tutor's own `progress.md` log, and an unapproved log means the
   tutor forgets the whole session. Switch the approval mode to **Auto-edit**
   (in the Codex panel's mode picker, or type `/mode auto-edit`): file edits
   apply automatically, while running commands still asks first (the student
   runs his own code himself anyway). Codex can't auto-approve just one file;
   if you'd rather stay in *Suggest* mode, teach the student that when the
   tutor saves its log, he clicks **Approve**.
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

> **Using GitHub Copilot instead?** In Copilot Chat's agent/mode picker choose
> the **tutor** agent (from `.github/agents/tutor.agent.md`), leave file-editing
> on but untick anything that runs terminal commands, and add
> `"chat.tools.edits.autoApprove": { "**/progress.md": true }` to your VS Code
> **user** settings so the log saves without a "Keep" click each time.

## Daily session

1. Open the folder and open the Codex chat (Copilot users: pick the **tutor**
   agent).
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
