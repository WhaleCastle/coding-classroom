#!/usr/bin/env python3
"""
render_sheet.py — build the student's hero-sheet.md from the FACTS in progress.md.

The Mentor (GPT-5 mini) only records simple facts in progress.md (a few counters and
the skill ledger). This script does ALL the derived bookkeeping — XP, Level, Class,
spellbook ranks, ability stars, trophies — and rewrites hero-sheet.md from scratch.

Because the sheet is REGENERATED from the facts (not mutated in place), it is
self-healing: a missed or wrong update never compounds — the next render is correct.

Usage:
    python3 tools/render_sheet.py [path-to-course-folder]
Default course folder: python-course/ (relative to repo root).
"""

import re, sys, os, time, unicodedata

# ---- canonical course data (extend as later chapters are written) -------------
# Skill -> the chapter that INTRODUCES it (drives 🔒 Locked vs 🌱 Apprentice).
INTRO_CH = {
    "print / strings": 1, "running a file in the terminal": 1,
    "variables": 2, "input": 2, "f-strings": 2,
    "if / decisions": 3, "comparisons": 3,
    "numbers & arithmetic": 4, "booleans & logic": 5,
    "while loops": 6, "for loops": 7, "lists": 8,
}
SKILL_ORDER = list(INTRO_CH)  # display order in the spellbook

# Short, friendly labels for the sheet (single source of truth — no drift).
DISPLAY = {
    "print / strings": "print / strings", "running a file in the terminal": "running a file",
    "variables": "variables", "input": "input", "f-strings": "f-strings",
    "if / decisions": "if / decisions", "comparisons": "comparisons",
    "numbers & arithmetic": "numbers & maths", "booleans & logic": "booleans & logic",
    "while loops": "while loops", "for loops": "for loops", "lists": "lists",
}

# Skills each boss proves (→ ⭐ Mastered when that boss is won).
BOSS_SKILLS = {
    "boss-01": ["print / strings", "variables", "input", "f-strings",
                "if / decisions", "comparisons"],
    "boss-02": ["numbers & arithmetic", "booleans & logic", "while loops",
                "variables", "input", "f-strings", "if / decisions", "comparisons"],
}

# Ability-score clusters (ledger-derived ones).
CLUSTERS = {
    "🧠 LOGIC  (decisions, true/false)": ["if / decisions", "comparisons", "booleans & logic"],
    "🔁 STAMINA (loops)":               ["while loops", "for loops"],
    "🎒 LORE   (lists & records)":       ["lists"],   # + dictionaries/strings/files later
}

CLASS_BANDS = [(0, 1, "Code Apprentice"), (2, 3, "Code Adept"), (4, 6, "Code Mage")]
VALID_TAGS = {"new", "learning", "solid", "shaky"}

# XP weights (recomputed fresh every render — no running total is ever carried).
XP = dict(chapter=20, mini=10, predict=5, debug=5, boss=50, hint=-25)


def parse_progress(text):
    """Pull the facts block + skill ledger out of progress.md — tolerant of small-model
    formatting quirks (case, multi-line lists, duplicate/unknown ids, placeholder values)."""
    # Forgive common small-model markdown noise in ONE pass (rather than patching every
    # regex): turn '*' list bullets into '-', and strip '*' and '`' emphasis so styled
    # entries like `* **chapters_cleared**: **3**` parse the same as `- chapters_cleared: 3`.
    # ('_' is left alone — it's part of fact keys like chapters_cleared.)
    text = re.sub(r"^(\s*)\*(\s)", r"\1-\2", text, flags=re.M)
    text = text.replace("*", "").replace("`", "")

    # The skill ledger lives in its own section; isolate it (below the heading) for ledger
    # parsing only.
    parts = re.split(r"#+\s*skills?\s+ledger", text, flags=re.I, maxsplit=1)
    ledger_text = parts[1] if len(parts) > 1 else ""

    # Read each fact from the WHOLE document — NOT just the text above the ledger heading.
    # The small-model tutor sometimes writes or reorders the `### Facts` block to sit AFTER
    # the ledger, which used to push hero_name (and the counters) outside the search window
    # so the sheet fell back to the "a new apprentice" placeholder. Fact keys are unique and
    # never collide with ledger skill names, so scanning the full text is safe.
    def fact(key, default=""):
        m = re.search(rf"^\s*-\s*{re.escape(key)}\s*:\s*(.*)$", text, re.M | re.I)
        return m.group(1).strip() if m else default

    def to_int(key):
        m = re.search(r"-?\d+", fact(key, "0"))
        return int(m.group()) if m else 0

    # bosses_won — read just the bosses_won entry (its line + any following bulleted items,
    # up to the next `- key:`), so a boss id mentioned in ANOTHER fact can't be miscounted.
    # Works for a same-line comma list OR a multi-line bulleted list; dedupe; keep only KNOWN ids.
    bw = re.search(r"^\s*-\s*bosses_won\s*:(.*?)(?=^\s*-\s*\w+\s*:|\Z)",
                   text, re.M | re.S | re.I)
    chunk = bw.group(1) if bw else ""
    seen, bosses = set(), []
    for b in re.findall(r"boss-\d+", chunk.lower()):
        if b in BOSS_SKILLS and b not in seen:   # ignore duplicates and unknown/mistyped ids
            seen.add(b); bosses.append(b)

    # hero_name — if it's unset or still the instructional placeholder, use a friendly default.
    name = fact("hero_name")
    if (not name) or ("names his hero" in name.lower()) or name.lstrip().startswith("("):
        name = "a new apprentice"

    facts = dict(
        hero_name=name,
        chapters=to_int("chapters_cleared"),
        bosses=bosses,
        mini=to_int("mini_challenges_done"),
        predict=to_int("predict_wins"),
        debug=to_int("break_it_fixes"),
        hints=to_int("boss_hints_used"),
        game_complete=fact("game_complete", "no").lower().startswith("y"),
    )

    ledger = {}
    body = re.split(r"\n##+\s", ledger_text)[0]
    for nm, tag in re.findall(r"^\s*-\s*(.+?):\s*(\w+)\s*$", body, re.M):
        nm, tag = nm.strip().lower(), tag.lower()   # tolerate "Variables: Solid" etc.
        if tag in VALID_TAGS:
            ledger[nm] = tag
    return facts, ledger


def compute(facts, ledger):
    mastered = set()
    for b in facts["bosses"]:
        mastered.update(BOSS_SKILLS.get(b, []))

    level = facts["chapters"] + len(facts["bosses"])
    xp = (XP["chapter"] * facts["chapters"] + XP["mini"] * facts["mini"]
          + XP["predict"] * facts["predict"] + XP["debug"] * facts["debug"]
          + XP["boss"] * len(facts["bosses"]) + XP["hint"] * facts["hints"])
    xp = max(0, xp)

    if facts["game_complete"]:
        cls = "Code Archmage"
    else:
        n = len(facts["bosses"])
        cls = next((name for lo, hi, name in CLASS_BANDS if lo <= n <= hi), "Code Mage")

    def rank(skill):
        t = ledger.get(skill, "")
        if skill in mastered:                     return "⭐"   # proven in a boss
        if t == "solid":                          return "⚔️"
        if t in ("learning", "shaky"):            return "🌱"   # actively learning it now
        if INTRO_CH[skill] <= facts["chapters"]:  return "🌱"   # introduced (chapter cleared)
        return "🔒"                                             # not taught yet

    ranks = {s: rank(s) for s in SKILL_ORDER}

    stars = {}
    for label, skills in CLUSTERS.items():
        stars[label] = min(5, sum(1 for s in skills if ranks[s] in ("⚔️", "⭐")))
    stars["🔧 DEBUGGING (fixing errors)"] = min(5, facts["debug"])
    stars["✨ CREATIVITY (your own designs)"] = min(5, facts["mini"])

    return dict(level=level, xp=xp, cls=cls, ranks=ranks, stars=stars,
                bosses=len(facts["bosses"]), mastered=mastered)


def dwidth(s):
    """On-screen width of a string in a monospace code block. Emoji/CJK glyphs take 2
    columns; the invisible variation-selector / zero-width-joiner / combining marks they
    carry take 0. Plain `len()` miscounts these (e.g. 🛠️ and ⚔️ each hide one extra
    codepoint), which is why padding by len() left the star bars ragged — so every column
    in this sheet is measured and padded by dwidth instead."""
    w = 0
    for ch in s:
        o = ord(ch)
        if ch in ("️", "︎", "‍") or unicodedata.combining(ch):
            continue
        # ★/☆ live in the "wide" 0x2600-0x27BF block but render as 1-column text symbols
        # (no emoji presentation), so the star bars must be counted as width 1, not 2.
        if o in (0x2605, 0x2606):
            w += 1
        elif (unicodedata.east_asian_width(ch) in ("W", "F")
                or 0x1F000 <= o <= 0x1FAFF or 0x2600 <= o <= 0x27BF or o == 0x2B50):
            w += 2
        else:
            w += 1
    return w


def render(facts, c):
    star_order = [
        "🧠 LOGIC  (decisions, true/false)", "🔁 STAMINA (loops)",
        "🎒 LORE   (lists & records)", "🔧 DEBUGGING (fixing errors)",
        "✨ CREATIVITY (your own designs)",
    ]

    # --- build the inner content rows as plain text first; the box is sized to fit them
    # (so a long hero name or a future trophy can never overflow the borders). ---
    def fit(text, width):                 # left-justify to a display width
        return text + " " * max(0, width - dwidth(text))

    content = [
        f"Name: {facts['hero_name']}     Class: {c['cls']}",
        f"Level {c['level']}     XP: {c['xp']}     Bosses slain: {c['bosses']}",
    ]
    LABEL_W = 34                           # ability label column -> star bars line up
    for label in star_order:
        n = c["stars"].get(label, 0)
        # ASCII pips (filled '*', empty '.') — unlike ★/☆ these are width-1 in EVERY
        # renderer, so the right border stays straight in terminals and VS Code chat alike.
        bar = "*" * n + "." * (5 - n)
        content.append(fit(label, LABEL_W) + bar)
    spell_section = len(content)
    # spellbook is a 2-column grid; pad the first column to the WIDEST entry (+2 gap) so the
    # second column starts at the same place on every row.
    entries = [f"{c['ranks'][s]} {DISPLAY[s]}" for s in SKILL_ORDER]
    COL = max(dwidth(e) for e in entries) + 2
    for i in range(0, len(entries), 2):
        pair = entries[i:i + 2]
        content.append((fit(pair[0], COL) + (pair[1] if len(pair) > 1 else "")).rstrip())
    trophy_section = len(content)
    trophies = {"boss-01": "⚔️ Slew the Gate Guardian",
                "boss-02": "⚔️ Bested the Pit Brawler"}
    won = [trophies[b] for b in facts["bosses"] if b in trophies]
    content.extend(won if won
                   else ["(none yet — your first boss awaits after Chapter 3!)"])

    # --- size the box to the widest row, then draw every border + row to that width ---
    INNER = max(dwidth(t) for t in content) + 2     # 1 lead + >=1 trail space

    def box(t=""):
        return "║ " + fit(t, INNER - 2) + " ║"

    def divider(corner_l, corner_r, title=None):
        if title is None:
            return corner_l + "═" * INNER + corner_r
        cap = f" {title} "
        gap = INNER - dwidth(cap)
        left = gap // 2
        return corner_l + "═" * left + cap + "═" * (gap - left) + corner_r

    def section(div, rows):
        # each section is wrapped in a blank box line top and bottom for breathing room
        L.append(div)
        L.append(box())
        L.extend(box(t) for t in rows)
        L.append(box())

    L = []
    section(divider("╔", "╗", "HERO CHARACTER SHEET"), content[0:2])
    section(divider("╠", "╣", "ABILITY SCORES"), content[2:spell_section])
    section(divider("╠", "╣", "SPELLBOOK"), content[spell_section:trophy_section])
    section(divider("╠", "╣", "TROPHIES"), content[trophy_section:])
    L.append(divider("╚", "╝"))
    L.append(" ⭐ Mastered   ⚔️ Adept   🌱 Apprentice   🔒 Locked")

    body = "\n".join(L)
    full = (
        "# Hero Character Sheet\n\n"
        "Your adventurer's record — the spells you've mastered, your abilities, and the\n"
        "trophies you've won as you level up. Your Mentor keeps it updated for you; open it\n"
        "any time to see how far you've come.\n\n"
        "```\n" + body + "\n```\n"
        "<!-- Auto-generated by tools/render_sheet.py from progress.md — do not hand-edit. -->\n"
    )
    # `full` is the openable .md doc (title + intro + fenced box + comment).
    # `body` is the BARE box only — no title, no fences, no comment — so the Mentor can drop
    # it straight into a chat code block without nested-fence collisions or stray markdown.
    return full, body


def render_once(prog, sheet):
    facts, ledger = parse_progress(open(prog, encoding="utf-8").read())
    full, body = render(facts, compute(facts, ledger))
    open(sheet, "w", encoding="utf-8").write(full)
    # companion bare-box file the Mentor pastes into chat (see AGENTS.md "hero character sheet").
    bare = os.path.splitext(sheet)[0] + ".txt"
    open(bare, "w", encoding="utf-8").write(body + "\n")


def main():
    watch_mode = "--watch" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    course = args[0] if args else os.path.join(root, "python-course")
    prog = os.path.join(course, "progress.md")
    sheet = os.path.join(course, "hero-sheet.md")

    if not watch_mode:
        if not os.path.exists(prog):
            print(f"render_sheet: no progress.md at {prog}", file=sys.stderr); sys.exit(1)
        render_once(prog, sheet)
        print(f"render_sheet: wrote {sheet}")
        return

    # --watch: keep the sheet current by re-rendering whenever progress.md changes (poll its
    # modification time — no external dependencies). Started in the background by the
    # folderOpen VS Code task, so a mid-session level-up shows up within ~2s, no manual step.
    print(f"render_sheet: watching {prog} … (Ctrl+C to stop)", flush=True)
    last = None
    while True:
        try:
            mtime = os.path.getmtime(prog) if os.path.exists(prog) else None
            if mtime != last:
                last = mtime
                if mtime is not None:
                    render_once(prog, sheet)
                    print("render_sheet: rendered", flush=True)  # signals the VS Code background matcher
        except Exception as e:                       # never let a transient parse error kill the watcher
            print(f"render_sheet: {e}", file=sys.stderr, flush=True)
        time.sleep(1.5)


if __name__ == "__main__":
    main()
