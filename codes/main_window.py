from tkinter import *
from tkinter import ttk
class Window:
    def __init__(self,root):
        self.root = root
        root.title("Algorithm visualizer")
        root.configure(bg = "#E6D7C3")

        #width dimension
        width = 600
        height = 500

        #Get screen dimenstions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        #calculate center position
        x = (screen_width - width) //2
        y = (screen_height - height) //2

        #set window size and position
        root.geometry(f"{width}x{height}+{x}+{y}")

        #dictionary of algorithms and their list
        self.dict = {"Sorting": ["Bubble sort", "Selection sort", "Insertion sort", "Merge sort", "Quick sort"],
                     "Searching": ["Linear Search","Binary Search"]}
        #two dropdown
        self.algoType = StringVar()
        self.algo = StringVar()
        #two dropdown menu
        self.AlgoTypeList = ttk.Combobox(self.root,textvariable=self.algoType,values=list(self.dict.keys()))
        self.AlgoTypeList.set("Select Algorithm Type")
        self.AlgoTypeList.pack(pady =20)

        self.AlgoName = ttk.Combobox(self.root,textvariable=self.algo,values="None")
        self.AlgoName.set("Select the Algorithm")
        self.AlgoName.pack(pady = 20)


        
root = Tk()
app = Window(root)
root.mainloop()
        