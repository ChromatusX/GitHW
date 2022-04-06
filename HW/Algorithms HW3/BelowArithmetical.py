def belowArith(nums):
    avg = 0
    mean = 0
    list = [ ] 
    
    for i in nums:
        avg = avg + i
    
    mean = avg / len(nums)
    
    
    for i in nums:
        if i < mean:
            list.append(i)

    return list 

#variable = input("Enter a string: ")
#print(f"You enter {variable}")

nums = [1,3,5,6,4,10,2,3]
print(belowArith(nums))

