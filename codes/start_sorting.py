from tkinter import *
import pygame

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

        #canvas of the graph
        self.Frame2 = Frame(root,width=self.canvasX, height=self.canvasY,bg="purple")
        self.Frame2.pack(side="left")

root = Tk()
s = Sorting(root)
root.mainloop()