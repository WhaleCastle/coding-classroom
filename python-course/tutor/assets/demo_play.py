"""
demo_play.py  —  a PLAYABLE trailer for *The Crypt of Broken Keys*.

This is a PRE-MADE ASSET, like the hero sprite. It exists so the student can
PLAY a few-minute taste of the kind of game he's going to build — a title
screen, naming his hero, walking a dungeon, a goblin fight, a choice that
changes the ending. He plays it; he does NOT read it to learn from, and he is
NEVER asked to write code like this. It's a trailer, not the syllabus.

The tutor may offer it on day one ("here's where we're heading") and again at
milestones (after combat in Ch 6, after the maze in Ch 14) to keep the goal
vivid.

Run it:  python demo_play.py
Pure Python 3 — no libraries to install.

Controls: type a letter then press ENTER.
    w / a / s / d  = move up / left / down / right
    c              = show your character sheet
    q              = quit the demo
"""

import random

# ---------------------------------------------------------------------------
# The dungeon. Each string is a row; each character is one cell.
#   #=wall  .=floor  @=start  G=goblin  H=hermit (talk)  X=exit
# The '#' walls are DRAWN as joined lines (┌ ─ ┐ │ └ ┘ ├ ┤ ┬ ┴ ┼) so the maze
# is easy to read; floors are shown as blank space.
# ---------------------------------------------------------------------------
MAZE = [
    "#####################",
    "#@..#...........#...#",
    "###.#####.#####.###.#",
    "#.#.....#...#...#G..#",
    "#.#####.#.#.#.###.###",
    "#.....#.#.#.#...#...#",
    "#.#####.#.#.###.###.#",
    "#...#...#.#...#.#...#",
    "#.#.#.###.###.#.#.###",
    "#.#.#...#...#.#.#...#",
    "###.###.###.#.#.###.#",
    "#..H#...#...#.#...#.#",
    "#.###.#######.###.#.#",
    "#.............#....X#",
    "#####################",
]

WALKABLE = set(".@GHX")

# Which box-drawing line to draw for a wall, based on which of its four
# neighbours (up, down, left, right) are also walls.
_LINES = {
    (False, False, False, False): "•",
    (True,  False, False, False): "│", (False, True,  False, False): "│",
    (False, False, True,  False): "─", (False, False, False, True):  "─",
    (True,  True,  False, False): "│", (False, False, True,  True):  "─",
    (False, True,  False, True):  "┌", (False, True,  True,  False): "┐",
    (True,  False, False, True):  "└", (True,  False, True,  False): "┘",
    (True,  True,  False, True):  "├", (True,  True,  True,  False): "┤",
    (False, True,  True,  True):  "┬", (True,  False, True,  True):  "┴",
    (True,  True,  True,  True):  "┼",
}


def _is_wall(r, c):
    return 0 <= r < len(MAZE) and 0 <= c < len(MAZE[r]) and MAZE[r][c] == "#"


def wall_glyph(r, c):
    """Pick the line character that connects this wall to its wall neighbours."""
    return _LINES[(_is_wall(r - 1, c), _is_wall(r + 1, c),
                   _is_wall(r, c - 1), _is_wall(r, c + 1))]


def find(symbol):
    """Return the [row, col] of the first cell holding `symbol`."""
    for r, row in enumerate(MAZE):
        c = row.find(symbol)
        if c != -1:
            return [r, c]
    return [1, 1]


def draw(hero, pos, defeated, spoken):
    """Print the dungeon with walls as joined lines and the hero as '@'."""
    print("\n" * 2)
    for r, row in enumerate(MAZE):
        line = ""
        for c, cell in enumerate(row):
            if [r, c] == pos:
                line += "@"
            elif cell == "#":
                line += wall_glyph(r, c)
            elif cell == "G" and (r, c) not in defeated:
                line += "G"
            elif cell == "H" and (r, c) not in spoken:
                line += "H"
            elif cell == "X":
                line += "X"
            else:                       # floor, or a feature already cleared
                line += " "
        print("  " + line)
    print(f"  {hero['name']} the {hero['cls']}   HP {hero['hp']}/{hero['max_hp']}")
    print("  lines = walls   @ you   G goblin   H hermit   X exit")
    print("  (w/a/s/d move, c sheet, q quit)")


def show_sheet(hero):
    print("\n  ┌─ CHARACTER SHEET ─────────────┐")
    print(f"  │  {hero['name']:<18}{hero['cls']:>10} │")
    print(f"  │  HP     : {hero['hp']:>3} / {hero['max_hp']:<14}│")
    print(f"  │  Attack : {hero['attack']:<19}│")
    print(f"  │  Bag    : {', '.join(hero['bag']) or '(empty)':<19}│")
    print("  └───────────────────────────────┘")


def fight(hero):
    """A short turn-based goblin fight."""
    goblin = 12
    print("\n  A GOBLIN leaps from the shadows!  (HP 12)")
    while goblin > 0 and hero["hp"] > 0:
        input("  Press ENTER to swing your weapon...")
        hit = hero["attack"] + random.randint(0, 4)
        goblin -= hit
        print(f"  You strike for {hit}!  Goblin HP: {max(goblin, 0)}")
        if goblin <= 0:
            break
        bite = random.randint(2, 5)
        hero["hp"] -= bite
        print(f"  The goblin bites for {bite}.  Your HP: {max(hero['hp'], 0)}")
    if hero["hp"] <= 0:
        return False
    print("  ★ The goblin falls! You find a Rusty Key. ★")
    hero["bag"].append("Rusty Key")
    return True


def talk(hero):
    """A conversation whose choice sets the ending."""
    print("\n  An OLD HERMIT looks up. \"Free me, kind soul... or take my")
    print("  lantern and leave. Choose what kind of hero you are.\"")
    while True:
        choice = input("  [1] Free him   [2] Take the lantern: ").strip()
        if choice == "1":
            print("  Hermit: \"Bless you. Mercy opens more than locks.\"")
            hero["mercy"] = True
            return
        if choice == "2":
            print("  You snatch the lantern. The hermit sighs in the dark.")
            hero["bag"].append("Lantern")
            hero["mercy"] = False
            return
        print("  (Type 1 or 2.)")


def ending(hero):
    print("\n  You reach the cracked door and step through...\n")
    if hero.get("mercy"):
        print("  ★  GOOD ENDING  ★")
        print("  Because you showed mercy in the dark, the curse lifts.")
        print(f"  {hero['name']} walks into the sun, a true hero.")
    else:
        print("  ☠  SHADOW ENDING  ☠")
        print("  You escape with the lantern, but the crypt's chill follows")
        print(f"  {hero['name']} home, and never quite leaves.")


def main():
    # ---- title ----
    print("=" * 44)
    print("        THE CRYPT OF BROKEN KEYS  (demo)")
    print("=" * 44)
    name = input("Name your hero: ").strip() or "Hero"
    cls = input("Class (warrior/mage/rogue): ").strip() or "warrior"
    hero = {
        "name": name, "cls": cls,
        "hp": 30, "max_hp": 30, "attack": 7,
        "bag": [], "mercy": None,
    }
    print(f"\nWelcome, {name} the {cls}. Find the exit (X).")

    pos = find("@")
    defeated = set()
    spoken = set()

    while True:
        draw(hero, pos, defeated, spoken)
        cmd = (input("> ").strip().lower() + " ")[0]
        if cmd == "q":
            print("You step back out of the crypt. (demo ended)")
            return
        if cmd == "c":
            show_sheet(hero)
            continue

        move = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}.get(cmd)
        if not move:
            print("  (Use w, a, s, d to move.)")
            continue

        nr, nc = pos[0] + move[0], pos[1] + move[1]
        if MAZE[nr][nc] not in WALKABLE:
            print("  A wall blocks your way.")
            continue
        pos = [nr, nc]

        cell = MAZE[nr][nc]
        here = (nr, nc)
        if cell == "G" and here not in defeated:
            if not fight(hero):
                print(f"\n  ☠ {hero['name']} has fallen in the dark. GAME OVER.")
                return
            defeated.add(here)
        elif cell == "H" and here not in spoken:
            talk(hero)
            spoken.add(here)
        elif cell == "X":
            ending(hero)
            return


if __name__ == "__main__":
    main()
