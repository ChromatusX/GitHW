def merge_sort(arr):
    size = len(arr)
    if size > 1:
        middle = size // 2 

        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        x=0
        y=0
        z=0

        leftsize = len(left)
        rightsize = len(right)

        while x < leftsize and y < rightsize :

            if left[x] >= right[y] :
                arr[z] = left[x]
                x +=1 
            else:
                arr[z] = right[y]
                y +=1
            z += 1

        while x < leftsize :
            arr[z] = left[x]
            x += 1
            z += 1
        
        while y < rightsize :
            arr[z] = right[y]
            y += 1
            z += 1
    
            
    return arr


test = [1,3,4,7,2,8,99,1,3]
print(merge_sort(test))