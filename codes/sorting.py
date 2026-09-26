import time
TYPE = 0
cmp = 0

def algochooser(numbers,paint, lable_comparison,something,TYPE_OF_DRAW,speed):
    global cmp, TYPE
    TYPE = TYPE_OF_DRAW
    #if something == "bubble_sort":
    lable_comparison.configure(text = "Number of comparisons")
    insertion_sort(numbers,paint,lable_comparison,speed)
    if TYPE == 0:
        paint(["lawn green"] * len(numbers))

    cmp = 0



def bubble_sort(numbers,paint,label_comparison,speed):
    global cmp, TYPE
    colors = []
    for i in range(len(numbers)):
        is_swapped = False
        for j in range(0,len(numbers)-1-i):
            if numbers[j] > numbers[j+1]:
                is_swapped = True
                numbers[j],numbers[j+1]= numbers[j+1],numbers[j]

                time.sleep(1/speed)
            cmp +=1
            if TYPE == 0:
                colors = ["#cc0000" if x == numbers[j] or x == numbers[j+1] else "antique white" for x in numbers]

            paint(colors)
            label_comparison.configure(text="No. of comparisons: " + str(cmp))

        #nothing swapped list is already sorted
        if not is_swapped:
            break
        time.sleep(1/speed)

def insertion_sort(numbers,paint,label_comparison,speed):
    global cmp, TYPE

    for i in range(1,len(numbers)):
        key = numbers[i]
        j = i -1
        while j >=0 and numbers[j] > key:
            numbers[j+1] = numbers[j]
            j-=1
            cmp +=1
        if TYPE == 0:
            colors = ["#cc0000" if x == key else "antique white" for x in numbers]
        numbers[j + 1] = key
        paint(colors)
        label_comparison.configure(text = "Number of comparisons: "+ str(cmp))
        time.sleep(1/speed)



