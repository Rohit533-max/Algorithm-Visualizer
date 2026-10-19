import time
cmp = 0



def linear_search(nums,paint,label_comparision,lable_index,speed,searched_element):
    global cmp
    for i in range(len(nums)):
        colors = []
        cmp +=1
        index = -1
        if nums[i] == searched_element:
            for x in range(len(nums)):
                if x < i:
                    colors.append("red")
                elif x == i:
                    colors.append("green")
                else:
                    colors.append("antiquie white")

            paint(colors)
            label_comparision.configure(text = "No of comparisions: " +str(cmp))
            index = i
            break
        else:
            for x in range(len(nums)):
                if x <= i:
                    colors.append("red")
                else:
                    colors.append("antique white")

                paint(colors)
                label_comparision.configure(text = "No of comparisions: "+ str(cmp))
            time.sleep(1/speed)
    if index == -1:
        lable_index.configure(text = "Element not found")
    else:
        lable_index.configure(text = "Element " + str(nums[index]) + "found at index " + str(index + 1))

def binary_search(nums,paint,label_comarision,lable_index,speed,searched_element):
    global cmp
    colors = ['antique white'] * len(nums)
    left,right = 0, len(nums)-1
    nums.sort()
    paint(colors)
    while left <= right:
        mid = left + (right - left) // 2
        colors[mid] = "Yellow"
        time.sleep(1/speed)
        if nums[mid] == searched_element:
            cmp +=1
            colors[mid] == 'green'
            paint(colors)
            label_comarision.configure(text = "No of comparisions: "+ str(cmp))
            index = mid
            break

        elif nums[mid] < searched_element:
            left +=1
            cmp +=1

            for x in range(mid +1):
                colors[x] = "red"
            paint(colors)
            label_comarision.configure(text = "No of comparisions: "+ str(cmp))

        else:
            right = mid -1
            cmp +=1

            for x in range(mid, len(nums)):
                colors[x] = "red"
            paint(colors)
            label_comarision.configure(text = "No of comparisions: " + str(cmp))
        time.sleep(1/speed)

    if index == -1:
        lable_index.configure(text = "Element not found")
    else:
        lable_index.configure(text = "Element" + str(nums[index]) + "found at index" + str(index +1))