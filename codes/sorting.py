def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]

    return arr
nums = [10,5,6,2,7,14,16]
print(bubble_sort(nums))