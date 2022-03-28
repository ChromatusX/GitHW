def unique(s):
    setstring = set(s)
    #print(setstring)
    #print(s)
    if len(setstring) == len(s) :
        return True
    else :
        return False 


variable = input("Enter a string:")
print(f"You enter {variable}")
print(unique(variable))