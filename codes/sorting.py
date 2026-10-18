import time
TYPE = 0
cmp = 0

def algochooser(numbers,paint, label_comparison,something,speed):
    global cmp, TYPE

    if something == "Bubble Sort":
        label_comparison.configure(text = "No. of comparisons:0")
        bubble_sort(numbers,paint,label_comparison,speed)
        paint(['lawn green']*len(numbers))
        cmp = 0

    elif something == "Selection Sort":
        label_comparison.configure(text = "No of comparisions: 0")
        selection_sort(numbers,paint,label_comparison,speed)
        paint(['lawn green']* len(numbers))
        cmp = 0

    elif something == "Insertion Sort":
        label_comparison(text = "No of comparisions: 0")
        insertion_sort(numbers,paint,label_comparison,speed)
        paint(['lawn green']*len(numbers))
        cmp = 0

    elif something == "Merge Sort":
        label_comparison.configure(text = "No. of comparisons:0")
        mergesort(numbers,0,len(numbers)-1,paint,label_comparison,speed)
        paint(['lawn green'] *len(numbers))
        cmp = 0

    elif something == "Quick Sort":
        label_comparison.configure(text = "No of comparisions: 0")
        quicksort(numbers,0,len(numbers) -1,paint,label_comparison,speed)
        paint(['lawn green'] * len(numbers))
        cmp = 0


def bubble_sort(numbers,paint,label_comparison,speed):
    global cmp
    colors = []
    for i in range(len(numbers)):
        is_swapped = False
        for j in range(0,len(numbers)-1-i):
            if numbers[j] > numbers[j+1]:
                is_swapped = True
                numbers[j],numbers[j+1]= numbers[j+1],numbers[j]

                time.sleep(1/speed)
            cmp +=1
            
            colors = ["#cc0000" if x == numbers[j] or x == numbers[j+1] else "antique white" for x in numbers]

            paint(colors)
            label_comparison.configure(text="No. of comparisons: " + str(cmp))

        #nothing swapped list is already sorted
        if not is_swapped:
            break
        time.sleep(1/speed)

def insertion_sort(numbers,paint,label_comparison,speed):
    global cmp

    for i in range(1,len(numbers)):
        key = numbers[i]
        j = i -1
        while j >=0 and numbers[j] > key:
            numbers[j+1] = numbers[j]
            j-=1
            cmp +=1
        
        colors = ["#cc0000" if x == key else "antique white" for x in numbers]
        numbers[j + 1] = key
        paint(colors)
        label_comparison.configure(text = "Number of comparisons: "+ str(cmp))
        time.sleep(1/speed)

def selection_sort(numbers,paint,label_comparison,speed):
    global cmp
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            cmp +=1
            if numbers[j] < numbers[min_index]:
                min_index = j
                colors = ["#cc0000" if x == min_index else "antique white" for x in range(len(numbers))]
                paint(colors)
                label_comparison.configure(text = "Number of comparisons: "+str(cmp))
                time.sleep(1/speed)

        #swap the min_index to its correct position
        numbers[i],numbers[min_index] = numbers[min_index],numbers[i]

def mergesort(number, left, right, paint, label_comparison, speed):
    if left >= right:
        return

    middle = (left + right) // 2

    mergesort(number, left, middle, paint, label_comparison, speed)
    mergesort(number, middle + 1, right, paint, label_comparison, speed)

    merge(number, left, middle, right, paint, label_comparison, speed)


def merge(number, left, middle, right, paint, label_comparison, speed):
    global cmp

    first = number[left:middle + 1]
    second = number[middle + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(first) and j < len(second):

        # Compare two elements
        cmp += 1

        if first[i] <= second[j]:
            number[k] = first[i]
            i += 1
        else:
            number[k] = second[j]
            j += 1

        k += 1

        # Show current merge
        colors = ["antique white"] * len(number)

        for x in range(left, middle + 1):
            colors[x] = "teal"

        for x in range(middle + 1, right + 1):
            colors[x] = "yellow"

        paint(colors)

        label_comparison.configure(
            text="No. of comparisons: " + str(cmp)
        )

        time.sleep(1 / speed)

    # Remaining elements
    while i < len(first):
        number[k] = first[i]
        i += 1
        k += 1

    while j < len(second):
        number[k] = second[j]
        j += 1
        k += 1

    # Show the completed merged section
    colors = ["antique white"] * len(number)

    for x in range(left, right + 1):
        colors[x] = "green"

    paint(colors)
    time.sleep(1 / speed)

def quicksort(number,start,end,paint,label_comparison,speed):
    if start < end:
        pivotIdx = partition(number,start,end,paint,label_comparison,speed)
        quicksort(number,start,pivotIdx-1,paint,label_comparison,speed)
        quicksort(number,pivotIdx+1,end,paint,label_comparison,speed)


def partition(number,start,end,paint,label_comparison,speed):
    global cmp 
    pivot = number[end]
    i = start -1
    color = []

    for val in range(len(number)):
        if val == start or val == end -1:
            color.append("#cc0000")
        elif val == end:
            color.append("yellow")
        else:
            color.append("antique white")

    paint(color)
    for j in range(start,end):
        if number[j] <= pivot:
            i+=1
            number[i],number[j] = number[j],number[i]
        time.sleep(1/speed)
        cmp +=1
        color =[]

        for c in range(len(number)):
            if c == start or c == end -1:
                color.append("#cc0000")
            elif c == end:
                color.append("yellow")
            else:
                color.append("antique white")


        paint(color)
        label_comparison.configure(text="No. of comparisons: " + str(cmp))

    #placing the pivot to right index
    i+=1
    number[i],number[end] = number[end],number[i]
    label_comparison.configure(text="No. of comparisons: " + str(cmp))

    return i