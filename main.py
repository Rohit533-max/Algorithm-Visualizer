import os
import sys
from tkinter import Tk

# Make sure the /codes folder is importable
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CODES_DIR = os.path.join(ROOT_DIR, "codes")

if CODES_DIR not in sys.path:
    sys.path.insert(0, CODES_DIR)

from codes.main_window import Window


def main():
    root = Tk()
    Window(root)
    root.mainloop()


if __name__ == "__main__":
    main()