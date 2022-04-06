def increment1(nums):
    result = [ ]
    size = len(nums)

    third = nums[size-1]
    second = nums[size-2]
    first = nums[size-3]

    third  += 1
    if(third != 10) : 
        result.append(first)
        result.append(second)
        result.append(third)
    else :
        third = 0
        second += 1
        if(second != 10) :
            result.append(first)
            result.append(second)
            result.append(third)

        else:
            second = 0
            
            first += 1
            if first == 10:
                first = 0
                result.append(1)
                result.append(first)
                result.append(second)
                result.append(third)
               
            else:
                result.append(first)
                result.append(second)
                result.append(third)

    return result

test1 = [0,9,9]
test2 = [1,2,9]
test3 = [1,2,3,4]
print(increment1(test1))
print(increment1(test2))
print(increment1(test3))

 