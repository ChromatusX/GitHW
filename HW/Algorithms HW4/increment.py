def increment1(nums):
    nums.reverse()
    size = len(nums)
    i = 0
    nums[0] += 1
        
    while i < size:
        #print(i)
        #print(size)
        if i+1 == size and nums[i] == 10:
            nums.append(0)
            nums[i] =0
            nums[i+1] +=1   

        elif nums[i] == 10:
            nums[i] =0
            nums[i+1] +=1              

        i += 1

    nums.reverse()

    return nums

test1 = [0,9,9]   #[1,0,0]
test2 = [1,2,9]    #[1,3,0]
test3 = [9,9,9,9]    #[1,0,0,0,0]
test4 = [9]         #[1,0]
test5 = [0,0]     #[0,1]

print(increment1(test1))
print(increment1(test2))
print(increment1(test3))
print(increment1(test4))
print(increment1(test5))
 