"""
maze_layout.py  —  the dungeon map for *The Crypt of Broken Keys*.

This is a PRE-MADE ASSET. In Chapter 14 the student is GIVEN this file so he
doesn't have to hand-design a big grid — his job is to write the engine that
DRAWS it, MOVES the hero through it, and stops him walking through walls.

The maze is a 2D array: a list of rows, where each row is a line of single
characters. You read a cell with two indexes — row first, then column:

    MAZE[row][col]        # row 0 is the top, col 0 is the left

Legend
    #  wall   (you cannot walk here)
    .  floor  (you can walk here)
    @  the hero's START square (also walkable floor)
    E  an enemy  -> triggers a combat encounter
    N  a person  -> triggers a conversation
    D  a door    -> needs a key
    X  the exit  -> ends the adventure

Customising it (optional): change the characters below to redraw the dungeon.
Keep every row the SAME length and keep the outer ring all '#' so the hero can
never escape the map.
"""

# The map. Each string is one row; each character is one cell.
MAZE = [
    "##########",
    "#@..#...E#",
    "#.#.#.##.#",
    "#.#...#N.#",
    "#.####.#.#",
    "#....D..X#",
    "##########",
]

# Handy named symbols so engine code reads clearly (e.g. cell == WALL).
WALL = "#"
FLOOR = "."
START = "@"
ENEMY = "E"
PERSON = "N"
DOOR = "D"
EXIT = "X"

# Everything the hero is allowed to step onto.
WALKABLE = (FLOOR, START, ENEMY, PERSON, DOOR, EXIT)


def find_start(maze):
    """Return the (row, col) of the '@' start square."""
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == START:
                return (row, col)
    return (1, 1)  # fallback if no '@' is drawn


if __name__ == "__main__":
    # Quick self-check: print the map and the start position.
    for line in MAZE:
        print(line)
    print("start at", find_start(MAZE))
