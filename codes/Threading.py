from tkinter import *
from main_window import Window
from threading import *


class START(Thread):
    def run(self):
        root = Tk()
        Window(root)
        root.mainloop()