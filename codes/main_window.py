from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from start_sorting import *
from start_searching import *
from sudoku import *
from nQueens import *

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
        self.dict = {"Sorting": ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"],
                     "Searching": ["Linear Search","Binary Search"],
                     "Backtracking": ["N-Queens", "Sudoku"]}
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
            Sorting(sort_window,self.algo.get())
            sort_window.mainloop()
        elif self.algoType.get() == "Searching":
            sort_window = Tk()

            #send it to start_sorting.py file
            Searching(sort_window,self.algo.get())
            sort_window.mainloop()

        elif self.algoType.get() == "Backtracking":
            if self.algo.get() == "Sudoku":
                speed = self.speed_var.get()
                self.root.destroy()
                sudoku(speed)

            else:
                speed = self.speed_var.get()
                size = self.size_var.get()
                self.root.destroy()
                N_Queens(size,speed)
    # Secondary window back button
    def Back(self):
        if getattr(self, "_backing_out", False):
            return

        self._backing_out = True
        self.root.destroy()
        import Start_Threading
        Start_Threading.open_main_window()

    def Run1(self):
        #if nothing is selected show an error
        if self.algoType.get() == "Select Algorithm Type":
            messagebox.showerror("Error!", "Please select an Algorithm type.")

        #if sorting is selected
        elif self.algoType.get() == "Sorting":
            #destroy the main window
            self.root.destroy()

            #go to the Run() function
            self.Run2()

        #if searching is selected
        elif self.algoType.get() == "Searching":
            #destroy the main window
            self.root.destroy()

            #go to the Run function
            self.Run2()

        # if backtracking is selected
        elif self.algoType.get() == "Backtracking":
            #create a new window
            self.root.destroy()
            self.root = Tk()

            # if sudoku is selected
            if self.algo.get() == "Sudoku":
                #size of the window
                wx,wy = 300,150

                #fit the window at the center of the screen
                wxs,wys = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
                WindowX,WindowY = (wxs / 2) - (wx / 2), (wys / 2) - (wy / 2)

                self.root.geometry('%dx%d+%d+%d' % (wx, wy, WindowX, WindowY))
                self.root.wm_resizable(False,False)

                #title of the window
                self.root.title("Sudoku Solver")

                #create a new frame for the speed slider and buttons
                frame = Frame(self.root,width=300, height=150, bg="aquamarine")
                frame.grid_propagate(0)
                frame.pack()

                #slider for speed
                self.speed_var = Scale(frame,label="Select Speed of Visualizer: ", from_ = 1, to= 100, orient= HORIZONTAL,
                                       length=230,bg="powder blue", troughcolor="blue", relief="solid")
                self.speed_var.place(relx = 0.12, rely=0.06)
                self.speed_var["highlightthickness"] = 0

                #button for starting visualizer
                next = Button(frame,text="Next>", bg="pale green", activebackground="lime green", command=self.Run2)
                next.place(relx=0.55, rely=0.66)

                #button for main menu
                back = Button(frame, text="<Back", bg="pale green", activebackground="lime green", command=self.Back) 
                back.place(relx=0.35, rely=0.65) 
                self.root.mainloop()

            elif self.algo.get() == "N-Queens":
                wx, wy = 300, 200
                # fit the window at the centre of the screen
                wxs, wys = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
                WINDOW_X, WINDOW_Y = (wxs / 2) - (wx / 2), (wys / 2) - (wy / 2)
                self.root.geometry('%dx%d+%d+%d' % (wx, wy, WINDOW_X, WINDOW_Y))
                self.root.wm_resizable(False, False)
                # title of the window
                self.root.title("N-Queens Solver Visualizer")

                #create frame for speed slider and button 
                frame = Frame(self.root,width=300, height=200, bg="aquamarine")
                frame.grid_propagate(0)
                frame.pack()
                self.size_var = Scale(frame, label="Select Size of the Chessboard :", from_=4, to=25,
                                        orient=HORIZONTAL,length=230, bg="powder blue", troughcolor="SteelBlue2", relief="solid") 
                self.size_var.place(relx=0.12, rely=0.06)
                self.size_var["highlightthickness"] = 0
                 # slider for speed
                self.speed_var = Scale(frame, label="Select Speed Of Visualizer :", from_=1, to=100, orient=HORIZONTAL,
                                       length=230, bg="powder blue", troughcolor="SteelBlue2", relief="solid",
                                       cursor="hand2")
                self.speed_var.place(relx=0.12, rely=0.4)
                self.speed_var["highlightthickness"] = 0
                # button for starting visualizer
                next = Button(frame, text="Next>", bg="pale green", activebackground="lime green",
                              command=self.Run2)
                next.place(relx=0.55, rely=0.8)
                # button for main menu
                back = Button(frame, text="<Back", bg="pale green", activebackground="lime green",
                              command=self.Back)
                back.place(relx=0.25, rely=0.8)
                self.root.mainloop()