def bubble_sort(arr):
    size = len(arr)

    for i in range(size):
        for j in range(size - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr


test = [1,3,4,7,2,8,99,1,3]
print(bubble_sort(test))