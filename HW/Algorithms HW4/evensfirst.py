def evenfirst(nums):
    even, odd = 0, len(nums)-1
    while even < odd :
        if nums[even] % 2 == 0:
            even += 1
        else :
            nums[even], nums[odd] = nums[odd], nums[even]
            odd -=1 
    
    return nums

test =  [7,3,5,6,4,10,3,2]

print(evenfirst(test))
