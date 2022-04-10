def selection_sort(arr):
    for i in range (len(arr)):
        min = i 

        for x in range(i+1, len(arr)):
            if arr[min] < arr[x]:
                min = x 

        arr[i], arr[min] = arr[min], arr[i]
            
    return arr


test = [1,3,4,7,2,8,99,1,3]
print(selection_sort(test))