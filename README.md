# Coding Classroom

An AI-tutored coding classroom for young beginners, designed to run inside
**VS Code with GitHub Copilot** (works in Cursor too). The AI is the tutor;
the student types every line of code himself.

## How it works

- `AGENTS.md` — the tutor's rulebook: teaching style, hard rules ("never write
  the student's code"), session flow. Read automatically by Copilot and Cursor.
- `.github/agents/tutor.agent.md` — a custom **read-only** tutor agent for
  VS Code Copilot Chat (no file-editing tools, so it *can't* do the work for
  the student).
- `python-course/`, `vscode-basics/` — one folder per course. Each contains
  `tutor/` (one fully-scripted lesson file per chapter), `student/` (the
  student's own work, one folder per chapter), and `progress.md` (the tutor's
  memory between sessions — the student updates it himself at session end).
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
   VS Code (File → Open Folder).
4. Open Copilot Chat. In the agent/mode picker choose the **tutor** agent and a
   small model (GPT-5 mini works well). If the tutor agent doesn't appear,
   use **Ask mode** — it also cannot edit files.
5. The student types: `Hi! I'm ready for my Python lesson.` — and off you go.

## Daily session

1. Open the folder, open Copilot Chat, pick the **tutor** agent.
2. Greet the tutor. It reads the progress files and suggests today's plan —
   accept it, or ask for a different chapter or a review.
3. Your work goes in the course's `student/chapter-XX/` folder; run code
   yourself in the terminal (`python yourfile.py`).
4. At the end, copy the tutor's progress block into that course's `progress.md`.
5. (Optional but great habit) Commit your work:
   `git add . && git commit -m "Chapter 2 session"`

## Rules of the classroom

- The tutor explains, hints, and reviews. It never writes your code.
- You run everything in the terminal yourself.
- Errors are normal. Read them — they're clues, not punishments.

## Course status

- **vscode-basics**: complete (3 short chapters) — start here.
- **python-course**: chapters 1–3 fully scripted; full 14-chapter map in
  `python-course/tutor/00-course-overview.md`. More chapters coming after the
  pilot.
- **php-course**: planned.

## License

MIT — share, adapt, teach.
