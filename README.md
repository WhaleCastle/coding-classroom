# Coding Classroom

An AI-tutored coding classroom for young beginners, designed to run inside
**VS Code with GitHub Copilot** (works in Cursor too). The AI is the tutor;
the student types every line of code himself.

## How it works

- `AGENTS.md` — the tutor's rulebook: teaching style, hard rules ("never write
  the student's code"), session flow. Read automatically by Copilot and Cursor.
- `.github/agents/tutor.agent.md` — a custom tutor agent for VS Code Copilot
  Chat. It is told never to write the student's code or run his programs — it
  only edits its own two log files (`progress.md` and the hero character sheet
  `hero-sheet.md`) — so the student always does the work.
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
2. In VS Code, install the **Python** extension and sign in to GitHub Copilot.
3. Clone or download this repo and open the `coding-classroom` folder in
   VS Code (File → Open Folder). When VS Code asks **"Do you trust the authors
   of this folder?"**, choose **Yes**.
4. Open Copilot Chat. In the agent/mode picker choose the **tutor** agent and a
   small model (GPT-5 mini works well). In its tools, leave file-editing on (it
   keeps a progress log) but turn OFF anything that runs terminal commands — the
   student runs his code himself. If the tutor agent doesn't appear, **Ask mode**
   works too, but it can't keep the progress log (you'd update it by hand).
5. **(One-time) Let the tutor save its logs without nagging.** So the student
   isn't asked to click "Keep" every time the tutor updates its log or the hero
   sheet, add this to your VS Code **user** settings — `Cmd/Ctrl+Shift+P` →
   **Preferences: Open User Settings (JSON)** — then reload VS Code:

   ```jsonc
   "chat.tools.edits.autoApprove": {
     "**/progress.md": true,
     "**/hero-sheet.md": true
   }
   ```

   This auto-keeps edits to `progress.md` and `hero-sheet.md` only — every other
   file still asks first, and the student always runs his own code in the terminal.
   (It's per machine, and the only files it ever touches are those two log files.)
6. The student types: `Hi! I'm ready for my Python lesson.` — and off you go.

## Daily session

1. Open the folder, open Copilot Chat, pick the **tutor** agent.
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
  `python-course/tutor/00-course-overview.md`. Chapters are being written and
  piloted in batches.
- **php-course**: planned.

## License

MIT — share, adapt, teach.
