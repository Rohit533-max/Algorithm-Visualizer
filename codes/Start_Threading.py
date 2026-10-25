from tkinter import Tk

def open_main_window():
    from main_window import Window
    root = Tk()
    Window(root)
    root.mainloop()