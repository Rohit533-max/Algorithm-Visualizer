from tkinter import *
import pygame
from threading import *
from sorting import algochooser
from random import sample,shuffle

class Sorting:
    def __init__(self,root,AlgonameVar):
        self.root = root

        #self.AlgoName = AlgoName
        self.AlgonameVar = AlgonameVar
        
        #window size
        width = 1200
        height = 700
        self.root.title("Sorting Algorithm Visualizer")

        #screen size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        #calculate the center position
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        #set the window size and position
        root.geometry(f"{width}x{height}+{x}+{y}")
        #sorting canvas size
        self.canvasX,self.canvasY = 800,700

        #left side information 
        self.Frame1X,self.Frame1Y = 400,700

        #starting size of array
        self.size = IntVar()
        self.size.set(15)

        #starting speed 
        self.speed = IntVar()
        self.speed.set(10)

        #graph_type 
        self.graph_type = IntVar()


        #starting point
        self.starting_point = 2

        #creating Frame in the left side
        self.Frame1 = Frame(root,width=self.Frame1X,height=self.Frame1Y,bg="light salmon")
        self.Frame1.pack(side="left")

        # Algorithm Information Table
        self.information = {'Bubble Sort': "Worst Case:O(n²)\nAverage Case:O(n²)\nBest Case:O(n)",
                            'Selection Sort': "Worst Case:O(n²)\nAverage Case:O(n²)\nBest Case:O(n²)",
                            'Merge Sort': "Worst Case:O(n*log n)\nAverage Case:O(n*log n)\nBest Case:O(n*log n)",
                            'Heap Sort': "Worst Case:O(n*log n)\nAverage Case:O(n*log n)\nBest Case:O(n*log n)",
                            'Insertion Sort': "Worst Case:O(n²)\nAverage Case:O(n²)\nBest Case:O(n)",
                            'Quick Sort': "Worst Case:O(n²)\nAverage Case:O(n*log n)\nBest Case:O(n*log n)",
                            'Shell Sort': "Worst Case:O(n²)\nAverage Case:O(n²)\nBest Case:O(n*log n)",
                            'Radix Sort': "Worst Case:O(k*(n+b))\nAverage Case:O(k*(n+b))\nBest Case:O(k*(n+b))"}



        #algorithm names
        self.algorithm = ['Bubble sort',"Selection sort", "Insertion sort", "Merger sort", "Quick sort"]

        #canvas of the graph
        self.Frame2 = Frame(root,width=self.canvasX, height=self.canvasY,bg="purple")
        self.Frame2.pack(side="left")
        self.canva = Canvas(self.Frame2,width=self.canvasX,height=self.canvasY, bg="blue")
        self.canva.pack(side='left')

        #label for showing the comparisons
        self.label_comparison = Label(self.Frame1,text="Number of comparison : 0", bg="light salmon", fg="yellow", font=("Arial",10))
        self.label_comparison.place(x = 1, y = 1)

        #creating a new array
        self.numbers = sample(range(20, self.canvasY-20),self.size.get())
        shuffle(self.numbers)
        self.rec_width = self.canvasX // self.size.get()

        for num in self.numbers:
            self.canva.create_rectangle(self.starting_point,self.canvasY - num, self.starting_point + self. rec_width,self.canvasY,fill = 'sandy brown')
            self.label_value = Label(self.canva, text = num, bg="sandy brown", fg="white")
            self.canva.create_window(self.starting_point + 16, self.canvasY - num + 12, window=self.label_value)
            self.starting_point += self.rec_width
        #creating a sort button
        self.sort_button = Button(self.Frame1, text="Sort", command= self.sort_list, bg="royal blue", fg="white", padx=2, pady=2)
        self.sort_button.place(x=20,y=22)

    def paint(self,colortype):
        #delete the previous charts
        self.canva.delete("all")

        self.starting_point = 2

        #width of each bar
        self.rec_width = self.canvasX / self.size.get()

        #bar graph implementation

        for i in range(len(self.numbers)):
            self.canva.create_rectangle(
                self.starting_point,self.canvasY - self.numbers[i], self.starting_point + self.rec_width, self.canvasY, fill=colortype[i]
            )
            self.label_value = Label(self.canva, text=self.numbers[i], bg="sandy brown")
            self.canva.create_window(self.starting_point + 16, self.canvasY - self.numbers[i] +12, window=self.label_value)
            self.starting_point += self.rec_width
        #update the graph frame
        self.Frame2.update()

    def new_list(self):
        numbers = []
        self.label_comparison.configure(text="No. of comparisons: 0")

        #enter random numbers into new array
        self.numbers = sample(range(20,self.canvasY-20), self.size.get())

       
        colortype = ['sandy brown'] * len(self.numbers)
        self.paint(colortype)

    def sort_list(self):
        self.label_comparison.configure(text = "Number of Comparisons : 0")
        startsort = Thread(target=algochooser, args=(self.numbers,self.paint,self.label_comparison,self.AlgonameVar,self.speed.get()))
        startsort.start()

