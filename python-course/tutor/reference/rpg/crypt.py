"""
crypt.py -- THE CRYPT OF BROKEN KEYS

Tutor-only reference solution for Chapter 20 (the capstone) -- and the
CUMULATIVE reference for the whole python-course: one complete run of the
RPG, assembled from every piece taught in Chapters 1-19. NEVER shown to the
student (root AGENTS.md hard rule 10) -- use only to shape hints and judge
his build. His game will differ in the details (names, dialogue, maze,
class choices) -- that's correct; what matters is the same pieces, wired
together: title screen, hero creation, a walkable maze, a combat encounter,
a conversation encounter, a locked door, save/load, and two endings.

Skills used, all earlier chapters, nothing forward-referenced: dictionaries
(9), functions + parameters (10), return values (11), random (12), 2D
lists + nested loops (14), nested if + dialogue dict + story flags (15),
file open/write/read/close (16), try/except ValueError + .strip() + input
validation (17).

Needs no asset file to run: the maze below is the SAME data as the given
tutor/assets/maze_layout.py, copied in as plain data so this file is
standalone. His own game instead writes `from maze_layout import MAZE`
after copying that asset in, exactly as Chapter 14 taught -- and Chapter
14's `controls.py` (`get_key()`) can replace the input()-based moves below
for real no-ENTER w/a/s/d play; this reference uses input() so it can be
tested with plain typed lines. Run: python3 crypt.py
"""

import random

# THE DUNGEON MAP (Chapter 14) -- a list of rows, read as maze[row][col].
WALL = "#"
FLOOR = "."
START = "@"
ENEMY = "E"
PERSON = "N"
DOOR = "D"
EXIT = "X"

MAZE_TEMPLATE = [
    "##########",
    "#@..#...E#",
    "#.#.#.##.#",
    "#.#...#N.#",
    "#.####.#.#",
    "#....D..X#",
    "##########",
]

def find_start(grid):
    """Nested for loop over the grid: return the [row, col] of '@'."""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == START:
                return [row, col]
    return [1, 1]

def clear_screen():
    # A cheap screen-wipe: push everything up out of view with blank lines.
    # In real play you'd call this after every step of walk_maze() so the
    # map redraws in the same spot (Chapter 14). Called only once here, at
    # the title, so a piped test run of this file stays easy to read.
    print("\n" * 50)

# SETUP -- title screen and hero creation (Chapters 1, 2, 4, 9).
def title_screen():
    clear_screen()
    print("=" * 44)
    print("     THE CRYPT OF BROKEN KEYS")
    print("=" * 44)
    print("A locked door. A wandering monster. A hermit with a riddle.")
    print("Somewhere below, the crypt still keeps its last key.\n")

def make_hero():
    """Ask the player's name and class, build the hero record (Ch 9)."""
    name = input("What is your hero's name? ").strip()
    if name == "":
        name = "Aldric"          # a friendly default -- never crash on blank input

    print("Choose a class: (1) Warrior  (2) Rogue")
    choice = input("> ").strip()
    if choice == "2":
        cls = "Rogue"
        hp = 24
        attack = 5
    else:
        cls = "Warrior"                      # anything but "2" -- a safe default
        hp = 30
        attack = 7

    hero = {
        "name": name, "cls": cls, "hp": hp, "max_hp": hp,
        "attack": attack, "gold": 0, "has_key": False,
    }
    print(f"\n{hero['name']} the {hero['cls']} enters the crypt. "
          f"HP {hero['hp']}/{hero['max_hp']}.\n")
    return hero

# COMBAT -- functions that answer, and real dice (Chapters 10, 11, 12).
MONSTERS = [
    {"name": "Goblin", "attack": 4, "hp": 12, "gold": 5},
    {"name": "Skeleton", "attack": 5, "hp": 10, "gold": 6},
    {"name": "Giant Rat", "attack": 2, "hp": 6, "gold": 2},
    {"name": "Cave Troll", "attack": 7, "hp": 20, "gold": 15},
]

def roll_damage(attacker):
    """RETURN a random hit built from the attacker's attack stat (Ch 11/12)."""
    low = max(1, attacker["attack"] - 2)
    high = attacker["attack"] + 2
    return random.randint(low, high)

def is_alive(fighter):
    """RETURN True while a fighter still has HP left (Ch 11)."""
    return fighter["hp"] > 0

def battle(hero):
    """A random monster steps out of the dark (Ch 12). Fight to the end."""
    picked = random.choice(MONSTERS)
    # Build a fresh dict field by field -- a copy, so the roster's own
    # monster record never gets hurt when we subtract HP from it below.
    enemy = {
        "name": picked["name"],
        "attack": picked["attack"],
        "hp": picked["hp"],
        "gold": picked["gold"],
    }
    print(f"A {enemy['name']} blocks the way! (HP {enemy['hp']})")

    while is_alive(hero) and is_alive(enemy):
        dmg = roll_damage(hero)
        enemy["hp"] -= dmg
        print(f"You strike the {enemy['name']} for {dmg}.")
        if not is_alive(enemy):
            break                              # it fell -- it doesn't get a last swing
        dmg = roll_damage(enemy)
        hero["hp"] -= dmg
        print(f"The {enemy['name']} hits back for {dmg}. (HP {max(hero['hp'], 0)})")

    if is_alive(hero):
        hero["gold"] += enemy["gold"]
        print(f"You defeated the {enemy['name']} and found {enemy['gold']} gold!\n")
        return True
    hero["hp"] = 0
    print(f"\n{hero['name']} has fallen in the dark...\n")
    return False

# CONVERSATION -- a dialogue dict and a story flag (Chapter 15).
HERMIT_LINES = {
    "1": "The hermit smiles: \"Kindness opens more doors than force, adventurer.\"",
    "2": "The hermit frowns: \"Then find your own way through the dark.\"",
}

def talk(hero):
    """The Hermit of the Crypt: answer kindly and he hands over the key."""
    print("\nAn old hermit blocks the path. \"Answer me true,\" he says,")
    print("\"and the rusty key to the far door is yours.\"")
    print("(1) Speak kindly and ask for his help.")
    print("(2) Demand the key.")
    choice = input("> ").strip()

    if choice == "1" or choice == "2":
        print(HERMIT_LINES[choice])
    else:
        print("The hermit waits, unimpressed. That wasn't an answer at all.")
        choice = "2"              # a silly reply counts as rude, not a crash

    if choice == "1":
        print("He presses a small rusty key into your hand.\n")
        hero["has_key"] = True    # the flag later code (the door, the ending) reads
    else:
        print("He turns away and says nothing more.\n")
        hero["has_key"] = False

# THE DUNGEON -- 2D list, nested loops, coordinates, collision (Chapter 14).

def draw_map(grid, pos):
    """Nested for loop: print every row, swapping the hero's cell for '@'."""
    for r in range(len(grid)):
        line = ""
        for c in range(len(grid[r])):
            line += START if [r, c] == pos else grid[r][c]
        print(line)

def walk_maze(hero):
    """Walk the crypt. Returns 'exit', 'quit' or 'dead'."""
    # A mutable copy we can edit as he explores -- for loop + append,
    # turning each row STRING into its own list of characters.
    grid = []
    for row in MAZE_TEMPLATE:
        row_chars = []
        for ch in row:
            row_chars.append(ch)
        grid.append(row_chars)

    pos = find_start(grid)
    grid[pos[0]][pos[1]] = FLOOR                  # the start square is just floor underneath

    print("Move with w (up) a (left) s (down) d (right). q saves and quits.\n")
    draw_map(grid, pos)

    while True:
        key = input("move> ").strip().lower()

        # Work out the TARGET square from the key -- one if/elif per
        # direction, same pattern as Chapter 14. Anything else stays put.
        if key == "q":
            return "quit"
        elif key == "w":
            target = [pos[0] - 1, pos[1]]
        elif key == "s":
            target = [pos[0] + 1, pos[1]]
        elif key == "a":
            target = [pos[0], pos[1] - 1]
        elif key == "d":
            target = [pos[0], pos[1] + 1]
        else:
            target = None

        if target == None:
            print("That's not a direction I know. Try w a s d, or q.")
        else:
            cell = grid[target[0]][target[1]]

            if cell == WALL:                      # check BEFORE moving -- collision (Ch 14)
                print("A solid wall. No way through.")
            elif cell == DOOR and not hero["has_key"]:
                print("The door is locked. You need a key.")
            else:
                pos = target                       # the move is allowed -- step onto it

                if cell == DOOR:
                    print("The rusty key turns. The door creaks open.")
                    grid[pos[0]][pos[1]] = FLOOR
                elif cell == ENEMY:
                    grid[pos[0]][pos[1]] = FLOOR   # this fight only happens once
                    if not battle(hero):
                        return "dead"
                elif cell == PERSON:
                    grid[pos[0]][pos[1]] = FLOOR   # this chat only happens once
                    talk(hero)
                elif cell == EXIT:
                    return "exit"

                draw_map(grid, pos)

# THE ENDING -- decided by his flags and HP (Chapters 5, 11, 15).
def ending(hero):
    print("\n" + "=" * 44)
    if hero["has_key"] and is_alive(hero):
        print(f"{hero['name']} unlocks the far door and finds the crypt's")
        print("hoard glittering in torchlight.       *** THE GOLDEN ENDING ***")
    else:
        print(f"{hero['name']} slips past the crypt's secrets and out into")
        print("daylight, alive but empty-handed.      *** THE NARROW ESCAPE ***")
    print(f"Final gold: {hero['gold']}")
    print("=" * 44 + "\n")

# SAVE CRYSTAL -- files (Ch 16), guarded against missing/bad data (Ch 17).
SAVE_FILE = "save.txt"

def save_game(hero):
    f = open(SAVE_FILE, "w")
    f.write(f"{hero['name']}\n")
    f.write(f"{hero['cls']}\n")
    f.write(f"{hero['hp']}\n")
    f.write(f"{hero['max_hp']}\n")
    f.write(f"{hero['attack']}\n")
    f.write(f"{hero['gold']}\n")
    f.write(f"{hero['has_key']}\n")
    f.close()
    print("The save crystal glows. Your progress is stored.\n")

def load_game():
    """Read the save file back into a hero dict. None if it can't be read."""
    try:
        f = open(SAVE_FILE)
        lines = []
        for line in f:
            lines.append(line.strip())
        f.close()
        hero = {
            "name": lines[0], "cls": lines[1],
            "hp": int(lines[2]), "max_hp": int(lines[3]),
            "attack": int(lines[4]), "gold": int(lines[5]),
            "has_key": lines[6] == "True",
        }
        print(f"The crystal remembers {hero['name']}. Welcome back.\n")
        return hero
    except FileNotFoundError:
        print("No save crystal found yet -- starting a new adventure.\n")
        return None
    except ValueError:
        print("The save crystal is cracked and unreadable -- starting fresh.\n")
        return None
    except IndexError:
        print("The save crystal is cracked and unreadable -- starting fresh.\n")
        return None

# THE MENU -- validated, safety-netted (Chapter 17).
def main_menu():
    while True:
        print("1) New Game   2) Load Game   3) Quit")
        raw = input("> ").strip()
        try:
            choice = int(raw)
            if choice in [1, 2, 3]:
                return choice
            print("That's not one of the choices. Try again.")
        except ValueError:
            print("Numbers only, please -- 1, 2 or 3.")

def main():
    title_screen()
    while True:
        choice = main_menu()
        if choice == 3:
            print("Farewell, adventurer.")
            return
        if choice == 2:
            hero = load_game()
        else:
            hero = make_hero()

        if hero != None:                          # None means nothing was loaded
            result = walk_maze(hero)
            if result == "exit":
                ending(hero)
                save_game(hero)
                return
            if result == "dead":
                print("Game over -- your crystal was not updated.\n")
                return
            if result == "quit":
                save_game(hero)
                print("Until next time, adventurer.\n")
                return
            # else: back to the top of the loop -- nothing to load, ask again

if __name__ == "__main__":
    main()
