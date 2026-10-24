from tkinter import *
from threading import *

class START(Thread):
    def run(self):
        from main_window import Window
        root = Tk()
        Window(root)
        root.mainloop()