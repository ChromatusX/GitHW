
def max_num(value1, value2 , value3):
    if(value1 > value2 and value1 > value3):
        print(f"The biggest value is {value1}")

    elif (value2 > value1 and value2 > value3):
        print(f"The biggest value is {value2}")

    else:
        print(f"The biggest value is {value3}")


value1, value2 , value3 = input("Enter 3 numbers: ").split()

print(value1, value2, value3 )
max_num(value1,value2,value3)