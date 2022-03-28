def splithalf(s):
    length = len(s)
    half = length // 2   
    extra = 0
    if length % 2 :
        extra = 1

    left = s[:half + extra]
    right = s[half + extra:]

    return right + left 

variable = input("Enter a string: ")
print(f"You enter {variable}")
print(splithalf(variable))