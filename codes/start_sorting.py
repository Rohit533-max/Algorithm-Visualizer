from tkinter import *
import pygame
from threading import *
from sorting import algochooser
from random import sample,shuffle

class Sorting:
    def __init__(self,root):
        self.root = root

        #self.AlgoName = AlgoName

        #window size
        self.x,self.y= 1200,700
        self.root.geometry(f"{self.x}x{self.y}")
        self.root.title("Sorting Algorithm Visualizer")

        #sorting canvas size
        self.canvasX,self.canvasY = 800,700

        #left side information 
        self.Frame1X,self.Frame1Y = 400,700

        #starting size of array
        self.size = IntVar()
        self.size.set(10)

        #starting speed 
        self.speed = IntVar()
        self.speed.set(10)

        #graph_type 0 means bar graph and 1 means color graph
        self.graph_type = IntVar()
        self.graph_type.set(0)
        self.TYPE = self.graph_type.get()

        #starting point
        self.starting_point = 2

        #creating Frame in the left side
        self.Frame1 = Frame(root,width=self.Frame1X,height=self.Frame1Y,bg="light salmon")
        self.Frame1.pack(side="left")

        # Algorithm Information Table
        self.information = {'Bubble Sort': "Worst Case:O(n²)\nAverage Case:O(n²)\nBest Case:O(n)"}

        #algorithm names
        self.algorithms = ['Bubble sort']

        #canvas of the graph
        self.Frame2 = Frame(root,width=self.canvasX, height=self.canvasY,bg="purple")
        self.Frame2.pack(side="left")
        self.canva = Canvas(self.Frame2,width=self.canvasX,height=self.canvasY, bg="blue")
        self.canva.pack(side='left')

        #creating a drop down menu for algorithm selection
        self.algo_var = "insertion_sort"

        #label for showing the comparisons
        self.label_comparison = Label(self.Frame1,text="Number of comparison : 0", bg="light salmon", fg="yellow", font=("Arial",10))
        self.label_comparison.place(x = 1, y = 1)

        #creating a new array
        self.numbers = sample(range(20, self.canvasY-20),self.size.get())
        shuffle(self.numbers)
        self.rec_width = self.canvasX // self.size.get()

        for num in self.numbers:
            self.canva.create_rectangle(self.starting_point,self.canvasY - num, self.starting_point + self. rec_width,self.canvasY,fill = 'sandy brown')
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
            self.starting_point += self.rec_width
        #update the graph frame
        self.Frame2.update()

    def new_list(self):
        numbers = []
        self.label_comparison.configure(text="No. of comparisons: 0")

        #enter random numbers into new array
        self.numbers = sample(range(20,self.canvasY-20), self.size.get())

        if self.TYPE == 0:
            colortype = ['sandy brown'] * len(self.numbers)
        self.paint(colortype)

    def sort_list(self):
        self.label_comparison.configure(text = "Number of Comparisons : 0")
        startsort = Thread(target=algochooser, args=(self.numbers,self.paint,self.label_comparison,self.algo_var,self.TYPE,self.speed.get()))
        startsort.start()


root = Tk()
s = Sorting(root)
root.mainloop()