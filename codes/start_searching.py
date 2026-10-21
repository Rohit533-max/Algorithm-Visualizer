from tkinter import *
from tkinter import messagebox
from searching import algochooser
from random import sample, shuffle
from threading import *

class Searching:
    def __init__(self,root,AlgonameVar):
        self.root = root

        #selected algorithm name
        self.AlgonameVar = AlgonameVar

        #window size
        width = 1200
        height= 700
        root.title("Searching Algorithm")

        #screen size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        #calculating the center
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        #set the screen
        root.geometry(f"{width}x{height}+{x}+{y}")

        #searching canvas size
        self.CanvasX = 800
        self.CanvasY = 700

        #Left side information frame size
        self.FrameX = 400
        self.FrameY = 700

        #starting array size
        self.size_var = IntVar()
        self.size_var.set(20)

        #starting speed 
        self.speed_var = IntVar()
        self.speed_var.set(10)

        #creating a frame in the left side
        self.Frame1 = Frame(root,width=self.FrameX, height=self.FrameY, bg= "Yellow")
        self.Frame1.pack(side="left")

        #starting point
        self.start_point = 2
        # Algorithm Information Table
        self.information = {'Linear Search': "Worst Case:O(n)\nAverage Case:O(n/2)\nBest Case:O(1)",
                            'Binary Search': "Worst Case:O(log n)\nAverage Case:O(log n)\nBest Case:O(1)"}

        # Alorithm name
        self.algorithm = ['Linear Search', 'Binary Search']

        #creating a frame for new buttons
        self.frame_btn1 = Frame(self.Frame1, width= 230, height= 40, bg = 'light salmon')
        self.frame_btn1.pack_propagate(0)
        self.frame_btn1.place(relx= 0.0, rely=0.14)

        # Button for generating new array
        self.arr_btn = Button(self.frame_btn1, text= "Generate", padx= 13, pady=3,bg='RoyalBlue', fg='azure',cursor="hand2")
        self.arr_btn.place(relx=0.15, rely=0.14)

        # Button for shuffle array
        self.sfl_btn = Button(self.frame_btn1, text = "Shuffle", padx=13, pady = 3, bg='RoyalBlue',fg='azure',cursor='hand2')
        self.sfl_btn.place(relx=0.60, rely=0.14)

        #text box for the search entry
        self.search_element = Entry(self.Frame1, width=26, bg= "white", fg="black")
        self.search_element.insert(END,'Enter an element to search: ')
        self.search_element.pack_propagate(0)
        self.search_element.place(relx=0.22, rely=0.22)

        # label for showing the number of comparisions
        self.label_comparision = Label(self.Frame1, text= "Number of comparisions: 0", bg= "light salmon", fg="midnight blue")
        self.label_comparision.place(relx=0.1, rely=0.65)

        # label for showing the searched element index
        self.label_index = Label(self.Frame1, width= 5 ,text = "", bg = "light salmon")
        self.label_index.place(relx=0.2, rely=0.58)

        #Frame for algorithm info
        self.algo_info = Frame(self.Frame1, bg = "tomato", width=230, height=150, relief="sunken",bd=4)
        self.algo_info.grid_propagate(0)
        self.algo_info.place(relx=0.03, rely=0.7)

        # # Label for algorithm info
        # self.algo_label = Label(self.algo_info, bg="tomato", fg = "white", text= self.information[self.AlgonameVar.get()])
        # self.algo_label.pack_propagate(0)
        # self.algo_label.place(relx=0.06, rely=0.25)

        #Back button
        self.back_btn = Button(self.Frame1, bg= "RoyalBlue", fg="white", text= "Back")
        self.back_btn.pack_propagate(0)
        self.back_btn.place(relx=0.2, rely=0.94)

        # Canvas for the graph
        self.Frame2 = Frame(self.root, width= self.CanvasX, height= self.CanvasY)
        self.Frame2.pack(side="left")
        self.canva = Canvas(self.Frame2, width= self.CanvasX, height= self.CanvasY, bg= "light goldenrod")
        self.canva.pack()

        # creating new array
        self.numbers = sample(range(20, self.CanvasY - 20), self.size_var.get())
        shuffle(list(set(self.numbers)))
        self.rec_width = self.CanvasX // self.size_var.get()

        for num in self.numbers:
            self.canva.create_rectangle(self.start_point, self.CanvasY - num, self.start_point + self.rec_width,
                                        self.CanvasY, fill = "sandy brown")
            self.label_value = Label(self.canva,text = num, bg="sandy brown", fg="white")
            self.canva.create_window(self.start_point + 16, self.CanvasY - num +12, window=self.label_value)
            self.start_point += self.rec_width

        # Creating the search button
        self.search_btn = Button(self.Frame1, text="Search", padx= 13, pady=3, bg="RoyalBlue", fg="azure")
        self.search_btn.place(relx=0.20, rely=0.05)


    #Function for back button to main window
    def back(self):
        pass

    # Function for painting the bars
    def paint(self,colortype):
        #delete the previous graph
        self.canva.delete("all")

        #start painting from here
        self.start_point = 2

        # width of each bar
        for i in range(len(self.numbers)):
            self.canva.create_rectangle(
                self.starting_point, self.CanvasY - self.numbers[i], self.start_point + self.rec_width, self.CanvasY, fill=colortype[i])
            self.label_value = Label(self.canva,text= self.numbers[i], bg="sandy brown", fg="white")
            self.canva.create_window(self.start_point + 16, self.CanvasY - self.numbers[i] +12, window=self.label_value)
            self.start_point += self.rec_width

        # upgdate the graph frame
        self.Frame2.update()

    # Function for creating a new list
    def new_list(self):
        numbers = []
        self.label_comparision.configure(text = "Number of comparisions: 0")
        self.lable_index.configure(text="")
        # enter random numbers in the new array

        self.numbers = sample(range(20, self.CanvasY - 20), self.speed_var.get())

        # shuffle the numbers
        shuffle(list(set(numbers)))
        colortype = ['sandy brown' for x in self.numbers]
        # paint the colored array
        self.paint(colortype)

    #Function for shuffling the array
    def shuffle_list(self):
        shuffle(self.numbers)
        self.label_comparision.configure(text="Number of comparisions: 0")
        self.lable_index.configure(text="")

        colortype = ['sandy brown' for x in self.numbers]
        self.paint(colortype)

    def search_list(self):
        self.label_comparision.configure(text="Number of Comparisions: 0")
        self.label_index.configure(text="")
        print(self.search_element.get(),self.AlgonameVar.get())
        if self.search_element.get().isdigit():
            startsearch = Thread(target=algochooser, args=(self.numbers,self.paint,self.label_comparision,self.label_index,"Linear Search",self.speed_var.get(),self.search_element.get()))
            startsearch.start()
        else:
            messagebox.showerror("Error!", "Please enter an integer!")


        
root = Tk()
Searching(root,'Linear Search')
root.mainloop()