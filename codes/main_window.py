from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from start_sorting import *
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

        #creating a style
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(
            "TCombobox",
            fieldbackground="#BE8337",  # Input area background
            background="#8F6A55",       # Dropdown arrow area
            foreground="#363636",       # Text color
            arrowcolor="white"        # Arrow color
        )

        # Set dropdown list colors
        root.option_add("*TCombobox*Listbox.background", "#FFF2E1")
        root.option_add("*TCombobox*Listbox.foreground", "#333333")
        root.option_add("*TCombobox*Listbox.selectBackground", "#7FA7A6")
        root.option_add("*TCombobox*Listbox.selectForeground", "#FFFFFF")
        #two dropdown menu
        self.AlgoTypeList = ttk.Combobox(self.root,textvariable=self.algoType,values=list(self.dict.keys()))
        
        self.AlgoTypeList.set("Select Algorithm Type")
        self.AlgoTypeList.place(x = 250, y = 200)

        #binding line
        self.AlgoTypeList.bind("<<ComboboxSelected>>",self.update_options)

        #second combobox
        self.AlgoName = ttk.Combobox(self.root,textvariable=self.algo,values=[],state="readonly")
        self.AlgoName.set("Select Algorithm")
        self.AlgoName.place(x = 250 , y = 250)

        #next button
        self.next_button = Button(self.root,text="Next",width=10,bg="#7FA7A6",command=self.Run1)
        self.next_button.place(x=270, y=290)

    #for automatic update on the 2nd list if something is chosen on the 1st list
    def update_options(self,event = None):
        algo_list = self.dict.get(self.AlgoTypeList.get(),[])

        self.AlgoName.set("Select Algorithm")
        self.AlgoName['values'] = algo_list


    # for running the algorithms
    def Run2(self):
        #if sorting is selected
        if self.algoType.get() == "Sorting":
            #create a new window for sorting algorithm
            sort_window = Tk()

            #send it to start_sorting.py file
            Sorting(sort_window,self.algoType.get())
            sort_window.mainloop()

    def Run1(self):
        #if nothing is selected show an error
        if self.algoType.get() == "Select Algorithm Type":
            messagebox.showerror("Please select an Algorithm Type.")

        #if sorting is selected
        elif self.algoType.get() == "Sorting":
            #destroy the main window
            self.root.destroy()

            #go to the Run() function
            self.Run2()

root = Tk()
app = Window(root)
root.mainloop()
        