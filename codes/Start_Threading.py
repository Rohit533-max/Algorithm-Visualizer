from tkinter import *
from main_window import Window
from threading import *


class begin(Thread):
    def run(self):
        root = Tk()
        Window(root)
        root.mainloop()