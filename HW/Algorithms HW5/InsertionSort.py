def insertion_sort(arr):
    size = len(arr)

    for i in range(1, size):
        key = arr[i]
        j = i-1

        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j=j-1

        arr[j+1] = key 

            
    return arr


test = [1,3,4,7,2,8,99,1,3]
print(insertion_sort(test))