"""
controls.py  —  single-key controls for *The Crypt of Broken Keys*.

This is a PRE-MADE ASSET. In Chapter 14 the student is GIVEN this file so his
maze can react the moment a key is pressed — no ENTER needed. Reading one raw
keypress needs different low-level code on Windows (`msvcrt`) and Mac/Linux
(`termios`), which is well outside the KS3–4 syllabus — that is exactly why it
lives here as a finished tool and is NEVER something the student writes or
reads the insides of.

He uses it with ONE line, just like `import random`:

    from controls import get_key

    key = get_key()        # waits for a single keypress, returns it lowercase

Copy this file into your chapter folder next to your maze program so the
import can find it.
"""

import sys


def get_key():
    """Read ONE keypress and return it as a lowercase letter — WITHOUT the
    player pressing ENTER."""
    try:
        import msvcrt                       # Windows
        ch = msvcrt.getch()
        if ch in (b"\x00", b"\xe0"):        # arrow / function keys send two bytes
            msvcrt.getch()                  # swallow the second byte
            return ""
        if ch == b"\x03":                   # Ctrl+C
            raise KeyboardInterrupt
        return ch.decode(errors="ignore").lower()
    except ImportError:
        import termios, tty                 # Mac / Linux
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        if ch == "\x03":                    # Ctrl+C
            raise KeyboardInterrupt
        return ch.lower()


if __name__ == "__main__":
    print("Press any key (q to quit)…")
    while True:
        k = get_key()
        print(f"you pressed: {k}")
        if k == "q":
            break
